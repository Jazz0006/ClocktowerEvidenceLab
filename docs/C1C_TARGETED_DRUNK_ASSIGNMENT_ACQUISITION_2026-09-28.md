# C1C — Targeted Drunk Assignment Acquisition

> Status: **IN PROGRESS / BOUNDED PRIMARY REVIEW QUEUE READY**
>
> Date: 2026-09-28
>
> Scope: Trouble Brewing Drunk assignment only. This is not a broad corpus-growth pass.

## 1. Purpose

C1B established that the current corpus contains four Drunk-assignment result cases but zero cases with an evidence-backed reconstructable pre-assignment setup prefix.

C1C therefore searches only for evidence that can close this specific gap.

The target evidence shape is:

~~~text
already-shown Townsfolk / seat layout
    + historically evidenced setup state before assignment
    + Storyteller chooses one shown Townsfolk participant as Drunk
    + resulting assignment
    + source provenance
    + assignment rationale / alternatives when explicitly present
~~~

Evidence Lab still does not derive the legal Drunk candidate set.

## 2. Completion target

The C1 completion gate seeks:

- at least 3 Drunk-assignment cases with reconstructable decision prefixes;
- seek 1–2 cases with explicit assignment rationale if available;
- preserve independent Storyteller coverage where practical.

C1C should stop broad searching once a small bounded primary-review queue exists.

A source does not count toward the replay target merely because it:

- contains a Drunk;
- shows the final grimoire;
- explains general Drunk strategy;
- gives later Drunk misinformation;
- allows a rules engine to infer legal candidates.

## 3. Targeted search result

The search produced two distinct source classes.

### 3.1 Historical game candidates

These may become replay cases after bounded primary review.

#### C1C-G01 — E0 / A Stud In Scarlet — P0

Primary source:

- No Rolls Barred;
- stable YouTube video ID: `qZBvRfM3Xow`;
- Storytellers: Ben Burns + Adam;
- Trouble Brewing;
- existing E0 human review already establishes Sullivan = Drunk, shown Empath, visible setup seat 9.

Why C1C reopens this case:

The public episode recap preserves the opening framing that the players are sent to sleep and the Storytellers then discuss how they will run the game.

Existing human review already has:

- approximately 09:49 — Sullivan is Drunk;
- approximately 10:32 — Sullivan is also made the Fortune Teller Red Herring.

C1B correctly refused to infer historical setup order from those source timestamps alone.

C1C asks a narrower question:

> Does the actual Storyteller setup conversation immediately around 09:30–10:40 explicitly establish what had already been fixed before Sullivan was selected as the Drunk?

Bounded primary-review target:

- start before the first Drunk-selection statement;
- identify every setup fact explicitly treated as already fixed;
- capture the exact assignment statement;
- distinguish discussion/proposal from final commitment;
- continue only far enough to determine whether later Red Herring/bluff choices occur after assignment;
- capture any explicit reason for choosing Sullivan/Empath;
- capture any explicitly considered/rejected alternative.

Bounded primary review result — 2026-09-28:

- at the point Sullivan is selected as the Drunk, the complete player role / shown-role layout is already fixed;
- Sullivan is selected as the Drunk while shown Empath;
- no assignment rationale is stated;
- no alternative Drunk participant/role is discussed;
- Red Herring = Sullivan is selected after the Drunk assignment;
- the internal order in which the individual roles inside the complete layout were originally chosen remains UNKNOWN.

Current status:

- assignment result: VERIFIED;
- shown role: VERIFIED = Empath;
- seat/layout: VERIFIED as already fixed before assignment;
- assignment prefix: **PREFIX_RECONSTRUCTABLE**;
- assignment rationale: UNKNOWN;
- explicitly considered/rejected alternatives: UNKNOWN;
- later Red Herring: VERIFIED as after assignment;
- replay status: **C1C REPLAY CASE 1 / 3**.

For replay, model the already-fixed complete role layout as one evidenced setup commitment group. This preserves the verified group ordering without inventing an internal role-selection order.

G01 is therefore resolved and no longer blocks on primary review.

#### C1C-G02 — Live and Imp-Person — P1

Primary source:

- No Rolls Barred;
- YouTube video ID: `m14N28Lq-jM`;
- Storytellers: Ben Burns + Tom;
- Trouble Brewing;
- released 2022-05-14.

Public secondary recap currently establishes:

- clockwise player/role layout;
- Brooke = Drunk, believes Undertaker;
- Demon bluffs = Investigator / Empath / Saint;
- Fortune Teller Red Herring = Carley herself;
- detailed Night/Day event history.

