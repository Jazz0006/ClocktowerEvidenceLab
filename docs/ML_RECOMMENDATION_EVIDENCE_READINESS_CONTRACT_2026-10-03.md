# ML Recommendation Evidence Readiness Contract — 2026-10-03

> Status: **EL-ML0 COMPLETE / ARCHITECTURE ACCEPTED**
>
> Scope: read-only architecture audit plus docs-only contract.
>
> Implementation status: **DEFERRED until evidence volume or a downstream dataset-builder need justifies code/schema work.**
>
> This document does not change C2 acquisition, evidence verification, Blood on the Clocktower legality, recommendation scoring, or production policy.

## 1. Purpose

Clocktower Evidence Lab should preserve today's high-quality Storyteller evidence so that a future Host-side or ModelLab-side dataset builder can project it into supervised, preference, and evaluation data without rewriting the historical evidence model.

The accepted architecture is:

```text
EvidenceLab canonical evidence
        ↓
derived ML-ready Recommendation Evidence Seed
        ↓
CampBoardGameHost / future ModelLab enrichment
        ↓
Actual Training Example
```

The three layers have different ownership and must not be collapsed.

A future model may learn Storyteller recommendation / ranking / rationale behavior. The game engine and Host remain authoritative for rules, legal candidates, canonical game state, validation, and production safety boundaries.

## 2. Non-goals and frozen boundaries

EL-ML0 does **not** authorize EvidenceLab to:

- become a recommendation engine;
- implement BotC legality or enumerate legal candidates;
- score candidate quality;
- add GOOD/BAD labels;
- infer that every unchosen legal candidate was bad;
- synthesize preference labels from outcomes;
- add a SQLite/Alembic migration;
- start model training;
- change C2 podcast ingestion or verification gates;
- copy Host rules or canonical Game State ownership into EvidenceLab.

The central invariant remains:

```text
expert chose A != B/C/D are bad
```

Likewise:

```text
observed historical choice != explicit preference
explicit preference != global ranking
legal unchosen != source-backed rejection
synthetic negative != historical evidence
```

## 3. Layer 1 — EvidenceLab canonical evidence

EvidenceLab continues to own source-backed history and expert evidence.

Canonical inputs include:

- `Source`;
- `EvidenceFragment`;
- `EvidenceAssertion`;
- reconstruction identity and revisions;
- setup commitments and semantic event history;
- `HistoricalPrefixBoundary`;
- `DecisionSlice`;
- observed Storyteller choice;
- explicit rationale;
- explicitly considered alternatives;
- explicitly rejected alternatives;
- verification;
- Storyteller identity and `independence_key`;
- provenance.

Layer 1 records what the source supports. It must not be reshaped around one future training recipe.

### 3.1 Historical decisions

Historical decisions should continue to use `DecisionSlice` rather than creating a parallel ML-specific historical-decision model.

The current `DecisionSlice` already provides:

- stable decision identity;
- game and reconstruction identity;
- decision type;
- controller;
- a reusable historical-prefix boundary;
- observed choice;
- resulting-history link;
- rationale assertion references;
- explicitly considered alternatives;
- explicitly rejected alternatives.

`materialize_historical_prefix(...)` already enforces the most important anti-leakage invariant: the boundary must precede the resulting setup commitment or semantic event, and setup-time prefixes require evidenced historical ordering.

### 3.2 Current historical-decision gaps

The current historical decision model is sufficient as the canonical historical owner, but a future ML export cannot be produced from `DecisionSlice` alone.

The derived export will also need to join or project:

- source assertion IDs supporting the observed choice;
- verification state / verification audit trail;
- Storyteller identity;
- Storyteller `independence_key`;
- source IDs and fragment/assertion provenance;
- an explicit bounded-generalization statement when one exists.

These are composition/export concerns, not reasons to duplicate `DecisionSlice`.

The source tree currently defines the `Verification` enum and the evidence standard refers to a `VerificationRecord` audit trail, but no durable `VerificationRecord` domain object is currently implemented. EL-ML0 does not create one; this remains a future evidence-domain implementation decision.

## 4. Layer 2 — RecommendationEvidenceSeedV1

A future `RecommendationEvidenceSeedV1` should be a **derived export/projection contract**.

It is:

- not a new source of truth;
- not a recommendation;
- not a training label by itself;
- not allowed to add legal candidates;
- not allowed to convert absence of choice into negative evidence.

Its job is to package source-backed evidence in a shape that a downstream dataset builder can safely enrich.

