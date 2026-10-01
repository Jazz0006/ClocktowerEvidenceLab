# NEXT DEVELOPMENT HANDOFF — C2 Podcast Batch Ingestion + C3 Drunk Candidate Comparison

> Current state: **C2 ACTIVE / C3 HOST-UNBLOCKING LANE ACTIVE / EL-TBGS-0/1 CROSS-PROJECT ACCEPTED**
>
> Branch: `experiment/investigator-semantic-review`
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
10. `docs/C2D_PRIMARY_AUDIO_REVIEW_QUEUE_2026-09-30.md`
11. `docs/C3_DRUNK_CANDIDATE_COMPARISON_EVIDENCE_2026-09-30.md`
12. `docs/TB_GAME_SNAPSHOT_INTEROPERABILITY_ROUTE_2026-09-30.md`
13. `docs/EL_TBGS_0_1_MAPPING_AND_IMPLEMENTATION_AUDIT_2026-09-30.md`
14. this file

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

C2D-S full-transcript semantic review is now **accepted for machine-first review assistance** after the Investigator benchmark. The Oracle VM produced a complete 2,156-segment `small.en` ASR, the semantic reviewer read the full transcript, timestamps were independently corrected against raw ASR, and the user confirmed the extracted Storyteller guidance was materially correct based on a prior full-episode listen.

One human correction is retained as a regression/QA example: the machine over-generalized the Spy discussion. The user's interpretation is that a one-Minion Spy + Investigator setup is comparatively uncommon because direct exposure reduces Spy operating room; if that exact setup exists, the Storyteller may have little alternative about which actual Minion can be identified.

The default clear-podcast path is therefore complete ASR -> full-transcript semantic extraction -> targeted human verification -> VERIFIED promotion. Full-episode human listening is reserved for low-confidence ASR, attribution/semantic conflicts, or sampled QA. Full audio/transcripts remain temporary and outside Git.

Mini MCP currently exposes fixed Oracle allow-listed Investigator `prepare/render/cleanup` tasks plus ASR dependency installation. The next workflow slice is to generalize the same bounded task pattern to additional explicitly selected podcast episodes rather than returning to whole-episode manual listening.

A new cross-project evidence dependency from CampBoardGameHost is now recorded as **C3 — Drunk Candidate Comparison / Rejection Evidence**. C3 does not reopen broad Drunk scouting and does not stop C2. It reuses C2C/C2D to target explicit same-prefix comparisons, rejections and conditional preferences. The first acceptance gate is one primary-audio VERIFIED item with a fixed setup/history prefix, candidate A vs candidate B, explicit preference/rejection, rationale and reconstructable assignment-time context.

The C2C/C2D audit found no need for a new evidence schema or ranking subsystem: `EXPLICIT_ALTERNATIVE` is already P0. The implementation enhancement adds conservative locator coverage for explicit rejection, explicit preference and conditional Drunk-assignment expressions.

The TB snapshot interoperability dependency is now closed for the current Drunk surface. Host TBGS-1 has accepted the EvidenceLab materializer/fixture and independently confirmed the G10 V1 payload byte-for-byte. No persistence migration, legality layer, or policy semantics were added. Host's post-TBGS-1 cutover recheck remains NOT PASSED solely because C3 has no Stage-1 VERIFIED same-prefix candidate comparison/rejection item yet.

Latest known code checkpoint before this documentation sync:
- production/test HEAD: `4d8da2c4be0eae40570ffea4134d9536bc748a5d`;
- PR #8: Draft / mergeable;
- bounded validation run #4: SUCCESS, run ID `36574401873`;
- quality #284: SUCCESS across Install / Ruff check / Ruff format / Pytest.

## 3. Current task

Keep **C2 and C3 moving in parallel**; C3 is now the only EvidenceLab lane that can unblock the current Host Drunk production-policy gate:

- treat the Investigator C2D-S benchmark as accepted for machine-first semantic review assistance;
- generalize the same bounded full-transcript workflow to additional explicitly selected clear podcast episodes, using targeted human verification instead of routine full-episode listening;
- keep VERIFIED evidence promotion human-confirmed; semantic output remains review assistance rather than automatic evidence promotion;
- continue automatic C2 batch ingestion rather than pausing for C3;
- route newly found explicit Drunk candidate comparisons/rejections through the same C2C -> C2D -> human verification path;
- treat EL-TBGS-0/1 as accepted/closed unless a later bounded TB surface requires another field;
- review `C3-Q01` first (`02:04:10–02:07:39`, about 3m29s); if it is Stage-1 qualifying, stop the C3 search and prepare the Host handoff immediately;
- if Q01 fails, review Q02 then Q03; include the standard snapshot when the evidence prefix is sufficient.

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

in parallel:
Host TBGS-0 contract                         COMPLETE / ACCEPTED
    -> EvidenceLab TB snapshot mapping audit COMPLETE
    -> pure materializer + deterministic V1 serialization COMPLETE / GREEN
    -> G10 cross-project golden fixture      COMPLETE / exact Host match
    -> Host TBGS-1 consumption               COMPLETE / ACCEPTED
    -> post-TBGS-1 cutover gate              NOT PASSED / BLOCKED ON C3 VERIFIED EVIDENCE
```

Use the existing manifest, batch runner and ASR adapter. Do not add a persistence migration merely for snapshot interoperability or temporary acquisition artifacts.

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
- do not treat machine confidence as verification;
- do not make the TB snapshot a second canonical reconstruction store;
- do not copy Host legality or legal-candidate enumeration into EvidenceLab;
- do not generalize the snapshot contract beyond Trouble Brewing before a real second-script need exists.

## 9. Historical documents

The pre-C2 roadmap/source-strategy/C1 handoff snapshots were moved under `docs/archive/` so they remain available for provenance without competing with the current authority.

Current authority is the C2 document set listed in section 1.
