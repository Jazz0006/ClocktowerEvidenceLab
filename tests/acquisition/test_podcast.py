from clocktower_evidence_lab.acquisition import podcast


_SAMPLE_RSS = """<?xml version="1.0" encoding="UTF-8"?>
<rss
    version="2.0"
    xmlns:itunes="http://www.itunes.com/dtds/podcast-1.0.dtd"
    xmlns:podcast="https://podcastindex.org/namespace/1.0"
>
  <channel>
    <title>Cult of the Clocktower</title>
    <item>
      <title>16: Drunk (Trouble Brewing) - With Clocktower Designer Steven Medway!</title>
      <guid isPermaLink="false">ecemnu</guid>
      <link>https://creators.spotify.com/pod/show/andrew-nathenson/episodes/ecemnu</link>
      <pubDate>Mon, 06 Apr 2020 17:00:00 GMT</pubDate>
      <itunes:duration>2:27:05</itunes:duration>
      <enclosure
          url="https://example.test/audio/drunk.mp3"
          length="123456"
          type="audio/mpeg"
      />
      <podcast:transcript
          url="https://example.test/transcript/drunk.vtt"
          type="text/vtt"
          language="en"
          rel="captions"
      />
      <podcast:transcript
          url="https://example.test/transcript/drunk.json"
          type="application/json"
          language="en"
      />
    </item>
    <item>
      <title>15: Chef (Trouble Brewing)</title>
      <guid isPermaLink="false">chef</guid>
      <itunes:duration>01:02:03</itunes:duration>
      <enclosure url="https://example.test/audio/chef.mp3" type="audio/mpeg" />
    </item>
  </channel>
</rss>
"""


def test_parse_podcast_rss_preserves_episode_and_transcript_locators() -> None:
    episodes = podcast.parse_podcast_rss(
        _SAMPLE_RSS,
        feed_url="https://anchor.fm/s/daf1f9c/podcast/rss",
    )

    drunk = episodes[0]

    assert drunk.guid == "ecemnu"
    assert drunk.title.startswith("16: Drunk")
    assert drunk.webpage_url == (
        "https://creators.spotify.com/pod/show/andrew-nathenson/episodes/ecemnu"
    )
    assert drunk.audio_url == "https://example.test/audio/drunk.mp3"
    assert drunk.duration_seconds == 8_825
    assert drunk.published_at is not None
    assert drunk.published_at.isoformat() == "2020-04-06T17:00:00+00:00"
    assert [transcript.url for transcript in drunk.transcripts] == [
        "https://example.test/transcript/drunk.vtt",
        "https://example.test/transcript/drunk.json",
    ]
    assert drunk.transcripts[0].media_type == "text/vtt"
    assert drunk.transcripts[0].language == "en"
    assert drunk.transcripts[0].rel == "captions"


def test_episode_without_feed_transcript_remains_explicitly_empty() -> None:
    episodes = podcast.parse_podcast_rss(
        _SAMPLE_RSS,
        feed_url="https://anchor.fm/s/daf1f9c/podcast/rss",
    )

    chef = episodes[1]

    assert chef.guid == "chef"
    assert chef.duration_seconds == 3_723
    assert chef.transcripts == ()


def test_find_episodes_is_case_insensitive_and_does_not_guess() -> None:
    episodes = podcast.parse_podcast_rss(
        _SAMPLE_RSS,
        feed_url="https://anchor.fm/s/daf1f9c/podcast/rss",
    )

    assert podcast.find_episodes(episodes, "DRUNK") == (episodes[0],)
    assert podcast.find_episodes(episodes, "investigator") == ()
