# EL-ML1A — Decision Point Benchmark Corpus Audit — 2026-10-05

> Status: **COMPLETE / BENCHMARK CONTRACT ACCEPTED / CORPUS BUILD AUTHORIZED**
>
> Scope: read-only evidence inventory plus docs-only benchmark contract. No model training, no Host legality duplication, no recommendation scoring, and no persistence migration.
>
> Parent authority: `docs/ML_RECOMMENDATION_EVIDENCE_READINESS_CONTRACT_2026-10-03.md`.

## 1. Purpose

EL-ML1A answers a different question from EL-LRE policy evidence: how many historical Storyteller decisions can be presented to a model with a leak-free pre-decision state while Host independently recovers the legal candidate domain?

The target benchmark shape is:

```text
complete pre-decision Game State
+ Host-owned legal candidates
+ prior multi-clue / multi-night context
-> candidate ranking
-> whole-game rationale
```

The current corpus is large enough to start the benchmark pipeline, but not large enough for a credible model-vs-algorithm verdict or model training.

## 2. DecisionPointBenchmarkV1 conceptual contract

```text
benchmark_id
evidence_kind = HISTORICAL_DECISION | EXPERT_GUIDANCE_PROBE
decision_family
game_group
source_group
storyteller_independence_key
historical_prefix_boundary / materialization reference
observed_choice
choice_verification
controller_evidence
rationale assertion references
explicit considered/rejected/comparison-loser evidence
Host enrichment requirements
allowed evaluation modes
benchmark_readiness
```

This is a derived benchmark/export contract, not a new canonical evidence owner. Existing `DecisionSlice`, setup commitments, semantic events and provenance remain authoritative.

## 3. Readiness classes

**READY** requires a source-backed Storyteller-controlled choice, a pre-decision historical prefix complete enough to materialize the relevant state without hindsight, adequate provenance/verification, preserved game/source/Storyteller grouping, and a decision surface that Host can independently classify and enumerate.

Rationale and explicit alternatives make a point richer but are not required for READY.

**PARTIAL** means a useful historical choice still needs bounded repair such as exact-prefix materialization, a missing seat/role map, primary verification, or control/legality confirmation.

**NOT_USABLE** for the historical benchmark means player-controlled/rules-forced, result-only with no recoverable prefix, machine-only where verification remains required, inaccessible primary evidence, or hypothetical guidance. Pure guidance may still be retained as `EXPERT_GUIDANCE_PROBE` / retrieval evidence.

## 4. Conservative READY historical inventory

| ID | Game / decision | Evidence richness | Split group |
| --- | --- | --- | --- |
| DP-R01 | G01 `A Stud In Scarlet` — Drunk assignment: Sullivan shown Empath | prefix reconstructable; choice verified; rationale/alternatives unknown | G01 |
| DP-R02 | G01 — Drunk-Empath Night-1 info = `0` | prefix includes prior Chef `1`; explicit rationale; explicit rejected `2` | G01 |
| DP-R03 | G05 `A Fond Farewell` — Chef becomes Drunk | complete pre-assignment layout; explicit misinformation-plan rationale | G05 |
| DP-R04 | G05 — Red Herring = Lyra | ordering Drunk -> RH -> bluffs; explicit neighbour-check rationale | G05 |
| DP-R05 | G10 Game 2 — Empath becomes Drunk | complete nine-seat shown layout; explicit Demon-adjacency rationale | G10 |
| DP-R06 | G10 Game 2 — Librarian pair = Drunk-Empath + Undertaker | reconstructed state; explicit recurring-information rationale; Host already recovered 40 legal outcomes | G10 |

Conservative READY summary:

```text
READY historical decision points: 6
independent game groups:          3
Storyteller independence groups: approximately 2
rationale-rich READY points:      5
```

The six points are enough to validate a benchmark/export pipeline, but three games and roughly two Storyteller independence groups are far too concentrated for a model-strategy conclusion.

## 5. High-value PARTIAL historical inventory

These are distinct historical candidates and are not counted as READY until their stated gap is closed.

### G10 longitudinal decisions — same split group as DP-R05/DP-R06

- ~17:29 Drunk-Empath receives `0`;
- ~18:05 Drunk-Empath receives truthful `1`, explicitly used to redirect suspicion after the living-neighbour state changes;
- ~18:50 executed Spy bluffing Virgin is shown as Virgin to Undertaker to reinforce the public bluff.

