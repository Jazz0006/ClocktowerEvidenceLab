# EL-ML1B-7 — Poisoned Ravenkeeper Whole-Game Prefix Audit — 2026-10-06

> Status: **COMPLETE / NOT PROMOTED / LATER-GAME HISTORICAL CHAIN RETAINED**
>
> Candidate: ClockTracker R06 / Debby / Trouble Brewing / 2025-10-05
>
> Source ID: `66d4356f-fa9f-468d-ba49-6e6858e2e80d`

## 1. Why this case was tested

Unlike FT1-A, WW2 and UT1-A, this candidate already belongs to an existing multi-night whole-game reconstruction.

The retained Night-4 chain is unusually clean:

```text
Poisoner targets Ravenkeeper
    -> Imp kills the poisoned Ravenkeeper
    -> Ravenkeeper death-trigger ability fires
    -> Ravenkeeper chooses the Imp
    -> Storyteller shows Slayer
```

The same source continues into Night 5 and Night 6, so this is a strong later-game/history-sensitive candidate rather than an isolated anecdote.

## 2. Source-backed state already available

`docs/C0_TB_RECONSTRUCTION_BATCH_01_2026-09-23.md` preserves:

- source identity and date;
- Good win result;
- Mayor executed immediately before the Night-4 section;
- Night 4 Poisoner -> Ravenkeeper;
- Night 4 Imp kills Ravenkeeper;
- Ravenkeeper chooses Imp and is shown Slayer;
- later Night-4 Fortune Teller information;
- Night-5 Imp star pass to Spy;
- Night-5 Fortune Teller information;
- Day-5 no execution;
- Night-6 Butler death.

This is enough to prove the local causal impairment chain and the observed Storyteller output.

## 3. Why the historical prefix is still incomplete

The existing reconstruction explicitly records the following as UNKNOWN or not safely recovered:

- Night 1–3 chronology;
- Storyteller identity;
- player count;
- full setup / actual role map;
- Red Herring;
- Demon bluffs;
- Butler Night-4 target;
- full later chronology.

For a Night-4 recommendation benchmark, Night 1–3 is not optional context. Any earlier information, deaths, claims, poison history, executions, or setup commitments may affect why `Slayer` was believable or useful at the moment the poisoned Ravenkeeper chose the Imp.

Therefore the exact state visible to the Storyteller before the `shown Slayer` decision cannot be reconstructed from the current corpus without omission.

## 4. What may be retained safely

The following historical relation remains source-backed:

```text
same-night status chain:
Poisoner -> Ravenkeeper impaired
Imp -> Ravenkeeper dies
Ravenkeeper -> chooses actual Imp
Storyteller -> false output Slayer
```

This is valuable for:

- ordering-sensitive impairment tests;
- later-game misinformation examples;
- verifying that status events must precede information evaluation;
- whole-game acquisition requirements.

It is not yet a canonical `GameState -> Storyteller decision` benchmark example.

## 5. No invented rationale

The retained reconstruction does not recover an explicit Storyteller rationale for choosing Slayer.

Do not infer that Slayer was chosen because:

- it was a Demon bluff;
- it fit a public claim;
- it redirected suspicion;
- it was maximally believable;
- it was better than Mayor or another role.

Those are all plausible possibilities, not source-backed historical facts.

## 6. Disposition

```text
STABLE SOURCE ID
+ WHOLE-GAME PARTIAL RECONSTRUCTION
+ LATER-GAME EVENT CHAIN
+ OBSERVED STORYTELLER OUTPUT
- COMPLETE SETUP
- NIGHT 1–3 HISTORY
- COMPLETE PRE-DECISION STATE
- EXPLICIT RATIONALE
= PARTIAL / NOT CANONICAL_SEED_MATERIALIZED
```

No new READY manifest row is added.

## 7. Acquisition implication

This case is a direct example of why EL-ML1C should prefer structured complete-game timelines rather than only final grimoire + sparse Notes.

A machine acquisition record for later-game benchmark use must preserve at minimum:

- initial seat/role state;
- setup commitments;
- every death/execution transition;
- poisoning/drunkenness state transitions;
- player actions that affect the current decision;
- prior private information;
- current living/dead topology.

Without those fields, a local Night-4 choice remains valuable evidence but not a full-state trajectory sample.

## 8. Next action

Continue whole-game repair with **R02 Drunk-Investigator**, which already retains more setup and role-chain information and therefore has a better chance of crossing the canonical-prefix gate.
