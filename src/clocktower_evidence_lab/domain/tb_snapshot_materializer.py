"""Pure Trouble Brewing snapshot materialization from EvidenceLab historical prefixes."""

import re
from collections.abc import Mapping, Sequence
from enum import StrEnum

from pydantic import BaseModel, ConfigDict, Field, model_validator

from clocktower_evidence_lab.domain.decision import DecisionSlice, materialize_historical_prefix
from clocktower_evidence_lab.domain.history import SemanticEvent, SetupCommitment
from clocktower_evidence_lab.domain.reconstruction import Game, GameSeat
from clocktower_evidence_lab.domain.tb_snapshot import (
    SnapshotField,
    TroubleBrewingGameSnapshotV1,
    TroubleBrewingSnapshotPosition,
    TroubleBrewingSnapshotSeat,
    TroubleBrewingSnapshotSetupState,
    TroubleBrewingSnapshotStage,
)


class TroubleBrewingRoleType(StrEnum):
    TOWNSFOLK = "TOWNSFOLK"
    OUTSIDER = "OUTSIDER"
    MINION = "MINION"
    DEMON = "DEMON"


class TroubleBrewingSnapshotProjectionMetadata(BaseModel):
    """Non-evidence projection metadata required by the Host V1 interchange shape."""

    model_config = ConfigDict(extra="forbid", frozen=True)

    game_seed: int
    role_types_by_external_id: Mapping[str, TroubleBrewingRoleType] = Field(min_length=1)

    @model_validator(mode="after")
    def _validate_role_ids(self) -> "TroubleBrewingSnapshotProjectionMetadata":
        normalized = [
            _normalize_external_role_id(role_id) for role_id in self.role_types_by_external_id
        ]
        if len(set(normalized)) != len(normalized):
            raise ValueError(
                "projection role metadata must not contain duplicate normalized role IDs"
            )
        return self

    def role_type(self, role_id: str) -> TroubleBrewingRoleType:
        normalized = _normalize_external_role_id(role_id)
        for candidate, role_type in self.role_types_by_external_id.items():
            if _normalize_external_role_id(candidate) == normalized:
                return role_type
        raise ValueError(f"missing projection role type for {normalized}")


def materialize_tb_drunk_precommit_snapshot(
    *,
    game: Game,
    game_seats: Sequence[GameSeat],
    decision: DecisionSlice,
    setup_history: Sequence[SetupCommitment],
    event_history: Sequence[SemanticEvent],
    projection_metadata: TroubleBrewingSnapshotProjectionMetadata,
) -> TroubleBrewingGameSnapshotV1:
    """Materialize the TBGS-0 setup-precommit snapshot for one Drunk assignment boundary."""

    if _normalize_external_role_id(game.script or "") != "trouble_brewing":
        raise ValueError("TB snapshot materializer requires a Trouble Brewing game")
    if decision.decision_type.upper() != "DRUNK_ASSIGNMENT":
        raise ValueError("TB precommit materializer requires a DRUNK_ASSIGNMENT decision")

    setup_prefix, event_prefix = materialize_historical_prefix(
        decision,
        setup_history,
        event_history,
    )
    if event_prefix:
        raise ValueError("Drunk setup-precommit snapshot cannot include ordinary game events")

    layouts = [item for item in setup_prefix if item.commitment_type == "SHOWN_ROLE_LAYOUT"]
    if len(layouts) != 1:
        raise ValueError("Drunk precommit snapshot requires exactly one SHOWN_ROLE_LAYOUT")

    layout = _require_object(layouts[0].value, "SHOWN_ROLE_LAYOUT value")
    has_drunk = _parse_has_drunk(layout)
    seat_entries = layout.get("seats")
    if not isinstance(seat_entries, list) or not seat_entries:
        raise ValueError("SHOWN_ROLE_LAYOUT requires a non-empty seats list")

    seats_by_id = _canonical_game_seats(game, game_seats)
    snapshot_seats: list[TroubleBrewingSnapshotSeat] = []
    seen_ids: set[str] = set()

    for raw_entry in seat_entries:
        entry = _require_object(raw_entry, "SHOWN_ROLE_LAYOUT seat")
        seat_id = entry.get("seat_id")
        shown_role = entry.get("shown_role")
        if not isinstance(seat_id, str) or not seat_id:
            raise ValueError("SHOWN_ROLE_LAYOUT seat requires a non-empty seat_id")
        if seat_id in seen_ids:
            raise ValueError("SHOWN_ROLE_LAYOUT seat IDs must be unique")
        seen_ids.add(seat_id)
        if not isinstance(shown_role, str) or not shown_role:
            raise ValueError("SHOWN_ROLE_LAYOUT seat requires a non-empty shown_role")

        seat = seats_by_id.get(seat_id)
        if seat is None:
            raise ValueError(f"SHOWN_ROLE_LAYOUT references unknown game seat {seat_id}")

        external_role_id = _normalize_external_role_id(shown_role)
        role_type = projection_metadata.role_type(external_role_id)
        actual_role = _precommit_actual_role(
            shown_role_id=external_role_id,
            shown_role_type=role_type,
            has_drunk=has_drunk,
        )

        snapshot_seats.append(
            TroubleBrewingSnapshotSeat(
                seat=seat.seat_order,
                shownRoleId=SnapshotField[str].known(external_role_id),
                actualRoleId=actual_role,
                alive=SnapshotField[bool].known(True),
                poisoned=SnapshotField[bool].known(False),
            )
        )

    if seen_ids != set(seats_by_id):
        raise ValueError("SHOWN_ROLE_LAYOUT must cover every provided game seat exactly once")

    snapshot_seats.sort(key=lambda item: item.seat)
    return TroubleBrewingGameSnapshotV1(
        gameId=game.game_id,
        gameSeed=projection_metadata.game_seed,
        position=TroubleBrewingSnapshotPosition(
            stage=TroubleBrewingSnapshotStage.SETUP_PRECOMMIT,
            phase=SnapshotField[str].not_applicable(),
            round=SnapshotField[int].not_applicable(),
            gameStateRevision=SnapshotField[int].not_applicable(),
            playerInputRevision=SnapshotField[int].not_applicable(),
        ),
        grimoireSeats=tuple(snapshot_seats),
        setupState=TroubleBrewingSnapshotSetupState(
            hasDrunk=_snapshot_has_drunk(has_drunk),
            drunkAssignmentSeat=_snapshot_drunk_assignment(has_drunk),
        ),
    )


