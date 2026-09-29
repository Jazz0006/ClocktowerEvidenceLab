"""C2B batch acquisition planning and external work-directory execution."""

from collections.abc import Callable
from enum import StrEnum
from hashlib import sha256
from pathlib import Path
from typing import Annotated, BinaryIO
from urllib.parse import urlparse
from urllib.request import urlopen

from pydantic import BaseModel, ConfigDict, Field

from clocktower_evidence_lab.acquisition import asr
from clocktower_evidence_lab.acquisition.podcast_manifest import (
    AcquisitionState,
    AsrState,
    PodcastEpisodeManifest,
    PodcastManifestEntry,
    active_acquisition_queue,
)

RelativePath = Annotated[str, Field(min_length=1, max_length=1_024)]
Sha256Text = Annotated[str, Field(pattern=r"^[0-9a-f]{64}$")]


class _BatchModel(BaseModel):
    model_config = ConfigDict(extra="forbid", frozen=True)


class BatchAcquisitionMode(StrEnum):
    """How one pending episode should enter the local acquisition work directory."""

    ADVERTISED_TRANSCRIPT = "ADVERTISED_TRANSCRIPT"
    AUDIO_ASR = "AUDIO_ASR"
    BLOCKED = "BLOCKED"


class BatchBlockReason(StrEnum):
    """Why an in-scope pending episode cannot currently be acquired."""

    MISSING_SOURCE_LOCATOR = "MISSING_SOURCE_LOCATOR"


class BatchPlanItem(_BatchModel):
    source_id: str = Field(min_length=1, max_length=512)
    mode: BatchAcquisitionMode
    locator: str | None = Field(default=None, max_length=2_048)
    payload_relative_path: RelativePath | None = None
    asr_relative_path: RelativePath | None = None
    block_reason: BatchBlockReason | None = None


class BatchPlan(_BatchModel):
    items: tuple[BatchPlanItem, ...]


class PayloadAcquisitionResult(_BatchModel):
    source_id: str = Field(min_length=1, max_length=512)
    payload_relative_path: RelativePath
    payload_sha256: Sha256Text
    payload_bytes: int = Field(ge=0)
    skipped_existing: bool


class BatchProgress(_BatchModel):
    """Git-safe progress metadata; full media/transcript bodies remain external."""

    source_id: str = Field(min_length=1, max_length=512)
    acquisition_state: AcquisitionState = AcquisitionState.NOT_ATTEMPTED
    asr_state: AsrState = AsrState.NOT_ATTEMPTED
    payload_relative_path: RelativePath | None = None
    payload_sha256: Sha256Text | None = None
    payload_bytes: int | None = Field(default=None, ge=0)
    asr_relative_path: RelativePath | None = None
    asr_model: str | None = Field(default=None, min_length=1, max_length=512)
    asr_segment_count: int | None = Field(default=None, ge=0)


def build_batch_plan(manifest: PodcastEpisodeManifest) -> BatchPlan:
    """Plan acquisition only for current-scope episodes not already acquired."""

    return BatchPlan(\n        items=tuple(_plan_entry(entry) for entry in active_acquisition_queue(manifest))\n    )


def _plan_entry(entry: PodcastManifestEntry) -> BatchPlanItem:
    source_key = entry.source_id.split(":", 1)[-1]
    root = f"episodes/{source_key}"

    if entry.transcript_urls:
        locator = entry.transcript_urls[0]
        extension = _locator_extension(locator, default=".transcript")
        return BatchPlanItem(
            source_id=entry.source_id,
            mode=BatchAcquisitionMode.ADVERTISED_TRANSCRIPT,
            locator=locator,
            payload_relative_path=f"{root}/source{extension}",
        )

    if entry.audio_url:
        extension = _locator_extension(entry.audio_url, default=".audio")
        return BatchPlanItem(
            source_id=entry.source_id,
            mode=BatchAcquisitionMode.AUDIO_ASR,
            locator=entry.audio_url,
            payload_relative_path=f"{root}/source{extension}",
            asr_relative_path=f"{root}/asr.json",
        )

    return BatchPlanItem(
        source_id=entry.source_id,
        mode=BatchAcquisitionMode.BLOCKED,
        block_reason=BatchBlockReason.MISSING_SOURCE_LOCATOR,
    )


def _locator_extension(locator: str, *, default: str) -> str:
    suffix = Path(urlparse(locator).path).suffix
    if not suffix or len(suffix) > 16:
        return default
    return suffix.lower()


