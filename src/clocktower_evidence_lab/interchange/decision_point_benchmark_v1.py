"""Versioned derived manifest for recommendation decision-point benchmarks."""

from enum import StrEnum
from typing import Annotated, Literal

from pydantic import BaseModel, ConfigDict, Field, JsonValue, model_validator

from clocktower_evidence_lab.domain.primitives import SemanticId, Verification

BENCHMARK_SCHEMA_NAME = "clocktower-decision-point-benchmark"
BENCHMARK_SCHEMA_VERSION = 1

ShortText = Annotated[str, Field(min_length=1, max_length=256)]
EvidenceRef = Annotated[str, Field(min_length=1, max_length=512)]


class BenchmarkReadiness(StrEnum):
    """Evidence-side readiness for downstream benchmark construction."""

    READY = "READY"
    PARTIAL = "PARTIAL"
    NOT_USABLE = "NOT_USABLE"


class BenchmarkMaterializationState(StrEnum):
    """Whether documented evidence has a canonical machine-readable seed yet."""

    DOCUMENTED_READY = "DOCUMENTED_READY"
    CANONICAL_SEED_MATERIALIZED = "CANONICAL_SEED_MATERIALIZED"


class EvaluationMode(StrEnum):
    """Evaluation shapes supported by source-backed evidence for one point."""

    LEGALITY = "LEGALITY"
    OBSERVED_CHOICE_RANK = "OBSERVED_CHOICE_RANK"
    EXPLICIT_PAIRWISE_PREFERENCE = "EXPLICIT_PAIRWISE_PREFERENCE"
    RATIONALE_BLIND_REVIEW = "RATIONALE_BLIND_REVIEW"
    COUNTERFACTUAL_SENSITIVITY = "COUNTERFACTUAL_SENSITIVITY"


class _InterchangeModel(BaseModel):
    model_config = ConfigDict(extra="forbid", frozen=True)


class DecisionPointBenchmarkEntryV1(_InterchangeModel):
    """One derived benchmark inventory row; canonical evidence remains authoritative."""

    benchmark_id: SemanticId
    evidence_kind: Literal["HISTORICAL_DECISION"] = "HISTORICAL_DECISION"
    decision_family: ShortText

    game_group: SemanticId
    source_group: SemanticId
    storyteller_independence_key: SemanticId | None = None

    historical_evidence_refs: tuple[EvidenceRef, ...]
    observed_choice: JsonValue | None = None
    verification: Verification

    readiness: BenchmarkReadiness
    materialization_state: BenchmarkMaterializationState
    canonical_decision_id: SemanticId | None = None
    prefix_materialization_ref: SemanticId | None = None

    rationale_evidence_refs: tuple[EvidenceRef, ...] = ()
    explicit_preference_evidence_refs: tuple[EvidenceRef, ...] = ()
    explicit_rejection_evidence_refs: tuple[EvidenceRef, ...] = ()
    allowed_evaluation_modes: tuple[EvaluationMode, ...]
    host_enrichment_requirements: tuple[ShortText, ...] = ()

    @model_validator(mode="after")
    def _validate_entry(self) -> "DecisionPointBenchmarkEntryV1":
        if not self.historical_evidence_refs:
            raise ValueError("benchmark entry requires at least one historical evidence reference")
        if not self.allowed_evaluation_modes:
            raise ValueError("benchmark entry requires at least one evaluation mode")

        _require_unique("historical evidence reference", self.historical_evidence_refs)
        _require_unique("rationale evidence reference", self.rationale_evidence_refs)
        _require_unique(
            "explicit preference evidence reference", self.explicit_preference_evidence_refs
        )
        _require_unique(
            "explicit rejection evidence reference", self.explicit_rejection_evidence_refs
        )
        _require_unique("evaluation mode", self.allowed_evaluation_modes)
        _require_unique("Host enrichment requirement", self.host_enrichment_requirements)

        if self.materialization_state is BenchmarkMaterializationState.CANONICAL_SEED_MATERIALIZED:
            if self.canonical_decision_id is None or self.prefix_materialization_ref is None:
                raise ValueError(
                    "materialized canonical seed requires decision and prefix materialization refs"
                )
        elif self.canonical_decision_id is not None or self.prefix_materialization_ref is not None:
            raise ValueError(
                "documented-ready entry cannot claim canonical decision/prefix materialization"
            )

        return self


class DecisionPointBenchmarkManifestV1(_InterchangeModel):
    """Deterministic manifest of benchmark inventory rows."""

    schema_name: Literal["clocktower-decision-point-benchmark"] = BENCHMARK_SCHEMA_NAME
    schema_version: Literal[1] = BENCHMARK_SCHEMA_VERSION
    manifest_id: SemanticId
    entries: tuple[DecisionPointBenchmarkEntryV1, ...]

    @model_validator(mode="after")
    def _validate_manifest(self) -> "DecisionPointBenchmarkManifestV1":
        benchmark_ids = tuple(entry.benchmark_id for entry in self.entries)
        _require_unique("benchmark ID", benchmark_ids)
        return self


def _require_unique(label: str, values: tuple) -> None:
    if len(set(values)) != len(values):
        raise ValueError(f"duplicate {label}")


def _canonical_manifest(
    manifest: DecisionPointBenchmarkManifestV1,
) -> DecisionPointBenchmarkManifestV1:
    return manifest.model_copy(
        update={
            "entries": tuple(sorted(manifest.entries, key=lambda item: item.benchmark_id)),
        }
    )


def dump_decision_point_benchmark_manifest_v1(
    manifest: DecisionPointBenchmarkManifestV1,
) -> str:
    """Serialize deterministically for the same semantic manifest content."""

    return _canonical_manifest(manifest).model_dump_json(
        by_alias=False,
        exclude_none=False,
        round_trip=True,
    )


def load_decision_point_benchmark_manifest_v1(
    encoded: str,
) -> DecisionPointBenchmarkManifestV1:
    """Strictly load one decision-point benchmark manifest V1."""

    return DecisionPointBenchmarkManifestV1.model_validate_json(encoded)
