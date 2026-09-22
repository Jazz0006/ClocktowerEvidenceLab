# E1 Domain and Persistence Proposal — 2026-09-22

> Status: **PROPOSED FROM COMPLETED E0**
>
> Goal: implement the smallest local-first foundation that can losslessly represent the E0 pilot and support reconstruction of a second real game.

## 1. Recommended foundation stack

Recommended baseline to freeze when E1 implementation is explicitly started:

- Python 3.12+;
- Pydantic v2 for domain/input validation;
- SQLite as the local working store;
- SQLAlchemy 2.x Core for persistence adapters;
- Alembic for deterministic schema migrations;
- pytest for tests;
- Ruff for formatting/linting;
- versioned JSON / JSONL for durable interchange.

This stack is an E1 proposal, not an implementation already authorized by E0 completion. Freeze it at E1 start after the user approves moving into implementation.

Do **not** choose the E2 UI framework yet.

Reasoning:

- evidence processing and future transcript tooling favor Python;
- SQLite fits local-first single-user evidence work;
- SQLAlchemy Core keeps persistence explicit without making ORM objects the domain model;
- Alembic gives auditable migrations from the first persisted version;
- Pydantic keeps UNKNOWN-friendly typed contracts separate from storage;
- JSON/JSONL remains easy to inspect, diff and hand off to CampBoardGameHost.

## 2. Ownership rule

Keep three boundaries separate:

```text
domain/evidence semantics
    ↓
application use-cases
    ↓
persistence adapters
```

Do not let SQLite rows or SQLAlchemy models become the authoritative domain API.

Stable semantic IDs are application/domain IDs.

Database row IDs, if used internally, must never become durable corpus identifiers.

### Decision-control taxonomy

Decision-control ownership is domain classification, not source provenance.

The E1 domain should be able to state that a decision family is player-controlled, Storyteller-controlled or unknown without pretending the primary source proved that classification.

Keep this lightweight: it is not a legality engine and must not enumerate legal alternatives.

## 3. Minimum E1 domain model

The first persisted version should support these concepts.

### Source

Identity and locator for a primary/secondary source.

Needed fields include:

- semantic source ID;
- source type/platform;
- stable external locator / platform ID;
- title/publisher/date when known;
- source fidelity/category;
- discovery/inclusion reason;
- metadata derivation/verification where material.

### Game

A reconstruction container.

Needed fields include:

- semantic game ID;
- script when known;
- storyteller identity/context;
- player/table context such as beginner/new-player when evidenced;
- reconstruction status;
- current reconstruction revision ID.

### EvidenceFragment

A source-region locator.

Must support:

- semantic fragment ID;
- source ID;
- source locator kind;
- start/end source timestamp when applicable;
- non-timed metadata/frame locator;
- concise evidence note;
- append-only raw evidence semantics.

A fragment timestamp means **source location only**.

### EvidenceAssertion

A concrete factual claim supported by evidence.

Must support:

- semantic assertion ID;
- subject / assertion type;
- structured value;
- derivation status;
- verification status;
- provenance links to one or more EvidenceFragments;
- optional reviewer inference provenance;
- revision history.

### SetupCommitment

A reconstructed setup-time commitment/fact.

Must support:

- semantic commitment ID;
- game ID;
- commitment kind;
- structured value;
- assertion/provenance links;
- historical ordering that may be partial/unknown.

Do not require a fake sequence number.

### SemanticEvent

A historical game event.

Must support at least:

- semantic event ID;
- game ID;
- phase;
- event kind;
- actor/control owner when known;
- structured payload;
- semantic order within the reconstructable portion;
- provenance links.

Source timestamps stay in EvidenceFragment, not SemanticEvent.

### DecisionSlice

A research-qualified Storyteller decision.

Must support:

- semantic decision ID;
- game ID;
- decision family/type;
- observed choice;
- links to evidence assertions/fragments;
- explicit decision prefix;
- rationale if source-supported;
- explicitly rejected alternatives if source-supported;
- actor if known;
- derivation/verification dimensions;
- GOLD qualification derived later from component evidence.

Do not store downstream legal alternatives in Evidence Lab.

### VerificationRecord

Audit trail for verification.

Minimum fields:

- verification record ID;
- target type + semantic target ID;
- resulting verification status;
- reviewer key;
- reviewed_at;
- evidence fragment IDs checked;
- concise note.

### StorytellerQualificationEvidence

Keep qualification evidence separate from individual game/decision evidence.

Minimum fields:

- storyteller key;
- source locator;
- concise qualification fact;
- derivation;
- verification.

## 4. Provenance relationships

E1 must support:

```text
EvidenceFragment  N:M  EvidenceAssertion
EvidenceAssertion N:M SetupCommitment / SemanticEvent
EvidenceFragment  N:M  SemanticEvent when direct linkage is useful
DecisionSlice     -> observed-choice assertion(s)
DecisionSlice     -> explicit prefix members
DecisionSlice     -> rationale/rejected-alternative assertions
VerificationRecord -> any verifiable semantic target
```

Do not assume one source fragment maps to one event.

## 5. Decision-prefix representation

E0 showed that a single integer boundary is insufficient.

For E1, prefer an explicit prefix reference:

- known prior setup commitment IDs;
- known prior semantic event IDs;
- ordering certainty / boundary note;
- unknown setup ordering is allowed.

The prefix is evidence-backed historical state, not a rules-engine world snapshot.

A derived snapshot may be built later, but the durable prefix references remain authoritative.

## 6. Historical ordering

Use two separate concepts:

### Source order

Lives only in source provenance:

- source timestamp/range;
- page/section/frame locator.

### Historical semantic order

Lives in reconstruction:

- phase;
- event order where known;
- partial/unknown order for setup commitments;
- explicit before/after constraints only where evidence supports them.

Do not infer setup order from edited video presentation order.

## 7. Derivation and verification enums

Persist independently.

Derivation:

- OBSERVED;
- RECONSTRUCTED;
- INFERRED;
- UNKNOWN;
- NOT_APPLICABLE.

Verification:

- UNVERIFIED;
- VERIFIED;
- DISPUTED.

Tests must prove that verification cannot silently rewrite derivation.

## 8. First migration / schema version

Start with:

- schema version `1`;
- forward-only deterministic migrations;
- migration history committed to Git;
- no production database checked into Git;
- a tiny test database created dynamically by tests.

The E0 pilot should be represented as a small versioned public corpus fixture/export only after the generic schema exists.

Do not encode A Stud player names, seat count or role-specific fields into table structure.

## 9. Versioned interchange

Use a versioned bundle envelope, conceptually:

```json
{
  "schema_version": 1,
  "exported_at": "...",
  "games": [],
  "sources": [],
  "evidence_fragments": [],
  "assertions": [],
  "setup_commitments": [],
  "events": [],
  "decision_slices": [],
  "verification_records": []
}
```

Exact JSON field names may evolve during E1 implementation.

For larger corpora, JSONL may split entity streams while retaining the same semantic IDs and schema version.

## 10. E1 tests required before E2

Tier 0 / domain:

- UNKNOWN round-trip;
- OBSERVED vs INFERRED preserved;
- verification independent from derivation;
- no implicit registration-witness promotion;
- decision prefix excludes later events;
- setup decisions can have unknown internal order;
- game-level context does not become choice-specific rationale;
- stable IDs independent of database row IDs.

Tier 1 / persistence:

- create/read/update reconstruction revision;
- evidence N:M provenance round-trip;
- verification record round-trip;
- migration from empty DB to schema v1;
- JSON export/import round-trip.

Tier 2 / pilot regression:

Represent the E0 A Stud pilot generically and prove:

- Sullivan actual Drunk + shown Empath can require multiple fragments/assertions;
- Chef=1 survives as a verified delivery without becoming a DecisionSlice;
- Drunk-Empath 0 preserves rationale and rejected alternative 2;
- Fortune Teller YES preserves OBSERVED result + INFERRED reviewer witness + UNKNOWN source-observed witness without collapsing statuses.

No test may branch on the case ID in production code.

## 11. Recommended initial repository shape

Create only when implementation begins:

```text
src/clocktower_evidence_lab/
    domain/
    application/
    persistence/
    interchange/

tests/
    domain/
    persistence/
    integration/
    pilot/

migrations/
schemas/
corpus/public/
```

Do not create empty modules solely to match this tree.

## 12. E1 first implementation slice

The smallest useful implementation slice should be:

1. project/quality tooling;
2. semantic ID + enums;
3. Source / EvidenceFragment / EvidenceAssertion;
4. SQLite schema v1 + migration;
5. persistence round-trip tests;
6. versioned export of those entities;
7. then add Game / SetupCommitment / SemanticEvent / DecisionSlice / VerificationRecord.

This sequence proves the provenance core before adding higher-level reconstruction structures.

Do not start E2 UI until the full E0 pilot can round-trip without information loss.
