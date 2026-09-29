# Clocktower Evidence Lab — Current Development Roadmap

> Status: **E0 COMPLETE / E1 COMPLETE / C0 COMPLETE / C1 COMPLETE / C2 ACTIVE**
>
> Current task: **C2 — Trouble Brewing Podcast Batch Ingestion**

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

### C2A — manifest

Enumerate relevant episodes from live RSS and deduplicate already-processed episodes by stable source identity.

### C2B — batch acquisition

Use feed transcript when present; otherwise acquire public audio outside Git and run timestamped ASR.

### C2C — structured extraction

Extract timestamped candidate windows for Storyteller decisions, rationale, setup reasoning, misinformation, registration, bluff selection, player experience, player agency, information strength, trajectories and explicit alternatives.

### C2D — bounded human review

Rank by current product relevance and novelty. Human-review only the high-value windows needed to promote evidence.

### C2E — evidence promotion

After primary-audio review, save concise provenance-backed expert-guidance evidence. Do not commit full transcripts.

Authority: `docs/C2_TB_PODCAST_BATCH_INGESTION_2026-09-29.md`.

## 5. C2 implementation constraints

- do not block C2 on YouTube automation;
- do not retranscribe already-processed stable episode identities unnecessarily;
- do not add a database migration merely to store temporary ASR output;
- keep full audio/transcripts outside Git;
- test stable manifest/extraction contracts and pure transformations;
- preserve machine-vs-human verification state explicitly;
- allow an episode to yield no useful candidate without treating that as failure.

## 6. Immediate next action

Start C2A.

Expected first implementation slice:

1. inspect the retained podcast acquisition code;
2. add a reproducible series/episode manifest contract;
3. enumerate the live RSS feed;
4. identify Trouble Brewing-relevant episodes and prior-processing status;
5. write focused tests for identity/dedup/status semantics;
6. run the normal Ruff/pytest quality gate;
7. only then begin batch ASR/extraction.

Do not reopen C1 or broad whole-game scouting unless C2 uncovers a concrete evidence dependency.

## 7. Deferred

- broad non-Trouble-Brewing acquisition;
- Storyteller-app telemetry;
- UI expansion;
- new persistence migrations without demonstrated need;
- policy scoring inside Evidence Lab;
- fully automated verification with no human promotion gate;
- YouTube-specific batch automation as a dependency of C2.
