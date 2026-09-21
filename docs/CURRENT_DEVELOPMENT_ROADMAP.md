# Clocktower Evidence Lab — Current Development Roadmap

> Status: infrastructure/bootstrap design
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
- Working persistence is SQLite.
- Durable interchange is versioned JSON/JSONL.
- Raw media is referenced, not copied.
- Real corpus and regression fixtures remain separate.

## 3. Milestones

### E0 — Evidence contract pilot — NEXT

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

### E1 — Domain and persistence foundation

After E0 validates the workflow:

- choose implementation stack;
- define stable semantic IDs;
- implement domain entities;
- implement SQLite working store;
- implement schema version;
- implement deterministic migrations from the first persisted version;
- implement versioned JSON/JSONL export/import;
- add focused integrity tests.

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

Do not choose the UI framework before E0.

E1 should choose the smallest local-first stack that gives:

- strong typed/domain validation;
- SQLite support;
- deterministic migrations;
- easy JSON/JSONL;
- low-friction testing;
- practical desktop/local-browser workflow;
- future transcript/analysis tooling.

Python is a strong candidate because of the evidence-processing workload, but it is not yet a frozen implementation decision.
