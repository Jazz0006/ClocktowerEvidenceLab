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

## Current targeted evidence gap — C1

The current product-directed gap is **Drunk assignment**.

CampBoardGameHost is moving from treating the selected Drunk identity as a fixed input to asking the Storyteller Decision Engine to choose which already-shown Townsfolk seat is actually the Drunk.

Evidence Lab therefore needs to preserve:

- the historical setup prefix immediately before that choice;
- the observed selected seat / shown role;
- explicit assignment rationale or alternatives when the source actually states them;
- later Drunk misinformation as a separate decision.

Evidence Lab does not derive the legal candidate set. That remains downstream rules-engine work.

C1A, C1B and C1C are complete. The bounded targeted-acquisition pass reached the replay target without reopening broad corpus growth.

C1C now has three `PREFIX_RECONSTRUCTABLE` Drunk-assignment cases:

- E0 `A Stud In Scarlet`: complete layout -> Sullivan / shown Empath selected as Drunk -> later Red Herring;
- `A Fond Farewell`: complete layout -> Chef selected as Drunk with explicit rationale -> later Red Herring/bluffs;
- The Megavoid Game 2: complete layout -> shown Empath selected as Drunk because adjacent to the Demon -> later information/bluff decisions.

The replay quota is **3 / 3**, with **2 explicit historical assignment-rationale cases**. Targeted C1C acquisition is stopped.

The next step is C1D: hand one stable historical prefix + observed choice + provenance package to CampBoardGameHost. CampBoardGameHost remains responsible for legal candidate derivation and recommendation replay/evaluation.

See:

- `docs/C1_DRUNK_ASSIGNMENT_EVIDENCE_UPGRADE_2026-09-28.md`;
- `docs/C1B_EXISTING_DRUNK_ASSIGNMENT_REAUDIT_2026-09-28.md`;
- `docs/C1C_TARGETED_DRUNK_ASSIGNMENT_ACQUISITION_2026-09-28.md`.

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
