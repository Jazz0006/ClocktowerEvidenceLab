"""C2C lightweight timestamped machine-candidate artifacts."""

from collections.abc import Iterable
from enum import StrEnum
from typing import Annotated

from pydantic import BaseModel, ConfigDict, Field, model_validator

from clocktower_evidence_lab.acquisition.asr import TranscriptSegment
from clocktower_evidence_lab.acquisition.podcast_manifest import (
    ExtractionState,
    HumanReviewState,
)

Millis = Annotated[int, Field(ge=0)]
Probability = Annotated[float, Field(ge=0.0, le=1.0)]
ShortText = Annotated[str, Field(min_length=1, max_length=512)]
TagText = Annotated[str, Field(min_length=1, max_length=128)]


class _CandidateModel(BaseModel):
    model_config = ConfigDict(extra="forbid", frozen=True)


class CandidateCategory(StrEnum):
    STORYTELLER_DECISION = "STORYTELLER_DECISION"
    STORYTELLER_RATIONALE = "STORYTELLER_RATIONALE"
    SETUP_LEVEL_REASONING = "SETUP_LEVEL_REASONING"
    MISINFORMATION_POLICY = "MISINFORMATION_POLICY"
    REGISTRATION_CHOICE = "REGISTRATION_CHOICE"
    DEMON_BLUFF_REASONING = "DEMON_BLUFF_REASONING"
    PLAYER_EXPERIENCE = "PLAYER_EXPERIENCE"
    PLAYER_AGENCY = "PLAYER_AGENCY"
    INFORMATION_STRENGTH = "INFORMATION_STRENGTH"
    CONFIRMATION_CHAIN = "CONFIRMATION_CHAIN"
    LONGITUDINAL_TRAJECTORY = "LONGITUDINAL_TRAJECTORY"
    EXPLICIT_ALTERNATIVE = "EXPLICIT_ALTERNATIVE"
    REAL_GAME_EXAMPLE = "REAL_GAME_EXAMPLE"


class CandidateProposal(_CandidateModel):
    """Machine extractor proposal referencing external transcript segment indexes."""

    segment_indexes: tuple[int, ...] = Field(min_length=1)
    category: CandidateCategory
    summary: ShortText
    tags: tuple[TagText, ...] = ()
    extraction_confidence: Probability | None = None


class MachineCandidate(_CandidateModel):
    """Git-safe candidate locator/interpretation, not verified evidence."""

    source_id: ShortText
    start_ms: Millis
    end_ms: Millis
    category: CandidateCategory
    summary: ShortText
    tags: tuple[TagText, ...] = ()
    extraction_confidence: Probability | None = None
    human_review_state: HumanReviewState = HumanReviewState.NOT_STARTED

    @model_validator(mode="after")
    def _validate_range(self) -> "MachineCandidate":
        if self.end_ms < self.start_ms:
            raise ValueError("end_ms must not precede start_ms")
        return self


class CandidateArtifact(_CandidateModel):
    """Lightweight C2C output with no transcript body."""

    schema_version: str = "c2c-candidate-artifact-v1"
    source_id: ShortText
    extraction_state: ExtractionState
    candidates: tuple[MachineCandidate, ...]

    @model_validator(mode="after")
    def _validate_state(self) -> "CandidateArtifact":
        expected = (
            ExtractionState.COMPLETE if self.candidates else ExtractionState.NO_USEFUL_CANDIDATES
        )
        if self.extraction_state is not expected:
            raise ValueError("extraction_state does not match candidate presence")
        return self


def materialize_candidate_artifact(
    *,
    source_id: str,
    segments: Iterable[TranscriptSegment],
    proposals: Iterable[CandidateProposal],
) -> CandidateArtifact:
    """Resolve proposal segment indexes into timestamp locators without copying text."""

    segment_by_index = {segment.index: segment for segment in segments}
    candidates: list[MachineCandidate] = []

    for proposal in proposals:
        selected: list[TranscriptSegment] = []
        for index in proposal.segment_indexes:
            try:
                selected.append(segment_by_index[index])
            except KeyError as exc:
                raise ValueError(f"unknown transcript segment index: {index}") from exc

        candidates.append(
            MachineCandidate(
                source_id=source_id,
                start_ms=min(segment.start_ms for segment in selected),
                end_ms=max(segment.end_ms for segment in selected),
                category=proposal.category,
                summary=proposal.summary,
                tags=proposal.tags,
                extraction_confidence=proposal.extraction_confidence,
            )
        )

    candidate_tuple = tuple(candidates)
    state = ExtractionState.COMPLETE if candidate_tuple else ExtractionState.NO_USEFUL_CANDIDATES
    return CandidateArtifact(
        source_id=source_id,
        extraction_state=state,
        candidates=candidate_tuple,
    )
