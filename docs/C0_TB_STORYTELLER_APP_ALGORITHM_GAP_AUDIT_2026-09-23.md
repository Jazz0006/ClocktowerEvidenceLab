# C0 Trouble Brewing → Storyteller App Algorithm Gap Audit — 2026-09-23

## 1. Purpose

This audit compares the first six reconstructed real Trouble Brewing games in ClocktowerEvidenceLab against the **live** Storyteller Decision Engine contract in `Jazz0006/CampBoardGameHost`.

This is read-only product research.

It does **not** modify CampBoardGameHost, does not declare observed human choices optimal, and does not derive numeric policy weights from game outcomes.

Evidence inputs:

- R01 — Ash / @CryptCore — 12 players;
- R02 — Jeff / @CryptCore + @Larrikin — 8 players;
- R03 — Scott / @sancho — 2025-09-24 — partial;
- R04 — Scott / @sancho — 2025-09-10 — 14 players;
- R05 — Leo The Leopard — 8 players — partial;
- R06 — Debby — partial.

Reconstruction authority:

- `docs/C0_TB_RECONSTRUCTION_BATCH_01_2026-09-23.md`
- `docs/C0_TB_CROSS_GAME_ALGORITHM_FINDINGS_2026-09-23.md`

## 2. Live CampBoardGameHost state audited

Live state checked during this audit:

- SDE-3A checkpoint PR #151 is merged to `main`;
- live `main` at audit time: `d1f6a3b351f229196f68eed70eb897b16f5d3d8c`;
- active continuation PR #152:
  - branch `sde-3a-feature-projection-shadow-pipeline`;
  - draft;
  - head observed during audit: `63da5f339271ffef154febfed17807ba4b704aa1`;
  - SDE-3A structured feature-projection shadow is documented as acceptance-complete / pending merge;
  - SDE-3B `BEGINNER_CONSERVATIVE_V1` has not started on this branch.

Do not assume these refs remain current in a later conversation; re-query before acting.

## 3. High-level conclusion

The six real-game reconstructions **do not require a new SDE architecture**.

The current SDE-3 contract already names most of the correct qualitative dimensions:

- strategic topology / cover;
- confirmation-chain impact;
- healthy-information utility;
- truth danger / credibility disruption;
- role-function exposure;
- impaired narrative coherence;
- bluff narrative;
- candidate relationships;
- future flexibility.

The main gap is implementation depth:

> most evidence-relevant feature families exist as typed placeholders, but the current structured shadow only projects strategic diagnostics today.

A second gap is historical/context binding:

> the current structured shadow deliberately leaves `SdeDecisionInputBindings` as `NotCaptured` and is limited to round-one First Night.

These are compatible with the staged SDE-3 route, but they must remain explicit so SDE-3B does not accidentally treat unavailable context as absent context.

## 4. Feature-by-feature comparison

| Real-game requirement | Evidence | Current SDE-3 contract | Current live projection | Audit result |
| --- | --- | --- | --- | --- |
| normalized Evil/Demon topology impact | R01–R04 | `StrategicDecisionFeatures` | PROJECTED | strong match |
| player-count-normalized pressure | R02=8, R01=12, R04=14 | normalized strategic ratios + forced-good fraction | PROJECTED | strong match; no numeric gate yet |
| semantic truth/false status | poisoned/Drunk outputs in R01–R06 | `semanticTruth` feature exists | generally NOT_PROJECTED in current structured shadow path | projector gap |
| confirmation chains | R02 Undertaker confirms Drunk; R04 RK/UT chains | `ConfirmationChainFeatures` exists | NOT_PROJECTED_YET | projector gap |
| healthy information preserved/lost | multiple parallel truthful/false channels in R01/R04 | `HealthyInformationUtilityFeatures` exists | NOT_PROJECTED_YET | projector gap |
| truth danger / credibility disruption | R04 dense interacting information | `TruthCredibilityFeatures` exists | NOT_PROJECTED_YET | projector gap; preference strength still under-evidenced |
| role-function exposure | Investigator / Spy / Recluse ecology | `RoleFunctionExposureFeatures` exists | NOT_PROJECTED_YET | projector gap; severity intentionally uncalibrated |
| persistent Drunk perceived world | R02, R04 | `ImpairedNarrativeFeatures` + documented shared persistent narrative owner | NOT_PROJECTED_YET | important pre-3B implementation gap |
| temporary Poisoner corruption | R01, R03, R04, R06 | impairment legality/history exists below SDE; same feature family can describe narrative consequence | NOT_PROJECTED_YET | must distinguish lifetime/context from Drunk |
| Red Herring contextual effect | R02, R04, R05 candidate context | setup precommit + policy dimension documented | strategic effect can be evaluated indirectly; contextual feature not separately projected | partial |
| bluff usability / narrative routes | R02 active bluff behavior, R05 player communication | `BluffNarrativeFeatures` exists | NOT_PROJECTED_YET | projector gap |
| relationships/collisions between candidate outputs | multi-clue bundles R01–R04 | `DecisionRelationshipFeatures` exists | NOT_PROJECTED_YET | projector gap |
| future flexibility | evolving worlds / Demon succession | `FutureFlexibilityFeatures` exists | NOT_PROJECTED_YET | projector gap |
| later confirmation must not leak backward | R02 | revision/lifecycle/historical-context architecture exists | first-night exact context is boundary-aware | architecture match |
| same-night state ordering before information | R06 poison → RK death → false RK information | canonical action/observation history exists | current structured production shadow is First-Night-only | later-phase replay gap |
| Demon succession | R02, R04, R06 | canonical history/strategic setup identity architecture exists | outside current first-night structured shadow | later-phase replay gap |
| player claims / table belief | R05 | some public-claim semantics exist elsewhere; not a core SDE-3 feature family | not projected into current structured shadow | optional future context; do not block V1 |

