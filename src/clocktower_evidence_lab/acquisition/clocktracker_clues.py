"""Prepare ClockTracker notes for clue extraction and check an extraction.

``prepare`` turns one parsed game into extractor input: the first grimoire page
as a seat roster and the notes split into identified lines, with player names
replaced (grimoire-matched names by their seat ``S<n>``, other capitalized names
by placeholders ``P<n>``). The placeholder table is private and must stay out of
Git.

``check`` performs structural checks of an extraction against that input only.
It does not decide whether a clue was true, legal or a good choice.
"""

import argparse
import json
import re
import sys
from collections.abc import Sequence
from pathlib import Path

from clocktower_evidence_lab.acquisition.clocktracker import (
    ClockTrackerGameSnapshot,
    parse_clocktracker_game_json,
)
from clocktower_evidence_lab.interchange.clocktracker_clue_extraction_v1 import ClueExtraction

_PHASE = re.compile(r"^(setup|night\s+(\d+)|day\s+(\d+))\b[^:]*:?\s*$", re.IGNORECASE)
_BULLET = re.compile(r"^\s*[-*•]\s*")
_WORD = re.compile(r"\b[A-Z][a-zA-Z'’]+\b")
_ALIAS = re.compile(r"\b[PS]\d+\b")
_INFO_HINTS = re.compile(
    r"\b(sees?|saw|learns?|learnt|gets?|got|picks?|checks?|undertakes?|ravenkeeps?|shown|told)\b",
    re.IGNORECASE,
)

# Capitalized words that are not player names.
_NOT_NAMES = {
    "a",
    "an",
    "and",
    "as",
    "at",
    "but",
    "day",
    "dies",
    "evil",
    "final",
    "for",
    "good",
    "herring",
    "in",
    "is",
    "it",
    "lead",
    "no",
    "nobody",
    "nothing",
    "night",
    "of",
    "on",
    "or",
    "red",
    "setup",
    "st",
    "storyteller",
    "team",
    "the",
    "then",
    "they",
    "this",
    "to",
    "trouble",
    "brewing",
    "wins",
    "yes",
    "players",
    "player",
    "ghost",
    "votes",
    "vote",
    "executed",
    "execution",
    "executions",
    "demon",
    "minion",
    "minions",
    "outsider",
    "outsiders",
    "townsfolk",
    "drunk",
    "poisoned",
    "washerwoman",
    "librarian",
    "investigator",
    "chef",
    "empath",
    "fortune",
    "teller",
    "undertaker",
    "monk",
    "ravenkeeper",
    "virgin",
    "slayer",
    "soldier",
    "mayor",
    "butler",
    "recluse",
    "saint",
    "poisoner",
    "spy",
    "scarlet",
    "woman",
    "baron",
    "imp",
}


def _alias_of(player_name: str | None) -> str | None:
    if not player_name:
        return None
    words = [w for w in player_name.split() if not w.isdigit()]
    name = " ".join(words).strip()
    return name if len(name) >= 2 else None


def prepare(game: ClockTrackerGameSnapshot) -> dict:
    if not game.grimoires or not game.grimoires[0].seats:
        raise ValueError("game has no grimoire page")
    seats = sorted(game.grimoires[0].seats, key=lambda s: (s.order, s.source_index))
    roster = [
        {
            "seat": i,
            "role_id": s.role_id,
            "related_role_id": s.related_role_id,
            "alignment": s.alignment,
            "reminders": list(s.reminders),
        }
        for i, s in enumerate(seats, start=1)
    ]
    token_names: dict[str, str] = {}
    for i, s in enumerate(seats, start=1):
        alias = _alias_of(s.player_name)
        if alias:
            token_names.setdefault(alias.lower(), f"S{i}")

    placeholders: dict[str, str] = {}

    def pseudonymize(text: str) -> str:
        for name in sorted(token_names, key=len, reverse=True):
            text = re.sub(rf"\b{re.escape(name)}\b", token_names[name], text, flags=re.IGNORECASE)

        def other(m: re.Match[str]) -> str:
            word = m.group(0)
            if word.lower() in _NOT_NAMES:
                return word
            key = word.lower()
            if key not in placeholders:
                placeholders[key] = f"P{len(placeholders) + 1}"
            return placeholders[key]

        return _WORD.sub(other, text)

    lines = []
    phase, number, counts = "PRE", 0, {}
    for raw in game.notes.splitlines():
        text = raw.strip()
        if not text:
            continue
        m = _PHASE.match(text)
        if m:
            phase = "SETUP" if m.group(1).lower() == "setup" else ("N" if m.group(2) else "D")
            number = int(m.group(2) or m.group(3) or 0)
            continue
        key = f"{phase}{number or ''}"
        counts[key] = counts.get(key, 0) + 1
        lines.append(
            {
                "line_id": f"{key}.{counts[key]}",
                "phase": {"N": "NIGHT", "D": "DAY"}.get(phase, phase),
                "number": number or None,
                "text": pseudonymize(_BULLET.sub("", text)),
            }
        )
    return {
        "game_id": game.game_id,
        "script": game.script,
        "roster": roster,
        "lines": lines,
        "private_placeholders": {v: k for k, v in placeholders.items()},
    }


