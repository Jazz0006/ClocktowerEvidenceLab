"""Current C2 Cult of the Clocktower podcast batch configuration."""

from collections.abc import Iterable

from clocktower_evidence_lab.acquisition.podcast import PodcastEpisode
from clocktower_evidence_lab.acquisition.podcast_manifest import (
    AcquisitionState,
    AsrState,
    ExtractionState,
    HumanReviewState,
    PodcastEpisodeManifest,
    PriorEpisodeProcessing,
    build_episode_manifest,
    stable_episode_id,
)

CULT_OF_CLOCKTOWER_FEED_URL = "https://anchor.fm/s/daf1f9c/podcast/rss"

_PRIOR_PROCESSING_BY_GUID = {
    "bf668470-a3fe-41d3-85e8-d028a63cf593": (
        "docs/C0_TB_CULT_OF_CLOCKTOWER_DRUNK_RATIONALE_PILOT_2026-09-28.md",
        HumanReviewState.PENDING,
    ),
    "1d03c939-76bb-3f58-5d86-cd6746d9b0a3": (
        "docs/C0_TB_CULT_OF_CLOCKTOWER_LIBRARIAN_RATIONALE_SCOUT_2026-09-28.md",
        HumanReviewState.PENDING,
    ),
    "e4b8704a-19d7-5c9f-e483-a659be61cc46": (
        "docs/C0_TB_CULT_OF_CLOCKTOWER_RECLUSE_RATIONALE_SCOUT_2026-09-28.md",
        HumanReviewState.PENDING,
    ),
    "5722d8e8-b89d-4067-91ac-1550b8da428d": (
        "docs/C2D_PRIMARY_AUDIO_REVIEW_QUEUE_2026-09-30.md",
        HumanReviewState.NOT_STARTED,
    ),
    "a271357d-10af-4969-8c7e-5545b871b5cb": (
        "docs/C2D_PRIMARY_AUDIO_REVIEW_QUEUE_2026-09-30.md",
        HumanReviewState.NOT_STARTED,
    ),
}


def build_c2_manifest(
    episodes: Iterable[PodcastEpisode],
) -> PodcastEpisodeManifest:
    """Build the current C2 manifest and retain stable prior-processing workflow state."""

    materialized = tuple(episodes)
    prior_processing = tuple(
        PriorEpisodeProcessing(
            source_id=stable_episode_id(episode),
            acquisition_state=AcquisitionState.COMPLETE,
            asr_state=AsrState.COMPLETE,
            extraction_state=ExtractionState.COMPLETE,
            human_review_state=_PRIOR_PROCESSING_BY_GUID[episode.guid][1],
            artifact_path=_PRIOR_PROCESSING_BY_GUID[episode.guid][0],
        )
        for episode in materialized
        if episode.guid in _PRIOR_PROCESSING_BY_GUID
    )
    return build_episode_manifest(
        materialized,
        prior_processing=prior_processing,
    )