Relevant assignment result:

~~~text
selected participant = Brooke
actual role = Drunk
shown role = Undertaker
~~~

This makes the source materially better than a generic “game with a Drunk” lead.

However, the currently indexed recap does **not** establish:

- historical order of setup commitments;
- state immediately before Brooke was selected;
- whether Brooke/Undertaker was chosen after the apparent Townsfolk layout existed;
- assignment rationale;
- explicit considered/rejected alternatives.

Bounded primary review result — 2026-09-28:

- around 04:10 the source reveals Brooke as the actual Drunk shown/believing Undertaker;
- no reason is stated for choosing Brooke as the Drunk;
- no alternative Drunk participant/role is discussed;
- the video presents the game as an already-designed setup rather than showing the Drunk-assignment construction process;
- therefore the source does not establish which setup commitments were historically fixed immediately before Brooke was selected.

Current assignment status:

- assignment result: VERIFIED by human primary review;
- shown role: VERIFIED = Undertaker;
- assignment prefix: **UNKNOWN / NOT PREFIX_RECONSTRUCTABLE**;
- assignment rationale: UNKNOWN;
- explicitly considered/rejected assignment alternatives: UNKNOWN;
- replay disposition: **DO NOT COUNT TOWARD C1C 3-CASE ASSIGNMENT QUOTA**.

C1C bounded locator search on 2026-09-28 additionally confirmed:

- the public episode index consistently identifies Brooke as the Drunk shown Undertaker;
- the public index exposes the complete role layout and other setup outcomes;
- no trustworthy setup timestamp or indexed primary transcript was recovered;
- automated search therefore cannot establish assignment chronology.

Do not guess a setup timestamp and do not import the fan recap as primary chronology.

Manual review is now complete for the assignment question. Do not spend more time trying to manufacture setup chronology from this episode unless a new unedited/setup-construction source for the same game appears.

### G02 independent value — explicit Drunk misinformation strategy

The same primary review recovered a separate high-value Storyteller strategy statement from Ben.

Paraphrased strategy:

- give Brooke correct information for the first one or two nights so that she does not suspect she is the Drunk;
- after that, continue giving her incorrect information.

Evidence classification:

- decision family: **Drunk misinformation / longitudinal impaired narrative**;
- source type: primary Storyteller commentary in a real game;
- historical assignment rationale: NOT APPLICABLE;
- assignment prefix evidence: does not improve;
- misinformation strategy/rationale: **EXPLICIT**;
- multi-night intent: **EXPLICIT**.

This must not be copied into the Drunk-assignment rationale field.

It is valuable for the separate downstream impaired-narrative policy because it provides direct expert evidence for deliberate early truth followed by sustained false information to protect the Drunk's subjective role belief.

#### C1C-G03 — official Trouble Brewing October 2019 Game 2 — P2

Primary source:

- official Blood on the Clocktower YouTube channel;
- video ID: `pVzZms1FTr4`;
- 8-player Trouble Brewing;
- Storyteller: Steven Medway.

Bounded primary review result — 2026-09-28:

The reviewed setup frame shows an 8-player Trouble Brewing game with:

- Ben — Mayor;
- Brittany — Poisoner;
- Zach — Investigator;
- Reggie — Empath;
- Evin — Ravenkeeper;
- Meg — Saint;
- Eden — Undertaker;
- Jon — Imp.

Therefore **no Drunk is in this setup**.

The source also shows Demon bluffs:

- Recluse;
- Fortune Teller;
- Monk.

Night-1 screenshots additionally preserve:

- Brittany the Poisoner poisons Zach;
- poisoned Zach, as Investigator, falsely learns that Reggie or Evin is the Scarlet Woman;
- Reggie, as Empath, learns 0 for living neighbours Zach and Evin.

Disposition for C1C assignment acquisition:

- **SCREENED OUT — NO DRUNK**;
- contributes 0 assignment replay cases;
- do not spend more C1C review time on this game.

Ancillary evidence value:

- useful primary example of temporary Poisoner corruption;
- useful first-night bundle where a false Investigator signal coexists with a healthy Empath 0;
- preserve as a future C0/SDE misinformation reference if needed, but do not widen C1C scope around it.

#### C1C-G04 — official Trouble Brewing October 2019 Game 1 — P2

Primary source:

- official Blood on the Clocktower YouTube channel;
- video ID: `2TlW06GVF8I`;
- 7-player Trouble Brewing;
- Storyteller: Jon Gjengset.