def _canonical_game_seats(game: Game, game_seats: Sequence[GameSeat]) -> dict[str, GameSeat]:
    relevant = [seat for seat in game_seats if seat.game_id == game.game_id]
    if len(relevant) != len(game_seats):
        raise ValueError("snapshot game seats must all belong to the requested game")
    if not relevant:
        raise ValueError("snapshot materialization requires game seats")
    if any(seat.seat_order is None for seat in relevant):
        raise ValueError("snapshot materialization requires known seat order")

    orders = sorted(seat.seat_order for seat in relevant)
    if orders != list(range(1, len(relevant) + 1)):
        raise ValueError("snapshot game seats must use contiguous order starting at 1")
    if len({seat.seat_id for seat in relevant}) != len(relevant):
        raise ValueError("snapshot game seat IDs must be unique")
    return {seat.seat_id: seat for seat in relevant}


def _parse_has_drunk(layout: dict[str, object]) -> bool | None:
    if "has_drunk" not in layout:
        raise ValueError(
            "SHOWN_ROLE_LAYOUT must carry has_drunk explicitly; materializer must not infer it "
            "from the later Drunk result"
        )
    value = layout["has_drunk"]
    if value is None or isinstance(value, bool):
        return value
    raise ValueError("SHOWN_ROLE_LAYOUT has_drunk must be boolean or null")


def _precommit_actual_role(
    *,
    shown_role_id: str,
    shown_role_type: TroubleBrewingRoleType,
    has_drunk: bool | None,
) -> SnapshotField[str]:
    if shown_role_type is not TroubleBrewingRoleType.TOWNSFOLK:
        return SnapshotField[str].known(shown_role_id)
    if has_drunk is True:
        return SnapshotField[str].uncommitted()
    if has_drunk is False:
        return SnapshotField[str].known(shown_role_id)
    return SnapshotField[str].unknown()


def _snapshot_has_drunk(has_drunk: bool | None) -> SnapshotField[bool]:
    if has_drunk is None:
        return SnapshotField[bool].unknown()
    return SnapshotField[bool].known(has_drunk)


def _snapshot_drunk_assignment(has_drunk: bool | None) -> SnapshotField[int]:
    if has_drunk is True:
        return SnapshotField[int].uncommitted()
    if has_drunk is False:
        return SnapshotField[int].not_applicable()
    return SnapshotField[int].unknown()


def _require_object(value: object, label: str) -> dict[str, object]:
    if not isinstance(value, dict):
        raise ValueError(f"{label} must be an object")
    return value


def _normalize_external_role_id(value: str) -> str:
    normalized = re.sub(r"[^a-z0-9]+", "_", value.strip().lower()).strip("_")
    if not normalized:
        raise ValueError("role ID cannot be blank")
    return normalized
