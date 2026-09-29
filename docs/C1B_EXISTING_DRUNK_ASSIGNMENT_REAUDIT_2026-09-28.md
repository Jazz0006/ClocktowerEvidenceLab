# C1B — Existing Drunk Assignment Corpus Re-audit

> Status: **COMPLETE — C1C NOT STARTED**
>
> Date: 2026-09-28
>
> Scope: existing Trouble Brewing evidence only. No new-source acquisition was performed.

## 1. Purpose

C1B pressure-tests the C1A generic setup-time decision contract against existing Drunk-bearing reconstructions.

The goal is not to promote weak evidence into replay-ready DecisionSlices. The goal is to answer, for each existing case:

- which participant/seat was selected as the Drunk, when established;
- which Townsfolk role they were shown, when established;
- whether the historical setup prefix immediately before assignment is reconstructable;
- whether assignment rationale or alternatives are explicitly sourced;
- which later misinformation belongs to a separate decision;
- whether the case can honestly instantiate the C1A `DecisionSlice` without hindsight leakage.

The source authority for this audit is existing Evidence Lab reconstruction material. No BotC legality or candidate enumeration is imported.

## 2. C1B domain correction exposed by the corpus

The existing corpus confirms a distinction that was already visible in the E0 notebook:

> a deterministic setup ordering used by a reconstruction is not necessarily evidence of the historical order in which setup commitments were actually made.

This matters because C1A setup-time prefix materialization uses setup order to determine which commitments existed before a choice.

Without an explicit distinction, a canonical reconstruction order could be mistaken for historical chronology.

C1B therefore adds the generic `SetupOrderBasis` contract:

- `EVIDENCED` — the setup order is supported strongly enough to be used as a historical setup-time prefix;
- `CANONICAL_ONLY` — the order is deterministic for reconstruction/serialization, but does not claim historical commitment chronology.

`SetupCommitment.setup_order_basis` defaults to `CANONICAL_ONLY`.

A setup-time `HistoricalPrefixBoundary` may be materialized only when the supplied setup history uses `EVIDENCED` ordering.

An event-time decision may still include the complete setup history when setup internal order is `CANONICAL_ONLY`, because by then setup as a whole is already committed and the internal ordering is not being used to decide prefix membership.

Tests-first evidence:

- RED: `058be4254f60cf34330c2fe08d22d185e493c447`;
- quality run #125 reached pytest and failed because `SetupOrderBasis` did not yet exist;
- generic history contract: `2b63cb781b0804b8744e2c56322ac29f539c2c6b`;
- setup-prefix guard: `d4aae665ebf291e3247df131183848130ffe2dba`;
- formatting-only follow-ups: `5adc2e191ef58ba2322d10083d17f372b6e8c9fc`, `03a52a15c5f6f3ad3bfbc2fae574e5ee2603b255`;
- quality run #129: PASS.

No persistence or Alembic change was introduced.

## 3. Projection summary

Replay-value descriptors are evidence-completeness descriptors only:

- `RESULT_ONLY`;
- `PREFIX_PARTIAL`;
- `PREFIX_RECONSTRUCTABLE`;
- `RATIONALE_EXPLICIT`;
- `ALTERNATIVES_EXPLICIT`.

| Case | Selected Drunk identity | Shown Townsfolk | Pre-assignment prefix | Assignment rationale | Explicit alternatives | C1A DecisionSlice now? |
| --- | --- | --- | --- | --- | --- | --- |
| E0 — A Stud In Scarlet | Sullivan; visible setup seat 9 | Empath | PARTIAL; setup internal order explicitly UNKNOWN | UNKNOWN | UNKNOWN | **NO** |
| R02 — Jeff / @CryptCore + @Larrikin | exact participant/seat not normalized in current reconstruction | Investigator | not reconstructable from current material | UNKNOWN | UNKNOWN | **NO** |
| R03 — Scott / @sancho 2025-09-24 | Chris | exact shown role UNKNOWN | not reconstructable from current material | UNKNOWN | UNKNOWN | **NO** |
| R04 — Scott / @sancho 2025-09-10 | Hylinn | UNKNOWN | PARTIAL; several setup facts known, historical assignment order not evidenced | UNKNOWN | UNKNOWN | **NO** |

Current C1B result:

- existing Drunk-bearing cases re-audited: **4**;
- cases with some assignment-result evidence: **4**;
- cases with both selected participant and shown Townsfolk established: **1** (E0);
- `PREFIX_RECONSTRUCTABLE` assignment cases: **0**;
- explicit assignment-rationale cases: **0**;
- explicit considered/rejected assignment alternatives: **0**;
- replay-ready C1A Drunk-assignment DecisionSlices: **0**.

This is an evidence result, not a domain failure.

The C1A contract should reject or withhold a DecisionSlice rather than fabricate a historical prefix.

## 4. E0 — A Stud In Scarlet

Authority:

- `docs/E0_A_STUD_IN_SCARLET_EVIDENCE_CONTRACT_PILOT.md`;
- `docs/E0_A_STUD_IN_SCARLET_PRIMARY_REVIEW_PACKET.md`.

### 4.1 Assignment result evidence

Primary-reviewed evidence establishes:

- Sullivan is the actual Drunk;
- Sullivan is shown/believes Empath;
- the visible setup frame places Sullivan at seat 9;
- the broader visible seating/role layout and Demon bluffs are recoverable.

For C1 purposes, the historical result is therefore strong:

~~~text
selected participant = Sullivan / visible setup seat 9
actual role = Drunk
shown role = Empath
~~~

### 4.2 Prefix status

The E0 notebook explicitly states that the exact historical order among setup commitments is UNKNOWN.

The source can establish multiple facts as pre-Night-1 commitments, but source presentation timestamps such as 09:49 and 10:32 are not historical setup timestamps.

Therefore:

- descriptor: `PREFIX_PARTIAL`;
- `SetupCommitment.setup_order_basis`: `CANONICAL_ONLY` unless new evidence establishes chronology;
- assignment-time `HistoricalPrefixBoundary`: not currently admissible;
- generic C1A `DecisionSlice`: not materialized.

### 4.3 Historical E0 DecisionSlice terminology

The pre-C1 E0 notebook admitted `DS-ASIS-001 — Drunk shown identity = Empath` under the earlier conceptual DecisionSlice vocabulary.

C1B must not silently reinterpret that older slice as a fully replayable **Drunk assignment** DecisionSlice.

It remains valid historical/result evidence that Sullivan is Drunk and shown Empath.

Under the stricter C1A contract, the assignment decision itself still lacks a reconstructable pre-assignment historical prefix.

### 4.4 Assignment rationale vs misinformation rationale

Assignment rationale remains `UNKNOWN`.

Later, at 12:41, Ben gives Sullivan-as-Empath the information `0` and explicitly explains that `2` would be less believable.

That evidence belongs to the **Drunk misinformation** decision.

It is not evidence for why Sullivan/Empath was selected as the Drunk.

C1B therefore preserves:

~~~text
assignment:
    Sullivan / Empath
    rationale = UNKNOWN
    alternatives = UNKNOWN

later misinformation:
    0
    rationale = explicit
    rejected alternative = 2
~~~

## 5. R02 — Jeff / @CryptCore + @Larrikin — 2025-09-30

Authority:

- `docs/C0_TB_RECONSTRUCTION_BATCH_01_2026-09-23.md`.

### 5.1 Assignment result evidence

The current reconstruction establishes:

- the Drunk believes they are the Investigator;
- on Night 1 they receive a false Scarlet Woman clue between the Empath and Fortune Teller;
- the Investigator claimant / Drunk is executed on Day 1.

However the current normalized reconstruction does not identify the exact participant/seat for the Drunk assignment.

The full seating / role table is also not transcribed.

Therefore the current assignment-result evidence is only partial:

~~~text
selected seat = UNKNOWN
shown role = Investigator
actual role = Drunk
~~~

Descriptor: `RESULT_ONLY`.

### 5.2 Prefix status

No reliable pre-assignment setup chronology is reconstructed.

Do not infer the missing seat or setup order from BotC legality or from later events.

A C1A setup-time DecisionSlice is therefore not admissible.

### 5.3 Later confirmation must not leak backward

Night 2 Undertaker information identifies the executed player as Drunk.

This is valuable later confirmation in the whole-game narrative.

It cannot be used as an input to the earlier Drunk-assignment prefix.

That later confirmation is exactly the kind of hindsight leakage C1 is designed to prevent.

Assignment rationale and explicit alternatives remain `UNKNOWN`.

## 6. R03 — Scott / @sancho — 2025-09-24

Authority:

- `docs/C0_TB_RECONSTRUCTION_BATCH_01_2026-09-23.md`.

### 6.1 Assignment result evidence

The indexed reconstruction establishes:

- Chris is Drunk;
- on Night 1 Chris receives Nick / Luca → Soldier;
- Chris's exact shown information role is not safely established.

Therefore:

~~~text
selected participant = Chris
canonical seat order = UNKNOWN
shown Townsfolk role = UNKNOWN
actual role = Drunk
~~~

Descriptor: `RESULT_ONLY`.

### 6.2 Prefix status

The game is already marked PARTIAL.

There is no evidence-backed pre-assignment setup chronology sufficient for a C1A setup prefix.

No Drunk-assignment DecisionSlice is materialized.

Later Undertaker information and later poisoned Fortune Teller history remain whole-game context only and must not backfill the assignment prefix.

Assignment rationale and alternatives remain `UNKNOWN`.

## 7. R04 — Scott / @sancho — 2025-09-10

Authority:

- `docs/C0_TB_RECONSTRUCTION_BATCH_01_2026-09-23.md`;
- `docs/C0_TB_R04_REPLAY_PREPARATION_2026-09-23.md`.

### 7.1 Assignment result evidence

Indexed Notes establish:

- Hylinn is Drunk;
- Hylinn later receives numeric information `0` on Night 1 and again on Night 2.

The exact shown Townsfolk role remains explicitly `UNKNOWN`.

The rendered grimoire token order has not been verified as canonical clockwise seat order.

Therefore:

~~~text
selected participant = Hylinn
verified seat order = UNKNOWN
shown Townsfolk role = UNKNOWN
actual role = Drunk
~~~

### 7.2 Prefix status

R04 replay preparation contains a working setup/precommit list:

- Red Herring: Sarah for Rhonda;
- Drunk identity: Hylinn;
- Demon bluffs: Chef / Investigator / Saint, reconstructed;
- Hylinn shown role: UNKNOWN.

Those `S01`–`S04` labels are useful replay-preparation ordering, but the currently accessible source does not establish that they are the historical order in which the Storyteller committed those setup choices.

C1B therefore must not promote that working order to `SetupOrderBasis.EVIDENCED`.

Descriptor: `PREFIX_PARTIAL`.

No setup-time C1A DecisionSlice is materialized.

### 7.3 Longitudinal misinformation remains separate

Hylinn receives `0` on Night 1 and again on Night 2.

That is valuable evidence for a persistent Drunk misinformation trajectory.

It does not establish:

- why Hylinn was selected as the Drunk;
- why Hylinn's shown role was selected;
- what alternatives were considered during assignment.

Assignment rationale and alternatives remain `UNKNOWN`.

## 8. C1A contract pressure-test result

C1B found one generic contract issue and one evidence limitation.

### 8.1 Contract issue — corrected

Before C1B, `setup_order` could be consumed as though every deterministic setup order represented historical chronology.

That was unsafe for E0-style edited sources.

`SetupOrderBasis` now prevents this contamination.

No Drunk-specific policy or rules logic was required.

### 8.2 Evidence limitation — do not “fix” in code

The existing corpus simply does not contain enough assignment-time chronology.

The correct response is not to:

- infer legal candidates;
- infer the Storyteller's motive;
- use final grimoire arrangement as proof of decision-time state;
- use later Undertaker/Fortune Teller information to reconstruct the earlier prefix;
- treat a canonical setup order as historical chronology.

The correct durable value is UNKNOWN / PARTIAL.

## 9. C1B completion result

C1B is complete for the current existing corpus.

It has:

- re-audited E0, R02, R03 and R04;
- separated Drunk assignment from later misinformation in every case;
- identified which assignment-result fields are actually known;
- explicitly preserved unknown seat/shown-role fields;
- prevented later-history hindsight leakage;
- found and corrected the canonical-order vs historical-order contract hazard;
- confirmed that Evidence Lab still does not enumerate legal Drunk candidates;
- confirmed that no persistence expansion is justified yet.

C1B does **not** produce the three replayable assignment cases required by the overall C1 completion gate.

That gap now belongs to C1C targeted acquisition.

## 10. Stop point

**Do not begin C1C automatically.**

The next step, if authorized, is targeted acquisition specifically for sources that can establish:

1. selected Drunk participant/seat;
2. shown Townsfolk role;
3. historical setup state immediately before assignment;
4. assignment chronology strong enough for `SetupOrderBasis.EVIDENCED`;
5. explicit assignment rationale and/or considered/rejected alternatives where available.

Broad “find more games with a Drunk” collection remains out of scope.
