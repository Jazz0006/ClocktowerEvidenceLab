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


class CandidateRule(_CandidateModel):
    """Conservative text-locator rule; a match is not evidence verification."""

    rule_id: TagText
    category: CandidateCategory
    term_groups: tuple[tuple[ShortText, ...], ...] = Field(min_length=1)
    summary: ShortText
    tags: tuple[TagText, ...] = ()
    extraction_confidence: Probability | None = None
    context_before: int = Field(default=0, ge=0, le=20)
    context_after: int = Field(default=0, ge=0, le=20)

    @model_validator(mode="after")
    def _validate_term_groups(self) -> "CandidateRule":
        if any(not group for group in self.term_groups):
            raise ValueError("candidate rule term groups must not be empty")
        return self


DEFAULT_C2_RULES: tuple[CandidateRule, ...] = (
    CandidateRule(
        rule_id="storyteller-decision",
        category=CandidateCategory.STORYTELLER_DECISION,
        term_groups=(("storyteller",), ("choose", "chose", "show", "give", "make")),
        summary="Keyword-located potential Storyteller decision discussion.",
        tags=("storyteller-choice",),
        extraction_confidence=0.35,
        context_before=1,
        context_after=1,
    ),
    CandidateRule(
        rule_id="storyteller-rationale",
        category=CandidateCategory.STORYTELLER_RATIONALE,
        term_groups=(("storyteller",), ("because", "reason", "why")),
        summary="Keyword-located potential Storyteller rationale.",
        tags=("rationale",),
        extraction_confidence=0.4,
        context_before=1,
        context_after=1,
    ),
    CandidateRule(
        rule_id="setup-reasoning",
        category=CandidateCategory.SETUP_LEVEL_REASONING,
        term_groups=(("setup", "set up", "first night"), ("choose", "because", "information")),
        summary="Keyword-located potential setup-level reasoning.",
        tags=("setup",),
        extraction_confidence=0.35,
        context_before=1,
        context_after=1,
    ),
    CandidateRule(
        rule_id="misinformation",
        category=CandidateCategory.MISINFORMATION_POLICY,
        term_groups=(
            ("drunk", "poison", "incorrect information", "false information"),
            ("give", "show", "tell", "information"),
        ),
        summary="Keyword-located potential misinformation-policy discussion.",
        tags=("misinformation",),
        extraction_confidence=0.4,
        context_before=1,
        context_after=1,
    ),
    CandidateRule(
        rule_id="registration",
        category=CandidateCategory.REGISTRATION_CHOICE,
        term_groups=(("recluse", "spy"), ("register", "registration")),
        summary="Keyword-located potential registration-choice discussion.",
        tags=("registration",),
        extraction_confidence=0.5,
        context_before=1,
        context_after=1,
    ),
    CandidateRule(
        rule_id="demon-bluff",
        category=CandidateCategory.DEMON_BLUFF_REASONING,
        term_groups=(("demon",), ("bluff", "bluffs")),
        summary="Keyword-located potential Demon-bluff discussion.",
        tags=("demon-bluff",),
        extraction_confidence=0.45,
        context_before=1,
        context_after=1,
    ),
    CandidateRule(
        rule_id="player-experience",
        category=CandidateCategory.PLAYER_EXPERIENCE,
        term_groups=(("new player", "beginner", "experienced player", "veteran"),),
        summary="Keyword-located potential player-experience discussion.",
        tags=("player-experience",),
        extraction_confidence=0.35,
        context_before=1,
        context_after=1,
    ),
    CandidateRule(
        rule_id="player-agency",
        category=CandidateCategory.PLAYER_AGENCY,
        term_groups=(("player", "poisoner"), ("choice", "choose", "agency", "target")),
        summary="Keyword-located potential player-agency discussion.",
        tags=("player-agency",),
        extraction_confidence=0.35,
        context_before=1,
        context_after=1,
    ),
    CandidateRule(
        rule_id="information-strength",
        category=CandidateCategory.INFORMATION_STRENGTH,
        term_groups=(("strong information", "too much information", "powerful information"),),
        summary="Keyword-located potential information-strength discussion.",
        tags=("information-strength",),
        extraction_confidence=0.4,
        context_before=1,
        context_after=1,
    ),
    CandidateRule(
        rule_id="confirmation-chain",
        category=CandidateCategory.CONFIRMATION_CHAIN,
        term_groups=(("confirm", "confirmation"),),
        summary="Keyword-located potential confirmation-chain discussion.",
        tags=("confirmation",),
        extraction_confidence=0.3,
        context_before=1,
        context_after=1,
    ),
    CandidateRule(
        rule_id="longitudinal",
        category=CandidateCategory.LONGITUDINAL_TRAJECTORY,
        term_groups=(("next night", "later", "previous", "again", "consistent"),),
        summary="Keyword-located potential longitudinal-information discussion.",
        tags=("trajectory",),
        extraction_confidence=0.25,
        context_before=1,
        context_after=1,
    ),
    CandidateRule(
        rule_id="explicit-alternative",
        category=CandidateCategory.EXPLICIT_ALTERNATIVE,
        term_groups=(("instead", "rather than", "another option", "or you could"),),
        summary="Keyword-located potential explicit-alternative discussion.",
        tags=("alternative",),
        extraction_confidence=0.35,
        context_before=1,
        context_after=1,
    ),
    CandidateRule(
        rule_id="real-game-example",
        category=CandidateCategory.REAL_GAME_EXAMPLE,
        term_groups=(("in a game", "one game", "i ran", "when i was storyteller"),),
        summary="Keyword-located potential real-game example.",
        tags=("real-game-example",),
        extraction_confidence=0.3,
        context_before=1,
        context_after=1,
    ),
)


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


def locate_rule_candidates(
    segments: Iterable[TranscriptSegment],
    *,
    rules: Iterable[CandidateRule] = DEFAULT_C2_RULES,
) -> tuple[CandidateProposal, ...]:
    """Locate conservative candidate windows without treating text matches as verified meaning."""

    materialized = tuple(segments)
    normalized_text = tuple(segment.text.casefold() for segment in materialized)
    proposals: list[CandidateProposal] = []

    for rule in rules:
        normalized_groups = tuple(
            tuple(term.casefold() for term in group) for group in rule.term_groups
        )
        for position, text in enumerate(normalized_text):
            if not all(any(term in text for term in group) for group in normalized_groups):
                continue

            start = max(0, position - rule.context_before)
            end = min(len(materialized), position + rule.context_after + 1)
            proposals.append(
                CandidateProposal(
                    segment_indexes=tuple(segment.index for segment in materialized[start:end]),
                    category=rule.category,
                    summary=rule.summary,
                    tags=rule.tags,
                    extraction_confidence=rule.extraction_confidence,
                )
            )

    return tuple(proposals)
