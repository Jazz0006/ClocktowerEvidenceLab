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

Replay preparation status: **REPLAY_PREP_PARTIAL / STRUCTURED ROLE MAP + BLUFFS RECOVERED / DECISION-PREFIX CHRONOLOGY STILL REQUIRES PER-BOUNDARY AUDIT**.

This replay preparation is **not yet runnable corpus truth**. It separates observed source content from reconstruction and inference so missing fields can be filled later without rewriting the event history.

A follow-up access pass attempted:

- the known player-side mirror Source `945f3458-39aa-4ef2-be1a-06aad9bca83c`;
- the public ClockTracker game API route;
- public image search for the grimoire.

The 2026-09-23 research tools did not expose the mirror/grimoire/API payload. On 2026-10-06 the bounded EL-ML1C CT-1 route fetched the public structured payload through GitHub Actions. Runs `37447792091` and `37448212336` recovered and normalized 14 grimoire snapshots, the complete role/related-role data, reminders and Demon bluffs. One intermediate snapshot (`79349`) has ambiguous duplicate persisted order and is explicitly flagged rather than repaired.

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
| R04-SC-003 | DEMON_BLUFFS | Chef / Investigator / Saint | OBSERVED structured game metadata | usable |
| R04-SC-004 | DRUNK_SHOWN_ROLE | Empath | OBSERVED structured `related_role_id` for Hylinn's Drunk token | usable |

The shown role is now source-backed by structured related-role metadata, not inferred from the numeric value 0.

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

**2026-10-06 update:** the rendered token order is now verified as the persisted grimoire circular sequence. ClockTracker's current `components/Grimoire.vue` sorts public tokens by `token.order` and positions the resulting indexed sequence around the circle. Preserve the first rendered token only as an analysis-derived seat-1 origin; the source does not assign semantic significance to that origin.

Therefore:

- the listed sequence may now be persisted as the source-backed circular `GameSeat.seat_order` sequence;
- adjacency-sensitive reconstruction may use this circle order;
- `Reyzant ↔ Paul` and `caspian3787 ↔ Wesley` remain INFERRED aliases and must not be silently promoted.

## 4. Working role reconstruction

This table records only what the Notes support directly or strongly reconstruct through explicit role-action wording.

| Player | Working role/state | Derivation | Notes |
| --- | --- | --- | --- |
| Hollie | Scarlet Woman; later Imp | OBSERVED structured snapshot + later Notes transition | initial snapshot `79346` = Scarlet Woman |
| Reyzant | Undertaker | OBSERVED structured snapshot | Notes alias to Wesley remains INFERRED |
| Maddox | Soldier | OBSERVED structured snapshot | closes earlier role UNKNOWN |
| Victor | Ravenkeeper | OBSERVED structured snapshot | consistent with Notes action |
| Rhonda | Fortune Teller | OBSERVED structured snapshot | consistent with repeated checks |
| caspian3787 | Imp | OBSERVED structured snapshot | Notes alias to Paul remains INFERRED |
| Nico | Slayer | OBSERVED structured snapshot | consistent with Notes action |
| Hylinn | Drunk shown Empath | OBSERVED structured role + related role | `role_id=drunk`, `related_role_id=empath` |
| Deonna | Poisoner; later Imp | OBSERVED initial structured snapshot + later Notes transition | initial snapshot = Poisoner |
| Sarah | Monk | OBSERVED structured snapshot + Notes | Red Herring reminder also present |
| Brian | Librarian | OBSERVED structured snapshot | closes earlier UNKNOWN exact role |
| Chris | Spy | OBSERVED structured snapshot | closes earlier INFERRED role |
| Josh | Washerwoman | OBSERVED structured snapshot | closes earlier UNKNOWN exact role |
| Andrew | Virgin | OBSERVED structured snapshot | consistent with later nomination death |

The initial role map is now source-backed rather than rules-engine reconstructed. Later role transitions still remain separate historical events.

CampBoardGameHost continues to own legality and rule validation; EvidenceLab only preserves the structured source state and chronology.

## 5. Ordered semantic replay prefix

The following is the minimal mechanically relevant history. Nominations/vote totals are omitted unless they change historical state.

### Setup / precommit

| Order | Event |
| ---: | --- |
| S01 | Red Herring commitment: Sarah for Rhonda |
| S02 | Drunk identity commitment: Hylinn |
| S03 | Demon-bluff bundle directly observed in structured metadata: Chef / Investigator / Saint |
| S04 | Hylinn actual Drunk / shown Empath from structured `role_id` + `related_role_id` |

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
- exact seat order / full role map: READY from structured snapshots;
- exact setup-commitment chronology before Red Herring selection: still requires bounded source audit;
- legal alternative enumeration: intentionally delegated to CampBoardGameHost.

### R04-D02 — Demon bluff bundle

Boundary:

~~~text
setup before Demon bluffs are committed
~~~

Observed/reconstructed choice:

- Chef / Investigator / Saint.

Current replay readiness:

- bundle: READY from structured game metadata;
- full role setup: READY from structured snapshot;
- exact commitment boundary before Demon bluffs: still requires bounded source audit;
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
- Brian actual role = Librarian: READY from structured snapshot;
- seat order/full role map: READY;
- exact setup/first-night commitments preceding Brian's clue: still PARTIAL.

This remains a high-value first-night impaired-information case; the blocker has shifted from identity to historical-prefix chronology.

### R04-D04 — Drunk Hylinn Night-1 information

Committed prefix:

~~~text
setup commitments including Hylinn = Drunk
~~~

Observed output:

- 0.

Current replay readiness:

- Drunk identity and output: READY;
- Hylinn shown ability = Empath: READY from structured related-role metadata;
- exact pre-output setup/first-night prefix: still PARTIAL.

Do not generate legal numeric alternatives in EvidenceLab; candidate legality remains Host-owned.

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

- historical event prefix through Night-4 order 026: largely READY from Notes;
- structured role map contains Reyzant = Undertaker; Notes alias `Wesley ↔ Reyzant` remains INFERRED;
- exact seat/role setup: READY at structured-source level;
- exact full decision-time prefix, including any omitted socially relevant chronology: still requires bounded audit;
- current CampBoardGameHost structured shadow: historical replay capability must be re-audited downstream.

This is an excellent later-phase replay case for future SDE historical shadow work.

## 7. Replay blockers

The original five source-data blockers are all closed:

1. **circular seat order** — CLOSED;
2. **full actual/shown role map** — CLOSED;
3. **Hylinn shown role** — CLOSED as Empath;
4. **Brian exact role** — CLOSED as Librarian;
5. **Demon bluff triplet** — CLOSED as Chef / Investigator / Saint.

Remaining blockers are now decision-specific rather than source-schema gaps:

- exact setup commitment order for setup-time decisions;
- exact first-night prefix before D03/D04;
- Notes alias resolution where a decision uses `Paul` / `Wesley` rather than the structured player names;
- any omitted public/social chronology required by a later-game rationale.

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

Do not repeat raw-grimoire acquisition for R04; that layer is now complete.

Re-audit R04 decision boundaries using the structured role map plus Notes chronology. Promote only a decision whose exact historical prefix can be represented without importing final-snapshot state backward.

The strongest next R04 candidate is D05 (poisoned Undertaker display) because its multi-night event chain is already substantially reconstructed. Setup-time D01/D02 and first-night D03/D04 remain more sensitive to unresolved setup ordering.
