# Clocktower Evidence Lab — Current Development Roadmap

> Status: E0 COMPLETE / MERGED; E1 domain and persistence foundation — ACTIVE (E1-3 COMPLETE)
>
> Primary objective: create a sustainable pipeline from external real-game sources to verified Storyteller decision evidence.

## 1. Program objective

Replace ad-hoc synthetic human labeling as the main calibration reference with a growing corpus of real, provenance-backed Storyteller decisions.

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

Next E1-4:

- implement repository/storage adapters for Source, EvidenceFragment and EvidenceAssertion;
- tests-first round-trip the domain models through migrated SQLite;
- enable SQLite foreign-key enforcement in the application connection owner;
- prove UNKNOWN/INFERRED, structured JSON, N:M fragment ordering and workflow dimensions survive round-trip without loss.

Later E1 steps:

- versioned JSON export;
- persistence round-trip tests;
- versioned JSON export;
- Storyteller / Game / GameSeat / ReconstructionRevision;
- SetupCommitment / SemanticEvent / DecisionSlice / VerificationRecord;
- Storyteller qualification through ordinary Storyteller-subject EvidenceAssertions.

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

### E3 — Verified expert corpus

Build a small independent expert corpus.

Targets are intentionally modest:

- several games from Ben Burns;
- at least one or two from Evin;
- at least one additional independent experienced/trusted Storyteller when feasible.

Measure:

- verified decision count;
- independence count;
- decision-family coverage;
- human minutes per verified decision.

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
- ClockTracker structured import;
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
