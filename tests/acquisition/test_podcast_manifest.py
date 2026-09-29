from clocktower_evidence_lab.acquisition import podcast, podcast_manifest

_FEED_URL = "https://anchor.fm/s/daf1f9c/podcast/rss"


def _episode(
    *,
    title: str,
    guid: str | None,
    audio_url: str | None = "https://example.test/audio.mp3",
    webpage_url: str | None = "https://example.test/episode",
) -> podcast.PodcastEpisode:
    return podcast.PodcastEpisode(
        feed_url=_FEED_URL,
        title=title,
        guid=guid,
        webpage_url=webpage_url,
        audio_url=audio_url,
    )


def test_stable_episode_id_uses_guid_not_mutable_title() -> None:
    original = _episode(
        title="16: Drunk (Trouble Brewing)",
        guid="bf668470-a3fe-41d3-85e8-d028a63cf593",
    )
    renamed = original.model_copy(update={"title": "16: The Drunk (Trouble Brewing)"})

    assert podcast_manifest.stable_episode_id(original) == podcast_manifest.stable_episode_id(\n        renamed\n    )


def test_stable_episode_id_falls_back_to_audio_locator_not_title() -> None:
    first = _episode(
        title="Episode title one",
        guid=None,
        audio_url="https://example.test/stable-audio.mp3",
        webpage_url=None,
    )
    renamed = first.model_copy(update={"title": "Episode title two"})

    assert podcast_manifest.stable_episode_id(first) == podcast_manifest.stable_episode_id(renamed)


def test_repeated_feed_reads_deduplicate_by_stable_identity() -> None:
    original = _episode(
        title="16: Drunk (Trouble Brewing)",
        guid="same-guid",
    )
    refreshed = original.model_copy(update={"title": "16: Updated Drunk (Trouble Brewing)"})

    episode_manifest = podcast_manifest.build_episode_manifest((original, refreshed))

    assert len(episode_manifest.episodes) == 1
    assert episode_manifest.episodes[0].title == refreshed.title


def test_trouble_brewing_title_variants_are_in_scope() -> None:
    assert (
        podcast_manifest.classify_trouble_brewing(
            "4.1: Trouble Brewing Revisited (Clocktower Con 2023)"
        )
        is podcast_manifest.EpisodeScope.IN_SCOPE
    )
    assert (
        podcast_manifest.classify_trouble_brewing(
            "24: Beggar and Gunslinger (Trouble Brewing Travelers Part 1)"
        )
        is podcast_manifest.EpisodeScope.IN_SCOPE
    )


def test_other_explicit_scripts_are_out_of_scope() -> None:
    assert (
        podcast_manifest.classify_trouble_brewing("3.19: Chambermaid (Bad Moon Rising)")
        is podcast_manifest.EpisodeScope.OUT_OF_SCOPE
    )
    assert (
        podcast_manifest.classify_trouble_brewing("2.1: Sects and Violets Crash Course")
        is podcast_manifest.EpisodeScope.OUT_OF_SCOPE
    )


def test_manifest_preserves_locators_and_independent_workflow_states() -> None:
    episode = _episode(
        title="15: Chef (Trouble Brewing)",
        guid="chef-guid",
    )

    episode_manifest = podcast_manifest.build_episode_manifest((episode,))
    entry = episode_manifest.episodes[0]

    assert entry.source_id == podcast_manifest.stable_episode_id(episode)
    assert entry.scope is podcast_manifest.EpisodeScope.IN_SCOPE
    assert entry.webpage_url == episode.webpage_url
    assert entry.audio_url == episode.audio_url
    assert entry.transcript_availability is podcast_manifest.TranscriptAvailability.NOT_ADVERTISED
    assert entry.acquisition_state is podcast_manifest.AcquisitionState.NOT_ATTEMPTED
    assert entry.asr_state is podcast_manifest.AsrState.NOT_ATTEMPTED
    assert entry.extraction_state is podcast_manifest.ExtractionState.NOT_ATTEMPTED
    assert entry.human_review_state is podcast_manifest.HumanReviewState.NOT_STARTED


