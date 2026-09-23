# C0 Trouble Brewing Cross-Game Algorithm Findings — 2026-09-23

## 1. Purpose

This document synthesizes the first reconstructed Trouble Brewing whole games into **evidence-backed hypotheses** for later Storyteller recommendation calibration.

It does not label any Storyteller decision GOOD/BAD and does not modify CampBoardGameHost policy.

Current reconstruction inputs:

- R01 — Ash / @CryptCore — 12 players;
- R02 — Jeff / @CryptCore + @Larrikin — 8 players;
- R03 — Scott / @sancho — 2025-09-24 — partial;
- R04 — Scott / @sancho — 2025-09-10 — 14 players.

Authoritative event detail remains in `docs/C0_TB_RECONSTRUCTION_BATCH_01_2026-09-23.md`.

## 2. Finding F1 — misinformation must be evaluated as a bundle

Observed across R01, R02 and R04:

- an impaired information role is never the only source of uncertainty;
- truthful information channels operate in parallel;
- Red Herring, Spy/Recluse registration and bluffs can create ambiguity without requiring arbitrary false information;
- later deaths and confirmation roles change how earlier information is interpreted.

Hypothesis:

> Recommendation quality should depend on the marginal effect of a candidate output on the **current whole information bundle**, not on whether that output is locally plausible in isolation.

This directly supports the project's topology/world-space direction and argues against role-local heuristics such as “a poisoned information role should usually receive false information” without considering the rest of the table.

## 3. Finding F2 — Drunk and Poisoner are not one generic unreliability mechanism

### Drunk pattern

R02:

- the Drunk believes they are Investigator;
- Night 1 creates a false Scarlet Woman world;
- the player is executed;
- Night 2 Undertaker learns Drunk.

R04:

- Hylinn is the Drunk;
- receives 0 repeatedly across nights.

The Drunk case is longitudinal. The information stream creates a persistent subjective world that may later be confirmed, challenged or reinterpreted.

### Poisoner pattern

R01 and R04 show poison moving between roles across nights:

- first-night information role;
- Slayer;
- Monk;
- Undertaker;
- other targets.

Poison is temporary and target-specific. A poisoned output sits inside a table containing other contemporaneous information that remains reliable.

Hypothesis:

> Downstream policy should model **persistent false-world continuity** for Drunk separately from **temporary per-night corruption** for Poisoner.

A single `unreliable=true` dimension is not enough for calibration.

## 4. Finding F3 — existing structural ambiguity changes the marginal value of another false clue

R02 and R04 contain Red Herring plus other misinformation mechanisms.

R04 in particular contains:

- Drunk information;
- Red Herring;
- Poisoner;
- Spy-related information;
- truthful Ravenkeeper/Undertaker information;
- repeated Fortune Teller information.

The table therefore already has multiple ambiguity sources before the Storyteller chooses a particular impaired output.

Hypothesis:

> The recommendation engine should account for an **existing ambiguity / misinformation budget** before choosing another discretionary false output.

This is not yet a numeric scoring rule. The evidence supports the dependency, not a threshold.

## 5. Finding F4 — later confirmation chains must not leak backward

R02 gives the clearest example:

~~~text
Night 1
Drunk shown Investigator receives false minion information

Day 1
the claimant is executed

Night 2
Undertaker learns Drunk
~~~

The Night-2 event materially changes how the table can interpret the Night-1 information, but it did not exist at the Night-1 decision boundary.

Hypothesis:

> Every recommendation comparison needs an explicit committed-prefix boundary. Later confirmation may be used to study consequences, but not as input to the earlier recommendation state.

This is now supported by real whole-game evidence rather than only architectural reasoning.

## 6. Finding F5 — repeated information is a trajectory, not a bag of independent results

R04 Fortune Teller sequence:

~~~text
N1 NO
N2 YES
N3 YES
N4 YES
N5 NO
N6 YES
~~~

The meaning of each result depends on:

- previous targets/results;
- Red Herring;
- deaths;
- Demon succession;
- which players remain plausible;
- accumulated public claims, where known.

R04 Drunk information also repeats rather than being independently regenerated each night.

Hypothesis:

> Multi-night information roles require trajectory-level evaluation. A new result should be scored against the worlds induced by prior outputs, not generated independently each night.

This strongly supports the already-planned persistent Drunk cognitive-world work.

## 7. Finding F6 — Demon succession must preserve history without freezing the current world

R02 and R04 both contain Imp self-kill / Demon transfer.

R04 contains two transfers:

~~~text
Paul
  → Hollie
  → Deonna
~~~

Older information remains part of player reasoning even as the active Demon changes.

