"""Core provenance entities for external evidence collection."""

from datetime import date
from enum import StrEnum
from typing import Annotated

from pydantic import BaseModel, ConfigDict, Field, JsonValue, model_validator

from clocktower_evidence_lab.domain.primitives import Derivation, SemanticId

ShortText = Annotated[str, Field(min_length=1, max_length=256)]
LongText = Annotated[str, Field(min_length=1, max_length=4_000)]
SourceMillis = Annotated[int, Field(ge=0)]


class _DomainModel(BaseModel):
    model_config = ConfigDict(extra="forbid", frozen=True)


class SourceKind(StrEnum):
    VIDEO = "VIDEO"
    STRUCTURED_RECORD = "STRUCTURED_RECORD"
    POSTMORTEM = "POSTMORTEM"
    ARTICLE = "ARTICLE"
    OTHER = "OTHER"


class InclusionReason(StrEnum):
    EXPERT_SOURCE_CENSUS = "EXPERT_SOURCE_CENSUS"
    SYSTEMATIC_SAMPLE = "SYSTEMATIC_SAMPLE"
    RANDOM_SAMPLE = "RANDOM_SAMPLE"
    TARGETED_RESEARCH_CASE = "TARGETED_RESEARCH_CASE"
    COMMUNITY_SUBMISSION = "COMMUNITY_SUBMISSION"
    ALGORITHM_FAILURE_REPORT = "ALGORITHM_FAILURE_REPORT"
    OTHER = "OTHER"


class ScreeningStatus(StrEnum):
    NOT_SCREENED = "NOT_SCREENED"
    SCREENED = "SCREENED"


class Reconstructability(StrEnum):
    UNKNOWN = "UNKNOWN"
    NOT_RECONSTRUCTABLE = "NOT_RECONSTRUCTABLE"
    PARTIAL = "PARTIAL"
    RECONSTRUCTABLE = "RECONSTRUCTABLE"


class SelectionDisposition(StrEnum):
    UNDECIDED = "UNDECIDED"
    SELECTED = "SELECTED"
    REJECTED = "REJECTED"
    DEFERRED = "DEFERRED"


class SourceLocatorKind(StrEnum):
    TIMESTAMP = "TIMESTAMP"
    TIMESTAMP_RANGE = "TIMESTAMP_RANGE"
    FRAME = "FRAME"
    RECORD = "RECORD"
    SECTION = "SECTION"
    OTHER = "OTHER"


class Source(_DomainModel):
    """A discoverable evidence source and its collection-workflow state."""

    source_id: SemanticId
    kind: SourceKind
    external_locator: ShortText
    inclusion_reason: InclusionReason
    platform: ShortText | None = None
    title: ShortText | None = None
    publisher: ShortText | None = None
    published_on: date | None = None
    discovery_note: LongText | None = None
    screening_status: ScreeningStatus = ScreeningStatus.NOT_SCREENED
    reconstructability: Reconstructability = Reconstructability.UNKNOWN
    selection_disposition: SelectionDisposition = SelectionDisposition.UNDECIDED
    rejection_reason: LongText | None = None

    @model_validator(mode="after")
    def _validate_rejection(self) -> "Source":
        if self.selection_disposition is SelectionDisposition.REJECTED:
            if self.rejection_reason is None:
                raise ValueError("rejected source requires rejection_reason")
        elif self.rejection_reason is not None:
            raise ValueError("rejection_reason is only valid for rejected sources")
        return self


class EvidenceFragment(_DomainModel):
    """A locator into a source, never a historical semantic-time record."""

    fragment_id: SemanticId
    source_id: SemanticId
    locator_kind: SourceLocatorKind
    source_start_ms: SourceMillis | None = None
    source_end_ms: SourceMillis | None = None
    locator: ShortText | None = None
    note: LongText | None = None

    @model_validator(mode="after")
    def _validate_locator(self) -> "EvidenceFragment":
        if self.source_end_ms is not None and self.source_start_ms is None:
            raise ValueError("source_end_ms requires source_start_ms")
        if (
            self.source_start_ms is not None
            and self.source_end_ms is not None
            and self.source_end_ms < self.source_start_ms
        ):
            raise ValueError("source_end_ms must not precede source_start_ms")

        if self.locator_kind in {SourceLocatorKind.TIMESTAMP, SourceLocatorKind.TIMESTAMP_RANGE}:
            if self.source_start_ms is None:
                raise ValueError("timestamp locator requires source_start_ms")
        elif self.locator is None:
            raise ValueError("non-timestamp locator requires locator")

        if self.locator_kind is SourceLocatorKind.TIMESTAMP_RANGE and self.source_end_ms is None:
            raise ValueError("timestamp range requires source_end_ms")
        return self


class InferenceProvenance(_DomainModel):
    """Reviewer provenance for a claim that is explicitly an inference."""

    reviewer_key: ShortText
    review_pass_id: SemanticId | None = None
    note: LongText | None = None


class EvidenceAssertion(_DomainModel):
    """A structured claim linked to one or more source fragments."""

    assertion_id: SemanticId
    subject_type: ShortText
    subject_id: SemanticId
    assertion_type: ShortText
    value: JsonValue
    derivation: Derivation
    fragment_ids: tuple[SemanticId, ...]
    inference_provenance: InferenceProvenance | None = None
    reconstruction_revision_id: SemanticId | None = None

    @model_validator(mode="after")
    def _validate_provenance(self) -> "EvidenceAssertion":
        if not self.fragment_ids:
            raise ValueError("assertion requires at least one evidence fragment")
        if len(set(self.fragment_ids)) != len(self.fragment_ids):
            raise ValueError("assertion evidence fragment IDs must be unique")

        if self.derivation is Derivation.INFERRED:
            if self.inference_provenance is None:
                raise ValueError("inferred assertion requires inference_provenance")
        elif self.inference_provenance is not None:
            raise ValueError("inference_provenance is only valid for inferred assertions")

        if (
            self.derivation is Derivation.RECONSTRUCTED
            and self.reconstruction_revision_id is None
        ):
            raise ValueError("reconstructed assertion requires reconstruction_revision_id")
        if (
            self.derivation is Derivation.OBSERVED
            and self.reconstruction_revision_id is not None
        ):
            raise ValueError("observed assertion cannot be reconstruction-revision scoped")
        return self