def extractor_input(prepared: dict) -> dict:
    """The part of a prepared game that may be shown to an extractor model."""

    return {k: v for k, v in prepared.items() if not k.startswith("private_")}


def check(prepared: dict, extraction: ClueExtraction) -> dict:
    errors: list[str] = []
    warnings: list[str] = []
    n = len(prepared["roster"])
    roster = {r["seat"]: r for r in prepared["roster"]}
    lines = {line["line_id"]: line for line in prepared["lines"]}
    resolved = {r.alias: r.seat for r in extraction.names if r.seat is not None}

    def resolve(text: str) -> str:
        return re.sub(
            r"\bP\d+\b",
            lambda m: f"S{resolved[m.group(0)]}" if m.group(0) in resolved else m.group(0),
            text,
        )

    def seat_ok(where: str, seat: int) -> None:
        if not 1 <= seat <= n:
            errors.append(f"{where}: seat {seat} outside 1..{n}")

    def quote_ok(where: str, line_id: str, quote: str) -> None:
        line = lines.get(line_id)
        if line is None:
            errors.append(f"{where}: unknown line {line_id}")
        elif quote not in line["text"] and quote not in resolve(line["text"]):
            errors.append(f"{where}: quote not found in line {line_id}")

    if extraction.game_id != prepared["game_id"]:
        errors.append("game_id does not match")
    for r in extraction.names:
        if r.alias not in prepared.get("private_placeholders", {r.alias: None}):
            errors.append(f"names: unknown placeholder {r.alias}")
        if r.seat is not None:
            seat_ok(f"names {r.alias}", r.seat)
        if r.basis in ("ROLE_EVIDENCE", "NAME_VARIANT") and (
            r.seat is None or not r.evidence_line_ids
        ):
            errors.append(f"names {r.alias}: {r.basis} needs a seat and evidence lines")
        for line_id in r.evidence_line_ids:
            if line_id not in lines:
                errors.append(f"names {r.alias}: unknown line {line_id}")

    for c in extraction.setup_choices:
        for s in c.seats:
            seat_ok(f"setup {c.line_id}", s)
        quote_ok(f"setup {c.line_id}", c.line_id, c.quote)

    covered = (
        {c.line_id for c in extraction.clues}
        | {s.line_id for s in extraction.skipped}
        | {c.line_id for c in extraction.setup_choices}
    )
    for c in extraction.clues:
        where = f"clue {c.line_id}"
        line = lines.get(c.line_id)
        if line is not None and (line["phase"] != "NIGHT" or line["number"] != c.night):
            errors.append(f"{where}: line is not in night {c.night}")
        for s in (c.recipient_seat, *c.chosen_seats, *c.shown.seats):
            seat_ok(where, s)
        r = roster.get(c.recipient_seat)
        if r and c.ability not in (r["role_id"], r["related_role_id"]):
            errors.append(f"{where}: seat {c.recipient_seat} is {r['role_id']}, not {c.ability}")
        quote_ok(where, c.line_id, c.quote)
        if line is not None:
            left = sorted(set(re.findall(r"\bP\d+\b", resolve(line["text"]))))
            if left:
                warnings.append(f"{where}: unresolved placeholder(s) {', '.join(left)}")
    for s in extraction.skipped:
        if s.line_id not in lines:
            errors.append(f"skipped: unknown line {s.line_id}")

    for line in prepared["lines"]:
        if (
            line["phase"] == "NIGHT"
            and line["line_id"] not in covered
            and _INFO_HINTS.search(line["text"])
        ):
            warnings.append(
                f"{line['line_id']}: looks like information but is neither a clue nor skipped"
            )

    return {
        "ok": not errors,
        "errors": errors,
        "warnings": warnings,
        "clues": len(extraction.clues),
        "setup_choices": len(extraction.setup_choices),
        "skipped": len(extraction.skipped),
    }


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    sub = parser.add_subparsers(dest="command", required=True)
    p = sub.add_parser("prepare", help="game JSON -> prepared JSON (private: keep out of Git)")
    p.add_argument("game_json", type=Path)
    p = sub.add_parser("input", help="prepared JSON -> extractor input (no private fields)")
    p.add_argument("prepared_json", type=Path)
    p = sub.add_parser("check", help="check an extraction against a prepared game")
    p.add_argument("prepared_json", type=Path)
    p.add_argument("extraction_json", type=Path)
    args = parser.parse_args(argv)

    if args.command == "prepare":
        game = parse_clocktracker_game_json(args.game_json.read_text(encoding="utf-8"))
        json.dump(prepare(game), sys.stdout, ensure_ascii=False, indent=2)
        return 0
    prepared = json.loads(args.prepared_json.read_text(encoding="utf-8"))
    if args.command == "input":
        json.dump(extractor_input(prepared), sys.stdout, ensure_ascii=False, indent=2)
        return 0
    extraction = ClueExtraction.model_validate_json(
        args.extraction_json.read_text(encoding="utf-8")
    )
    report = check(prepared, extraction)
    json.dump(report, sys.stdout, ensure_ascii=False, indent=2)
    return 0 if report["ok"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
