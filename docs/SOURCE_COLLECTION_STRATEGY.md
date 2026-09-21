# External Source Collection Strategy

## 1. Goal

Build a broad but provenance-aware external real-game corpus that can replace ad-hoc synthetic human labeling as the primary calibration reference for Storyteller decision research.

The first objective is not maximum volume.

It is a repeatable process with low enough human cost that the corpus can grow continuously.

## 2. Source priority

### Tier A — expert/trusted Storyteller primary recordings

Highest initial priority.

Examples include official TPI games and games run by independently verifiable experienced/trusted Storytellers.

These are the main source of candidate GOLD decision evidence.

### Tier B — high-fidelity primary real-game recordings

Useful even when Storyteller expertise is not independently established.

Strong for real-game generalization and later user-population research.

### Tier C — structured public game records

Examples include ClockTracker shared records.

Potentially large and machine-friendly, but often weaker on exact decision timing, rationale and complete committed-prefix reconstruction.

### Tier D — community reports / postmortems / discussions

Useful for:

- policy-dimension discovery;
- explicit rationale;
- unusual interaction discovery;
- source leads.

Do not treat them as equivalent to primary verification.

## 3. Source census before cherry-picking

For priority Storytellers/channels, maintain a census of discoverable eligible games rather than searching only for cases matching a current hypothesis.

A source inventory record should preserve:

- discovered;
- screened;
- reconstructable;
- selected;
- rejected;
- rejection reason.

This creates a denominator and makes selection bias visible.

## 4. Screening pass

Do not fully reconstruct every discovered game.

A cheap screening pass should determine:

- Storyteller identity;
- script;
- approximate player count;
- whether setup/seating is recoverable;
- whether night decisions are visible;
- whether the grimoire is visible;
- whether Storyteller commentary/rationale exists;
- whether the video is heavily edited;
- whether player experience can be established;
- which phases are reconstructable.

The screening score, if any, measures reconstruction value/cost only. It is not a Storyteller-quality score.

## 5. Reconstruction selection

Prefer a balanced queue.

Do not retain only:

- spectacular games;
- controversial games;
- algorithm failures;
- strange role interactions.

Track selection reason.

Recommended reasons:

```text
EXPERT_SOURCE_CENSUS
SYSTEMATIC_SAMPLE
RANDOM_SAMPLE
TARGETED_RESEARCH_CASE
COMMUNITY_SUBMISSION
ALGORITHM_FAILURE_REPORT
OTHER
```

## 6. Initial expert coverage strategy

The first corpus should contain multiple independent Storytellers before drawing strong policy conclusions.

A practical initial target is:

- 2–3 reconstructable games from one well-documented expert Storyteller;
- 1–2 from a second independent expert Storyteller;
- at least one additional independent source when feasible.

The purpose is schema/workflow validation and independence, not statistical representativeness.

## 7. Human-in-the-loop automation

AI/tooling may assist with:

- transcript keyword search;
- candidate timestamp discovery;
- proposed semantic event extraction;
- duplicate-source detection;
- source metadata normalization.

AI proposals are not evidence by themselves.

Human verification remains required for evidence promoted to VERIFIED/GOLD.

## 8. Collection success metrics

Track:

- sources discovered;
- sources screened;
- reconstructable games;
- verified decision slices;
- Storyteller independence count;
- decision-family coverage;
- script coverage;
- player-experience coverage;
- average human effort per verified decision.

The last metric is a primary product metric for the Evidence Lab.
