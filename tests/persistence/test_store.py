from pathlib import Path

import pytest
from alembic import command
from alembic.config import Config
from sqlalchemy.exc import IntegrityError

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
from clocktower_evidence_lab.persistence.store import (
    SQLiteProvenanceStore,
    create_sqlite_engine,
)

ROOT = Path(__file__).resolve().parents[2]


def _migrated_store(tmp_path: Path) -> SQLiteProvenanceStore:
    database_path = tmp_path / "evidence.sqlite"
    config = Config(str(ROOT / "alembic.ini"))
    config.set_main_option("script_location", str(ROOT / "migrations"))
    config.set_main_option("sqlalchemy.url", f"sqlite:///{database_path.as_posix()}")
    command.upgrade(config, "head")
    return SQLiteProvenanceStore(create_sqlite_engine(database_path))


def _source() -> Source:
    return Source(
        source_id="source:youtube:example",
        kind=SourceKind.VIDEO,
        platform="youtube",
        platform_source_id="example",
        external_locator="https://example.test/watch/example",
        inclusion_reason=InclusionReason.EXPERT_SOURCE_CENSUS,
        discovery_note="Discovered through a complete expert-source census.",
        screening_status=ScreeningStatus.SCREENED,
        reconstructability=Reconstructability.PARTIAL,
        selection_disposition=SelectionDisposition.SELECTED,
    )


def _fragment(fragment_id: str, start_ms: int) -> EvidenceFragment:
    return EvidenceFragment(
        fragment_id=fragment_id,
        source_id="source:youtube:example",
        locator_kind=SourceLocatorKind.TIMESTAMP_RANGE,
        source_start_ms=start_ms,
        source_end_ms=start_ms + 3_000,
        note="Concise source evidence note.",
    )


def test_sqlite_connection_owner_enables_foreign_keys(tmp_path: Path) -> None:
    store = _migrated_store(tmp_path)

    with store.engine.connect() as connection:
        assert connection.exec_driver_sql("PRAGMA foreign_keys").scalar_one() == 1


def test_source_round_trip_preserves_independent_workflow_dimensions(tmp_path: Path) -> None:
    store = _migrated_store(tmp_path)
    source = _source()

    store.insert_source(source)

    assert store.get_source(source.source_id) == source


def test_fragment_round_trip_preserves_source_locator_time(tmp_path: Path) -> None:
    store = _migrated_store(tmp_path)
    source = _source()
    fragment = _fragment("fragment:example:001", 632_000)

    store.insert_source(source)
    store.insert_fragment(fragment)

    assert store.get_fragment(fragment.fragment_id) == fragment


def test_assertion_round_trip_preserves_status_scope_json_and_inference(tmp_path: Path) -> None:
    store = _migrated_store(tmp_path)
    source = _source()
    fragments = (
        _fragment("fragment:example:001", 632_000),
        _fragment("fragment:example:002", 900_000),
        _fragment("fragment:example:003", 910_000),
    )
    assertions = (
        EvidenceAssertion(
            assertion_id="assertion:observed",
            subject_type="INTERACTION",
            subject_id="interaction:game1:ft1",
            assertion_type="DELIVERED_RESULT",
            value={"result": "YES", "targets": ["seat:game1:2", "seat:game1:4"]},
            derivation=Derivation.OBSERVED,
            fragment_ids=(fragments[0].fragment_id,),
        ),
        EvidenceAssertion(
            assertion_id="assertion:source-title",
            subject_type="SOURCE",
            subject_id=source.source_id,
            assertion_type="TITLE",
            value="Example game",
            derivation=Derivation.RECONSTRUCTED,
            fragment_ids=(fragments[1].fragment_id, fragments[0].fragment_id),
        ),
        EvidenceAssertion(
            assertion_id="assertion:inferred",
            subject_type="INTERACTION",
            subject_id="interaction:game1:ft1",
            assertion_type="REGISTRATION_WITNESS",
            value="RECLUSE_AS_DEMON",
            derivation=Derivation.INFERRED,
            fragment_ids=(fragments[0].fragment_id, fragments[2].fragment_id),
            inference_provenance=InferenceProvenance(
                reviewer_key="reviewer:human:1",
                review_pass_id="review-pass:e1-4",
                note="Reviewer interpretation, not source-observed.",
            ),
            scope=AssertionScope.RECONSTRUCTION,
            reconstruction_revision_id="revision:game1:1",
        ),
        EvidenceAssertion(
            assertion_id="assertion:unknown",
            subject_type="INTERACTION",
            subject_id="interaction:game1:ft1",
            assertion_type="SOURCE_OBSERVED_REGISTRATION_WITNESS",
            value=None,
            derivation=Derivation.UNKNOWN,
            fragment_ids=(fragments[0].fragment_id,),
        ),
    )

    store.insert_source(source)
    for fragment in fragments:
        store.insert_fragment(fragment)
    for assertion in assertions:
        store.insert_assertion(assertion)

    for assertion in assertions:
        assert store.get_assertion(assertion.assertion_id) == assertion


def test_many_to_many_fragment_links_preserve_assertion_order(tmp_path: Path) -> None:
    store = _migrated_store(tmp_path)
    source = _source()
    first = _fragment("fragment:example:first", 100_000)
    shared = _fragment("fragment:example:shared", 200_000)
    last = _fragment("fragment:example:last", 300_000)

    first_assertion = EvidenceAssertion(
        assertion_id="assertion:first",
        subject_type="GAME",
        subject_id="game:1",
        assertion_type="FIRST_FACT",
        value=1,
        derivation=Derivation.OBSERVED,
        fragment_ids=(shared.fragment_id, first.fragment_id),
    )
    second_assertion = EvidenceAssertion(
        assertion_id="assertion:second",
        subject_type="GAME",
        subject_id="game:1",
        assertion_type="SECOND_FACT",
        value=2,
        derivation=Derivation.OBSERVED,
        fragment_ids=(last.fragment_id, shared.fragment_id),
    )

    store.insert_source(source)
    for fragment in (first, shared, last):
        store.insert_fragment(fragment)
    store.insert_assertion(first_assertion)
    store.insert_assertion(second_assertion)

    assert store.get_assertion(first_assertion.assertion_id).fragment_ids == (
        shared.fragment_id,
        first.fragment_id,
    )
    assert store.get_assertion(second_assertion.assertion_id).fragment_ids == (
        last.fragment_id,
        shared.fragment_id,
    )


def test_foreign_keys_reject_orphan_fragment(tmp_path: Path) -> None:
    store = _migrated_store(tmp_path)
    orphan = EvidenceFragment(
        fragment_id="fragment:orphan",
        source_id="source:missing",
        locator_kind=SourceLocatorKind.TIMESTAMP,
        source_start_ms=1_000,
    )

    with pytest.raises(IntegrityError):
        store.insert_fragment(orphan)


def test_assertion_insert_is_atomic_when_fragment_reference_is_missing(tmp_path: Path) -> None:
    store = _migrated_store(tmp_path)
    assertion = EvidenceAssertion(
        assertion_id="assertion:orphan-link",
        subject_type="GAME",
        subject_id="game:1",
        assertion_type="FACT",
        value=True,
        derivation=Derivation.OBSERVED,
        fragment_ids=("fragment:missing",),
    )

    with pytest.raises(IntegrityError):
        store.insert_assertion(assertion)

    assert store.get_assertion(assertion.assertion_id) is None