Bounded primary review result — 2026-09-28:

The reviewed 7-player Trouble Brewing setup shows:

- Jordan — Spy;
- Jason — Ravenkeeper;
- Reggie — Undertaker;
- Evin — Virgin;
- Zach — Imp;
- Meg — Mayor;
- Nicole — Washerwoman.

Therefore **no Drunk is in this setup**.

The Demon learns three bluffs:

- Investigator;
- Soldier;
- Chef.

Night-1 primary screenshots also preserve an explicit registration witness:

- Nicole, as Washerwoman, falsely learns that Zach or Jordan is the Soldier;
- the video explicitly states this information is possible because **Jordan, the Spy, is registering as the Soldier** for this interaction.

Disposition for C1C assignment acquisition:

- **SCREENED OUT — NO DRUNK**;
- contributes 0 Drunk-assignment replay cases;
- do not spend more C1C review time on this game.

Ancillary evidence value:

- strong primary example of an explicit historical Spy registration witness;
- unlike rules-derived compatible witnesses, this witness is source-observed and may be recorded as historical evidence;
- useful future registration / Washerwoman / Spy calibration case outside the narrow C1C assignment quota.

#### C1C-G05 — A Fond Farewell — NEW P0

Primary source:

- official Blood on the Clocktower YouTube channel;
- video ID: `M5VY5GnXAxw`;
- title: `Trouble Brewing - A Fond Farewell`;
- Storyteller: Ben Burns;
- exact script: Trouble Brewing;
- source chapters expose `Intro & Setup` from 00:00 to 04:25.

Prior project collection notes treat this as a Drunk-bearing game and therefore make it a much stronger next C1C candidate than an unscreened generic Trouble Brewing video.

Important provenance rule:

- those prior notes are a locator lead only for this C1C pass;
- do not promote assignment result/prefix/rationale until the primary setup segment is re-reviewed under the C1 contract.

Bounded primary-review questions:

1. Is a Drunk actually in the setup?
2. Which player is selected, and what Townsfolk are they shown?
3. At that point, is the complete role/shown-role layout already fixed?
4. Is there an explicit reason for the Drunk assignment?
5. Are any other Drunk candidates explicitly considered/rejected?
6. Which later setup choices (for example Red Herring or Demon bluffs) occur after assignment?

Bounded primary review result — 2026-09-28:

- before the Drunk decision, the complete player-role layout is already fixed;
- at **03:32**, Ben commits to making the **Chef** the Drunk;
- Ben explicitly connects that assignment to a planned misinformation narrative: give the Drunk Chef a **ridiculously high number**;
- Ben also discusses Recluse, Scarlet Woman and adjacency to a Traveler as surrounding setup/context considerations;
- no other Drunk candidate participant/role is discussed in the reviewed segment;
- at **04:04**, Ben selects **Lyra as the Red Herring**, explicitly because Fortune Tellers often choose their neighbours;
- at **04:47**, Demon bluffs are assigned.

Verified setup ordering:

~~~text
complete player-role layout fixed
    ↓
03:32 Drunk assignment: Chef
    + explicit assignment rationale:
      enable a deliberately extreme Chef misinformation narrative
    ↓
04:04 Red Herring = Lyra
    ↓
04:47 Demon bluffs
~~~

Current assignment status:

- assignment result: VERIFIED;
- shown role: VERIFIED = Chef;
- assignment prefix: **PREFIX_RECONSTRUCTABLE**;
- assignment rationale: **EXPLICIT**;
- explicit alternative Drunk candidates: NONE OBSERVED;
- surrounding setup considerations: PRESENT, but must not be misclassified as rejected Drunk candidates;
- later Red Herring / bluff setup: VERIFIED as after assignment;
- replay status: **C1C REPLAY CASE 2 / 3**.

This is the first C1C historical case with explicit Drunk-assignment rationale.

Do not collapse the rationale into later misinformation execution. The evidence supports both:
1. an assignment-time reason for choosing the Chef as Drunk;
2. a planned later misinformation style (ridiculously high Chef number).

Those are related but remain separate semantic decisions.

#### C1C-G06 — An Introduction to Blood on the Clocktower — NEW P0

Primary source locator:

- YouTube video ID: `nuOq54FHDsg`;
- title: `An Introduction to Blood on the Clocktower`;
- described by contemporary BotC/TPI material as a real filmed game rather than a scripted demonstration;
- filmed with experienced Sydney players;
- Steven Medway is explicitly part of the Storyteller/production context.