These are high-value because they test cross-night history and public narrative. Their semantics are already strong, but exact pre-decision benchmark prefixes have not yet been materialized.

### Verified historical anecdotes needing exact-prefix reconstruction

- **FT1-A poisoned Fortune Teller:** observed `NO`, explicit legal `YES` alternative, contemporaneous future-chain rationale, and later retrospective preference shift. Very high priority because it cleanly separates decision-time reasoning from hindsight.
- **WW2 poisoned Washerwoman:** Demon + Demon-bluff false pair, explicit rationale and rejected failure mode; exact pre-decision state still needs reconstruction.
- **UT1-A / SR1-F Undertaker:** truthful Spy display chosen because the public narrative made the truth socially difficult; count once because both documents describe the same historical event.

### Investigator / Ravenkeeper historical candidates

- published expert real-game Drunk-Investigator Scarlet Woman clue inside a coherent false world;
- official February 2019 poisoned Investigator false Scarlet Woman clue;
- R02 Drunk-Investigator Scarlet Woman between Empath / Fortune Teller;
- published poisoned Ravenkeeper choosing Imp and being shown Mayor;
- existing whole-game reconstruction with poisoned Ravenkeeper choosing Imp and being shown Slayer.

These retain useful observed choices, but one or more of exact-prefix completeness, strict primary verification, rationale and candidate comparison are still missing.

### R04 replay-preparation candidates

R04 already identifies five candidate Storyteller decisions:

1. Red Herring setup;
2. Demon bluff bundle;
3. poisoned Brian Night-1 information;
4. Drunk Hylinn Night-1 information;
5. poisoned Wesley Night-4 Undertaker information.

The remaining blockers are bounded: verified clockwise seat order, full actual-role map, Hylinn shown role, Brian information role, and direct Demon-bluff confirmation. R04 is therefore a high-leverage repair target: one game-level reconstruction can unlock several early- and later-game benchmark points without creating false independence.

### R01 / R03 and DS1 leads

- R01 poisoned Washerwoman false Chef pair and R03 poisoned Fortune Teller `YES` preserve useful surrounding topology but are not benchmark-ready.
- DS1 Spy M11 describes a potentially excellent Star Pass successor comparison (less-trusted Baron chosen over trusted Spy because the Spy remained more valuable as support), but it is still machine-semantic/audio-ready and strict historical reconstruction is incomplete. Treat it as `NOT_USABLE YET / HIGH-VALUE VERIFICATION LEAD`.

Conservative current floor:

```text
high-value PARTIAL historical candidates: >= 18 distinct decisions
```

This number must not be interpreted as eighteen guaranteed future READY samples. Host control/legality review and EvidenceLab prefix repair may eliminate or merge candidates.

## 6. Expert guidance is a separate asset

The mature EL-LRE material — WW1, INV1, DB1, RH1, FT1 generic guidance, CHEF1, EM1, UT1 state-dependent guidance, LIB1, MR1 and Q04 — is already valuable for retrieval and explicit guidance probes.

Keep it as:

```text
EXPERT_GUIDANCE_PROBE / RETRIEVAL_EVIDENCE
```

not as historical whole-game benchmark rows. Q04 remains an excellent pairwise preference probe, but does not satisfy the historical Decision Point quota.

## 7. Pilot corpus target

### EL-ML1B pipeline target

```text
20-30 READY historical decision points
>= 8 independent game groups
>= 4 Storyteller independence groups
>= 6 decision families
>= 40% later-game / multi-night / history-sensitive points
```

This target is for benchmark-pipeline validation and an early pilot, not model training.

### First meaningful comparison target

```text
50-80 READY historical decision points
10-15+ games
3-5+ independent Storyteller/source groups
6-10 decision families
substantial later-game representation
```

A stronger Base-LLM-vs-RAG-vs-future-fine-tuning route decision should eventually aim for roughly 120-200 decision points from 25-40 games and 5+ Storyteller independence groups.

## 8. Acquisition strategy change

EL-ML1A changes the default marginal-value calculation. The benchmark gap should **not** trigger broad podcast policy mining.

Preferred order:

```text
1. repair existing whole-game PARTIAL decision points
2. extract more decisions from already-reconstructed games
3. targeted source reacquisition only for a specific missing prefix field
4. acquire new complete games only if repair cannot reach the pilot target
5. acquire new expert guidance only when benchmark errors expose a concrete reasoning gap
```

This preserves the project invariant that whole-game context is the primary acquisition unit.