## 5. Critical finding A — typed feature presence is not feature availability

Current `DecisionFeatures` is well-shaped for the evidence.

However, the current projector populates:

- `strategic`;
- optionally `semanticTruth` only when a caller supplies it.

The live `ExactConsequenceDecisionFeaturesProjector` used by the structured shadow calls the projector without supplying semantic truth.

Therefore in the current PR #152 structured shadow:

- `strategic` is projected;
- `semanticTruth` remains unavailable;
- confirmation-chain, healthy-information, truth/credibility, role exposure, impaired narrative, bluff narrative, relationships and future flexibility all remain `NOT_PROJECTED_YET`.

This is acceptable as an incremental SDE-3A contract state.

It becomes unsafe only if SDE-3B policy logic treats `Unavailable` as equivalent to “feature is absent / healthy / zero cost”.

### Required policy guard

SDE-3B should fail closed or explicitly defer a policy dimension whose required feature is unavailable.

Do not convert:

~~~text
FeatureProjection.Unavailable
~~~

into:

~~~text
empty set
zero severity
no problem
~~~

## 6. Critical finding B — committed and player-controlled inputs are typed but not captured in the current shadow

The SDE candidate contract already has:

- `CommittedDecisionInputRef`;
- `PlayerControlledDecisionInputRef`;
- `SdeDecisionInputBindings.Captured`.

This is exactly the right ownership shape.

But the current `StructuredInformationShadowAdapter` deliberately emits:

~~~text
inputBindings = SdeDecisionInputBindings.NotCaptured
~~~

and current tests assert that state.

For the current Chef/Empath numeric proof this is reasonable.

It is insufficient for later evidence shapes where the policy result depends on fixed prior inputs, including:

- Fortune Teller player-chosen pair;
- Poisoner player-chosen target;
- committed Red Herring;
- committed Drunk shown identity;
- earlier delivered information that constrains a persistent perceived world.

### Required boundary

Before an interaction type is allowed to use those contextual dimensions in SDE-3B, its adapter should capture the relevant input refs or prove from the lifecycle contract that none exist.

Do not let `NotCaptured` silently mean “no prior input”.

## 7. Critical finding C — current structured shadow is intentionally First-Night-only

`StructuredInformationProductionShadow.evaluateFirstNight(...)` explicitly limits the production bridge to:

- `FIRST_NIGHT`;
- round 1;
- setup identities before ordinary later-game identity/death changes;
- current first-night semantic timeline replay.

The code itself states broader historical phases belong to later SDE slices.

This is a sound staged boundary.

But R02/R04/R06 demonstrate that several important policy properties are intrinsically longitudinal:

- Drunk continuity;
- later Undertaker/Ravenkeeper confirmation;
- moving Poisoner target;
- same-night poison before death-trigger information;
- Demon succession;
- repeated Fortune Teller sequence.

### Consequence

SDE-3B may reasonably begin as a **first-night provisional policy**, but project documentation and tests should not imply that cross-night impaired narrative or later-phase recommendation replay is already production-shadow-capable.

Longitudinal evidence should be retained now and used when the later historical shadow slice is implemented.

## 8. Critical finding D — Drunk and Poisoner need one shared narrative framework but different lifetime semantics

The current SDE route correctly rejects role-specific coherence hacks and calls for one persistent role-agnostic narrative mechanism.

The evidence supports that architecture, with one refinement:

- Drunk misinformation can define a persistent subjective world across nights;
- Poisoner corruption is temporary, normally bounded to the current poisoned state/night;
- both use the same role semantic proposition domains;
- their **history/lifetime constraints differ**.

A generic impaired-narrative owner should therefore operate over:

~~~text
semantic proposition
+ impairment source/lifetime
+ committed prior observations
+ decision boundary
~~~

rather than one generic boolean `impaired`.

This is a semantic requirement, not a request for Drunk-specific and Poisoner-specific policy classes.

## 9. Critical finding E — real-game evidence strengthens the case for confirmation topology

R02 provides a compact real chain:

~~~text
Drunk Investigator false clue
    → execution
    → Undertaker learns Drunk
~~~

R04 contains:

- Ravenkeeper → Poisoner;
- Undertaker execution information;
- later poisoned Undertaker information;
- repeated Fortune Teller outputs.

The current contract already has `ConfirmationChainFeatures`, but no live projector populates it in the structured shadow.

