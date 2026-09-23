# C0 Trouble Brewing Reconstruction Batch 01 — 2026-09-23

## 1. Scope

This is the first whole-game reconstruction batch from the Trouble Brewing-only C0 acquisition sprint.

The purpose is to preserve interacting setup, misinformation, information delivery, deaths and Demon transitions across a real game so the reconstructed bundle can later be compared with Storyteller App recommendation behavior.

This document is a research working artifact, not a VERIFIED/GOLD corpus import.

Because direct ClockTracker API/page extraction is not currently available in the research environment, the reconstruction below uses exact public ClockTracker game locators plus search-indexed excerpts from those pages. Therefore the status used here is:

- `INDEX_OBSERVED`: content exposed by the search index for the exact ClockTracker game page;
- `PRIOR_C0_OBSERVED`: field recorded during the earlier C0 screening pass from the same exact locator;
- `UNKNOWN`: not safely recoverable from the currently accessible source surface;
- `ANALYSIS`: downstream interpretation, never evidence.

Before promotion to VERIFIED/GOLD, material fields must be checked against the direct source record or another primary source.

Do not infer missing chronology. Do not treat a ClockTracker grimoire page as an automatic semantic night snapshot.

---

## 2. Game R01 — Ash / @CryptCore — Trouble Brewing — 2025-10-03

### 2.1 Source identity

- ClockTracker source ID: `27fc5093-5c64-400e-bd47-d22df5e6087e`
- locator: https://www.clocktracker.app/game/27fc5093-5c64-400e-bd47-d22df5e6087e
- script: Trouble Brewing
- player count: 12
- Storyteller: `@CryptCore`
- recorder/player presentation: Ash
- Ash role: Scarlet Woman
- result: Evil won
- source status: strong A reconstruction candidate

Storyteller/player/result metadata was established during C0 screening from the exact ClockTracker locator.

### 2.2 Ordered reconstruction

| Phase | Reconstructed event | Status |
| --- | --- | --- |
| Night 1 | Washerwoman is poisoned. | INDEX_OBSERVED |
| Night 1 | Poisoned Washerwoman is shown Karyn / Jordan as a Chef pair; Notes explicitly characterize this as incorrect information. | INDEX_OBSERVED |
| Night 1 | Investigator is shown a Baron between the Recluse and Drenaw. The exact registration/actual-role explanation is not reconstructed here. | INDEX_OBSERVED |
| Night 1 | Empath receives 0 while seated between Investigator and Undertaker. | INDEX_OBSERVED |
| Day 1 | Washerwoman is executed. | INDEX_OBSERVED |
| Night 2 | Slayer is poisoned. | INDEX_OBSERVED |
| Night 2 | Monk protects the Imp. | INDEX_OBSERVED |
| Night 2 | Imp kills Undertaker. | INDEX_OBSERVED |
| Night 2 | Empath receives another 0, between Investigator and Saint. | INDEX_OBSERVED |
| Day 2 | Oddish, the Recluse, is executed. | INDEX_OBSERVED |
| Night 3 | Monk is poisoned. | INDEX_OBSERVED |
| Night 3 | Monk again chooses the Imp as protection target. | INDEX_OBSERVED |
| Night 3 | Imp kills Monk. | INDEX_OBSERVED |
| Night 3 | Empath receives 0 between Investigator and Saint. | INDEX_OBSERVED |
| Day 3 | Investigator nominates the Virgin and is executed as part of the Virgin interaction. | INDEX_OBSERVED |
| Night 4 | Slayer is poisoned. | INDEX_OBSERVED |
| Night 4 | Empath is killed. | INDEX_OBSERVED |
| Day 4 | Detailed day sequence is currently incomplete. | UNKNOWN |
| Night 5 | Virgin is poisoned. | INDEX_OBSERVED |
| Night 5 | Imp kills Saint. | INDEX_OBSERVED |
| Day 5 | Town chooses to sleep. | INDEX_OBSERVED |
| Night 6 | Imp kills Virgin. | INDEX_OBSERVED |
| Later / final | Full final-day sequence is not yet safely reconstructed from the current indexed excerpts. | UNKNOWN |

### 2.3 Delivered-information ledger

