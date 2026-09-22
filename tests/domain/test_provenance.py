import pytest
from pydantic import ValidationError

from clocktower_evidence_lab.domain.primitives import Derivation, Verification
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


def test_source_workflow_dimensions_remain_independent() -> None:
    source = Source(
        source_id="source:youtube:example",
        kind=SourceKind.VIDEO,
        platform="youtube",
        platform_source_id="example",
        external_locator="https://example.test/watch/example",
        inclusion_reason=InclusionReason.EXPERT_SOURCE_CENSUS,
        screening_status=ScreeningStatus.SCREENED,
        reconstructability=Reconstructability.PARTIAL,
        selection_disposition=SelectionDisposition.REJECTED,
        rejection_reason="Night decisions are edited out.",
    )

    assert source.screening_status is ScreeningStatus.SCREENED
    assert source.reconstructability is Reconstructability.PARTIAL
    assert source.selection_disposition is SelectionDisposition.REJECTED
    assert source.rejection_reason == "Night decisions are edited out."


def test_source_does_not_duplicate_evidentiary_metadata_fields() -> None:
    with pytest.raises(ValidationError):
        Source(
            source_id="source:youtube:metadata-duplication",
            kind=SourceKind.VIDEO,
            platform="youtube",
            platform_source_id="metadata-duplication",
            external_locator="https://example.test/watch/metadata-duplication",
            inclusion_reason=InclusionReason.SYSTEMATIC_SAMPLE,
            title="This belongs in an EvidenceAssertion.",
        )


def test_rejected_source_requires_rejection_reason() -> None:
    with pytest.raises(ValidationError):
        Source(
            source_id="source:youtube:rejected",
            kind=SourceKind.VIDEO,
            external_locator="rejected",
            inclusion_reason=InclusionReason.SYSTEMATIC_SAMPLE,
            selection_disposition=SelectionDisposition.REJECTED,
        )


def test_evidence_fragment_timestamp_is_source_locator_only() -> None:
    fragment = EvidenceFragment(
        fragment_id="fragment:example:001",
        source_id="source:youtube:example",
        locator_kind=SourceLocatorKind.TIMESTAMP_RANGE,
        source_start_ms=632_000,
        source_end_ms=635_000,
        note="Storyteller explains the visible result.",
    )

    assert fragment.source_start_ms == 632_000
    assert fragment.source_end_ms == 635_000

    with pytest.raises(ValidationError):
        EvidenceFragment(
            fragment_id="fragment:example:bad",
            source_id="source:youtube:example",
            locator_kind=SourceLocatorKind.TIMESTAMP,
            source_start_ms=632_000,
            historical_phase="NIGHT_1",
        )


def test_evidence_fragment_rejects_invalid_source_range() -> None:
    with pytest.raises(ValidationError):
        EvidenceFragment(
            fragment_id="fragment:example:range",
            source_id="source:youtube:example",
            locator_kind=SourceLocatorKind.TIMESTAMP_RANGE,
            source_start_ms=635_000,
            source_end_ms=632_000,
        )


def test_assertions_support_many_to_many_fragment_provenance() -> None:
    actual_role = EvidenceAssertion(
        assertion_id="assertion:seat4:actual-role",
        subject_type="GAME_SEAT",
        subject_id="seat:game1:4",
        assertion_type="ACTUAL_ROLE",
        value="RECLUSE",
        derivation=Derivation.RECONSTRUCTED,
        fragment_ids=("fragment:setup:frame", "fragment:review:role"),
        scope=AssertionScope.RECONSTRUCTION,
        reconstruction_revision_id="revision:game1:1",
    )
    visible_result = EvidenceAssertion(
        assertion_id="assertion:ft:result",
        subject_type="INTERACTION",
        subject_id="interaction:game1:ft1",
        assertion_type="DELIVERED_RESULT",
        value={"result": "YES"},
        derivation=Derivation.OBSERVED,
        fragment_ids=("fragment:review:role",),
    )

    assert actual_role.fragment_ids == ("fragment:setup:frame", "fragment:review:role")
    assert visible_result.fragment_ids == ("fragment:review:role",)


def test_reconstruction_scoped_assertion_requires_explicit_revision_id() -> None:
    with pytest.raises(ValidationError):
        EvidenceAssertion(
            assertion_id="assertion:reconstruction-without-revision",
            subject_type="GAME_SEAT",
            subject_id="seat:game1:4",
            assertion_type="ACTUAL_ROLE",
            value="RECLUSE",
            derivation=Derivation.RECONSTRUCTED,
            fragment_ids=("fragment:setup:frame", "fragment:review:role"),
            scope=AssertionScope.RECONSTRUCTION,
        )


