import json
from pathlib import Path

import pytest
from pydantic import ValidationError

from clocktower_evidence_lab.domain.primitives import Verification
from clocktower_evidence_lab.interchange.decision_point_benchmark_v1 import (
    BENCHMARK_SCHEMA_NAME,
    BENCHMARK_SCHEMA_VERSION,
    BenchmarkMaterializationState,
    BenchmarkReadiness,
    DecisionPointBenchmarkEntryV1,
    DecisionPointBenchmarkManifestV1,
    EvaluationMode,
    dump_decision_point_benchmark_manifest_v1,
    load_decision_point_benchmark_manifest_v1,
)


def _entry(
    benchmark_id: str = "benchmark:el-ml1b:dp-r01",
    game_group: str = "game-group:g01",
) -> DecisionPointBenchmarkEntryV1:
    return DecisionPointBenchmarkEntryV1(
        benchmark_id=benchmark_id,
        decision_family="DRUNK_ASSIGNMENT",
        game_group=game_group,
        source_group="source-group:a-stud-in-scarlet",
        storyteller_independence_key=None,
        historical_evidence_refs=(
            "docs/C1C_TARGETED_DRUNK_ASSIGNMENT_ACQUISITION_2026-09-28.md#G01",
        ),
        observed_choice={"shown_role": "Empath", "actual_role": "Drunk"},
        verification=Verification.VERIFIED,
        readiness=BenchmarkReadiness.READY,
        materialization_state=BenchmarkMaterializationState.DOCUMENTED_READY,
        allowed_evaluation_modes=(EvaluationMode.OBSERVED_CHOICE_RANK,),
        host_enrichment_requirements=("LEGAL_CANDIDATE_DOMAIN",),
    )


def test_manifest_round_trip_preserves_benchmark_semantics() -> None:
    manifest = DecisionPointBenchmarkManifestV1(
        manifest_id="benchmark-manifest:el-ml1b-ready-v1",
        entries=(_entry(),),
    )

    encoded = dump_decision_point_benchmark_manifest_v1(manifest)
    restored = load_decision_point_benchmark_manifest_v1(encoded)

    assert restored == manifest
    assert restored.schema_name == BENCHMARK_SCHEMA_NAME
    assert restored.schema_version == BENCHMARK_SCHEMA_VERSION
    assert restored.entries[0].verification is Verification.VERIFIED


def test_manifest_serialization_is_canonical_by_benchmark_id() -> None:
    first = _entry("benchmark:el-ml1b:dp-r01", "game-group:g01")
    second = _entry("benchmark:el-ml1b:dp-r02", "game-group:g01")

    forward = DecisionPointBenchmarkManifestV1(
        manifest_id="benchmark-manifest:el-ml1b-ready-v1",
        entries=(first, second),
    )
    reverse = DecisionPointBenchmarkManifestV1(
        manifest_id="benchmark-manifest:el-ml1b-ready-v1",
        entries=(second, first),
    )

    assert dump_decision_point_benchmark_manifest_v1(forward) == (
        dump_decision_point_benchmark_manifest_v1(reverse)
    )


def test_duplicate_benchmark_ids_are_rejected() -> None:
    with pytest.raises(ValidationError):
        DecisionPointBenchmarkManifestV1(
            manifest_id="benchmark-manifest:el-ml1b-ready-v1",
            entries=(_entry(), _entry()),
        )


def test_documented_ready_does_not_require_fabricated_canonical_ids() -> None:
    entry = _entry()

    assert entry.canonical_decision_id is None
    assert entry.prefix_materialization_ref is None


def test_materialized_seed_requires_canonical_decision_and_prefix_refs() -> None:
    payload = _entry().model_dump()
    payload["materialization_state"] = BenchmarkMaterializationState.CANONICAL_SEED_MATERIALIZED

    with pytest.raises(ValidationError):
        DecisionPointBenchmarkEntryV1(**payload)


def test_materialized_seed_accepts_canonical_refs_when_present() -> None:
    payload = _entry().model_dump()
    payload.update(
        {
            "materialization_state": BenchmarkMaterializationState.CANONICAL_SEED_MATERIALIZED,
            "canonical_decision_id": "decision:g01:drunk-assignment",
            "prefix_materialization_ref": "prefix:g01:before-drunk-assignment",
        }
    )

    entry = DecisionPointBenchmarkEntryV1(**payload)

    assert entry.canonical_decision_id == "decision:g01:drunk-assignment"


def test_evidence_refs_and_evaluation_modes_must_not_be_empty() -> None:
    payload = _entry().model_dump()
    payload["historical_evidence_refs"] = ()
    with pytest.raises(ValidationError):
        DecisionPointBenchmarkEntryV1(**payload)

    payload = _entry().model_dump()
    payload["allowed_evaluation_modes"] = ()
    with pytest.raises(ValidationError):
        DecisionPointBenchmarkEntryV1(**payload)


def test_unsupported_schema_version_is_rejected() -> None:
    manifest = DecisionPointBenchmarkManifestV1(
        manifest_id="benchmark-manifest:el-ml1b-ready-v1",
        entries=(_entry(),),
    )
    payload = json.loads(dump_decision_point_benchmark_manifest_v1(manifest))
    payload["schema_version"] = 2

    with pytest.raises(ValidationError):
        load_decision_point_benchmark_manifest_v1(json.dumps(payload))


def test_checked_in_el_ml1b_ready_manifest_preserves_conservative_inventory() -> None:
    encoded = Path("docs/EL_ML1B_READY_HISTORICAL_BENCHMARK_V1.json").read_text(encoding="utf-8")
    manifest = load_decision_point_benchmark_manifest_v1(encoded)

    assert len(manifest.entries) == 6
    assert {entry.game_group for entry in manifest.entries} == {
        "game-group:g01",
        "game-group:g05",
        "game-group:g10-game2",
    }
    assert all(entry.readiness is BenchmarkReadiness.READY for entry in manifest.entries)
    assert all(
        entry.materialization_state is BenchmarkMaterializationState.DOCUMENTED_READY
        for entry in manifest.entries
    )
    assert all(entry.canonical_decision_id is None for entry in manifest.entries)
    assert all(entry.prefix_materialization_ref is None for entry in manifest.entries)
