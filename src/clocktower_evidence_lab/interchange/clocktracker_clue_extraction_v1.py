"""Versioned output of extracting information clues from ClockTracker notes.

An extraction records what the notes *say* a player was shown, against the
grimoire seats. It is source-derived and UNVERIFIED: it does not decide whether
a clue was true, legal or good. Those judgements belong to the consumer.

Privacy: records refer to players only by seat (``S1``..``Sn``, from grimoire
token order). Player names never appear in an extraction.
"""

from typing import Literal

from pydantic import BaseModel, ConfigDict, Field

SCHEMA_ID = "evidence-lab.clocktracker-clue-extraction"
SCHEMA_VERSION = 1

# Trouble Brewing abilities that give a player information.
INFORMATION_ABILITIES = (
    "washerwoman",
    "librarian",
    "investigator",
    "chef",
    "empath",
    "fortune_teller",
    "undertaker",
    "ravenkeeper",
)

Ability = Literal[
    "washerwoman",
    "librarian",
    "investigator",
    "chef",
    "empath",
    "fortune_teller",
    "undertaker",
    "ravenkeeper",
]


class _Model(BaseModel):
    model_config = ConfigDict(extra="forbid", frozen=True)


class NameResolution(_Model):
    """How a placeholder (``P1``..) for a name not on the grimoire maps to a seat.

    Names that match a grimoire token are replaced by their seat during
    preparation and need no resolution. ``seat`` is ``None`` for a name that is
    not a player (e.g. the storyteller) or cannot be resolved. ``NAME_VARIANT``
    is a spelling variant of a grimoire name (e.g. Holly / Hollie).
    """

    alias: str = Field(pattern=r"^P\d+$")
    seat: int | None = Field(default=None, ge=1)
    basis: Literal["ROLE_EVIDENCE", "NAME_VARIANT", "NOT_A_PLAYER", "UNRESOLVED"]
    evidence_line_ids: tuple[str, ...] = ()


class ShownContent(_Model):
    """What the recipient was shown, exactly as the notes state it."""

    seats: tuple[int, ...] = ()
    role_id: str | None = None
    number: int | None = None
    answer: Literal["YES", "NO"] | None = None
    no_outsiders: bool = False


class ClueRecord(_Model):
    line_id: str
    night: int = Field(ge=1)
    recipient_seat: int = Field(ge=1)
    ability: Ability
    chosen_seats: tuple[int, ...] = ()
    shown: ShownContent
    # Storyteller annotations copied from the notes, e.g. "drunk", "poisoned",
    # "red herring", "Spy registers as Chef". Not interpreted.
    note_annotations: tuple[str, ...] = ()
    quote: str = Field(min_length=1)


class SetupChoice(_Model):
    line_id: str
    kind: Literal["RED_HERRING", "DRUNK", "DEMON_BLUFFS", "OTHER"]
    seats: tuple[int, ...] = ()
    role_ids: tuple[str, ...] = ()
    quote: str = Field(min_length=1)


class SkippedLine(_Model):
    line_id: str
    reason: str = Field(min_length=1)


class ClueExtraction(_Model):
    schema_id: Literal["evidence-lab.clocktracker-clue-extraction"] = SCHEMA_ID
    schema_version: Literal[1] = SCHEMA_VERSION
    game_id: str
    extractor: str = Field(min_length=1)
    names: tuple[NameResolution, ...] = ()
    setup_choices: tuple[SetupChoice, ...] = ()
    clues: tuple[ClueRecord, ...] = ()
    # Night lines about information abilities that could not be recorded.
    skipped: tuple[SkippedLine, ...] = ()