| Phase | Recipient / shown role | Delivered information | Reliability context |
| --- | --- | --- | --- |
| N1 | Washerwoman | Karyn / Jordan → Chef pair | recipient poisoned; Notes state information was incorrect |
| N1 | Investigator | Baron between Recluse and Drenaw | exact historical registration/actual-role basis UNKNOWN |
| N1 | Empath | 0 | no impairment recovered for Empath at this point |
| N2 | Empath | 0 | no impairment recovered for Empath |
| N3 | Empath | 0 | no impairment recovered for Empath |

### 2.4 State / interaction bundle

This game already preserves a useful sequence of simultaneous pressures:

- N1 misinformation is caused by Poisoner hitting a first-night information role;
- the Investigator and Empath generate additional information in the same initial world;
- poison then moves to Slayer, Monk, Slayer again and Virgin across later nights;
- Monk protection choices and Demon kills evolve while information accumulates;
- repeated Empath 0 results persist through changing deaths/neighbourhood state.

### 2.5 Explicit unknowns

- complete seating / actual-role table has not yet been transcribed into this reconstruction;
- Demon bluffs have not yet been recovered into this batch;
- the actual role corresponding to the Investigator's Baron ping is not asserted;
- some Day 4 and final-day chronology remains missing;
- no Storyteller rationale is recovered yet.

### 2.6 Algorithm-facing observations — ANALYSIS ONLY

The immediate value is not whether any single result was "good". The useful calibration question is whether the recommendation engine can model a bundle where a strong false first-night signal is already injected by Poisoner while several independent truthful information channels remain active, and then update later information recommendations as poison moves elsewhere.

---

## 3. Game R02 — Jeff / @CryptCore + @Larrikin — Trouble Brewing — 2025-09-30

### 3.1 Source identity

- ClockTracker source ID: `de5f126b-89f5-4c78-a898-f5724a93430e`
- locator: https://www.clocktracker.app/game/de5f126b-89f5-4c78-a898-f5724a93430e
- script: Trouble Brewing
- player count: 8
- Storytellers: `@CryptCore`, `@Larrikin`
- recorder/player presentation: Jeff
- source status: strong A reconstruction candidate

Storyteller/player-count metadata was established during the C0 screening pass from this exact locator.

### 3.2 Ordered reconstruction

| Phase | Reconstructed event | Status |
| --- | --- | --- |
| Night 1 | The Drunk, believing they are the Investigator, is shown a Scarlet Woman between the Empath and Fortune Teller. | INDEX_OBSERVED |
| Night 1 | Empath receives 0. | INDEX_OBSERVED |
| Night 1 | Fortune Teller chooses Amy and John and receives NO. | INDEX_OBSERVED |
| Day 1 | Spy is bluffing Recluse. | INDEX_OBSERVED |
| Day 1 | Imp is bluffing Mayor. | INDEX_OBSERVED |
| Day 1 | Investigator claimant / Drunk is executed. | INDEX_OBSERVED |
| Night 2 | Imp kills Ravenkeeper. | INDEX_OBSERVED |
| Night 2 | Ravenkeeper learns Undertaker. | INDEX_OBSERVED |
| Night 2 | Undertaker learns Drunk. | INDEX_OBSERVED |
| Night 2 | Empath receives 0. | INDEX_OBSERVED |
| Night 2 | Fortune Teller chooses Jake and Jade; the result is not safely visible in the current index surface. | INDEX_OBSERVED / result UNKNOWN |
| Day 2 | Complete nomination/execution sequence is not yet recovered. | UNKNOWN |
| Night 3 | Imp kills Empath. | INDEX_OBSERVED |
| Night 3 | Undertaker learns Slayer. | INDEX_OBSERVED |
| Night 3 | Fortune Teller checks Dave (Imp) and Jade (Red Herring) and receives YES. | INDEX_OBSERVED |
| Day 3 | Prior C0 screening records that the Drunk Investigator information is publicly discussed; exact claim sequence still needs direct-source verification. | PRIOR_C0_OBSERVED |
| Night 4 | Dave, the Imp, self-kills/starpasses to John, the Spy. | INDEX_OBSERVED |
| Night 4 | Fortune Teller chooses Amy and Dave and receives YES. | INDEX_OBSERVED |
| Day 5 / final | Nobody is executed because of a tie. | INDEX_OBSERVED |

