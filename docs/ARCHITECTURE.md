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
Versioned Corpus Export / decision-time historical prefix
    ↓
TB-only standard snapshot materialization
    ↓
TroubleBrewingGameSnapshotV1-compatible interchange
    ↓
CampBoardGameHost rules / decision-context projection
    ↓
Legal alternatives / registration witnesses
    ↓
Exact / topology diagnostics
    ↓
Policy research
```

No arrow from the downstream analysis path may rewrite historical evidence. The TB snapshot is a derived interoperability view, not a second canonical reconstruction store.

## 2.1 Acquisition preprocessing boundary

C2 introduces a batch acquisition layer before durable evidence promotion:

```text
RSS / public media locator
    -> episode manifest
    -> transcript locator or ASR
    -> machine candidate extraction
    -> bounded human primary-source review
    -> EvidenceFragment / EvidenceAssertion
```

The episode manifest and machine extraction artifacts are workflow/acquisition data, not a parallel truth store.

They may track operational status such as acquired, ASR-complete, extracted or review-pending, but those states must not substitute for `Derivation` / `Verification`.

Full copyrighted media and full machine transcripts remain outside Git and need not enter the canonical evidence export.

This preprocessing layer should remain source-generic enough that future video/multimodal acquisition can feed the same reviewed-evidence boundary without changing core historical entities.

## 3. Core domain entities

### Source

A public or otherwise authorized evidence source.

Examples:

- YouTube video;
- official TPI recording;
- ClockTracker shared game;
- Reddit postmortem;
- published article.

Source stores stable source identity/locator plus discovery/screening workflow state, not reconstructed game truth. Descriptive source metadata that itself requires derivation/verification (for example a reconstructed title, publisher or publication date) uses ordinary Source-subject EvidenceAssertions rather than a parallel metadata-confidence system.

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

### HistoricalPrefixBoundary

A reusable decision-time boundary over the authoritative reconstruction history.

The boundary must support setup-time decisions as well as ordinary semantic events. It identifies what historical commitments/events are included immediately before a Storyteller decision.

A boundary must never include the resulting commitment/event of the decision it is used to analyse.

Setup ordering has two distinct meanings:

- `SetupOrderBasis.EVIDENCED`: the relative setup order is supported strongly enough to define a historical setup-time prefix;
- `SetupOrderBasis.CANONICAL_ONLY`: the order exists only to make reconstruction/serialization deterministic.

A `CANONICAL_ONLY` order must never be used to decide which setup commitments existed before a setup-time choice. It remains safe as deterministic presentation order for event-time decisions after setup as a whole is already committed.

### Setup-time decisions

Some Storyteller decisions occur while setup is still being committed rather than during the ordinary night/day event stream.

Drunk assignment is the current concrete example:

```text
shown-role / seat layout committed
    ↓
decision boundary
    ↓
Storyteller chooses one shown Townsfolk seat as the actual Drunk
    ↓
resulting SetupCommitment
```

The resulting setup fact remains authoritative reconstruction history. A DecisionSlice is a derived analytical view that references the relevant prefix and resulting commitment.

Evidence Lab stores explicitly observed considered/rejected alternatives when present, but legal-alternative enumeration belongs to the downstream rules consumer.

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

For the current Trouble Brewing-only interoperability route, decision-boundary snapshots should converge on the same domain semantics as CampBoardGameHost's versioned `TroubleBrewingGameSnapshotV1`. EvidenceLab materializes that snapshot from one reconstruction revision and one historical prefix; Host materializes it from live canonical setup/session/history owners.

The snapshot state-value contract distinguishes `KNOWN(value)`, `UNCOMMITTED`, `UNKNOWN`, and `NOT_APPLICABLE`. `UNCOMMITTED` means the historical decision creating the fact has not happened at that boundary; `UNKNOWN` means the fact cannot be established from the reconstruction. Evidence derivation/verification remains a separate provenance layer and must not be collapsed into those snapshot states.

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

Integration remains file-based export/import. Avoid direct database coupling and do not share mutable runtime objects across repositories.

For Trouble Brewing, the integration target is now a shared **versioned semantic snapshot contract** rather than bespoke per-case mapping:

```text
EvidenceLab
SetupCommitment + SemanticEvent prefix
    -> pure snapshot materializer
    -> TroubleBrewingGameSnapshotV1-compatible interchange

CampBoardGameHost
live canonical setup/session/history
    -> pure snapshot projector
    -> same TroubleBrewingGameSnapshotV1 semantics
```

Observed expert choice, rationale, explicit alternatives and provenance remain separate EvidenceLab decision/evidence records. They are not fields in the pre-decision game snapshot.

CampBoardGameHost remains responsible for BotC legality, legal candidate derivation, rules interpretation and recommendation policy after consuming the snapshot.

The first cross-project golden fixture is the already accepted G10 Drunk-assignment decision prefix: shown-seat layout known, Drunk presence known, Drunk assignment `UNCOMMITTED`, and all later setup/night facts excluded.

Do not add a persistence migration merely to support this first snapshot slice. The authoritative route is `docs/TB_GAME_SNAPSHOT_INTEROPERABILITY_ROUTE_2026-09-30.md`.
