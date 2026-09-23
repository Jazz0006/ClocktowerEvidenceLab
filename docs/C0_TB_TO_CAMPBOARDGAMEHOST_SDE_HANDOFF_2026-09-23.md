# C0 Trouble Brewing → CampBoardGameHost SDE Handoff — 2026-09-23

## 1. Purpose

Provide a narrow cross-project handoff from ClocktowerEvidenceLab to the live Storyteller Decision Engine work in `Jazz0006/CampBoardGameHost`.

This document is informational.

It does not authorize changes in CampBoardGameHost and does not turn observed human Storyteller choices into policy truth.

## 2. Live SDE state at handoff

Re-query before acting in a later conversation.

At this checkpoint:

- PR #151 — SDE-3A engine/feature/policy contract: MERGED;
- PR #152 — structured feature projection shadow: MERGED;
- CampBoardGameHost `main`: `2a9051f1b0282bd25d01d46d36fe797857cc429d`;
- PR #153 — `SDE-3B: implement BEGINNER_CONSERVATIVE_V1 policy`:
  - OPEN;
  - DRAFT;
  - branch `sde-3b-beginner-conservative-v1`;
  - observed head `0ae46279d5c179f6a44ed6e4c814b6f614a0057f`.

Do not assume these refs remain current.

## 3. Evidence Lab artifacts to read

Primary:

1. `docs/C0_TB_RECONSTRUCTION_BATCH_01_2026-09-23.md`
2. `docs/C0_TB_CROSS_GAME_ALGORITHM_FINDINGS_2026-09-23.md`
3. `docs/C0_TB_STORYTELLER_APP_ALGORITHM_GAP_AUDIT_2026-09-23.md`
4. `docs/C0_TB_TARGETED_RATIONALE_SEARCH_2026-09-23.md`
5. `docs/C0_TB_R04_REPLAY_PREPARATION_2026-09-23.md`

Supporting acquisition log:

- `docs/C0_TROUBLE_BREWING_ACQUISITION_SPRINT_2026-09-23.md`

## 4. Evidence set now available

Six representative Trouble Brewing reconstructions:

| Case | Size | Main evidence shape |
| --- | ---: | --- |
| R01 Ash/@CryptCore | 12 | moving Poisoner + repeated Empath + parallel truthful/false channels |
| R02 Jeff/@CryptCore+@Larrikin | 8 | Drunk false world → Undertaker confirmation + Red Herring + Imp→Spy |
| R03 Scott 2025-09-24 | partial | poisoned FT output + Undertaker chain + UNKNOWN gaps |
| R04 Scott/@sancho 2025-09-10 | 14 | Drunk continuity + RH + moving poison + RK/UT + long FT trajectory + two Demon transfers |
| R05 Leo | 8 partial | mechanical info + public claims/table-belief context |
| R06 Debby | partial | poison → RK death → false RK info + later Imp→Spy |

These games validate evidence shapes and lifecycle dependencies.

They do **not** establish optimal policy or numeric weights.

## 5. SDE-3B compatibility audit

The current PR #153 policy direction is compatible with the evidence.

### 5.1 Correct: unavailable dimensions remain explicit

Current V1 policy:

- defers when strategic projection itself is unavailable;
- records `PREFERENCE_DIMENSIONS_NOT_PROJECTED` when non-strategic preference dimensions are unavailable;
- does not interpret missing features as zero/healthy/neutral.

Evidence Lab recommendation:

- KEEP.

This is required by R01–R06 because confirmation, impairment narrative, semantic truth and future flexibility are not yet fully projected.

### 5.2 Correct: no invented numeric thresholds

Current V1:

- rejects only exact defined zero retained credible Evil structure;
- keeps every non-zero candidate alive in an explicit survivor equivalence band;
- does not use fixed healthy-information thresholds, raw player-count cutoffs or weighted scores.

Evidence Lab recommendation:

- KEEP.

The six games support qualitative dependencies but are not sufficient to fit numeric policy gates.

### 5.3 Correct: survivor selection remains weight-free

Current selector chooses deterministically among SURVIVOR candidates using stable seeded hashing.

Evidence Lab recommendation:

- ACCEPT as a provisional tie-break seam.

Do not reinterpret the selected survivor as evidence that the policy prefers it on an unprojected dimension.

## 6. Highest-value next feature projectors

The evidence suggests the following order once V1 core contract is stable.

This is an engineering-priority suggestion, **not** a political-style ranking or game-quality score.

### Confirmation-chain impact

Strong support:

- R02: Drunk Investigator claim → execution → Undertaker learns Drunk;
- R04: Ravenkeeper → Poisoner; Undertaker confirmation chain; FT sequence;
- independent expert guidance from Beardy explicitly discusses Ravenkeeper confirmation chains and game-stage-dependent Spy reveal/misregistration.

Needed semantics:

- support / contradiction between observations;
- whether one new observation authenticates a role/claim;
- whether it collapses a major ambiguity route.

Do not hard-code Ravenkeeper+Undertaker role pairs.