def acquire_payload(
    item: BatchPlanItem,
    work_dir: str | Path,
    *,
    opener: Callable[..., BinaryIO] = urlopen,
    timeout_seconds: float = 30.0,
    chunk_size: int = 1024 * 1024,
) -> PayloadAcquisitionResult:
    """Stream one public payload into the external work directory and reuse it if present."""

    if item.mode is BatchAcquisitionMode.BLOCKED or item.locator is None:
        raise ValueError("blocked batch item has no acquirable locator")
    if item.payload_relative_path is None:
        raise ValueError("batch item is missing payload_relative_path")
    if chunk_size <= 0:
        raise ValueError("chunk_size must be positive")

    target = Path(work_dir) / item.payload_relative_path
    target.parent.mkdir(parents=True, exist_ok=True)

    if target.exists():
        digest, size = _hash_file(target, chunk_size=chunk_size)
        return PayloadAcquisitionResult(
            source_id=item.source_id,
            payload_relative_path=item.payload_relative_path,
            payload_sha256=digest,
            payload_bytes=size,
            skipped_existing=True,
        )

    temporary = target.with_name(target.name + ".part")
    hasher = sha256()
    size = 0
    try:
        with opener(item.locator, timeout=timeout_seconds) as response:
            with temporary.open("wb") as output:
                while chunk := response.read(chunk_size):
                    output.write(chunk)
                    hasher.update(chunk)
                    size += len(chunk)
        temporary.replace(target)
    finally:
        if temporary.exists() and not target.exists():
            temporary.unlink()

    return PayloadAcquisitionResult(
        source_id=item.source_id,
        payload_relative_path=item.payload_relative_path,
        payload_sha256=hasher.hexdigest(),
        payload_bytes=size,
        skipped_existing=False,
    )


def run_audio_asr(
    item: BatchPlanItem,
    work_dir: str | Path,
    *,
    transcriber: Callable[..., asr.AsrTranscript] = asr.transcribe_audio,
    model_name: str = "small.en",
    device: str = "cpu",
    compute_type: str = "int8",
    language: str | None = "en",
) -> BatchProgress:
    """Run ASR for an acquired audio item and keep full transcript JSON outside Git."""

    if item.mode is not BatchAcquisitionMode.AUDIO_ASR:
        raise ValueError("ASR is only valid for AUDIO_ASR batch items")
    if item.payload_relative_path is None or item.asr_relative_path is None:
        raise ValueError("audio ASR item is missing required work-directory paths")

    work_root = Path(work_dir)
    audio_path = work_root / item.payload_relative_path
    if not audio_path.is_file():
        raise FileNotFoundError(audio_path)

    transcript = transcriber(
        audio_path,
        model_name=model_name,
        device=device,
        compute_type=compute_type,
        language=language,
    )

    asr_path = work_root / item.asr_relative_path
    asr_path.parent.mkdir(parents=True, exist_ok=True)
    asr_path.write_text(transcript.model_dump_json(indent=2) + "\n", encoding="utf-8")

    payload_sha256, payload_bytes = _hash_file(audio_path)
    return BatchProgress(
        source_id=item.source_id,
        acquisition_state=AcquisitionState.COMPLETE,
        asr_state=AsrState.COMPLETE,
        payload_relative_path=item.payload_relative_path,
        payload_sha256=payload_sha256,
        payload_bytes=payload_bytes,
        asr_relative_path=item.asr_relative_path,
        asr_model=transcript.model_name,
        asr_segment_count=len(transcript.segments),
    )


def apply_batch_progress(
    manifest: PodcastEpisodeManifest,
    progress_items: tuple[BatchProgress, ...],
) -> PodcastEpisodeManifest:
    """Apply machine workflow progress without changing extraction or human-review state."""

    progress_by_source_id = {progress.source_id: progress for progress in progress_items}
    updated_entries = []
    for entry in manifest.episodes:
        progress = progress_by_source_id.get(entry.source_id)
        if progress is None:
            updated_entries.append(entry)
            continue
        updated_entries.append(
            entry.model_copy(
                update={
                    "acquisition_state": progress.acquisition_state,
                    "asr_state": progress.asr_state,
                }
            )
        )

    return manifest.model_copy(update={"episodes": tuple(updated_entries)})


def _hash_file(path: Path, *, chunk_size: int = 1024 * 1024) -> tuple[str, int]:
    hasher = sha256()
    size = 0
    with path.open("rb") as source:
        while chunk := source.read(chunk_size):
            hasher.update(chunk)
            size += len(chunk)
    return hasher.hexdigest(), size
