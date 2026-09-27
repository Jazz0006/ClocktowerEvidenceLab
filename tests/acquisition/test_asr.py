from dataclasses import dataclass

import pytest
from pydantic import ValidationError

from clocktower_evidence_lab.acquisition.asr import (
    TranscriptSegment,
    normalize_segments,
)


@dataclass(frozen=True)
class _RawSegment:
    start: float
    end: float
    text: str


def test_normalize_segments_converts_seconds_to_milliseconds() -> None:
    segments = normalize_segments(
        [
            _RawSegment(start=1.234, end=4.567, text="  Storyteller rationale.  "),
            _RawSegment(start=5.0, end=7.25, text="Second segment."),
        ]
    )

    assert segments == (
        TranscriptSegment(
            index=0,
            start_ms=1_234,
            end_ms=4_567,
            text="Storyteller rationale.",
        ),
        TranscriptSegment(
            index=1,
            start_ms=5_000,
            end_ms=7_250,
            text="Second segment.",
        ),
    )


def test_normalize_segments_skips_blank_text_but_preserves_source_timing() -> None:
    segments = normalize_segments(
        [
            _RawSegment(start=0.0, end=1.0, text="   "),
            _RawSegment(start=1.0, end=2.0, text="Useful."),
        ]
    )

    assert segments == (TranscriptSegment(index=0, start_ms=1_000, end_ms=2_000, text="Useful."),)


def test_normalize_segments_rejects_invalid_ranges() -> None:
    with pytest.raises(ValidationError):
        normalize_segments([_RawSegment(start=2.0, end=1.0, text="Broken.")])
