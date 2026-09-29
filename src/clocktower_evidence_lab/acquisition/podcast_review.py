"""C2D deterministic review-packet ranking over lightweight machine candidates."""

from enum import StrEnum
from typing import Annotated

from pydantic import BaseModel, ConfigDict, Field, model_validator

from clocktower_evidence_lab.acquisition.podcast_candidates import (
    CandidateArtifact,
    CandidateCategory,
    MachineCandidate,
)
from clocktower_evidence_lab.acquisition.podcast_manifest import HumanReviewState

Millis = Annotated[int, Field(ge=0)]
Probability = Annotated[float, Field(ge=0.0, le=1.0)]
ShortText = Annotated[str, Field(min_length=1, max_length=512)]
TagText = Annotated[str, Field(min_length=1, max_length=128)]


class _ReviewModel(BaseModel):
    model_config = ConfigDict(extra="forbid", frozen=True)


class ReviewPriority(StrEnum):
    """Acquisition-review priority only; never a Storyteller decision-quality label."""

    P0 = "P0"
    P1 = "P1"
    P2 = "P2"


_PRIORITY_BY_CATEGORY: dict[CandidateCategory, ReviewPriority] = {
    CandidateCategory.STORYTELLER_RATIONALE: ReviewPriority.P0,
    CandidateCategory.SETUP_LEVEL_REASONING: ReviewPriority.P0,
    CandidateCategory.REGISTRATION_CHOICE: ReviewPriority.P0,
    CandidateCategory.DEMON_BLUFF_REASONING: ReviewPriority.P0,
    CandidateCategory.INFORMATION_STRENGTH: ReviewPriority.P0,
    CandidateCategory.EXPLICIT_ALTERNATIVE: ReviewPriority.P0,
    CandidateCategory.MISINFORMATION_POLICY: ReviewPriority.P1,
    CandidateCategory.PLAYER_AGENCY: ReviewPriority.P1,
    CandidateCategory.CONFIRMATION_CHAIN: ReviewPriority.P1,
    CandidateCategory.LONGITUDINAL_TRAJECTORY: ReviewPriority.P1,
    CandidateCategory.PLAYER_EXPERIENCE: ReviewPriority.P1,
    CandidateCategory.STORYTELLER_DECISION: ReviewPriority.P1,
    CandidateCategory.REAL_GAME_EXAMPLE: ReviewPriority.P2,
}
_PRIORITY_RANK = {
    ReviewPriority.P0: 0,
    ReviewPriority.P1: 1,
    ReviewPriority.P2: 2,
}
_CATEGORY_RANK = {category: index for index, category in enumerate(CandidateCategory)}


class ReviewWindow(_ReviewModel):
    """One bounded source-audio window selected for human primary-source review."""

    source_id: ShortText
    start_ms: Millis
    end_ms: Millis
    priority: ReviewPriority
    categories: tuple[CandidateCategory, ...]
    machine_summaries: tuple[ShortText, ...]
    tags: tuple[TagText, ...] = ()
    candidate_count: int = Field(ge=1)
    max_extraction_confidence: Probability | None = None

    @model_validator(mode="after")
    def _validate_range(self) -> "ReviewWindow":
        if self.end_ms < self.start_ms:
            raise ValueError("end_ms must not precede start_ms")
        return self


class ReviewPacket(_ReviewModel):
    """Lightweight C2D output describing where a human should listen first."""

    schema_version: str = "c2d-review-packet-v1"
    source_id: ShortText
    source_candidate_count: int = Field(ge=0)
    selected_candidate_count: int = Field(ge=0)
    total_review_ms: Millis
    human_review_state: HumanReviewState = HumanReviewState.NOT_STARTED
    windows: tuple[ReviewWindow, ...]


def build_review_packet(
    artifact: CandidateArtifact,
    *,
    merge_gap_ms: int = 5_000,
    max_windows: int = 12,
    max_review_ms: int = 600_000,
) -> ReviewPacket:
    """Merge, prioritize and budget machine candidates for bounded human review."""

    if merge_gap_ms < 0:
        raise ValueError("merge_gap_ms must be non-negative")
    if max_windows < 0:
        raise ValueError("max_windows must be non-negative")
    if max_review_ms < 0:
        raise ValueError("max_review_ms must be non-negative")

    merged = _merge_candidates(artifact, merge_gap_ms=merge_gap_ms)
    ranked = sorted(merged, key=_review_sort_key)

    selected: list[ReviewWindow] = []
    total_review_ms = 0
    for window in ranked:
        if len(selected) >= max_windows:
            break
        duration = window.end_ms - window.start_ms
        if total_review_ms + duration > max_review_ms:
            continue
        selected.append(window)
        total_review_ms += duration

    return ReviewPacket(
        source_id=artifact.source_id,
        source_candidate_count=len(artifact.candidates),
        selected_candidate_count=sum(window.candidate_count for window in selected),
        total_review_ms=total_review_ms,
        windows=tuple(selected),
    )


def _merge_candidates(
    artifact: CandidateArtifact,
    *,
    merge_gap_ms: int,
) -> tuple[ReviewWindow, ...]:
    ordered = sorted(
        artifact.candidates,
        key=lambda candidate: (candidate.start_ms, candidate.end_ms, candidate.category.value),
    )
    groups: list[list[MachineCandidate]] = []
    group_end = -1

    for candidate in ordered:
        if candidate.source_id != artifact.source_id:
            raise ValueError("candidate source_id does not match artifact source_id")
        if not groups or candidate.start_ms > group_end + merge_gap_ms:
            groups.append([candidate])
            group_end = candidate.end_ms
            continue
        groups[-1].append(candidate)
        group_end = max(group_end, candidate.end_ms)

    return tuple(_materialize_review_window(group) for group in groups)


def _materialize_review_window(candidates: list[MachineCandidate]) -> ReviewWindow:
    categories = tuple(
        sorted(
            {candidate.category for candidate in candidates},
            key=lambda category: _CATEGORY_RANK[category],
        )
    )
    summaries = tuple(dict.fromkeys(candidate.summary for candidate in candidates))
    tags = tuple(sorted({tag for candidate in candidates for tag in candidate.tags}))
    confidences = [
        candidate.extraction_confidence
        for candidate in candidates
        if candidate.extraction_confidence is not None
    ]
    priority = min(
        (_PRIORITY_BY_CATEGORY[category] for category in categories),
        key=lambda value: _PRIORITY_RANK[value],
    )

    return ReviewWindow(
        source_id=candidates[0].source_id,
        start_ms=min(candidate.start_ms for candidate in candidates),
        end_ms=max(candidate.end_ms for candidate in candidates),
        priority=priority,
        categories=categories,
        machine_summaries=summaries,
        tags=tags,
        candidate_count=len(candidates),
        max_extraction_confidence=max(confidences) if confidences else None,
    )


def _review_sort_key(window: ReviewWindow) -> tuple[int, int, float, int, int]:
    confidence = window.max_extraction_confidence
    return (
        _PRIORITY_RANK[window.priority],
        -len(window.categories),
        -(confidence if confidence is not None else -1.0),
        window.end_ms - window.start_ms,
        window.start_ms,
    )
