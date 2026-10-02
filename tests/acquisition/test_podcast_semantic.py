# ruff: noqa: I001

from io import StringIO

import pytest

from clocktower_evidence_lab.acquisition import (
    asr,
    podcast_batch,
    podcast_manifest,
    podcast_semantic,
)


RSS = """<?xml version="1.0" encoding="UTF-8"?>
<rss version="2.0">
  <channel>
    <title>Cult of the Clocktower</title>
    <item>
      <title>18: Investigator (Trouble Brewing)</title>
      <guid>5722d8e8-b89d-4067-91ac-1550b8da428d</guid>
      <enclosure url="https://example.test/investigator.mp3" type="audio/mpeg" />
    </item>
  </channel>
</rss>
"""

QUEUE_RSS = """<?xml version="1.0" encoding="UTF-8"?>
<rss version="2.0">
  <channel>
    <title>Cult of the Clocktower</title>
    <item>
      <title>18: Investigator (Trouble Brewing)</title>
      <guid>5722d8e8-b89d-4067-91ac-1550b8da428d</guid>
      <enclosure url="https://example.test/investigator.mp3" type="audio/mpeg" />
    </item>
    <item>
      <title>15: Chef (Trouble Brewing)</title>
      <guid>chef-guid</guid>
      <enclosure url="https://example.test/chef.mp3" type="audio/mpeg" />
    </item>
    <item>
      <title>16: Drunk (Trouble Brewing)</title>
      <guid>bf668470-a3fe-41d3-85e8-d028a63cf593</guid>
      <enclosure url="https://example.test/drunk.mp3" type="audio/mpeg" />
    </item>
    <item>
      <title>22: Imp (Trouble Brewing)</title>
      <guid>a271357d-10af-4969-8c7e-5545b871b5cb</guid>
      <enclosure url="https://example.test/imp.mp3" type="audio/mpeg" />
    </item>
    <item>
      <title>Other script (Bad Moon Rising)</title>
      <guid>bmr-guid</guid>
      <enclosure url="https://example.test/bmr.mp3" type="audio/mpeg" />
    </item>
  </channel>
</rss>
"""

ROLE_PRIORITY_RSS = """<?xml version="1.0" encoding="UTF-8"?>
<rss version="2.0">
  <channel>
    <title>Cult of the Clocktower</title>
    <item>
      <title>15: Chef (Trouble Brewing)</title>
      <guid>chef-guid</guid>
      <enclosure url="https://example.test/chef.mp3" type="audio/mpeg" />
    </item>
    <item>
      <title>10: Ravenkeeper (Trouble Brewing)</title>
      <guid>ravenkeeper-guid</guid>
      <enclosure url="https://example.test/ravenkeeper.mp3" type="audio/mpeg" />
    </item>
    <item>
      <title>12: Monk (Trouble Brewing)</title>
      <guid>monk-guid</guid>
      <enclosure url="https://example.test/monk.mp3" type="audio/mpeg" />
    </item>
    <item>
      <title>13: Soldier (Trouble Brewing) - With Official Storyteller Jon Gjengset!</title>
      <guid>soldier-guid</guid>
      <enclosure url="https://example.test/soldier.mp3" type="audio/mpeg" />
    </item>
  </channel>
</rss>
"""

GENERAL_STORYTELLING_PRIORITY_RSS = """<?xml version="1.0" encoding="UTF-8"?>
<rss version="2.0">
  <channel>
    <title>Cult of the Clocktower</title>
    <item>
      <title>13: Soldier (Trouble Brewing) - With Official Storyteller Jon Gjengset!</title>
      <guid>soldier-guid</guid>
      <enclosure url="https://example.test/soldier.mp3" type="audio/mpeg" />
    </item>
    <item>
      <title>4.2: Storytelling Like a Pro</title>
      <guid>storytelling-pro-guid</guid>
      <enclosure url="https://example.test/storytelling-pro.mp3" type="audio/mpeg" />
    </item>
    <item>
      <title>3.26: Zombuul (Bad Moon Rising)</title>
      <guid>bmr-guid</guid>
      <enclosure url="https://example.test/bmr.mp3" type="audio/mpeg" />
    </item>
  </channel>
</rss>
"""


