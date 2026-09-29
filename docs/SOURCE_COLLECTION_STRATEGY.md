# External Source Collection Strategy

## 1. Goal

Build a provenance-aware corpus that supports Storyteller research through two complementary source families:

1. **whole real games** — the primary historical/replay evidence unit;
2. **qualified expert guidance** — a complementary rationale corpus used to explain, challenge or refine policy dimensions.

Decision slices and expert-guidance claims are derived research views. Neither should erase the underlying source/provenance boundary.

The first objective is not maximum volume. It is a repeatable process with low enough human cost that useful evidence can grow without discarding uncertainty.

## 2. Current product scope

CampBoardGameHost currently targets **Trouble Brewing**. Active Evidence Lab acquisition should therefore remain Trouble Brewing-first unless a concrete cross-script requirement is opened.

Unsupported scripts may be inventoried but should not consume current reconstruction/review effort.

## 3. Source families

### 3.1 Whole-game evidence — primary historical corpus

Preferred sources:

- high-fidelity structured public real-game records;
- expert/trusted Storyteller primary recordings;
- other reconstructable primary real-game recordings;
- linked multi-source records for the same game.

Preserve when evidence permits:

- setup/seating;
- shown roles;
- setup modifiers;
- Demon bluffs;
- ordered player actions;
- ordered Storyteller outputs;
- state changes;
- misinformation/registration choices;
- later-night evolution;
- outcome/context;
- explicit rationale.

The desired acquisition unit is still the whole game and its interacting information bundle.

### 3.2 Expert audio/podcast guidance — complementary rationale corpus

Public expert podcasts are valuable when a qualified Storyteller/designer discusses:

- why one legal choice may be preferable in one context and not another;
- setup-level reasoning;
- misinformation continuity;
- information strength;
- registration intent;
- bluff interaction;
- player experience;
- player agency;
- explicit considered/rejected alternatives;
- concrete real-game examples.

Podcast guidance is **not** a replayable historical game by default.

Machine transcripts are discovery aids and locator artifacts until primary-audio review promotes a concise claim into verified evidence.

Current active route: `docs/C2_TB_PODCAST_BATCH_INGESTION_2026-09-29.md`.

## 4. Current acquisition priority — C2 podcast batch

C1 Drunk-assignment acquisition is **complete and stopped** for the current product need.

Do not resume broad “find more games with a Drunk” searching unless a downstream replay exposes a concrete missing field.

The active acquisition task is now C2:

```text
live podcast RSS
    -> episode manifest
    -> transcript locator or ASR
    -> structured candidate extraction
    -> relevance ranking
    -> bounded human audio review
    -> concise provenance-backed expert guidance
```

The earlier Drunk, Librarian and Recluse podcast scouts prove the route and should be treated as already-processed source identities when building the batch manifest.

## 5. Podcast batch screening

For each episode, determine cheaply:

- stable source identity;
- Trouble Brewing relevance;
- expert/guest identity and qualification evidence;
- duration;
- audio availability;
- feed-advertised transcript availability;
- existing prior processing status;
- likely Storyteller/rationale density.

Prioritize episodes that directly address current algorithm dimensions.

Do not manually listen from the beginning unless automatic location fails.

## 6. Structured extraction target

Machine extraction should create candidate windows rather than verified claims.

Each candidate should preserve at least:

- source/episode ID;
- start/end timestamp;
- candidate category;
- concise machine summary;
- referenced role/mechanism when detectable;
- extraction confidence;
- human-review state.

Candidate categories should include Storyteller decisions/rationale, setup reasoning, misinformation, registration, bluff selection, player experience, player agency, information strength, longitudinal trajectories and explicit alternatives.

## 7. Human verification gate

AI/tooling may assist with:

- source inventory;
- deduplication;
- RSS parsing;
- transcript locator discovery;
- ASR;
- transcript keyword/semantic search;
- candidate classification;
- review-packet construction.

AI proposals are not evidence by themselves.

Promotion to VERIFIED expert guidance requires primary-source review sufficient to confirm:

- speaker;
- meaning;
- context;
- timestamp;
- source identity.

Use UNKNOWN rather than inventing attribution or motive.

## 8. Copyright/storage boundary

For public audio/video:

- store stable source identity and locator;
- store timestamps/ranges;
- store concise factual paraphrases;
- use minimal quotation only when evidentially necessary;
- keep full copyrighted audio/video outside Git;
- keep full machine transcripts outside Git.

Repository artifacts may contain lightweight acquisition metadata and short review packets.

## 9. Selection-bias control

Keep the whole-game corpus and expert-guidance corpus conceptually distinct.

For whole games, preserve discovery/screening/selection reasons and do not collect only spectacular cases.

For expert audio, maintain a reproducible episode manifest so the project can distinguish:

- discovered;
- in scope;
- processed;
- no useful rationale found;
- candidate windows found;
- human reviewed;
- promoted to verified guidance.

Do not retain only episodes that agree with a current Host hypothesis.

## 10. Success metrics

Whole-game track:

- trustworthy reconstructable games;
- independent Storyteller coverage;
- multi-night/multi-clue context;
- replayable decision prefixes;
- human effort per reconstruction.

Expert-audio track:

- relevant episodes inventoried;
- percent automatically acquired/transcribed;
- high-value candidate windows per episode;
- human review minutes per source hour;
- verified novel guidance items;
- independent expert coverage;
- explicit conflicting/contrasting guidance preserved.

The current C2 headline metric is **verified high-value guidance per minute of human review**, not transcript volume.
