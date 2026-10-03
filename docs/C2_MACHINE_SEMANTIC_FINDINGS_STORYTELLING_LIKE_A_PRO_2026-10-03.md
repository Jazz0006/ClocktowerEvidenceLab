# C2 Machine Semantic Findings — 4.2 Storytelling Like a Pro — 2026-10-03

> Status: **MACHINE SEMANTIC REVIEW ONLY / NOT VERIFIED**
>
> Source: `4.2: Storytelling Like a Pro`
>
> Source ID: `podcast:ce72b96641813cdbacdfc3a1f4061980`
>
> GUID: `8e6b4f3f-69d7-4892-a5f3-922ce4e6d88e`
>
> ASR: `small.en`, 1,345 timestamped segments, approximately 2h10m.
>
> The complete transcript was reviewed in bounded time windows. Full audio and full ASR remain temporary external artifacts and are not committed to Git.

## High-value machine-understood findings

These findings are semantic-review candidates only. None is promoted to VERIFIED by this pass.

### C2-SLP-M01 — establish accessibility, attention, and Storyteller-contact conventions before play

**Window:** approximately `00:15:15–00:18:21`

Machine-understood meaning:

- before roles are distributed, the Storyteller can explicitly establish accessibility conventions, a shared signal for regaining group attention, and a norm that newer or script-inexperienced players should speak with the Storyteller early;
- doing this before role assignment reduces the chance that later Storyteller contact itself becomes suspicious;
- the stated rationale includes catching genuine ability misunderstandings and making later Storyteller contact feel normal.

Potential downstream dimensions:

- player experience;
- new-player handling;
- public narrative / meta suppression;
- rules-comprehension safety.

### C2-SLP-M02 — do not shortcut baseline first-night communication even with experienced players

**Window:** approximately `00:29:15–00:31:00`

Machine-understood meaning:

- a concrete game example describes the Storyteller abbreviating the normal Minion/Demon identification sequence to save time;
- the players were experienced, but the shortened presentation caused evil-team identity confusion, contributed to miscoordination, and materially affected the game;
- the speaker's takeaway is to remain consistent and explicitly deliver baseline information rather than assuming experienced players will infer it correctly.

Potential downstream dimensions:

- first-night sequencing;
- information-delivery reliability;
- cross-night consistency;
- player experience.

This is a strong operational lesson, but not evidence about character-selection ranking.

### C2-SLP-M03 — night choices should use an explicit confirmation loop

**Window:** approximately `00:32:28–00:36:37`

Machine-understood meaning:

- when a player selects another player at night, the Storyteller should confirm the intended target rather than infer a pointing gesture;
- similarly, when multiple players are meant to see one another, the Storyteller should verify that each player actually saw the required people;
- if there is doubt, wake the player again and reconfirm;
- the rationale is that a silent misread can produce catastrophic authoritative-state errors.

Potential downstream dimensions:

- authoritative commit safety;
- information-delivery reliability;
- target confirmation;
- night-state transition design.

### C2-SLP-M04 — avoid leaking hidden state through incidental night timing or physical meta

**Window:** approximately `00:39:08–00:43:02`

Machine-understood meaning:

- accidental touches, unusually long or short nights, and wake-order timing can create unintended meta-information;
- the speakers describe deliberately normalizing or varying timing when legal to reduce the reliability of these accidental signals;
- they distinguish this from legitimate player deductions based on in-game information.

Potential downstream dimensions:

- information leakage;
- timing consistency;
- meta suppression;
- hidden-state protection.

Any automated use should remain rules-safe: do not reorder actions where order is mechanically significant.

### C2-SLP-M05 — daytime listening is input to later Storyteller decisions

**Windows:** approximately `00:47:00–00:49:29` and `01:13:13–01:15:18`

Machine-understood meaning:

- during private conversations, the Storyteller should listen enough to understand what worlds and narratives players are building;
- this knowledge can inform later Storyteller-controlled information such as Savant information, Fisherman advice, and misinformation choices;
- the source also frames daytime listening as useful for understanding evil bluffs, social worlds, and the current flow of the game.

Potential downstream dimensions:

- public claims / evil narrative;
- misinformation choice;
- information strength;
- dynamic recommendation context.

This is directly relevant to the recommendation-engine design goal: current public/private narrative state can be useful enrichment context for later recommendations.

### C2-SLP-M06 — time is an active Storyteller control variable, not a fixed constant

**Window:** approximately `00:49:39–00:59:43`

Machine-understood meaning:

- day length and nomination timing are presented as active tools for controlling pace and information exchange;
- examples include allowing more time when conversations are too isolated, shortening days when coordination is becoming overly complete, varying timing by script and player count, and giving newer players more time;
- the speakers explicitly prefer adaptive timing over a rigid timer once the Storyteller has enough experience, while recommending timers as a useful novice guardrail;
- expectations should be communicated clearly and applied consistently enough that players are not stressed by unexplained timing changes.

Potential downstream dimensions:

- player experience;
- pace / game-flow state;
- public information propagation;
- player-count and experience context.

**Policy-sensitive:** do not encode specific “shorten the day when Good is connecting X information” weighting without human primary-audio confirmation and explicit product-policy review. The source contains context-dependent examples, not a universal optimization rule.

### C2-SLP-M07 — do not over-structure town discussion merely because the Storyteller can

**Window:** approximately `01:21:43–01:28:01`

