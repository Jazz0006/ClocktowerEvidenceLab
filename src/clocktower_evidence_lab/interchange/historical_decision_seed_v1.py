"""Versioned derived materialization for one canonical historical Storyteller decision."""

from collections.abc import Iterable
from typing import Literal

from pydantic import BaseModel, ConfigDict, model_validator

from clocktower_evidence_lab.domain.decision import (
    DecisionSlice,
    materialize_historical_prefix,
)
from clocktower_evidence_lab.domain.history import (
    SemanticEvent,
    SetupCommitment,
    SourceGameLink,
    SourceGameMatchStatus,
)
from clocktower_evidence_lab.domain.primitives import SemanticId, Verification
from clocktower_evidence_lab.domain.provenance import (
    AssertionScope,
    EvidenceAssertion,
    EvidenceFragment,
    Source,
)
from clocktower_evidence_lab.domain.reconstruction import (
    Game,
    GameSeat,
    ReconstructionRevision,
    Storyteller,
)

HISTORICAL_DECISION_SEED_SCHEMA_NAME = "clocktower-historical-decision-seed"
HISTORICAL_DECISION_SEED_SCHEMA_VERSION = 1


class _InterchangeModel(BaseModel):
    model_config = ConfigDict(extra="forbid", frozen=True)


class HistoricalItemProvenanceV1(_InterchangeModel):
    """Evidence assertions supporting one authoritative history item."""

    history_item_id: SemanticId
    evidence_assertion_ids: tuple[SemanticId, ...]

    @model_validator(mode="after")
    def _validate_assertions(self) -> "HistoricalItemProvenanceV1":
        if not self.evidence_assertion_ids:
            raise ValueError("history provenance requires at least one evidence assertion")
        _require_unique("history provenance assertion ID", self.evidence_assertion_ids)
        return self


