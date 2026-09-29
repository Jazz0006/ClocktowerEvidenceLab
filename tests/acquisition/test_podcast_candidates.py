import pytest

from clocktower_evidence_lab.acquisition import asr, podcast_candidates, podcast_manifest


def _segments() -> tuple[asr.TranscriptSegment, ...]:
    return (
        asr.TranscriptSegment(
            index=0,
            start_ms=1_000,
            end_ms=2_000,
            text="first machine transcript segment",
        ),
        asr.TranscriptSegment(
            index=1,
            start_ms=2_100,
            end_ms=4_000,
            text="second machine transcript segment",
        ),
    )


def test_materialize_candidate_preserves_timestamp_span_without_transcript_text() -> None:
    proposal = podcast_candidates.CandidateProposal(
        segment_indexes=(0, 1),
        category=podcast_candidates.CandidateCategory.STORYTELLER_RATIONALE,
        summary="Potential rationale for selecting a Drunk target.",
        tags=("drunk", "setup"),
        extraction_confidence=0.8,
    )

    artifact = podcast_candidates.materialize_candidate_artifact(
        source_id="podcast:example",
        segments=_segments(),
        proposals=(proposal,),
    )
    candidate = artifact.candidates[0]

    assert candidate.source_id == "podcast:example"
    assert candidate.start_ms == 1_000
    assert candidate.end_ms == 4_000
    assert candidate.category is podcast_candidates.CandidateCategory.STORYTELLER_RATIONALE
    assert candidate.human_review_state is podcast_manifest.HumanReviewState.NOT_STARTED

    dumped = artifact.model_dump(mode="json")
    assert dumped["extraction_state"] == "COMPLETE"
    assert "transcript_text" not in dumped["candidates"][0]
    assert "segments" not in dumped["candidates"][0]
    assert "first machine transcript segment" not in artifact.model_dump_json()


def test_zero_candidate_episode_is_a_normal_completed_extraction() -> None:
    artifact = podcast_candidates.materialize_candidate_artifact(
        source_id="podcast:example",
        segments=_segments(),
        proposals=(),
    )

    assert artifact.extraction_state is podcast_manifest.ExtractionState.NO_USEFUL_CANDIDATES
    assert artifact.candidates == ()


def test_extraction_complete_does_not_promote_human_review() -> None:
    proposal = podcast_candidates.CandidateProposal(
        segment_indexes=(1,),
        category=podcast_candidates.CandidateCategory.PLAYER_AGENCY,
        summary="Potential player-agency discussion.",
    )

    artifact = podcast_candidates.materialize_candidate_artifact(
        source_id="podcast:example",
        segments=_segments(),
        proposals=(proposal,),
    )

    assert artifact.extraction_state is podcast_manifest.ExtractionState.COMPLETE
    assert (
        artifact.candidates[0].human_review_state
        is podcast_manifest.HumanReviewState.NOT_STARTED
    )


def test_candidate_materialization_rejects_unknown_segment_index() -> None:
    proposal = podcast_candidates.CandidateProposal(
        segment_indexes=(99,),
        category=podcast_candidates.CandidateCategory.REAL_GAME_EXAMPLE,
        summary="Potential example.",
    )

    with pytest.raises(ValueError, match="unknown transcript segment index"):
        podcast_candidates.materialize_candidate_artifact(
            source_id="podcast:example",
            segments=_segments(),
            proposals=(proposal,),
        )


def test_candidate_timestamp_range_is_deterministic_for_reordered_indexes() -> None:
    first = podcast_candidates.CandidateProposal(
        segment_indexes=(0, 1),
        category=podcast_candidates.CandidateCategory.INFORMATION_STRENGTH,
        summary="Potential information-strength discussion.",
    )
    reordered = first.model_copy(update={"segment_indexes": (1, 0)})

    first_artifact = podcast_candidates.materialize_candidate_artifact(
        source_id="podcast:example",
        segments=_segments(),
        proposals=(first,),
    )
    reordered_artifact = podcast_candidates.materialize_candidate_artifact(
        source_id="podcast:example",
        segments=_segments(),
        proposals=(reordered,),
    )

    assert first_artifact.candidates[0].start_ms == reordered_artifact.candidates[0].start_ms
    assert first_artifact.candidates[0].end_ms == reordered_artifact.candidates[0].end_ms
