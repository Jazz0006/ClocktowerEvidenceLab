import json
from datetime import UTC, datetime

import pytest
from pydantic import ValidationError

from clocktower_evidence_lab.domain.primitives import Derivation
from clocktower_evidence_lab.domain.provenance import (
    AssertionScope,
    EvidenceAssertion,
    EvidenceFragment,
    InclusionReason,
    InferenceProvenance,
    Reconstructability,
    ScreeningStatus,
    SelectionDisposition,
    Source,
    SourceKind,
    SourceLocatorKind,
)
from clocktower_evidence_lab.interchange.provenance_v1 import (
    PROVENANCE_SCHEMA_NAME,
    PROVENANCE_SCHEMA_VERSION,
    ProvenanceBundleV1,
    dump_provenance_bundle,
    load_provenance_bundle,
)

EXPORTED_AT = datetime(2026, 9, 22, 12, 0, tzinfo=UTC)


def _source(source_id: str = "source:youtube:example") -> Source:
    return Source(
        source_id=source_id,
        kind=SourceKind.VIDEO,
        platform="youtube",
        platform_source_id=source_id.rsplit(":", 1)[-1],
        external_locator=f"https://example.test/{source_id}",
        inclusion_reason=InclusionReason.EXPERT_SOURCE_CENSUS,
        screening_status=ScreeningStatus.SCREENED,
        reconstructability=Reconstructability.PARTIAL,
        selection_disposition=SelectionDisposition.SELECTED,
    )


def _fragment(
    fragment_id: str = "fragment:example:001",
    source_id: str = "source:youtube:example",
    start_ms: int = 100_000,
) -> EvidenceFragment:
    return EvidenceFragment(
        fragment_id=fragment_id,
        source_id=source_id,
        locator_kind=SourceLocatorKind.TIMESTAMP_RANGE,
        source_start_ms=start_ms,
        source_end_ms=start_ms + 2_500,
        note="Concise evidence note.",
    )


def _inferred_assertion(
    assertion_id: str = "assertion:example:inferred",
    fragment_ids: tuple[str, ...] = ("fragment:example:001",),
) -> EvidenceAssertion:
    return EvidenceAssertion(
        assertion_id=assertion_id,
        subject_type="INTERACTION",
        subject_id="interaction:game1:ft1",
        assertion_type="REGISTRATION_WITNESS",
        value={"witness": "RECLUSE_AS_DEMON", "confidence_note": None},
        derivation=Derivation.INFERRED,
        fragment_ids=fragment_ids,
        inference_provenance=InferenceProvenance(
            reviewer_key="reviewer:human:1",
            review_pass_id="review-pass:e1-5",
            note="Reviewer inference only.",
        ),
        scope=AssertionScope.RECONSTRUCTION,
        reconstruction_revision_id="revision:game1:1",
    )


def test_provenance_bundle_round_trip_preserves_semantic_evidence() -> None:
    source = _source()
    first = _fragment()
    second = _fragment("fragment:example:002", start_ms=200_000)
    inferred = _inferred_assertion(fragment_ids=(second.fragment_id, first.fragment_id))
    unknown = EvidenceAssertion(
        assertion_id="assertion:example:unknown",
        subject_type="INTERACTION",
        subject_id="interaction:game1:ft1",
        assertion_type="SOURCE_OBSERVED_REGISTRATION_WITNESS",
        value=None,
        derivation=Derivation.UNKNOWN,
        fragment_ids=(first.fragment_id,),
    )

    bundle = ProvenanceBundleV1(
        exported_at=EXPORTED_AT,
        sources=(source,),
        evidence_fragments=(first, second),
        assertions=(inferred, unknown),
    )

    encoded = dump_provenance_bundle(bundle)
    restored = load_provenance_bundle(encoded)

    assert restored == bundle
    assert restored.schema_name == PROVENANCE_SCHEMA_NAME
    assert restored.schema_version == PROVENANCE_SCHEMA_VERSION
    assert restored.assertions[0].derivation is Derivation.INFERRED
    assert restored.assertions[1].derivation is Derivation.UNKNOWN
    assert restored.assertions[0].fragment_ids == (second.fragment_id, first.fragment_id)


