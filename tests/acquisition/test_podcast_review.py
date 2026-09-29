from clocktower_evidence_lab.acquisition import podcast_candidates, podcast_manifest, podcast_review


def _candidate(
    start_ms: int,
    end_ms: int,
    category: podcast_candidates.CandidateCategory,
    *,
    confidence: float = 0.4,
    summary: str = "Machine-located candidate.",
    tags: tuple[str, ...] = (),
) -> podcast_candidates.MachineCandidate:
    return podcast_candidates.MachineCandidate(
        source_id="podcast:example",
        start_ms=start_ms,
        end_ms=end_ms,
        category=category,
        summary=summary,
        tags=tags,
        extraction_confidence=confidence,
    )


def _artifact(
    candidates: tuple[podcast_candidates.MachineCandidate, ...],
) -> podcast_candidates.CandidateArtifact:
    return podcast_candidates.CandidateArtifact(
        source_id="podcast:example",
        extraction_state=(
            podcast_manifest.ExtractionState.COMPLETE
            if candidates
            else podcast_manifest.ExtractionState.NO_USEFUL_CANDIDATES
        ),
        candidates=candidates,
    )


def test_review_packet_merges_overlapping_and_nearby_candidates() -> None:
    artifact = _artifact(
        (
            _candidate(
                10_000,
                20_000,
                podcast_candidates.CandidateCategory.STORYTELLER_RATIONALE,
                tags=("rationale",),
            ),
            _candidate(
                22_000,
                30_000,
                podcast_candidates.CandidateCategory.EXPLICIT_ALTERNATIVE,
                tags=("alternative",),
            ),
            _candidate(
                50_000,
                55_000,
                podcast_candidates.CandidateCategory.PLAYER_EXPERIENCE,
            ),
        )
    )

    packet = podcast_review.build_review_packet(
        artifact,
        merge_gap_ms=3_000,
        max_windows=10,
        max_review_ms=600_000,
    )

    assert len(packet.windows) == 2
    merged = packet.windows[0]
    assert merged.start_ms == 10_000
    assert merged.end_ms == 30_000
    assert merged.categories == (
        podcast_candidates.CandidateCategory.STORYTELLER_RATIONALE,
        podcast_candidates.CandidateCategory.EXPLICIT_ALTERNATIVE,
    )
    assert merged.candidate_count == 2
    assert set(merged.tags) == {"rationale", "alternative"}


def test_review_packet_prioritizes_direct_rationale_over_generic_discovery() -> None:
    artifact = _artifact(
        (
            _candidate(
                10_000,
                15_000,
                podcast_candidates.CandidateCategory.REAL_GAME_EXAMPLE,
                confidence=0.9,
            ),
            _candidate(
                30_000,
                35_000,
                podcast_candidates.CandidateCategory.STORYTELLER_RATIONALE,
                confidence=0.3,
            ),
        )
    )

    packet = podcast_review.build_review_packet(
        artifact,
        merge_gap_ms=0,
        max_windows=1,
        max_review_ms=600_000,
    )

    assert len(packet.windows) == 1
    assert packet.windows[0].categories == (
        podcast_candidates.CandidateCategory.STORYTELLER_RATIONALE,
    )
    assert packet.windows[0].priority is podcast_review.ReviewPriority.P0


def test_review_packet_respects_window_and_time_budget_deterministically() -> None:
    artifact = _artifact(
        (
            _candidate(
                0,
                30_000,
                podcast_candidates.CandidateCategory.STORYTELLER_RATIONALE,
            ),
            _candidate(
                60_000,
                90_000,
                podcast_candidates.CandidateCategory.REGISTRATION_CHOICE,
            ),
            _candidate(
                120_000,
                150_000,
                podcast_candidates.CandidateCategory.INFORMATION_STRENGTH,
            ),
        )
    )

    first = podcast_review.build_review_packet(
        artifact,
        merge_gap_ms=0,
        max_windows=3,
        max_review_ms=65_000,
    )
    second = podcast_review.build_review_packet(
        artifact,
        merge_gap_ms=0,
        max_windows=3,
        max_review_ms=65_000,
    )

    assert first == second
    assert len(first.windows) == 2
    assert first.total_review_ms == 60_000


def test_review_packet_does_not_claim_human_review_or_copy_transcript_text() -> None:
    artifact = _artifact(
        (
            _candidate(
                10_000,
                20_000,
                podcast_candidates.CandidateCategory.MISINFORMATION_POLICY,
                summary="Potential misinformation-policy discussion.",
            ),
        )
    )

    packet = podcast_review.build_review_packet(artifact)
    dumped = packet.model_dump(mode="json")

    assert packet.human_review_state is podcast_manifest.HumanReviewState.NOT_STARTED
    assert dumped["windows"][0]["machine_summaries"] == [
        "Potential misinformation-policy discussion."
    ]
    assert "transcript_text" not in packet.model_dump_json()
    assert "segments" not in packet.model_dump_json()


def test_zero_candidate_artifact_produces_empty_review_packet() -> None:
    packet = podcast_review.build_review_packet(_artifact(()))

    assert packet.windows == ()
    assert packet.total_review_ms == 0
    assert packet.source_candidate_count == 0
    assert packet.selected_candidate_count == 0
    assert packet.human_review_state is podcast_manifest.HumanReviewState.NOT_STARTED


def test_review_packet_writer_serializes_lightweight_packet(
    tmp_path,
) -> None:
    artifact = _artifact(
        (
            _candidate(
                10_000,
                20_000,
                podcast_candidates.CandidateCategory.STORYTELLER_RATIONALE,
            ),
        )
    )
    packet = podcast_review.build_review_packet(artifact)
    output = tmp_path / "review.json"

    written = podcast_review.write_review_packet(packet, output)

    payload = written.read_text(encoding="utf-8")
    assert written == output
    assert '"schema_version": "c2d-review-packet-v1"' in payload
    assert '"human_review_state": "NOT_STARTED"' in payload
    assert "transcript_text" not in payload
