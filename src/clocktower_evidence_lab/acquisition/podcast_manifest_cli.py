"""CLI for building the current C2 podcast episode manifest from live RSS."""

import argparse
import sys
from collections.abc import Sequence
from pathlib import Path

from clocktower_evidence_lab.acquisition.c2_podcast import (
    CULT_OF_CLOCKTOWER_FEED_URL,
    build_c2_manifest,
)
from clocktower_evidence_lab.acquisition.podcast import parse_podcast_rss
from clocktower_evidence_lab.acquisition.podcast_manifest import (
    EpisodeScope,
    active_acquisition_queue,
)
from clocktower_evidence_lab.acquisition.podcast_probe import fetch_rss


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        description="Build the C2 Trouble Brewing podcast manifest from live RSS."
    )
    parser.add_argument("--feed-url", default=CULT_OF_CLOCKTOWER_FEED_URL)
    parser.add_argument("--output", type=Path)
    parser.add_argument("--timeout-seconds", type=float, default=30.0)
    args = parser.parse_args(argv)

    rss = fetch_rss(args.feed_url, timeout_seconds=args.timeout_seconds)
    episodes = parse_podcast_rss(rss, feed_url=args.feed_url)
    manifest = build_c2_manifest(episodes)
    payload = manifest.model_dump_json(indent=2) + "\n"

    if args.output is None:
        sys.stdout.write(payload)
    else:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(payload, encoding="utf-8")

    in_scope = sum(entry.scope is EpisodeScope.IN_SCOPE for entry in manifest.episodes)
    queued = len(active_acquisition_queue(manifest))
    print(
        (
            f"episodes={len(manifest.episodes)} "
            f"in_scope={in_scope} "
            f"acquisition_queue={queued}"
        ),
        file=sys.stderr,
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
