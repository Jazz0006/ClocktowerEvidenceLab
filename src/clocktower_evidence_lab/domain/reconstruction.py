"""Reconstruction identity and revision-domain entities."""

from datetime import datetime
from enum import StrEnum
from typing import Annotated

from pydantic import BaseModel, ConfigDict, Field, JsonValue, model_validator

from clocktower_evidence_lab.domain.primitives import SemanticId

ShortText = Annotated[str, Field(min_length=1, max_length=256)]
LongText = Annotated[str, Field(min_length=1, max_length=4_000)]
SeatOrder = Annotated[int, Field(ge=1)]


class _DomainModel(BaseModel):
    model_config = ConfigDict(extra="forbid", frozen=True)


class ReconstructionStatus(StrEnum):
    NOT_STARTED = "NOT_STARTED"
    PARTIAL = "PARTIAL"
    COMPLETE = "COMPLETE"


class Storyteller(_DomainModel):
    """Stable public Storyteller identity without qualification scoring."""

    storyteller_id: SemanticId
    independence_key: SemanticId
    display_name: ShortText | None = None


class StorytellerAssignment(_DomainModel):
    """A Storyteller's game-scoped role assignment."""

    storyteller_id: SemanticId
    role: ShortText


class Game(_DomainModel):
    """A game container whose current revision pointer has one owner."""

    game_id: SemanticId
    script: ShortText | None = None
    storyteller_assignments: tuple[StorytellerAssignment, ...] = ()
    reconstruction_status: ReconstructionStatus = ReconstructionStatus.NOT_STARTED
    current_reconstruction_revision_id: SemanticId | None = None

    @model_validator(mode="after")
    def _validate_storyteller_assignments(self) -> "Game":
        storyteller_ids = [
            assignment.storyteller_id for assignment in self.storyteller_assignments
        ]
        if len(set(storyteller_ids)) != len(storyteller_ids):
            raise ValueError("game storyteller assignments must use unique storyteller IDs")
        return self


class GameSeat(_DomainModel):
    """A participant identity scoped strictly to one game."""

    seat_id: SemanticId
    game_id: SemanticId
    seat_order: SeatOrder | None = None
    seat_label: ShortText | None = None
    display_name: ShortText | None = None
    experience_metadata: JsonValue | None = None


class ReconstructionRevision(_DomainModel):
    """One auditable interpretation revision of a game's reconstruction."""

    revision_id: SemanticId
    game_id: SemanticId
    parent_revision_id: SemanticId | None = None
    created_at: datetime
    change_note: LongText | None = None

    @model_validator(mode="after")
    def _validate_revision(self) -> "ReconstructionRevision":
        if self.parent_revision_id == self.revision_id:
            raise ValueError("reconstruction revision cannot parent itself")
        if self.created_at.tzinfo is None or self.created_at.utcoffset() is None:
            raise ValueError("created_at must be timezone-aware")
        return self
