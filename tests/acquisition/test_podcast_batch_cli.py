from pathlib import Path

from clocktower_evidence_lab.acquisition import podcast, podcast_batch_cli, podcast_manifest


def test_batch_cli_plan_only_reads_manifest_without_creating_work_artifacts(
    tmp_path: Path,
    capsys,
) -> None:
    episode = podcast.PodcastEpisode(
        feed_url="https://anchor.fm/s/daf1f9c/podcast/rss",
        title="15: Chef (Trouble Brewing)",
        guid="chef-guid",
        audio_url="https://example.test/chef.mp3",
    )
    manifest = podcast_manifest.build_episode_manifest((episode,))
    manifest_path = tmp_path / "manifest.json"
    manifest_path.write_text(manifest.model_dump_json(indent=2), encoding="utf-8")
    work_dir = tmp_path / "work"

    result = podcast_batch_cli.main(
        [
            str(manifest_path),
            "--work-dir",
            str(work_dir),
            "--plan-only",
        ]
    )

    captured = capsys.readouterr()
    assert result == 0
    assert '"mode": "AUDIO_ASR"' in captured.out
    assert not work_dir.exists()
