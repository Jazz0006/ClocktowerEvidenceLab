"""CLI for executing C2B podcast acquisition from a C2A manifest."""

import argparse
import sys
from collections.abc import Sequence
from pathlib import Path

from clocktower_evidence_lab.acquisition.podcast_batch import (
    apply_batch_progress,
    build_batch_plan,
    run_batch_plan,
)
from clocktower_evidence_lab.acquisition.podcast_manifest import PodcastEpisodeManifest


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        description="Execute the C2 podcast batch plan in an external work directory."
    )
    parser.add_argument("manifest", type=Path)
    parser.add_argument("--work-dir", type=Path, required=True)
    parser.add_argument("--plan-only", action="store_true")
    parser.add_argument("--guid", action="append", default=[])
    args = parser.parse_args(argv)

    manifest = PodcastEpisodeManifest.model_validate_json(args.manifest.read_text(encoding="utf-8"))
    if args.guid:
        requested_guids = set(args.guid)
        selected = tuple(entry for entry in manifest.episodes if entry.guid in requested_guids)
        found_guids = {entry.guid for entry in selected}
        missing_guids = requested_guids - found_guids
        if missing_guids:
            parser.error(f"GUIDs not present in manifest: {sorted(missing_guids)}")
        manifest = manifest.model_copy(update={"episodes": selected})

    plan = build_batch_plan(manifest)

    if args.plan_only:
        sys.stdout.write(plan.model_dump_json(indent=2) + "\n")
        return 0

    result = run_batch_plan(plan, args.work_dir)
    updated_manifest = apply_batch_progress(manifest, result.progress)

    args.work_dir.mkdir(parents=True, exist_ok=True)
    (args.work_dir / "batch-progress.json").write_text(
        result.model_dump_json(indent=2) + "\n",
        encoding="utf-8",
    )
    (args.work_dir / "manifest.updated.json").write_text(
        updated_manifest.model_dump_json(indent=2) + "\n",
        encoding="utf-8",
    )

    print(
        (
            f"completed={len(result.progress)} "
            f"blocked={len(result.blocked_items)} "
            f"work_dir={args.work_dir}"
        ),
        file=sys.stderr,
    )
    return 2 if result.blocked_items else 0


if __name__ == "__main__":
    raise SystemExit(main())