def test_serialized_contract_is_domain_shaped_not_sqlite_shaped() -> None:
    source = _source()
    fragment = _fragment()
    assertion = _inferred_assertion()

    encoded = dump_provenance_bundle(
        ProvenanceBundleV1(
            exported_at=EXPORTED_AT,
            sources=(source,),
            evidence_fragments=(fragment,),
            assertions=(assertion,),
        )
    )
    payload = json.loads(encoded)

    assert payload["schema_name"] == "clocktower-evidence-provenance"
    assert payload["schema_version"] == 1
    assert "value" in payload["assertions"][0]
    assert "value_json" not in payload["assertions"][0]
    assert "fragment_ids" in payload["assertions"][0]
    assert "fragment_order" not in payload["assertions"][0]
    assert "verification" not in payload["assertions"][0]
    assert "historical_phase" not in payload["evidence_fragments"][0]


def test_canonical_json_does_not_depend_on_input_collection_order() -> None:
    first_source = _source("source:youtube:a")
    second_source = _source("source:youtube:b")
    first_fragment = _fragment("fragment:a", first_source.source_id, 100_000)
    second_fragment = _fragment("fragment:b", second_source.source_id, 200_000)
    first_assertion = EvidenceAssertion(
        assertion_id="assertion:a",
        subject_type="SOURCE",
        subject_id=first_source.source_id,
        assertion_type="TITLE",
        value="A",
        derivation=Derivation.RECONSTRUCTED,
        fragment_ids=(first_fragment.fragment_id,),
    )
    second_assertion = EvidenceAssertion(
        assertion_id="assertion:b",
        subject_type="SOURCE",
        subject_id=second_source.source_id,
        assertion_type="TITLE",
        value="B",
        derivation=Derivation.RECONSTRUCTED,
        fragment_ids=(second_fragment.fragment_id,),
    )

    forward = ProvenanceBundleV1(
        exported_at=EXPORTED_AT,
        sources=(first_source, second_source),
        evidence_fragments=(first_fragment, second_fragment),
        assertions=(first_assertion, second_assertion),
    )
    reverse = ProvenanceBundleV1(
        exported_at=EXPORTED_AT,
        sources=(second_source, first_source),
        evidence_fragments=(second_fragment, first_fragment),
        assertions=(second_assertion, first_assertion),
    )

    assert dump_provenance_bundle(forward) == dump_provenance_bundle(reverse)


@pytest.mark.parametrize(
    ("collection_name", "items"),
    [
        ("sources", (_source(), _source())),
        ("evidence_fragments", (_fragment(), _fragment())),
        (
            "assertions",
            (
                _inferred_assertion(),
                _inferred_assertion(),
            ),
        ),
    ],
)
def test_duplicate_semantic_ids_are_rejected(collection_name: str, items: tuple) -> None:
    kwargs = {
        "exported_at": EXPORTED_AT,
        "sources": (_source(),),
        "evidence_fragments": (_fragment(),),
        "assertions": (_inferred_assertion(),),
    }
    kwargs[collection_name] = items

    with pytest.raises(ValidationError):
        ProvenanceBundleV1(**kwargs)


def test_orphan_fragment_source_reference_is_rejected() -> None:
    with pytest.raises(ValidationError):
        ProvenanceBundleV1(
            exported_at=EXPORTED_AT,
            sources=(_source(),),
            evidence_fragments=(_fragment(source_id="source:missing"),),
            assertions=(),
        )


def test_orphan_assertion_fragment_reference_is_rejected() -> None:
    with pytest.raises(ValidationError):
        ProvenanceBundleV1(
            exported_at=EXPORTED_AT,
            sources=(_source(),),
            evidence_fragments=(_fragment(),),
            assertions=(_inferred_assertion(fragment_ids=("fragment:missing",)),),
        )


def test_unsupported_schema_version_is_rejected_on_import() -> None:
    bundle = ProvenanceBundleV1(
        exported_at=EXPORTED_AT,
        sources=(_source(),),
        evidence_fragments=(_fragment(),),
        assertions=(_inferred_assertion(),),
    )
    payload = json.loads(dump_provenance_bundle(bundle))
    payload["schema_version"] = 2

    with pytest.raises(ValidationError):
        load_provenance_bundle(json.dumps(payload))


def test_exported_at_must_be_timezone_aware() -> None:
    with pytest.raises(ValidationError):
        ProvenanceBundleV1(
            exported_at=datetime(2026, 9, 22, 12, 0),
            sources=(),
            evidence_fragments=(),
            assertions=(),
        )
