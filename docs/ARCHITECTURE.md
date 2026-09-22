# Architecture

## 1. Architectural objective

Clocktower Evidence Lab is an evidence-reconstruction system, not a game engine.

Its durable architecture should remain valid if:

- the UI is replaced;
- SQLite is replaced;
- the recommendation engine changes completely;
- CampBoardGameHost is refactored;
- new Blood on the Clocktower scripts are added;
- current policy hypotheses are rejected.

## 2. Logical layers

```text
Source Inventory
    ↓
Raw Evidence References
    ↓
Evidence Assertions
    ↓
Canonical Reconstruction
    ├── Setup / identities / commitments
    └── Ordered semantic event stream
    ↓
Decision Slices
    ↓
Verification
    ↓
Versioned Corpus Export
```

A downstream analysis path is separate:

```text
Versioned Corpus Export
    ↓
CampBoardGameHost canonical/rules projection
    ↓
Legal alternatives / registration witnesses
    ↓
Exact / topology diagnostics
    ↓
Policy research
```

No arrow from the downstream analysis path may rewrite historical evidence.

## 3. Core domain entities

### Source

A public or otherwise authorized evidence source.

Examples:

- YouTube video;
- official TPI recording;
- ClockTracker shared game;
- Reddit postmortem;
- published article.

Source stores identity and discovery/screening metadata, not reconstructed game truth.

### Game

A real game associated with one or more sources.

A game may be only partially reconstructed.

### EvidenceFragment

A precise location within a source.

For video this normally means source + timestamp or timestamp range.

For structured records it may be source + stable record locator.

### EvidenceAssertion

A claim derived from evidence.

Examples:

- seat 4 actual role is Recluse;
- the Poisoner targeted seat 7;
- the Storyteller delivered YES to the Fortune Teller.

Assertions carry derivation and verification state and link to evidence fragments.

### ReconstructionRevision

A versioned coherent interpretation of the game based on assertions.

A new revision may correct or refine an earlier one.

### SemanticEvent

An ordered historical event.

Events model game semantics, not UI clicks.

The first implementation should support a small extensible set such as:

```text
SETUP_COMMITTED
PHASE_CHANGED
PLAYER_ACTION_COMMITTED
STORYTELLER_CHOICE_COMMITTED
INFORMATION_DELIVERED
REGISTRATION_DECLARED
PUBLIC_REVEAL
NOMINATION
VOTE
EXECUTION
DEATH
ROLE_CHANGED
ALIGNMENT_CHANGED
GAME_ENDED
```

Payloads may be typed by event kind.

### DecisionSlice

A research-ready Storyteller decision with:

- a game/reconstruction reference;
- decision type;
- Storyteller identity;
- boundary event sequence;
- observed choice;
- source evidence;
- derivation/verification;
- optional rationale;
- optional explicitly rejected alternatives;
- contextual metadata.

A DecisionSlice does not contain a quality verdict.

### Storyteller

A stable public identity / independence key plus evidence supporting experience/trust qualification.

Multiple games by one Storyteller remain one independence source.

## 4. Event sourcing and snapshots

The authoritative history is the setup commitments plus ordered semantic events.

Derived snapshots may be stored for performance or UX:

- setup snapshot;
- phase boundary snapshot;
- decision boundary snapshot;
- final snapshot.

Snapshots are disposable materialized views and must not become a second source of truth.

## 5. Decision-time semantics

A DecisionSlice anchors to an event boundary.

Conceptually:

```text
events 1..N are committed
--------------------------
decision boundary
--------------------------
observed Storyteller choice
events N+1...
```

Downstream analysis receives the reconstruction prefix through `N`, plus the observed choice separately.

Later events are unavailable to the counterfactual reconstruction.

## 6. Persistence

### Working store

E1 freezes SQLite as the initial local working store, with SQLAlchemy 2.x Core as the persistence adapter layer and Alembic for deterministic migrations.

Pydantic domain models remain separate from SQL rows. SQLite primary keys or row identifiers must never become durable corpus identifiers, and persistence remains replaceable behind an application/persistence boundary.

### Durable export

Versioned JSON/JSONL.

The export contract is more durable than the working database schema.

Recommended conceptual export bundle:

```text
manifest.json
sources.jsonl
evidence_fragments.jsonl
assertions.jsonl
games.jsonl
events.jsonl
decisions.jsonl
storytellers.jsonl
```

The exact physical split may change after the E0 pilot.

## 7. Git policy for corpus data

Git may contain:

- schema definitions;
- public source catalog;
- small curated verified reconstructions;
- migration test data;
- documentation.

Do not commit:

- full video/audio;
- long transcripts;
- local working SQLite database;
- private submissions;
- bulk generated diagnostics.

If the corpus becomes large, move bulk data to separate storage while retaining stable export/import compatibility.

## 8. Integration with CampBoardGameHost

Initial integration is file-based export/import.

Avoid direct database coupling.

The Evidence Lab export should provide historical facts and decision boundary context.

CampBoardGameHost remains responsible for mapping that evidence into its current canonical rules/game-state representation.

This intentionally allows either project to evolve without owning the other's internal schema.
