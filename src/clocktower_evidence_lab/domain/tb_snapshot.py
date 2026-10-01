"""Trouble Brewing V1 decision-time snapshot semantics shared with CampBoardGameHost."""

from enum import StrEnum
from typing import Literal

from pydantic import BaseModel, ConfigDict, Field, model_validator

SNAPSHOT_SCHEMA_ID = "botc.tb.game-snapshot"
SNAPSHOT_SCHEMA_VERSION = 1
SNAPSHOT_SCRIPT_ID = "trouble_brewing"


class _SnapshotModel(BaseModel):
    model_config = ConfigDict(extra="forbid", frozen=True, populate_by_name=True)


class SnapshotFieldState(StrEnum):
    KNOWN = "KNOWN"
    UNCOMMITTED = "UNCOMMITTED"
    UNKNOWN = "UNKNOWN"
    NOT_APPLICABLE = "NOT_APPLICABLE"


class SnapshotField[T](_SnapshotModel):
    """Four-state value matching the Host TBGS-0 interchange contract."""

    state: SnapshotFieldState
    value: T | None = None

    @model_validator(mode="after")
    def _validate_value_shape(self) -> "SnapshotField[T]":
        if self.state is SnapshotFieldState.KNOWN:
            if self.value is None:
                raise ValueError("KNOWN snapshot field requires a value")
        elif self.value is not None:
            raise ValueError(f"{self.state} snapshot field must not carry a value")
        return self

    @classmethod
    def known(cls, value: T) -> "SnapshotField[T]":
        return cls(state=SnapshotFieldState.KNOWN, value=value)

    @classmethod
    def uncommitted(cls) -> "SnapshotField[T]":
        return cls(state=SnapshotFieldState.UNCOMMITTED)

    @classmethod
    def unknown(cls) -> "SnapshotField[T]":
        return cls(state=SnapshotFieldState.UNKNOWN)

    @classmethod
    def not_applicable(cls) -> "SnapshotField[T]":
        return cls(state=SnapshotFieldState.NOT_APPLICABLE)


class TroubleBrewingSnapshotStage(StrEnum):
    SETUP_PRECOMMIT = "SETUP_PRECOMMIT"
    SETUP_COMMITTED = "SETUP_COMMITTED"
    RUNTIME = "RUNTIME"


class TroubleBrewingSnapshotPosition(_SnapshotModel):
    stage: TroubleBrewingSnapshotStage
    phase: SnapshotField[str]
    round: SnapshotField[int]
    game_state_revision: SnapshotField[int] = Field(
        default_factory=SnapshotField[int].not_applicable,
        alias="gameStateRevision",
    )
    player_input_revision: SnapshotField[int] = Field(
        default_factory=SnapshotField[int].not_applicable,
        alias="playerInputRevision",
    )

    @model_validator(mode="after")
    def _validate_known_numbers(self) -> "TroubleBrewingSnapshotPosition":
        if self.round.state is SnapshotFieldState.KNOWN and self.round.value <= 0:
            raise ValueError("known Trouble Brewing snapshot round must be positive")
        for label, field in (
            ("game-state", self.game_state_revision),
            ("player-input", self.player_input_revision),
        ):
            if field.state is SnapshotFieldState.KNOWN and field.value < 0:
                raise ValueError(f"known {label} revision cannot be negative")
        return self


class TroubleBrewingSnapshotSeat(_SnapshotModel):
    seat: int = Field(ge=1)
    shown_role_id: SnapshotField[str] = Field(alias="shownRoleId")
    actual_role_id: SnapshotField[str] = Field(alias="actualRoleId")
    alive: SnapshotField[bool]
    poisoned: SnapshotField[bool]

    @model_validator(mode="after")
    def _validate_known_role_ids(self) -> "TroubleBrewingSnapshotSeat":
        for label, field in (
            ("shown", self.shown_role_id),
            ("actual", self.actual_role_id),
        ):
            if field.state is SnapshotFieldState.KNOWN and not field.value.strip():
                raise ValueError(f"known {label} role ID cannot be blank")
        return self


class TroubleBrewingSnapshotSetupState(_SnapshotModel):
    has_drunk: SnapshotField[bool] = Field(alias="hasDrunk")
    drunk_assignment_seat: SnapshotField[int] = Field(alias="drunkAssignmentSeat")

    @model_validator(mode="after")
    def _validate_drunk_state(self) -> "TroubleBrewingSnapshotSetupState":
        if (
            self.drunk_assignment_seat.state is SnapshotFieldState.KNOWN
            and self.drunk_assignment_seat.value <= 0
        ):
            raise ValueError("known Drunk assignment seat must be positive")

        if self.has_drunk.state is SnapshotFieldState.KNOWN:
            if self.has_drunk.value is False:
                if self.drunk_assignment_seat.state is not SnapshotFieldState.NOT_APPLICABLE:
                    raise ValueError(
                        "known non-Drunk setup must mark Drunk assignment NOT_APPLICABLE"
                    )
            elif self.drunk_assignment_seat.state is SnapshotFieldState.NOT_APPLICABLE:
                raise ValueError("known Drunk setup cannot mark Drunk assignment NOT_APPLICABLE")
        return self


class TroubleBrewingGameSnapshotV1(_SnapshotModel):
    """Versioned immutable TB snapshot compatible with the Host TBGS-0 contract."""

    schema_id: Literal["botc.tb.game-snapshot"] = Field(
        default=SNAPSHOT_SCHEMA_ID,
        alias="schemaId",
    )
    schema_version: Literal[1] = Field(
        default=SNAPSHOT_SCHEMA_VERSION,
        alias="schemaVersion",
    )
    game_id: str = Field(min_length=1, alias="gameId")
    script: Literal["trouble_brewing"] = SNAPSHOT_SCRIPT_ID
    game_seed: int = Field(alias="gameSeed")
    position: TroubleBrewingSnapshotPosition
    grimoire_seats: tuple[TroubleBrewingSnapshotSeat, ...] = Field(alias="grimoireSeats")
    setup_state: TroubleBrewingSnapshotSetupState = Field(alias="setupState")

    @model_validator(mode="after")
    def _validate_seats(self) -> "TroubleBrewingGameSnapshotV1":
        if not self.grimoire_seats:
            raise ValueError("Trouble Brewing snapshot must contain at least one seat")

        seat_numbers = [item.seat for item in self.grimoire_seats]
        if seat_numbers != list(range(1, len(seat_numbers) + 1)):
            raise ValueError(
                "Trouble Brewing snapshot seats must be ordered canonically "
                "from 1 through player count"
            )

        drunk_seat = self.setup_state.drunk_assignment_seat
        if drunk_seat.state is SnapshotFieldState.KNOWN and drunk_seat.value not in seat_numbers:
            raise ValueError("known Drunk assignment must reference a snapshot seat")
        return self
