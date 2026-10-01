"""Temporary full-transcript workspace for machine-first podcast semantic review."""

from __future__ import annotations

import shutil
from pathlib import Path
from typing import Annotated, TextIO

from pydantic import BaseModel, ConfigDict, Field

from clocktower_evidence_lab.acquisition.asr import AsrTranscript
from clocktower_evidence_lab.acquisition.c2_podcast import CULT_OF_CLOCKTOWER_FEED_URL
from clocktower_evidence_lab.acquisition.podcast import PodcastEpisode, parse_podcast_rss
from clocktower_evidence_lab.acquisition.podcast_batch import (
    BatchProgress,
    apply_batch_progress,
    build_batch_plan,
    run_batch_plan,
)
from clocktower_evidence_lab.acquisition.podcast_manifest import (
    build_episode_manifest,
    stable_episode_id,
)
from clocktower_evidence_lab.acquisition.podcast_probe import fetch_rss

ShortText = Annotated[str, Field(min_length=1, max_length=512)]
SESSION_MARKER_FILENAME = ".semantic-review-session.json"
BATCH_PROGRESS_FILENAME = "batch-progress.json"
UPDATED_MANIFEST_FILENAME = "manifest.updated.json"


class _SemanticModel(BaseModel):
    model_config = ConfigDict(extra="forbid", frozen=True)


class SemanticReviewSession(_SemanticModel):
    """Marker proving a directory belongs to the bounded semantic-review workflow."""

    schema_version: str = "c2-semantic-review-session-v1"
    guid: ShortText
    source_id: ShortText
    episode_title: ShortText


def prepare_semantic_session(
    *,
    guid: str,
    work_dir: str | Path,
    feed_url: str = CULT_OF_CLOCKTOWER_FEED_URL,
    timeout_seconds: float = 30.0,
) -> SemanticReviewSession:
    """Acquire one episode and full ASR into a marked temporary directory.

    This intentionally rebuilds a one-episode manifest without retained prior-processing
    state so a previously processed episode may be re-transcribed for a semantic benchmark.
    """

    root = _safe_workspace_root(work_dir)
    existing = _read_marker_if_present(root)
    if existing is not None:
        if existing.guid != guid:
            raise ValueError("semantic workspace belongs to a different episode")
        return _resume_semantic_session(existing, root)

    if root.exists() and any(root.iterdir()):
        raise ValueError("semantic workspace must be empty unless it has a valid marker")

    rss = fetch_rss(feed_url, timeout_seconds=timeout_seconds)
    episodes = parse_podcast_rss(rss, feed_url=feed_url)
    episode = _select_episode(episodes, guid=guid)
    session = SemanticReviewSession(
        guid=guid,
        source_id=stable_episode_id(episode),
        episode_title=episode.title,
    )

    root.mkdir(parents=True, exist_ok=True)
    _marker_path(root).write_text(session.model_dump_json(indent=2) + "\n", encoding="utf-8")
    return _run_session_acquisition(session, episode, root)


def render_semantic_transcript(
    *,
    work_dir: str | Path,
    output: TextIO,
) -> SemanticReviewSession:
    """Render the complete timestamped ASR transcript without creating another copy."""

    root = _safe_workspace_root(work_dir)
    session = _read_required_marker(root)
    progress = _read_single_progress(root, expected_source_id=session.source_id)
    if progress.asr_relative_path is None:
        raise ValueError("semantic session has no ASR transcript path")

    transcript_path = root / progress.asr_relative_path
    transcript = AsrTranscript.model_validate_json(transcript_path.read_text(encoding="utf-8"))

    output.write(
        f"# source_id={session.source_id} guid={session.guid} "
        f"model={transcript.model_name} segments={len(transcript.segments)}\n"
    )
    for segment in transcript.segments:
        output.write(
            f"{_format_ms(segment.start_ms)}-{_format_ms(segment.end_ms)}\t{segment.text}\n"
        )
    return session


