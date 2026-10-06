import json

from clocktower_evidence_lab.acquisition.clocktracker import (
    clocktracker_game_api_url,
    parse_clocktracker_game_json,
)

_GAME_ID = "de5f126b-89f5-4c78-a898-f5724a93430e"


def _payload(*, second_role_id: str | None = "fortune_teller") -> str:
    return json.dumps(
        {
            "id": _GAME_ID,
            "date": "2025-09-30T00:00:00.000Z",
            "script": "Trouble Brewing",
            "player_count": 8,
            "traveler_count": 0,
            "storyteller": "@CryptCore",
            "co_storytellers": ["@Larrikin"],
            "notes": "Night 1\nExample source notes",
            "ignored_upstream_field": "allowed",
            "grimoire": [
                {
                    "id": 91,
                    "tokens": [
                        {
                            "order": 2,
                            "player_name": "Second",
                            "role_id": second_role_id,
                            "role": (
                                {
                                    "id": "fortune_teller",
                                    "name": "Fortune Teller",
                                    "type": "TOWNSFOLK",
                                }
                                if second_role_id is not None
                                else None
                            ),
                            "alignment": "GOOD",
                            "is_dead": False,
                            "used_ghost_vote": False,
                            "reminders": [],
                        },
                        {
                            "order": 1,
                            "player_name": "First",
                            "player_id": "player-1",
                            "role_id": "drunk",
                            "role": {
                                "id": "drunk",
                                "name": "Drunk",
                                "type": "OUTSIDER",
                            },
                            "related_role_id": "investigator",
                            "related_role": {
                                "id": "investigator",
                                "name": "Investigator",
                                "type": "TOWNSFOLK",
                            },
                            "alignment": "GOOD",
                            "is_dead": True,
                            "used_ghost_vote": True,
                            "reminders": [
                                {"reminder": "Is The Drunk", "token_url": "ignored"},
                                {"reminder": ""},
                            ],
                            "another_ignored_field": 123,
                        },
                    ],
                }
            ],
            "demon_bluffs": [
                {
                    "role_id": "mayor",
                    "role": {"id": "mayor", "name": "Mayor", "type": "TOWNSFOLK"},
                },
                {"role_id": "saint", "role": None},
            ],
        }
    )


def test_parse_clocktracker_game_json_preserves_structured_source_fields() -> None:
    snapshot = parse_clocktracker_game_json(_payload())

    assert snapshot.game_id == _GAME_ID
    assert snapshot.player_count == 8
    assert snapshot.traveler_count == 0
    assert snapshot.storyteller == "@CryptCore"
    assert snapshot.co_storytellers == ("@Larrikin",)
    assert snapshot.notes.startswith("Night 1")
    assert snapshot.complete_primary_role_map is True

    grimoire = snapshot.primary_grimoire
    assert grimoire is not None
    assert grimoire.grimoire_id == 91
    assert [seat.order for seat in grimoire.seats] == [1, 2]

    first = grimoire.seats[0]
    assert first.player_name == "First"
    assert first.role_id == "drunk"
    assert first.role_name == "Drunk"
    assert first.related_role_id == "investigator"
    assert first.related_role_name == "Investigator"
    assert first.is_dead is True
    assert first.used_ghost_vote is True
    assert first.reminders == ("Is The Drunk",)

    assert [(bluff.role_id, bluff.role_name) for bluff in snapshot.demon_bluffs] == [
        ("mayor", "Mayor"),
        ("saint", None),
    ]


def test_missing_role_remains_missing_instead_of_being_inferred() -> None:
    snapshot = parse_clocktracker_game_json(_payload(second_role_id=None))

    assert snapshot.complete_primary_role_map is False
    grimoire = snapshot.primary_grimoire
    assert grimoire is not None
    assert grimoire.seats[1].role_id is None
    assert grimoire.seats[1].role_name is None


def test_multiple_grimoire_pages_are_not_flattened_into_one_state() -> None:
    payload = json.loads(_payload())
    payload["grimoire"].append({"id": 92, "tokens": []})

    snapshot = parse_clocktracker_game_json(json.dumps(payload))

    assert len(snapshot.grimoires) == 2
    assert snapshot.primary_grimoire is None
    assert snapshot.complete_primary_role_map is False


def test_duplicate_token_order_is_rejected() -> None:
    payload = json.loads(_payload())
    payload["grimoire"][0]["tokens"][1]["order"] = 2

    try:
        parse_clocktracker_game_json(json.dumps(payload))
    except ValueError as exc:
        assert "duplicate token.order" in str(exc)
    else:
        raise AssertionError("duplicate token.order should be rejected")


def test_clocktracker_game_api_url_accepts_only_uuid_game_ids() -> None:
    assert clocktracker_game_api_url(_GAME_ID) == (
        "https://clocktracker.app/api/games/de5f126b-89f5-4c78-a898-f5724a93430e"
    )

    try:
        clocktracker_game_api_url("not-a-game-id")
    except ValueError as exc:
        assert "must be a UUID" in str(exc)
    else:
        raise AssertionError("invalid game ID should be rejected")
