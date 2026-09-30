"""Deterministic JSON codec for the Host-compatible Trouble Brewing snapshot V1."""

from clocktower_evidence_lab.domain.tb_snapshot import TroubleBrewingGameSnapshotV1


def dump_tb_game_snapshot_v1(snapshot: TroubleBrewingGameSnapshotV1) -> str:
    """Serialize with the same stable field order and compact JSON shape as Host TBGS-0."""

    return snapshot.model_dump_json(
        by_alias=True,
        exclude_none=True,
        round_trip=True,
    )


def load_tb_game_snapshot_v1(encoded: str) -> TroubleBrewingGameSnapshotV1:
    """Strictly load one Trouble Brewing V1 snapshot."""

    return TroubleBrewingGameSnapshotV1.model_validate_json(encoded)
