from pathlib import Path

import pytest

from clocktower_evidence_lab.domain.decision import (
    DecisionResultLink,
    DecisionSlice,
    HistoricalPrefixBoundary,
)
from clocktower_evidence_lab.domain.history import (
    ControlOwner,
    SemanticEvent,
    SetupCommitment,
    SetupOrderBasis,
)
from clocktower_evidence_lab.domain.reconstruction import Game, GameSeat
from clocktower_evidence_lab.domain.tb_snapshot import SnapshotFieldState
from clocktower_evidence_lab.domain.tb_snapshot_materializer import (
    TroubleBrewingRoleType,
    TroubleBrewingSnapshotProjectionMetadata,
    materialize_tb_drunk_precommit_snapshot,
)
from clocktower_evidence_lab.interchange.tb_game_snapshot_v1 import (
    dump_tb_game_snapshot_v1,
    load_tb_game_snapshot_v1,
)

FIXTURE = Path(__file__).with_name("g10-game2-precommit-tbgs-v1.json")


def _game() -> Game:
    return Game(
        game_id="evidence:c1d:g10-game2",
        script="trouble_brewing",
        current_reconstruction_revision_id="revision:g10:1",
    )


def _game_seats() -> tuple[GameSeat, ...]:
    return tuple(
        GameSeat(
            seat_id=f"seat:g10:{seat}",
            game_id="evidence:c1d:g10-game2",
            seat_order=seat,
            seat_label=f"Seat {seat}",
        )
        for seat in range(1, 10)
    )


def _shown_layout(*, has_drunk: bool | None = True) -> SetupCommitment:
    roles = (
        "EMPATH",
        "IMP",
        "UNDERTAKER",
        "LIBRARIAN",
        "SPY",
        "MONK",
        "MAYOR",
        "VIRGIN",
        "BUTLER",
    )
    return SetupCommitment(
        commitment_id="setup:g10:shown-layout",
        game_id="evidence:c1d:g10-game2",
        reconstruction_revision_id="revision:g10:1",
        setup_order=1,
        setup_order_basis=SetupOrderBasis.EVIDENCED,
        commitment_type="SHOWN_ROLE_LAYOUT",
        controller=ControlOwner.STORYTELLER,
        value={
            "has_drunk": has_drunk,
            "seats": [
                {"seat_id": f"seat:g10:{seat}", "shown_role": role}
                for seat, role in enumerate(roles, start=1)
            ],
        },
    )


def _drunk_result() -> SetupCommitment:
    return SetupCommitment(
        commitment_id="setup:g10:drunk-assignment",
        game_id="evidence:c1d:g10-game2",
        reconstruction_revision_id="revision:g10:1",
        setup_order=2,
        setup_order_basis=SetupOrderBasis.EVIDENCED,
        commitment_type="DRUNK_ASSIGNMENT",
        controller=ControlOwner.STORYTELLER,
        subject_seat_id="seat:g10:1",
        value={"actual_role": "DRUNK", "shown_role": "EMPATH"},
    )


def _later_red_herring() -> SetupCommitment:
    return SetupCommitment(
        commitment_id="setup:g10:red-herring",
        game_id="evidence:c1d:g10-game2",
        reconstruction_revision_id="revision:g10:1",
        setup_order=3,
        setup_order_basis=SetupOrderBasis.EVIDENCED,
        commitment_type="RED_HERRING",
        controller=ControlOwner.STORYTELLER,
        subject_seat_id="seat:g10:7",
    )


def _later_information() -> SemanticEvent:
    return SemanticEvent(
        event_id="event:g10:librarian-info",
        game_id="evidence:c1d:g10-game2",
        reconstruction_revision_id="revision:g10:1",
        event_order=1,
        phase="NIGHT_1",
        event_type="INFORMATION_DELIVERED",
        controller=ControlOwner.STORYTELLER,
        value={"role": "LIBRARIAN"},
    )


def _decision() -> DecisionSlice:
    return DecisionSlice(
        decision_id="decision:g10:drunk-assignment",
        game_id="evidence:c1d:g10-game2",
        reconstruction_revision_id="revision:g10:1",
        decision_type="DRUNK_ASSIGNMENT",
        controller=ControlOwner.STORYTELLER,
        historical_prefix_boundary=HistoricalPrefixBoundary(setup_through_order=1),
        subject_seat_id="seat:g10:1",
        observed_choice={"selected_seat_id": "seat:g10:1", "shown_role": "EMPATH"},
        resulting_history=DecisionResultLink(
            setup_commitment_id="setup:g10:drunk-assignment",
            setup_order=2,
        ),
    )


