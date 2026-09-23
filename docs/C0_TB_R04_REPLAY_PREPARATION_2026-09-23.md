# C0 Trouble Brewing R04 Replay Preparation — 2026-09-23

## 1. Purpose

Prepare the strongest reconstructed Trouble Brewing game for later CampBoardGameHost historical replay without importing BotC legality into Evidence Lab.

Game:

- reconstruction ID: `R04`
- source: ClockTracker
- source game ID: `ffb40a93-3d7b-42c4-bba8-bc9c363dcd30`
- Storyteller: Scott / `@sancho`
- script: Trouble Brewing
- date: 2025-09-10
- players: 14
- result: Evil won — context only, not a quality label

Primary working reconstruction:

- `docs/C0_TB_RECONSTRUCTION_BATCH_01_2026-09-23.md`

This replay preparation is **not yet runnable corpus truth**. It separates observed source content from reconstruction and inference so missing fields can be filled later without rewriting the event history.

## 2. Source-level setup facts

### 2.1 Directly supported by indexed Notes

- game uses Trouble Brewing;
- 14-player composition is described as 9 Townsfolk / 1 Outsider / 3 Minions / 1 Demon;
- Sarah is explicitly identified as Monk;
- Sarah is Red Herring for Rhonda;
- Hylinn is explicitly identified as Drunk;
- Paul learns Chef / Investigator / Saint at the beginning of the game;
- Deonna performs Poisoner actions;
- Paul performs Imp kill/self-kill actions;
- Rhonda performs Fortune Teller choices;
- Victor performs Ravenkeeper action;
- Wesley performs Undertaker actions;
- Nico performs Slayer action;
- Andrew is the target of a nomination that causes Brian to die to the Virgin ability.

### 2.2 Working setup commitments

| ID | Type | Value | Derivation | Replay status |
| --- | --- | --- | --- | --- |
| R04-SC-001 | RED_HERRING | Sarah for Rhonda | OBSERVED | usable |
| R04-SC-002 | DRUNK_IDENTITY | Hylinn | OBSERVED | usable |
| R04-SC-003 | DEMON_BLUFFS | Chef / Investigator / Saint | RECONSTRUCTED from Paul's Night-1 learn + later Demon actions | needs direct grimoire confirmation |
| R04-SC-004 | DRUNK_SHOWN_ROLE | UNKNOWN | UNKNOWN | blocker for Hylinn information replay |

Do not infer `DRUNK_SHOWN_ROLE` from the numeric value 0.

## 3. Participant identity / seat-order status

The indexed page exposes a rendered grimoire-token order:

~~~text
Hollie
Reyzant
Maddox
Victor
Rhonda
caspian3787
Nico
Hylinn
Deonna
Sarah
Brian
Chris
Josh
Andrew
~~~

The Notes use the names `Paul` and `Wesley` but not `Reyzant` or `caspian3787`.

A set-difference interpretation suggests:

- `Reyzant` ↔ `Paul`;
- `caspian3787` ↔ `Wesley`.

These mappings are **INFERRED**, not source-observed.

Most importantly, the rendered token order has **not** been independently verified as canonical clockwise seat order.

Therefore:

- preserve it as `source_render_order_candidate`;
- do not persist it as `GameSeat.seat_order` yet;
- do not run adjacency-sensitive replay from it until direct grimoire verification.

## 4. Working role reconstruction

This table records only what the Notes support directly or strongly reconstruct through explicit role-action wording.

| Player | Working role/state | Derivation | Notes |
| --- | --- | --- | --- |
| Paul | Imp | RECONSTRUCTED | learns three apparent bluffs; performs Demon kills/self-kill |
| Deonna | Poisoner; later Imp | RECONSTRUCTED | repeated poison actions; becomes Imp Night 6 |
| Sarah | Monk | OBSERVED | explicit setup text |
| Hylinn | Drunk | OBSERVED | explicit Notes text |
| Rhonda | Fortune Teller | RECONSTRUCTED | repeated two-player checks with YES/NO results |
| Victor | Ravenkeeper | RECONSTRUCTED | explicit “ravenkeeps” action |
| Wesley | Undertaker | RECONSTRUCTED | explicit “undertakes” actions |
| Nico | Slayer | RECONSTRUCTED | explicit Slayer action |
| Andrew | likely Virgin | RECONSTRUCTED | Brian dies to Virgin ability after nominating Andrew |
| Brian | information role that receives a two-player Saint clue | UNKNOWN exact role | do not label Librarian from rules alone |
| Josh | information role that receives a two-player Chef clue | UNKNOWN exact role | do not label Washerwoman from rules alone |
| Chris | likely Spy | INFERRED | Night-1 note annotates Spy in Josh clue; exact source-token association needs direct grimoire |
| Hollie | Minion; becomes Imp Night 4 | RECONSTRUCTED / exact setup role UNKNOWN | do not infer Scarlet Woman solely from later Demon transfer |
| Maddox | role UNKNOWN | UNKNOWN | Undertaker later reports Soldier; Evidence Lab does not turn that output into actual role without source verification |