Hypothesis:

> Reconstruction and policy evaluation require time-indexed role/state transitions. Historical facts must remain stable while current-world ownership changes.

Do not overwrite a player's historical role/state in place and then evaluate earlier information against the mutated current state.

## 8. Finding F7 — confirmation roles are part of information topology

Undertaker and Ravenkeeper are not merely extra independent clues.

Examples:

- R02 Ravenkeeper identifies Undertaker, then Undertaker identifies Drunk;
- R04 Ravenkeeper identifies Poisoner;
- R04 Undertaker produces a normal result, then later receives information while poisoned.

These form chains of support or contradiction between claims.

Hypothesis:

> The engine should eventually represent **information dependency/confirmation topology**, not merely count the number of clues pointing at each alignment.

This may be approximated initially by world-space effects rather than an explicit graph, but the evidence shows the dependency exists.

## 9. Finding F8 — player count likely changes information pressure, but current evidence is not enough for numeric calibration

The first batch includes:

- 8 players — R02;
- 12 players — R01;
- 14 players — R04.

A clue eliminating or strongly implicating two players has different proportional impact at these sizes.

However, three strong games are not enough to derive numeric player-count coefficients.

Current conclusion:

- preserve player count as a first-class calibration dimension;
- do not fit thresholds from this batch;
- continue comparing normalized world-space / candidate-space impact rather than raw clue counts.

## 10. What the evidence does **not** establish

The current batch does not establish:

- that the observed Storyteller choices are optimal;
- why the Storytellers made each choice;
- a universal target evil win rate;
- numeric weights for misinformation;
- a required amount of false information per game;
- a direct causal relationship between any one clue and the final winner.

Outcome remains context, not a quality label.

## 11. Domain-model pressure exposed by reconstruction

The first reconstruction batch confirms several concepts are required before a durable whole-game corpus can be persisted cleanly.

### 11.1 Blocking gap — Source record to logical Game linkage

ClockTracker can contain multiple UUID Source records for one real game.

The domain therefore needs an explicit relationship such as:

~~~text
Source
  ↕
SourceGameLink
  ↕
Game
~~~

Requirements:

- many Sources may support one logical Game;
- one Source must not silently create a second Game;
- matching status must distinguish candidate / verified same / verified different / unresolved;
- the link itself may need provenance or reviewer verification.

This is now a blocking gap for E1-7 persistence because reconstruction already uses duplicate source records.

### 11.2 Blocking gap — ordered SemanticEvent / information delivery representation

Whole-game reconstruction repeatedly requires events such as:

- poison target chosen;
- protection chosen;
- Demon kill;
- execution/death;
- shown-role/setup commitment;
- information targets;
- delivered information;
- role/alignment transition.

Free-form assertions alone are not sufficient as the canonical historical timeline.

This confirms the planned `SemanticEvent` layer is required before importing these games.

### 11.3 Blocking gap — SetupCommitment

Red Herring, Drunk shown identity, Demon bluffs and similar setup-time commitments materially affect later interpretation.

These need historical committed-prefix identity separate from ordinary night events.

This confirms the planned `SetupCommitment` concept.

### 11.4 Required event fields / semantics

The reconstruction pressure implies at least:

- game/revision identity;
- semantic event identity;
- phase/day-night label;
- deterministic order within the reconstruction;
- event type;
- actor/subject seat when known;
- target seat(s) when known;
- delivered value/result when present;
- impairment/modifier context when directly evidenced;
- provenance through EvidenceAssertions/Fragments;
- explicit UNKNOWN for missing fields.

Do not encode Trouble-Brewing-specific role branches into the generic persistence layer. Role-specific payloads should remain typed data interpreted downstream.

## 12. C0 engineering conclusion

C0 has now done more than prove source availability.

It has demonstrated that:

1. ClockTracker can yield whole-game Trouble Brewing bundles rich enough for algorithm research;
2. those bundles expose repeated longitudinal dependencies that isolated decision examples miss;
3. the current E1 reconstruction identity layer is not yet sufficient to persist the discovered evidence cleanly;
4. Source→logical-Game matching and ordered semantic history are blocking concepts before the deferred E1-7 persistence work should resume.

Recommended immediate sequence:

~~~text
C0 reconstructed games
    ↓
freeze minimal SourceGameLink + SetupCommitment + SemanticEvent contract
    ↓
tests-first domain implementation
    ↓
persist reconstruction identity + ordered game history
    ↓
import first verified TB games
    ↓
compare real bundles with Storyteller App recommendation output
~~~

Do not add policy scoring to Evidence Lab.
