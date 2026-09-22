"""Versioned JSON interchange for the E1 provenance core."""

from datetime import datetime
from typing import Literal

from pydantic import BaseModel, ConfigDict, model_validator

from clocktower_evidence_lab.domain.provenance import (
    EvidenceAssertion,
    EvidenceFragment,
    Source,
)

PROVENANCE_SCHEMA_NAME = "clocktower-evidence-provenance"
PROVENANCE_SCHEMA_VERSION = 1


class ProvenanceBundleV1(BaseModel):
    """Durable version-1 provenance bundle independent of SQLite layout."""

    model_config = ConfigDict(extra="forbid", frozen=True)

    schema_name: Literal["clocktower-evidence-provenance"] = PROVENANCE_SCHEMA_NAME
    schema_version: Literal[1] = PROVENANCE_SCHEMA_VERSION
    exported_at: datetime
    sources: tuple[Source, ...] = ()
    evidence_fragments: tuple[EvidenceFragment, ...] = ()
    assertions: tuple[EvidenceAssertion, ...] = ()

    @model_validator(mode="after")
    def _validate_bundle(self) -> "ProvenanceBundleV1":
        if self.exported_at.tzinfo is None or self.exported_at.utcoffset() is None:
            raise ValueError("exported_at must be timezone-aware")

        source_ids = [item.source_id for item in self.sources]
        fragment_ids = [item.fragment_id for item in self.evidence_fragments]
        assertion_ids = [item.assertion_id for item in self.assertions]

        _require_unique("source", source_ids)
        _require_unique("evidence fragment", fragment_ids)
        _require_unique("assertion", assertion_ids)

        source_id_set = set(source_ids)
        for fragment in self.evidence_fragments:
            if fragment.source_id not in source_id_set:
                raise ValueError(
                    f"evidence fragment {fragment.fragment_id} references missing source "
                    f"{fragment.source_id}"
                )

        fragment_id_set = set(fragment_ids)
        for assertion in self.assertions:
            missing = [item for item in assertion.fragment_ids if item not in fragment_id_set]
            if missing:
                raise ValueError(
                    f"assertion {assertion.assertion_id} references missing evidence fragments: "
                    + ", ".join(missing)
                )

        return self


def _require_unique(label: str, semantic_ids: list[str]) -> None:
    if len(set(semantic_ids)) != len(semantic_ids):
        raise ValueError(f"duplicate {label} semantic ID")


def _canonical_bundle(bundle: ProvenanceBundleV1) -> ProvenanceBundleV1:
    return bundle.model_copy(
        update={
            "sources": tuple(sorted(bundle.sources, key=lambda item: item.source_id)),
            "evidence_fragments": tuple(
                sorted(bundle.evidence_fragments, key=lambda item: item.fragment_id)
            ),
            "assertions": tuple(sorted(bundle.assertions, key=lambda item: item.assertion_id)),
        }
    )


def dump_provenance_bundle(bundle: ProvenanceBundleV1) -> str:
    """Serialize one provenance bundle deterministically for the same semantic content."""

    canonical = _canonical_bundle(bundle)
    return canonical.model_dump_json(
        by_alias=False,
        exclude_none=False,
        round_trip=True,
    )


def load_provenance_bundle(encoded: str) -> ProvenanceBundleV1:
    """Load and strictly validate a version-1 provenance bundle."""

    return ProvenanceBundleV1.model_validate_json(encoded)
