import pytest
from pydantic import ValidationError

from clocktower_evidence_lab.domain.history import (
    ControlOwner,
    SemanticEvent,
    SetupCommitment,
    SourceGameLink,
    SourceGameMatchStatus,
)


def test_multiple_sources_may_refer_to_one_logical_game_without_becoming_game_ids() -> None:
    storyteller_record = SourceGameLink(
        link_id="source-game-link:scott-st",
        source_id="source:clocktracker:storyteller",
        game_id="game:scott-2025-09-10",
        match_status=SourceGameMatchStatus.VERIFIED_SAME,
    )
    player_record = SourceGameLink(
        link_id="source-game-link:scott-player",
        source_id="source:clocktracker:player",
        game_id="game:scott-2025-09-10",
        match_status=SourceGameMatchStatus.VERIFIED_SAME,
    )

    assert storyteller_record.game_id == player_record.game_id
    assert storyteller_record.source_id != player_record.source_id


def test_source_game_match_state_is_explicit_and_can_record_negative_review() -> None:
    rejected_match = SourceGameLink(
        link_id="source-game-link:not-the-same-game",
        source_id="source:clocktracker:candidate",
        game_id="game:other",
        match_status=SourceGameMatchStatus.VERIFIED_DIFFERENT,
    )

    assert rejected_match.match_status is SourceGameMatchStatus.VERIFIED_DIFFERENT

    with pytest.raises(ValidationError):
        SourceGameLink(
            link_id="source-game-link:implicit-match",
            source_id="source:clocktracker:candidate",
            game_id="game:other",
            verified_same=True,
        )


def test_setup_commitment_is_revision_scoped_and_ordered_before_game_events() -> None:
    commitment = SetupCommitment(
        commitment_id="setup:game1:red-herring",
        game_id="game:1",
        reconstruction_revision_id="revision:game1:1",
        setup_order=2,
        commitment_type="RED_HERRING",
        controller=ControlOwner.STORYTELLER,
        subject_seat_id="seat:game1:4",
        value={"fortune_teller_seat_id": "seat:game1:7"},
    )

    assert commitment.setup_order == 2
    assert commitment.controller is ControlOwner.STORYTELLER

    with pytest.raises(ValidationError):
        SetupCommitment(
            commitment_id="setup:game1:missing-revision",
            game_id="game:1",
            setup_order=1,
            commitment_type="DEMON_BLUFFS",
            controller=ControlOwner.STORYTELLER,
            value=["CHEF", "MONK", "SOLDIER"],
        )


def test_setup_commitment_rejects_nonpositive_order() -> None:
    with pytest.raises(ValidationError):
        SetupCommitment(
            commitment_id="setup:game1:bad-order",
            game_id="game:1",
            reconstruction_revision_id="revision:game1:1",
            setup_order=0,
            commitment_type="DRUNK_SHOWN_ROLE",
            controller=ControlOwner.STORYTELLER,
            value="EMPATH",
        )


def test_semantic_event_has_revision_global_order_and_generic_targets() -> None:
    event = SemanticEvent(
        event_id="event:game1:n2:ft-result",
        game_id="game:1",
        reconstruction_revision_id="revision:game1:1",
        event_order=17,
        phase="NIGHT_2",
        event_type="INFORMATION_DELIVERY",
        controller=ControlOwner.STORYTELLER,
        target_seat_ids=("seat:game1:3",),
        value={"result": "YES"},
    )

    assert event.event_order == 17
    assert event.phase == "NIGHT_2"
    assert event.target_seat_ids == ("seat:game1:3",)


def test_semantic_event_allows_unknown_actor_and_value_without_guessing() -> None:
    event = SemanticEvent(
        event_id="event:game1:d3:unknown",
        game_id="game:1",
        reconstruction_revision_id="revision:game1:1",
        event_order=23,
        phase="DAY_3",
        event_type="EXECUTION",
        controller=ControlOwner.UNKNOWN,
        actor_seat_id=None,
        target_seat_ids=(),
        value=None,
    )

    assert event.actor_seat_id is None
    assert event.value is None


def test_semantic_event_rejects_duplicate_targets_and_nonpositive_order() -> None:
    with pytest.raises(ValidationError):
        SemanticEvent(
            event_id="event:game1:duplicate-targets",
            game_id="game:1",
            reconstruction_revision_id="revision:game1:1",
            event_order=1,
            phase="NIGHT_1",
            event_type="PLAYER_CHOICE",
            controller=ControlOwner.PLAYER,
            target_seat_ids=("seat:game1:2", "seat:game1:2"),
        )

    with pytest.raises(ValidationError):
        SemanticEvent(
            event_id="event:game1:bad-order",
            game_id="game:1",
            reconstruction_revision_id="revision:game1:1",
            event_order=0,
            phase="NIGHT_1",
            event_type="INFORMATION_DELIVERY",
            controller=ControlOwner.STORYTELLER,
        )


def test_semantic_event_does_not_accept_source_locator_time_as_historical_time() -> None:
    with pytest.raises(ValidationError):
        SemanticEvent(
            event_id="event:game1:bad-time",
            game_id="game:1",
            reconstruction_revision_id="revision:game1:1",
            event_order=1,
            phase="NIGHT_1",
            event_type="INFORMATION_DELIVERY",
            controller=ControlOwner.STORYTELLER,
            source_start_ms=632_000,
        )
