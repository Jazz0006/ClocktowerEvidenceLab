"""CLI for temporary full-transcript semantic-review sessions."""

import argparse
import sys
from collections.abc import Sequence
from pathlib import Path

from clocktower_evidence_lab.acquisition.podcast_semantic import (
    cleanup_current_semantic_session,
    cleanup_semantic_session,
    prepare_next_semantic_session,
    prepare_semantic_session,
    render_current_semantic_transcript,
    render_current_semantic_window,
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

    prepare_next = subparsers.add_parser("prepare-next")
    prepare_next.add_argument("--queue-root", type=Path, required=True)

    render_current = subparsers.add_parser("render-current")
    render_current.add_argument("--queue-root", type=Path, required=True)

    render_window = subparsers.add_parser("render-current-window")
    render_window.add_argument("--queue-root", type=Path, required=True)
    render_window.add_argument("--start-ms", type=int, required=True)
    render_window.add_argument("--end-ms", type=int, required=True)

    cleanup_current = subparsers.add_parser("cleanup-current")
    cleanup_current.add_argument("--queue-root", type=Path, required=True)

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

    if args.command == "cleanup":
        session = cleanup_semantic_session(work_dir=args.work_dir)
        print(
            f"cleaned source_id={session.source_id} guid={session.guid} work_dir={args.work_dir}",
            file=sys.stderr,
        )
        return 0

    if args.command == "prepare-next":
        session = prepare_next_semantic_session(queue_root=args.queue_root)
        print(
            f"prepared-next source_id={session.source_id} guid={session.guid} "
            f"queue_root={args.queue_root}",
            file=sys.stderr,
        )
        return 0

    if args.command == "render-current":
        render_current_semantic_transcript(queue_root=args.queue_root, output=sys.stdout)
        return 0

    if args.command == "render-current-window":
        render_current_semantic_window(
            queue_root=args.queue_root,
            start_ms=args.start_ms,
            end_ms=args.end_ms,
            output=sys.stdout,
        )
        return 0

    session = cleanup_current_semantic_session(queue_root=args.queue_root)
    print(
        f"cleaned-current source_id={session.source_id} guid={session.guid} "
        f"queue_root={args.queue_root}",
        file=sys.stderr,
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
