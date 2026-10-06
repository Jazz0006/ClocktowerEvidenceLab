"""Single-game ClockTracker public-source probe.

Network acquisition is deliberately separate from payload normalization so tests
and evidence review do not depend on live external access.
"""

import argparse
import json
from collections.abc import Sequence
from pathlib import Path
from urllib.request import Request, urlopen

from clocktower_evidence_lab.acquisition.clocktracker import (
    clocktracker_game_api_url,
    parse_clocktracker_game_json,
)

_DEFAULT_USER_AGENT = "ClocktowerEvidenceLab/0.1 clocktracker-source-probe"


def fetch_clocktracker_game_json(
    game_id: str,
    *,
    timeout_seconds: float = 30.0,
) -> str:
    """Fetch one explicitly named public ClockTracker game payload."""

    request = Request(
        clocktracker_game_api_url(game_id),
        headers={"User-Agent": _DEFAULT_USER_AGENT},
    )
    with urlopen(request, timeout=timeout_seconds) as response:  # noqa: S310
        charset = response.headers.get_content_charset() or "utf-8"
        return response.read().decode(charset)


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        description=(
            "Fetch or parse one explicit ClockTracker game payload. "
            "This normalizes source data only and does not verify evidence."
        )
    )
    parser.add_argument("game_id")
    parser.add_argument(
        "--input-json",
        type=Path,
        help="Parse a previously captured payload instead of using the network.",
    )
    parser.add_argument("--timeout-seconds", type=float, default=30.0)
    args = parser.parse_args(argv)

    if args.input_json is None:
        raw_json = fetch_clocktracker_game_json(
            args.game_id,
            timeout_seconds=args.timeout_seconds,
        )
    else:
        raw_json = args.input_json.read_text(encoding="utf-8")

    snapshot = parse_clocktracker_game_json(raw_json)
    if snapshot.game_id != args.game_id:
        parser.error(
            f"payload game ID {snapshot.game_id!r} does not match requested "
            f"game ID {args.game_id!r}"
        )

    print(
        json.dumps(
            snapshot.model_dump(mode="json"),
            ensure_ascii=False,
            indent=2,
            sort_keys=True,
        )
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
