"""Command-line probe for podcast RSS episode/transcript locators."""

import argparse
import json
from collections.abc import Sequence
from urllib.request import Request, urlopen

from clocktower_evidence_lab.acquisition.podcast import find_episodes, parse_podcast_rss

_DEFAULT_USER_AGENT = "ClocktowerEvidenceLab/0.1 podcast-source-probe"


def fetch_rss(feed_url: str, *, timeout_seconds: float = 30.0) -> str:
    """Fetch RSS text without downloading episode audio or transcript bodies."""

    request = Request(feed_url, headers={"User-Agent": _DEFAULT_USER_AGENT})
    with urlopen(request, timeout=timeout_seconds) as response:  # noqa: S310
        charset = response.headers.get_content_charset() or "utf-8"
        return response.read().decode(charset)


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        description="Locate podcast episode audio/transcript URLs from a public RSS feed."
    )
    parser.add_argument("feed_url")
    parser.add_argument("--title-contains", required=True)
    parser.add_argument("--timeout-seconds", type=float, default=30.0)
    args = parser.parse_args(argv)

    rss = fetch_rss(args.feed_url, timeout_seconds=args.timeout_seconds)
    episodes = parse_podcast_rss(rss, feed_url=args.feed_url)
    matches = find_episodes(episodes, args.title_contains)

    print(
        json.dumps(
            [episode.model_dump(mode="json") for episode in matches],
            ensure_ascii=False,
            indent=2,
            sort_keys=True,
        )
    )
    return 0 if matches else 1


if __name__ == "__main__":
    raise SystemExit(main())
