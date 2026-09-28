"""Derived decision-time views over authoritative reconstruction history."""

from collections.abc import Iterable, Sequence
from typing import Annotated

from pydantic import BaseModel, ConfigDict, Field, JsonValue, model_validator

from clocktower_evidence_lab.domain.history import (
    ControlOwner,
    SemanticEvent,
    SetupCommitment,
    SetupOrderBasis,
)
from clocktower_evidence_lab.domain.primitives import SemanticId

ShortText = Annotated[str, Field(min_length=1, max_length=256)]
NonNegativeOrder = Annotated[int, Field(ge=0)]
PositiveOrder = Annotated[int, Field(ge=1)]


class _DomainModel(BaseModel):
    model_config = ConfigDict(extra="forbid", frozen=True)


class HistoricalPrefixBoundary(_DomainModel):
    """Decision-time boundary expressed as the latest included history order."""

    setup_through_order: NonNegativeOrder | None = None
    event_through_order: NonNegativeOrder | None = None

    @model_validator(mode="after")
    def _validate_exactly_one_boundary(self) -> "HistoricalPrefixBoundary":
        selected = sum(
            value is not None for value in (self.setup_through_order, self.event_through_order)
        )
        if selected != 1:
            raise ValueError("historical prefix boundary must select exactly one history stream")
        return self


class DecisionResultLink(_DomainModel):
    """Reference to the authoritative history item created by the observed choice."""

    setup_commitment_id: SemanticId | None = None
    setup_order: PositiveOrder | None = None
    semantic_event_id: SemanticId | None = None
    event_order: PositiveOrder | None = None

    @model_validator(mode="after")
    def _validate_exactly_one_result(self) -> "DecisionResultLink":
        has_setup = self.setup_commitment_id is not None or self.setup_order is not None
        has_event = self.semantic_event_id is not None or self.event_order is not None

        if has_setup == has_event:
            raise ValueError("decision result must link to exactly one history item")
        if has_setup and (self.setup_commitment_id is None or self.setup_order is None):
            raise ValueError("setup result link requires both commitment ID and setup order")
        if has_event and (self.semantic_event_id is None or self.event_order is None):
            raise ValueError("event result link requires both event ID and event order")
        return self


class ExplicitAlternative(_DomainModel):
    """A source-backed alternative explicitly considered or rejected by the controller."""

    value: JsonValue
    evidence_assertion_ids: tuple[SemanticId, ...]

    @model_validator(mode="after")
    def _validate_evidence(self) -> "ExplicitAlternative":
        if not self.evidence_assertion_ids:
            raise ValueError("explicit alternative requires source-backed evidence assertions")
        if len(set(self.evidence_assertion_ids)) != len(self.evidence_assertion_ids):
            raise ValueError("explicit alternative evidence assertion IDs must be unique")
        return self


class DecisionSlice(_DomainModel):
    """Derived analytical view of one choice at its historical decision boundary."""

    decision_id: SemanticId
    game_id: SemanticId
    reconstruction_revision_id: SemanticId
    decision_type: ShortText
    controller: ControlOwner
    historical_prefix_boundary: HistoricalPrefixBoundary
    subject_seat_id: SemanticId | None = None
    observed_choice: JsonValue | None = None
    resulting_history: DecisionResultLink
    rationale_assertion_ids: tuple[SemanticId, ...] | None = None
    explicitly_considered_alternatives: tuple[ExplicitAlternative, ...] | None = None
    explicitly_rejected_alternatives: tuple[ExplicitAlternative, ...] | None = None

    @model_validator(mode="after")
    def _validate_prefix_precedes_result(self) -> "DecisionSlice":
        if self.rationale_assertion_ids is not None:
            if not self.rationale_assertion_ids:
                raise ValueError("source-backed rationale requires at least one evidence assertion")
            if len(set(self.rationale_assertion_ids)) != len(self.rationale_assertion_ids):
                raise ValueError("rationale evidence assertion IDs must be unique")

        boundary = self.historical_prefix_boundary
        result = self.resulting_history

        if result.setup_commitment_id is not None:
            if boundary.setup_through_order is None:
                raise ValueError("setup result requires a setup-prefix boundary")
            if boundary.setup_through_order >= result.setup_order:
                raise ValueError("setup decision prefix cannot include its resulting commitment")
        else:
            if boundary.event_through_order is None:
                raise ValueError("event result requires an event-prefix boundary")
            if boundary.event_through_order >= result.event_order:
                raise ValueError("event decision prefix cannot include its resulting event")

        return self