This dimension should be among the earliest non-strategic projectors because it is repeatedly visible in the real corpus and because raw Evil-topology retention alone cannot express whether two clues mutually authenticate one another.

Do not hard-code named role pairs. Project the generic dependency/support/contradiction relationship from semantic propositions/history.

## 10. Critical finding F — current player-count normalization direction is supported

The first reconstructed set deliberately includes:

- 8-player R02/R05;
- 12-player R01;
- 14-player R04.

Current SDE strategic projection uses ratios and explicit player-count-normalized forced-good/forced-evil fractions rather than raw seat counts alone.

That direction matches the evidence need.

The corpus is **not** large enough to set player-count thresholds or infer that the same ratio should have identical policy severity at every size.

Keep the normalized features; defer numeric gates.

## 11. Critical finding G — player social state is useful evidence but should not block BEGINNER_CONSERVATIVE_V1

R05 preserves public player communication and strategic advice.

This shows that mechanical state is not the complete explanation of table belief.

However:

- social notes are sparse across the corpus;
- ClockTracker does not consistently provide them;
- Storyteller App cannot reliably depend on them as mandatory input.

Recommended boundary:

- preserve claims/table-belief context in Evidence Lab when available;
- allow future optional policy/replay research to consume it;
- do not make social-state reconstruction a mandatory dependency for SDE-3B V1.

## 12. Legacy 90/10 bridge

CampBoardGameHost intentionally retains the approximate impaired-information 90/10 false-family bridge as compatibility code.

The real-game bundle evidence does not support using a fixed false rate as the future SDE policy model.

The new evidence instead shows that impaired output value depends on:

- existing reliable information;
- existing ambiguity mechanisms;
- prior impaired narrative;
- player count / topology;
- confirmation chains;
- future information trajectory.

This is **not** a request to delete the compatibility bridge now.

It should remain clearly legacy and must not become a training label or calibration truth for SDE-3B.

## 13. What the six games can already validate

Without claiming optimality, the current reconstruction set can validate architecture and replay behavior.

### R01

Useful for:

- temporary poison moving between roles;
- simultaneous truthful and false channels;
- repeated Empath trajectory.

### R02

Useful for:

- Drunk false-world continuity;
- later confirmation;
- Red Herring + Fortune Teller;
- Demon transfer;
- bluff context.

### R03

Useful for:

- poisoned Fortune Teller result beside Undertaker confirmation;
- partial-history / UNKNOWN handling.

### R04

Strongest bundle-level case:

- 14 players;
- Drunk continuity;
- Red Herring;
- moving Poisoner;
- Ravenkeeper;
- Undertaker;
- multi-night Fortune Teller trajectory;
- two Demon transfers.

### R05

Useful for:

- mechanical information plus public claim/table-belief context;
- Recluse-adjacent Empath ambiguity;
- source-index conflict handling.

### R06

Useful for:

- same-night state order:
  Poisoner → Ravenkeeper death → impaired Ravenkeeper output;
- next-night Demon succession;
- later-phase historical replay.

## 14. What these games cannot yet calibrate

Do not use these six games to freeze:

- numeric healthy-information floor;
- numeric catastrophic/near-catastrophic thresholds;
- role-function exposure severity;
- exact preference for true vs false impaired information;
- Demon bluff triplet ordering;
- global tradeoff weights.

Most reconstructed ClockTracker Notes record what happened, not explicit Storyteller rationale or rejected alternatives.

They are strong architecture/replay evidence and weaker preference-strength evidence.

## 15. Recommended SDE sequence informed by C0

The current CampBoardGameHost route remains sound, with a concrete evidence-informed implementation order:

~~~text
finish / merge SDE-3A contract checkpoint when separately authorized
    ↓
before consuming a feature in SDE-3B:
    ensure its projector is actually available
    ↓
early non-strategic projection priorities:
    confirmation-chain impact
    healthy-information utility
    semantic truth / impairment context
    impaired-narrative coherence
    contextual Red-Herring relationships
    ↓
capture committed/player-controlled input refs per migrated interaction
    ↓
BEGINNER_CONSERVATIVE_V1
    uses only available typed features
    never treats unavailable as zero
    no unsupported numeric weights
    ↓
SDE-3C DecisionTrace / replay
    ↓
replay reconstructed TB decision prefixes
    ↓
later historical-phase shadow
    supports multi-night trajectories and Demon succession
~~~

## 16. Evidence Lab next action

Do not return to broad game discovery.

The next high-value Evidence Lab work should be one of two targeted activities:

1. **replay-package preparation**:
   normalize R01–R06 into setup commitments + ordered semantic events + decision boundaries that CampBoardGameHost can later consume;

2. **targeted rationale acquisition**:
   search specifically for explicit experienced-Storyteller rationale in the still-unresolved SDE policy dimensions, especially:
   - healthy-information floor;
   - independent cross-night impaired-information believability;
   - role-function exposure;
   - Demon-bluff triplet reasoning.

The whole-game corpus should continue growing only when a new game adds a missing evidence shape or materially improves independent-Storyteller coverage.