def cleanup_semantic_session(*, work_dir: str | Path) -> SemanticReviewSession:
    """Delete only a marked semantic-review workspace, including audio and ASR."""

    root = _safe_workspace_root(work_dir)
    session = _read_required_marker(root)
    shutil.rmtree(root)
    return session


def _resume_semantic_session(
    session: SemanticReviewSession,
    root: Path,
) -> SemanticReviewSession:
    progress_path = root / BATCH_PROGRESS_FILENAME
    if progress_path.is_file():
        progress = _read_single_progress(root, expected_source_id=session.source_id)
        if progress.asr_relative_path is not None and (root / progress.asr_relative_path).is_file():
            return session

    rss = fetch_rss(CULT_OF_CLOCKTOWER_FEED_URL)
    episodes = parse_podcast_rss(rss, feed_url=CULT_OF_CLOCKTOWER_FEED_URL)
    episode = _select_episode(episodes, guid=session.guid)
    if stable_episode_id(episode) != session.source_id:
        raise ValueError("semantic session source identity no longer matches live RSS")
    return _run_session_acquisition(session, episode, root)


def _run_session_acquisition(
    session: SemanticReviewSession,
    episode: PodcastEpisode,
    root: Path,
) -> SemanticReviewSession:
    manifest = build_episode_manifest((episode,))
    result = run_batch_plan(build_batch_plan(manifest), root)
    if result.blocked_items or len(result.progress) != 1:
        raise RuntimeError("semantic acquisition did not complete exactly one episode")

    updated_manifest = apply_batch_progress(manifest, result.progress)
    (root / BATCH_PROGRESS_FILENAME).write_text(
        result.model_dump_json(indent=2) + "\n",
        encoding="utf-8",
    )
    (root / UPDATED_MANIFEST_FILENAME).write_text(
        updated_manifest.model_dump_json(indent=2) + "\n",
        encoding="utf-8",
    )
    _read_single_progress(root, expected_source_id=session.source_id)
    return session


def _select_episode(
    episodes: tuple[PodcastEpisode, ...],
    *,
    guid: str,
) -> PodcastEpisode:
    matches = tuple(episode for episode in episodes if episode.guid == guid)
    if len(matches) != 1:
        raise ValueError(f"expected exactly one RSS episode for GUID {guid!r}")
    return matches[0]


def _read_single_progress(root: Path, *, expected_source_id: str) -> BatchProgress:
    from clocktower_evidence_lab.acquisition.podcast_batch import BatchRunResult

    result = BatchRunResult.model_validate_json(
        (root / BATCH_PROGRESS_FILENAME).read_text(encoding="utf-8")
    )
    if len(result.progress) != 1:
        raise ValueError("semantic session progress must contain exactly one episode")
    progress = result.progress[0]
    if progress.source_id != expected_source_id:
        raise ValueError("semantic session progress source_id does not match marker")
    return progress


def _safe_workspace_root(work_dir: str | Path) -> Path:
    root = Path(work_dir).expanduser().resolve()
    forbidden = {Path("/").resolve(), Path.home().resolve()}
    if root in forbidden:
        raise ValueError("refusing unsafe semantic workspace root")
    if len(root.parts) < 4:
        raise ValueError("semantic workspace root is too broad")
    return root


def _marker_path(root: Path) -> Path:
    return root / SESSION_MARKER_FILENAME


def _read_marker_if_present(root: Path) -> SemanticReviewSession | None:
    marker = _marker_path(root)
    if not marker.is_file():
        return None
    return SemanticReviewSession.model_validate_json(marker.read_text(encoding="utf-8"))


def _read_required_marker(root: Path) -> SemanticReviewSession:
    session = _read_marker_if_present(root)
    if session is None:
        raise ValueError("semantic workspace is missing its session marker")
    return session


def _format_ms(value: int) -> str:
    total_seconds, milliseconds = divmod(value, 1_000)
    hours, remainder = divmod(total_seconds, 3_600)
    minutes, seconds = divmod(remainder, 60)
    return f"{hours:02d}:{minutes:02d}:{seconds:02d}.{milliseconds:03d}"
