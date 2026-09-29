"""CLI for building bounded C2D human-review packets from machine candidates."""

import argparse
from collections.abc import Sequence
from pathlib import Path

from clocktower_evidence_lab.acquisition.podcast_candidates import CandidateArtifact
from clocktower_evidence_lab.acquisition.podcast_review import (
    build_review_packet,
    write_review_packet,
)


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        description="Build a bounded C2D primary-audio review packet from C2C candidates."
    )
    parser.add_argument("candidate_json", type=Path)
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--merge-gap-ms", type=int, default=5_000)
    parser.add_argument("--max-windows", type=int, default=12)
    parser.add_argument("--max-review-seconds", type=int, default=600)
    args = parser.parse_args(argv)

    artifact = CandidateArtifact.model_validate_json(
        args.candidate_json.read_text(encoding="utf-8")
    )
    packet = build_review_packet(
        artifact,
        merge_gap_ms=args.merge_gap_ms,
        max_windows=args.max_windows,
        max_review_ms=args.max_review_seconds * 1_000,
    )
    write_review_packet(packet, args.output)

    print(
        (
            f"windows={len(packet.windows)} "
            f"selected_candidates={packet.selected_candidate_count} "
            f"review_seconds={packet.total_review_ms / 1_000:.1f} "
            f"human_review_state={packet.human_review_state}"
        )
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
