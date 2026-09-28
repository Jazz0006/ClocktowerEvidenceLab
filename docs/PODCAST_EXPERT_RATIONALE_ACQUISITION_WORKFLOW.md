# Podcast Expert-Rationale Acquisition Workflow

## Purpose

Use public expert podcasts as a **rationale source** without confusing machine transcripts with verified evidence or replacing the project's whole-game-first acquisition strategy.

This workflow is appropriate when a qualified Storyteller/designer discusses why a Storyteller choice is useful, harmful, context-dependent or player-experience-dependent.

## Source hierarchy

Podcast material is normally:

~~~text
EXPERT_GUIDANCE_WITH_GAME_EXAMPLES
~~~

unless the episode itself contains enough reconstructable game state to qualify under a stronger existing Evidence Lab category.

It is not a replay case merely because the speaker is qualified.

## Acquisition cascade

1. Probe the public RSS feed.
2. Preserve stable episode identity, webpage locator and audio enclosure URL.
3. Check whether the feed advertises a Podcasting 2.0 transcript locator.
4. If a transcript locator exists, treat it as a discovery aid rather than verified evidence.
5. If no transcript exists, download the public audio outside Git and run optional ASR.
6. Keep the complete machine transcript outside Git.
7. Search the timestamped segments for policy-relevant concepts.
8. Reduce the episode to short candidate windows.
9. Human-review only those windows against the primary audio.
10. Commit concise paraphrases + timestamps + derivation/verification state, never a long transcript reproduction.

## Repository tools

Probe a feed:

~~~bash
clocktower-podcast-probe \
  "https://example.test/podcast/rss" \
  --title-contains "Drunk"
~~~

Install optional ASR support:

~~~bash
python -m pip install -e ".[asr]"
~~~

Transcribe already-downloaded audio:

~~~bash
clocktower-podcast-asr episode.mp3 \
  --output episode.asr.json \
  --model small.en \
  --device cpu \
  --compute-type int8 \
  --language en
~~~

The ASR JSON is an acquisition artifact and should normally remain untracked.

## Evidence rules

Machine transcript text is not automatically:

- an observed source quote;
- verified speaker attribution;
- a verified Storyteller principle;
- a policy recommendation;
- a legal-alternative judgment.

ASR is allowed to answer:

> Where should a human reviewer listen?

It is not allowed to answer:

> What has been verified as the speaker's intended rationale?

Primary-audio review owns that promotion step.

## Search priority

Prefer concepts that map to known Evidence Lab / Storyteller gaps:

- whole-setup choice rationale;
- persistent Drunk world / trajectory;
- healthy-information strength;
- confirmation-chain severity;
- role-function exposure;
- player experience / beginner handling;
- Demon bluff interaction;
- player-controlled versus Storyteller-controlled choices;
- explicit rejected alternatives;
- reasons a candidate output was chosen over another.

Stop early when an episode contains only generic advice that does not map to a concrete policy dimension.

## Copyright boundary

Do not commit:

- full audio;
- full machine transcript;
- large transcript excerpts.

Commit only:

- source identity;
- source URL/ID;
- timestamps/ranges;
- concise factual paraphrases;
- minimal quotation only when evidentially necessary.

## Success criterion

A podcast source is worth processing when automation reduces a long episode to a small primary-audio review packet and the reviewed windows add a missing rationale dimension or challenge an existing assumption.

The Drunk pilot on 2026-09-28 reduced a 2:27:27 episode to roughly 15 minutes of P0 review windows.
