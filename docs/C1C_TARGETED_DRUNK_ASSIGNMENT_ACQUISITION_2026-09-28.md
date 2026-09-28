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

Current status:

- assignment result: strong secondary reconstruction lead;
- full layout: strong secondary reconstruction lead;
- assignment prefix: UNKNOWN;
- assignment rationale: UNKNOWN;
- next action: **BOUNDED_PRIMARY_SETUP_REVIEW_REQUIRED**.

Do not import the fan recap as primary chronology.

#### C1C-G03 — official Trouble Brewing October 2019 Game 2 — P2

Primary source:

- official Blood on the Clocktower YouTube channel;
- video ID: `pVzZms1FTr4`;
- 8-player Trouble Brewing;
- Storyteller: Steven Medway.

This is a high-value independent-Storyteller primary candidate.

Current indexed metadata verifies the game identity, script, player count and Storyteller, but the current search surface has not established:

- whether a Drunk is in this exact setup;
- selected Drunk participant;
- shown Townsfolk role;
- assignment chronology.

Disposition:

- **PRIMARY_CANDIDATE / DRUNK_PRESENCE_NOT_YET_ESTABLISHED**;
- perform only a bounded setup/grimoire review if G01/G02 do not close enough of the replay target.

#### C1C-G04 — official Trouble Brewing October 2019 Game 1 — P2

Primary source:

- official Blood on the Clocktower YouTube channel;
- video ID: `2TlW06GVF8I`;
- 7-player Trouble Brewing;
- Storyteller: Jon Gjengset.

As with G03, current indexed metadata verifies game identity, script, player count and Storyteller but not Drunk presence/assignment.

Disposition:

- **PRIMARY_CANDIDATE / DRUNK_PRESENCE_NOT_YET_ESTABLISHED**;
- lower priority than G01/G02 because it first requires screening for whether the required evidence shape exists.

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

A prior machine-ASR pass identified candidate windows around the part discussing how to choose the Drunk, but that machine transcript remains `HUMAN_REVIEW_PENDING`.

C1C treatment:

- source identity/subject: verified from public episode metadata;
- prior machine transcript: locator aid only;
- detailed assignment claims: do not promote until checked against original audio;
- classification: **QUALIFIED_GUIDANCE / NOT_A_REPLAY_CASE**.

Do not repeat whole-episode transcription. If reviewed, use only the already-identified bounded assignment window.

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

2. **G02 Live and Imp-Person bounded setup review**
   - known Drunk = Brooke / shown Undertaker;
   - full layout already available as a secondary lead;
   - review only the setup-construction section first.

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

- replayable Drunk-assignment cases: **1 / target 3**;
- explicit historical assignment-rationale cases: **0 / seek 1–2**;
- qualified general assignment-rationale sources: **2+**;
- remaining high-value bounded historical game candidates: G02 immediate + G03/G04 secondary.

Therefore C1C remains:

**IN PROGRESS / BOUNDED PRIMARY REVIEW REQUIRED**

This is not a reason to enter C1D.

## 9. Next checkpoint

The next C1C checkpoint is **G02 — Live and Imp-Person**.

Review only the setup-construction section and answer:

1. Is the complete apparent role / shown-role layout already fixed before Brooke is selected as the Drunk?
2. What exact source moment establishes Brooke = Drunk shown Undertaker?
3. Is any assignment rationale stated?
4. Are any alternative Drunk participants/roles explicitly considered or rejected?
5. Which setup choices are demonstrably after assignment?

Do not use the secondary recap to manufacture chronology. If the primary source does not establish prefix membership, retain the case as partial and move to the next bounded candidate.
