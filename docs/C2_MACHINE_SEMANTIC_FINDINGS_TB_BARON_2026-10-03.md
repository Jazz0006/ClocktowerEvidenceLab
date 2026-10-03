# C2 Machine Semantic Findings — Baron — 2026-10-03

> Status: **MACHINE SEMANTIC REVIEW ONLY / NOT VERIFIED**
>
> Source: `Baron (Trouble Brewing)`
>
> Source ID: `podcast:e6854a67b728314eeb50dd7f0612eae6`
>
> GUID: `bd0cc82b-5fb6-4053-acb1-038f5b2493a6`
>
> ASR: `small.en`, 3,018 timestamped segments, approximately 66 minutes.
>
> Guest context recovered from the episode: Andrew Conant describes having played roughly 84 games, with approximately 50 as Storyteller. He is not introduced as an official Storyteller.

This pass prioritizes Storyteller-controlled setup decisions: whether to include Baron, player-count effects, which Outsiders to add, Drunk frequency, anti-meta variation, and player-experience considerations.

## High-value machine-understood findings

### C2-BARON-M01 — Baron power scales sharply with player count because the same +2 Outsiders replace a larger fraction of Townsfolk in small games

**Window:** approximately `00:52:52–00:54:16`

Machine-understood meaning:

- the speakers identify the primary Storyteller decisions around Baron as whether to include it and, if so, which Outsiders to add;
- they caution that Baron is especially strong in 5–6 player games;
- in a 6-player game, Baron's +2 changes roughly one third of the character composition, while the proportional effect is much smaller in a 15-player game;
- with only one Townsfolk left in a small Baron game, that Townsfolk may need to carry unusually high informational weight, making the game more swingy if that player dies early.

Potential downstream dimensions:

- player count;
- setup-strength budget;
- Townsfolk information density;
- swinginess / fragility;
- Minion impact as a fraction of setup.

**E3 disposition:** generic setup guidance; no fixed historical decision-state comparison.

### C2-BARON-M02 — Baron can be useful to introduce Outsider gameplay at zero-native-Outsider counts, but predictable repeated use creates Storyteller meta

**Window:** approximately `00:54:30–00:55:42`

Machine-understood meaning:

- in counts such as 7 or 10 where the base setup can contain no Outsiders, Baron is described as an enjoyable way to bring the Outsider layer into the game;
- however, repeatedly adding Baron whenever the native count is zero would make the setup pattern predictable;
- one speaker explicitly notes that his players may already be able to meta him because he personally prefers setups containing Outsiders.

Potential downstream dimensions:

- native Outsider count;
- content diversity / experience variety;
- anti-meta variation;
- Storyteller historical tendency.

**E3 disposition:** generic anti-meta setup guidance only.

### C2-BARON-M03 — vary which Outsiders appear; the mere possibility of Drunk can generate uncertainty even when Drunk is absent

**Window:** approximately `00:56:49–00:58:08`

Machine-understood meaning:

- the speakers recommend spreading Outsider selections across games rather than repeatedly choosing the same subset;
- Drunk is specifically called out as tempting to include because it has many interesting interactions;
- nevertheless, they argue that the *possibility* of Drunk already changes player interpretation, so an actual Drunk is not required every time to create useful uncertainty;
- deliberately omitting Drunk can subvert group expectations and prevent the Storyteller from teaching a fixed Baron→Drunk association.

Potential downstream dimensions:

- Outsider composition diversity;
- Drunk presence/absence;
- anti-meta value;
- latent uncertainty;
- historical frequency balancing.

**E3 disposition:** strong setup-policy feature support, but not a fixed same-state candidate comparison.

### C2-BARON-M04 — underusing Butler can itself create a meta leak

**Windows:** approximately `00:42:04–00:44:13` and `00:56:49–00:58:08`

Machine-understood meaning:

- both speakers discuss a tendency for Storytellers to use Butler less often because its interactions are less directly controlled by the Storyteller;
- they explicitly argue that Butler still needs to appear often enough to avoid a predictable setup distribution;
- if a group learns that Butler is rarely selected, Baron/Outsider deduction becomes easier and certain Evil outsider bluffs become safer.

Potential downstream dimensions:

- role-frequency meta;
- Outsider selection diversity;
- Storyteller control preference;
- bluff-space preservation.

**E3 disposition:** generic anti-meta guidance.

### C2-BARON-M05 — four-Outsider Baron setups can collapse an important uncertainty dimension once Baron is inferred

**Window:** approximately `00:58:30–00:59:29`

Machine-understood meaning:

- in a player count with two native Outsiders, adding Baron puts all four Trouble Brewing Outsiders into play;
- one speaker says he generally dislikes this shape because once players identify Baron, there is no remaining uncertainty about *which* Outsiders are absent;
- the concern is not raw legality but information ecology: the setup itself has revealed an entire category of possibilities.

