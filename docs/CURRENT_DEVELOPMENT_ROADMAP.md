# Clocktower Evidence Lab — Current Development Roadmap

> Status: E0 COMPLETE / MERGED; E1 foundation — ACTIVE; C0 Trouble Brewing reconstruction — ACTIVE; C0-driven whole-game domain correction COMPLETE
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

### Immediate research gate — C0 Trouble Brewing evidence-acquisition sprint

The current Storyteller App supports **Trouble Brewing only**. C0 is therefore narrowed from a broad ClockTracker prevalence audit to a fast acquisition sprint for high-value Trouble Brewing whole games.

Do not spend current effort measuring other scripts. Unsupported scripts are out of scope for this gate.

Current target:

1. discover roughly 20–30 usable public Trouble Brewing whole-game records;
2. promote roughly 10–15 to A-grade when possible;
3. cover at least 2–3 independent Storytellers;
4. include several games with meaningful multi-night information evolution;
5. find 1–2 ClockTracker + primary-video same-game pairs for enrichment validation.

Prioritize records with interacting information mechanisms rather than isolated interesting clues. High-value examples include combinations of information Townsfolk with Drunk, Red Herring, Poisoner, Spy/Recluse registration, Demon bluffs and multi-night information changes.

A/B/C grading remains as defined in `docs/SOURCE_COLLECTION_STRATEGY.md`, but the success criterion is now product-directed:

~~~text
enough high-quality Trouble Brewing whole games
    → reconstruct interacting information bundles
    → compare with current Storyteller recommendation behavior
    → identify systematic policy/weighting gaps
~~~

The goal is not a statistically representative model of ClockTracker usage.

Initial C0 research has already established:

- public ClockTracker search/index surfaces many Trouble Brewing records across several communities and users;
- supply quantity is therefore unlikely to be the main bottleneck;
- at least one strong A-grade candidate has been verified: a 14-player Trouble Brewing game recorded by @sancho/Scott with detailed setup, Night/Day chronology, Poisoner targets, Drunk information, Red Herring, Spy registration, Ravenkeeper/Undertaker/Fortune Teller information and a later Imp transition;
- the remaining problem is efficient quality screening for detailed Notes and reconstructability.

The detailed sprint log is `docs/C0_TROUBLE_BREWING_ACQUISITION_SPRINT_2026-09-23.md`.

C0 has now crossed the acquisition threshold and begun formal whole-game reconstruction.

Current reconstruction artifacts:

- `docs/C0_TB_RECONSTRUCTION_BATCH_01_2026-09-23.md`;
- `docs/C0_TB_CROSS_GAME_ALGORITHM_FINDINGS_2026-09-23.md`.

The first batch includes an 8-player, 12-player and 14-player game plus one partial reconstruction. Scott/@sancho 2025-09-10 is currently the strongest record, with ordered Setup → Day 7 chronology.

C0 reconstruction has exposed blocking domain-model gaps before the old E1-7 persistence step:

1. explicit many-to-one Source → logical Game linkage with duplicate/match state;
2. first-class SetupCommitment;
3. ordered SemanticEvent / information-delivery history with revision and provenance boundaries.

The minimal contracts for those three concepts have now been implemented tests-first in `domain/history.py`.

RED commit: `cd8c9fa3a4dbf38f8e8fabbae451b1641efe3247` — quality failed as expected before the module existed.

GREEN commit: `7c245da6692b2dd33cec2f8599a7dd96487abcb0` — quality passed.

Do not immediately expand persistence merely because the contracts now exist.

The representative reconstruction set has now reached six games and the first live Storyteller App comparison is complete.

New authority:

- `docs/C0_TB_STORYTELLER_APP_ALGORITHM_GAP_AUDIT_2026-09-23.md`

Live CampBoardGameHost audit result:

- the SDE-3 feature contract already names the major evidence-backed dimensions;
- current structured shadow projection materially populates strategic diagnostics, while most non-strategic feature families remain `NOT_PROJECTED_YET`;
- `SdeDecisionInputBindings` has the correct committed/player-input shape, but the current structured adapter deliberately emits `NotCaptured`;
- the current production shadow is explicitly First-Night-only, so multi-night Drunk/Poisoner trajectories, confirmation chains and Demon succession are not yet replayable through that path;
- these are staged implementation gaps, not evidence for a new recommendation architecture.

Current product-directed priority is now to prepare a small replay-ready evidence package from the strongest reconstructed games, beginning with R04, and to keep targeted rationale acquisition focused on the remaining policy-strength gaps rather than returning to broad source discovery.

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

C0-driven whole-game history contract correction — COMPLETE:

- `SourceGameLink` + explicit match status;
- `SetupCommitment`;
- ordered `SemanticEvent`;
- generic `ControlOwner`;
- revision-scoped setup/history;
- UNKNOWN-friendly actor/value fields;
- no source timestamp leakage into semantic event time;
- no Trouble-Brewing-specific policy code.

Next product-directed action:

- continue reconstructing the existing A-grade Trouble Brewing queue;
- prioritize whole-game bundles with multi-night information interaction;
- begin algorithm-facing comparison once a small representative set is reconstructed;
- defer persistence expansion unless manual reconstruction is materially blocked by lack of durable storage.

When persistence becomes the bottleneck, resume with:

- extend SQLAlchemy/Alembic schema for Storyteller / Game / StorytellerAssignment / GameSeat / ReconstructionRevision plus the newly required whole-game linkage/history entities;
- add append-only persistence round trips;
- enforce same-game and revision referential integrity;
- preserve Game as sole current-revision owner.

DecisionSlice / VerificationRecord remain later E1 work after the historical game model is durable.

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