Contemporary source notes give the clockwise lineup:

- Lucy — Imp;
- Misha — Virgin;
- Julian — Baron;
- Myeisha — Ravenkeeper;
- Lewis — Chef;
- **Kurt — Drunk shown Undertaker**;
- Marianna — evil Bone Collector Traveler;
- Doug — Saint;
- Fil — Washerwoman;
- Claire — Empath;
- Abdallah — Spy.

The same source notes later Drunk Undertaker misinformation materially influenced the game.

Why this is the preferred third candidate:

- exact Trouble Brewing core game with a Traveler recorded separately;
- Drunk result is already strongly identified by contemporary source material;
- creator/TPI Storyteller context gives independent coverage beyond the Ben/NRB cases;
- it is an actual historical game, not a generic setup example.

C1C primary-review questions:

1. Does the video expose the complete player-role / shown-role layout before Kurt is established as the Drunk?
2. What exact source moment establishes Kurt = Drunk shown Undertaker?
3. Is any assignment rationale stated?
4. Are any alternative Drunk participants/roles explicitly considered or rejected?
5. Which later setup commitments are visibly after the Drunk assignment?

Primary review correction — 2026-09-28:

The source is a **game introduction / illustrative explainer, not a recording of a real historical game**.

Therefore the apparent lineup and Kurt = Drunk shown Undertaker must not be treated as historical game evidence.

Disposition:

- **REJECTED — NOT A REAL GAME**;
- contributes 0 assignment replay cases;
- contributes 0 historical rationale cases;
- do not use the illustrative lineup as corpus truth.

Acquisition lesson:

A source may display a complete plausible setup while still being an instructional/example presentation. Before promoting a setup into historical evidence, confirm that the source is recording an actual played game rather than explaining the game with an illustrative configuration.

#### C1C-G07 — Trouble Brewing: Yeah Boi! — NEW P0

Primary source locator:

- YouTube video ID: `EsTXhFKtER8`;
- title: `Trouble Brewing - Yeah Boi! | TPI & Friends Play Blood on the Clocktower (in Person!)`;
- The Pandemonium Institute / TPI & Friends;
- exact script: Trouble Brewing;
- real in-person played game;
- public recommendations describe it as a compact example where experienced/expert Clocktower players are still challenged by Trouble Brewing.

Why G07 is now P0:

- source is clearly a real played game, avoiding the G06 instructional-source failure mode;
- source quality / TPI context is stronger than the remaining generic community candidates;
- it provides independent production context from the two counted Ben/NRB cases;
- the full game is under roughly one hour, so initial Drunk-presence screening should be cheap.

Current unknowns:

- whether this exact setup contains a Drunk;
- if so, selected player and shown Townsfolk role;
- whether setup construction / assignment chronology is visible;
- assignment rationale / alternatives.

Primary-access check — 2026-09-29:

- human review of the linked primary YouTube source reports the video is now **Private**;
- older public indexes still identify the episode, but they cannot substitute for an accessible primary source.

Disposition:

- **REJECTED FOR CURRENT C1C — PRIMARY SOURCE NOT PUBLICLY ACCESSIBLE**;
- contributes 0 replay cases;
- do not ask for manual review unless the primary video becomes accessible again;
- preserve the locator only as provenance history.

#### C1C-G08 — Edd Gabriel / The CLASSIC script! Trouble Brewing with a LEGEND — HOLD

Primary source locator:

- YouTube video ID: `xYrWpBH5mJM`;
- two real Trouble Brewing games in one video;
- Edd Gabriel is the Storyteller;
- public chaptering exposes game boundaries / grimoire reveals, allowing bounded screening without watching both games in full.

Current status:

- real-game status: established;
- Drunk presence: UNKNOWN;
- assignment chronology: UNKNOWN.

Current access status:

- current web search did not reliably surface the exact primary video;
- accessibility has therefore not been independently confirmed.

Disposition:

- **HOLD — DO NOT SPEND HUMAN REVIEW TIME YET**;
- retain as a lead only until the primary URL can be revalidated.

#### C1C-G09 — Dicebreaker Let's Play Blood on the Clocktower — REVIEWED

Primary source locator:

- YouTube video ID: `m9RPf8tXxR4`;
- real Trouble Brewing playthrough.

Bounded primary review result — 2026-09-29:

The visible 7-player setup is:

- Monk;
- Empath;
- Recluse;
- **Drunk shown Librarian**;
- Imp;
- Baron;
- Mayor.

The source presents the completed identity layout and then begins play. It does **not** expose the historical setup-construction sequence that selected the Librarian seat to become the Drunk.

