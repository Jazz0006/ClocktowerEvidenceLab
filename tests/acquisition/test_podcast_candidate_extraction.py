from pathlib import Path

from clocktower_evidence_lab.acquisition import asr, podcast_candidates


def _segments(*texts: str) -> tuple[asr.TranscriptSegment, ...]:
    return tuple(
        asr.TranscriptSegment(
            index=index,
            start_ms=index * 1_000,
            end_ms=(index + 1) * 1_000,
            text=text,
        )
        for index, text in enumerate(texts)
    )


def test_rule_locator_requires_every_term_group() -> None:
    rule = podcast_candidates.CandidateRule(
        rule_id="registration-rationale",
        category=podcast_candidates.CandidateCategory.REGISTRATION_CHOICE,
        term_groups=(("recluse", "spy"), ("register", "registration")),
        summary="Keyword-located potential registration-choice discussion.",
        tags=("registration",),
    )

    proposals = podcast_candidates.locate_rule_candidates(
        _segments(
            "The Recluse is difficult.",
            "The Recluse can register as evil here.",
        ),
        rules=(rule,),
    )

    assert len(proposals) == 1
    assert proposals[0].segment_indexes == (1,)
    assert proposals[0].category is podcast_candidates.CandidateCategory.REGISTRATION_CHOICE


def test_rule_locator_can_include_bounded_context_without_copying_text() -> None:
    rule = podcast_candidates.CandidateRule(
        rule_id="rationale",
        category=podcast_candidates.CandidateCategory.STORYTELLER_RATIONALE,
        term_groups=(("storyteller",), ("because", "reason", "why")),
        summary="Keyword-located potential Storyteller rationale.",
        context_before=1,
        context_after=1,
    )
    segments = _segments(
        "Previous context.",
        "As the Storyteller, I choose this because it changes the worlds.",
        "Following context.",
    )

    proposals = podcast_candidates.locate_rule_candidates(segments, rules=(rule,))

    assert proposals[0].segment_indexes == (0, 1, 2)
    assert proposals[0].summary == "Keyword-located potential Storyteller rationale."
    assert "changes the worlds" not in proposals[0].model_dump_json()


def test_rule_locator_is_deterministic_and_returns_zero_for_no_match() -> None:
    rule = podcast_candidates.CandidateRule(
        rule_id="bluff",
        category=podcast_candidates.CandidateCategory.DEMON_BLUFF_REASONING,
        term_groups=(("demon",), ("bluff", "bluffs")),
        summary="Keyword-located potential Demon-bluff discussion.",
    )
    segments = _segments("General discussion with no target terms.")

    first = podcast_candidates.locate_rule_candidates(segments, rules=(rule,))
    second = podcast_candidates.locate_rule_candidates(segments, rules=(rule,))

    assert first == second == ()


def test_default_c2_rules_locate_registration_and_explicit_alternative_windows() -> None:
    proposals = podcast_candidates.locate_rule_candidates(
        _segments(
            "The Recluse can register as evil for the Investigator.",
            "Instead, you could show the real Minion and give them another explanation.",
        )
    )

    categories = {proposal.category for proposal in proposals}

    assert podcast_candidates.CandidateCategory.REGISTRATION_CHOICE in categories
    assert podcast_candidates.CandidateCategory.EXPLICIT_ALTERNATIVE in categories


def test_extract_asr_candidate_artifact_and_writer_keep_transcript_outside_output(
    tmp_path: Path,
) -> None:
    transcript = asr.AsrTranscript(
        model_name="small.en",
        language="en",
        segments=_segments(
            "The Recluse can register as evil for the Investigator.",
            "Instead, you could show the real Minion.",
        ),
    )

    artifact = podcast_candidates.extract_asr_candidate_artifact(
        source_id="podcast:example",
        transcript=transcript,
    )
    output = tmp_path / "candidates.json"
    podcast_candidates.write_candidate_artifact(artifact, output)

    payload = output.read_text(encoding="utf-8")
    assert artifact.candidates
    assert '"source_id": "podcast:example"' in payload
    assert "The Recluse can register as evil" not in payload
    assert "Instead, you could show the real Minion" not in payload


def test_rule_locator_matches_required_term_groups_across_adjacent_segments() -> None:
    rule = podcast_candidates.CandidateRule(
        rule_id="split-rationale",
        category=podcast_candidates.CandidateCategory.STORYTELLER_RATIONALE,
        term_groups=(("storyteller",), ("because", "reason", "why")),
        summary="Keyword-located potential Storyteller rationale.",
        context_before=0,
        context_after=0,
    )
    segments = _segments(
        "As the Storyteller, I choose the Recluse here.",
        "Because the Investigator already has very strong information.",
        "Unrelated later discussion.",
    )

    proposals = podcast_candidates.locate_rule_candidates(segments, rules=(rule,))

    assert len(proposals) == 1
    assert proposals[0].segment_indexes == (0, 1)


def test_rule_locator_deduplicates_overlapping_matches_for_one_rule() -> None:
    rule = podcast_candidates.CandidateRule(
        rule_id="repeated-rationale",
        category=podcast_candidates.CandidateCategory.STORYTELLER_RATIONALE,
        term_groups=(("storyteller",), ("because",)),
        summary="Keyword-located potential Storyteller rationale.",
        context_before=1,
        context_after=1,
    )
    segments = _segments(
        "The Storyteller chooses this because it opens worlds.",
        "The Storyteller may choose it because the table is converging.",
    )

    proposals = podcast_candidates.locate_rule_candidates(segments, rules=(rule,))

    assert len(proposals) == 1
    assert proposals[0].segment_indexes == (0, 1)
