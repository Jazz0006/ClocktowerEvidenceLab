# Clocktower Evidence Lab

Clocktower Evidence Lab is a local-first evidence collection and reconstruction project for real **Blood on the Clocktower** games.

Its first objective is deliberately narrow:

> Turn high-value external real games—especially games run by verified experienced/trusted Storytellers—into structured, verifiable Storyteller decision evidence that can be reused by CampBoardGameHost and future research.

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
versioned canonical reconstruction
    ↓
decision-time slices
    ↓
verification
    ↓
versioned export
    ↓
CampBoardGameHost analysis
```

## First-phase scope

The first phase focuses on external evidence only:

1. expert / official primary-video games;
2. other high-fidelity real-game videos;
3. structured public game records such as ClockTracker;
4. community reports and postmortems as qualitative evidence.

Direct telemetry from the Storyteller app is explicitly deferred.

## Storage direction

The project is local-first.

- **SQLite** is the working database.
- **JSON / JSONL** is the durable interchange and archive format.
- Public source media is not copied into the repository; retain source identifiers, URLs, timestamps and concise evidential notes.
- Small curated public reconstructions may be versioned in Git.
- A large corpus may later move to separate storage without changing the canonical export contract.

See:

- `AGENTS.md`
- `docs/ARCHITECTURE.md`
- `docs/EVIDENCE_AND_PROVENANCE_STANDARD.md`
- `docs/SOURCE_COLLECTION_STRATEGY.md`
- `docs/TESTING_STRATEGY.md`
- `docs/CURRENT_DEVELOPMENT_ROADMAP.md`
- `docs/NEXT_DEVELOPMENT_HANDOFF.md`
