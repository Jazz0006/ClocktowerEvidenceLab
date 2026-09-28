# C1 — Drunk Assignment Evidence Upgrade

> Status: **C1A + C1B COMPLETE / C1C IN PROGRESS — bounded primary review required**
>
> Date: 2026-09-28
>
> Scope: Trouble Brewing only for the current product stage.

## 1. Why C1 exists

CampBoardGameHost is changing the Drunk workflow.

Previously, the selected Drunk identity was effectively fixed before the recommendation system ran. The evidence consumer could therefore treat “seat X is the Drunk, shown Townsfolk Y” as input.

The new production direction is:

```text
template decides whether a Drunk exists
    ↓
seat / shown-role layout exists
    ↓
Storyteller Decision Engine chooses which shown Townsfolk seat is actually the Drunk
    ↓
later setup / night decisions continue
    ↓
Drunk misinformation is chosen when that shown role acts
```

Evidence Lab must therefore preserve a new research decision: **Drunk assignment**.

This is distinct from the already-studied question of what misinformation a known Drunk should receive.

## 2. Frozen semantic split

C1 treats three concepts separately.

### 2.1 Drunk existence

Historical fact that the setup contains a Drunk.

For the current product route, setup/template logic decides whether the Drunk exists. Evidence Lab records the historical fact when evidenced but does not evaluate that template choice.

### 2.2 Drunk assignment

Storyteller-controlled setup-time choice of which apparent Townsfolk seat is actually the Drunk while continuing to believe they are their shown Townsfolk role.

This is the new algorithm-facing decision.

### 2.3 Drunk misinformation

A later Storyteller-controlled information/output choice for the already-selected Drunk acting as their shown role.

Example:

```text
Decision A
choose Sullivan / shown Empath as the Drunk

later

Decision B
give the Drunk-as-Empath 0 rather than another result
```

Evidence Lab must never collapse A and B into one “Drunk decision.”

## 3. Authority boundary

Evidence Lab records historical evidence and reconstructable decision prefixes.

Evidence Lab does **not** derive the legal Drunk candidate set.

In particular, Evidence Lab must not use Blood on the Clocktower rules to produce an authoritative list such as:

```text
eligible Drunk candidates = seat 2, seat 4, seat 7
```

That enumeration belongs to CampBoardGameHost or another downstream rules consumer.

Evidence Lab may record candidate/alternative seats only when the source itself establishes that the Storyteller considered, compared or rejected them.

Therefore distinguish:

- observed chosen seat;
- explicitly considered alternative;
- explicitly rejected alternative;
- downstream-derived legal alternative.

Only the first three are historical evidence.

## 4. Historical decision prefix

Drunk assignment occurs during setup, before ordinary night information delivery.

C1 therefore requires a first-class historical prefix boundary that can refer to setup commitments as well as ordinary semantic events.

The core invariant is:

> A Drunk-assignment decision prefix must stop immediately before the commitment that records the resulting Drunk assignment.

The selected Drunk cannot already appear as known input to the replay that is supposed to choose the Drunk.

Later setup choices, Red Herring choices, Poisoner actions, delivered information and game outcomes must not leak backward into that prefix unless historically committed before the Drunk choice.

The exact production order remains owned by CampBoardGameHost. Evidence Lab only preserves the historical ordering evidenced for a real game.

## 5. Domain direction

C1 should remain generic and must not introduce a role-specific rules engine.

### 5.1 HistoricalPrefixBoundary

Add a generic boundary concept capable of identifying the latest included setup commitment or semantic event.

The contract should support at least:

- setup-prefix boundary;
- event-prefix boundary.

It must reject ambiguous combinations and future references.

### 5.2 DecisionSlice

Promote the deferred generic DecisionSlice contract because setup-time Drunk assignment now creates a concrete product need.

Conceptual fields:

```text
decision_id
game_id
reconstruction_revision_id
decision_type
controller
historical_prefix_boundary
subject_seat_id
observed_choice
resulting_commitment_id or resulting_event_id
rationale assertion references
explicitly considered alternatives
explicitly rejected alternatives
derivation / verification references
```

Exact field ownership should be settled by C1A tests before persistence work.

`decision_type = DRUNK_ASSIGNMENT` is a semantic label, not a rules implementation.

### 5.3 Resulting state remains history

The resulting fact such as:

```text
Sullivan actual role = Drunk
shown role = Empath
```

belongs in the authoritative reconstructed setup/history.

The DecisionSlice is a derived analytical view that identifies the Storyteller choice and its decision-time prefix.

Do not make DecisionSlice a second authoritative game-history store.

## 6. Evidence-strength dimensions for Drunk assignment

Do not create a decision-quality score.

For collection/replay usefulness, Drunk-assignment evidence may be described by independent reconstruction dimensions such as:

- `RESULT_ONLY` — final Drunk identity is known, but the decision prefix is not reconstructable;
- `PREFIX_PARTIAL` — some pre-assignment context is known;
- `PREFIX_RECONSTRUCTABLE` — material pre-assignment setup context can be reconstructed without hindsight leakage;
- `RATIONALE_EXPLICIT` — the source explicitly states why the selected seat/role was chosen;
- `ALTERNATIVES_EXPLICIT` — the source explicitly establishes considered or rejected alternatives.

These are evidence/replay descriptors only. They do not imply GOOD/BAD Storyteller quality.

## 7. Existing corpus re-audit

Do not restart broad corpus acquisition.

First re-audit existing Trouble Brewing games that contain a Drunk.

### 7.1 E0 — A Stud In Scarlet

Known evidence already establishes:

- Sullivan is the actual Drunk;
- Sullivan is shown Empath;
- the setup frame is recoverable;
- later, Sullivan receives Empath information 0;
- Ben explicitly explains why 2 would be less believable.

C1 interpretation:

- Drunk assignment result: evidenced;
- pre-assignment prefix: candidate for reconstruction;
- assignment rationale: currently UNKNOWN unless additional setup commentary establishes it;
- misinformation rationale: explicit.

Do not use the “2 would be less believable” explanation as evidence for why Sullivan/Empath was selected as the Drunk.

### 7.2 Existing C0 Drunk games

Re-audit R02, R04 and any other existing Drunk-bearing reconstruction for:

- chosen Drunk seat;
- shown Townsfolk identity;
- reconstructable pre-assignment shown-role/seating layout;
- ordering relative to other setup commitments when evidenced;
- explicit assignment rationale;
- explicit considered/rejected alternatives;
- later misinformation and longitudinal continuity.

Do not infer missing rationale from the final setup.

## 8. Targeted acquisition strategy

After the existing-corpus re-audit, collect only where a concrete Drunk-assignment gap remains.

Highest-value sources are:

- expert/trusted Storyteller point-of-view recordings;
- live grimoire/setup construction;
- setup commentary;
- post-game review;
- podcasts/interviews where the Storyteller explains a specific real setup;
- paired structured record + primary recording.

A ClockTracker final grimoire that only identifies the Drunk remains useful, but is normally result-only or prefix-partial evidence.

The immediate target is small:

- at least 3 Drunk-assignment cases with reconstructable decision prefixes;
- seek 1–2 cases with explicit assignment rationale if available;
- preserve multiple independent Storytellers when practical.

Do not resume broad 20–30 game quota collection merely for C1.

## 9. Screening additions

When a game contains a Drunk, screening should answer when evidence permits:

- Is Drunk presence known?
- Is the chosen Drunk seat known?
- Is the shown Townsfolk identity known?
- Is the broader shown-role/seating layout known?
- Is the Drunk assignment demonstrably Storyteller-controlled in this source?
- Can the historical boundary immediately before assignment be reconstructed?
- Which setup commitments are evidenced as already committed at that boundary?
- Is assignment rationale explicit?
- Are considered alternatives explicit?
- Are rejected alternatives explicit?
- Is later Drunk information recoverable?
- Is multi-night Drunk continuity recoverable?

UNKNOWN is valid for every unsupported item.

## 10. CampBoardGameHost handoff

The intended handoff for one Drunk-assignment case is:

```text
Evidence Lab
    historical pre-assignment prefix
    + observed expert choice
    + provenance
    + rationale / explicit alternatives when observed
            ↓
CampBoardGameHost
    derive legal Drunk candidates
    + run production Drunk-selection SDE
    + compare recommendation with observed historical choice
```

A second downstream replay may then evaluate misinformation after the Drunk has been selected.

Evidence Lab must not score whether the observed choice or production recommendation is better.

## 11. Implementation route

### C1A — Generic domain contract — COMPLETE

C1A was completed tests-first on 2026-09-28.

Implemented generic domain contracts:

- `HistoricalPrefixBoundary` with mutually exclusive setup/event prefixes;
- `DecisionResultLink` linking a derived decision to exactly one authoritative `SetupCommitment` or `SemanticEvent`;
- generic `DecisionSlice` with game/revision identity, decision type, controller, observed choice, resulting-history link, optional source-backed rationale, and optional explicitly considered/rejected alternatives;
- `ExplicitAlternative` carrying evidence-assertion references rather than downstream legal alternatives;
- `materialize_historical_prefix(...)`, which validates game/revision identity, deterministic ordering and result linkage before projecting only the committed historical prefix.

Tests-first evidence:

- RED contract commit: `8ec9a22770eab30b428b5a9a97b302ab20aa6ec1`;
- formatting-only correction: `8c80d80d997a89852c22eb77a350e86af6fb16aa`;
- meaningful RED: quality run #120 reached pytest and failed with `ModuleNotFoundError` for the not-yet-implemented `domain.decision`;
- GREEN implementation: `a44b6b16cd46939b8aef3db5dffb8e1d02b5c94e`;
- exact-audit cleanup: `01ef9d3f3df09581776d9ab6b052d0f1a64b318f`;
- final implementation gate: quality run #122 PASS, including Ruff check, Ruff format and 65 pytest tests.

