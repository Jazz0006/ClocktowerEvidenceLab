from pathlib import Path

from clocktower_evidence_lab.acquisition import (
    podcast_candidates,
    podcast_manifest,
    podcast_review_cli,
)


def test_review_cli_converts_candidate_artifact_to_bounded_packet(
    tmp_path: Path,
) -> None:
    artifact = podcast_candidates.CandidateArtifact(
        source_id="podcast:example",
        extraction_state=podcast_manifest.ExtractionState.COMPLETE,
        candidates=(
            podcast_candidates.MachineCandidate(
                source_id="podcast:example",
                start_ms=10_000,
                end_ms=20_000,
                category=podcast_candidates.CandidateCategory.STORYTELLER_RATIONALE,
                summary="Potential Storyteller rationale.",
                extraction_confidence=0.4,
            ),
        ),
    )
    input_path = tmp_path / "candidates.json"
    output_path = tmp_path / "review.json"
    input_path.write_text(artifact.model_dump_json(indent=2), encoding="utf-8")

    result = podcast_review_cli.main(
        [
            str(input_path),
            "--output",
            str(output_path),
            "--max-windows",
            "3",
            "--max-review-seconds",
            "120",
        ]
    )

    payload = output_path.read_text(encoding="utf-8")
    assert result == 0
    assert '"schema_version": "c2d-review-packet-v1"' in payload
    assert '"priority": "P0"' in payload
    assert '"human_review_state": "NOT_STARTED"' in payload
