"""Bounded parsing for one public ClockTracker game payload.

This module normalizes source data only. It does not verify game claims, infer
missing roles, or promote source fields into canonical EvidenceLab evidence.
"""

import json
from uuid import UUID

from pydantic import BaseModel, ConfigDict, Field


class _ExternalModel(BaseModel):
    model_config = ConfigDict(extra="ignore", frozen=True)


class _StableModel(BaseModel):
    model_config = ConfigDict(extra="forbid", frozen=True)


class _RolePayload(_ExternalModel):
    id: str | None = None
    name: str | None = None
    type: str | None = None


class _ReminderPayload(_ExternalModel):
    reminder: str = ""
    token_url: str | None = None


class _TokenPayload(_ExternalModel):
    order: int
    player_name: str = ""
    player_id: str | None = None
    role_id: str | None = None
    related_role_id: str | None = None
    alignment: str | None = None
    is_dead: bool = False
    used_ghost_vote: bool = False
    role: _RolePayload | None = None
    related_role: _RolePayload | None = None
    reminders: tuple[_ReminderPayload, ...] = ()


class _GrimoirePayload(_ExternalModel):
    id: int | None = None
    tokens: tuple[_TokenPayload, ...] = ()


class _DemonBluffPayload(_ExternalModel):
    role_id: str | None = None
    name: str | None = None
    role: _RolePayload | None = None


class _GamePayload(_ExternalModel):
    id: str
    date: str | None = None
    script: str | None = None
    player_count: int | None = Field(default=None, ge=0)
    traveler_count: int | None = Field(default=None, ge=0)
    notes: str = ""
    storyteller: str | None = None
    co_storytellers: tuple[str, ...] = ()
    grimoire: tuple[_GrimoirePayload, ...] = ()
    demon_bluffs: tuple[_DemonBluffPayload, ...] = ()


class ClockTrackerSeatSnapshot(_StableModel):
    """One persisted ClockTracker grimoire token in circular order."""

    order: int
    player_name: str | None
    player_id: str | None
    role_id: str | None
    role_name: str | None
    related_role_id: str | None
    related_role_name: str | None
    alignment: str | None
    is_dead: bool
    used_ghost_vote: bool
    reminders: tuple[str, ...]


class ClockTrackerGrimoireSnapshot(_StableModel):
    """One ClockTracker grimoire page without cross-page guessing."""

    grimoire_id: int | None
    seats: tuple[ClockTrackerSeatSnapshot, ...]


class ClockTrackerDemonBluffSnapshot(_StableModel):
    role_id: str | None
    role_name: str | None


class ClockTrackerGameSnapshot(_StableModel):
    """Stable acquisition projection of one ClockTracker game response."""

    game_id: str
    date: str | None
    script: str | None
    player_count: int | None
    traveler_count: int | None
    storyteller: str | None
    co_storytellers: tuple[str, ...]
    notes: str
    grimoires: tuple[ClockTrackerGrimoireSnapshot, ...]
    demon_bluffs: tuple[ClockTrackerDemonBluffSnapshot, ...]

    @property
    def primary_grimoire(self) -> ClockTrackerGrimoireSnapshot | None:
        """Return a grimoire only when the source has exactly one page."""

        if len(self.grimoires) != 1:
            return None
        return self.grimoires[0]

    @property
    def complete_primary_role_map(self) -> bool:
        """Whether the single grimoire page has a role ID for every seat token."""

        grimoire = self.primary_grimoire
        return bool(grimoire and grimoire.seats) and all(
            seat.role_id is not None for seat in grimoire.seats
        )


def clocktracker_game_api_url(game_id: str) -> str:
    """Return the public single-game API URL for one explicit UUID."""

    try:
        canonical_id = str(UUID(game_id))
    except ValueError as exc:
        raise ValueError("ClockTracker game_id must be a UUID") from exc
    return f"https://clocktracker.app/api/games/{canonical_id}"


def parse_clocktracker_game_json(json_text: str) -> ClockTrackerGameSnapshot:
    """Parse one ClockTracker API response without inferring missing source fields."""

    try:
        raw = json.loads(json_text)
    except json.JSONDecodeError as exc:
        raise ValueError("invalid ClockTracker game JSON") from exc

    payload = _GamePayload.model_validate(raw)
    grimoires = tuple(_normalize_grimoire(grimoire) for grimoire in payload.grimoire)
    demon_bluffs = tuple(
        ClockTrackerDemonBluffSnapshot(
            role_id=bluff.role_id,
            role_name=bluff.role.name if bluff.role is not None else None,
        )
        for bluff in payload.demon_bluffs
    )

    return ClockTrackerGameSnapshot(
        game_id=payload.id,
        date=payload.date,
        script=payload.script,
        player_count=payload.player_count,
        traveler_count=payload.traveler_count,
        storyteller=_clean_text(payload.storyteller),
        co_storytellers=tuple(name for name in payload.co_storytellers if name.strip()),
        notes=payload.notes,
        grimoires=grimoires,
        demon_bluffs=demon_bluffs,
    )


def _normalize_grimoire(payload: _GrimoirePayload) -> ClockTrackerGrimoireSnapshot:
    ordered_tokens = sorted(payload.tokens, key=lambda token: token.order)
    orders = [token.order for token in ordered_tokens]
    if len(set(orders)) != len(orders):
        raise ValueError("ClockTracker grimoire contains duplicate token.order values")

    seats = tuple(
        ClockTrackerSeatSnapshot(
            order=token.order,
            player_name=_clean_text(token.player_name),
            player_id=token.player_id,
            role_id=token.role_id,
            role_name=token.role.name if token.role is not None else None,
            related_role_id=token.related_role_id,
            related_role_name=(token.related_role.name if token.related_role is not None else None),
            alignment=token.alignment,
            is_dead=token.is_dead,
            used_ghost_vote=token.used_ghost_vote,
            reminders=tuple(
                reminder.reminder for reminder in token.reminders if reminder.reminder.strip()
            ),
        )
        for token in ordered_tokens
    )
    return ClockTrackerGrimoireSnapshot(grimoire_id=payload.id, seats=seats)


def _clean_text(value: str | None) -> str | None:
    if value is None:
        return None
    cleaned = value.strip()
    return cleaned or None