This is deliberately more conservative than a rules-engine reconstruction.

CampBoardGameHost may later validate compatible actual-role assignments using its own legality owners.

## 5. Ordered semantic replay prefix

The following is the minimal mechanically relevant history. Nominations/vote totals are omitted unless they change historical state.

### Setup / precommit

| Order | Event |
| ---: | --- |
| S01 | Red Herring commitment: Sarah for Rhonda |
| S02 | Drunk identity commitment: Hylinn |
| S03 | Demon-bluff bundle observed/reconstructed as Chef / Investigator / Saint |
| S04 | Hylinn shown role remains UNKNOWN |

### Night 1

| Order | Controller | Event |
| ---: | --- | --- |
| 001 | PLAYER | Deonna chooses Brian as Poisoner target |
| 002 | STORYTELLER | Josh receives Chris / Paul → Chef information |
| 003 | STORYTELLER | Brian receives Hollie / Deonna → Saint information while poisoned |
| 004 | STORYTELLER | Hylinn receives numeric result 0 while Drunk |
| 005 | PLAYER | Rhonda chooses Nico / Wesley |
| 006 | STORYTELLER/AUTOMATIC-UNKNOWN | Rhonda receives NO |

### Day 1

| Order | Event |
| ---: | --- |
| 007 | Maddox is executed and dies |

### Night 2

| Order | Controller | Event |
| ---: | --- | --- |
| 008 | PLAYER | Deonna chooses Sarah as Poisoner target |
| 009 | PLAYER | Sarah chooses Wesley for Monk protection |
| 010 | PLAYER | Paul chooses Victor as Demon kill |
| 011 | PLAYER | Victor chooses Deonna for Ravenkeeper information |
| 012 | STORYTELLER/AUTOMATIC-UNKNOWN | Victor receives Poisoner |
| 013 | STORYTELLER/AUTOMATIC-UNKNOWN | Wesley receives Soldier as Undertaker information |
| 014 | STORYTELLER | Hylinn receives 0 while Drunk |
| 015 | PLAYER | Rhonda chooses Sarah / Josh |
| 016 | STORYTELLER/AUTOMATIC-UNKNOWN | Rhonda receives YES; Notes identify Red Herring relevance |

### Night 3 / Day 3

| Order | Controller | Event |
| ---: | --- | --- |
| 017 | PLAYER | Deonna chooses Sarah as Poisoner target |
| 018 | PLAYER | Sarah chooses Wesley for Monk protection |
| 019 | PLAYER | Paul kills Hylinn |
| 020 | PLAYER | Rhonda chooses Sarah / Paul |
| 021 | STORYTELLER/AUTOMATIC-UNKNOWN | Rhonda receives YES; Notes identify Red Herring + Demon relevance |
| 022 | PLAYER | Nico uses Slayer on Sarah; no kill |
| 023 | AUTOMATIC/PLAYER-STATE | Sarah is executed and dies |

### Night 4 / Day 4

| Order | Controller | Event |
| ---: | --- | --- |
| 024 | PLAYER | Deonna poisons Wesley |
| 025 | PLAYER | Paul kills himself |
| 026 | AUTOMATIC/ROLE-TRANSITION | Hollie becomes Imp |
| 027 | STORYTELLER | poisoned Wesley receives Scarlet Woman as Undertaker information |
| 028 | PLAYER | Rhonda chooses Josh / Paul |
| 029 | STORYTELLER/AUTOMATIC-UNKNOWN | Rhonda receives YES |
| 030 | PLAYER | Brian nominates Andrew |
| 031 | AUTOMATIC/ROLE-ABILITY | Brian is executed/dies to Virgin ability |

### Night 5 / Day 5

| Order | Controller | Event |
| ---: | --- | --- |
| 032 | PLAYER | Deonna poisons Wesley |
| 033 | PLAYER | Hollie kills Wesley |
| 034 | PLAYER | Rhonda chooses Josh / Andrew |
| 035 | STORYTELLER/AUTOMATIC-UNKNOWN | Rhonda receives NO |
| 036 | AUTOMATIC/PLAYER-STATE | Josh is executed and dies |

