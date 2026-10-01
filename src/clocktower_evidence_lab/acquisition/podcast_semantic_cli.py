"""CLI for temporary full-transcript semantic-review sessions."""

import argparse
import sys
from collections.abc import Sequence
from pathlib import Path

from clocktower_evidence_lab.acquisition.podcast_semantic import (
    cleanup_semantic_session,
    prepare_semantic_session,
    render_semantic_transcript,
)


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        description=(
            "Prepare, render, or clean a temporary podcast semantic-review workspace. "
            "Full audio/transcript artifacts remain outside Git."
        )
    )
    subparsers = parser.add_subparsers(dest="command", required=True)

    prepare = subparsers.add_parser("prepare")
    prepare.add_argument("--guid", required=True)
    prepare.add_argument("--work-dir", type=Path, required=True)

    render = subparsers.add_parser("render")
    render.add_argument("--work-dir", type=Path, required=True)

    cleanup = subparsers.add_parser("cleanup")
    cleanup.add_argument("--work-dir", type=Path, required=True)

    args = parser.parse_args(argv)

    if args.command == "prepare":
        session = prepare_semantic_session(guid=args.guid, work_dir=args.work_dir)
        print(
            f"prepared source_id={session.source_id} guid={session.guid} work_dir={args.work_dir}",
            file=sys.stderr,
        )
        return 0

    if args.command == "render":
        render_semantic_transcript(work_dir=args.work_dir, output=sys.stdout)
        return 0

    session = cleanup_semantic_session(work_dir=args.work_dir)
    print(
        f"cleaned source_id={session.source_id} guid={session.guid} work_dir={args.work_dir}",
        file=sys.stderr,
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