### 4.1 Evidence kinds

At minimum:

```text
HISTORICAL_DECISION
EXPERT_GUIDANCE
```

`HISTORICAL_DECISION` is projected from a historical `DecisionSlice` plus its source/verification/Storyteller evidence.

`EXPERT_GUIDANCE` is projected from verified expert guidance that may not belong to any concrete historical game.

### 4.2 Conceptual V1 fields

The future contract should be versioned and include, where applicable:

```text
schema_version
seed_id
evidence_kind
decision_type

game_id
reconstruction_revision_id
historical_prefix_boundary

observed_choice

explicit_preference
explicitly_considered_candidates
explicitly_rejected_candidates
explicit_comparison_losers

condition_assertion_ids
rationale_assertion_ids
choice_or_preference_assertion_ids
source_assertion_ids
source_ids

verification
storyteller_id
storyteller_independence_key

bounded_generalization_scope
```

Rules:

- `game_id`, reconstruction identity and historical prefix are required for historical decision seeds and absent for pure general guidance unless the source actually refers to a concrete reconstructed game.
- `observed_choice` is historical evidence, not an automatic pairwise winner.
- `explicit_preference` must be source-backed and must preserve its named/expressed comparison scope.
- `explicitly_considered_candidates` mean only candidates the source actually considered.
- `explicitly_rejected_candidates` mean only source-backed rejection.
- `explicit_comparison_losers` mean only a source-backed loser in an explicit comparison.
- `bounded_generalization_scope` is a guardrail describing the source-supported condition/scope; it is not a policy rule.
- seed-level `verification` is only a projection/eligibility summary; underlying assertion-level verification/provenance remains authoritative and must stay traceable.

Stable seed IDs should be semantic and reproducible from canonical evidence identity, not database row IDs.

## 5. Candidate semantics and negative provenance

The following concepts must remain distinct across the ML pipeline.

### 5.1 Canonical evidence relations

EvidenceLab may directly support:

```text
OBSERVED_CHOICE
EXPLICIT_PREFERENCE
EXPLICIT_CONSIDERATION
EXPLICIT_REJECTION
EXPLICIT_COMPARISON_LOSER
```

Every canonical relation above must remain traceable to source/reconstruction provenance. Explicit preference, consideration, rejection, and comparison-loser relations require source-backed assertions for that stated relation; an observed historical choice may be observed or reconstructed, but the future seed must still carry the assertion/verification linkage supporting it.

### 5.2 Training-negative provenance

A downstream training/evaluation builder must preserve at least:

```text
EXPLICIT_REJECTED
EXPLICIT_COMPARISON_LOSER
LEGAL_UNCHOSEN
SYNTHETIC_NEGATIVE
```

The first two can be strong source-backed preference evidence when verified.

The latter two are downstream-derived categories:

- `LEGAL_UNCHOSEN`: Host/model-builder determined that a candidate was legal at that prefix but it was not chosen.
- `SYNTHETIC_NEGATIVE`: generated by a downstream training recipe.

EvidenceLab must not emit either as if it were source-backed rejection.

In particular:

```text
LEGAL_UNCHOSEN must never automatically become a DPO rejected sample.
```

A downstream experiment may choose to use legal-unchosen or synthetic candidates for a specific training objective, but it must preserve their provenance category and must not write that interpretation back into canonical evidence.

## 6. Layer 3 — RecommendationTrainingExampleV1

Actual training examples belong primarily to CampBoardGameHost or a future independent ModelLab / dataset builder.

Conceptually:

```text
RecommendationEvidenceSeedV1
+ canonical Game State at the historical prefix
+ legal candidate domain
+ optional recommendation context
+ explicit dataset/training recipe
= RecommendationTrainingExampleV1
```

Only Layer 3 may decide how one seed is converted into SFT, preference, ranking, or evaluation data.

EvidenceLab does not copy the Host rules engine merely to build this layer.

### 6.1 Input versus target separation

For historical recommendations, model input may contain only facts/context committed before the decision.

The observed choice, resulting commitment, source rationale, later history, and outcome are not pre-decision input features merely because they are useful training targets or evaluation metadata.

A training builder should explicitly separate:

```text
input_eligible
target_or_label
evaluation_metadata
provenance_only
```

This prevents accidental hindsight leakage.

## 7. Anti-leakage contract

The existing `HistoricalPrefixBoundary` is accepted as the foundation of future recommendation-training anti-leakage.

For a historical decision, model input must be derivable only from:

```text
historical state committed BEFORE the decision
```

It must exclude:

- the resulting decision itself;
- the resulting setup commitment or semantic event;
- later Storyteller decisions;
- later player actions;
- later deaths;
- later information;
- later public revelations;
- final outcome/winner;
- any later reconstruction fact that was not committed/available at the decision boundary.

For setup-time decisions, a canonical serialization order is not enough. `SetupOrderBasis.EVIDENCED` remains required when relative setup chronology is used to define the prefix.

For pure expert guidance such as Q04, there is no historical event prefix. The seed instead preserves only the source-stated condition and comparison scope; a downstream Host/ModelLab builder may later match that bounded guidance against canonical legal game states.

## 8. Expert comparative guidance

Q04 demonstrates a durable evidence shape that is not a historical `DecisionSlice`.

Forcing such material into `DecisionSlice` would require inventing a game identity, reconstruction revision, historical result link, or event chronology that the source does not supply.

Therefore EvidenceLab will likely need a future durable typed object for comparative expert guidance, conceptually named one of:

- `ExpertPreferenceEvidence`;
- `ComparativeGuidanceEvidence`.

EL-ML0 does **not** freeze the implementation name or persistence schema.

The minimum durable semantics should include:

```text
guidance_id
decision_type
condition_assertion_ids
candidate / option identities as stated by the source
explicit_preference_assertion_ids
explicit_rejection_or_loser_assertion_ids
rationale_assertion_ids
source_assertion_ids
verification
storyteller_id
storyteller_independence_key
bounded_generalization_scope
```

This object should reuse ordinary `EvidenceAssertion` / `EvidenceFragment` / `Source` provenance rather than create a second evidence subsystem.

Implementation should wait until verified comparative-guidance volume or C2E promotion needs justify a durable typed entity.

## 9. Dataset split and independence contract

Future train/eval splitting must support grouping by at least:

- `game_id`;
- `source_id`;
- Storyteller `independence_key`.

Required rule:

```text
different DecisionSlices from the same game must not be randomly split across train and evaluation
and then treated as independent evaluation examples.
```

Likewise, multiple clips/windows from one source episode should be groupable by `source_id`, and multiple games/guidance items from one Storyteller must remain identifiable through the same independence key.

The exact split policy belongs to ModelLab/dataset building, but EvidenceLab must preserve the grouping keys needed to enforce it.

## 10. Worked example 1 — Q04 Monk conditional preference

Source: `12: Monk (Trouble Brewing)`, verified primary-audio window `00:43:28–00:44:30`.

The verified evidence shape is:

```text
condition:
  setup/seating already fixed
  Empath between two Good players
  Empath away from the Demon

candidate A:
  Monk

candidate B:
  Empath

explicit preference:
  use Monk as the Drunk instead of the named Empath under this condition

rationale:
  preserve healthy Empath / information-role information
```

ML-readiness assessment:

- evidence kind: `EXPERT_GUIDANCE`;
- preference-training eligible in principle because the A-vs-B preference is explicit and source-backed;
- condition-bounded;
- rationale-backed;
- verified;
- must carry source and Storyteller independence provenance.

It must **not** be projected as:

```text
Monk > Empath globally
Monk > every other legal Drunk candidate
non-information role > information role
```

A future preference training example can only preserve the explicit comparison within the stated condition unless downstream evidence adds further support.

## 11. Worked example 2 — G10 Librarian pair at ~16:52

The historical evidence establishes:

- a concrete reconstructed game state;
- a functioning Librarian;
- observed information pair: actual Drunk-Empath + Undertaker;
- explicit rationale: both Empath and Undertaker produce recurring information, so uncertainty about which is Drunk affects interpretation of both future information streams;
- a qualified independent Storyteller identity.

Host can independently recover **40** legal functioning-Librarian truthful player-visible outcomes for that exact state.

ML-readiness assessment:

- evidence kind: `HISTORICAL_DECISION`;
- strong historical SFT/evaluation seed once the choice/provenance/verification joins are exported;
- historical prefix is the required model-input boundary;
- observed choice and rationale are target/evaluation evidence, not pre-decision input;
- Host may enrich the seed with the 40 legal outcomes.

EvidenceLab must not transform the Host's legal domain into:

```text
chosen Undertaker pair = good
other 39 legal outcomes = rejected
```

The other 39 are `LEGAL_UNCHOSEN`, not `EXPLICIT_REJECTED`.

