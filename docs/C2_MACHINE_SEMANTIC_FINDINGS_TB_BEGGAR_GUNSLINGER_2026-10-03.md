# C2 Machine Semantic Findings — Beggar + Gunslinger — 2026-10-03

> Status: **MACHINE SEMANTIC REVIEW ONLY / NOT VERIFIED**
>
> Source: `Beggar and Gunslinger (Trouble Brewing Travelers Part 1)`
>
> Source ID: `podcast:aa0aef8a9fe8a32d9690734f2f0e7bc2`
>
> GUID: `ff9272cb-c6d4-4db0-8678-7caaaf1c946e`
>
> ASR: `small.en`, 1,662 timestamped segments, approximately 1h27m.
>
> The complete transcript was reviewed in bounded windows. Full audio and full ASR remain temporary external artifacts and are not committed to Git.

## High-value machine-understood findings

These are semantic-review candidates only. None is promoted to VERIFIED by this pass.

### C2-BG-M01 — Traveler alignment choice should consider current team state, not only default alignment frequency

**Window:** approximately `00:05:30–00:07:37`

Machine-understood meaning:

- the speakers discuss that most Travelers may generally be Good, but Storytellers often consider which team is currently struggling when assigning an arriving Traveler;
- a first Traveler may reasonably be Evil when Evil is already under pressure;
- with multiple Travelers, Storytellers may also think about whether the new Traveler counterbalances the alignment or impact of earlier Travelers;
- the discussion is explicitly contextual and partly theory-crafting, not a universal ratio rule.

Potential downstream dimensions:

- Traveler alignment recommendation;
- current team-state context;
- multi-Traveler interaction;
- balance intervention.

**Policy-sensitive:** do not encode a fixed “losing team gets the Traveler” rule without human confirmation and explicit product-policy review.

### C2-BG-M02 — Traveler role choice should account for intrinsic game-state impact, not only player preference

**Windows:** approximately `00:08:26–00:11:19`, `00:43:05–00:43:48`, and `01:25:20–01:26:55`

Machine-understood meaning:

- Beggar is described as relatively low-impact on arrival compared with Gunslinger, Thief, Bureaucrat, or Scapegoat;
- the speakers repeatedly distinguish Travelers by how strongly they reshape voting, information, or endgame structure;
- a Storyteller need not offer every Traveler as a free player choice;
- instead, the Storyteller can preselect a bounded set of roles that fit the current game and then allow the player to choose within that set;
- when multiple Travelers arrive, the Storyteller can choose the set of Traveler roles first, then let the players decide who receives which one.

Potential downstream dimensions:

- Traveler role-assignment recommendation;
- role impact / swing profile;
- bounded player choice;
- current-game compatibility.

This is directly relevant to a future Traveler-assignment decision type.

### C2-BG-M03 — Beggar has an implicit voting-math bias that can help Evil even when the Beggar is Good

**Windows:** approximately `00:24:28–00:29:18` and `01:24:23–01:25:19`

Machine-understood meaning:

- Beggar adds another living player to the execution threshold while beginning without a vote;
- in some player-count states this means Good needs one additional Good voter to reach the execution threshold;
- the speakers therefore describe Beggar as having an intrinsic tendency to help Evil through voting math, independently of the Beggar's alignment;
- a Good Beggar who fails to acquire vote tokens may eventually be helping Good more by accepting exile than by remaining alive without voting power.

Potential downstream dimensions:

- Traveler role impact;
- voting-math projection;
- current player count;
- alignment-independent role bias.

This is a strong candidate for an explicit `role_effect_profile` or similar enrichment feature rather than a simple alignment label.

### C2-BG-M04 — registration choices should consider which result preserves the intended team pressure

**Windows:** approximately `00:21:04–00:24:12` and `00:37:13–00:38:04`

Machine-understood meaning:

- the episode discusses both Recluse and Spy interactions with Beggar alignment information;
- a concrete game example has an Evil Beggar receive a dead Spy's vote token;
- although Spy could register as Good, the Storyteller chose to show the Spy as Evil because showing Good could encourage the Evil Beggar to publicly accuse the Spy of being Evil, inadvertently harming the Evil team;
- the rationale is not “always misregister Spy/Recluse,” but to choose registration with awareness of how the information will interact with the recipient's incentives and the wider game narrative.

Potential downstream dimensions:

- registration;
- misinformation choice;
- recipient alignment/incentives;
- downstream narrative effects.

This is directly relevant to recommendation logic that evaluates consequences of multiple legally valid registration outcomes.

### C2-BG-M05 — Traveler seat and arrival timing can alter existing information roles

