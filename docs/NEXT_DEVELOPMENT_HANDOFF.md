# NEXT DEVELOPMENT HANDOFF — C2 Podcast Batch Ingestion

> Current state: **C2 ACTIVE**
>
> Branch: `docs/podcast-batch-ingestion-route-20260929`
>
> Repository: `Jazz0006/ClocktowerEvidenceLab`

## 1. Read first

Read in this order:

1. `AGENTS.md`
2. `README.md`
3. `docs/ARCHITECTURE.md`
4. `docs/EVIDENCE_AND_PROVENANCE_STANDARD.md`
5. `docs/SOURCE_COLLECTION_STRATEGY.md`
6. `docs/TESTING_STRATEGY.md`
7. `docs/CURRENT_DEVELOPMENT_ROADMAP.md`
8. `docs/PODCAST_EXPERT_RATIONALE_ACQUISITION_WORKFLOW.md`
9. `docs/C2_TB_PODCAST_BATCH_INGESTION_2026-09-29.md`
10. this file

At the start of the next conversation, re-check live `main`, this branch, open PRs/checks and exact file state. Do not assume this handoff's branch status is still live.

## 2. Current baseline

C1 remains complete and broad Drunk-assignment acquisition remains stopped.

C2 has now completed two implementation slices:

- **C2A manifest — COMPLETE / GREEN**
  - live RSS parser + show/episode metadata;
  - stable source identity;
  - Trouble Brewing scope classification;
  - independent acquisition / ASR / extraction / human-review state;
  - stable-GUID deduplication of the retained Drunk, Librarian and Recluse scouts;
  - manifest CLI and bounded live-RSS validation.
- **C2B batch acquisition — IMPLEMENTATION COMPLETE / GREEN**
  - advertised-transcript-first planning;
  - audio + optional faster-whisper fallback;
  - explicit external work directory;
  - resumable payload download;
  - resumable ASR without needless retranscription;
  - blocked-locator preservation;
  - batch runner + CLI;
  - progress application that cannot promote extraction/human-review/verification state.

The latest C2B quality gate passed Install / Ruff check / Ruff format / Pytest.

A real multi-episode batch has **not** yet been claimed as reviewed evidence. Full audio/transcript artifacts must remain outside Git.

## 3. Current task

Implement **C2C — structured candidate extraction**.

Goal:

```text
external feed transcript / ASR artifact
    -> timestamp-preserving machine candidate extraction
    -> lightweight candidate records
    -> zero-or-more candidates per episode
    -> later relevance ranking / bounded human review
```

Do not start by manually listening to whole episodes.

## 4. C2C minimum contract

Each candidate should preserve at least:

- stable episode/source ID;
- start/end timestamp;
- candidate category;
- concise machine summary;
- optional role/mechanism tags;
- machine extraction quality/confidence when useful;
- human-review state.

Initial categories remain those defined in the C2 authority document, including Storyteller decision/rationale, setup reasoning, misinformation, registration, Demon bluff reasoning, player experience/agency, information strength, confirmation chains, longitudinal trajectories, explicit alternatives and real-game examples.

Do not put the complete transcript text into Git-managed candidate artifacts.

## 5. Required invariants

1. extraction is a locator/triage layer, not evidence verification;
2. candidate timestamps survive deterministic serialization;
3. extraction complete does not imply human review complete;
4. ASR complete does not imply extraction complete;
5. an in-scope episode may validly yield zero useful candidates;
6. candidate records do not embed full copyrighted transcript payloads;
7. source identity is stable and inherited from the C2A manifest;
8. C2C remains source-generic enough to accept feed transcripts or ASR segments without creating a second evidence subsystem.

## 6. Implementation sequence

```text
define candidate domain/serialization contract
    -> focused tests
    -> deterministic extraction primitives over timestamped segments
    -> lightweight artifact writer
    -> quality gate
    -> bounded real multi-episode C2B run
    -> C2C extraction over that batch
    -> C2D relevance/review packets
```

Use the existing manifest, batch runner and ASR adapter. Do not add a persistence migration unless this real workflow proves lightweight artifacts insufficient.

## 7. Evidence boundary

Machine transcript/candidate extraction is acquisition assistance only.

Promotion requires primary-audio review confirming speaker, meaning, context and timestamp.

Keep full copyrighted audio/transcripts outside Git.

## 8. Do not do

- do not reopen broad C1 Drunk acquisition;
- do not switch back to quota-driven whole-game collection;
- do not implement BotC legality or policy scoring;
- do not add persistence migrations without a demonstrated batch-workflow need;
- do not make YouTube automation a prerequisite for C2;
- do not treat machine confidence as verification.

## 9. Historical documents

The pre-C2 roadmap/source-strategy/C1 handoff snapshots were moved under `docs/archive/` so they remain available for provenance without competing with the current authority.

Current authority is the C2 document set listed in section 1.