def test_prior_processing_is_applied_by_stable_source_id_not_title() -> None:
    episode = _episode(
        title="16: Renamed Drunk Episode (Trouble Brewing)",
        guid="bf668470-a3fe-41d3-85e8-d028a63cf593",
    )
    prior = podcast_manifest.PriorEpisodeProcessing(
        source_id=podcast_manifest.stable_episode_id(episode),
        acquisition_state=podcast_manifest.AcquisitionState.COMPLETE,
        asr_state=podcast_manifest.AsrState.COMPLETE,
        extraction_state=podcast_manifest.ExtractionState.COMPLETE,
        human_review_state=podcast_manifest.HumanReviewState.PENDING,
        artifact_path="docs/C0_TB_CULT_OF_CLOCKTOWER_DRUNK_RATIONALE_PILOT_2026-09-28.md",
    )

    episode_manifest = podcast_manifest.build_episode_manifest(
        (episode,),
        prior_processing=(prior,),
    )
    entry = episode_manifest.episodes[0]

    assert entry.acquisition_state is podcast_manifest.AcquisitionState.COMPLETE
    assert entry.asr_state is podcast_manifest.AsrState.COMPLETE
    assert entry.extraction_state is podcast_manifest.ExtractionState.COMPLETE
    assert entry.human_review_state is podcast_manifest.HumanReviewState.PENDING
    assert entry.prior_artifact_path == prior.artifact_path
    assert podcast_manifest.active_acquisition_queue(episode_manifest) == ()


def test_out_of_scope_episode_remains_in_inventory_but_not_active_queue() -> None:
    episode = _episode(
        title="3.19: Chambermaid (Bad Moon Rising)",
        guid="bmr-guid",
    )

    episode_manifest = podcast_manifest.build_episode_manifest((episode,))

    assert episode_manifest.episodes[0].scope is podcast_manifest.EpisodeScope.OUT_OF_SCOPE
    assert podcast_manifest.active_acquisition_queue(episode_manifest) == ()


def test_unknown_scope_episode_is_not_automatically_queued() -> None:
    episode = _episode(
        title="Special episode without a script marker",
        guid="special-guid",
    )

    episode_manifest = podcast_manifest.build_episode_manifest((episode,))

    assert episode_manifest.episodes[0].scope is podcast_manifest.EpisodeScope.UNKNOWN
    assert podcast_manifest.active_acquisition_queue(episode_manifest) == ()


def test_in_scope_episode_with_audio_and_no_transcript_enters_acquisition_queue() -> None:
    episode = _episode(
        title="1: Washerwoman (Trouble Brewing)",
        guid="washerwoman-guid",
    )

    episode_manifest = podcast_manifest.build_episode_manifest((episode,))

    assert podcast_manifest.active_acquisition_queue(episode_manifest) == (
        episode_manifest.episodes[0],
    )


def test_asr_and_extraction_complete_do_not_imply_human_review_complete() -> None:
    episode = _episode(
        title="6: Recluse (Trouble Brewing)",
        guid="recluse-guid",
    )
    prior = podcast_manifest.PriorEpisodeProcessing(
        source_id=podcast_manifest.stable_episode_id(episode),
        acquisition_state=podcast_manifest.AcquisitionState.COMPLETE,
        asr_state=podcast_manifest.AsrState.COMPLETE,
        extraction_state=podcast_manifest.ExtractionState.NO_USEFUL_CANDIDATES,
        human_review_state=podcast_manifest.HumanReviewState.NOT_STARTED,
    )

    entry = podcast_manifest.build_episode_manifest(
        (episode,),
        prior_processing=(prior,),
    ).episodes[0]

    assert entry.asr_state is podcast_manifest.AsrState.COMPLETE
    assert entry.extraction_state is podcast_manifest.ExtractionState.NO_USEFUL_CANDIDATES
    assert entry.human_review_state is podcast_manifest.HumanReviewState.NOT_STARTED


def test_manifest_serialization_contains_only_lightweight_locator_metadata() -> None:
    episode = _episode(
        title="2: Librarian (Trouble Brewing)",
        guid="librarian-guid",
    )

    dumped = podcast_manifest.build_episode_manifest((episode,)).model_dump(mode="json")
    entry = dumped["episodes"][0]

    assert entry["audio_url"] == "https://example.test/audio.mp3"
    assert "audio_bytes" not in entry
    assert "transcript_text" not in entry
    assert "segments" not in entry
