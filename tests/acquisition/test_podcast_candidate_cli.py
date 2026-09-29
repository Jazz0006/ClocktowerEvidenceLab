from pathlib import Path

from clocktower_evidence_lab.acquisition import asr, podcast_candidate_cli


def test_candidate_cli_converts_external_asr_to_lightweight_candidate_json(
    tmp_path: Path,
) -> None:
    transcript = asr.AsrTranscript(
        model_name="small.en",
        language="en",
        segments=(
            asr.TranscriptSegment(
                index=0,
                start_ms=1_000,
                end_ms=2_000,
                text="The Recluse can register as evil for the Investigator.",
            ),
        ),
    )
    asr_path = tmp_path / "asr.json"
    output_path = tmp_path / "candidates.json"
    asr_path.write_text(transcript.model_dump_json(indent=2), encoding="utf-8")

    result = podcast_candidate_cli.main(
        [
            str(asr_path),
            "--source-id",
            "podcast:example",
            "--output",
            str(output_path),
        ]
    )

    payload = output_path.read_text(encoding="utf-8")
    assert result == 0
    assert '"source_id": "podcast:example"' in payload
    assert '"category": "REGISTRATION_CHOICE"' in payload
    assert "The Recluse can register as evil" not in payload
