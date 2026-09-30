# Clocktower Evidence Lab — Current Development Roadmap

> Status: **E0 COMPLETE / E1 COMPLETE / C0 COMPLETE / C1 COMPLETE / C2 ACTIVE / C3 TARGETED LANE ACTIVE**
>
> Current task: **C2 — Trouble Brewing Podcast Batch Ingestion**, with **C3 — Drunk Candidate Comparison / Rejection Evidence** running as a narrow evidence lane over the same pipeline.

## 1. Program objective

Build a durable evidence system that replaces ad-hoc synthetic judgment with provenance-backed external evidence.

The corpus has two complementary tracks:

```text
whole real games
    -> historical reconstruction / replay evidence

qualified expert guidance
    -> rationale / policy-dimension evidence
```

Whole-game history remains the primary historical collection unit. Expert guidance does not become replay evidence merely because the source is authoritative.

## 2. Frozen boundaries

- Evidence Lab owns evidence, reconstruction, provenance, verification and acquisition workflow.
- CampBoardGameHost owns BotC legality, legal alternatives, world solving and recommendation policy.
- UNKNOWN is first-class.
- Later history must not leak backward into earlier decisions.
- machine extraction is not equivalent to verified evidence.
- raw copyrighted media and full transcripts stay outside Git.
- expert choice/guidance is evidence, not a GOOD/BAD policy label.
- whole-game and expert-guidance corpora remain distinguishable even when they inform the same downstream feature.

## 3. Completed checkpoints

### E0 — evidence-contract pilot — COMPLETE

Established the source/evidence/reconstruction/verification contract using a real primary-source Trouble Brewing game.

### E1 — domain and persistence foundation — COMPLETE / MERGED

Established Python/Pydantic/SQLite/SQLAlchemy/Alembic/pytest/Ruff foundation, provenance entities, versioned interchange, reconstruction identity, setup/event history and durable evidence invariants.

### C0 — Trouble Brewing acquisition/reconstruction checkpoint — COMPLETE

Established a representative whole-game corpus and cross-project evidence handoff. Broad quota-driven corpus growth is no longer the default.

### C1 — Drunk Assignment Evidence Upgrade — COMPLETE

Established:

- Drunk existence != Drunk assignment != Drunk misinformation;
- setup-time historical-prefix contracts;
- 3/3 replayable assignment cases;
- 2 explicit historical assignment-rationale cases;
- successful G10 downstream replay in CampBoardGameHost.

C1 targeted acquisition is stopped unless a concrete downstream gap reopens it.

## 4. Current checkpoint — C2 Podcast Batch Ingestion

The earlier podcast pilot proved the route:

```text
RSS -> audio locator -> ASR -> timestamped candidates -> bounded human review
```

Reusable RSS/ASR tooling and Drunk/Librarian/Recluse scout artifacts are already on main.

C2 now turns that one-off path into a batch pipeline for the remaining Trouble Brewing-relevant episodes of the same expert series.

### C2A — manifest — COMPLETE / GREEN

Live RSS inventory, stable source identity, Trouble Brewing scope classification, independent workflow states and Drunk/Librarian/Recluse prior-scout deduplication are implemented and covered by deterministic tests plus a bounded live RSS validation.

### C2B — batch acquisition — IMPLEMENTATION COMPLETE / GREEN

The batch planner/runner and CLI now:

- prefer advertised transcript locators when present;
- otherwise acquire public audio into an explicit external work directory;
- run timestamped ASR through the retained optional adapter;
- reuse existing payload and ASR artifacts after interruption;
- preserve blocked/missing-locator items explicitly;
- write only lightweight progress/updated-manifest metadata alongside external artifacts;
- never promote ASR completion into human review or evidence verification.

A bounded real two-episode operational validation has completed successfully for Investigator and Imp. This proves the C2B acquisition path on real inputs but does not mean the resulting candidates have been human-reviewed or promoted.

### C2C — structured extraction — IMPLEMENTATION COMPLETE / GREEN

The extractor now provides timestamp-preserving lightweight candidate artifacts across the C2 category set, including Storyteller decisions/rationale, setup reasoning, misinformation, registration, Demon bluff reasoning, player experience/agency, information strength, confirmation chains, longitudinal trajectories, explicit alternatives and real-game examples.

The extractor:
- preserves stable source identity and start/end timestamps;
- stores concise machine summaries/tags/confidence without transcript bodies;
- treats zero useful candidates as a normal completed extraction;
- keeps human-review state independent from extraction completion;
- matches rationale terms across adjacent ASR segments and merges overlapping windows to avoid duplicate review packets.