def _projection_metadata() -> TroubleBrewingSnapshotProjectionMetadata:
    return TroubleBrewingSnapshotProjectionMetadata(
        game_seed=20_260_929,
        role_types_by_external_id={
            "empath": TroubleBrewingRoleType.TOWNSFOLK,
            "imp": TroubleBrewingRoleType.DEMON,
            "undertaker": TroubleBrewingRoleType.TOWNSFOLK,
            "librarian": TroubleBrewingRoleType.TOWNSFOLK,
            "spy": TroubleBrewingRoleType.MINION,
            "monk": TroubleBrewingRoleType.TOWNSFOLK,
            "mayor": TroubleBrewingRoleType.TOWNSFOLK,
            "virgin": TroubleBrewingRoleType.TOWNSFOLK,
            "butler": TroubleBrewingRoleType.OUTSIDER,
        },
    )


def test_g10_precommit_materialization_matches_host_tbgs0_golden_fixture() -> None:
    snapshot = materialize_tb_drunk_precommit_snapshot(
        game=_game(),
        game_seats=_game_seats(),
        decision=_decision(),
        setup_history=(_shown_layout(), _drunk_result(), _later_red_herring()),
        event_history=(_later_information(),),
        projection_metadata=_projection_metadata(),
    )

    encoded = dump_tb_game_snapshot_v1(snapshot)
    assert encoded == FIXTURE.read_text(encoding="utf-8").strip()

    assert snapshot.setup_state.drunk_assignment_seat.state is SnapshotFieldState.UNCOMMITTED
    actual_by_seat = {seat.seat: seat.actual_role_id for seat in snapshot.grimoire_seats}
    for seat in (1, 3, 4, 6, 7, 8):
        assert actual_by_seat[seat].state is SnapshotFieldState.UNCOMMITTED
    assert actual_by_seat[2].value == "imp"
    assert actual_by_seat[5].value == "spy"
    assert actual_by_seat[9].value == "butler"


def test_snapshot_json_round_trip_preserves_uncommitted_distinct_from_unknown() -> None:
    known_drunk_snapshot = materialize_tb_drunk_precommit_snapshot(
        game=_game(),
        game_seats=_game_seats(),
        decision=_decision(),
        setup_history=(_shown_layout(), _drunk_result()),
        event_history=(),
        projection_metadata=_projection_metadata(),
    )
    unknown_drunk_snapshot = materialize_tb_drunk_precommit_snapshot(
        game=_game(),
        game_seats=_game_seats(),
        decision=_decision(),
        setup_history=(_shown_layout(has_drunk=None), _drunk_result()),
        event_history=(),
        projection_metadata=_projection_metadata(),
    )

    assert (
        known_drunk_snapshot.setup_state.drunk_assignment_seat.state
        is SnapshotFieldState.UNCOMMITTED
    )
    assert (
        unknown_drunk_snapshot.setup_state.drunk_assignment_seat.state is SnapshotFieldState.UNKNOWN
    )
    assert (
        unknown_drunk_snapshot.grimoire_seats[0].actual_role_id.state is SnapshotFieldState.UNKNOWN
    )

    encoded = dump_tb_game_snapshot_v1(unknown_drunk_snapshot)
    restored = load_tb_game_snapshot_v1(encoded)
    assert dump_tb_game_snapshot_v1(restored) == encoded
    assert restored.setup_state.drunk_assignment_seat.state is SnapshotFieldState.UNKNOWN


def test_materializer_does_not_backfill_has_drunk_from_resulting_assignment() -> None:
    original_layout = _shown_layout()
    assert isinstance(original_layout.value, dict)
    layout = original_layout.model_copy(
        update={
            "value": {
                "seats": original_layout.value["seats"],
            }
        }
    )

    with pytest.raises(ValueError, match="must carry has_drunk explicitly"):
        materialize_tb_drunk_precommit_snapshot(
            game=_game(),
            game_seats=_game_seats(),
            decision=_decision(),
            setup_history=(layout, _drunk_result()),
            event_history=(),
            projection_metadata=_projection_metadata(),
        )


def test_materializer_requires_projection_metadata_instead_of_owning_tb_legality() -> None:
    metadata = _projection_metadata().model_copy(
        update={
            "role_types_by_external_id": {
                key: value
                for key, value in _projection_metadata().role_types_by_external_id.items()
                if key != "empath"
            }
        }
    )

    with pytest.raises(ValueError, match="missing projection role type for empath"):
        materialize_tb_drunk_precommit_snapshot(
            game=_game(),
            game_seats=_game_seats(),
            decision=_decision(),
            setup_history=(_shown_layout(), _drunk_result()),
            event_history=(),
            projection_metadata=metadata,
        )