Current assignment status:

- Drunk presence: VERIFIED;
- shown Townsfolk role: VERIFIED = Librarian;
- selected participant/seat: recoverable from the visible layout if normalized later;
- assignment prefix: **UNKNOWN / NOT PREFIX_RECONSTRUCTABLE**;
- assignment rationale: UNKNOWN;
- explicitly considered/rejected Drunk alternatives: UNKNOWN;
- replay disposition: **RESULT_ONLY — DO NOT COUNT TOWARD C1C 3-CASE QUOTA**.

Additional primary-reviewed facts:

- around **52:30**, the Empath receives `1`;
- around **53:05**, Saint is shown/confirmed as one of the Demon bluffs.

Registration-provenance note:

From the visible seating, the Empath's neighbours are compatible with the Recluse being the only apparent source of an evil registration needed for result `1`. However, unless the primary video explicitly states the registration choice, Evidence Lab must keep the historical registration witness UNKNOWN / INFERRED rather than OBSERVED. This is another useful boundary case between source evidence and downstream rules-engine explanation.

#### C1C-G10 — The Megavoid Storytelling Tips & Tricks — NEW P0

Primary source:

- YouTube video ID: `G9z25aM9u7s`;
- title: `Storytelling Tips & Tricks - BLOOD ON THE CLOCKTOWER (+ game playthrough!)`;
- current public source;
- exact focus: Storytelling Trouble Brewing;
- source description chapters:
  - 07:53 — `Who to Make Drunk`;
  - 11:22 — `Game Playthrough 1`;
  - 16:23 — `Game 2`.

Why this is useful:

- the Drunk-selection discussion is explicitly isolated into a short bounded chapter;
- the same source immediately follows with two Trouble Brewing playthrough segments;
- this creates a chance to connect stated Storyteller policy to actual game setup decisions without reviewing a long full-game video.

Current qualification note:

- The Megavoid is an independent Blood on the Clocktower Storytelling-focused creator, not TPI-affiliated;
- current community/resource indexes regularly recommend the channel for Storyteller learning;
- this is weaker qualification evidence than Steven Medway / Ben Burns and should remain separately labelled.

C1C review order:

1. verify whether the two playthrough segments are actual recorded games rather than hypothetical/simulated walkthroughs;
2. if actual, check whether either game contains a Drunk;
3. only if Drunk exists, inspect enough setup material to determine whether the apparent role layout precedes the assignment;
4. separately capture the 07:53 `Who to Make Drunk` guidance if it adds a rationale not already covered by Steven/Ben.

Bounded human review of the `Who to Make Drunk` guidance section recovered two explicit Storyteller heuristics:

1. **Topology-driven Drunk assignment**
   - example: if an Empath is sitting between two Evil players, she would probably make that Empath the Drunk;
   - evidence type: explicit Storyteller assignment guidance;
   - feature family: whole-setup topology / neighbour composition;
   - significance: direct support for setup-first assignment based on how a healthy information role would otherwise interact with the actual seating.

2. **Drunk Undertaker misinformation tied to an Evil bluff**
   - example: if the Drunk is shown Undertaker and an Evil player dies, she would probably show the Drunk Undertaker the identity that Evil player had been bluffing as;
   - evidence type: explicit impaired-information guidance;
   - feature family: public claim / bluff continuity;
   - significance: false information is chosen to reinforce an already-established social narrative rather than generated independently.

These two heuristics must remain semantically separate:

~~~text
setup topology
    -> who should become Drunk

public bluff / death context
    -> what false Undertaker identity to show later
~~~

The first adds a concrete setup-first assignment rationale. The second is longitudinal misinformation policy, not assignment rationale.

Current qualification caveat:

- this remains independent Storyteller guidance, weaker than Steven Medway / Ben Burns creator-level evidence;
- do not count either statement as a historical replay case.

Playthrough human-review checkpoint — 2026-09-29:

- **Game Playthrough 1 (11:22): NO DRUNK** in the reviewed game; screen out for C1C Drunk-assignment acquisition;
- **Game 2 (16:23): Drunk assignment is present**;
- at approximately **16:29**, the Storyteller explicitly states that because an **Empath is sitting next to the Demon**, she decides to make that Empath the Drunk;
- this is an **explicit historical assignment rationale candidate** linking local seating topology to the Drunk choice;
- do not yet promote Game 2 to `PREFIX_RECONSTRUCTABLE`: real-game status, the exact already-fixed setup state before 16:29, and the resulting assignment/prefix still require completion of the bounded human review;
- no replay-quota increment is made at this checkpoint.

