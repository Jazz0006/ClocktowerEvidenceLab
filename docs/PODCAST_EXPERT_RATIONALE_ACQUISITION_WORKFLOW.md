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

For the machine-first semantic benchmark, use the temporary semantic lifecycle:

```bash
clocktower-podcast-semantic prepare \
  --guid <episode-guid> \
  --work-dir /path/outside/repo/semantic-session

clocktower-podcast-semantic render \
  --work-dir /path/outside/repo/semantic-session

clocktower-podcast-semantic cleanup \
  --work-dir /path/outside/repo/semantic-session
```

`prepare` intentionally allows a previously processed episode to be re-acquired for a bounded semantic benchmark. `render` streams the complete timestamped ASR to the semantic consumer rather than writing a second transcript. `cleanup` is marker-gated and removes the temporary audio and ASR workspace after analysis. The complete transcript is therefore available for contextual understanding without becoming a durable Git artifact.

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

The original C2C keyword rules remain useful as cheap deterministic locators, but they are not treated as the ceiling of machine understanding. The C2D-S benchmark adds a full-transcript semantic pass that may identify relevant rationale even when no simple keyword rule fired. Its output must remain lightweight and provenance-linked.

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

Prefer windows that map to known Storyteller research needs and current Host LRE decision-family gaps:

- whole-setup choice rationale;
- healthy first-night pair/target construction;
- Drunk selection and persistent Drunk trajectory;
- healthy-information strength;
- impaired-information choice and longitudinal consistency;
- confirmation-chain severity;
- Spy/Recluse exposure versus concealment;
- Demon bluff and Red Herring selection;
- Mayor redirection and Demon succession when Storyteller-controlled;
- player experience / beginner handling;
- player agency;
- explicit preference/rejection/contrasted alternatives;
- reasons one output was chosen over another.

When EL-LRE has an active bounded request, raise windows with an explicit A-vs-B preference, explicit rejection or historical Storyteller choice plus rationale. Do not infer that other downstream-legal candidates were rejected merely because the source did not choose them.

Stop early on low-value generic discussion.

An episode may validly yield no promoted evidence.

## 8. Copyright boundary

Do not commit or durably publish:

- full audio;
- full machine transcript;
- large transcript excerpts.

Full audio and full ASR may exist temporarily in an explicitly marked Oracle-VM processing workspace for acquisition and semantic analysis. They must be deleted after the semantic-review session is complete or abandoned.

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

## 10. Current validation checkpoint

The C2 batch path completed bounded real Investigator/Imp validation and has since matured into the accepted queue-owned semantic workflow:

```text
live RSS
    -> stable manifest identity
    -> public audio acquisition
    -> timestamped ASR outside Git
    -> full-transcript semantic review
    -> lightweight timestamped findings
    -> bounded primary-audio verification when needed
    -> cleanup-current
```

C2D review-packet generation and the review CLI are implemented and GREEN. The Investigator full-transcript benchmark established machine-first semantic review as accepted acquisition assistance; machine output still cannot promote itself to VERIFIED evidence.

EL-LRE now supplies bounded Host-facing review priority without changing this pipeline. The first current target is the healthy Washerwoman review defined in `docs/EL_LRE_REPLACEMENT_POLICY_EVIDENCE_ALIGNMENT_2026-10-04.md`.

## 11. Success criterion

The batch workflow succeeds when automation reduces many hours of relevant expert audio to small, auditable human-review packets and those reviews add verified rationale dimensions or useful counterexamples.

Primary metric:

**verified high-value guidance per minute of human review**.
