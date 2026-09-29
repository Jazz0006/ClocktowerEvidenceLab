from io import BytesIO
from pathlib import Path

from clocktower_evidence_lab.acquisition import asr, podcast, podcast_batch, podcast_manifest

_FEED_URL = "https://anchor.fm/s/daf1f9c/podcast/rss"


def _episode(
    *,
    title: str = "15: Chef (Trouble Brewing)",
    guid: str = "chef-guid",
    audio_url: str | None = "https://example.test/chef.mp3",
    transcripts: tuple[podcast.PodcastTranscriptReference, ...] = (),
) -> podcast.PodcastEpisode:
    return podcast.PodcastEpisode(
        feed_url=_FEED_URL,
        title=title,
        guid=guid,
        audio_url=audio_url,
        transcripts=transcripts,
    )


def test_batch_plan_prefers_advertised_transcript_locator() -> None:
    episode = _episode(
        transcripts=(
            podcast.PodcastTranscriptReference(
                url="https://example.test/chef.vtt",
                media_type="text/vtt",
            ),
        )
    )
    manifest = podcast_manifest.build_episode_manifest((episode,))

    plan = podcast_batch.build_batch_plan(manifest)
    item = plan.items[0]

    assert item.mode is podcast_batch.BatchAcquisitionMode.ADVERTISED_TRANSCRIPT
    assert item.locator == "https://example.test/chef.vtt"
    assert item.payload_relative_path.endswith(".vtt")
    assert item.asr_relative_path is None


def test_batch_plan_uses_audio_asr_when_no_transcript_is_advertised() -> None:
    manifest = podcast_manifest.build_episode_manifest((_episode(),))

    item = podcast_batch.build_batch_plan(manifest).items[0]

    assert item.mode is podcast_batch.BatchAcquisitionMode.AUDIO_ASR
    assert item.locator == "https://example.test/chef.mp3"
    assert item.payload_relative_path.endswith(".mp3")
    assert item.asr_relative_path.endswith("asr.json")


def test_batch_plan_excludes_processed_and_out_of_scope_episodes() -> None:
    processed = _episode(guid="processed-guid")
    out_of_scope = _episode(
        title="3.19: Chambermaid (Bad Moon Rising)",
        guid="bmr-guid",
    )
    pending = _episode(guid="pending-guid")
    processed_id = podcast_manifest.stable_episode_id(processed)
    manifest = podcast_manifest.build_episode_manifest(
        (processed, out_of_scope, pending),
        prior_processing=(
            podcast_manifest.PriorEpisodeProcessing(
                source_id=processed_id,
                acquisition_state=podcast_manifest.AcquisitionState.COMPLETE,
            ),
        ),
    )

    plan = podcast_batch.build_batch_plan(manifest)

    assert [item.source_id for item in plan.items] == [podcast_manifest.stable_episode_id(pending)]


def test_missing_locator_is_explicitly_blocked() -> None:
    manifest = podcast_manifest.build_episode_manifest((_episode(audio_url=None),))

    item = podcast_batch.build_batch_plan(manifest).items[0]

    assert item.mode is podcast_batch.BatchAcquisitionMode.BLOCKED
    assert item.locator is None
    assert item.block_reason is podcast_batch.BatchBlockReason.MISSING_SOURCE_LOCATOR


def test_batch_paths_are_stable_relative_and_safe() -> None:
    item = podcast_batch.build_batch_plan(
        podcast_manifest.build_episode_manifest((_episode(),))
    ).items[0]

    payload = Path(item.payload_relative_path)
    asr_path = Path(item.asr_relative_path)

    assert not payload.is_absolute()
    assert not asr_path.is_absolute()
    assert ".." not in payload.parts
    assert ":" not in item.payload_relative_path
    assert item.source_id.split(":", 1)[1] in payload.parts


class _FakeResponse:
    def __init__(self, payload: bytes) -> None:
        self._stream = BytesIO(payload)

    def __enter__(self) -> "_FakeResponse":
        return self

    def __exit__(self, *_args: object) -> None:
        return None

    def read(self, size: int = -1) -> bytes:
        return self._stream.read(size)


def test_acquire_payload_streams_to_work_dir_and_resumes_existing_file(
    tmp_path: Path,
) -> None:
    item = podcast_batch.build_batch_plan(
        podcast_manifest.build_episode_manifest((_episode(),))
    ).items[0]
    calls = 0

    def opener(_url: str, *, timeout: float) -> _FakeResponse:
        nonlocal calls
        calls += 1
        assert timeout == 30.0
        return _FakeResponse(b"podcast-audio")

    first = podcast_batch.acquire_payload(item, tmp_path, opener=opener, chunk_size=4)
    second = podcast_batch.acquire_payload(item, tmp_path, opener=opener, chunk_size=4)

    payload_path = tmp_path / item.payload_relative_path
    assert payload_path.read_bytes() == b"podcast-audio"
    assert first.skipped_existing is False
    assert second.skipped_existing is True
    assert calls == 1
    assert first.payload_sha256 == second.payload_sha256
    assert first.payload_bytes == len(b"podcast-audio")


