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
G01_R01_SEED_FIXTURE = Path("docs/EL_ML1B_G01_DP_R01_CANONICAL_SEED_V1.json")
G01_R02_SEED_FIXTURE = Path("docs/EL_ML1B_G01_DP_R02_CANONICAL_SEED_V1.json")
G05_R03_SEED_FIXTURE = Path("docs/EL_ML1B_G05_DP_R03_CANONICAL_SEED_V1.json")
G05_R04_SEED_FIXTURE = Path("docs/EL_ML1B_G05_DP_R04_CANONICAL_SEED_V1.json")
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


def test_checked_in_g01_seeds_share_reconstruction_and_materialize_leak_free_prefixes() -> None:
    r01 = load_historical_decision_seed_v1(G01_R01_SEED_FIXTURE.read_text(encoding="utf-8"))
    r02 = load_historical_decision_seed_v1(G01_R02_SEED_FIXTURE.read_text(encoding="utf-8"))

    assert r01.game == r02.game
    assert r01.game.game_id == "evidence:e0:g01-a-stud-in-scarlet"
    assert r01.reconstruction_revision == r02.reconstruction_revision
    assert r01.storytellers == r02.storytellers
    assert r01.sources == r02.sources
    assert r01.setup_history == r02.setup_history
    assert r01.source_group == r02.source_group == "source-group:g01-a-stud-in-scarlet"
    assert r01.storyteller_independence_key == r02.storyteller_independence_key == "st-ben-burns"

    r01_setup, r01_events = materialize_historical_prefix(
        r01.decision, r01.setup_history, r01.event_history
    )
    assert [item.commitment_id for item in r01_setup] == ["setup:g01:shown-layout"]
    assert r01_events == ()
    assert r01.decision.observed_choice == {
        "selected_seat_id": "seat:g01:9",
        "shown_role": "EMPATH",
        "resulting_actual_role": "DRUNK",
    }
    assert r01.decision.rationale_assertion_ids is None
    assert r01.decision.explicitly_rejected_alternatives is None

    r02_setup, r02_events = materialize_historical_prefix(
        r02.decision, r02.setup_history, r02.event_history
    )
    assert [item.commitment_id for item in r02_setup] == [
        "setup:g01:shown-layout",
        "setup:g01:drunk-assignment",
        "setup:g01:red-herring",
    ]
    assert [item.event_id for item in r02_events] == ["event:g01:n1-chef-info"]
    assert r02.decision.observed_choice == 0
    assert r02.decision.explicitly_considered_alternatives is None
    assert [item.value for item in r02.decision.explicitly_rejected_alternatives or ()] == [2]

    encoded_r01 = dump_historical_decision_seed_v1(r01)
    encoded_r02 = dump_historical_decision_seed_v1(r02)
    assert (
        dump_historical_decision_seed_v1(load_historical_decision_seed_v1(encoded_r01))
        == encoded_r01
    )
    assert (
        dump_historical_decision_seed_v1(load_historical_decision_seed_v1(encoded_r02))
        == encoded_r02
    )


def test_checked_in_g05_seeds_share_reconstruction_and_preserve_intermediate_setup() -> None:
    r03 = load_historical_decision_seed_v1(G05_R03_SEED_FIXTURE.read_text(encoding="utf-8"))
    r04 = load_historical_decision_seed_v1(G05_R04_SEED_FIXTURE.read_text(encoding="utf-8"))

    assert r03.game == r04.game
    assert r03.game.game_id == "evidence:c1c:g05-a-fond-farewell"
    assert r03.reconstruction_revision == r04.reconstruction_revision
    assert r03.storytellers == r04.storytellers
    assert r03.sources == r04.sources
    assert r03.setup_history == r04.setup_history
    assert r03.storyteller_independence_key == r04.storyteller_independence_key == "st-ben-burns"
    assert len(r03.game_seats) == 20

    r03_setup, r03_events = materialize_historical_prefix(
        r03.decision, r03.setup_history, r03.event_history
    )
    assert [item.commitment_id for item in r03_setup] == ["setup:g05:pre-drunk-state"]
    assert r03_events == ()
    assert r03.decision.observed_choice == {
        "selected_seat_id": "seat:g05:12",
        "shown_role": "CHEF",
        "resulting_actual_role": "DRUNK",
    }
    assert r03.decision.explicitly_rejected_alternatives is None

    r04_setup, r04_events = materialize_historical_prefix(
        r04.decision, r04.setup_history, r04.event_history
    )
    assert [item.commitment_id for item in r04_setup] == [
        "setup:g05:pre-drunk-state",
        "setup:g05:drunk-assignment",
        "setup:g05:washerwoman-info",
    ]
    assert r04_events == ()
    assert r04.decision.observed_choice == {
        "selected_seat_id": "seat:g05:5",
        "shown_role": "UNDERTAKER",
        "red_herring": True,
    }
    assert r04.decision.explicitly_rejected_alternatives is None

    pre_drunk_state = r03_setup[0].value
    assert isinstance(pre_drunk_state, dict)
    seats = {item["seat_id"]: item for item in pre_drunk_state["seats"]}
    assert seats["seat:g05:12"]["shown_role"] == "CHEF"
    assert seats["seat:g05:14"]["traveller_alignment"] == "EVIL"
    assert seats["seat:g05:15"]["traveller_alignment"] == "GOOD"
    assert seats["seat:g05:17"]["traveller_alignment"] == "EVIL"

    encoded_r03 = dump_historical_decision_seed_v1(r03)
    encoded_r04 = dump_historical_decision_seed_v1(r04)
    assert (
        dump_historical_decision_seed_v1(load_historical_decision_seed_v1(encoded_r03))
        == encoded_r03
    )
    assert (
        dump_historical_decision_seed_v1(load_historical_decision_seed_v1(encoded_r04))
        == encoded_r04
    )


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

    by_id = {entry.benchmark_id: entry for entry in manifest.entries}
    g01_r01 = load_historical_decision_seed_v1(G01_R01_SEED_FIXTURE.read_text(encoding="utf-8"))
    g01_r02 = load_historical_decision_seed_v1(G01_R02_SEED_FIXTURE.read_text(encoding="utf-8"))
    g05_r03 = load_historical_decision_seed_v1(G05_R03_SEED_FIXTURE.read_text(encoding="utf-8"))
    g05_r04 = load_historical_decision_seed_v1(G05_R04_SEED_FIXTURE.read_text(encoding="utf-8"))
    for benchmark_id, checked_in_seed in (
        ("benchmark:el-ml1b:dp-r01", g01_r01),
        ("benchmark:el-ml1b:dp-r02", g01_r02),
        ("benchmark:el-ml1b:dp-r03", g05_r03),
        ("benchmark:el-ml1b:dp-r04", g05_r04),
    ):
        entry = by_id[benchmark_id]
        assert (
            entry.materialization_state is BenchmarkMaterializationState.CANONICAL_SEED_MATERIALIZED
        )
        assert entry.canonical_decision_id == checked_in_seed.decision.decision_id
        assert entry.prefix_materialization_ref == checked_in_seed.prefix_materialization_ref
        assert entry.observed_choice == checked_in_seed.decision.observed_choice
        assert entry.storyteller_independence_key == checked_in_seed.storyteller_independence_key

    remaining = [by_id["benchmark:el-ml1b:dp-r06"]]
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
