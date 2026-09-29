# Clocktower Evidence Lab

Clocktower Evidence Lab is a local-first evidence collection and reconstruction project for real **Blood on the Clocktower** games.

Its first objective is deliberately narrow:

> Turn high-value external real games—especially games run by verified experienced/trusted Storytellers—into structured, verifiable whole-game evidence from which Storyteller decisions can later be studied in their full information context.

The project is **not** a recommendation engine and does not decide whether an observed Storyteller choice was good or bad.

## Project boundary

Clocktower Evidence Lab owns:

- external source discovery and screening;
- source inventory and reconstruction status;
- raw evidence references such as URL, source ID and timestamp;
- evidence assertions with field/event-level provenance;
- canonical reconstructed game history;
- decision-time boundaries;
- verification state;
- Storyteller identity / independence metadata;
- versioned corpus export.

CampBoardGameHost owns:

- game/rules legality;
- legal alternative enumeration;
- registration witness enumeration;
- exact/strategic world analysis;
- policy diagnostics;
- recommendation policy;
- later extraction of regression fixtures.

The Evidence Lab must never become a second Blood on the Clocktower rules engine.

## Core evidence flow

```text
source discovery
    ↓
source screening / census
    ↓
raw evidence references
    ↓
evidence assertions
    ↓
versioned canonical whole-game reconstruction
    ↓
ordered information / state history
    ↓
optional decision-time slices
    ↓
verification
    ↓
versioned export
    ↓
CampBoardGameHost analysis
```

## First-phase scope

The first phase focuses on external evidence only.

Collection is now **whole-game first**. The immediate source-research priority is:

1. high-fidelity structured public real-game records, especially ClockTracker records created by experienced/trusted Storytellers;
2. expert / official primary-video games used to fill missing rationale, table-state and social context;
3. other high-fidelity real-game videos;
4. community reports and postmortems as qualitative evidence.

A DecisionSlice is a downstream projection from a reconstructed game, not the primary acquisition unit.

Direct telemetry from the Storyteller app is explicitly deferred.

Targeted expert podcasts may also be used as a complementary **rationale source**. Podcast transcripts are discovery aids only: full audio/transcripts stay outside Git, and machine-located windows require primary-audio review before they become verified evidence.

See `docs/PODCAST_EXPERT_RATIONALE_ACQUISITION_WORKFLOW.md`.

## Current product checkpoint — C2

C1 Drunk Assignment Evidence Upgrade is **complete**. Its bounded acquisition target reached 3/3 replayable assignment cases and downstream replay succeeded, so broad Drunk-assignment searching remains stopped.

The active task is now **C2 — Trouble Brewing Podcast Batch Ingestion**.

Current implementation status:

- **C2A episode manifest — COMPLETE / GREEN**;
- **C2B batch acquisition runner + CLI — COMPLETE / GREEN**;
- **C2C structured candidate extraction — NEXT**.

The earlier podcast pilot proved that public RSS + audio enclosure + optional faster-whisper ASR can reduce long expert episodes to small timestamped review packets. C2 now has a reproducible manifest and resumable external-work-directory batch runner. A real multi-episode batch run, structured extraction, bounded human review and evidence promotion are still required before C2 itself is complete.

C2 keeps the evidence boundary explicit:

- full audio and machine transcripts stay outside Git;
- machine transcript/extraction is a locator and candidate-discovery layer;
- primary-audio review promotes only concise provenance-backed guidance;
- podcasts complement, but do not replace, whole-game reconstruction/replay evidence.

Start with:

- `docs/C2_TB_PODCAST_BATCH_INGESTION_2026-09-29.md`;
- `docs/PODCAST_EXPERT_RATIONALE_ACQUISITION_WORKFLOW.md`;
- `docs/NEXT_DEVELOPMENT_HANDOFF.md`.

## Storage direction

The project is local-first. E1 has frozen the initial implementation foundation:

- **Python 3.12+** with **Pydantic v2** for domain/input validation;
- **SQLite** as the local working database;
- **SQLAlchemy 2.x Core** for persistence adapters, without making database rows the domain API;
- **Alembic** for deterministic schema migrations;
- **pytest** and **Ruff** for the quality gate;
- **versioned JSON / JSONL** for durable interchange.

The E2 UI framework remains deliberately unfrozen.

Public source media is not copied into the repository; retain source identifiers, URLs, timestamps and concise evidential notes. Small curated public reconstructions may be versioned in Git. A large corpus may later move to separate storage without changing the canonical export contract.

See:

- `AGENTS.md`
- `docs/ARCHITECTURE.md`
- `docs/EVIDENCE_AND_PROVENANCE_STANDARD.md`
- `docs/SOURCE_COLLECTION_STRATEGY.md`
- `docs/TESTING_STRATEGY.md`
- `docs/CURRENT_DEVELOPMENT_ROADMAP.md`
- `docs/NEXT_DEVELOPMENT_HANDOFF.md`
- `docs/PODCAST_EXPERT_RATIONALE_ACQUISITION_WORKFLOW.md`