A bounded real two-episode C2B -> C2C validation has completed successfully for Investigator and Imp.

### C2D — bounded human review — IMPLEMENTATION GREEN / REAL REVIEW QUEUE READY

The review-packet model, deterministic candidate merge/ranking, time/window budgets, lightweight writer and `clocktower-podcast-review` CLI are implemented and GREEN. P0/P1/P2 remain review-triage priorities only and do not score Storyteller choices.

The successful bounded Investigator/Imp run #4 artifacts have now been passed through C2D without retranscription:

- Investigator: 63 machine candidates -> 53 merged windows -> 12 selected review windows covering 16 candidate hits; 127.32 seconds total review time.
- Imp: 61 machine candidates -> 50 merged windows -> 12 selected review windows covering 17 candidate hits; 258.28 seconds total review time.
- Combined bounded primary-audio queue: 24 windows / 385.60 seconds (6m25.6s).

Both review packets retain `human_review_state=NOT_STARTED`. Packet generation is acquisition assistance, not evidence verification. The next gate is actual human primary-audio review of those bounded windows.

### C2E — evidence promotion

After primary-audio review, save concise provenance-backed expert-guidance evidence. Do not commit full transcripts.

Authority: `docs/C2_TB_PODCAST_BATCH_INGESTION_2026-09-29.md`.

## 5. C3 — Drunk Candidate Comparison / Rejection Evidence — ACTIVE TARGETED LANE

CampBoardGameHost's Drunk-assignment production cutover audit established a concrete downstream gap: execution infrastructure is ready, but Beginner automatic assignment still lacks source-backed semantics for comparing or rejecting legal Drunk candidates under one fixed setup/history prefix.

C3 therefore reuses C2 rather than creating new acquisition infrastructure:

```text
RSS / audio
    -> ASR
    -> C2C candidate extraction
    -> C2D bounded review
    -> human primary-audio verification
    -> verified comparison evidence
```

The C2C/C2D audit found that `EXPLICIT_ALTERNATIVE` is already the correct semantic bucket and already receives P0 review priority. The narrow implementation gap is locator vocabulary: explicit rejection, explicit preference and conditional Drunk-assignment language must be discoverable even when the speaker does not say “Storyteller”.

C3 Stage-1 acceptance is **not a quota**. It is one VERIFIED item with:

```text
fixed setup/history prefix
+ candidate A vs candidate B
+ explicit preference/rejection
+ rationale
+ reconstructable assignment-time context
```

Once that exists, prepare an immediate EvidenceLab -> CampBoardGameHost handoff so the Host can test a first bounded, versioned Drunk production-policy predicate.

Do not infer rankings over unmentioned candidates, do not infer rules from outcomes, and do not encode legality or recommendation policy here. C5 / `BEGINNER_CONSERVATIVE_V2` remains a separate gate.

Authority: `docs/C3_DRUNK_CANDIDATE_COMPARISON_EVIDENCE_2026-09-30.md`.

## 6. C2 implementation constraints

- do not block C2 on YouTube automation;
- do not retranscribe already-processed stable episode identities unnecessarily;
- do not add a database migration merely to store temporary ASR output;
- keep full audio/transcripts outside Git;
- test stable manifest/extraction contracts and pure transformations;
- preserve machine-vs-human verification state explicitly;
- allow an episode to yield no useful candidate without treating that as failure.

## 7. Immediate next action

Continue both compatible lanes without interrupting C2:

1. perform the existing **C2D bounded primary-audio review** over the 24 Investigator/Imp windows (6m25.6s total), promoting only claims confirmed from primary audio;
2. continue C2 automatic batch ingestion for remaining Trouble Brewing-relevant podcast material;
3. apply the C3 locator enhancement to new/reprocessed C2C extraction so explicit candidate rejection/preference and conditional Drunk-assignment windows reach bounded review;
4. as soon as one C3 item satisfies the Stage-1 VERIFIED structure, prepare the Host handoff immediately rather than waiting for a sample quota.

Keep broad C1 Drunk scouting stopped. C3 is the concrete downstream evidence dependency and must stay comparison/rejection-focused.

## 8. Deferred

- broad non-Trouble-Brewing acquisition;
- Storyteller-app telemetry;
- UI expansion;
- new persistence migrations without demonstrated need;
- policy scoring inside Evidence Lab;
- fully automated verification with no human promotion gate;
- YouTube-specific batch automation as a dependency of C2.