def test_prepare_reacquires_one_episode_even_when_semantic_read_is_separate_from_prior_state(
    tmp_path, monkeypatch
):
    root = tmp_path / "semantic" / "investigator"
    monkeypatch.setattr(podcast_semantic, "fetch_rss", lambda *args, **kwargs: RSS)

    def fake_run(plan, work_dir):
        assert len(plan.items) == 1
        item = plan.items[0]
        assert item.asr_relative_path is not None
        asr_path = work_dir / item.asr_relative_path
        asr_path.parent.mkdir(parents=True, exist_ok=True)
        asr_path.write_text(
            asr.AsrTranscript(
                model_name="small.en",
                language="en",
                language_probability=1.0,
                segments=(
                    asr.TranscriptSegment(
                        index=0,
                        start_ms=1_000,
                        end_ms=2_500,
                        text="Storyteller consideration.",
                    ),
                ),
            ).model_dump_json(indent=2)
            + "\n",
            encoding="utf-8",
        )
        return podcast_batch.BatchRunResult(
            progress=(
                podcast_batch.BatchProgress(
                    source_id=item.source_id,
                    acquisition_state=podcast_manifest.AcquisitionState.COMPLETE,
                    asr_state=podcast_manifest.AsrState.COMPLETE,
                    payload_relative_path=item.payload_relative_path,
                    payload_sha256="0" * 64,
                    payload_bytes=123,
                    asr_relative_path=item.asr_relative_path,
                    asr_model="small.en",
                    asr_segment_count=1,
                ),
            ),
            blocked_items=(),
        )

    monkeypatch.setattr(podcast_semantic, "run_batch_plan", fake_run)

    session = podcast_semantic.prepare_semantic_session(
        guid="5722d8e8-b89d-4067-91ac-1550b8da428d",
        work_dir=root,
    )

    assert session.episode_title == "18: Investigator (Trouble Brewing)"
    assert (root / podcast_semantic.SESSION_MARKER_FILENAME).is_file()
    assert (root / podcast_semantic.BATCH_PROGRESS_FILENAME).is_file()


def test_render_outputs_complete_timestamped_transcript_without_writing_second_copy(tmp_path):
    root = tmp_path / "semantic" / "investigator"
    asr_path = root / "episodes" / "source" / "asr.json"
    asr_path.parent.mkdir(parents=True)

    session = podcast_semantic.SemanticReviewSession(
        guid="guid-1",
        source_id="podcast:source",
        episode_title="Investigator",
    )
    (root / podcast_semantic.SESSION_MARKER_FILENAME).write_text(
        session.model_dump_json(indent=2) + "\n",
        encoding="utf-8",
    )
    (root / podcast_semantic.BATCH_PROGRESS_FILENAME).write_text(
        podcast_batch.BatchRunResult(
            progress=(
                podcast_batch.BatchProgress(
                    source_id=session.source_id,
                    acquisition_state=podcast_manifest.AcquisitionState.COMPLETE,
                    asr_state=podcast_manifest.AsrState.COMPLETE,
                    payload_relative_path="episodes/source/source.mp3",
                    payload_sha256="1" * 64,
                    payload_bytes=456,
                    asr_relative_path="episodes/source/asr.json",
                    asr_model="small.en",
                    asr_segment_count=2,
                ),
            ),
            blocked_items=(),
        ).model_dump_json(indent=2)
        + "\n",
        encoding="utf-8",
    )
    asr_path.write_text(
        asr.AsrTranscript(
            model_name="small.en",
            language="en",
            language_probability=0.99,
            segments=(
                asr.TranscriptSegment(index=0, start_ms=0, end_ms=1_250, text="First."),
                asr.TranscriptSegment(
                    index=1,
                    start_ms=61_002,
                    end_ms=62_345,
                    text="Second.",
                ),
            ),
        ).model_dump_json(indent=2)
        + "\n",
        encoding="utf-8",
    )

    output = StringIO()
    podcast_semantic.render_semantic_transcript(work_dir=root, output=output)

    rendered = output.getvalue()
    assert "segments=2" in rendered
    assert "00:00:00.000-00:00:01.250\tFirst." in rendered
    assert "00:01:01.002-00:01:02.345\tSecond." in rendered
    assert sorted(path.name for path in root.rglob("*") if path.is_file()) == [
        ".semantic-review-session.json",
        "asr.json",
        "batch-progress.json",
    ]


