import json

from clocktower_evidence_lab.acquisition.clocktracker import parse_clocktracker_game_json
from clocktower_evidence_lab.acquisition.clocktracker_clues import (
    check,
    extractor_input,
    prepare,
)
from clocktower_evidence_lab.interchange.clocktracker_clue_extraction_v1 import ClueExtraction

_ID = "00000000-0000-4000-8000-000000000001"


def _game() -> dict:
    tokens = [
        ("Alice 20250101", "empath", None),
        ("bob99", "imp", None),
        ("Carol", "drunk", "investigator"),
    ]
    notes = "Setup:\n- Carol is the Drunk\n\nNight 1:\n- Alice learns a 0\n- Bob kills Alice\n"
    payload = {
        "id": _ID,
        "script": "Trouble Brewing",
        "notes": notes,
        "grimoire": [
            {
                "id": 1,
                "tokens": [
                    {"order": i, "player_name": n, "role_id": r, "related_role_id": rr}
                    for i, (n, r, rr) in enumerate(tokens)
                ],
            }
        ],
    }
    return prepare(parse_clocktracker_game_json(json.dumps(payload)))


def test_extractor_input_contains_no_player_names() -> None:
    prepared = _game()
    text = json.dumps(extractor_input(prepared))

    for name in ("Alice", "Carol", "Bob", "bob99", "20250101"):
        assert name not in text
    assert "private_placeholders" not in text
    assert [line["text"] for line in prepared["lines"]] == [
        "S3 is the Drunk",
        "S1 learns a 0",
        "P1 kills S1",
    ]
    assert prepared["private_placeholders"] == {"P1": "bob"}


def _extraction(**clue: object) -> ClueExtraction:
    base = {
        "line_id": "N1.1",
        "night": 1,
        "recipient_seat": 1,
        "ability": "empath",
        "shown": {"number": 0},
        "quote": "S1 learns a 0",
    }
    return ClueExtraction.model_validate(
        {
            "game_id": _ID,
            "extractor": "test",
            "names": [
                {"alias": "P1", "seat": 2, "basis": "ROLE_EVIDENCE", "evidence_line_ids": ["N1.2"]}
            ],
            "clues": [{**base, **clue}],
        }
    )


def test_check_accepts_consistent_extraction() -> None:
    report = check(_game(), _extraction())

    assert report["ok"], report["errors"]
    assert report["warnings"] == []


def test_check_rejects_wrong_ability_seat_and_quote() -> None:
    prepared = _game()

    assert not check(prepared, _extraction(ability="chef"))["ok"]
    assert not check(prepared, _extraction(recipient_seat=9))["ok"]
    assert not check(prepared, _extraction(quote="S1 learns a 2"))["ok"]
    assert not check(prepared, _extraction(line_id="SETUP.1"))["ok"]
    # A Drunk is recorded with the ability they believe they have.
    drunk = _extraction(recipient_seat=3, ability="investigator")
    assert "seat 3 is drunk" not in " ".join(check(prepared, drunk)["errors"])
