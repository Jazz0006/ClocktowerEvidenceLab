# Clocktower Evidence Lab — Current Development Roadmap

> Status: E0 COMPLETE / MERGED; E1 domain and persistence foundation — ACTIVE (E1-6 COMPLETE); ClockTracker source-quality research gate — NEXT
>
> Primary objective: create a sustainable pipeline from external real-game sources to trustworthy whole-game reconstructions, preserving the interacting information context from which Storyteller decisions can later be studied.

## 1. Program objective

Replace ad-hoc synthetic human labeling as the main empirical reference with a growing corpus of real, provenance-backed **whole games** run by experienced/trusted Storytellers.

The collection unit is the game history, not an isolated clue. The corpus should preserve multiple interacting information sources, setup commitments, later state changes and outcomes so downstream analysis can evaluate decisions in context.

Decision slices remain useful derived analytical views, but they are not the primary acquisition target.

The first product is an external evidence collector/reconstruction workbench.

Storyteller-app telemetry is deferred.

## 2. Frozen project principles

- Evidence Lab is independent from CampBoardGameHost.
- Evidence Lab does not own game legality or recommendation policy.
- Facts/reconstruction/inference are distinct.
- Provenance is field/event level.
- UNKNOWN is first-class.
- Historical event order and decision-time boundaries are first-class.
- Later history must not leak into earlier decision reconstruction.
- Expert choice is not a GOOD/BAD label.
- Winner is not a decision-quality label.
- Storyteller identity/independence is retained.
- GOLD is decision-level and derived.
- E1 implementation stack is frozen: Python 3.12+, Pydantic v2, SQLite, SQLAlchemy 2.x Core, Alembic, pytest, Ruff.
- Durable interchange is versioned JSON/JSONL; exact entity envelope can evolve during E1 without changing semantic ownership.
- Raw media is referenced, not copied.
- Real corpus and regression fixtures remain separate.
- Whole-game reconstruction is the primary collection unit; DecisionSlices are derived from the game history rather than driving source selection.
- Structured records and primary recordings are complementary evidence sources and may be linked to the same game.

## 2.1 Collection-route correction — 2026-09-23

Research after E0 established that the next collection problem is not finding more isolated Storyteller principles or single-decision examples.

The main research value comes from preserving **whole real games**, because multiple information choices interact and their effects only become visible in the evolving game state.

Current direction:

~~~text
high-quality structured real-game record
    ↓
whole-game reconstruction
    ↓
optional video/audio enrichment
    ↓
verified multi-clue historical context
    ↓
derived decision slices / downstream analysis
~~~

ClockTracker is now the first source family to audit because its current data model can represent substantially more than simple game-result statistics:

- structured grimoire tokens with role, related role, alignment, seat/order and player identity/name;
- death and ghost-vote state;
- reminder tokens;
- Demon bluffs and Fabled;
- Notes and final result;
- multiple grimoire pages, where later pages are cloned from earlier pages and then independently editable.

Important limitation: ClockTracker's `GrimoireSnapshot` feature is edit/restore history, not an automatic semantic per-night timeline. The inspected code also does not establish a canonical structured night-action/event log. Chronological reconstruction therefore depends on how completely a recorder used grimoire pages, reminders and Notes.

YouTube/video remains important, but its default role changes from primary manual reconstruction source to **enrichment source** for:

- spoken Storyteller rationale;
- claims / bluffs / table belief;
- exact action timing;
- gaps or ambiguities in structured records.

### Immediate research gate — C0 ClockTracker corpus suitability audit

Before continuing E1-7 implementation, run a bounded quality audit of approximately 50–100 public Storyteller-recorded ClockTracker games.

This is a screening study, not bulk corpus ingestion.

Measure at minimum:

1. proportion with complete/near-complete grimoire;
2. proportion with detailed ordered Notes;
3. presence of Demon bluffs and relevant reminder tokens;
4. use of multiple grimoire pages;
5. recoverability of nightly actions and delivered information;
6. recoverability of setup modifiers such as Drunk / Red Herring / poison state where applicable;
7. Storyteller identity and ability to establish expert/trusted status without guessing;
8. occurrence of explicit Storyteller rationale;
9. stable public locator/access characteristics;
10. approximate human effort needed to turn a strong record into a corpus-ready whole-game reconstruction.