### Night 6 / Day 6

| Order | Controller | Event |
| ---: | --- | --- |
| 037 | PLAYER | Deonna poisons Nico |
| 038 | PLAYER | Hollie kills herself |
| 039 | AUTOMATIC/ROLE-TRANSITION | Deonna becomes Imp |
| 040 | PLAYER | Rhonda chooses Andrew / Paul |
| 041 | STORYTELLER/AUTOMATIC-UNKNOWN | Rhonda receives YES |
| 042 | AUTOMATIC/PLAYER-STATE | Rhonda is executed and dies |

### Night 7 / Day 7

| Order | Controller | Event |
| ---: | --- | --- |
| 043 | PLAYER | Deonna kills Nico |
| 044 | AUTOMATIC/PLAYER-STATE | Chris is executed and dies |
| 045 | CONTEXT | Evil wins |

The `STORYTELLER/AUTOMATIC-UNKNOWN` controller label is intentional. Evidence Lab records the delivered result but does not decide whether rules forced it; CampBoardGameHost owns that determination.

## 6. Candidate Storyteller decision boundaries

These are replay candidates, not quality labels.

### R04-D01 — Red Herring setup

Boundary:

~~~text
setup commitments before Red Herring selection
~~~

Observed choice:

- Sarah for Rhonda.

Current replay readiness:

- observed choice: READY;
- player count/script: READY;
- exact seat order / full role map: BLOCKED;
- legal alternative enumeration: intentionally delegated to CampBoardGameHost.

### R04-D02 — Demon bluff bundle

Boundary:

~~~text
setup before Demon bluffs are committed
~~~

Observed/reconstructed choice:

- Chef / Investigator / Saint.

Current replay readiness:

- bundle: RECONSTRUCTED, direct grimoire confirmation still desired;
- full setup: PARTIAL;
- legal candidate generation belongs downstream.

### R04-D03 — poisoned Brian Night-1 information

Committed prefix:

~~~text
setup commitments
+ Deonna chooses Brian as poison target
~~~

Observed output:

- Hollie / Deonna → Saint.

Current replay readiness:

- poison target and delivered output: READY;
- Brian exact actual/shown ability: BLOCKED;
- seat order/full role map: BLOCKED.

This is a high-value first-night impaired-information case once those setup fields are recovered.

### R04-D04 — Drunk Hylinn Night-1 information

Committed prefix:

~~~text
setup commitments including Hylinn = Drunk
~~~

Observed output:

- 0.

Current replay readiness:

- Drunk identity and output: READY;
- Hylinn shown ability: BLOCKED.

Do not generate legal numeric alternatives until the shown ability is verified.

### R04-D05 — poisoned Wesley Night-4 Undertaker information

Committed prefix:

~~~text
all events through Night 4 order 026
including:
Deonna poisons Wesley
Paul self-kills
Hollie becomes Imp
~~~

Observed output:

- Scarlet Woman.

Current replay readiness:

- historical prefix: largely READY;
- Wesley Undertaker identity: RECONSTRUCTED;
- exact seat/role setup: PARTIAL;
- current CampBoardGameHost structured shadow: NOT CAPABLE — First-Night-only.

This is an excellent later-phase replay case for future SDE historical shadow work.

## 7. Replay blockers

The smallest remaining R04 blockers are:

1. **verified clockwise seat order**;
2. **full actual role map from the grimoire**;
3. **Hylinn shown role**;
4. **Brian actual/shown information role**;
5. direct confirmation of the three Demon bluffs from grimoire metadata rather than only Notes semantics.

These are much smaller than reconstructing the game again.

## 8. Downstream ownership

ClocktowerEvidenceLab exports only:

- observed/reconstructed setup commitments;
- ordered historical events;
- candidate decision boundaries;
- observed choices;
- derivation/provenance/UNKNOWN state.

CampBoardGameHost must own:

- legal alternative enumeration;
- rules-forced vs discretionary classification;
- Spy/Recluse compatible registration branches;
- world solving;
- DecisionFeatures projection;
- policy comparison.

No downstream rule conclusion should be copied back into Evidence Lab as source observation.

## 9. Immediate next action

Do not reconstruct another entire game yet.

First try to close R04 blockers through a direct ClockTracker grimoire view, screenshot, mirror source, or other primary structured representation.

If those fields remain inaccessible in the current research environment, preserve this package as `REPLAY_PREP_PARTIAL` and prepare R02 next; do not guess missing setup.
