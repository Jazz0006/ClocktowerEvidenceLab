from clocktower_evidence_lab.acquisition.c2_podcast import build_c2_manifest
from clocktower_evidence_lab.acquisition.podcast import PodcastEpisode
from clocktower_evidence_lab.acquisition.podcast_manifest import (
    AcquisitionState,
    AsrState,
    ExtractionState,
    HumanReviewState,
    active_acquisition_queue,
)


_FEED_URL = "https://anchor.fm/s/daf1f9c/podcast/rss"


def _episode(title: str, guid: str) -> PodcastEpisode:
    return PodcastEpisode(
        feed_url=_FEED_URL,
        title=title,
        guid=guid,
        audio_url=f"https://example.test/{guid}.mp3",
    )


def test_c2_manifest_recognizes_retained_drunk_librarian_recluse_scouts() -> None:
    episodes = (
        _episode(
            "16: Drunk renamed (Trouble Brewing)",
            "bf668470-a3fe-41d3-85e8-d028a63cf593",
        ),
        _episode(
            "8: Librarian renamed (Trouble Brewing)",
            "1d03c939-76bb-3f58-5d86-cd6746d9b0a3",
        ),
        _episode(
            "6: Recluse renamed (Trouble Brewing)",
            "e4b8704a-19d7-5c9f-e483-a659be61cc46",
        ),
        _episode("15: Chef (Trouble Brewing)", "new-chef-guid"),
    )

    manifest = build_c2_manifest(episodes)

    processed = manifest.episodes[:3]
    assert all(entry.acquisition_state is AcquisitionState.COMPLETE for entry in processed)
    assert all(entry.asr_state is AsrState.COMPLETE for entry in processed)
    assert all(entry.extraction_state is ExtractionState.COMPLETE for entry in processed)
    assert all(entry.human_review_state is HumanReviewState.PENDING for entry in processed)
    assert all(entry.prior_artifact_path for entry in processed)

    assert active_acquisition_queue(manifest) == (manifest.episodes[3],)