### Semantic truth + impairment binding

Strong support:

- R01 poisoned Washerwoman;
- R03 poisoned Fortune Teller;
- R04 Drunk + multiple poisoned roles;
- R06 poisoned Ravenkeeper.

Important ownership rule already identified in PR #153:

- `ObservationReliability.RECEIVED_AS_FUNCTIONING` is not proof that the ability was functioning;
- current impairment must come from the canonical rules/session owner.

Needed projection input:

~~~text
candidate proposition
+ authoritative current ability-state / impairment binding
+ committed historical observations
~~~

### Impaired-narrative coherence

Strong support:

- R02 Drunk false world later confirmed as Drunk;
- R04 repeated Drunk result across nights;
- R06 temporary poison causes one false death-trigger result.

Required distinction:

- Drunk: persistent subjective-world pressure;
- Poisoner: temporary impairment lifetime;
- same generic narrative owner;
- no Drunk-specific / Poisoner-specific policy hacks.

### Healthy-information utility

Evidence motivation:

- R01/R04 show false channels alongside several independent truthful channels;
- the marginal value of another false output depends on what healthy information remains.

Do not implement a numeric “misinformation budget” yet.

### Contextual role-function exposure

Evidence motivation:

- Ravenkeeper/Spy expert guidance says direct reveal vs bluff-role display can change with game stage;
- therefore exposure severity is contextual, not a universal reject.

Still missing:

- a replayable expert game with explicit considered/rejected alternatives.

## 7. Cross-night replay boundary

Current structured production shadow is First-Night-only.

This is acceptable for the current SDE-3B slice.

Do not claim that V1 currently covers:

- cross-night Drunk continuity;
- later Undertaker/Ravenkeeper confirmation;
- moving Poisoner targets;
- same-night later-phase impairment ordering;
- Demon succession;
- repeated FT trajectories.

R04 and R06 should become later historical-shadow regression cases.

## 8. Input-binding boundary

The current typed SDE contract already has:

- committed decision input refs;
- player-controlled decision input refs.

The current structured adapter still has paths where input bindings are not captured.

Before policy consumes contextual features for an interaction, bind the applicable historical inputs, for example:

- Fortune Teller selected pair;
- Poisoner target;
- Red Herring commitment;
- Drunk shown identity;
- prior delivered observations relevant to narrative continuity.

`NotCaptured` must mean “adapter has not bound the inputs”, not “there were no inputs”.

## 9. R04 replay package status

R04 is the strongest whole-game evidence case, but currently:

- `REPLAY_PREP_PARTIAL / BLOCKED_ON_DIRECT_GRIMOIRE`.

The chronological event package is prepared.

Remaining blockers:

1. verified clockwise seat order;
2. full actual-role map from direct grimoire;
3. Hylinn shown role;
4. Brian exact actual/shown role;
5. direct bluff-triplet confirmation.

Current tools cannot access the direct ClockTracker grimoire/API/mirror payload.

Do not guess these fields.

## 10. Expert rationale enrichment

New independent qualitative support:

- Beardy / Clocktower Academy Ravenkeeper TB episode;
- classification: `EXPERT_GUIDANCE_WITH_GAME_EXAMPLES`;
- explicit policy signal: Spy reveal/misregistration choice is game-state/lifecycle dependent;
- explicit confirmation-chain importance;
- impaired Ravenkeeper information can swing the information topology strongly.

This supports implementing the feature dimensions.

It does not justify numeric weights.

No new qualified Trouble Brewing ClockTracker whole-game record with explicit Storyteller rationale was found in the dedicated rationale search.

Practical source split:

~~~text
ClockTracker
    -> mechanical whole-game backbone

expert commentary / postgame
    -> rationale enrichment
~~~

## 11. What not to import as policy truth

Do not convert any of the following into SDE weights or labels:

- Evil/Good final result;
- frequency of true vs false impaired outputs in six games;
- one Storyteller's observed silent choice;
- first-time/community Storyteller advice;
- the legacy 90/10 impaired-information compatibility bridge;
- search-index missing fields.

## 12. Concrete use of Evidence Lab during PR #153

PR #153 can continue its conservative V1 contract without waiting for more Evidence Lab collection.

Evidence Lab should be used to constrain claims:

- V1 may use only projected features;
- missing preferences remain limitations;
- no unsupported soft ordering;
- no cross-night capability claim until a later historical shadow exists.

When the next non-strategic projector is implemented, use the matching R-case as a semantic regression target.

## 13. Next Evidence Lab work

The broad acquisition phase is over.

Continue only along two narrow tracks:

1. **replay readiness**
   - close direct-grimoire blockers if a new access path becomes available;
   - prepare smaller replay prefixes where setup is fully recoverable;

2. **targeted rationale**
   - seek explicit qualified Storyteller reasoning for:
     - healthy-information floor;
     - persistent impaired narrative;
     - role-function exposure;
     - Demon bluff triplet choice.

Do not expand raw corpus count merely to increase N.
