"""Podcast RSS probing for expert-rationale source acquisition."""

from collections.abc import Iterable
from datetime import UTC, datetime
from email.utils import parsedate_to_datetime
from typing import Annotated
from xml.etree import ElementTree

from pydantic import BaseModel, ConfigDict, Field

LocatorText = Annotated[str, Field(min_length=1, max_length=2_048)]
ShortText = Annotated[str, Field(min_length=1, max_length=512)]


class _AcquisitionModel(BaseModel):
    model_config = ConfigDict(extra="forbid", frozen=True)


class PodcastTranscriptReference(_AcquisitionModel):
    """A transcript locator advertised by a podcast feed."""

    url: LocatorText
    media_type: ShortText | None = None
    language: ShortText | None = None
    rel: ShortText | None = None


class PodcastEpisode(_AcquisitionModel):
    """Episode metadata needed to locate audio or an advertised transcript."""

    feed_url: LocatorText
    title: ShortText
    guid: ShortText | None = None
    webpage_url: LocatorText | None = None
    published_at: datetime | None = None
    duration_seconds: int | None = Field(default=None, ge=0)
    audio_url: LocatorText | None = None
    transcripts: tuple[PodcastTranscriptReference, ...] = ()


def parse_podcast_rss(xml_text: str, *, feed_url: str) -> tuple[PodcastEpisode, ...]:
    """Parse RSS episode locators without downloading audio or transcript bodies."""

    try:
        root = ElementTree.fromstring(xml_text)
    except ElementTree.ParseError as exc:
        raise ValueError("invalid podcast RSS XML") from exc

    episodes: list[PodcastEpisode] = []
    for item in _iter_elements(root, "item"):
        title = _child_text(item, "title")
        if title is None:
            continue

        enclosure = _first_child(item, "enclosure")
        audio_url = enclosure.attrib.get("url") if enclosure is not None else None

        transcript_refs = tuple(
            PodcastTranscriptReference(
                url=url,
                media_type=element.attrib.get("type"),
                language=element.attrib.get("language"),
                rel=element.attrib.get("rel"),
            )
            for element in _direct_children(item, "transcript")
            if (url := element.attrib.get("url"))
        )

        episodes.append(
            PodcastEpisode(
                feed_url=feed_url,
                title=title,
                guid=_child_text(item, "guid"),
                webpage_url=_child_text(item, "link"),
                published_at=_parse_published_at(_child_text(item, "pubDate")),
                duration_seconds=_parse_duration_seconds(_child_text(item, "duration")),
                audio_url=audio_url,
                transcripts=transcript_refs,
            )
        )

    return tuple(episodes)


def find_episodes(
    episodes: Iterable[PodcastEpisode],
    title_contains: str,
) -> tuple[PodcastEpisode, ...]:
    """Return case-insensitive title matches without inferring a fuzzy match."""

    query = title_contains.strip().casefold()
    if not query:
        raise ValueError("title_contains must not be blank")
    return tuple(episode for episode in episodes if query in episode.title.casefold())


def _local_name(tag: str) -> str:
    if "}" in tag:
        return tag.rsplit("}", 1)[1]
    return tag


def _iter_elements(root: ElementTree.Element, local_name: str):
    for element in root.iter():
        if _local_name(element.tag) == local_name:
            yield element


def _direct_children(parent: ElementTree.Element, local_name: str):
    for child in parent:
        if _local_name(child.tag) == local_name:
            yield child


def _first_child(
    parent: ElementTree.Element,
    local_name: str,
) -> ElementTree.Element | None:
    return next(_direct_children(parent, local_name), None)


def _child_text(parent: ElementTree.Element, local_name: str) -> str | None:
    child = _first_child(parent, local_name)
    if child is None or child.text is None:
        return None
    value = child.text.strip()
    return value or None


def _parse_published_at(value: str | None) -> datetime | None:
    if value is None:
        return None
    try:
        parsed = parsedate_to_datetime(value)
    except (TypeError, ValueError):
        return None
    if parsed.tzinfo is None:
        return parsed.replace(tzinfo=UTC)
    return parsed


def _parse_duration_seconds(value: str | None) -> int | None:
    if value is None:
        return None

    cleaned = value.strip()
    if not cleaned:
        return None
    if cleaned.isdigit():
        return int(cleaned)

    parts = cleaned.split(":")
    if len(parts) not in {2, 3} or not all(part.isdigit() for part in parts):
        return None

    numbers = [int(part) for part in parts]
    if len(numbers) == 2:
        minutes, seconds = numbers
        hours = 0
    else:
        hours, minutes, seconds = numbers

    if minutes >= 60 or seconds >= 60:
        return None
    return hours * 3_600 + minutes * 60 + seconds
