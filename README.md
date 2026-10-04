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

## Current product checkpoint — C2 + EL-LRE

C1 Drunk Assignment Evidence Upgrade is **complete**. Its bounded acquisition target reached 3/3 replayable assignment cases and downstream replay succeeded, so broad Drunk-assignment searching remains stopped.

The primary acquisition lane remains **C2 — Trouble Brewing Podcast Batch Ingestion / full-transcript semantic review**. Host-facing triage is now governed by **EL-LRE — replacement-policy evidence alignment**: bounded evidence requests are prioritized by decision family, while Host remains the owner of legality, legal alternatives, versioned policy, replay/evaluation and production cutover.

**C3 — Drunk Candidate Comparison / Rejection Evidence** remains historically valid and Stage-1 accepted through human-verified Q04, but it is no longer the general continuation lane. Its comparison semantics are generalized by EL-LRE.

Current implementation status:

- **C2A episode manifest — COMPLETE / GREEN**;
- **C2B batch acquisition runner + CLI — COMPLETE / GREEN**;
- **C2C structured candidate extraction — COMPLETE / GREEN**;
- **bounded real multi-episode C2B -> C2C validation — COMPLETE / GREEN** for Investigator and Imp;
- **C2D bounded review packets + review CLI — IMPLEMENTATION GREEN**;
- **C2D-S queue-owned full-transcript semantic review — OPERATIONAL / ACCEPTED FOR MACHINE-FIRST REVIEW ASSISTANCE**;
- **EL-LRE0 Host LRE evidence alignment — AUDIT COMPLETE / DOCS-ONLY**.

The podcast route remains unchanged: queue-owned `prepare-next -> complete ASR -> full-transcript semantic review -> lightweight timestamped findings -> LRE-aware triage -> targeted human verification only where needed -> cleanup-current`. Full media/transcripts remain outside Git.

C2 and EL-LRE keep the evidence boundary explicit:

- full audio and machine transcripts stay outside Git;
- machine transcript/extraction/semantic understanding is acquisition and review assistance, not verification;
- primary-audio review is required before a finding becomes VERIFIED evidence;
- `OBSERVED_CHOICE`, `EXPLICIT_PREFERENCE`, `EXPLICIT_REJECTION`, `EXPLICIT_COMPARISON_LOSER`, downstream `LEGAL_UNCHOSEN`, and `SYNTHETIC_NEGATIVE` remain distinct;
- podcasts complement, but do not replace, whole-game reconstruction/replay evidence;
- generic expert comparative guidance can support a bounded policy dimension without being forced into a fabricated historical game;
- one expert choice never implies a global ranking.

The TB-only interoperability slice and EL-ML0 architecture remain accepted. Functioning Librarian V2 and `DRUNK_ASSIGNMENT_Q04_V1` are already Host-side production policy islands; EvidenceLab keeps their source evidence but does not reopen those scopes unless Host supplies a new bounded gap.

Start with:

- `docs/EL_LRE_REPLACEMENT_POLICY_EVIDENCE_ALIGNMENT_2026-10-04.md`;
- `docs/C2_TB_PODCAST_BATCH_INGESTION_2026-09-29.md`;
- `docs/PODCAST_EXPERT_RATIONALE_ACQUISITION_WORKFLOW.md`;
- `docs/ML_RECOMMENDATION_EVIDENCE_READINESS_CONTRACT_2026-10-03.md`;
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
- `docs/TB_GAME_SNAPSHOT_INTEROPERABILITY_ROUTE_2026-09-30.md`
- `docs/EL_TBGS_0_1_MAPPING_AND_IMPLEMENTATION_AUDIT_2026-09-30.md`
- `docs/PODCAST_EXPERT_RATIONALE_ACQUISITION_WORKFLOW.md`