### 3.3 Delivered-information ledger

| Phase | Recipient / shown role | Delivered information | Reliability / structural context |
| --- | --- | --- | --- |
| N1 | Drunk shown Investigator | Scarlet Woman between Empath / Fortune Teller | Drunk misinformation |
| N1 | Empath | 0 | no impairment recovered |
| N1 | Fortune Teller | Amy + John → NO | John later identified as Spy; exact registration basis is not inferred |
| N2 | Ravenkeeper | Undertaker | death-trigger information |
| N2 | Undertaker | Drunk | confirms Day-1 executed player as Drunk |
| N2 | Empath | 0 | no impairment recovered |
| N2 | Fortune Teller | Jake + Jade → UNKNOWN | result not safely recovered |
| N3 | Undertaker | Slayer | observed |
| N3 | Fortune Teller | Dave (Imp) + Jade (Red Herring) → YES | both Demon and Red-Herring pathways are present; historical witness need not be inferred |
| N4 | Fortune Teller | Amy + Dave → YES | Dave was the prior Imp immediately before/at the starpass sequence; exact action ordering beyond the Notes sequence should be checked directly |

### 3.4 State / interaction bundle

This game is especially valuable because several information narratives collide:

1. the Drunk Investigator starts a fully false minion world;
2. the Spy simultaneously bluffs Recluse and the Imp bluffs Mayor;
3. the Day-1 execution of the Drunk feeds directly into an Undertaker result on Night 2;
4. the Ravenkeeper adds another role confirmation on death;
5. Fortune Teller information evolves across multiple nights and includes an explicit Imp + Red Herring YES;
6. the Imp later transfers Demonhood to the Spy.

This is exactly the kind of multi-clue evolving game state that isolated DecisionSlices cannot represent on their own.

### 3.5 Explicit unknowns

- complete seating / all actual roles are not yet transcribed;
- Demon bluff list beyond the observed active Spy-Recluse and Imp-Mayor bluff behavior is UNKNOWN;
- N2 Fortune Teller result is UNKNOWN;
- some day nomination/execution sequences are incomplete;
- exact final result/winner is not asserted in this batch unless reverified directly;
- Storyteller rationale is not recovered.

### 3.6 Algorithm-facing observations — ANALYSIS ONLY

This game gives a strong future test for consistency algorithms: the Drunk's false world must coexist with later Undertaker confirmation that the executed claimant was Drunk, while Fortune Teller information, Red Herring, Spy bluffing and eventual Demon transfer continue to form alternative worlds. A recommendation algorithm should evaluate these as a joint evolving information bundle rather than independently scoring each clue.

---

## 4. Game R03 — Scott / @sancho — Trouble Brewing — 2025-09-24 — PARTIAL

### 4.1 Source identity

- Storyteller-side ClockTracker source ID: `72d771f4-e866-44cc-8c92-803955ce33e3`
- locator: https://clocktracker.app/game/72d771f4-e866-44cc-8c92-803955ce33e3
- player-side mirror: `5522250b-d848-4498-a8fd-5138f40d8b53`
- mirror locator: https://clocktracker.app/game/5522250b-d848-4498-a8fd-5138f40d8b53
- script: Trouble Brewing
- Storyteller: Scott / `@sancho`
- duplicate handling: both Source records belong to one logical Game after duplicate verification
- reconstruction status in this batch: PARTIAL

### 4.2 Ordered reconstruction

