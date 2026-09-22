from datetime import UTC, datetime

import pytest
from pydantic import ValidationError

from clocktower_evidence_lab.domain.reconstruction import (
    Game,
    GameSeat,
    ReconstructionRevision,
    ReconstructionStatus,
    Storyteller,
    StorytellerAssignment,
)


def test_storyteller_keeps_identity_separate_from_qualification() -> None:
    storyteller = Storyteller(
        storyteller_id="storyteller:ben-burns",
        independence_key="storyteller-independence:ben-burns",
        display_name="Ben Burns",
    )

    assert storyteller.independence_key == "storyteller-independence:ben-burns"

    with pytest.raises(ValidationError):
        Storyteller(
            storyteller_id="storyteller:ben-burns",
            independence_key="storyteller-independence:ben-burns",
            display_name="Ben Burns",
            quality_score="VERIFIED_EXPERT_OR_TRUSTED",
        )


def test_game_seat_is_game_scoped_without_global_player_identity() -> None:
    seat = GameSeat(
        seat_id="seat:game1:4",
        game_id="game:1",
        seat_order=4,
        display_name="Elliott",
        experience_metadata={"explicit_first_game": False},
    )

    assert seat.game_id == "game:1"
    assert seat.seat_order == 4

    with pytest.raises(ValidationError):
        GameSeat(
            seat_id="seat:game1:4",
            game_id="game:1",
            seat_order=4,
            global_player_id="player:elliott",
        )


def test_game_owns_current_revision_pointer_without_parallel_revision_status() -> None:
    game = Game(
        game_id="game:1",
        script="Trouble Brewing",
        storyteller_assignments=(
            StorytellerAssignment(
                storyteller_id="storyteller:ben-burns",
                role="PRIMARY",
            ),
        ),
        reconstruction_status=ReconstructionStatus.PARTIAL,
        current_reconstruction_revision_id="revision:game1:2",
    )

    assert game.current_reconstruction_revision_id == "revision:game1:2"

    with pytest.raises(ValidationError):
        Game(
            game_id="game:1",
            reconstruction_status=ReconstructionStatus.PARTIAL,
            current_reconstruction_revision_id="revision:game1:2",
            current_revision_status="CURRENT",
        )


def test_game_rejects_duplicate_storyteller_assignments() -> None:
    assignment = StorytellerAssignment(
        storyteller_id="storyteller:ben-burns",
        role="PRIMARY",
    )

    with pytest.raises(ValidationError):
        Game(
            game_id="game:1",
            storyteller_assignments=(assignment, assignment),
        )


def test_reconstruction_revision_is_auditable_but_not_self_current() -> None:
    revision = ReconstructionRevision(
        revision_id="revision:game1:2",
        game_id="game:1",
        parent_revision_id="revision:game1:1",
        created_at=datetime(2026, 9, 23, 0, 0, tzinfo=UTC),
        change_note="Corrected seating interpretation from additional evidence.",
    )

    assert revision.parent_revision_id == "revision:game1:1"

    with pytest.raises(ValidationError):
        ReconstructionRevision(
            revision_id="revision:game1:2",
            game_id="game:1",
            parent_revision_id="revision:game1:2",
            created_at=datetime(2026, 9, 23, 0, 0, tzinfo=UTC),
        )

    with pytest.raises(ValidationError):
        ReconstructionRevision(
            revision_id="revision:game1:2",
            game_id="game:1",
            created_at=datetime(2026, 9, 23, 0, 0),
        )


def test_revision_has_no_second_current_or_superseded_flag() -> None:
    with pytest.raises(ValidationError):
        ReconstructionRevision(
            revision_id="revision:game1:1",
            game_id="game:1",
            created_at=datetime(2026, 9, 23, 0, 0, tzinfo=UTC),
            is_current=True,
        )

    with pytest.raises(ValidationError):
        ReconstructionRevision(
            revision_id="revision:game1:1",
            game_id="game:1",
            created_at=datetime(2026, 9, 23, 0, 0, tzinfo=UTC),
            superseded=True,
        )
