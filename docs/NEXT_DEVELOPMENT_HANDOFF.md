# NEXT DEVELOPMENT HANDOFF — C2 Podcast Batch Ingestion + C3 Drunk Candidate Comparison

> Current state: **C2 ACTIVE / C3 TARGETED LANE ACTIVE**
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
10. `docs/C2D_PRIMARY_AUDIO_REVIEW_QUEUE_2026-09-30.md`\n11. this file

At the start of the next conversation, re-check live `main`, this branch, open PRs/checks and exact file state. Do not assume this handoff's branch status is still live.

## 2. Current baseline

C1 remains complete and broad Drunk-assignment acquisition remains stopped.

C2 has now completed three implementation slices:

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

- **C2C structured candidate extraction — IMPLEMENTATION COMPLETE / GREEN**
  - timestamp-preserving lightweight candidate artifacts;
  - 13 C2 candidate categories;
  - concise machine summary/tags/confidence without transcript bodies;
  - zero-candidate episodes remain normal completed extraction;
  - human review remains independent from extraction completion;
  - adjacent-ASR-segment rationale matching with overlapping-window deduplication;
  - candidate CLI.

The latest C2C quality gate passed Install / Ruff check / Ruff format / Pytest.

A bounded real two-episode C2B -> C2C validation has completed successfully for **Investigator + Imp**. Full audio/transcript artifacts remained outside Git; the workflow uploaded lightweight validation artifacts only. This is acquisition/extraction validation, not reviewed evidence.

C2D implementation is now GREEN. `podcast_review.py`, focused tests and `podcast_review_cli.py` define deterministic merging, review priorities, review-time/window budgets, a lightweight packet writer and the `clocktower-podcast-review` entry point.

The successful real Investigator/Imp candidate artifacts from bounded validation run #4 were reused directly with no retranscription and converted into real C2D review packets:

- Investigator: 63 candidates -> 53 merged windows -> 12 selected windows / 16 selected candidate hits / 127.32 seconds;
- Imp: 61 candidates -> 50 merged windows -> 12 selected windows / 17 selected candidate hits / 258.28 seconds;
- combined: 24 windows / 385.60 seconds (6m25.6s).

Both packets remain `human_review_state=NOT_STARTED`; no candidate has been promoted to verified evidence. The durable per-window human-review queue is `docs/C2D_PRIMARY_AUDIO_REVIEW_QUEUE_2026-09-30.md`.

Latest known code checkpoint before this documentation sync:
- production/test HEAD: `4d8da2c4be0eae40570ffea4134d9536bc748a5d`;
- PR #8: Draft / mergeable;
- bounded validation run #4: SUCCESS, run ID `36574401873`;
- quality #284: SUCCESS across Install / Ruff check / Ruff format / Pytest.

## 3. Current task

Perform the **bounded primary-audio review** over the already-generated Investigator/Imp C2D packets, then enter C2E only for claims that the human review actually confirms.

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

Completed:

```text
C2A manifest
    -> C2B batch acquisition
    -> C2C candidate extraction
    -> bounded real Investigator/Imp validation
```

Current:

```text
C2D model/writer/CLI GREEN
    -> real Investigator/Imp review packets GENERATED
    -> bounded primary-audio review (24 windows / 6m25.6s)
    -> C2E verified guidance promotion
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
