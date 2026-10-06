import json

from clocktower_evidence_lab.acquisition.clocktracker_probe import main

_GAME_ID = "de5f126b-89f5-4c78-a898-f5724a93430e"


def test_probe_can_parse_captured_payload_without_network(tmp_path, capsys) -> None:
    payload_path = tmp_path / "clocktracker-game.json"
    payload_path.write_text(
        json.dumps(
            {
                "id": _GAME_ID,
                "script": "Trouble Brewing",
                "player_count": 8,
                "storyteller": "@CryptCore",
                "co_storytellers": ["@Larrikin"],
                "notes": "Night 1",
                "grimoire": [
                    {
                        "id": 1,
                        "tokens": [
                            {
                                "order": 1,
                                "player_name": "Example",
                                "role_id": "investigator",
                                "role": {"id": "investigator", "name": "Investigator"},
                                "alignment": "GOOD",
                            }
                        ],
                    }
                ],
                "demon_bluffs": [],
            }
        ),
        encoding="utf-8",
    )

    assert main([_GAME_ID, "--input-json", str(payload_path)]) == 0

    normalized = json.loads(capsys.readouterr().out)
    assert normalized["game_id"] == _GAME_ID
    assert normalized["grimoires"][0]["seats"][0]["role_id"] == "investigator"


def test_probe_rejects_captured_payload_for_a_different_game(tmp_path) -> None:
    payload_path = tmp_path / "clocktracker-game.json"
    payload_path.write_text(
        json.dumps(
            {
                "id": "66d4356f-fa9f-468d-ba49-6e6858e2e80d",
                "grimoire": [],
                "demon_bluffs": [],
            }
        ),
        encoding="utf-8",
    )

    try:
        main([_GAME_ID, "--input-json", str(payload_path)])
    except SystemExit as exc:
        assert exc.code == 2
    else:
        raise AssertionError("mismatched payload ID should be rejected")
