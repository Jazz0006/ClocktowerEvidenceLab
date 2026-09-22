"""Create the initial provenance-core working schema."""

from collections.abc import Sequence

import sqlalchemy as sa
from alembic import op

revision: str = "0001_provenance_core"
down_revision: str | None = None
branch_labels: str | Sequence[str] | None = None
depends_on: str | Sequence[str] | None = None


def upgrade() -> None:
    op.create_table(
        "sources",
        sa.Column("source_id", sa.String(length=128), primary_key=True),
        sa.Column("kind", sa.String(length=32), nullable=False),
        sa.Column("external_locator", sa.String(length=2048), nullable=False),
        sa.Column("inclusion_reason", sa.String(length=64), nullable=False),
        sa.Column("platform", sa.String(length=256), nullable=True),
        sa.Column("platform_source_id", sa.String(length=256), nullable=True),
        sa.Column("discovery_note", sa.String(length=4000), nullable=True),
        sa.Column("screening_status", sa.String(length=32), nullable=False),
        sa.Column("reconstructability", sa.String(length=32), nullable=False),
        sa.Column("selection_disposition", sa.String(length=32), nullable=False),
        sa.Column("rejection_reason", sa.String(length=4000), nullable=True),
        sa.CheckConstraint(
            "kind IN ('VIDEO', 'STRUCTURED_RECORD', 'POSTMORTEM', 'ARTICLE', 'OTHER')",
            name="ck_sources_kind",
        ),
        sa.CheckConstraint(
            "inclusion_reason IN ('EXPERT_SOURCE_CENSUS', 'SYSTEMATIC_SAMPLE', "
            "'RANDOM_SAMPLE', 'TARGETED_RESEARCH_CASE', 'COMMUNITY_SUBMISSION', "
            "'ALGORITHM_FAILURE_REPORT', 'OTHER')",
            name="ck_sources_inclusion_reason",
        ),
        sa.CheckConstraint(
            "screening_status IN ('NOT_SCREENED', 'SCREENED')",
            name="ck_sources_screening_status",
        ),
        sa.CheckConstraint(
            "reconstructability IN ('UNKNOWN', 'NOT_RECONSTRUCTABLE', 'PARTIAL', "
            "'RECONSTRUCTABLE')",
            name="ck_sources_reconstructability",
        ),
        sa.CheckConstraint(
            "selection_disposition IN ('UNDECIDED', 'SELECTED', 'REJECTED', 'DEFERRED')",
            name="ck_sources_selection_disposition",
        ),
        sa.CheckConstraint(
            "((selection_disposition = 'REJECTED' AND rejection_reason IS NOT NULL) "
            "OR (selection_disposition != 'REJECTED' AND rejection_reason IS NULL))",
            name="ck_sources_rejection_reason",
        ),
    )

    op.create_table(
        "evidence_fragments",
        sa.Column("fragment_id", sa.String(length=128), primary_key=True),
        sa.Column(
            "source_id",
            sa.String(length=128),
            sa.ForeignKey("sources.source_id", ondelete="RESTRICT"),
            nullable=False,
        ),
        sa.Column("locator_kind", sa.String(length=32), nullable=False),
        sa.Column("source_start_ms", sa.BigInteger(), nullable=True),
        sa.Column("source_end_ms", sa.BigInteger(), nullable=True),
        sa.Column("locator", sa.String(length=2048), nullable=True),
        sa.Column("note", sa.String(length=4000), nullable=True),
        sa.CheckConstraint(
            "locator_kind IN ('TIMESTAMP', 'TIMESTAMP_RANGE', 'FRAME', 'RECORD', "
            "'SECTION', 'OTHER')",
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
    op.create_index(
        "ix_evidence_fragments_source_id",
        "evidence_fragments",
        ["source_id"],
        unique=False,
    )

    op.create_table(
        "evidence_assertions",
        sa.Column("assertion_id", sa.String(length=128), primary_key=True),
        sa.Column("subject_type", sa.String(length=256), nullable=False),
        sa.Column("subject_id", sa.String(length=128), nullable=False),
        sa.Column("assertion_type", sa.String(length=256), nullable=False),
        sa.Column("value_json", sa.JSON(), nullable=False),
        sa.Column("derivation", sa.String(length=32), nullable=False),
        sa.Column("inference_reviewer_key", sa.String(length=128), nullable=True),
        sa.Column("inference_review_pass_id", sa.String(length=128), nullable=True),
        sa.Column("inference_note", sa.String(length=4000), nullable=True),
        sa.Column("scope", sa.String(length=32), nullable=False),
        sa.Column("reconstruction_revision_id", sa.String(length=128), nullable=True),
        sa.CheckConstraint(
            "derivation IN ('OBSERVED', 'RECONSTRUCTED', 'INFERRED', 'UNKNOWN', 'NOT_APPLICABLE')",
            name="ck_evidence_assertions_derivation",
        ),
        sa.CheckConstraint(
            "scope IN ('EVIDENCE', 'RECONSTRUCTION')",
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
    op.create_index(
        "ix_evidence_assertions_subject",
        "evidence_assertions",
        ["subject_type", "subject_id"],
        unique=False,
    )
    op.create_index(
        "ix_evidence_assertions_revision",
        "evidence_assertions",
        ["reconstruction_revision_id"],
        unique=False,
    )

    op.create_table(
        "assertion_fragments",
        sa.Column(
            "assertion_id",
            sa.String(length=128),
            sa.ForeignKey("evidence_assertions.assertion_id", ondelete="RESTRICT"),
            primary_key=True,
        ),
        sa.Column(
            "fragment_id",
            sa.String(length=128),
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
    op.create_index(
        "ix_assertion_fragments_fragment_id",
        "assertion_fragments",
        ["fragment_id"],
        unique=False,
    )


def downgrade() -> None:
    raise NotImplementedError("Clocktower Evidence Lab migrations are forward-only")
