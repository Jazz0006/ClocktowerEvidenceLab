"""CLI for converting external ASR artifacts into lightweight C2C candidates."""

import argparse
from collections.abc import Sequence
from pathlib import Path

from clocktower_evidence_lab.acquisition.asr import AsrTranscript
from clocktower_evidence_lab.acquisition.podcast_candidates import (
    extract_asr_candidate_artifact,
    write_candidate_artifact,
)


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        description="Extract lightweight C2C candidates from an external ASR JSON artifact."
    )
    parser.add_argument("asr_json", type=Path)
    parser.add_argument("--source-id", required=True)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args(argv)

    transcript = AsrTranscript.model_validate_json(args.asr_json.read_text(encoding="utf-8"))
    artifact = extract_asr_candidate_artifact(
        source_id=args.source_id,
        transcript=transcript,
    )
    write_candidate_artifact(artifact, args.output)

    print(f"candidates={len(artifact.candidates)} extraction_state={artifact.extraction_state}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