def test_audio_asr_writes_full_transcript_only_to_external_work_dir(
    tmp_path: Path,
) -> None:
    item = podcast_batch.build_batch_plan(
        podcast_manifest.build_episode_manifest((_episode(),))
    ).items[0]
    audio_path = tmp_path / item.payload_relative_path
    audio_path.parent.mkdir(parents=True)
    audio_path.write_bytes(b"fake-audio")

    def transcriber(
        path: str | Path,
        *,
        model_name: str,
        device: str,
        compute_type: str,
        language: str | None,
    ) -> asr.AsrTranscript:
        assert Path(path) == audio_path
        assert model_name == "small.en"
        assert device == "cpu"
        assert compute_type == "int8"
        assert language == "en"
        return asr.AsrTranscript(
            model_name=model_name,
            language="en",
            language_probability=0.99,
            segments=(
                asr.TranscriptSegment(
                    index=0,
                    start_ms=1000,
                    end_ms=2500,
                    text="machine transcript text",
                ),
            ),
        )

    progress = podcast_batch.run_audio_asr(
        item,
        tmp_path,
        transcriber=transcriber,
    )

    full_asr_path = tmp_path / item.asr_relative_path
    assert "machine transcript text" in full_asr_path.read_text(encoding="utf-8")
    dumped = progress.model_dump(mode="json")
    assert dumped["asr_state"] == "COMPLETE"
    assert dumped["asr_segment_count"] == 1
    assert "segments" not in dumped
    assert "transcript_text" not in dumped


def test_applying_batch_progress_does_not_promote_human_review() -> None:
    episode = _episode()
    manifest = podcast_manifest.build_episode_manifest((episode,))
    source_id = manifest.episodes[0].source_id
    progress = podcast_batch.BatchProgress(
        source_id=source_id,
        acquisition_state=podcast_manifest.AcquisitionState.COMPLETE,
        asr_state=podcast_manifest.AsrState.COMPLETE,
        payload_relative_path="episodes/example/audio.mp3",
        payload_sha256="a" * 64,
        payload_bytes=123,
        asr_relative_path="episodes/example/asr.json",
        asr_model="small.en",
        asr_segment_count=5,
    )

    updated = podcast_batch.apply_batch_progress(manifest, (progress,))
    entry = updated.episodes[0]

    assert entry.acquisition_state is podcast_manifest.AcquisitionState.COMPLETE
    assert entry.asr_state is podcast_manifest.AsrState.COMPLETE
    assert entry.extraction_state is podcast_manifest.ExtractionState.NOT_ATTEMPTED
    assert entry.human_review_state is podcast_manifest.HumanReviewState.NOT_STARTED


def test_run_batch_plan_handles_transcript_audio_and_blocked_items(
    tmp_path: Path,
) -> None:
    transcript_episode = _episode(
        guid="transcript-guid",
        transcripts=(
            podcast.PodcastTranscriptReference(
                url="https://example.test/transcript-guid.vtt",
                media_type="text/vtt",
            ),
        ),
    )
    audio_episode = _episode(guid="audio-guid")
    blocked_episode = _episode(guid="blocked-guid", audio_url=None)
    manifest = podcast_manifest.build_episode_manifest(
        (transcript_episode, audio_episode, blocked_episode)
    )
    plan = podcast_batch.build_batch_plan(manifest)

    payloads = {
        "https://example.test/transcript-guid.vtt": b"WEBVTT",
        "https://example.test/chef.mp3": b"fake-audio",
    }

    def opener(url: str, *, timeout: float) -> _FakeResponse:
        assert timeout == 30.0
        return _FakeResponse(payloads[url])

    transcriber_calls = 0

    def transcriber(
        path: str | Path,
        *,
        model_name: str,
        device: str,
        compute_type: str,
        language: str | None,
    ) -> asr.AsrTranscript:
        nonlocal transcriber_calls
        transcriber_calls += 1
        assert Path(path).read_bytes() == b"fake-audio"
        return asr.AsrTranscript(
            model_name=model_name,
            language=language,
            segments=(
                asr.TranscriptSegment(
                    index=0,
                    start_ms=0,
                    end_ms=1000,
                    text="candidate",
                ),
            ),
        )

    result = podcast_batch.run_batch_plan(
        plan,
        tmp_path,
        opener=opener,
        transcriber=transcriber,
    )

    assert len(result.progress) == 2
    assert len(result.blocked_items) == 1
    transcript_progress, audio_progress = result.progress
    assert transcript_progress.asr_state is podcast_manifest.AsrState.NOT_REQUIRED
    assert audio_progress.asr_state is podcast_manifest.AsrState.COMPLETE
    assert result.blocked_items[0].source_id == podcast_manifest.stable_episode_id(
        blocked_episode
    )
    assert transcriber_calls == 1


def test_run_audio_asr_reuses_existing_external_asr_artifact(
    tmp_path: Path,
) -> None:
    item = podcast_batch.build_batch_plan(
        podcast_manifest.build_episode_manifest((_episode(),))
    ).items[0]
    audio_path = tmp_path / item.payload_relative_path
    audio_path.parent.mkdir(parents=True)
    audio_path.write_bytes(b"fake-audio")

    calls = 0

    def transcriber(
        _path: str | Path,
        *,
        model_name: str,
        device: str,
        compute_type: str,
        language: str | None,
    ) -> asr.AsrTranscript:
        nonlocal calls
        calls += 1
        return asr.AsrTranscript(
            model_name=model_name,
            language=language,
            segments=(
                asr.TranscriptSegment(
                    index=0,
                    start_ms=0,
                    end_ms=1000,
                    text="reusable transcript",
                ),
            ),
        )

    first = podcast_batch.run_audio_asr(item, tmp_path, transcriber=transcriber)
    second = podcast_batch.run_audio_asr(item, tmp_path, transcriber=transcriber)

    assert calls == 1
    assert first.asr_skipped_existing is False
    assert second.asr_skipped_existing is True
    assert first.asr_segment_count == second.asr_segment_count == 1
