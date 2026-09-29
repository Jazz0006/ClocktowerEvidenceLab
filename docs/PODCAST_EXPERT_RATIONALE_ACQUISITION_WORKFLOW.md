# Podcast Expert-Rationale Acquisition Workflow

## Purpose

Use public expert podcasts as a **rationale source** without confusing machine transcripts with verified evidence or replacing the project's whole-game-first historical corpus.

This workflow is now the operational acquisition path for C2.

Authority for the current batch: `docs/C2_TB_PODCAST_BATCH_INGESTION_2026-09-29.md`.

## 1. Evidence role

Podcast material is normally:

```text
EXPERT_GUIDANCE_WITH_GAME_EXAMPLES
```

unless an episode itself contains enough reconstructable historical game state to qualify under an existing whole-game evidence category.

It is not replay evidence merely because the speaker is qualified.

## 2. Batch acquisition cascade

For the series:

1. enumerate the live public RSS feed;
2. create/update the episode manifest using stable source identity;
3. classify current Trouble Brewing relevance;
4. recognize previously processed episodes and reuse their status/artifact links;
5. preserve webpage/audio/transcript locators;
6. use a feed-advertised transcript as a discovery aid when present;
7. otherwise acquire public audio outside Git and run timestamped ASR;
8. keep complete audio/transcript artifacts outside Git;
9. run structured candidate extraction;
10. rank candidate windows by product relevance and evidence novelty;
11. human-review only the bounded high-value packet;
12. promote only confirmed concise paraphrases + timestamps + provenance.

## 3. Existing repository tools

Probe a feed or episode:

```bash
clocktower-podcast-probe \
  "https://example.test/podcast/rss" \
  --title-contains "Drunk"
```

Install optional ASR support:

```bash
python -m pip install -e ".[asr]"
```

Transcribe already-downloaded audio:

```bash
clocktower-podcast-asr episode.mp3 \
  --output episode.asr.json \
  --model small.en \
  --device cpu \
  --compute-type int8 \
  --language en
```

The ASR JSON is an acquisition artifact and should normally remain untracked.

Build the current C2 manifest:

```bash
clocktower-podcast-manifest \
  --output /path/outside/repo/c2-manifest.json
```

Inspect the C2B batch plan without downloading:

```bash
clocktower-podcast-batch \
  /path/outside/repo/c2-manifest.json \
  --work-dir /path/outside/repo/c2-work \
  --plan-only
```

Execute the resumable batch after installing ASR support:

```bash
clocktower-podcast-batch \
  /path/outside/repo/c2-manifest.json \
  --work-dir /path/outside/repo/c2-work
```

The batch runner reuses existing payload and ASR artifacts after interruption. It writes full source/transcript artifacts only beneath the explicit work directory; its progress and updated-manifest JSON remain machine workflow metadata, not VERIFIED evidence.

## 4. C2 manifest contract

The batch manifest should track, at minimum:

- stable episode/source ID;
- title;
- publication date;
- duration;
- webpage/audio/transcript locators;
- script/current-scope classification;
- acquisition state;
- ASR state;
- extraction state;
- human-review state;
- retained prior-artifact link when applicable.

Do not use title matching as the only dedup key.

The existing Drunk, Librarian and Recluse scouts are already-processed identities and should be represented as such.

## 5. Candidate extraction

Machine extraction should locate, not verify.

Initial categories:

```text
STORYTELLER_DECISION
STORYTELLER_RATIONALE
SETUP_LEVEL_REASONING
MISINFORMATION_POLICY
REGISTRATION_CHOICE
DEMON_BLUFF_REASONING
PLAYER_EXPERIENCE
PLAYER_AGENCY
INFORMATION_STRENGTH
CONFIRMATION_CHAIN
LONGITUDINAL_TRAJECTORY
EXPLICIT_ALTERNATIVE
REAL_GAME_EXAMPLE
```

Each candidate should include:

- source/episode identity;
- timestamp/range;
- category;
- concise machine summary;
- role/mechanism tags when useful;
- machine confidence or extraction quality;
- human-review state.

Machine confidence is not verification.

## 6. Evidence rules

Machine transcript text is not automatically:

- an observed source quote;
- verified speaker attribution;
- a verified Storyteller principle;
- a policy recommendation;
- a legal-alternative judgment.

ASR and LLM extraction may answer:

> Where should a human reviewer listen, and what might be relevant there?

They may not answer:

> What has been verified as the speaker's intended rationale?

Primary-audio review owns promotion.

## 7. Human-review priority

Prefer windows that map to known Storyteller research needs:

- whole-setup choice rationale;
- Drunk selection and persistent Drunk trajectory;
- healthy-information strength;
- confirmation-chain severity;
- Spy/Recluse exposure versus concealment;
- Demon bluff selection;
- player experience / beginner handling;
- player agency;
- explicit rejected/contrasted alternatives;
- reasons one legal output was chosen over another.

Stop early on low-value generic discussion.

An episode may validly yield no promoted evidence.

## 8. Copyright boundary

Do not commit:

- full audio;
- full machine transcript;
- large transcript excerpts.

Commit only:

- stable source identity;
- locators;
- timestamps/ranges;
- lightweight machine candidate metadata;
- concise reviewed paraphrases;
- minimal quotation only when evidentially necessary.

## 9. Prior pilot result

The 2026-09-28 Drunk pilot demonstrated the path end-to-end:

- 2:27:27 public episode;
- no feed-advertised transcript;
- public audio enclosure available;
- faster-whisper ASR completed;
- 1609 timestamped segments;
- long source reduced to a small high-value human-review packet.

Librarian and Recluse scouts subsequently reused the same route.

Those artifacts are historical acquisition evidence for the workflow, not a reason to continue episode-by-episode manual scouting.

## 10. Success criterion

The batch workflow succeeds when automation reduces many hours of relevant expert audio to small, auditable human-review packets and those reviews add verified rationale dimensions or useful counterexamples.

Primary metric:

**verified high-value guidance per minute of human review**.
