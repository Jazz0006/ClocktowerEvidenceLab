"""Current SQLAlchemy Core schema for the provenance persistence boundary."""

from enum import StrEnum

import sqlalchemy as sa

from clocktower_evidence_lab.domain.primitives import Derivation
from clocktower_evidence_lab.domain.provenance import (
    AssertionScope,
    InclusionReason,
    Reconstructability,
    ScreeningStatus,
    SelectionDisposition,
    SourceKind,
    SourceLocatorKind,
)


def _sql_enum_values(enum_type: type[StrEnum]) -> str:
    return ", ".join(f"'{item.value}'" for item in enum_type)


metadata = sa.MetaData()

sources = sa.Table(
    "sources",
    metadata,
    sa.Column("source_id", sa.String(128), primary_key=True),
    sa.Column("kind", sa.String(32), nullable=False),
    sa.Column("external_locator", sa.String(2048), nullable=False),
    sa.Column("inclusion_reason", sa.String(64), nullable=False),
    sa.Column("platform", sa.String(256), nullable=True),
    sa.Column("platform_source_id", sa.String(256), nullable=True),
    sa.Column("discovery_note", sa.String(4000), nullable=True),
    sa.Column("screening_status", sa.String(32), nullable=False),
    sa.Column("reconstructability", sa.String(32), nullable=False),
    sa.Column("selection_disposition", sa.String(32), nullable=False),
    sa.Column("rejection_reason", sa.String(4000), nullable=True),
    sa.CheckConstraint(
        f"kind IN ({_sql_enum_values(SourceKind)})",
        name="ck_sources_kind",
    ),
    sa.CheckConstraint(
        f"inclusion_reason IN ({_sql_enum_values(InclusionReason)})",
        name="ck_sources_inclusion_reason",
    ),
    sa.CheckConstraint(
        f"screening_status IN ({_sql_enum_values(ScreeningStatus)})",
        name="ck_sources_screening_status",
    ),
    sa.CheckConstraint(
        f"reconstructability IN ({_sql_enum_values(Reconstructability)})",
        name="ck_sources_reconstructability",
    ),
    sa.CheckConstraint(
        f"selection_disposition IN ({_sql_enum_values(SelectionDisposition)})",
        name="ck_sources_selection_disposition",
    ),
    sa.CheckConstraint(
        "((selection_disposition = 'REJECTED' AND rejection_reason IS NOT NULL) "
        "OR (selection_disposition != 'REJECTED' AND rejection_reason IS NULL))",
        name="ck_sources_rejection_reason",
    ),
)

evidence_fragments = sa.Table(
    "evidence_fragments",
    metadata,
    sa.Column("fragment_id", sa.String(128), primary_key=True),
    sa.Column(
        "source_id",
        sa.String(128),
        sa.ForeignKey("sources.source_id", ondelete="RESTRICT"),
        nullable=False,
    ),
    sa.Column("locator_kind", sa.String(32), nullable=False),
    sa.Column("source_start_ms", sa.BigInteger(), nullable=True),
    sa.Column("source_end_ms", sa.BigInteger(), nullable=True),
    sa.Column("locator", sa.String(2048), nullable=True),
    sa.Column("note", sa.String(4000), nullable=True),
    sa.CheckConstraint(
        f"locator_kind IN ({_sql_enum_values(SourceLocatorKind)})",
        name="ck_evidence_fragments_locator_kind",
    ),
    sa.CheckConstraint(
        "source_start_ms IS NULL OR source_start_ms >= 0",
        name="ck_evidence_fragments_start_nonnegative",
    ),
    sa.CheckConstraint(
        "source_end_ms IS NULL OR source_end_ms >= 0",
        name="ck_evidence_fragments_end_nonnegative",
    ),
    sa.CheckConstraint(
        "source_end_ms IS NULL OR source_start_ms IS NOT NULL",
        name="ck_evidence_fragments_end_requires_start",
    ),
    sa.CheckConstraint(
        "source_end_ms IS NULL OR source_end_ms >= source_start_ms",
        name="ck_evidence_fragments_range_order",
    ),
    sa.CheckConstraint(
        "(locator_kind NOT IN ('TIMESTAMP', 'TIMESTAMP_RANGE') OR source_start_ms IS NOT NULL)",
        name="ck_evidence_fragments_timestamp_requires_start",
    ),
    sa.CheckConstraint(
        "(locator_kind != 'TIMESTAMP_RANGE' OR source_end_ms IS NOT NULL)",
        name="ck_evidence_fragments_range_requires_end",
    ),
    sa.CheckConstraint(
        "(locator_kind IN ('TIMESTAMP', 'TIMESTAMP_RANGE') OR locator IS NOT NULL)",
        name="ck_evidence_fragments_non_timestamp_requires_locator",
    ),
)
sa.Index("ix_evidence_fragments_source_id", evidence_fragments.c.source_id)

