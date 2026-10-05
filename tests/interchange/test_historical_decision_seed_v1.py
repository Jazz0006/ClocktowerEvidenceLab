import json
from pathlib import Path

import pytest
from pydantic import ValidationError

from clocktower_evidence_lab.domain.decision import materialize_historical_prefix
from clocktower_evidence_lab.interchange.decision_point_benchmark_v1 import (
    BenchmarkMaterializationState,
    load_decision_point_benchmark_manifest_v1,
)
from clocktower_evidence_lab.interchange.historical_decision_seed_v1 import (
    HISTORICAL_DECISION_SEED_SCHEMA_NAME,
    HISTORICAL_DECISION_SEED_SCHEMA_VERSION,
    dump_historical_decision_seed_v1,
    load_historical_decision_seed_v1,
)

SEED_FIXTURE = Path("docs/EL_ML1B_G10_DP_R05_CANONICAL_SEED_V1.json")
MANIFEST_FIXTURE = Path("docs/EL_ML1B_READY_HISTORICAL_BENCHMARK_V1.json")


def _seed():
    return load_historical_decision_seed_v1(SEED_FIXTURE.read_text(encoding="utf-8"))


def test_checked_in_g10_dp_r05_seed_round_trips_and_materializes_leak_free_prefix() -> None:
    seed = _seed()

    assert seed.schema_name == HISTORICAL_DECISION_SEED_SCHEMA_NAME
    assert seed.schema_version == HISTORICAL_DECISION_SEED_SCHEMA_VERSION
    assert seed.game_group == "game-group:g10-game2"
    assert seed.source_group == "source-group:g10-megavoid-game2"
    assert seed.storyteller_independence_key == "st-the-megavoid"
    assert seed.decision.decision_id == "decision:g10:drunk-assignment"
    assert seed.decision.observed_choice == {
        "selected_seat_id": "seat:g10:1",
        "shown_role": "EMPATH",
        "resulting_actual_role": "DRUNK",
    }

    setup_prefix, event_prefix = materialize_historical_prefix(
        seed.decision,
        seed.setup_history,
        seed.event_history,
    )

    assert [item.commitment_id for item in setup_prefix] == ["setup:g10:shown-layout"]
    assert event_prefix == ()
    assert all(
        item.commitment_id != seed.decision.resulting_history.setup_commitment_id
        for item in setup_prefix
    )

    encoded = dump_historical_decision_seed_v1(seed)
    restored = load_historical_decision_seed_v1(encoded)
    assert dump_historical_decision_seed_v1(restored) == encoded


def test_g10_dp_r05_manifest_refs_are_backed_by_checked_in_seed() -> None:
    seed = _seed()
    manifest = load_decision_point_benchmark_manifest_v1(
        MANIFEST_FIXTURE.read_text(encoding="utf-8")
    )
    entries = {entry.benchmark_id: entry for entry in manifest.entries}

    materialized = entries["benchmark:el-ml1b:dp-r05"]
    assert (
        materialized.materialization_state
        is BenchmarkMaterializationState.CANONICAL_SEED_MATERIALIZED
    )
    assert materialized.canonical_decision_id == seed.decision.decision_id
    assert materialized.prefix_materialization_ref == seed.prefix_materialization_ref
    assert materialized.observed_choice == seed.decision.observed_choice
    assert materialized.game_group == seed.game_group
    assert materialized.source_group == seed.source_group
    assert materialized.storyteller_independence_key == seed.storyteller_independence_key

    remaining = [
        entry for entry in manifest.entries if entry.benchmark_id != "benchmark:el-ml1b:dp-r05"
    ]
    assert all(
        entry.materialization_state is BenchmarkMaterializationState.DOCUMENTED_READY
        for entry in remaining
    )
    assert all(entry.canonical_decision_id is None for entry in remaining)
    assert all(entry.prefix_materialization_ref is None for entry in remaining)


def test_seed_rejects_unresolved_rationale_provenance() -> None:
    payload = json.loads(SEED_FIXTURE.read_text(encoding="utf-8"))
    payload["decision"]["rationale_assertion_ids"] = ["assertion:g10:missing"]

    with pytest.raises(ValidationError, match="rationale assertion"):
        load_historical_decision_seed_v1(json.dumps(payload))


def test_seed_rejects_decision_prefix_that_includes_its_result() -> None:
    payload = json.loads(SEED_FIXTURE.read_text(encoding="utf-8"))
    payload["decision"]["historical_prefix_boundary"]["setup_through_order"] = 2

    with pytest.raises(ValidationError):
        load_historical_decision_seed_v1(json.dumps(payload))


def test_seed_rejects_history_provenance_for_the_wrong_subject() -> None:
    payload = json.loads(SEED_FIXTURE.read_text(encoding="utf-8"))
    payload["history_provenance"][0]["evidence_assertion_ids"] = [
        "assertion:g10:drunk-assignment-choice"
    ]

    with pytest.raises(ValidationError, match="history provenance assertion subject"):
        load_historical_decision_seed_v1(json.dumps(payload))


def test_seed_rejects_fragment_that_does_not_resolve_to_a_source() -> None:
    payload = json.loads(SEED_FIXTURE.read_text(encoding="utf-8"))
    payload["evidence_fragments"][0]["source_id"] = "source:g10:missing"

    with pytest.raises(ValidationError, match="fragment source"):
        load_historical_decision_seed_v1(json.dumps(payload))
