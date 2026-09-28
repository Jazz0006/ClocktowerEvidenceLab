import pytest
from pydantic import ValidationError

from clocktower_evidence_lab.domain.decision import (
    DecisionResultLink,
    DecisionSlice,
    ExplicitAlternative,
    HistoricalPrefixBoundary,
    materialize_historical_prefix,
)
from clocktower_evidence_lab.domain.history import ControlOwner, SemanticEvent, SetupCommitment


def _setup(order: int, commitment_type: str) -> SetupCommitment:
    return SetupCommitment(
        commitment_id=f"setup:game1:{order}",
        game_id="game:1",
        reconstruction_revision_id="revision:game1:1",
        setup_order=order,
        commitment_type=commitment_type,
        controller=ControlOwner.STORYTELLER,
        subject_seat_id=f"seat:game1:{order}",
        value={"order": order},
    )


def _event(order: int, event_type: str) -> SemanticEvent:
    return SemanticEvent(
        event_id=f"event:game1:{order}",
        game_id="game:1",
        reconstruction_revision_id="revision:game1:1",
        event_order=order,
        phase="NIGHT_1",
        event_type=event_type,
        controller=ControlOwner.STORYTELLER,
        value={"order": order},
    )


def _setup_decision(
    *,
    boundary_order: int = 2,
    result_order: int = 3,
    **overrides: object,
) -> DecisionSlice:
    data: dict[str, object] = {
        "decision_id": "decision:game1:drunk-assignment",
        "game_id": "game:1",
        "reconstruction_revision_id": "revision:game1:1",
        "decision_type": "DRUNK_ASSIGNMENT",
        "controller": ControlOwner.STORYTELLER,
        "historical_prefix_boundary": HistoricalPrefixBoundary(
            setup_through_order=boundary_order
        ),
        "subject_seat_id": "seat:game1:3",
        "observed_choice": {
            "selected_seat_id": "seat:game1:3",
            "shown_role": "EMPATH",
        },
        "resulting_history": DecisionResultLink(
            setup_commitment_id=f"setup:game1:{result_order}",
            setup_order=result_order,
        ),
    }
    data.update(overrides)
    return DecisionSlice(**data)


def test_historical_prefix_boundary_is_unambiguous_between_setup_and_events() -> None:
    setup_boundary = HistoricalPrefixBoundary(setup_through_order=2)
    event_boundary = HistoricalPrefixBoundary(event_through_order=7)

    assert setup_boundary.setup_through_order == 2
    assert setup_boundary.event_through_order is None
    assert event_boundary.event_through_order == 7
    assert event_boundary.setup_through_order is None

    with pytest.raises(ValidationError):
        HistoricalPrefixBoundary()

    with pytest.raises(ValidationError):
        HistoricalPrefixBoundary(setup_through_order=2, event_through_order=7)


def test_setup_time_decision_cannot_include_its_own_or_later_result_commitment() -> None:
    with pytest.raises(ValidationError):
        _setup_decision(boundary_order=3, result_order=3)

    with pytest.raises(ValidationError):
        _setup_decision(boundary_order=4, result_order=3)


def test_setup_prefix_materialization_excludes_later_setup_and_all_events() -> None:
    setup_history = (
        _setup(1, "SHOWN_ROLE_LAYOUT"),
        _setup(2, "DEMON_BLUFFS"),
        _setup(3, "DRUNK_ASSIGNMENT"),
        _setup(4, "RED_HERRING"),
    )
    event_history = (_event(1, "PLAYER_ACTION_COMMITTED"),)

    decision = _setup_decision(boundary_order=2, result_order=3)
    setup_prefix, event_prefix = materialize_historical_prefix(
        decision,
        setup_history,
        event_history,
    )

    assert [item.setup_order for item in setup_prefix] == [1, 2]
    assert event_prefix == ()
    assert setup_history[2].commitment_id == decision.resulting_history.setup_commitment_id
    assert setup_history[2] not in setup_prefix
    assert setup_history[3] not in setup_prefix


