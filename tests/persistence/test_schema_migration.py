from pathlib import Path

from alembic import command
from alembic.config import Config
from sqlalchemy import create_engine, inspect, text

from clocktower_evidence_lab.persistence.schema import metadata

ROOT = Path(__file__).resolve().parents[2]
EXPECTED_TABLES = {
    "sources",
    "evidence_fragments",
    "evidence_assertions",
    "assertion_fragments",
}


def _upgrade_empty_database(database_path: Path):
    config = Config(str(ROOT / "alembic.ini"))
    config.set_main_option("script_location", str(ROOT / "migrations"))
    config.set_main_option("sqlalchemy.url", f"sqlite:///{database_path.as_posix()}")
    command.upgrade(config, "head")
    return create_engine(f"sqlite:///{database_path.as_posix()}")


def _schema_signature(engine) -> tuple:
    inspector = inspect(engine)
    signature = []

    for table_name in sorted(EXPECTED_TABLES):
        columns = tuple(
            (
                column["name"],
                str(column["type"]),
                bool(column["nullable"]),
                int(column.get("primary_key", 0)),
            )
            for column in inspector.get_columns(table_name)
        )
        foreign_keys = tuple(
            sorted(
                (
                    tuple(foreign_key["constrained_columns"]),
                    foreign_key["referred_table"],
                    tuple(foreign_key["referred_columns"]),
                )
                for foreign_key in inspector.get_foreign_keys(table_name)
            )
        )
        unique_constraints = tuple(
            sorted(
                tuple(constraint["column_names"])
                for constraint in inspector.get_unique_constraints(table_name)
            )
        )
        signature.append((table_name, columns, foreign_keys, unique_constraints))

    return tuple(signature)


def test_initial_migration_creates_schema_v1_from_empty_database(tmp_path: Path) -> None:
    engine = _upgrade_empty_database(tmp_path / "schema-v1.sqlite")
    inspector = inspect(engine)

    assert set(inspector.get_table_names()) == EXPECTED_TABLES | {"alembic_version"}

    with engine.connect() as connection:
        revision = connection.execute(text("select version_num from alembic_version")).scalar_one()

    assert revision == "0001_provenance_core"


def test_migrated_schema_matches_current_sqlalchemy_metadata(tmp_path: Path) -> None:
    migrated_engine = _upgrade_empty_database(tmp_path / "migrated.sqlite")
    metadata_engine = create_engine("sqlite://")
    metadata.create_all(metadata_engine)

    assert _schema_signature(migrated_engine) == _schema_signature(metadata_engine)


def test_initial_migration_is_deterministic(tmp_path: Path) -> None:
    first_engine = _upgrade_empty_database(tmp_path / "first.sqlite")
    second_engine = _upgrade_empty_database(tmp_path / "second.sqlite")

    assert _schema_signature(first_engine) == _schema_signature(second_engine)


def test_schema_uses_semantic_ids_without_surrogate_row_identity(tmp_path: Path) -> None:
    engine = _upgrade_empty_database(tmp_path / "semantic-ids.sqlite")
    inspector = inspect(engine)

    expected_primary_keys = {
        "sources": ["source_id"],
        "evidence_fragments": ["fragment_id"],
        "evidence_assertions": ["assertion_id"],
        "assertion_fragments": ["assertion_id", "fragment_id"],
    }

    for table_name, primary_key in expected_primary_keys.items():
        assert inspector.get_pk_constraint(table_name)["constrained_columns"] == primary_key
        assert "id" not in {column["name"] for column in inspector.get_columns(table_name)}


def test_schema_preserves_provenance_and_ownership_boundaries(tmp_path: Path) -> None:
    engine = _upgrade_empty_database(tmp_path / "boundaries.sqlite")
    inspector = inspect(engine)

    source_columns = {column["name"] for column in inspector.get_columns("sources")}
    fragment_columns = {
        column["name"] for column in inspector.get_columns("evidence_fragments")
    }
    assertion_columns = {
        column["name"] for column in inspector.get_columns("evidence_assertions")
    }
    link_columns = {
        column["name"] for column in inspector.get_columns("assertion_fragments")
    }

    assert {"platform_source_id", "external_locator"} <= source_columns
    assert {"title", "publisher", "published_on"}.isdisjoint(source_columns)

    assert {"source_start_ms", "source_end_ms", "locator"} <= fragment_columns
    assert {"historical_phase", "semantic_order"}.isdisjoint(fragment_columns)

    assert {
        "value_json",
        "derivation",
        "scope",
        "reconstruction_revision_id",
        "inference_reviewer_key",
        "inference_review_pass_id",
        "inference_note",
    } <= assertion_columns
    assert "verification" not in assertion_columns

    assert link_columns == {"assertion_id", "fragment_id", "fragment_order"}
