"""Optional ASR adapter for timestamp discovery from public audio sources."""

from collections.abc import Iterable
from pathlib import Path
from typing import Annotated, Protocol

from pydantic import BaseModel, ConfigDict, Field, model_validator

Millis = Annotated[int, Field(ge=0)]
Probability = Annotated[float, Field(ge=0.0, le=1.0)]


class _AcquisitionModel(BaseModel):
    model_config = ConfigDict(extra="forbid", frozen=True)


class _RawSegment(Protocol):
    start: float
    end: float
    text: str


class TranscriptSegment(_AcquisitionModel):
    """Machine-produced transcript segment used only as a source locator candidate."""

    index: int = Field(ge=0)
    start_ms: Millis
    end_ms: Millis
    text: str = Field(min_length=1)

    @model_validator(mode="after")
    def _validate_range(self) -> "TranscriptSegment":
        if self.end_ms < self.start_ms:
            raise ValueError("end_ms must not precede start_ms")
        return self


class AsrTranscript(_AcquisitionModel):
    """Machine transcript metadata plus timestamped segments.

    This is an acquisition artifact, not a verified EvidenceAssertion.
    """

    model_name: str = Field(min_length=1)
    language: str | None = None
    language_probability: Probability | None = None
    segments: tuple[TranscriptSegment, ...]


def normalize_segments(segments: Iterable[_RawSegment]) -> tuple[TranscriptSegment, ...]:
    """Normalize faster-whisper-like segments into durable millisecond locators."""

    normalized: list[TranscriptSegment] = []
    for segment in segments:
        text = segment.text.strip()
        if not text:
            continue

        normalized.append(
            TranscriptSegment(
                index=len(normalized),
                start_ms=round(segment.start * 1_000),
                end_ms=round(segment.end * 1_000),
                text=text,
            )
        )

    return tuple(normalized)


def transcribe_audio(
    audio_path: str | Path,
    *,
    model_name: str = "small.en",
    device: str = "cpu",
    compute_type: str = "int8",
    language: str | None = "en",
    beam_size: int = 5,
    vad_filter: bool = True,
) -> AsrTranscript:
    """Transcribe local audio with the optional faster-whisper dependency."""

    try:
        from faster_whisper import WhisperModel
    except ImportError as exc:
        raise RuntimeError(
            'ASR support is optional; install with: pip install -e ".[asr]"'
        ) from exc

    model = WhisperModel(
        model_name,
        device=device,
        compute_type=compute_type,
    )
    raw_segments, info = model.transcribe(
        str(audio_path),
        language=language,
        beam_size=beam_size,
        vad_filter=vad_filter,
    )
    normalized = normalize_segments(raw_segments)

    detected_language = getattr(info, "language", language)
    detected_probability = getattr(info, "language_probability", None)

    return AsrTranscript(
        model_name=model_name,
        language=detected_language,
        language_probability=detected_probability,
        segments=normalized,
    )