def test_render_current_window_outputs_only_overlapping_segments(tmp_path):
    root = tmp_path / "semantic" / "queue"
    current = root / podcast_semantic.CURRENT_SESSION_DIRNAME
    asr_path = current / "episodes" / "source" / "asr.json"
    asr_path.parent.mkdir(parents=True)
    session = podcast_semantic.SemanticReviewSession(
        guid="guid-window",
        source_id="podcast:window",
        episode_title="Window",
    )
    (current / podcast_semantic.SESSION_MARKER_FILENAME).write_text(
        session.model_dump_json(indent=2) + "\n", encoding="utf-8"
    )
    (current / podcast_semantic.BATCH_PROGRESS_FILENAME).write_text(
        podcast_batch.BatchRunResult(
            progress=(
                podcast_batch.BatchProgress(
                    source_id=session.source_id,
                    acquisition_state=podcast_manifest.AcquisitionState.COMPLETE,
                    asr_state=podcast_manifest.AsrState.COMPLETE,
                    payload_relative_path="episodes/source/source.mp3",
                    payload_sha256="3" * 64,
                    payload_bytes=123,
                    asr_relative_path="episodes/source/asr.json",
                    asr_model="small.en",
                    asr_segment_count=3,
                ),
            ),
            blocked_items=(),
        ).model_dump_json(indent=2)
        + "\n",
        encoding="utf-8",
    )
    asr_path.write_text(
        asr.AsrTranscript(
            model_name="small.en",
            language="en",
            language_probability=1.0,
            segments=(
                asr.TranscriptSegment(index=0, start_ms=1_000, end_ms=2_000, text="Before."),
                asr.TranscriptSegment(index=1, start_ms=5_000, end_ms=6_000, text="Inside."),
                asr.TranscriptSegment(index=2, start_ms=9_000, end_ms=10_000, text="After."),
            ),
        ).model_dump_json(indent=2)
        + "\n",
        encoding="utf-8",
    )

    output = StringIO()
    podcast_semantic.render_current_semantic_window(
        queue_root=root, start_ms=4_500, end_ms=6_500, output=output
    )

    rendered = output.getvalue()
    assert "segments=1" in rendered
    assert "Inside." in rendered
    assert "Before." not in rendered
    assert "After." not in rendered


def test_cleanup_requires_marker_and_only_removes_marked_workspace(tmp_path):
    unmarked = tmp_path / "semantic" / "unmarked"
    unmarked.mkdir(parents=True)
    sentinel = unmarked / "keep.txt"
    sentinel.write_text("keep", encoding="utf-8")

    with pytest.raises(ValueError, match="missing its session marker"):
        podcast_semantic.cleanup_semantic_session(work_dir=unmarked)
    assert sentinel.is_file()

    marked = tmp_path / "semantic" / "marked"
    marked.mkdir(parents=True)
    session = podcast_semantic.SemanticReviewSession(
        guid="guid-2",
        source_id="podcast:source-2",
        episode_title="Investigator",
    )
    (marked / podcast_semantic.SESSION_MARKER_FILENAME).write_text(
        session.model_dump_json(indent=2) + "\n",
        encoding="utf-8",
    )
    (marked / "source.mp3").write_bytes(b"audio")
    (marked / "asr.json").write_text("{}", encoding="utf-8")

    cleaned = podcast_semantic.cleanup_semantic_session(work_dir=marked)

    assert cleaned == session
    assert not marked.exists()


