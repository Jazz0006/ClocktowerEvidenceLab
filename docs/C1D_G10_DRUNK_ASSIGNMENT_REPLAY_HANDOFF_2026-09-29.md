# C1D — G10 Game 2 Drunk Assignment Replay Handoff — 2026-09-29

> Status: **COMPLETE — DOWNSTREAM HOST REPLAY ACCEPTED**
>
> Source project: `Jazz0006/ClocktowerEvidenceLab`
>
> Downstream consumer: `Jazz0006/CampBoardGameHost`
>
> Scope: Trouble Brewing Drunk assignment only.

## 1. Purpose

This artifact is the first C1D cross-project replay package.

It exports one stable historical Drunk-assignment decision boundary without exporting Blood on the Clocktower legality or a recommendation verdict.

The downstream contract is:

```text
Evidence Lab historical prefix
    + observed Storyteller choice
    + source-backed rationale
    + provenance
            ↓
CampBoardGameHost
    derive legal Drunk candidates from its own rules/setup owners
    + map the observed historical choice into that legal domain
    + run the current shadow SDE/replay surface
    + compare descriptively without treating the expert choice as policy truth
```

## 2. Selected case

Case: **C1C-G10 Game 2 — The Megavoid**

Primary source:

- YouTube video ID: `G9z25aM9u7s`;
- title: `Storytelling Tips & Tricks - BLOOD ON THE CLOCKTOWER (+ game playthrough!)`;
- playthrough chapter begins at approximately 16:23;
- Drunk assignment occurs at approximately 16:29.

Why this case is used first:

- the complete seat / shown-role layout is evidenced as fixed before the Drunk assignment;
- the observed Drunk choice is explicit;
- the assignment rationale is explicit;
- later setup and night decisions can be cleanly excluded from the prefix;
- the rationale depends on whole-setup topology that CampBoardGameHost can reconstruct from its own canonical state.

This does **not** mean the historical choice is labelled optimal.

## 3. Historical prefix

The internal order in which individual roles were originally selected is UNKNOWN.

The evidence supports treating the already-fixed full seat / shown-role layout as one grouped setup commitment.

Clockwise from the shown Empath seat:

| Seat | Shown role |
| ---: | --- |
| 1 | Empath |
| 2 | Imp |
| 3 | Undertaker |
| 4 | Librarian |
| 5 | Spy |
| 6 | Monk |
| 7 | Mayor |
| 8 | Virgin |
| 9 | Butler |

Historical setup boundary:

```text
setup order 1
    SHOWN_ROLE_LAYOUT
    order basis = EVIDENCED
    complete nine-seat layout above

---------------- decision boundary ----------------

setup order 2
    DRUNK_ASSIGNMENT
    seat 1 / shown Empath -> actual Drunk
```

The assignment result itself is **not** part of the prefix.

## 4. Observed choice

Observed Storyteller choice:

```json
{
  "selected_seat": 1,
  "shown_role": "empath",
  "resulting_actual_role": "drunk"
}
```

Evidence classification:

- Drunk presence: VERIFIED;
- selected shown role: VERIFIED;
- resulting actual role: VERIFIED;
- prefix: `PREFIX_RECONSTRUCTABLE`;
- assignment rationale: `RATIONALE_EXPLICIT`;
- explicitly considered alternatives: none observed;
- explicitly rejected alternatives: none observed.

## 5. Source-backed assignment rationale

At approximately 16:29, the Storyteller explains that the shown Empath is made Drunk because the Empath is sitting next to the Demon.

Normalized evidence meaning:

```text
whole-setup neighbour topology
    -> healthy Empath would interact directly with a Demon neighbour
    -> Storyteller chooses that Empath as the Drunk
```

This is historical rationale, not a downstream feature weight.

Evidence Lab does not translate it into:

- a numeric score;
- a universal preference;
- a hard rejection rule;
- a statement that every Empath next to a Demon should be Drunk.

## 6. Explicit exclusions from the prefix

The following occur after the Drunk assignment and must not be available to the downstream replay as pre-assignment inputs:

- approximately 16:52 — Librarian information involving the Drunk-Empath and Undertaker;
- approximately 17:17 — Demon bluff triplet;
- approximately 17:29 — Drunk Empath receives `0`;
- approximately 18:05 — Drunk Empath later receives a truthful `1` for deceptive narrative effect;
- approximately 18:50 — Spy / Undertaker registration and bluff-continuity interaction;
- later public claims, executions, deaths or outcome information.

These remain useful separate evidence but cannot backfill the assignment rationale or historical prefix.

## 7. Evidence Lab domain projection

The C1A generic contract can represent this case without adding a Drunk-specific schema.

Conceptually:

```text
SetupCommitment(
    setup_order = 1,
    setup_order_basis = EVIDENCED,
    commitment_type = SHOWN_ROLE_LAYOUT,
    value = complete nine-seat shown-role layout
)

DecisionSlice(
    decision_type = DRUNK_ASSIGNMENT,
    historical_prefix_boundary.setup_through_order = 1,
    observed_choice = seat 1 / shown Empath,
    resulting_history = setup order 2 DRUNK_ASSIGNMENT,
    rationale_assertion_ids = source-backed 16:29 rationale assertion
)

SetupCommitment(
    setup_order = 2,
    setup_order_basis = EVIDENCED,
    commitment_type = DRUNK_ASSIGNMENT,
    subject = seat 1,
    value = actual Drunk / shown Empath
)
```

No legal alternatives are exported.

## 8. Downstream replay requirements

CampBoardGameHost should independently confirm all of the following:

1. its Trouble Brewing intermediate setup can represent the nine shown identities with `hasDrunk = true`;
2. its rules-owned `TroubleBrewingDrunkCandidateDomain` derives the legal candidate set without Evidence Lab supplying it;
3. seat 1 / shown Empath is present in that legal candidate set;
4. the DLB-2 hypothetical projector can project the observed historical choice without mutating the intermediate setup;
5. the DLB-3A shadow surface carries the complete Host-derived legal domain into normal SetupPrecommit / DecisionTrace / replay infrastructure;
6. frozen `BEGINNER_CONSERVATIVE_V1` remains Deferred until an evidence-backed DLB-3B consequence projector exists;
7. the historical observed choice is used only as replay evidence, not as a hard-coded production answer.

## 9. C1D success condition

This handoff has crossed the Evidence Lab → CampBoardGameHost boundary successfully.

Accepted downstream Host checkpoint:

- Host PR: #173 — `C1D: replay G10 Drunk assignment evidence`;
- accepted executable head: `87240bb1e3ba6cfe61461905741659d3ba5426ae`;
- Host CI #3532: GREEN;
- Android full unit tests + debug APK assemble: GREEN;
- ASP contract tests: GREEN;
- Real Clingo cross-validation: GREEN;
- R2 #3273: GREEN.

The Host regression independently derived the six legal Townsfolk candidates, mapped the observed seat-1 Empath choice into that domain, carried the case through the existing DLB-3A shadow/DecisionTrace surface, and preserved frozen V1 deferral with no policy selection.

Therefore:

- C1D is COMPLETE;
- C1 can close without a persistence migration;
- additional C1C acquisition remains stopped unless downstream work exposes a concrete missing evidence field;
- DLB-3B may proceed to a score-free setup-level consequence contract using the full three-case replay package and two explicit-rationale cases;
- any production preference/rejection semantics remain a separate evidence/versioning decision.

## 10. Important comparison case for DLB-3B

The second rationale-bearing case, **A Fond Farewell**, must remain visible during DLB-3B design.

Its rationale is different:

```text
shown Chef
    -> choose Chef as Drunk
    -> support a deliberately extreme Chef misinformation narrative
```

Together, G10 and A Fond Farewell show that a setup-level consequence contract cannot be only a neighbour-topology detector.

At minimum, DLB-3B design must preserve room for distinct evidence-backed consequence families such as:

- healthy-information suppression / topology consequence;
- future impaired-information / narrative opportunity.

This handoff does not assign weights between those families.