| Phase | Reconstructed event | Status |
| --- | --- | --- |
| Night 1 | Nick sees Butler / Soldier / Mayor. | INDEX_OBSERVED |
| Night 1 | Deonna poisons Brian. | INDEX_OBSERVED |
| Night 1 | Chris, while Drunk, is shown Nick / Luca as Soldier. | INDEX_OBSERVED |
| Night 1 | Tyler receives Empath 0. | INDEX_OBSERVED |
| Night 1 | Hylinn chooses Wesley / Deonna as Fortune Teller targets and receives NO. | INDEX_OBSERVED |
| Day 1 | Detailed execution/nomination sequence is only partially indexed in the current pass. | UNKNOWN |
| Night 2 | Deonna poisons Hylinn. | INDEX_OBSERVED |
| Night 2 | Wesley protects Luca. | INDEX_OBSERVED |
| Night 2 | Nick kills Tyler. | INDEX_OBSERVED |
| Night 2 | Maddox, as Undertaker, learns Drunk. | INDEX_OBSERVED |
| Night 2 | Hylinn chooses Wesley / Nico and receives YES while poisoned. | INDEX_OBSERVED |
| Day 2 | Detailed day sequence remains incomplete. | UNKNOWN |
| Night 3 | Current indexed excerpts were not sufficient to reconstruct safely. | UNKNOWN |
| Day 3 | Current indexed excerpts were not sufficient to reconstruct safely. | UNKNOWN |
| Night 4 | Nick kills Hylinn. | INDEX_OBSERVED |
| Night 4 | Maddox learns Poisoner as Undertaker result. | INDEX_OBSERVED |
| Day 4 | Indexed Notes preserve nominations/votes and Luana's execution/death; exact vote ledger should be transcribed during direct review. | INDEX_OBSERVED |
| Night 5 | Notes show Nick kills another player, but the current excerpt is truncated before a safe full reconstruction. | PARTIAL / UNKNOWN |

### 4.3 Delivered-information ledger

| Phase | Recipient / shown role | Delivered information | Reliability context |
| --- | --- | --- | --- |
| N1 | Nick / first-night information role | Butler / Soldier / Mayor | exact role of recipient not asserted from the excerpt alone |
| N1 | Chris / shown information role | Nick / Luca → Soldier | Chris is explicitly marked Drunk |
| N1 | Tyler / Empath | 0 | no impairment recovered for Tyler |
| N1 | Hylinn / Fortune Teller | Wesley + Deonna → NO | not marked poisoned on N1 excerpt |
| N2 | Maddox / Undertaker | Drunk | observed |
| N2 | Hylinn / Fortune Teller | Wesley + Nico → YES | Hylinn is poisoned that night |
| N4 | Maddox / Undertaker | Poisoner | observed |

### 4.4 Why this remains PARTIAL

The available exact-page index gives high-value N1, N2 and N4 evidence, but N3 and portions of the day chronology are still missing from the current surface.

Do not bridge those gaps using assumptions, mirror similarity or game rules.

### 4.5 Algorithm-facing observations — ANALYSIS ONLY

Even this partial reconstruction is already valuable: the Night-2 Fortune Teller YES is explicitly delivered while the Fortune Teller is poisoned, while Undertaker is simultaneously building a separate role-confirmation chain. This gives a concrete example where false information must be evaluated against the entire accumulated table rather than merely made "plausible" locally.

---


## 4A. Game R04 — Scott / @sancho — Trouble Brewing — 2025-09-10

### 4A.1 Source identity

- ClockTracker source ID: `ffb40a93-3d7b-42c4-bba8-bc9c363dcd30`
- locator: https://clocktracker.app/game/ffb40a93-3d7b-42c4-bba8-bc9c363dcd30
- script: Trouble Brewing
- player count: 14
- Storyteller: Scott / `@sancho`
- community: Asheville Clocktower Club
- location: in person / Well Played Asheville
- result: Evil won
- source status: strongest current A-grade whole-game record

The exact public game page exposes ordered Notes from Setup through Day 7.

### 4A.2 Setup commitments

| Commitment | Reconstructed value | Status |
| --- | --- | --- |
| Red Herring | Sarah (Monk) is the Red Herring for Rhonda's Fortune Teller ability | INDEX_OBSERVED |
| Drunk | Hylinn is marked as the Drunk | INDEX_OBSERVED |
| other full-role assignments | Present in the grimoire but not all transcribed into this batch | PARTIAL |

### 4A.3 Ordered reconstruction

