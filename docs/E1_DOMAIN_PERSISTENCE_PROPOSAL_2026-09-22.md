# E1 Domain and Persistence Proposal — 2026-09-22

> Status: **FROZEN FOR E1 IMPLEMENTATION**
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

This stack is frozen for E1 implementation. E1 may refine dependency versions and internal module shape, but changing the language, working-store technology, persistence approach or migration strategy requires an explicit architecture update.

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

### E1-start ownership audit

Before implementation, E1 freezes these anti-dual-track rules:

- `Game.current_reconstruction_revision_id` is the single owner of which revision is current; revisions do not maintain a second mutable current/superseded status.
- `VerificationRecord` is the single owner of verification transitions; entity-level current verification is a projection, not a separately writable fact.
- reconstruction-dependent assertions are revision-scoped; raw/source-backed or non-reconstruction assertions are not silently attached to a revision.
- direct EvidenceFragment-to-event links are locator support only and do not create a parallel claim/verification subsystem.

These constraints prevent ownership duplication, reconstruction-revision leakage and provenance divergence without adding a new abstraction layer.

## 3. Minimum E1 domain model

The first persisted version should support these concepts.

### Source

Identity and locator for a primary/secondary source.

Needed fields include:

- semantic source ID;
- source type/platform;
- stable external locator and optional platform source ID;
- discovery path / inclusion reason;
- discovery metadata;
- screening status/result;
- reconstructability assessment;
- selection disposition / selected-for-reconstruction flag;
- rejection reason when applicable;
- metadata derivation/verification where material.

These are **separate workflow dimensions**, not one mutually exclusive status enum. A source may be discovered, screened, judged reconstructable and then selected; a rejected source still remains in the denominator.

These fields satisfy the source-census / selection-bias requirements without inventing a separate `ResearchLead` entity during E1.

Descriptive source metadata whose truth itself has evidentiary status—such as title, publisher/channel or publication date when those values are reconstructed or independently verified—is represented through ordinary `EvidenceAssertion` records whose subject is the `Source`. Do not duplicate those facts as independently writable `Source` fields. Stable locator/identity fields remain on `Source` because they identify where the evidence comes from rather than asserting game history.

### Storyteller

Stable public identity / independence key for Storyteller evidence aggregation.

Needed fields include:

- semantic Storyteller ID;
- public display name when appropriate;
- independence key;
- optional public identity/source links;
- no derived quality score.

Multiple games by the same Storyteller must resolve to the same independence identity when evidence supports that linkage.

### GameSeat

Game-scoped participant/seat identity.

This is required by the E0 pilot for stable references such as:

- Sullivan as the Drunk / shown Empath;
- Blair selecting Tom + Elliott;
- Jon receiving Chef information.

Needed fields include:

- semantic seat ID;
- game ID;
- seat/order label or number;
- display name / game-scoped participant label;
- optional evidence-backed player-experience metadata;
- no requirement for a global player identity.

Events, setup commitments and assertions should reference seat IDs rather than copying names into free text.

### Game

A reconstruction container.

Needed fields include:

- semantic game ID;
- script when known;
- Storyteller ID(s) / role context;
- player/table context such as beginner/new-player when evidenced;
- reconstruction status;
- current reconstruction revision ID, which is the sole authoritative pointer to the current revision.

### ReconstructionRevision

Versioned interpretation of a game's reconstructable historical state.

Needed fields include:

- semantic revision ID;
- game ID;
- parent revision ID when applicable;
- created_at;
- reason / concise change note;
- no independently writable current/superseded flag; currentness is derived from `Game.current_reconstruction_revision_id` and revision ancestry;
- no rewriting of raw EvidenceFragments.

Corrections to seating, setup interpretation, event order or decision boundaries create a new revision rather than silently mutating the evidence history.

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
- current verification status as a projection of VerificationRecord history (`UNVERIFIED` when no verification record exists), not as an independently writable source of truth;
- provenance links to one or more EvidenceFragments;
- optional reviewer inference provenance;
- assertion scope independent from derivation: evidence-scoped or reconstruction-scoped;
- reconstruction revision ID when and only when the assertion is reconstruction-scoped;
- supersedes relation where a reconstruction-dependent assertion replaces an earlier interpretation.

Raw/source-backed and non-reconstruction claims remain append-only and have no reconstruction revision ID. Reconstruction-dependent assertions must carry a reconstruction revision ID and are revised by creating a new revision-scoped assertion or superseding relation rather than mutating prior history in place. Derivation does not determine revision scope: for example, source metadata may be RECONSTRUCTED without belonging to a game ReconstructionRevision, while an INFERRED reviewer interpretation may be revision-scoped. An assertion must never be silently reused across revisions merely because its structured value happens to match.

### SetupCommitment

A reconstructed setup-time commitment/fact.

Must support:

- semantic commitment ID;
- game ID;
- reconstruction revision ID;
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
- reconstruction revision ID;
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
- reconstruction revision ID;
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

VerificationRecord is the sole write/audit owner of verification transitions. A target's current verification status is a derived projection from this history; do not maintain a second mutable verification flag that can diverge.

Minimum fields:

- verification record ID;
- target type + semantic target ID;
- resulting verification status;
- reviewer key;
- reviewed_at;
- evidence fragment IDs checked;
- concise note.

### Storyteller qualification evidence

Do **not** create a second evidence entity for Storyteller qualification.

Qualification facts are ordinary `EvidenceAssertion` records whose subject is a `Storyteller`, backed by the normal Source / EvidenceFragment provenance and VerificationRecord audit trail.

Examples:

- long-running official/community Storyteller involvement;
- official content/convention role;
- other evidence supporting the project's trust/experience classification.

A Storyteller qualification summary or derived status may be materialized as a view/application projection later, but the evidence owner remains `EvidenceAssertion`.

This avoids a second derivation/verification/provenance model.

## 4. Provenance relationships

E1 must support:

```text
Storyteller       1:N  Game role assignments
Game              1:N  GameSeat
Game              1:N  ReconstructionRevision
ReconstructionRevision 1:N SetupCommitment / SemanticEvent / DecisionSlice
EvidenceFragment  N:M  EvidenceAssertion
EvidenceAssertion N:M  SetupCommitment / SemanticEvent
EvidenceFragment  N:M  SemanticEvent when direct locator linkage is useful (this does not replace assertion-level derivation/verification where a concrete factual claim is being made)
DecisionSlice     -> observed-choice assertion(s)
DecisionSlice     -> explicit prefix members
DecisionSlice     -> rationale/rejected-alternative assertions
VerificationRecord -> any verifiable semantic target
```

Events and setup commitments must reference `GameSeat` semantic IDs when they refer to players/seats. Do not rely on copied display names as identity.

Do not assume one source fragment maps to one event.

## 5. Decision-prefix representation

E0 showed that a single integer boundary is insufficient.

For E1, prefer an explicit prefix reference within one ReconstructionRevision:

- reconstruction revision ID;
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

- working-store schema version `1`, represented by Alembic revision `0001_provenance_core`;
- Alembic as the sole owner of working-store migration position; do not add a second mutable schema-version table;
- forward-only deterministic migrations;
- migration history committed to Git;
- no production database checked into Git;
- tiny test databases created dynamically by tests;
- a test proving the historical migration schema matches the current SQLAlchemy Core metadata shape.

The E0 pilot should be represented as a small versioned public corpus fixture/export only after the generic schema exists.

Do not encode A Stud player names, seat count or role-specific fields into table structure.

## 9. Versioned interchange

Use a versioned bundle envelope, conceptually:

```json
{
  "schema_version": 1,
  "exported_at": "...",
  "storytellers": [],
  "games": [],
  "game_seats": [],
  "reconstruction_revisions": [],
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

E1 may introduce a narrowly named provenance-core interchange before later reconstruction entities exist. That first contract must contain only implemented semantics; do not add empty speculative entity records merely to mimic the eventual full-corpus bundle. A later full-corpus interchange may version independently when Game/Reconstruction/Decision semantics are implemented.

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

- create/read/update reconstruction revision without rewriting raw evidence;
- source discovery / screening / reconstructability / selection / rejection dimensions round-trip without collapsing into one state;
- Storyteller independence identity round-trip;
- SetupCommitment / SemanticEvent / DecisionSlice cannot silently cross ReconstructionRevision boundaries;
- GameSeat references survive setup/event/decision round-trip;
- evidence N:M provenance round-trip;
- verification record round-trip;
- migration from empty DB to schema v1;
- JSON export/import round-trip including Storyteller-subject qualification assertions.

Tier 2 / pilot regression:

Represent the E0 A Stud pilot generically and prove:

- the nine game-scoped seats can be referenced stably without creating global player identities;
- Sullivan actual Drunk + shown Empath can require multiple fragments/assertions;
- Chef=1 survives as a verified delivery without becoming a DecisionSlice;
- Drunk-Empath 0 preserves rationale and rejected alternative 2;
- Fortune Teller YES preserves OBSERVED result + INFERRED reviewer witness + UNKNOWN source-observed witness without collapsing statuses;
- a corrected reconstruction can create a new revision without rewriting the raw primary fragments or the prior revision.

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
7. then add Storyteller / Game / GameSeat / ReconstructionRevision;
8. then add SetupCommitment / SemanticEvent / DecisionSlice / VerificationRecord;
9. represent Storyteller qualification through ordinary Storyteller-subject EvidenceAssertions, with no parallel evidence subsystem.

This sequence proves the provenance core before adding higher-level reconstruction structures.

Do not start E2 UI until the full E0 pilot can round-trip without information loss.