evidence_assertions = sa.Table(
    "evidence_assertions",
    metadata,
    sa.Column("assertion_id", sa.String(128), primary_key=True),
    sa.Column("subject_type", sa.String(256), nullable=False),
    sa.Column("subject_id", sa.String(128), nullable=False),
    sa.Column("assertion_type", sa.String(256), nullable=False),
    sa.Column("value_json", sa.JSON(), nullable=False),
    sa.Column("derivation", sa.String(32), nullable=False),
    sa.Column("inference_reviewer_key", sa.String(128), nullable=True),
    sa.Column("inference_review_pass_id", sa.String(128), nullable=True),
    sa.Column("inference_note", sa.String(4000), nullable=True),
    sa.Column("scope", sa.String(32), nullable=False),
    sa.Column("reconstruction_revision_id", sa.String(128), nullable=True),
    sa.CheckConstraint(
        f"derivation IN ({_sql_enum_values(Derivation)})",
        name="ck_evidence_assertions_derivation",
    ),
    sa.CheckConstraint(
        f"scope IN ({_sql_enum_values(AssertionScope)})",
        name="ck_evidence_assertions_scope",
    ),
    sa.CheckConstraint(
        "((derivation = 'INFERRED' AND inference_reviewer_key IS NOT NULL) "
        "OR (derivation != 'INFERRED' AND inference_reviewer_key IS NULL "
        "AND inference_review_pass_id IS NULL AND inference_note IS NULL))",
        name="ck_evidence_assertions_inference_provenance",
    ),
    sa.CheckConstraint(
        "((scope = 'RECONSTRUCTION' AND reconstruction_revision_id IS NOT NULL) "
        "OR (scope = 'EVIDENCE' AND reconstruction_revision_id IS NULL))",
        name="ck_evidence_assertions_revision_scope",
    ),
)
sa.Index(
    "ix_evidence_assertions_subject",
    evidence_assertions.c.subject_type,
    evidence_assertions.c.subject_id,
)
sa.Index(
    "ix_evidence_assertions_revision",
    evidence_assertions.c.reconstruction_revision_id,
)

assertion_fragments = sa.Table(
    "assertion_fragments",
    metadata,
    sa.Column(
        "assertion_id",
        sa.String(128),
        sa.ForeignKey("evidence_assertions.assertion_id", ondelete="RESTRICT"),
        primary_key=True,
    ),
    sa.Column(
        "fragment_id",
        sa.String(128),
        sa.ForeignKey("evidence_fragments.fragment_id", ondelete="RESTRICT"),
        primary_key=True,
    ),
    sa.Column("fragment_order", sa.Integer(), nullable=False),
    sa.UniqueConstraint(
        "assertion_id",
        "fragment_order",
        name="uq_assertion_fragments_assertion_order",
    ),
    sa.CheckConstraint(
        "fragment_order >= 0",
        name="ck_assertion_fragments_order_nonnegative",
    ),
)
sa.Index("ix_assertion_fragments_fragment_id", assertion_fragments.c.fragment_id)