class HistoricalDecisionSeedV1(_InterchangeModel):
    """Derived, leak-free materialization backed by canonical evidence-domain objects."""

    schema_name: Literal["clocktower-historical-decision-seed"] = (
        HISTORICAL_DECISION_SEED_SCHEMA_NAME
    )
    schema_version: Literal[1] = HISTORICAL_DECISION_SEED_SCHEMA_VERSION

    materialization_id: SemanticId
    prefix_materialization_ref: SemanticId

    game_group: SemanticId
    source_group: SemanticId
    storyteller_independence_key: SemanticId | None = None

    game: Game
    reconstruction_revision: ReconstructionRevision
    storytellers: tuple[Storyteller, ...]
    game_seats: tuple[GameSeat, ...]

    sources: tuple[Source, ...]
    source_game_links: tuple[SourceGameLink, ...]
    evidence_fragments: tuple[EvidenceFragment, ...]
    evidence_assertions: tuple[EvidenceAssertion, ...]

    setup_history: tuple[SetupCommitment, ...]
    event_history: tuple[SemanticEvent, ...]
    history_provenance: tuple[HistoricalItemProvenanceV1, ...]

    decision: DecisionSlice
    observed_choice_assertion_ids: tuple[SemanticId, ...]
    choice_verification: Verification

    @model_validator(mode="after")
    def _validate_seed(self) -> "HistoricalDecisionSeedV1":
        game_id = self.game.game_id
        revision_id = self.reconstruction_revision.revision_id

        if self.reconstruction_revision.game_id != game_id:
            raise ValueError("reconstruction revision must belong to seed game")
        if self.game.current_reconstruction_revision_id != revision_id:
            raise ValueError("seed game must point at the materialized reconstruction revision")
        if self.decision.game_id != game_id:
            raise ValueError("decision must belong to seed game")
        if self.decision.reconstruction_revision_id != revision_id:
            raise ValueError("decision must use the materialized reconstruction revision")
        if self.decision.observed_choice is None:
            raise ValueError("historical decision seed requires an observed choice")

        storyteller_ids = tuple(item.storyteller_id for item in self.storytellers)
        _require_unique("Storyteller ID", storyteller_ids)
        storyteller_by_id = {item.storyteller_id: item for item in self.storytellers}
        for assignment in self.game.storyteller_assignments:
            if assignment.storyteller_id not in storyteller_by_id:
                raise ValueError("game Storyteller assignment must resolve in seed storytellers")
        if self.storyteller_independence_key is not None and not any(
            item.independence_key == self.storyteller_independence_key for item in self.storytellers
        ):
            raise ValueError("Storyteller independence key must resolve in seed storytellers")

        seat_ids = tuple(item.seat_id for item in self.game_seats)
        _require_unique("game seat ID", seat_ids)
        seat_id_set = set(seat_ids)
        for seat in self.game_seats:
            if seat.game_id != game_id:
                raise ValueError("game seat must belong to seed game")
        if (
            self.decision.subject_seat_id is not None
            and self.decision.subject_seat_id not in seat_id_set
        ):
            raise ValueError("decision subject seat must resolve in seed game seats")

        source_ids = tuple(item.source_id for item in self.sources)
        _require_unique("source ID", source_ids)
        source_id_set = set(source_ids)

        link_ids = tuple(item.link_id for item in self.source_game_links)
        _require_unique("source-game link ID", link_ids)
        for link in self.source_game_links:
            if link.game_id != game_id:
                raise ValueError("source-game link must point at seed game")
            if link.source_id not in source_id_set:
                raise ValueError("source-game link source must resolve in seed sources")
            if link.match_status is not SourceGameMatchStatus.VERIFIED_SAME:
                raise ValueError(
                    "canonical historical seed requires VERIFIED_SAME source-game links"
                )

        fragment_ids = tuple(item.fragment_id for item in self.evidence_fragments)
        _require_unique("evidence fragment ID", fragment_ids)
        fragment_id_set = set(fragment_ids)
        for fragment in self.evidence_fragments:
            if fragment.source_id not in source_id_set:
                raise ValueError("evidence fragment source must resolve in seed sources")

        assertion_ids = tuple(item.assertion_id for item in self.evidence_assertions)
        _require_unique("evidence assertion ID", assertion_ids)
        assertion_by_id = {item.assertion_id: item for item in self.evidence_assertions}
        for assertion in self.evidence_assertions:
            if any(fragment_id not in fragment_id_set for fragment_id in assertion.fragment_ids):
                raise ValueError("evidence assertion fragment must resolve in seed fragments")
            if (
                assertion.scope is AssertionScope.RECONSTRUCTION
                and assertion.reconstruction_revision_id != revision_id
            ):
                raise ValueError(
                    "reconstruction-scoped assertion must use seed reconstruction revision"
                )

        for item in self.setup_history:
            _validate_seat_refs(
                seat_id_set,
                subject_seat_id=item.subject_seat_id,
                target_seat_ids=item.target_seat_ids,
                label="setup history",
            )
        for item in self.event_history:
            _validate_seat_refs(
                seat_id_set,
                actor_seat_id=item.actor_seat_id,
                subject_seat_id=item.subject_seat_id,
                target_seat_ids=item.target_seat_ids,
                label="event history",
            )

        history_items = (*self.setup_history, *self.event_history)
        history_item_ids = tuple(
            item.commitment_id if isinstance(item, SetupCommitment) else item.event_id
            for item in history_items
        )
        _require_unique("history item ID", history_item_ids)
        history_item_id_set = set(history_item_ids)

        provenance_ids = tuple(item.history_item_id for item in self.history_provenance)
        _require_unique("history provenance item ID", provenance_ids)
        if set(provenance_ids) != history_item_id_set:
            raise ValueError("every seed history item requires exactly one provenance record")
        for item in self.history_provenance:
            _require_resolved_assertions(
                "history provenance",
                item.evidence_assertion_ids,
                assertion_by_id,
            )
            _require_assertion_subject(
                "history provenance",
                item.evidence_assertion_ids,
                item.history_item_id,
                assertion_by_id,
            )

        _require_resolved_assertions(
            "observed choice",
            self.observed_choice_assertion_ids,
            assertion_by_id,
        )
        if not self.observed_choice_assertion_ids:
            raise ValueError("historical decision seed requires observed-choice provenance")
        _require_assertion_subject(
            "observed choice",
            self.observed_choice_assertion_ids,
            self.decision.decision_id,
            assertion_by_id,
        )
        if not any(
            assertion_by_id[assertion_id].value == self.decision.observed_choice
            for assertion_id in self.observed_choice_assertion_ids
        ):
            raise ValueError("observed-choice provenance must support the decision observed choice")

        if self.decision.rationale_assertion_ids is not None:
            _require_resolved_assertions(
                "rationale",
                self.decision.rationale_assertion_ids,
                assertion_by_id,
            )
            _require_assertion_subject(
                "rationale",
                self.decision.rationale_assertion_ids,
                self.decision.decision_id,
                assertion_by_id,
            )

        for alternatives in (
            self.decision.explicitly_considered_alternatives,
            self.decision.explicitly_rejected_alternatives,
        ):
            if alternatives is None:
                continue
            for alternative in alternatives:
                _require_resolved_assertions(
                    "explicit alternative",
                    alternative.evidence_assertion_ids,
                    assertion_by_id,
                )
                _require_assertion_subject(
                    "explicit alternative",
                    alternative.evidence_assertion_ids,
                    self.decision.decision_id,
                    assertion_by_id,
                )

        # This validates history identity/order/result linkage and the no-hindsight boundary.
        materialize_historical_prefix(
            self.decision,
            self.setup_history,
            self.event_history,
        )

        return self


