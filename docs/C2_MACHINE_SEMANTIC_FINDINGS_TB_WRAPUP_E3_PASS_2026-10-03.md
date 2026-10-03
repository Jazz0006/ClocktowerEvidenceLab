# C2 Machine Semantic Findings — TB wrap-up E3-targeted pass — 2026-10-03

> Status: **MACHINE SEMANTIC REVIEW ONLY / NOT VERIFIED**
>
> Source ID: `podcast:a9357d2933f5afe3c682c30e1d09a6ff`
>
> GUID: `8d701722-2da6-40b5-8d97-419711d78fda`
>
> ASR: `small.en`, 788 timestamped segments, approximately 36 minutes.
>
> The transcript self-describes this episode as a Trouble Brewing wrap-up / material missed from prior character episodes. Full audio and ASR remain external temporary artifacts.

## Review objective

This pass intentionally applies the current Host C5 / E3 acquisition priority rather than treating every Storyteller remark equally.

Priority search:

1. non-Ben Drunk/Poison misinformation choice-over-alternatives with believability / continuity rationale;
2. Investigator/Librarian + Spy/Recluse exposure/concealment choice-over-alternatives;
3. Demon-bluff set/triplet comparison;
4. healthy-information balance with recoverable alternatives.

An E3 re-entry candidate still requires a qualified Storyteller/source, recoverable decision-time state, observed Storyteller-controlled choice, recoverable legal alternatives, explicit rationale, and a generic typed feature mapping.

## High-value machine-understood findings

### C2-TBW-M01 — Drunk Empath misinformation should be judged by the conclusion it induces, not merely by whether the number is false

**Window:** approximately `00:03:07–00:03:43` and `00:10:20–00:10:33`

Machine-understood meaning:

- the discussion notes that Empath information is unusually predictable to the Evil team;
- an obviously wrong Empath number can expose that the Empath is Drunk/poisoned and therefore fail to mislead;
- the episode explicitly references the Storyteller giving a Drunk Empath **true information** when that truth still pushes the player toward the intended wrong conclusion.

Potential downstream dimensions:

- impaired-information believability;
- recipient inference;
- Evil-side detectability;
- truthful-output-as-misinformation;
- narrative continuity.

**E3 disposition:** valuable support for the target dimension, but **not an E3 case**. The passage gives a general principle/example rather than one reconstructable observed Storyteller decision with a named alternative result and committed state. No immediate human verification is required unless a later production predicate attempts to use this passage directly.

### C2-TBW-M02 — a Drunk Investigator may already generate enough false-world pressure without additional manipulation

**Window:** approximately `00:15:03–00:15:44`

Machine-understood meaning:

- the speakers discuss an Investigator known by Evil to be Drunk because both indicated players are non-Minions;
- Evil can exploit that false world by killing one indicated player so the other looks more like the Minion;
- they also note that a Drunk Investigator may create substantial confusion on its own because both healthy players will sincerely deny being Minions.

Potential downstream dimensions:

- impaired-information strength;
- downstream narrative consequences;
- Investigator false-world persistence;
- marginal value of additional manipulation.

**E3 disposition:** not a Storyteller choice-over-alternatives case. It is primarily player/Evil strategy discussing consequences of a Drunk Investigator world.

### C2-TBW-M03 — Storyteller should support plausible bluffs consistently to avoid meta-confirming real roles or real mistakes

**Window:** approximately `00:23:20–00:25:30`

Machine-understood meaning:

- the episode gives a direct Storyteller principle: when a player is bluffing a role and behaves as if a mechanical mistake occurred, the Storyteller can respond as they would to a genuine player with that role;
- a Fortune Teller bluff example has the Storyteller act as though they accidentally failed to wake the player and put everyone back to sleep;
- a Butler bluff example similarly receives the same rules-neutral response a real Butler would receive;
- the rationale is to preserve a consistent precedent so later genuine Storyteller corrections do not confirm a player's role through meta-information.

Potential downstream dimensions:

- Storyteller speech/action neutrality;
- meta-information leakage;
- bluff support;
- operational error recovery.

**E3 disposition:** strong general Storyteller guidance but outside the current C5 choice-over-alternatives targets. It should remain machine-understood corpus material.

### C2-TBW-M04 — Slayer/Recluse registration at four alive is described as a potentially high-value Storyteller allowance

**Window:** approximately `00:33:30–00:33:49`

Machine-understood meaning:

- when four players are alive and a Slayer shoots a claimed Recluse, the speaker expects the Storyteller may often allow the Recluse to die;
- the stated reasons are both dramatic and informational: the interaction is memorable, and if it occurs it strongly confirms the Recluse/Slayer world because Scarlet Woman rescue is no longer available at four alive.

Potential downstream dimensions:

- Recluse registration;
- public information strength;
- player experience / drama;
- endgame state.

**E3 disposition:** not a reconstructable observed Storyteller decision, and the source frames it as player strategic expectation rather than an explicit Storyteller comparison among legal registration alternatives.

## Strict E3 result

**No E3 re-entry candidate was found in this episode.**

The closest current-target material is M01 because it directly addresses believable Drunk misinformation, but it lacks:

- a concrete observed Storyteller-controlled decision;
- one fixed recoverable game state;
- an explicit alternative output considered/rejected in that state.

Therefore this episode should **not** trigger bounded primary-audio verification for C5.

## Next collection priority

Continue the semantic queue, but elevate only passages with language equivalent to:

```text
I considered / could have given X,
but chose Y because ...
```

especially when the decision concerns:

1. Drunk/Poison output coherence or detectability;
2. Investigator/Librarian interaction with Spy/Recluse exposure;
3. Demon bluff set selection;
4. whole-setup healthy-information balance.

Ordinary role strategy and general Storyteller principles remain useful corpus material but should not consume E3 verification bandwidth.