def test_event_prefix_materialization_includes_setup_and_only_prior_events() -> None:
    setup_history = (_setup(1, "SHOWN_ROLE_LAYOUT"), _setup(2, "RED_HERRING"))
    event_history = (
        _event(1, "PLAYER_ACTION_COMMITTED"),
        _event(2, "STORYTELLER_CHOICE_COMMITTED"),
        _event(3, "INFORMATION_DELIVERED"),
        _event(4, "DEATH"),
    )
    decision = DecisionSlice(
        decision_id="decision:game1:information-result",
        game_id="game:1",
        reconstruction_revision_id="revision:game1:1",
        decision_type="INFORMATION_RESULT",
        controller=ControlOwner.STORYTELLER,
        historical_prefix_boundary=HistoricalPrefixBoundary(event_through_order=2),
        observed_choice={"result": "YES"},
        resulting_history=DecisionResultLink(
            semantic_event_id="event:game1:3",
            event_order=3,
        ),
    )

    setup_prefix, event_prefix = materialize_historical_prefix(
        decision,
        setup_history,
        event_history,
    )

    assert setup_prefix == setup_history
    assert [item.event_order for item in event_prefix] == [1, 2]
    assert event_history[2] not in event_prefix
    assert event_history[3] not in event_prefix


def test_event_decision_cannot_include_its_own_result_event() -> None:
    with pytest.raises(ValidationError):
        DecisionSlice(
            decision_id="decision:game1:information-result",
            game_id="game:1",
            reconstruction_revision_id="revision:game1:1",
            decision_type="INFORMATION_RESULT",
            controller=ControlOwner.STORYTELLER,
            historical_prefix_boundary=HistoricalPrefixBoundary(event_through_order=3),
            observed_choice={"result": "YES"},
            resulting_history=DecisionResultLink(
                semantic_event_id="event:game1:3",
                event_order=3,
            ),
        )


def test_explicit_alternatives_are_source_backed_and_not_legal_alternatives() -> None:
    considered = ExplicitAlternative(
        value={"seat_id": "seat:game1:2", "shown_role": "CHEF"},
        evidence_assertion_ids=("assertion:game1:considered-seat2",),
    )
    rejected = ExplicitAlternative(
        value={"seat_id": "seat:game1:4", "shown_role": "FORTUNE_TELLER"},
        evidence_assertion_ids=("assertion:game1:rejected-seat4",),
    )
    decision = _setup_decision(
        rationale_assertion_ids=("assertion:game1:assignment-rationale",),
        explicitly_considered_alternatives=(considered,),
        explicitly_rejected_alternatives=(rejected,),
    )

    assert decision.explicitly_considered_alternatives == (considered,)
    assert decision.explicitly_rejected_alternatives == (rejected,)

    with pytest.raises(ValidationError):
        _setup_decision(legal_alternatives=({"seat_id": "seat:game1:5"},))


def test_unknown_rationale_and_alternatives_survive_domain_round_trip() -> None:
    decision = _setup_decision(
        rationale_assertion_ids=None,
        explicitly_considered_alternatives=None,
        explicitly_rejected_alternatives=None,
    )

    restored = DecisionSlice.model_validate(decision.model_dump(mode="json"))

    assert restored.rationale_assertion_ids is None
    assert restored.explicitly_considered_alternatives is None
    assert restored.explicitly_rejected_alternatives is None


def test_materialization_rejects_cross_revision_history_and_stale_result_order() -> None:
    decision = _setup_decision(boundary_order=1, result_order=2)
    wrong_revision = SetupCommitment(
        commitment_id="setup:game1:99",
        game_id="game:1",
        reconstruction_revision_id="revision:game1:2",
        setup_order=99,
        commitment_type="LATER_SETUP",
    )

    with pytest.raises(ValueError, match="same game and reconstruction revision"):
        materialize_historical_prefix(
            decision,
            (_setup(1, "SHOWN_ROLE_LAYOUT"), _setup(2, "DRUNK_ASSIGNMENT"), wrong_revision),
            (),
        )

    stale_link = _setup_decision(
        boundary_order=1,
        result_order=3,
        resulting_history=DecisionResultLink(
            setup_commitment_id="setup:game1:2",
            setup_order=3,
        ),
    )

    with pytest.raises(ValueError, match="resulting setup order"):
        materialize_historical_prefix(
            stale_link,
            (_setup(1, "SHOWN_ROLE_LAYOUT"), _setup(2, "DRUNK_ASSIGNMENT")),
            (),
        )
