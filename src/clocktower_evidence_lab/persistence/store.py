"""Append-only SQLAlchemy Core persistence for the provenance domain."""

from pathlib import Path
from typing import Any

import sqlalchemy as sa
from sqlalchemy import Engine, event

from clocktower_evidence_lab.domain.primitives import Derivation, SemanticId
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
from clocktower_evidence_lab.persistence.schema import (
    assertion_fragments,
    evidence_assertions,
    evidence_fragments,
    sources,
)


def _enable_sqlite_foreign_keys(dbapi_connection: Any, _connection_record: Any) -> None:
    cursor = dbapi_connection.cursor()
    try:
        cursor.execute("PRAGMA foreign_keys=ON")
    finally:
        cursor.close()


def create_sqlite_engine(database_path: str | Path) -> Engine:
    """Create the application-owned SQLite engine with FK enforcement enabled."""

    path = Path(database_path).resolve()
    engine = sa.create_engine(f"sqlite:///{path.as_posix()}")
    event.listen(engine, "connect", _enable_sqlite_foreign_keys)
    return engine


class SQLiteProvenanceStore:
    """Append-only persistence adapter for Source, Fragment and Assertion."""

    def __init__(self, engine: Engine) -> None:
        self.engine = engine

    def insert_source(self, source: Source) -> None:
        with self.engine.begin() as connection:
            connection.execute(
                sources.insert().values(
                    source_id=source.source_id,
                    kind=source.kind.value,
                    external_locator=source.external_locator,
                    inclusion_reason=source.inclusion_reason.value,
                    platform=source.platform,
                    platform_source_id=source.platform_source_id,
                    discovery_note=source.discovery_note,
                    screening_status=source.screening_status.value,
                    reconstructability=source.reconstructability.value,
                    selection_disposition=source.selection_disposition.value,
                    rejection_reason=source.rejection_reason,
                )
            )

    def get_source(self, source_id: SemanticId) -> Source | None:
        with self.engine.connect() as connection:
            row = (
                connection.execute(
                    sa.select(sources).where(sources.c.source_id == source_id)
                )
                .mappings()
                .one_or_none()
            )

        if row is None:
            return None

        return Source(
            source_id=row["source_id"],
            kind=SourceKind(row["kind"]),
            external_locator=row["external_locator"],
            inclusion_reason=InclusionReason(row["inclusion_reason"]),
            platform=row["platform"],
            platform_source_id=row["platform_source_id"],
            discovery_note=row["discovery_note"],
            screening_status=ScreeningStatus(row["screening_status"]),
            reconstructability=Reconstructability(row["reconstructability"]),
            selection_disposition=SelectionDisposition(row["selection_disposition"]),
            rejection_reason=row["rejection_reason"],
        )

    def insert_fragment(self, fragment: EvidenceFragment) -> None:
        with self.engine.begin() as connection:
            connection.execute(
                evidence_fragments.insert().values(
                    fragment_id=fragment.fragment_id,
                    source_id=fragment.source_id,
                    locator_kind=fragment.locator_kind.value,
                    source_start_ms=fragment.source_start_ms,
                    source_end_ms=fragment.source_end_ms,
                    locator=fragment.locator,
                    note=fragment.note,
                )
            )

    def get_fragment(self, fragment_id: SemanticId) -> EvidenceFragment | None:
        with self.engine.connect() as connection:
            row = (
                connection.execute(
                    sa.select(evidence_fragments).where(
                        evidence_fragments.c.fragment_id == fragment_id
                    )
                )
                .mappings()
                .one_or_none()
            )

        if row is None:
            return None

        return EvidenceFragment(
            fragment_id=row["fragment_id"],
            source_id=row["source_id"],
            locator_kind=SourceLocatorKind(row["locator_kind"]),
            source_start_ms=row["source_start_ms"],
            source_end_ms=row["source_end_ms"],
            locator=row["locator"],
            note=row["note"],
        )

    def insert_assertion(self, assertion: EvidenceAssertion) -> None:
        inference = assertion.inference_provenance

        with self.engine.begin() as connection:
            connection.execute(
                evidence_assertions.insert().values(
                    assertion_id=assertion.assertion_id,
                    subject_type=assertion.subject_type,
                    subject_id=assertion.subject_id,
                    assertion_type=assertion.assertion_type,
                    value_json=assertion.value,
                    derivation=assertion.derivation.value,
                    inference_reviewer_key=(
                        inference.reviewer_key if inference is not None else None
                    ),
                    inference_review_pass_id=(
                        inference.review_pass_id if inference is not None else None
                    ),
                    inference_note=inference.note if inference is not None else None,
                    scope=assertion.scope.value,
                    reconstruction_revision_id=assertion.reconstruction_revision_id,
                )
            )
            connection.execute(
                assertion_fragments.insert(),
                [
                    {
                        "assertion_id": assertion.assertion_id,
                        "fragment_id": fragment_id,
                        "fragment_order": order,
                    }
                    for order, fragment_id in enumerate(assertion.fragment_ids)
                ],
            )

    def get_assertion(self, assertion_id: SemanticId) -> EvidenceAssertion | None:
        with self.engine.connect() as connection:
            row = (
                connection.execute(
                    sa.select(evidence_assertions).where(
                        evidence_assertions.c.assertion_id == assertion_id
                    )
                )
                .mappings()
                .one_or_none()
            )
            if row is None:
                return None

            fragment_ids = tuple(
                connection.execute(
                    sa.select(assertion_fragments.c.fragment_id)
                    .where(assertion_fragments.c.assertion_id == assertion_id)
                    .order_by(assertion_fragments.c.fragment_order)
                ).scalars()
            )

        inference_provenance = None
        if row["inference_reviewer_key"] is not None:
            inference_provenance = InferenceProvenance(
                reviewer_key=row["inference_reviewer_key"],
                review_pass_id=row["inference_review_pass_id"],
                note=row["inference_note"],
            )

        return EvidenceAssertion(
            assertion_id=row["assertion_id"],
            subject_type=row["subject_type"],
            subject_id=row["subject_id"],
            assertion_type=row["assertion_type"],
            value=row["value_json"],
            derivation=Derivation(row["derivation"]),
            fragment_ids=fragment_ids,
            inference_provenance=inference_provenance,
            scope=AssertionScope(row["scope"]),
            reconstruction_revision_id=row["reconstruction_revision_id"],
        )