Potential downstream dimensions:

- Outsider-composition uncertainty;
- information-space compression;
- setup transparency;
- player count / native Outsider count.

**E3 disposition:** explicit preference and rationale, but not tied to a reconstructable historical fixed setup.

### C2-BARON-M06 — Baron may be a poorer first-game Minion assignment for inexperienced players because its power is passive and its fun depends on bluffing skill

**Window:** approximately `01:02:49–01:04:20`

Machine-understood meaning:

- the speakers distinguish experienced players, who can exploit Baron's freedom to make creative bluffs, from first-time players who may feel they have "nothing to do";
- unlike Poisoner, Baron offers no recurring mechanical action that makes its impact immediately legible to a novice;
- they therefore suggest Baron may be a less effective Minion choice when the Storyteller is deliberately optimizing for a strong first-player experience.

Potential downstream dimensions:

- player experience;
- role comprehensibility;
- agency visibility;
- first-game enjoyment;
- assignment suitability.

**E3 disposition:** strong player-experience setup guidance; no specific historical candidate comparison.

### C2-BARON-M07 — setup construction should preserve possibility-space rather than maximize one favorite interaction repeatedly

**Windows:** approximately `00:55:30–00:59:29`

Machine-understood meaning:

- both speakers repeatedly frame Clocktower as a game of possibilities;
- favorite interactions such as Drunk or Recluse can tempt a Storyteller into recurring patterns;
- they recommend preserving diversity in Outsider combinations so players cannot solve the setup through Storyteller habits;
- this supports treating anti-meta diversity as a first-class setup consideration rather than an afterthought.

Potential downstream dimensions:

- possibility-space preservation;
- anti-meta;
- setup diversity;
- repeated-pattern penalty.

**E3 disposition:** generic setup-design guidance.

### C2-BARON-M08 — the Storyteller's Baron decisions are concentrated before play: Minion inclusion and Outsider composition are the high-leverage controls

**Window:** approximately `00:52:23–00:53:14`

Machine-understood meaning:

- unlike characters with recurring Storyteller choices, Baron does most of its work at setup;
- the episode explicitly reduces the main Storyteller decisions to whether Baron enters the setup and which Outsiders its ability introduces;
- this is useful architectural evidence that Baron recommendations belong primarily to setup-time recommendation state rather than night-by-night runtime policy.

Potential downstream dimensions:

- decision timing;
- setup-time vs runtime control;
- candidate-domain ownership;
- recommendation-state phase.

**E3 disposition:** architecture/decision-shape support, not ranking evidence.

### C2-BARON-M09 — Storyteller objective includes player experience, not merely maximizing Evil mechanical strength

**Window:** approximately `01:04:20–01:05:15`

Machine-understood meaning:

- the speakers explicitly frame the Storyteller as an impartial facilitator whose objective is to create an entertaining experience;
- they describe "everyone having fun" and reaching an interesting final three as useful success signals;
- this contextualizes the earlier advice not to choose Baron solely because it is mechanically powerful when a novice player may have a poor experience with its passive role.

Potential downstream dimensions:

- player enjoyment;
- game trajectory;
- final-three quality;
- mechanical strength vs experience tradeoff.

**E3 disposition:** broad Storyteller objective guidance; not suitable by itself for numeric policy weighting.

## Strict E3 result

**No new E3 PASS is admitted from this episode.**

The strongest product-facing material is setup-policy guidance rather than a reconstructable historical same-state decision. In particular:

- **M01** gives a clear player-count-dependent Baron strength concern;
- **M03** gives explicit Drunk-presence anti-meta guidance;
- **M05** gives an information-compression rationale against routinely using the all-four-Outsiders Baron shape;
- **M06** gives player-experience-sensitive Minion assignment guidance.

None of those sections provides the full committed state, legal alternative domain, observed selected candidate, and historical choice-over-alternatives rationale required for strict E3 re-entry.

## Product-facing triage

Most useful for future recommendation work:

1. **M01** — scale setup-strength budget by player count;
2. **M03** — Drunk should not be a default Baron add; absence itself preserves uncertainty and suppresses meta;
3. **M05** — all-four-Outsiders can over-compress setup possibilities;
4. **M06** — Baron assignment should account for player experience and visible agency;
5. **M04/M07** — role-frequency and composition diversity matter because Storyteller habits become exploitable;
6. **M08** — Baron is primarily a setup-time recommendation problem.

No immediate human primary-audio review is requested unless Host opens a bounded gap around Baron setup strength, Outsider composition, player-experience-sensitive role assignment, or anti-meta setup diversity.
