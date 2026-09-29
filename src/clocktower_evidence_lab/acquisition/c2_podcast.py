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

_PRIOR_SCOUT_ARTIFACTS_BY_GUID = {
    "bf668470-a3fe-41d3-85e8-d028a63cf593": (
        "docs/C0_TB_CULT_OF_CLOCKTOWER_DRUNK_RATIONALE_PILOT_2026-09-28.md"
    ),
    "1d03c939-76bb-3f58-5d86-cd6746d9b0a3": (
        "docs/C0_TB_CULT_OF_CLOCKTOWER_LIBRARIAN_RATIONALE_SCOUT_2026-09-28.md"
    ),
    "e4b8704a-19d7-5c9f-e483-a659be61cc46": (
        "docs/C0_TB_CULT_OF_CLOCKTOWER_RECLUSE_RATIONALE_SCOUT_2026-09-28.md"
    ),
}


def build_c2_manifest(
    episodes: Iterable[PodcastEpisode],
) -> PodcastEpisodeManifest:
    """Build the current C2 manifest and retain stable prior-scout workflow state."""

    materialized = tuple(episodes)
    prior_processing = tuple(
        PriorEpisodeProcessing(
            source_id=stable_episode_id(episode),
            acquisition_state=AcquisitionState.COMPLETE,
            asr_state=AsrState.COMPLETE,
            extraction_state=ExtractionState.COMPLETE,
            human_review_state=HumanReviewState.PENDING,
            artifact_path=_PRIOR_SCOUT_ARTIFACTS_BY_GUID[episode.guid],
        )
        for episode in materialized
        if episode.guid in _PRIOR_SCOUT_ARTIFACTS_BY_GUID
    )
    return build_episode_manifest(
        materialized,
        prior_processing=prior_processing,
    )