C1A did **not** add persistence, Alembic changes, Drunk-specific legality/policy logic, or Evidence-Lab-derived legal alternatives.

C1B has not started. Stop after this checkpoint until the project owner chooses the next step.

C1A implementation contract:

Add the minimum generic contracts required for:

- setup-time HistoricalPrefixBoundary;
- DecisionSlice;
- linkage from an observed choice to its resulting SetupCommitment/SemanticEvent;
- rationale and explicit alternatives without legal-alternative enumeration.

Mandatory invariants include:

1. a Drunk-assignment prefix cannot contain its own resulting assignment;
2. later setup/event history cannot leak into an earlier decision prefix;
3. explicit observed alternatives remain distinct from downstream-derived legal alternatives;
4. UNKNOWN rationale/alternatives round-trip without guessing.

Do not add persistence in C1A.

### C1B — Existing corpus projection — COMPLETE

C1B re-audited four existing Drunk-bearing cases:

- E0 `A Stud In Scarlet`;
- R02;
- R03;
- R04.

Detailed audit:

- `docs/C1B_EXISTING_DRUNK_ASSIGNMENT_REAUDIT_2026-09-28.md`.

Result:

- 4 cases contain some Drunk-assignment result evidence;
- only E0 currently establishes both selected participant/visible seat and shown Townsfolk role;
- 0 existing cases have an evidence-backed `PREFIX_RECONSTRUCTABLE` assignment boundary;
- 0 existing cases contain explicit assignment rationale;
- 0 contain explicit considered/rejected assignment alternatives;
- therefore 0 setup-time Drunk-assignment DecisionSlices are promoted under the stricter C1A contract.

C1B also exposed and corrected a generic chronology hazard: deterministic setup ordering is not automatically historical commitment order. `SetupOrderBasis.EVIDENCED` is now required for setup-time prefix materialization; `CANONICAL_ONLY` remains valid only for deterministic reconstruction ordering.

This is a successful schema/evidence pressure test, not a reason to guess missing history.

C1C has not started.

### C1C — Targeted acquisition — IN PROGRESS

The first targeted search pass is complete and has deliberately stopped broad discovery.

Authority:

- `docs/C1C_TARGETED_DRUNK_ASSIGNMENT_ACQUISITION_2026-09-28.md`.

Current bounded queue:

1. E0 `A Stud In Scarlet` setup conversation around the already-known 09:49 Drunk / 10:32 Red Herring region;
2. `Live and Imp-Person` setup section — Brooke = Drunk shown Undertaker is already a strong result/layout lead;
3. bounded verification of the Steven Medway Drunk podcast assignment section as general guidance, not a replay case;
4. official 2019 Trouble Brewing Game 2 (Steven Medway) and Game 1 (Jon Gjengset) only if the first two historical candidates do not close enough of the replay gap.

New guidance evidence supports the architectural direction that the apparent Townsfolk setup may exist before choosing which Townsfolk becomes the Drunk, and that assignment may depend on player/seat context. This is guidance evidence only; it does not backfill historical prefixes.

Current C1C quota state:

- replayable Drunk-assignment cases: **1 / target 3**;
- first replayable case: E0 `A Stud In Scarlet` — complete role layout verified before Sullivan is selected as Drunk, with Red Herring selected later;
- explicit historical assignment-rationale cases: **0 / seek 1–2**.

E0's assignment rationale and alternatives correctly remain UNKNOWN.

C1C therefore remains `IN PROGRESS`. The next bounded target is `Live and Imp-Person`.

Do not enter C1D until the replay package is sufficiently stable for downstream handoff.

### C1D — CampBoardGameHost replay handoff

Export one stable Drunk-assignment case and confirm the downstream project can:

- derive its legal alternatives itself;
- reconstruct the intended decision prefix;
- run the current Drunk-selection algorithm;
- compare without Evidence Lab owning the verdict.

### C1E — Persistence only if justified

Only after C1A–D stabilise the semantics, decide whether to persist/export:

- Game / GameSeat / ReconstructionRevision;
- SourceGameLink;
- SetupCommitment;
- SemanticEvent;
- HistoricalPrefixBoundary;
- DecisionSlice.

Do not create an Alembic migration merely because C1 introduced a new concept.

## 12. C1 completion gate

C1 is complete when:

- setup-time DecisionSlice is represented by a stable generic domain contract;
- Drunk assignment and Drunk misinformation are structurally separate;
- setup-time prefix boundaries prevent hindsight leakage;
- Evidence Lab does not enumerate legal Drunk candidates;
- existing Drunk corpus has received the targeted re-audit;
- at least 3 replayable Drunk-assignment cases exist;
- explicit-rationale cases have been captured when available;
- at least one case crosses the Evidence Lab → CampBoardGameHost replay boundary;
- roadmap, handoff, collection and provenance documentation remain synchronized.

Persistence expansion is not itself a C1 completion requirement.
