"""Whole-game reconstruction history contracts exposed by C0 evidence."""

from enum import StrEnum
from typing import Annotated

from pydantic import BaseModel, ConfigDict, Field, JsonValue, model_validator

from clocktower_evidence_lab.domain.primitives import SemanticId

ShortText = Annotated[str, Field(min_length=1, max_length=256)]
LongText = Annotated[str, Field(min_length=1, max_length=4_000)]
PositiveOrder = Annotated[int, Field(ge=1)]


class _DomainModel(BaseModel):
    model_config = ConfigDict(extra="forbid", frozen=True)


class SourceGameMatchStatus(StrEnum):
    """Review state for whether one evidence source refers to one logical game."""

    UNRESOLVED = "UNRESOLVED"
    CANDIDATE = "CANDIDATE"
    VERIFIED_SAME = "VERIFIED_SAME"
    VERIFIED_DIFFERENT = "VERIFIED_DIFFERENT"


class ControlOwner(StrEnum):
    """Who controlled a historical choice when that ownership is known."""

    PLAYER = "PLAYER"
    STORYTELLER = "STORYTELLER"
    AUTOMATIC = "AUTOMATIC"
    UNKNOWN = "UNKNOWN"


class SourceGameLink(_DomainModel):
    """A reviewed source-to-logical-game association candidate."""

    link_id: SemanticId
    source_id: SemanticId
    game_id: SemanticId
    match_status: SourceGameMatchStatus = SourceGameMatchStatus.UNRESOLVED
    note: LongText | None = None


class SetupCommitment(_DomainModel):
    """A revision-scoped setup fact committed before ordinary game events."""

    commitment_id: SemanticId
    game_id: SemanticId
    reconstruction_revision_id: SemanticId
    setup_order: PositiveOrder
    commitment_type: ShortText
    controller: ControlOwner = ControlOwner.UNKNOWN
    subject_seat_id: SemanticId | None = None
    target_seat_ids: tuple[SemanticId, ...] = ()
    value: JsonValue | None = None

    @model_validator(mode="after")
    def _validate_targets(self) -> "SetupCommitment":
        if len(set(self.target_seat_ids)) != len(self.target_seat_ids):
            raise ValueError("setup commitment target seat IDs must be unique")
        return self


class SemanticEvent(_DomainModel):
    """One ordered historical event in a reconstruction revision."""

    event_id: SemanticId
    game_id: SemanticId
    reconstruction_revision_id: SemanticId
    event_order: PositiveOrder
    phase: ShortText
    event_type: ShortText
    controller: ControlOwner = ControlOwner.UNKNOWN
    actor_seat_id: SemanticId | None = None
    subject_seat_id: SemanticId | None = None
    target_seat_ids: tuple[SemanticId, ...] = ()
    value: JsonValue | None = None

    @model_validator(mode="after")
    def _validate_targets(self) -> "SemanticEvent":
        if len(set(self.target_seat_ids)) != len(self.target_seat_ids):
            raise ValueError("semantic event target seat IDs must be unique")
        return self