Classify sampled records as A/B/C reconstructability as defined in `docs/SOURCE_COLLECTION_STRATEGY.md`.

Gate outcome:

- if A/B records are common enough, design later ingestion around ClockTracker-first reconstruction plus selective video enrichment;
- if strong records are rare, keep ClockTracker as a discovery/partial-state source and retain video as the primary reconstruction path;
- do not decide this from schema capability alone; measure actual public records.

E1-7 remains the next implementation step after this bounded research gate unless the audit exposes a domain-model gap that must be corrected first.

## 3. Milestones

### E0 — Evidence contract pilot — COMPLETE

Goal:

Manually reconstruct one high-value primary-source expert game using the proposed conceptual model before building application infrastructure around assumptions.

Preferred first case:

- Ben Burns — `A Stud In Scarlet`

Why:

- useful first-night information choices;
- Drunk shown identity/information;
- Fortune Teller interaction;
- Recluse registration implications;
- Chef information;
- existing D5F research context makes reconstruction gaps easier to identify.

Bootstrap gate completed on 2026-09-21:

- all eight bootstrap documents existed on the live repository;
- repository boundaries and evidence invariants were consistent;
- one conflict was corrected before pilot work: SQLite / exact working-store technology had been described as both frozen and deferred; it is now explicitly provisional through E0;
- working branch: `e0-evidence-contract-pilot`.

Pilot notebook:

- `docs/E0_A_STUD_IN_SCARLET_EVIDENCE_CONTRACT_PILOT.md`

Primary review packet:

- `docs/E0_A_STUD_IN_SCARLET_PRIMARY_REVIEW_PACKET.md`

Current pilot state:

- stable primary-video locator confirmed (`qZBvRfM3Xow`);
- first human primary-review pass completed with a setup/grimoire screenshot plus timestamps 09:49, 10:32, 11:53, 12:41 and 15:18;
- full visible setup/seating and Demon bluffs are now primary-supported;
- Sullivan actual Drunk + shown Empath and Red Herring setup commitments are primary-supported;
- Drunk-as-Empath 0 is primary-verified with explicit choice-specific rationale and explicit rejection of alternative 2;
- Fortune Teller Tom+Elliott -> YES is primary-verified as player action + delivered output; Recluse-as-Demon is retained only as an INFERRED reviewer interpretation while source-observed historical witness remains UNKNOWN;
- Chef=1 is primary-verified as a delivery event without being forced into a DecisionSlice;
- beginner/new-player table context is primary-reviewed and kept at game level rather than copied into every choice rationale;
- 3 E0 DecisionSlices are admitted, none GOLD-qualified yet;
- E0 completion audit: `docs/E0_EVIDENCE_CONTRACT_COMPLETION_AUDIT_2026-09-22.md`;
- E1 proposal: `docs/E1_DOMAIN_PERSISTENCE_PROPOSAL_2026-09-22.md`.

Deliverables:

1. source record;
2. screening record;
3. game/setup reconstruction;
4. ordered Night-1 event timeline;
5. at least 3 Storyteller decision slices;
6. evidence fragments/timestamps for material claims;
7. derivation + verification states;
8. explicit list of schema/workflow gaps discovered;
9. draft export shape.

Success condition:

A downstream researcher can understand exactly what happened, what remains unknown, and where every material assertion came from without consulting informal notes.

No production legality or policy scoring is implemented.

### E1 — Domain and persistence foundation — ACTIVE

E0 has validated the workflow and PR #1 has been squash-merged to `main` at `6a672a9dc6b7fa13f98aef8a7e6b1e616889d667`.

Current E1 branch: `e1-domain-persistence-foundation`.

Draft PR: `#2` — keep draft until explicit merge authorization.

Use `docs/E1_DOMAIN_PERSISTENCE_PROPOSAL_2026-09-22.md` as the implementation contract.

E1-start architecture audit froze these ownership constraints:

- `Game.current_reconstruction_revision_id` is the sole owner of current revision;
- `VerificationRecord` is the sole owner of verification transitions;
- reconstruction-dependent EvidenceAssertions must be explicitly revision-scoped;
- direct EvidenceFragment-to-event links are locator support, not a second claim/verification path.

E1-1 is complete:

- Python 3.12+ project/quality tooling is established;
- the E1 stack is frozen to Pydantic v2 + SQLite + SQLAlchemy Core + Alembic + pytest + Ruff + versioned JSON/JSONL;
- GitHub Actions runs the quality gate;
- stable semantic-ID validation exists independently of database rows;
- Derivation and Verification are separate durable enums.

E1-2 is complete:

- Source / EvidenceFragment / EvidenceAssertion domain contracts are implemented;
- source screening / reconstructability / selection remain independent workflow dimensions;
- source timestamps are locator-only and cannot masquerade as historical semantic time;
- EvidenceFragment ↔ EvidenceAssertion supports N:M provenance;
- reviewer inference remains explicitly INFERRED with reviewer provenance;
- Verification is not an independently writable EvidenceAssertion field;
- assertion revision scope is independent from derivation;
- reconstruction-scoped assertions require an explicit revision ID;
- evidentiary source metadata such as reconstructed title/publisher/date is expressed as Source-subject EvidenceAssertions, preventing a second metadata provenance system;
- final E1-2 quality gate is GREEN.

E1-3 is complete:

- current SQLAlchemy Core metadata exists for Source, EvidenceFragment, EvidenceAssertion and assertion-fragment N:M links;
- semantic IDs are database primary keys; no surrogate row IDs were introduced;
- Alembic revision `0001_provenance_core` deterministically migrates an empty SQLite database to schema v1;
- the historical migration is explicit and does not import current metadata to create tables;
- migration tests prove two fresh databases produce the same structural signature;
- migration tests prove current metadata and migrated schema agree on columns, primary/foreign keys, unique/check constraints and indexes;
- structured assertion JSON, source locator fields, assertion scope/revision identity and inference provenance are persisted structurally;
- EvidenceAssertion has no mutable verification column;
- the quality workflow now emits Ruff formatting diffs on failure;
- final E1-3 quality gate is GREEN.

E1-4 is complete:

- append-only SQLAlchemy Core store implemented for Source, EvidenceFragment and EvidenceAssertion;
- only insert/get operations exist; no update/delete/upsert path was introduced;
- application-owned SQLite engines enable `PRAGMA foreign_keys=ON` on every DBAPI connection;
- Source workflow dimensions and source locator timestamps round-trip exactly;
- assertion JSON values, derivation, inference provenance, scope and reconstruction revision ID round-trip without loss;
- ordered N:M assertion-fragment provenance survives persistence;
- orphan fragment references fail under foreign-key enforcement;
- assertion + fragment-link insert is transactional, so a failed provenance link leaves no partial assertion row;
- final E1-4 quality gate is GREEN.

E1-5 is complete:

- versioned provenance JSON envelope implemented for Source / EvidenceFragment / EvidenceAssertion;
- schema name/version are explicit and unsupported versions are rejected;
- canonical serialization is deterministic for the same semantic content and exported_at;
- bundle import validates duplicate semantic IDs and Source → Fragment / Assertion → Fragment referential integrity;
- UNKNOWN / INFERRED, reviewer inference provenance, structured JSON values and ordered assertion-fragment provenance round-trip without loss;
- export shape is domain-shaped rather than SQLite-shaped;
- source timestamps remain source-locator fields only;
- no placeholder Game/Storyteller/Decision records were invented;
- final E1-5 quality gate is GREEN at `7cfd032e15986e0b3247cb39210600dc14856bbd`.

E1-6 is complete:

- Storyteller / StorytellerAssignment / Game / GameSeat / ReconstructionRevision domain contracts are implemented tests-first;
- Storyteller stores stable identity and independence key but no qualification score;
- GameSeat is strictly game-scoped and exposes no global-player identity field;
- Game.current_reconstruction_revision_id is the only current-revision pointer;
- ReconstructionRevision contains game/parent identity, timezone-aware creation time and change note, with no second current/superseded flag;
- duplicate Storyteller assignments and self-parenting revisions are rejected;
- no SetupCommitment / SemanticEvent / DecisionSlice / VerificationRecord or rules logic was introduced;
- final E1-6 quality gate is GREEN at `0fc9f37c73be0374162cc1e7bdf2c9718f782be4`.

Next E1-7 — implementation resumes after C0:

- first review the C0 ClockTracker audit for any domain-model gap that affects whole-game reconstruction;
- then extend SQLAlchemy/Alembic schema for Storyteller / Game / GameSeat / ReconstructionRevision;
- add append-only persistence round-trip for those entities;
- enforce game-scoped foreign keys and same-game current/parent revision integrity where the persistence boundary has enough information;
- preserve Game as sole current-revision owner;
- do not add SetupCommitment / SemanticEvent / DecisionSlice / VerificationRecord yet.

Later E1 steps:

- extend versioned interchange for Storyteller / Game / GameSeat / ReconstructionRevision;
- add SetupCommitment / SemanticEvent / DecisionSlice / VerificationRecord;
- represent Storyteller qualification through ordinary Storyteller-subject EvidenceAssertions.

Success condition:

The E0 pilot can be represented and round-tripped without information loss.

### E2 — Minimal reconstruction workbench

Implement the minimum workflow UI:

1. Sources
2. Game Reconstruction
3. Decision Review
4. Corpus Browser

Required capabilities:

- source screening;
- timestamp evidence markers;
- seating/setup editor;
- semantic event timeline;
- decision boundary creation;
- rationale/rejected-alternative notes;
- partial reconstruction;
- UNKNOWN-friendly fields;
- verification pass.

Success condition:

A second expert game can be reconstructed substantially faster than E0 while preserving equal or better provenance quality.

### E3 — Verified expert whole-game corpus

Build a small independent corpus of reconstructable expert-run **whole games**.

Targets are intentionally modest and should be revisited after C0:

- several high-fidelity games from at least one well-documented expert Storyteller;
- games from at least one second independent expert Storyteller;
- at least one additional independent experienced/trusted Storyteller when feasible;
- prioritize games where multiple information sources interact across more than one phase.

Measure:

- reconstructable whole-game count;
- Storyteller independence count;
- multi-clue / multi-phase coverage;
- script and player-count coverage;
- verified decisions derivable from those games;
- human minutes per reconstructed whole game;
- incremental cost of video enrichment when a structured record already exists.

### E4 — CampBoardGameHost export bridge

Define a narrow file-based import contract.

CampBoardGameHost should consume:

- setup/commitment facts;
- ordered event prefix;
- observed decision;
- provenance/verification metadata.

CampBoardGameHost then reconstructs legal alternatives using its own rules owners.

Success condition:

At least one verified decision is replayed at the correct historical prefix and matched to the production legal candidate domain without hindsight leakage.

### E5 — Collection scale improvements

Only after workflow quality is proven:

- transcript-assisted timestamp discovery;
- AI-proposed event extraction with human confirmation;
- source census automation;
- duplicate detection;
- automated ClockTracker structured import, after C0 has established which public fields are actually reliable;
- batch corpus QA.

### E6 — Storyteller-app telemetry — DEFERRED

Later, design direct automatic capture from the Storyteller app.

Do not let future telemetry needs distort the first external-evidence collector.

## 4. Explicit non-goals before E4

Do not:

- build a recommendation engine;
- duplicate Blood on the Clocktower rules;
- assign GOOD/BAD expert labels;
- infer unchosen alternatives are bad;
- train a model;
- create cloud/backend infrastructure;
- ingest a large corpus before the workflow is validated;
- optimize for every future script before real evidence requires it.

## 5. Initial repository shape

Conceptual target:

```text
/
├── AGENTS.md
├── README.md
├── docs/
│   ├── ARCHITECTURE.md
│   ├── EVIDENCE_AND_PROVENANCE_STANDARD.md
│   ├── SOURCE_COLLECTION_STRATEGY.md
│   ├── TESTING_STRATEGY.md
│   ├── CURRENT_DEVELOPMENT_ROADMAP.md
│   └── NEXT_DEVELOPMENT_HANDOFF.md
├── schemas/
├── src/
├── tests/
└── corpus/
    └── public/
```

Do not create empty architecture layers merely to match the tree. Add them when E1 implementation gives them responsibility.

## 6. First implementation decision gate

The E1 foundation decision is now frozen:

- Python 3.12+;
- Pydantic v2;
- SQLite;
- SQLAlchemy 2.x Core;
- Alembic;
- pytest;
- Ruff;
- versioned JSON / JSONL.

Do not choose the E2 UI framework yet. The UI must adapt to the durable evidence/domain contract rather than owning it.