## 9. EL-ML1B execution route

### ML1B-1 — materialize the six READY seeds

Do not wait for more collection. The benchmark now creates the first concrete downstream need for the smallest machine-readable `RecommendationEvidenceSeedV1` / benchmark-manifest projection.

Constraints:

- derived projection only;
- no new persistence authority;
- no legality enumeration in EvidenceLab;
- preserve verification/provenance and game/source/Storyteller grouping;
- preserve `observed choice != preference`.

### ML1B-2 — G10 longitudinal prefix extraction

Attempt bounded materialization for the three later G10 decisions. Use them to validate:

- multiple decision points sharing one game split group;
- cross-night/history/public-claim context;
- the Host-facing Game State fields required for later-game recommendation.

### ML1B-3 — close R04 blockers

Do not reconstruct R04 from scratch. Target only the known missing setup fields and bluff confirmation. If closed, R04 can contribute several points including the important Night-4 poisoned Undertaker case.

### ML1B-4 — promote FT1-A, WW2 and UT1-A historical prefixes

These already have unusually strong rationale evidence. The next value is state recovery, not another generic policy principle.

### ML1B-5 — repair R01/R02/R03 and official Investigator/Ravenkeeper cases

Use exact missing-field lists; preserve UNKNOWN when the primary source cannot close them.

### ML1B-6 — systematic new whole-game acquisition only if needed

If READY remains below 20 after repair:

- select complete Trouble Brewing games with Storyteller/grimoire visibility;
- prefer Storytellers not already dominant in the corpus;
- preserve every discretionary Storyteller decision found, not just spectacular cases;
- record inclusion/rejection reason for selection-bias control.

## 10. Benchmark split contract

Never split decisions from one game independently.

Minimum grouping keys:

```text
game_group
source_group
storyteller_independence_key
```

Rules:

1. all decision points from one game stay in the same split;
2. repeated clips/documents describing one historical event are one benchmark item;
3. multiple games from one Storyteller remain identifiable for independence-aware reporting;
4. multiple clips from one expert episode are not independent sources;
5. held-out historical choice/rationale and later outcomes must never enter inference input.

## 11. Allowed evaluation modes

### Legality

Host supplies legal candidates. The model ranks/selects only within that domain.

### Observed-choice rank

Report Top-1 / Top-3 / Top-5 and reciprocal rank of the historical choice. Unchosen legal candidates remain `LEGAL_UNCHOSEN`, not rejected.

### Explicit pairwise preference

Only when the source explicitly supports A over B or rejects B. Good examples include E0 Drunk-Empath `0` vs explicit rejected `2`, Q04 Monk vs Empath, and FT1-A's explicit current-night alternative with contemporaneous/hindsight separation.

### Rationale blind review

Hide source rationale from the model and judge whether it identifies the source-supported important factors without requiring wording imitation.

### Counterfactual sensitivity

Downstream may create clearly labelled synthetic counterfactuals that change one bounded factor such as player experience, neighbour alignment, prior information, public bluff or information topology. Synthetic cases never become historical evidence.

## 12. Experiment boundary after EL-ML1B

The first real experiment should compare:

```text
A. Current Host deterministic recommendation
B. Base LLM: Game State + Host legal candidates
C. LLM + retrieval: Game State + legal candidates + VERIFIED bounded EvidenceLab guidance
```

Historical observed choice, source rationale, explicit preference/rejection labels, later events and outcome remain hidden during inference.

Report legality, observed-choice rank, explicit-pairwise agreement where supported, rationale review and error families separately.

**No model training is authorized by EL-ML1A.**

## 13. Accepted EL-ML1A decisions

```text
EL-ML1A COMPLETE

DecisionPointBenchmarkV1 conceptual contract:
    ACCEPTED

Current conservative READY historical inventory:
    6 decisions / 3 games / ~2 Storyteller independence groups

Current high-value PARTIAL historical inventory:
    >= 18 distinct candidates, not guaranteed to promote

Pilot collection target:
    20-30 READY
    >= 8 games
    >= 4 Storyteller independence groups
    >= 40% history-sensitive later-game decisions

Broad podcast policy mining:
    NO LONGER DEFAULT

Primary next route:
    EL-ML1B — benchmark manifest + existing-corpus prefix repair

Model training:
    NOT AUTHORIZED

Host legality ownership:
    UNCHANGED

Canonical EvidenceLab schema/persistence:
    UNCHANGED
```
