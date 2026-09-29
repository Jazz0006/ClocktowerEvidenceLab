"""Stable podcast episode manifest for batch acquisition workflow state."""

from collections.abc import Iterable
from enum import StrEnum
from hashlib import sha256
from typing import Annotated

from pydantic import BaseModel, ConfigDict, Field

from clocktower_evidence_lab.acquisition.podcast import PodcastEpisode

ShortText = Annotated[str, Field(min_length=1, max_length=512)]
ArtifactPath = Annotated[str, Field(min_length=1, max_length=1_024)]


class _ManifestModel(BaseModel):
    model_config = ConfigDict(extra="forbid", frozen=True)


class EpisodeScope(StrEnum):
    """Current-product scope classification for an inventoried episode."""

    IN_SCOPE = "IN_SCOPE"
    OUT_OF_SCOPE = "OUT_OF_SCOPE"
    UNKNOWN = "UNKNOWN"


class TranscriptAvailability(StrEnum):
    """Whether the feed advertises a transcript locator."""

    ADVERTISED = "ADVERTISED"
    NOT_ADVERTISED = "NOT_ADVERTISED"


class AcquisitionState(StrEnum):
    NOT_ATTEMPTED = "NOT_ATTEMPTED"
    COMPLETE = "COMPLETE"
    FAILED = "FAILED"


class AsrState(StrEnum):
    NOT_ATTEMPTED = "NOT_ATTEMPTED"
    NOT_REQUIRED = "NOT_REQUIRED"
    COMPLETE = "COMPLETE"
    FAILED = "FAILED"


class ExtractionState(StrEnum):
    NOT_ATTEMPTED = "NOT_ATTEMPTED"
    COMPLETE = "COMPLETE"
    NO_USEFUL_CANDIDATES = "NO_USEFUL_CANDIDATES"
    FAILED = "FAILED"


class HumanReviewState(StrEnum):
    NOT_STARTED = "NOT_STARTED"
    PENDING = "PENDING"
    COMPLETE = "COMPLETE"


class PriorEpisodeProcessing(_ManifestModel):
    """Previously completed workflow state keyed by stable source identity."""

    source_id: ShortText
    acquisition_state: AcquisitionState = AcquisitionState.NOT_ATTEMPTED
    asr_state: AsrState = AsrState.NOT_ATTEMPTED
    extraction_state: ExtractionState = ExtractionState.NOT_ATTEMPTED
    human_review_state: HumanReviewState = HumanReviewState.NOT_STARTED
    artifact_path: ArtifactPath | None = None


class PodcastManifestEntry(_ManifestModel):
    """Lightweight locator and workflow state for one podcast episode."""

    source_id: ShortText
    show_title: ShortText | None = None
    feed_url: str = Field(min_length=1, max_length=2_048)
    title: ShortText
    guid: ShortText | None = None
    published_at: object | None = None
    duration_seconds: int | None = Field(default=None, ge=0)
    webpage_url: str | None = Field(default=None, min_length=1, max_length=2_048)
    audio_url: str | None = Field(default=None, min_length=1, max_length=2_048)
    transcript_urls: tuple[str, ...] = ()
    transcript_availability: TranscriptAvailability
    scope: EpisodeScope
    acquisition_state: AcquisitionState = AcquisitionState.NOT_ATTEMPTED
    asr_state: AsrState = AsrState.NOT_ATTEMPTED
    extraction_state: ExtractionState = ExtractionState.NOT_ATTEMPTED
    human_review_state: HumanReviewState = HumanReviewState.NOT_STARTED
    prior_artifact_path: ArtifactPath | None = None


class PodcastEpisodeManifest(_ManifestModel):
    """Git-safe batch inventory: locator metadata only, never full media/transcript text."""

    schema_version: str = "c2a-podcast-manifest-v1"
    episodes: tuple[PodcastManifestEntry, ...]


def stable_episode_id(episode: PodcastEpisode) -> str:
    """Return a title-independent stable source identity for an RSS episode."""

    if episode.guid:
        identity_kind = "guid"
        identity_value = episode.guid
        identity_scope = episode.feed_url
    elif episode.audio_url:
        identity_kind = "audio"
        identity_value = episode.audio_url
        identity_scope = ""
    elif episode.webpage_url:
        identity_kind = "webpage"
        identity_value = episode.webpage_url
        identity_scope = ""
    else:
        raise ValueError(
            "podcast episode needs RSS GUID, audio URL, or webpage URL for stable identity"
        )

    digest = sha256(
        "\x00".join((identity_kind, identity_scope, identity_value)).encode("utf-8")
    ).hexdigest()
    return f"podcast:{digest[:32]}"


def classify_trouble_brewing(title: str) -> EpisodeScope:
    """Classify explicit script labels conservatively for the current TB-only scope."""

    normalized = title.casefold()
    if "(trouble brewing)" in normalized:
        return EpisodeScope.IN_SCOPE
    if "(bad moon rising)" in normalized or "(sects & violets)" in normalized:
        return EpisodeScope.OUT_OF_SCOPE
    return EpisodeScope.UNKNOWN


def build_episode_manifest(
    episodes: Iterable[PodcastEpisode],
    *,
    prior_processing: Iterable[PriorEpisodeProcessing] = (),
) -> PodcastEpisodeManifest:
    """Build a deduplicated manifest without media or transcript payload bodies."""

    prior_by_source_id: dict[str, PriorEpisodeProcessing] = {}
    for prior in prior_processing:
        if prior.source_id in prior_by_source_id:
            raise ValueError(f"duplicate prior processing source_id: {prior.source_id}")
        prior_by_source_id[prior.source_id] = prior

    entries_by_source_id: dict[str, PodcastManifestEntry] = {}
    for episode in episodes:
        source_id = stable_episode_id(episode)
        prior = prior_by_source_id.get(source_id)
        entry = PodcastManifestEntry(
            source_id=source_id,
            show_title=getattr(episode, "show_title", None),
            feed_url=episode.feed_url,
            title=episode.title,
            guid=episode.guid,
            published_at=episode.published_at,
            duration_seconds=episode.duration_seconds,
            webpage_url=episode.webpage_url,
            audio_url=episode.audio_url,
            transcript_urls=tuple(reference.url for reference in episode.transcripts),
            transcript_availability=(
                TranscriptAvailability.ADVERTISED
                if episode.transcripts
                else TranscriptAvailability.NOT_ADVERTISED
            ),
            scope=classify_trouble_brewing(episode.title),
            acquisition_state=(
                prior.acquisition_state
                if prior is not None
                else AcquisitionState.NOT_ATTEMPTED
            ),
            asr_state=prior.asr_state if prior is not None else AsrState.NOT_ATTEMPTED,
            extraction_state=(
                prior.extraction_state
                if prior is not None
                else ExtractionState.NOT_ATTEMPTED
            ),
            human_review_state=(
                prior.human_review_state
                if prior is not None
                else HumanReviewState.NOT_STARTED
            ),
            prior_artifact_path=prior.artifact_path if prior is not None else None,
        )
        entries_by_source_id[source_id] = entry

    return PodcastEpisodeManifest(episodes=tuple(entries_by_source_id.values()))


def active_acquisition_queue(
    manifest: PodcastEpisodeManifest,
) -> tuple[PodcastManifestEntry, ...]:
    """Return only current-scope episodes that still require source acquisition."""

    return tuple(
        entry
        for entry in manifest.episodes
        if entry.scope is EpisodeScope.IN_SCOPE
        and entry.acquisition_state is not AcquisitionState.COMPLETE
    )