**Window:** approximately `00:44:00–00:46:12`

Machine-understood meaning:

- Traveler seating can interfere with Empath information by inserting a Traveler next to the Empath;
- the speakers prefer not to use seating conventions that would themselves confirm the Empath;
- one idea discussed is to let the Traveler select a seat before alignment is finalized, leaving the Storyteller some room to account for the resulting information topology;
- the discussion does not reach a single mandatory rule.

Potential downstream dimensions:

- seating / adjacency context;
- Traveler alignment;
- information-role preservation;
- anti-meta constraints.

**Ambiguous / policy-sensitive:** this should remain machine-only until a concrete production rule is considered.

### C2-BG-M06 — Gunslinger is highly swingy; adding one mid-game is materially different from starting with one

**Windows:** approximately `00:48:26–00:53:53` and `01:22:50–01:25:19`

Machine-understood meaning:

- Gunslinger is described as unusually powerful because it adds additional player deaths controlled through public voting;
- a mid-game arrival is considered much more disruptive than a Gunslinger present from the start because claims, bluffs, and candidate worlds have already narrowed;
- one speaker says they are much more willing to start a game with Gunslinger than add one after several days;
- the episode also characterizes Gunslinger as an “amplifier”: if Good's model of the game is accurate, Gunslinger can make Good much stronger; if Good is badly wrong, a Good Gunslinger may accelerate Good's collapse.

Potential downstream dimensions:

- Traveler role choice;
- arrival timing;
- town belief quality;
- role swing / amplification profile.

This strongly supports modeling Traveler choice as `current state × role swing profile × player belief quality`, rather than only “which team needs help.”

### C2-BG-M07 — Storyteller should constrain Gunslinger decision time to preserve role balance and game pace

**Window:** approximately `01:20:13–01:21:21`

Machine-understood meaning:

- after the first vote, the Storyteller should keep the eligible target set mechanically clear;
- a short amount of town discussion can be useful, but extended whole-town debate around the Gunslinger choice is described as harmful to pacing and as giving Good excessive analysis time;
- the speakers recommend keeping pressure on the Gunslinger to choose rather than allowing the decision to become a long collective solve.

Potential downstream dimensions:

- timing / pace;
- public decision UX;
- role balance;
- authoritative action resolution.

**Policy-sensitive:** exact time limits such as 10–30 seconds should not be encoded without human primary-audio confirmation; the useful principle is bounded decision time, not a universal fixed duration.

### C2-BG-M08 — Storyteller introduction framing can itself bias how a Traveler is perceived

**Window:** approximately `00:40:39–00:42:38`

Machine-understood meaning:

- because Traveler abilities are not necessarily familiar to all players, the Storyteller often explains the role when it enters play;
- the wording and tone of that explanation can make the Traveler ability sound strongly pro-Good, optional, threatening, or harmless;
- the speakers explicitly note that this gives the Storyteller influence over how the table initially perceives the Traveler;
- the recommended stance is awareness and clarity rather than deliberately manipulating that perception.

Potential downstream dimensions:

- Storyteller speech neutrality;
- public narrative;
- onboarding / role explanation;
- information leakage.

## Triage

### Most directly useful to product / algorithm architecture

1. **M02 — Traveler role assignment should use a bounded candidate set selected for the current game**
2. **M03 — model intrinsic role impact separately from Traveler alignment**
3. **M04 — registration alternatives should be evaluated by downstream recipient/narrative consequences**
4. **M06 — Traveler choice depends on arrival timing and current town belief quality, not only team balance**
5. **M07 — decision-time pacing is part of role balance**

### Likely new Recommendation Engine decision surface

A future `TRAVELER_ASSIGNMENT` recommendation request could plausibly use:

- current player count and alive/dead state;
- current Good/Evil performance or uncertainty;
- current public claims / world state;
- current Traveler set and alignments;
- candidate Traveler role impact profile;
- expected player stay duration;
- seating / adjacency effects;
- player experience level;
- whether the Traveler is arriving late versus present from game start.

The output should be candidate Traveler roles/alignment options with reasons, not an unconditional global ranking.

## Verification disposition

No item above requires immediate human review merely to remain in the machine-understood corpus.

Human primary-audio confirmation **is required before**:

- M01 becomes an alignment-balancing policy;
- M04 is used to justify a specific production registration preference;
- M05 is used to create an alignment rule from seating;
- M06 is converted into a concrete Traveler-role ranking;
- M07 is turned into a fixed decision timer;
- any item is promoted to VERIFIED evidence.

The temporary full audio and ASR workspace may be cleaned after this lightweight record is safely committed.
