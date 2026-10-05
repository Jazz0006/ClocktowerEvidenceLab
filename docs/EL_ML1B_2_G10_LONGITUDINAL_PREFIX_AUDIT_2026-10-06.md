# EL-ML1B-2 — G10 Longitudinal Prefix Extraction Audit — 2026-10-06

> Status: **COMPLETE / 0 OF 3 PROMOTED / 3 PREFIX-BLOCKED**
>
> Scope: the three retained later G10 Game 2 Storyteller decisions at approximately 17:29, 18:05 and 18:50.
>
> Authority: EL-ML1A benchmark audit, the canonical G10 DP-R05/DP-R06 reconstruction, C1C human primary review, and the no-hindsight benchmark contract.

## 1. Purpose

EL-ML1B-2 tests whether one already-canonical game can be extended from setup decisions into a genuine longitudinal Storyteller trajectory.

The promotion gate is stricter than “the observed choice is known”:

```text
shared canonical game/reconstruction
+ source-backed observed decision
+ every historically relevant setup/event fact before that decision
+ source-backed decision boundary
+ no hindsight leakage
= longitudinal canonical seed
```

Unknown omitted events must stay UNKNOWN. A retained timestamp sequence is not sufficient if the repository cannot serialize the intervening game state.

## 2. Shared G10 setup history already canonical

The completed G10 reconstruction establishes:

1. complete nine-seat shown-role layout;
2. ~16:29 Drunk assignment: seat 1 shown Empath -> actual Drunk;
3. ~16:52 Librarian information: seat 1 Drunk-Empath + seat 3 Undertaker;
4. ~17:17 Demon bluffs: Ravenkeeper / Saint / Washerwoman.

DP-R05 and DP-R06 already materialize leak-free prefixes over this shared setup history.

## 3. Candidate audit

### 3.1 ~17:29 — Drunk Empath receives 0

Source-backed facts:

- seat 1 is the actual Drunk shown Empath;
- the preceding setup commitments above are source-backed;
- at approximately 17:29 the Storyteller gives the Drunk Empath `0`;
- no separate choice-specific rationale or explicit alternative is retained.

Blocking gap:

The retained evidence does **not** serialize the complete Night-1 event/action sequence before the 17:29 decision. In particular, it does not establish whether any other player action / private-information event had already occurred and become part of the decision-time state before this Empath output.

The absence of a retained Butler/Spy/other Night-1 event is not evidence that no such event occurred.

Disposition:

**PARTIAL / PREFIX-BLOCKED.**

Do not create DP-R07 yet. The observed `0` remains useful source evidence, but an exact longitudinal prefix cannot be claimed.

### 3.2 ~18:05 — later Drunk Empath receives truthful 1 for deceptive effect

Source-backed facts:

- this is a later Drunk-Empath output in the same game;
- the living-neighbour state has changed;
- the Storyteller deliberately gives `1`;
- the source explicitly says `1` is actually true in that state;
- the stated narrative intent is to redirect suspicion toward the new neighbour.

Blocking gaps:

- exact living/dead seat state at 18:05 is not serialized;
- the intervening Day-1 execution/death history is not retained;
- the immediately preceding player-action / information history is not retained;
- no source-backed same-state `1` versus `0/2` comparison exists.

Disposition:

**PARTIAL / PREFIX-BLOCKED.**

This remains strong rationale evidence but is not a canonical benchmark seed.

### 3.3 ~18:50 — Spy executed after Virgin bluff; Undertaker shown Virgin

Source-backed facts:

- the Spy has publicly claimed Virgin;
- the Spy is executed;
- the Undertaker is shown Virgin rather than Spy;
- the source explicitly demonstrates Spy registration / bluff-continuity behavior.

Blocking gaps:

- the exact public-claim chronology is not serialized;
- the exact nomination/execution/death transition is not serialized as canonical events;
- the 17:29 and 18:05 information events are not yet part of a complete shared event history;
- the complete pre-Undertaker decision state therefore cannot be materialized without omission.

Disposition:

**PARTIAL / PREFIX-BLOCKED.**

The event remains high-value longitudinal evidence, especially for public-narrative continuity, but should not be promoted until the day/night trajectory is reconstructed.

## 4. Result

EL-ML1B-2 does **not** promote any of the three G10 longitudinal candidates.

This is a useful architecture result rather than a failed experiment:

- setup-only canonicalization can be recovered from sparse Storyteller commentary;
- later-game recommendation evidence requires chronological game-state capture, not only isolated Storyteller choices;
- exact living/dead state, public claims, executions, player actions and prior private information become first-class benchmark inputs;
- this directly supports EL-ML1C's shift toward complete-game sources with chronological records plus Storyteller/grimoire visibility.

The six existing READY seeds remain unchanged and authoritative.

## 5. Next action

Proceed to **EL-ML1B-3 — R04 blocker repair**.

R04 is higher leverage than spending more time on G10 because one bounded reconstruction may unlock multiple early- and later-night decisions already identified in the repository.

For G10, do not reopen manual review unless a new source artifact provides the missing chronological state. If new complete-game acquisition becomes necessary later, G10 should be treated as an example of the minimum event-history fidelity required by the acquisition pipeline.