def test_prepare_recovers_when_marked_progress_lost_its_asr_file(tmp_path, monkeypatch):
    root = tmp_path / "semantic" / "investigator"
    root.mkdir(parents=True)
    session = podcast_semantic.SemanticReviewSession(
        guid="5722d8e8-b89d-4067-91ac-1550b8da428d",
        source_id="podcast:expected",
        episode_title="18: Investigator (Trouble Brewing)",
    )
    (root / podcast_semantic.SESSION_MARKER_FILENAME).write_text(
        session.model_dump_json(indent=2) + "\n",
        encoding="utf-8",
    )
    (root / podcast_semantic.BATCH_PROGRESS_FILENAME).write_text(
        podcast_batch.BatchRunResult(
            progress=(
                podcast_batch.BatchProgress(
                    source_id=session.source_id,
                    acquisition_state=podcast_manifest.AcquisitionState.COMPLETE,
                    asr_state=podcast_manifest.AsrState.COMPLETE,
                    payload_relative_path="episodes/source/source.mp3",
                    payload_sha256="2" * 64,
                    payload_bytes=10,
                    asr_relative_path="episodes/source/asr.json",
                    asr_model="small.en",
                    asr_segment_count=1,
                ),
            ),
            blocked_items=(),
        ).model_dump_json(indent=2)
        + "\n",
        encoding="utf-8",
    )

    monkeypatch.setattr(podcast_semantic, "fetch_rss", lambda *args, **kwargs: RSS)
    monkeypatch.setattr(podcast_semantic, "stable_episode_id", lambda episode: session.source_id)

    calls = []

    def fake_acquire(current_session, episode, work_dir):
        calls.append((current_session, episode.guid, work_dir))
        return current_session

    monkeypatch.setattr(podcast_semantic, "_run_session_acquisition", fake_acquire)

    resumed = podcast_semantic.prepare_semantic_session(
        guid=session.guid,
        work_dir=root,
    )

    assert resumed == session
    assert calls == [(session, session.guid, root)]


def test_prepare_next_uses_fixed_tb_queue_and_prioritizes_imp(tmp_path, monkeypatch):
    root = tmp_path / "semantic" / "queue"
    monkeypatch.setattr(podcast_semantic, "fetch_rss", lambda *args, **kwargs: QUEUE_RSS)

    calls = []

    def fake_prepare(*, guid, work_dir, feed_url, timeout_seconds):
        calls.append((guid, work_dir, feed_url, timeout_seconds))
        return podcast_semantic.SemanticReviewSession(
            guid=guid,
            source_id=f"podcast:{guid}",
            episode_title="selected",
        )

    monkeypatch.setattr(podcast_semantic, "prepare_semantic_session", fake_prepare)

    session = podcast_semantic.prepare_next_semantic_session(
        queue_root=root,
        feed_url="https://example.test/feed.xml",
    )

    assert session.guid == podcast_semantic.IMP_GUID
    assert calls == [
        (
            podcast_semantic.IMP_GUID,
            root / podcast_semantic.CURRENT_SESSION_DIRNAME,
            "https://example.test/feed.xml",
            30.0,
        )
    ]


def test_prepare_next_prioritizes_drunk_after_imp_is_complete(tmp_path, monkeypatch):
    root = tmp_path / "semantic" / "queue"
    root.mkdir(parents=True)
    (root / podcast_semantic.QUEUE_STATE_FILENAME).write_text(
        podcast_semantic.SemanticReviewQueueState(
            completed_guids=(
                podcast_semantic.INVESTIGATOR_GUID,
                podcast_semantic.IMP_GUID,
            )
        ).model_dump_json(indent=2)
        + "\n",
        encoding="utf-8",
    )
    monkeypatch.setattr(podcast_semantic, "fetch_rss", lambda *args, **kwargs: QUEUE_RSS)

    selected = []

    def fake_prepare(*, guid, work_dir, feed_url, timeout_seconds):
        selected.append(guid)
        return podcast_semantic.SemanticReviewSession(
            guid=guid,
            source_id=f"podcast:{guid}",
            episode_title="selected",
        )

    monkeypatch.setattr(podcast_semantic, "prepare_semantic_session", fake_prepare)

    podcast_semantic.prepare_next_semantic_session(
        queue_root=root,
        feed_url="https://example.test/feed.xml",
    )

    assert selected == [podcast_semantic.DRUNK_GUID]


