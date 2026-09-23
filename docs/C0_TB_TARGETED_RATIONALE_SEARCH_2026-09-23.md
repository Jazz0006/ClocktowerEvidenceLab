# C0 Trouble Brewing Targeted Rationale Search — 2026-09-23

## 1. Purpose

After the first six whole-game reconstructions, broad game discovery is no longer the highest-value evidence activity.

This pass searches specifically for **explicit Storyteller rationale** relevant to the remaining Storyteller Decision Engine policy dimensions:

1. healthy-information floor / middle band;
2. impaired-information believability and longitudinal coherence;
3. role-function exposure / confirmation-chain severity;
4. Demon-bluff route quality;
5. contextual multi-axis tradeoffs.

The search does not promote advice merely because it sounds reasonable. Storyteller identity/experience and source type remain separate evidence dimensions.

## 2. Admission levels used in this pass

### WHOLE_GAME_EXPERT_RATIONALE

Preferred target:

- experienced/trusted Storyteller is independently identifiable;
- concrete real game is reconstructable;
- relevant decision and rationale are tied to the game state.

This can later support high-value DecisionSlices.

### EXPERT_GUIDANCE_WITH_GAME_EXAMPLES

Useful but weaker:

- experienced Storyteller is independently supportable;
- explicit rationale is given;
- examples from real games may be discussed;
- no complete reconstructable game state is available.

This can validate **which policy dimensions matter**, but should not be used as a replay case or as numeric calibration.

### COMMUNITY_RATIONALE

Useful only as a lead/generalization source:

- Storyteller experience is self-described or unverified;
- or the source is a community discussion without stable expert identity.

Do not use this level to freeze SDE preference strength.

## 3. New admitted expert-guidance source — Beardy / Ravenkeeper

Source:

- Clocktower Academy — `Ravenkeeper (TB) w/ Beardy`;
- published 2026-03-27;
- transcript surfaced publicly through Listen Notes;
- source locator: https://www.listennotes.com/podcasts/clocktower-academy/ravenkeeper-tb-w-beardy-wQl6i4IEDqG/
- episode describes Beardy as a highly experienced Blood on the Clocktower content creator/streamer and references his prior Storytelling 101 appearance;
- Beardy's own public site also documents substantial ongoing game/storytelling volume.

Admission:

- **EXPERT_GUIDANCE_WITH_GAME_EXAMPLES**
- not a whole-game reconstruction;
- not GOLD;
- valuable qualitative policy evidence.

### 3.1 Explicit Storyteller rationale recovered

Beardy explains that what a sober/healthy Ravenkeeper should learn from a Spy is **game-state dependent**.

Paraphrased rationale:

- if the Ravenkeeper dies early, such as Night 2, showing the Spy's current bluff can be a reasonable way to support the evil team;
- if the interaction happens near Final 3, directly showing Spy may instead be appropriate;
- the decision is balance/context dependent rather than a fixed “always reveal Spy” or “always misregister Spy” rule.

This directly supports a contextual policy dimension around:

- role-function exposure;
- confirmation-chain strength;
- lifecycle/game-stage sensitivity;
- evil-cover preservation.

It argues against a fixed role-local penalty such as:

~~~text
Ravenkeeper targets Spy
    → always show Spy
~~~

or:

~~~text
Ravenkeeper targets Spy
    → always show bluff role
~~~

### 3.2 Confirmation-chain rationale

The same discussion explicitly treats Ravenkeeper information as capable of:

- confirming another information role;
- establishing that a claimed information role is not the Drunk;
- joining a confirmation chain;
- producing much larger impact late in the game than early in the game.

This independently supports the already-created SDE feature family:

- `ConfirmationChainFeatures`

and supports the C0 finding that raw topology retention alone does not capture information value.

### 3.3 Impaired Ravenkeeper examples

The episode also discusses real-game anecdotes where:

- a Drunk or poisoned Ravenkeeper receives incorrect role information;
- that misinformation can directly cause a good player to be executed;
- the same role can swing strongly for Good or Evil depending on impairment and context.

The useful policy signal is **not** “make impaired Ravenkeeper information false.”

The useful signal is:

> impairment information value is contextual and interacts with confirmation strength, game phase and what the table can infer.

This supports the generic impaired-narrative architecture, not a role-specific hard rule.

## 4. New evidence consequence

Before this pass, role-function exposure severity and confirmation topology were supported mainly by:

- internal mechanical reasoning;
- reconstructed whole-game examples;
- prior qualitative expert evidence.

This source adds an independent experienced-Storyteller rationale that explicitly makes the choice **context and lifecycle dependent**.

Current evidence maturity adjustment:

### Confirmation-chain importance

Upgrade from:

~~~text
real-game observed structure + architecture rationale
~~~

to:

~~~text
real-game observed structure
+ independent explicit expert guidance
~~~

This is enough to justify implementing/projecting the dimension.

It is still insufficient to freeze numeric thresholds.

### Role-function exposure

Upgrade slightly:

- explicit expert rationale shows direct role revelation can be correct or undesirable depending on game state;
- therefore exposure severity should remain a soft/contextual feature rather than a universal reject.

Still missing:

- a complete reconstructable expert game with legal alternatives and an explicit considered/rejected exposure choice.

## 5. Sources screened but not admitted to expert calibration

### 5.1 Experienced Storyteller asking for TB advice — Reddit 2026

A poster self-reports roughly two years of storytelling experience and asks for advice on making Trouble Brewing more engaging.

The discussion contains useful examples of:

- using Recluse/Spy registration;
- helping inexperienced evil players;
- Demon bluff quality;
- game pace.

Disposition:

- **COMMUNITY_RATIONALE / LEAD ONLY**
- experience is self-described rather than independently established in this pass;
- comments are multi-author and not cleanly attributable to one qualified Storyteller;
- no single reconstructable game + rationale contract.

Do not use for expert calibration.

### 5.2 First-time Storyteller reports

Multiple sources contain explicit reasoning such as:

- selecting the Drunk because evil players were adjacent;
- choosing active/informative roles for first-time players;
- selecting role bags to create an interesting dynamic.

These are useful examples of the types of decisions Storytellers make.

Disposition:

- **REJECTED FOR EXPERT POLICY CALIBRATION**
- first-time/new Storyteller status is explicit.

They may be retained only if a future project studies novice-Storyteller behavior.

### 5.3 Community fairness / “what would you do” discussions

Several Trouble Brewing threads contain strong opinions on:

- not exposing both Minions to Investigator;
- avoiding harmful bluff combinations;
- using Recluse as an alternate Investigator ping;
- how much misinformation a game needs.

Disposition:

- **LEAD / COMMUNITY DISCUSSION ONLY**
- these are opinions about another Storyteller's game;
- they are not primary rationale from the original Storyteller;
- silent alternatives must not be converted into expert GOOD/BAD labels.

### 5.4 Official Trouble Brewing overview

The official Trouble Brewing page states the broad design principle that believable falsehood gives Evil room while Good combines logic/information.

Disposition:

- useful background;
- not a new real-game rationale case;
- do not use it to derive numeric misinformation targets.

## 6. Search result for the four targeted gaps

| Gap | New result | Current status |
| --- | --- | --- |
| healthy-information floor / middle band | no new qualified explicit whole-game rationale | still open |
| independent impaired-information believability | Beardy gives contextual impaired Ravenkeeper examples, but not a complete replayable decision with alternatives | improved qualitative support; still open for GOLD |
| role-function exposure / confirmation severity | Beardy explicitly says Spy reveal vs bluff-role display depends on early/late game state | meaningful independent expert support |
| Demon-bluff triplet rationale | no qualified explicit choice-over-alternatives case found | still open |
| multi-axis tradeoff | Beardy evidence reinforces context dependence, not numeric ordering | corpus problem remains |

## 7. Relationship to the six reconstructed games

The Beardy guidance is especially compatible with:

### R02

Ravenkeeper / Undertaker / Drunk confirmation chain demonstrates how one information event can authenticate another.

### R04

Ravenkeeper → Poisoner and later Undertaker / Fortune Teller chains show that role information can radically change the table's topology and credibility structure.

### R06

A poisoned Ravenkeeper is weaponized into incorrect role information, matching the expert-guidance warning that an impaired Ravenkeeper can swing strongly for Evil.

The guidance therefore adds rationale-level support to patterns already visible in real whole-game records.

It does **not** prove that the observed R02/R04/R06 Storytellers chose optimally.

## 8. ClockTracker rationale search result

A dedicated Trouble Brewing ClockTracker search was run using rationale-oriented terms such as:

- `because`;
- `wanted to`;
- `I chose`;
- `decided`;
- `red herring` + rationale terms;
- `drunk` / `poisoned` + rationale terms.

No usable **Trouble Brewing whole-game ClockTracker record with explicit Storyteller decision rationale** was recovered from the public search index in this pass.

This is a source-family finding, not proof that no such records exist.

Current practical division of labor is therefore:

~~~text
ClockTracker
    → setup / grimoire / reminders
    → ordered Notes
    → mechanical whole-game backbone

expert podcast / postgame / primary commentary
    → why this information was chosen
    → why an alternative was rejected
    → lifecycle / balance rationale
~~~

Do not delay mechanical reconstruction waiting for ClockTracker to provide rationale that it often does not record.

## 9. Acquisition decision

Do not return to broad web/community advice collection.

The next rationale search should be narrower:

1. primary/postgame commentary by independently established Storytellers already present in the corpus;
2. official/TPI or high-confidence experienced Storyteller game recordings with postgame explanation;
3. exact decisions involving:
   - healthy-information strength;
   - persistent Drunk world;
   - explicit role-function exposure choice;
   - Demon-bluff triplet selection.

Stop when the source lacks either:

- attributable qualified Storyteller identity; or
- a concrete decision/rationale that maps to an SDE feature.

## 10. Product implication

The new source does **not** justify changing policy weights.

It does strengthen one engineering priority from the algorithm-gap audit:

> confirmation-chain impact and contextual role-function exposure should be among the earliest non-strategic feature projectors implemented before SDE-3B relies on those dimensions.

`FeatureProjection.Unavailable` must remain explicit until such projection exists.