Provisional Game 2 evidence shape:

~~~text
Empath adjacent to Demon
    -> explicit Storyteller rationale
    -> choose that Empath as Drunk
~~~

This historical statement is stronger than the earlier generic 07:53 Empath-between-evil guidance because it is tied to a specific playthrough decision, but replay status remains pending until the pre-assignment prefix is source-established.

Disposition:

- **GAME 1: SCREENED OUT — NO DRUNK**;
- **GAME 2: HIGH-VALUE ASSIGNMENT-RATIONALE CANDIDATE / PREFIX REVIEW IN PROGRESS**;
- current replay quota remains **2 / 3**;
- do not widen acquisition while Game 2 bounded review is still open.

### 3.2 Assignment-guidance sources

These sources improve the evidence taxonomy and tell us what to look for, but they are **not historical replay cases**.

#### C1C-A01 — Cult of the Clocktower episode 16 / Steven Medway

Source:

- `16: Drunk (Trouble Brewing) - With Clocktower Designer Steven Medway!`;
- Cult of the Clocktower;
- published 2020-04-06;
- approximately 2h27m;
- Andrew Nathenson + Steven Medway.

The episode explicitly includes a Storyteller section devoted to running the Drunk.

A prior machine-ASR pass identified candidate windows around the part discussing how to choose the Drunk. The assignment window at 01:28:18–01:29:18 has now received bounded human primary review.

C1C treatment:

- source identity/subject: verified from public episode metadata;
- machine transcript remains a locator/extraction aid;
- the 01:28:18–01:29:18 assignment claims are now **HUMAN-VERIFIED** against the original audio;
- speaker attribution for that assignment discussion is **Steven Medway**;
- reviewer reports no material assignment condition/example was omitted from the machine paraphrase;
- classification: **VERIFIED CREATOR-LEVEL ASSIGNMENT GUIDANCE / NOT_A_REPLAY_CASE**.

Do not repeat whole-episode transcription.

### A01 ASR synthesis with bounded human verification

The prior full-episode ASR produced 1,609 timestamped segments. The following windows are the high-value leads recovered from that pass.

#### 01:28:18–01:29:18 — how to choose the Drunk — VERIFIED

Human primary review confirms Steven Medway is the speaker and confirms the machine paraphrase did not omit a material assignment condition.

Steven describes three distinct Storyteller approaches:

1. choose the **player** you want to be the Drunk;
2. choose the **Townsfolk role** you want to function as the Drunk;
3. inspect the **whole setup**, then decide which player/role should become the Drunk.

C1C significance:

- this is direct conceptual support for treating Drunk assignment as an active Storyteller decision rather than a fixed template input;
- the third approach directly matches the CampBoardGameHost late-binding route: apparent role/seat context first, Drunk selection afterward;
- the first two approaches imply that assignment policy may legitimately depend on both player-level context and role-level information topology;
- no legal candidate set is implied by the podcast; legality remains downstream.

Evidence status:

- source: original podcast audio;
- speaker: Steven Medway — VERIFIED by human primary review;
- semantic paraphrase: VERIFIED as materially complete for the assignment point;
- exact wording: intentionally not preserved;
- replay status: NOT_APPLICABLE — this is creator-level guidance, not a historical game decision.

#### 01:50:01–01:52:37 — Drunk Chef

Machine-ASR lead:

- Drunk Chef misinformation should be chosen with the actual seating/setup in mind;
- the magnitude of the false Chef number matters;
- the useful false number is contextual rather than a fixed rule.

Relevance:

- strong support for assignment + misinformation coupling;
- consistent with the independently primary-verified `A Fond Farewell` case, where Ben chooses the Chef as Drunk in order to support an extreme later Chef number;
- this remains misinformation-policy guidance, not another assignment replay case.

#### 01:54:39–01:56:05 — Drunk Empath continuity

Machine-ASR lead:

- an Empath result such as `2` can create strong self-doubt;
- once a Drunk Empath receives information, the Storyteller should remember the prior information and maintain a believable multi-night narrative rather than treating each night independently.

Relevance:

- directly supports longitudinal impaired-narrative state;
- aligns with G02 Ben Burns commentary about early true information followed by sustained false information;
- this is a separate Drunk misinformation policy dimension, not assignment rationale.

#### 01:56:10–01:57:41 — Drunk Fortune Teller

Machine-ASR lead:

- Fortune Teller misinformation may not require the same kind of cross-night continuity as Empath information;
- different shown roles therefore have different narrative-memory requirements.

Relevance:

- argues against one generic “always stay numerically consistent” rule;
- supports role-semantic projection downstream rather than role-name hacks in Evidence Lab.

#### 02:04:10–02:07:39 — beginner/expert handling

Machine-ASR lead:

- some shown roles are easier for beginners to inhabit as a Drunk;
- Monk/Soldier-like roles were discussed as more beginner-friendly than Ravenkeeper-like roles.

Relevance:

- supports player-experience as a legitimate assignment feature;
- consistent with independent experienced-Storyteller guidance that assignment may change depending on whether a player is new or experienced;
- exact role preference and speaker attribution still require audio verification.

#### 02:17:37–02:22:47 — Poisoner vs Drunk control

Machine-ASR lead:

- a Poisoner actively chooses a target and therefore expresses player intent that the target should be impaired;
- the Storyteller tends to respect that player-controlled intent when deciding whether/how to provide false information;
- the Drunk differs because the Storyteller has substantially more control over the misinformation trajectory.

Relevance:

- supports keeping Poisoner corruption and Drunk misinformation in one broad impaired-information framework but with different control/lifetime semantics;
- does not affect the Drunk-assignment replay quota.

#### 02:22:58–02:24:17 — narrative-level summary

Machine-ASR lead:

- information should be chosen based on the narrative the actual game has developed rather than by evaluating a role in isolation.

Relevance:

- supports history-aware policy features;
- reinforces that Storyteller recommendation should consume committed prior observations and current game context.

### A01 review result

The C1C assignment-relevant podcast checkpoint is complete.

Verified creator-level guidance now supports three legitimate Storyteller assignment modes:

1. **player-first** — decide which player should become the Drunk;
2. **role-first** — decide which Townsfolk role should become the Drunk;
3. **setup-first** — inspect the whole setup, then decide which player/role should become the Drunk.

Architectural implication:

- CampBoardGameHost must not assume Drunk assignment is reducible to role-only scoring;
- the decision input may legitimately include player context, shown-role semantics and whole-setup topology;
- the current late-binding route is directly compatible with Steven Medway's setup-first mode;
- Evidence Lab still does not derive legal candidate sets.

The later podcast windows remain machine-ASR guidance leads for Drunk misinformation / longitudinal policy and do not block C1C assignment completion.

#### C1C-A02 — Ben Burns beginner setup guidance

A current public advice index attributes a beginner Trouble Brewing setup pattern to Ben Burns:

- establish a familiar beginner setup containing several Townsfolk;
- then select one of those Townsfolk to be the Drunk;
- the stated broad reason includes the reveal/fun value of discovering who the Drunk was.

C1C significance:

- directly supports the new CampBoardGameHost production direction that Drunk assignment can occur after the apparent Townsfolk setup exists;
- supports the semantic distinction between Drunk existence and Drunk assignment;
- provides general rationale for the assignment step.

Limit:

- this is recurring setup guidance, not one reconstructable historical game;
- it cannot satisfy the replay-case quota.

Classification: **QUALIFIED_ASSIGNMENT_GUIDANCE / NOT_A_REPLAY_CASE**.

#### C1C-A03 — experienced-Storyteller player-agency example

A 2025 public essay by an author who reports roughly 279 games played and about 170 Storyteller games gives an explicit Drunk-assignment example:

- when a new player draws Demon next to an Empath, the Storyteller may choose that Empath as the Drunk;
- with experienced players in the same geometry, the Storyteller may choose someone else;
- the stated reason is preserving the new Demon's opportunity to play/bluff rather than being immediately exposed.

C1C significance:

- clear example of assignment depending on seating, role identity and player experience;
- shows the rationale is not simply “which misinformation is easiest to fake”;
- gives a concrete feature family that CampBoardGameHost may later consume from its own state.

Limit:

- guidance/example rather than a fully reconstructable historical case;
- no legal candidate enumeration is imported;
- not counted toward replay target.

Classification: **EXPERIENCED_STORYTELLER_ASSIGNMENT_RATIONALE / NOT_A_REPLAY_CASE**.

## 4. Explicitly screened-out evidence shape

A public first-time-Storyteller Trouble Brewing report describes making the Chef Drunk after noticing Evil seated together.

This is a useful example of the evidence shape C1 wants:

~~~text
observed seating pressure
    → assignment rationale
    → selected Drunk role
~~~

However the source explicitly identifies the author as a first-time Storyteller.

Disposition:

- **REJECTED_FOR_EXPERT_CALIBRATION**;
- may remain a research lead/evidence-shape example;
- must not be counted as qualified Storyteller assignment evidence.

This preserves the existing qualification standard rather than lowering it simply because the rationale is convenient.

## 5. What C1C learned

### 5.1 The acquisition target is now narrower than “find a Drunk game”

A final grimoire with a Drunk normally gives assignment result only.

For the new SDE calibration task, the rare/high-value source surface is:

- Storyteller setup construction;
- live grimoire construction;
- setup commentary before Night 1;
- post-game commentary that explicitly reconstructs the assignment decision.

### 5.2 General expert guidance supports the new production ordering

The newly surfaced guidance is consistent with:

~~~text
choose/build apparent Townsfolk setup
    ↓
inspect player/seat/role context
    ↓
choose which Townsfolk becomes Drunk
~~~

This is useful architecture evidence.

It is not permission to rewrite any historical game's unknown prefix.

### 5.3 E0 is now the first replayable assignment case

C1B correctly treated E0 conservatively because the stored evidence did not establish assignment-time prefix membership.

The C1C bounded primary review has now established enough partial chronology:

~~~text
complete role / shown-role layout fixed
    ↓
Sullivan selected as Drunk, shown Empath
    ↓
Red Herring = Sullivan selected later
~~~

The exact internal order of role selection inside the complete layout remains UNKNOWN and is intentionally not reconstructed.

This is sufficient for the first `PREFIX_RECONSTRUCTABLE` Drunk-assignment case.

## 6. Acquisition queue

Use this order:

1. **G01 E0 — COMPLETE / REPLAY CASE 1**
   - complete role layout is verified before Drunk assignment;
   - Sullivan = Drunk shown Empath;
   - Red Herring is later;
   - assignment rationale/alternatives remain UNKNOWN.

2. **G02 Live and Imp-Person — ASSIGNMENT REVIEW COMPLETE / NOT REPLAYABLE**
   - Brooke = Drunk shown Undertaker is primary-verified;
   - no assignment rationale or alternatives;
   - source shows an already-designed setup, so the pre-assignment prefix remains UNKNOWN;
   - do not count toward the 3-case assignment quota;
   - retain Ben's explicit multi-night Drunk misinformation strategy separately.

3. **A01 Steven Medway podcast bounded assignment window**
   - verify general assignment rationale/alternatives against original audio;
   - do not count as historical replay.

4. **G03/G04 official games**
   - screen only setup/grimoire portions for Drunk presence;
   - proceed deeper only if a Drunk assignment is actually present and setup chronology is visible.

This queue is intentionally small.

## 7. Stop / escalation conditions

Do not resume broad web searching when:

- a source only exposes final role state;
- a source has no Storyteller/setup POV;
- a video requires full-game transcription merely to learn whether a Drunk exists;
- a community report has explicit rationale but no qualified Storyteller basis;
- the only way to recover prefix membership is downstream BotC legality.

Escalate a candidate to a C1 replay case only when source review establishes enough chronology for `SetupOrderBasis.EVIDENCED`.

## 8. Current C1C status

C1C has successfully produced a bounded evidence-acquisition queue and added independent assignment-rationale guidance.

It has **not yet** satisfied the full replay quota, but the first historical replay case is now complete:

- replayable Drunk-assignment cases: **2 / target 3**;
- explicit historical assignment-rationale cases: **1 / seek 1–2**;
- qualified general assignment-rationale sources: **2+**;
- G02 assignment result is verified but not prefix-reconstructable;
- G05 `A Fond Farewell` is now replay case 2 / 3 and provides the first explicit historical assignment rationale;
- G02 adds one explicit real-game Drunk misinformation strategy case, separate from the assignment quota;
- G03/G04 were screened out because they contain no Drunk.

Therefore C1C remains:

**IN PROGRESS / BOUNDED PRIMARY REVIEW REQUIRED**

This is not a reason to enter C1D.

## 9. Next checkpoint

The next C1C checkpoint is targeted acquisition of **one additional Drunk-bearing primary case** with visible setup construction.

Current quota is now 2 / 3, so broad discovery remains unnecessary. Prefer one source that adds either:
- independent Storyteller coverage; or
- another explicit assignment-rationale example.

G02 is closed for the assignment question:

- result = verified;
- prefix = unknown;
- rationale = unknown;
- assignment alternatives = unknown;
- misinformation strategy = explicit and retained separately.

Do not re-open G02 assignment chronology without a new source surface.