def materialize_historical_prefix(
    decision: DecisionSlice,
    setup_history: Sequence[SetupCommitment],
    event_history: Sequence[SemanticEvent],
) -> tuple[tuple[SetupCommitment, ...], tuple[SemanticEvent, ...]]:
    """Project only the authoritative history committed before one decision."""

    _validate_history_identity(decision, setup_history, event_history)

    setup_items = tuple(sorted(setup_history, key=lambda item: item.setup_order))
    event_items = tuple(sorted(event_history, key=lambda item: item.event_order))
    _validate_deterministic_orders(setup_items, event_items)
    _validate_result_link(decision, setup_items, event_items)

    boundary = decision.historical_prefix_boundary
    if boundary.setup_through_order is not None:
        _validate_setup_prefix_order_evidence(setup_items)
        _validate_boundary_order_exists(
            boundary.setup_through_order,
            (item.setup_order for item in setup_items),
            "setup",
        )
        return (
            tuple(item for item in setup_items if item.setup_order <= boundary.setup_through_order),
            (),
        )

    _validate_boundary_order_exists(
        boundary.event_through_order,
        (item.event_order for item in event_items),
        "event",
    )
    return (
        setup_items,
        tuple(item for item in event_items if item.event_order <= boundary.event_through_order),
    )


def _validate_history_identity(
    decision: DecisionSlice,
    setup_history: Sequence[SetupCommitment],
    event_history: Sequence[SemanticEvent],
) -> None:
    for item in (*setup_history, *event_history):
        if (
            item.game_id != decision.game_id
            or item.reconstruction_revision_id != decision.reconstruction_revision_id
        ):
            raise ValueError(
                "decision history must belong to the same game and reconstruction revision"
            )


def _validate_deterministic_orders(
    setup_history: Sequence[SetupCommitment],
    event_history: Sequence[SemanticEvent],
) -> None:
    setup_orders = [item.setup_order for item in setup_history]
    event_orders = [item.event_order for item in event_history]
    if len(set(setup_orders)) != len(setup_orders):
        raise ValueError("setup history orders must be unique")
    if len(set(event_orders)) != len(event_orders):
        raise ValueError("semantic event history orders must be unique")


def _validate_result_link(
    decision: DecisionSlice,
    setup_history: Sequence[SetupCommitment],
    event_history: Sequence[SemanticEvent],
) -> None:
    result = decision.resulting_history
    if result.setup_commitment_id is not None:
        matches = [
            item for item in setup_history if item.commitment_id == result.setup_commitment_id
        ]
        if len(matches) != 1:
            raise ValueError("resulting setup commitment must resolve exactly once in history")
        if matches[0].setup_order != result.setup_order:
            raise ValueError("resulting setup order does not match authoritative history")
        return

    matches = [item for item in event_history if item.event_id == result.semantic_event_id]
    if len(matches) != 1:
        raise ValueError("resulting semantic event must resolve exactly once in history")
    if matches[0].event_order != result.event_order:
        raise ValueError("resulting event order does not match authoritative history")


def _validate_boundary_order_exists(
    boundary_order: int,
    existing_orders: Iterable[int],
    history_kind: str,
) -> None:
    if boundary_order == 0:
        return
    if boundary_order not in tuple(existing_orders):
        raise ValueError(f"{history_kind} prefix boundary must identify an existing history order")


def _validate_setup_prefix_order_evidence(
    setup_history: Sequence[SetupCommitment],
) -> None:
    if any(
        item.setup_order_basis is not SetupOrderBasis.EVIDENCED
        for item in setup_history
    ):
        raise ValueError(
            "setup-prefix materialization requires evidenced historical setup order"
        )