| Phase | Reconstructed event | Status |
| --- | --- | --- |
| Night 1 | Paul receives Chef / Investigator / Saint information. | INDEX_OBSERVED |
| Night 1 | Deonna poisons Brian. | INDEX_OBSERVED |
| Night 1 | Josh is shown Chris / Paul as Chef; Notes mark Spy involvement. | INDEX_OBSERVED |
| Night 1 | Brian is shown Holly / Deonna as Saint while poisoned. | INDEX_OBSERVED |
| Night 1 | Hylinn receives 0 while Drunk. | INDEX_OBSERVED |
| Night 1 | Rhonda checks Nico / Wesley and receives NO. | INDEX_OBSERVED |
| Day 1 | Maddox is executed and dies. | INDEX_OBSERVED |
| Night 2 | Deonna poisons Sarah. | INDEX_OBSERVED |
| Night 2 | Sarah protects Wesley, but the protection fails because Sarah is poisoned. | INDEX_OBSERVED |
| Night 2 | Paul kills Victor. | INDEX_OBSERVED |
| Night 2 | Victor, as Ravenkeeper, checks Deonna and learns Poisoner. | INDEX_OBSERVED |
| Night 2 | Wesley, as Undertaker, learns Soldier from Maddox's execution. | INDEX_OBSERVED |
| Night 2 | Hylinn again receives 0 while Drunk. | INDEX_OBSERVED |
| Night 2 | Rhonda checks Sarah / Josh and receives YES; Sarah is the Red Herring. | INDEX_OBSERVED |
| Night 3 | Deonna poisons Sarah again. | INDEX_OBSERVED |
| Night 3 | Sarah again protects Wesley; protection again fails due to poison. | INDEX_OBSERVED |
| Night 3 | Paul kills Hylinn. | INDEX_OBSERVED |
| Night 3 | Rhonda checks Sarah / Paul and receives YES; the pair contains both the Red Herring and the Demon. | INDEX_OBSERVED |
| Day 3 | Nico uses Slayer on Sarah; nothing happens. | INDEX_OBSERVED |
| Day 3 | Sarah is executed and dies. | INDEX_OBSERVED |
| Night 4 | Deonna poisons Wesley. | INDEX_OBSERVED |
| Night 4 | Paul kills himself. | INDEX_OBSERVED |
| Night 4 | Hollie becomes the Imp. | INDEX_OBSERVED |
| Night 4 | Wesley learns Scarlet Woman as Undertaker information while poisoned. | INDEX_OBSERVED |
| Night 4 | Rhonda checks Josh / Paul and receives YES. | INDEX_OBSERVED |
| Day 4 | Brian nominates Andrew and is executed/dies to the Virgin ability. | INDEX_OBSERVED |
| Night 5 | Deonna poisons Wesley again. | INDEX_OBSERVED |
| Night 5 | Hollie kills Wesley. | INDEX_OBSERVED |
| Night 5 | Rhonda checks Josh / Andrew and receives NO. | INDEX_OBSERVED |
| Day 5 | Josh is executed and dies. | INDEX_OBSERVED |
| Night 6 | Deonna poisons Nico. | INDEX_OBSERVED |
| Night 6 | Hollie kills herself. | INDEX_OBSERVED |
| Night 6 | Deonna becomes the Imp. | INDEX_OBSERVED |
| Night 6 | Rhonda checks Andrew / Paul and receives YES. | INDEX_OBSERVED |
| Day 6 | Rhonda is executed and dies. | INDEX_OBSERVED |
| Night 7 | Deonna kills Nico. | INDEX_OBSERVED |
| Day 7 | Chris is executed with two players left including the Demon. | INDEX_OBSERVED |
| Final | Evil team wins. | INDEX_OBSERVED |

### 4A.4 Delivered-information ledger

| Phase | Recipient / role | Delivered information | Reliability / interaction context |
| --- | --- | --- | --- |
| N1 | Paul | Chef / Investigator / Saint | exact recipient role needs grimoire transcription |
| N1 | Josh | Chris / Paul → Chef | Notes explicitly include Spy involvement |
| N1 | Brian | Holly / Deonna → Saint | Brian is poisoned |
| N1 | Hylinn / shown Empath-like information role | 0 | Hylinn is the Drunk |
| N1 | Rhonda / Fortune Teller | Nico + Wesley → NO | neither Red Herring nor known Demon in pair from Notes |
| N2 | Victor / Ravenkeeper | Deonna → Poisoner | death-trigger information |
| N2 | Wesley / Undertaker | Soldier | follows Maddox execution |
| N2 | Hylinn | 0 | Drunk misinformation/constructed world continues |
| N2 | Rhonda / Fortune Teller | Sarah + Josh → YES | Sarah is Red Herring |
| N3 | Rhonda / Fortune Teller | Sarah + Paul → YES | Sarah = Red Herring; Paul = Demon |
| N4 | Wesley / Undertaker | Scarlet Woman | Wesley is poisoned |
| N4 | Rhonda / Fortune Teller | Josh + Paul → YES | Paul is prior Demon immediately before transfer |
| N5 | Rhonda / Fortune Teller | Josh + Andrew → NO | no impairment recorded for Rhonda |
| N6 | Rhonda / Fortune Teller | Andrew + Paul → YES | Paul is former Demon; exact registration basis should not be inferred beyond observed output |