def test_reconstructed_source_metadata_is_not_forced_into_game_revision() -> None:
    assertion = EvidenceAssertion(
        assertion_id="assertion:source:title",
        subject_type="SOURCE",
        subject_id="source:youtube:example",
        assertion_type="TITLE",
        value="Example game",
        derivation=Derivation.RECONSTRUCTED,
        fragment_ids=("fragment:index:title",),
    )

    assert assertion.scope is AssertionScope.EVIDENCE
    assert assertion.reconstruction_revision_id is None


def test_assertion_requires_nonempty_unique_fragment_provenance() -> None:
    with pytest.raises(ValidationError):
        EvidenceAssertion(
            assertion_id="assertion:no-provenance",
            subject_type="GAME",
            subject_id="game:1",
            assertion_type="TABLE_CONTEXT",
            value="BEGINNER",
            derivation=Derivation.OBSERVED,
            fragment_ids=(),
        )

    with pytest.raises(ValidationError):
        EvidenceAssertion(
            assertion_id="assertion:duplicate-provenance",
            subject_type="GAME",
            subject_id="game:1",
            assertion_type="TABLE_CONTEXT",
            value="BEGINNER",
            derivation=Derivation.OBSERVED,
            fragment_ids=("fragment:1", "fragment:1"),
        )


def test_reviewer_inference_stays_inferred_and_requires_provenance() -> None:
    with pytest.raises(ValidationError):
        EvidenceAssertion(
            assertion_id="assertion:registration",
            subject_type="INTERACTION",
            subject_id="interaction:game1:ft1",
            assertion_type="REGISTRATION_WITNESS",
            value="RECLUSE_AS_DEMON",
            derivation=Derivation.INFERRED,
            fragment_ids=("fragment:ft:yes",),
        )

    assertion = EvidenceAssertion(
        assertion_id="assertion:registration",
        subject_type="INTERACTION",
        subject_id="interaction:game1:ft1",
        assertion_type="REGISTRATION_WITNESS",
        value="RECLUSE_AS_DEMON",
        derivation=Derivation.INFERRED,
        fragment_ids=("fragment:ft:yes",),
        inference_provenance=InferenceProvenance(
            reviewer_key="reviewer:human:1",
            review_pass_id="review-pass:e0-primary-1",
            note="Reviewer interpretation; not stated by the source.",
        ),
    )

    assert assertion.derivation is Derivation.INFERRED
    assert assertion.inference_provenance is not None


def test_inferred_assertion_may_be_revision_scoped_without_changing_derivation() -> None:
    assertion = EvidenceAssertion(
        assertion_id="assertion:revision-inference",
        subject_type="INTERACTION",
        subject_id="interaction:game1:ft1",
        assertion_type="REGISTRATION_WITNESS",
        value="RECLUSE_AS_DEMON",
        derivation=Derivation.INFERRED,
        fragment_ids=("fragment:ft:yes",),
        inference_provenance=InferenceProvenance(
            reviewer_key="reviewer:human:1",
            review_pass_id="review-pass:e0-primary-1",
        ),
        scope=AssertionScope.RECONSTRUCTION,
        reconstruction_revision_id="revision:game1:1",
    )

    assert assertion.derivation is Derivation.INFERRED
    assert assertion.reconstruction_revision_id == "revision:game1:1"


def test_evidence_scoped_assertion_cannot_be_silently_given_revision_id() -> None:
    with pytest.raises(ValidationError):
        EvidenceAssertion(
            assertion_id="assertion:observed-revision-leak",
            subject_type="GAME",
            subject_id="game:1",
            assertion_type="TABLE_CONTEXT",
            value="BEGINNER",
            derivation=Derivation.OBSERVED,
            fragment_ids=("fragment:context",),
            reconstruction_revision_id="revision:game1:1",
        )


def test_verification_is_not_an_independently_writable_assertion_field() -> None:
    with pytest.raises(ValidationError):
        EvidenceAssertion(
            assertion_id="assertion:verified-too-early",
            subject_type="GAME",
            subject_id="game:1",
            assertion_type="TABLE_CONTEXT",
            value="BEGINNER",
            derivation=Derivation.OBSERVED,
            fragment_ids=("fragment:context",),
            verification=Verification.VERIFIED,
        )
