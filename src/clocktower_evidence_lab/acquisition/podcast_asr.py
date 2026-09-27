"""CLI for producing a local timestamped ASR acquisition artifact."""

import argparse
from collections.abc import Sequence
from pathlib import Path

from clocktower_evidence_lab.acquisition.asr import transcribe_audio


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        description="Transcribe local podcast audio into a timestamped JSON acquisition artifact."
    )
    parser.add_argument("audio_path", type=Path)
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--model", default="small.en")
    parser.add_argument("--device", default="cpu")
    parser.add_argument("--compute-type", default="int8")
    parser.add_argument("--language", default="en")
    parser.add_argument("--beam-size", type=int, default=5)
    args = parser.parse_args(argv)

    transcript = transcribe_audio(
        args.audio_path,
        model_name=args.model,
        device=args.device,
        compute_type=args.compute_type,
        language=args.language,
        beam_size=args.beam_size,
    )
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(
        transcript.model_dump_json(indent=2) + "\n",
        encoding="utf-8",
    )
    print(
        f"wrote {len(transcript.segments)} timestamped ASR segments to {args.output}"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