def test_prepare_next_prioritizes_soldier_by_title_after_guid_priorities(tmp_path, monkeypatch):
    root = tmp_path / "semantic" / "queue"
    root.mkdir(parents=True)
    monkeypatch.setattr(
        podcast_semantic,
        "fetch_rss",
        lambda *args, **kwargs: ROLE_PRIORITY_RSS,
    )

    selected = []

    def fake_prepare(*, guid, work_dir, feed_url, timeout_seconds):
        selected.append(guid)
        return podcast_semantic.SemanticReviewSession(
            guid=guid,
            source_id=f"podcast:{guid}",
            episode_title="selected",
        )

    monkeypatch.setattr(podcast_semantic, "prepare_semantic_session", fake_prepare)

    podcast_semantic.prepare_next_semantic_session(
        queue_root=root,
        feed_url="https://example.test/feed.xml",
    )

    assert selected == ["soldier-guid"]


def test_prepare_next_prioritizes_curated_general_storytelling_episode(tmp_path, monkeypatch):
    root = tmp_path / "semantic" / "queue"
    root.mkdir(parents=True)
    monkeypatch.setattr(
        podcast_semantic,
        "fetch_rss",
        lambda *args, **kwargs: GENERAL_STORYTELLING_PRIORITY_RSS,
    )

    selected = []

    def fake_prepare(*, guid, work_dir, feed_url, timeout_seconds):
        selected.append(guid)
        return podcast_semantic.SemanticReviewSession(
            guid=guid,
            source_id=f"podcast:{guid}",
            episode_title="selected",
        )

    monkeypatch.setattr(podcast_semantic, "prepare_semantic_session", fake_prepare)

    podcast_semantic.prepare_next_semantic_session(
        queue_root=root,
        feed_url="https://example.test/feed.xml",
    )

    assert selected == ["storytelling-pro-guid"]


def test_cleanup_current_advances_lightweight_queue_state(tmp_path, monkeypatch):
    root = tmp_path / "semantic" / "queue"
    current = root / podcast_semantic.CURRENT_SESSION_DIRNAME
    current.mkdir(parents=True)
    session = podcast_semantic.SemanticReviewSession(
        guid=podcast_semantic.IMP_GUID,
        source_id="podcast:imp",
        episode_title="22: Imp (Trouble Brewing)",
    )

    monkeypatch.setattr(
        podcast_semantic,
        "cleanup_semantic_session",
        lambda *, work_dir: session if work_dir == current else None,
    )

    cleaned = podcast_semantic.cleanup_current_semantic_session(queue_root=root)
    state = podcast_semantic.SemanticReviewQueueState.model_validate_json(
        (root / podcast_semantic.QUEUE_STATE_FILENAME).read_text(encoding="utf-8")
    )

    assert cleaned == session
    assert state.completed_guids == (
        podcast_semantic.INVESTIGATOR_GUID,
        podcast_semantic.IMP_GUID,
    )


def test_prepare_next_skips_completed_and_out_of_scope_entries(tmp_path, monkeypatch):
    root = tmp_path / "semantic" / "queue"
    root.mkdir(parents=True)
    (root / podcast_semantic.QUEUE_STATE_FILENAME).write_text(
        podcast_semantic.SemanticReviewQueueState(
            completed_guids=(
                podcast_semantic.INVESTIGATOR_GUID,
                podcast_semantic.IMP_GUID,
                podcast_semantic.DRUNK_GUID,
            )
        ).model_dump_json(indent=2)
        + "\n",
        encoding="utf-8",
    )
    monkeypatch.setattr(podcast_semantic, "fetch_rss", lambda *args, **kwargs: QUEUE_RSS)

    selected = []

    def fake_prepare(*, guid, work_dir, feed_url, timeout_seconds):
        selected.append(guid)
        return podcast_semantic.SemanticReviewSession(
            guid=guid,
            source_id=f"podcast:{guid}",
            episode_title="selected",
        )

    monkeypatch.setattr(podcast_semantic, "prepare_semantic_session", fake_prepare)

    podcast_semantic.prepare_next_semantic_session(
        queue_root=root,
        feed_url="https://example.test/feed.xml",
    )

    assert selected == ["chef-guid"]