def _require_unique(label: str, values: Iterable[object]) -> None:
    materialized = tuple(values)
    if len(set(materialized)) != len(materialized):
        raise ValueError(f"duplicate {label}")


def _require_resolved_assertions(
    label: str,
    assertion_ids: tuple[SemanticId, ...],
    assertion_by_id: dict[SemanticId, EvidenceAssertion],
) -> None:
    missing = tuple(
        assertion_id for assertion_id in assertion_ids if assertion_id not in assertion_by_id
    )
    if missing:
        raise ValueError(f"{label} assertion must resolve in seed evidence assertions")


def _require_assertion_subject(
    label: str,
    assertion_ids: tuple[SemanticId, ...],
    expected_subject_id: SemanticId,
    assertion_by_id: dict[SemanticId, EvidenceAssertion],
) -> None:
    if any(
        assertion_by_id[assertion_id].subject_id != expected_subject_id
        for assertion_id in assertion_ids
    ):
        raise ValueError(f"{label} assertion subject must match referenced object")


def _validate_seat_refs(
    seat_id_set: set[SemanticId],
    *,
    label: str,
    actor_seat_id: SemanticId | None = None,
    subject_seat_id: SemanticId | None = None,
    target_seat_ids: tuple[SemanticId, ...] = (),
) -> None:
    referenced = tuple(
        seat_id
        for seat_id in (actor_seat_id, subject_seat_id, *target_seat_ids)
        if seat_id is not None
    )
    if any(seat_id not in seat_id_set for seat_id in referenced):
        raise ValueError(f"{label} seat reference must resolve in seed game seats")


def _canonical_seed(seed: HistoricalDecisionSeedV1) -> HistoricalDecisionSeedV1:
    return seed.model_copy(
        update={
            "storytellers": tuple(sorted(seed.storytellers, key=lambda item: item.storyteller_id)),
            "game_seats": tuple(
                sorted(
                    seed.game_seats,
                    key=lambda item: (
                        item.seat_order is None,
                        item.seat_order or 0,
                        item.seat_id,
                    ),
                )
            ),
            "sources": tuple(sorted(seed.sources, key=lambda item: item.source_id)),
            "source_game_links": tuple(
                sorted(seed.source_game_links, key=lambda item: item.link_id)
            ),
            "evidence_fragments": tuple(
                sorted(seed.evidence_fragments, key=lambda item: item.fragment_id)
            ),
            "evidence_assertions": tuple(
                sorted(seed.evidence_assertions, key=lambda item: item.assertion_id)
            ),
            "setup_history": tuple(sorted(seed.setup_history, key=lambda item: item.setup_order)),
            "event_history": tuple(sorted(seed.event_history, key=lambda item: item.event_order)),
            "history_provenance": tuple(
                sorted(seed.history_provenance, key=lambda item: item.history_item_id)
            ),
        }
    )


def dump_historical_decision_seed_v1(seed: HistoricalDecisionSeedV1) -> str:
    """Serialize deterministically for the same semantic seed."""

    return _canonical_seed(seed).model_dump_json(
        by_alias=False,
        exclude_none=False,
        round_trip=True,
    )


def load_historical_decision_seed_v1(encoded: str) -> HistoricalDecisionSeedV1:
    """Strictly load and validate one historical-decision seed V1."""

    return HistoricalDecisionSeedV1.model_validate_json(encoded)