Unless the source supplies a concrete A-vs-B comparison/rejection, G10 is not automatically a 1-positive / 39-negative preference dataset. It is presently better suited to historical SFT and held-out evaluation, with legal-domain enrichment performed downstream.

## 12. Audit result — what is already ML-ready

EvidenceLab already has strong foundations:

1. stable semantic IDs;
2. field/event-level source provenance;
3. derivation distinct from verification;
4. versioned reconstruction identity;
5. setup commitments plus ordered semantic event history;
6. `HistoricalPrefixBoundary`;
7. executable prevention of resulting-decision leakage in `DecisionSlice`;
8. observed choice kept separate from the historical prefix;
9. source-backed rationale references;
10. explicit considered/rejected alternatives represented separately from legal alternatives;
11. Storyteller identity and `independence_key`;
12. explicit project invariant that expert choice is evidence, not a quality label;
13. cross-project snapshot projection that leaves expert choice/rationale/provenance outside the pre-decision Game State.

These are the expensive architectural properties to get right. No new rules engine or training-specific database design is needed now.

## 13. Remaining structural gaps

The important future gaps are:

1. no implemented `RecommendationEvidenceSeedV1` derived export;
2. no durable typed expert-comparative-guidance entity for Q04-like evidence;
3. no implemented durable `VerificationRecord` object despite the documented verification/audit concept;
4. `DecisionSlice` does not itself carry observed-choice assertion IDs, Storyteller identity, verification, or source IDs, so a future seed exporter must join them from canonical evidence;
5. no dataset-builder contract yet combines seeds with Host canonical Game State / legal candidates;
6. no implemented split manifest/grouping contract for game/source/Storyteller independence.

These are future projection/dataset concerns. They do not invalidate today's canonical evidence.

## 14. What must be standardized now

EL-ML0 freezes the following semantics now because allowing ambiguity would lose information or create unsafe labels later:

- three-layer ownership boundary;
- `expert chose A != unchosen candidates are bad`;
- historical observed choice distinct from explicit preference;
- explicit rejection/comparison loser distinct from legal unchosen;
- legal unchosen distinct from synthetic negative;
- `LEGAL_UNCHOSEN` cannot automatically become DPO rejection;
- historical model input uses only pre-decision committed state;
- `HistoricalPrefixBoundary` is the anti-leakage foundation;
- Storyteller/source/game grouping keys must survive future export for independent evaluation;
- pure expert guidance must not be forced into a fabricated historical `DecisionSlice`.

## 15. What should be deferred

Defer until evidence volume or a concrete downstream consumer justifies implementation:

- Pydantic implementation of `RecommendationEvidenceSeedV1`;
- durable `ExpertPreferenceEvidence` / `ComparativeGuidanceEvidence`;
- training-example schema;
- dataset builder;
- SFT/DPO/QLoRA pipeline;
- model selection;
- negative sampling recipe;
- scoring/ranking objectives;
- persistence migration;
- cross-script generalization.

A useful implementation trigger would be either:

- enough verified historical/comparative items that manual handoff becomes error-prone; or
- a Host/ModelLab dataset-builder milestone that requires stable machine-readable export.

## 16. C2 impact

No immediate C2 pipeline change is required.

Current C2 behavior already preserves the information most important to future ML readiness:

- stable source identity;
- timestamps;
- candidate categories;
- bounded human verification;
- explicit alternatives/rejections when actually stated;
- concise provenance-backed promotion rather than transcript dumping.

C2 should continue as the primary lane.

When verified comparative guidance is promoted in C2E, reviewers should continue preserving conditions, named alternatives, rejection/preference wording, rationale, source identity, and speaker/Storyteller identity where available. This is a clarification of evidence fidelity, not a new C2 schema or workflow.

## 17. Accepted EL-ML0 decisions

```text
EL-ML0 COMPLETE / ARCHITECTURE ACCEPTED

RecommendationEvidenceSeedV1:
    YES — future derived export is warranted
    IMPLEMENTATION DEFERRED

ExpertPreferenceEvidence / ComparativeGuidanceEvidence:
    YES — likely needed for Q04-like durable typed guidance
    IMPLEMENTATION DEFERRED pending evidence volume

Production schema migration:
    NO

C2 immediate code/workflow changes:
    NO

BotC legality / legal candidate enumeration in EvidenceLab:
    NO

Training-example ownership:
    CampBoardGameHost or future ModelLab / dataset builder

Historical anti-leakage owner:
    EvidenceLab HistoricalPrefixBoundary + authoritative reconstruction prefix
```