Machine-understood meaning:

- all three speakers are strongly skeptical of Storyteller-run “round robin” claim sequences in which the Storyteller decides who speaks in order;
- their concern is that it transfers agency from the town to the Storyteller, changes information timing, may force evil players to claim at a Storyteller-selected moment, and can flatten which information feels important;
- if the town wants a structured claim round, it can generally self-organize one;
- the Storyteller should instead intervene narrowly when someone is not being heard.

Potential downstream dimensions:

- player agency;
- public claim timing;
- information topology;
- facilitation boundaries.

This is group-style-sensitive guidance, not a hard legality rule.

### C2-SLP-M08 — add only enough nomination structure to achieve the facilitation goal

**Window:** approximately `01:29:07–01:35:26`

Machine-understood meaning:

- the speakers describe different nomination/defense structures and do not identify one universally correct format;
- the shared goal is that relevant speakers, especially the defender, are actually heard and the game remains on pace;
- one explicit principle is to add structure only when the group needs it, and remove structure when the same goals are already being achieved organically;
- experienced Storytellers are encouraged to experiment and refine their facilitation style rather than imitate one fixed format.

Potential downstream dimensions:

- player experience;
- adaptive facilitation;
- nomination pacing;
- group-skill context.

### C2-SLP-M09 — distinguish dramatic flavor from information-bearing Storyteller speech

**Window:** approximately `01:49:14–01:49:42`

Machine-understood meaning:

- execution narration can accidentally validate or reinforce a player's claimed role;
- even when a role claim is already public, the Storyteller referencing that role in flavor can change how players interpret the claim because Storyteller speech carries authority;
- therefore flavor should avoid character-linked hints unless such signaling is deliberately rules-safe and intended.

Potential downstream dimensions:

- public narrative;
- information leakage;
- Storyteller neutrality;
- claim handling.

### C2-SLP-M10 — fake game endings can exploit informational asymmetry and damage trust

**Window:** approximately `01:49:47–01:55:52`

Machine-understood meaning:

- repeated fake endings are discouraged because they can dilute the emotional impact of the real ending;
- more importantly, a false end can cause Evil to reveal information when the game is actually continuing, for example around Scarlet Woman, Evil Twin, or Mastermind-like states;
- the speakers frame Storyteller authority as a position of trust: using privileged knowledge merely to trick players can feel different from shared dramatic storytelling;
- if an adversarial Storyteller persona is used, the group should already understand and accept that style.

Potential downstream dimensions:

- hidden-state protection;
- Storyteller trust;
- end-state communication;
- player experience.

### C2-SLP-M11 — end-game debrief should preserve player emotion before Storyteller narration

**Window:** approximately `01:56:02–02:04:45`

Machine-understood meaning:

- after the game ends, players should be allowed an initial emotional reaction before the Storyteller retakes attention;
- debrief should highlight the important causal moments rather than replay every mechanical event;
- the Storyteller can use privileged observations to create a shared narrative, for example explaining that a team that appeared dominant was actually uncertain internally;
- the speakers differ on whether winner announcement should precede or follow the story, with a general preference from some speakers for announcing the result first unless the game is unusually convoluted.

Potential downstream dimensions:

- post-game UX;
- evidence narrative;
- causal explanation;
- player experience.

Because the speakers explicitly disagree on reveal order, this item should not be converted into a single mandatory rule.

### C2-SLP-M12 — preserve decision rationale and explicitly audit mistakes after the game

**Window:** approximately `02:05:02–02:08:04`

Machine-understood meaning:

- when the Storyteller later believes a discretionary decision was wrong, the recommended practice is to explain the original rationale, acknowledge what should have been considered, and discuss the better alternative after the game;
- if the decision was reasonable from the information available at the time but happened to turn out poorly, the Storyteller need not label it a mistake merely because of the outcome;
- player feedback should be heard as part of a collaborative review rather than treated as an attack to defend against;
- the source explicitly frames this as useful critical reflection: “would you do anything differently?”

Potential downstream dimensions:

- DecisionTrace;
- replay / post-game audit;
- rationale preservation;
- outcome-bias avoidance;
- human feedback loop.

This is especially relevant to the Host / Recommendation Engine architecture: preserving decision-time context and rationale enables later quality review without judging solely from the final outcome.

## Triage

### Most directly useful to product / algorithm architecture

1. **M03 — explicit confirmation loops for authoritative night choices**
2. **M05 — player narratives as enrichment context for later Storyteller decisions**
3. **M06 — adaptive time/pace as game-state context, with policy-sensitive limits**
4. **M09 — Storyteller speech can unintentionally become information**
5. **M12 — preserve decision-time rationale for replay and post-game audit**

### Useful primarily as Storyteller UX / facilitation guidance

- M01 accessibility and pre-game conventions
- M07 round-robin / town agency
- M08 adaptive nomination structure
- M10 trust and fake endings
- M11 post-game narration

## Verification disposition

No item requires immediate human review merely to remain in the machine-understood corpus.

Human primary-audio confirmation **is required before**:

- M06 is turned into a concrete timing preference, weighting, or optimization policy;
- M07/M08 are encoded as normative facilitation rules rather than optional style guidance;
- M05 is used to justify a specific misinformation or information-strength choice in production;
- any item is promoted to VERIFIED evidence.

The temporary full audio and ASR workspace may be cleaned after this lightweight record is safely committed.