### 4A.5 Longitudinal information bundle

This game contains several overlapping long-running information systems:

1. **Drunk continuity** — Hylinn receives repeated 0 results across multiple nights rather than unrelated random misinformation.
2. **Red Herring continuity** — Sarah repeatedly participates in Fortune Teller YES results before dying.
3. **Moving Poisoner target** — poison shifts from Brian to Sarah, Wesley and Nico, changing which information/action channels are unreliable each night.
4. **Undertaker chain** — Wesley receives apparently useful execution information, then later receives Scarlet Woman while poisoned.
5. **Fortune Teller chain** — Rhonda receives a sequence of NO / YES / YES / YES / NO / YES across changing pairs and two Demon transfers.
6. **Demon succession** — Paul → Hollie → Deonna changes the true evil center of gravity while older information remains in circulation.

### 4A.6 Explicit unknowns

- full seating/role table is not yet normalized into this reconstruction;
- exact Demon bluff list is not transcribed here;
- the precise historical registration basis behind every information result is not inferred unless Notes explicitly state it;
- player claims and table belief are mostly absent from this structured record;
- Storyteller rationale is not recovered.

### 4A.7 Algorithm-facing observations — ANALYSIS ONLY

R04 is currently the best calibration case for a future whole-game recommendation comparison.

A locally plausible output is not sufficient. The algorithm must preserve a globally coherent evolving information landscape while:

- one false channel is deliberately maintained by Drunk continuity;
- another false/ambiguous channel is structurally created by Red Herring;
- a moving Poisoner temporarily corrupts different roles;
- truthful confirmation channels remain active;
- Demon identity changes twice.

This game therefore strongly supports evaluating recommendation quality at the **bundle trajectory** level rather than scoring each information result independently.


## 5. Batch-level findings

### 5.1 The whole-game unit is already paying off

Across the first three reconstructions, the important structure is not a single Storyteller output.

The recurring pattern is:

~~~text
setup commitments / impairment
    → first-night information bundle
    → public executions and claims
    → later confirmation roles
    → moving poison
    → repeated information
    → deaths / seating changes
    → Demon succession
~~~

The current recommendation engine will ultimately need to be compared against this evolving bundle, not against isolated outputs.

### 5.2 Drunk and Poisoner create different longitudinal problems

The reconstructed examples already contain both:

- a Drunk information world that should remain narratively coherent across later evidence;
- temporary Poisoner corruption whose target moves and whose misleading output sits beside truthful information from other roles.

These should not collapse into one generic `unreliable=true` treatment in downstream analysis.

### 5.3 Confirmation chains matter

Jeff's game shows a particularly useful pattern:

~~~text
Drunk Investigator claim
    → Day-1 execution
    → Undertaker learns Drunk
    → other information continues
~~~

That later confirmation changes the value and interpretation of the earlier false world. A future algorithm comparison therefore needs decision-time boundaries: later confirmation may explain the eventual game state but must not leak backward into what the Storyteller could know or intend at an earlier decision.

### 5.4 Source-record dedup remains mandatory

Scott's Storyteller-side and Brian's player-side records preserve matching chronology for the same real game.

Both sources are useful evidence, but corpus counts must remain logical-game counts rather than raw ClockTracker UUID counts.

---

## 6. Next reconstruction batch

Before expanding discovery again:

1. finish direct/stronger reconstruction of Scott 2025-09-24 if accessible;
2. reconstruct Scott 2025-09-10 from the exact Storyteller record and mirror;
3. reconstruct one compact 8-player and one larger 12–14-player game from the remaining A queue;
4. then begin the first cross-game algorithm-facing comparison.

Do not resume E1-7 merely because this batch exists. First determine whether the reconstruction workflow exposes a blocking domain gap.
