# C2 Machine Semantic Findings — Mayor — 2026-10-04

> Status: **MACHINE SEMANTIC REVIEW ONLY / NOT VERIFIED**
>
> Source: `Mayor (Trouble Brewing)`
>
> Source ID: `podcast:37c46be5c4807ffbe17c286f8c7ab647`
>
> GUID: `96b42f2d-0e28-0a7c-10ac-15cdfe85c9af`
>
> ASR: `small.en`, 3,403 timestamped segments, approximately 71 minutes.

This full-episode pass reviewed all 3,403 ASR segments. It prioritizes Storyteller-controlled Mayor-bounce decisions, Drunk selection, setup information density, player-experience calibration, final-three risk structure and Minion counterplay.

## High-value machine-understood findings

### C2-MAYOR-M01 — Mayor bounce should usually redirect the Demon kill, not simply erase it

**Window:** approximately `00:04:16–00:05:44`

Machine-understood meaning:

- the speakers distinguish the intended feel of Mayor from a generic “night kill immunity” effect;
- they prefer interpreting the ability as redirecting the Demon’s attack to another player rather than routinely nullifying a kill through a protected/dead target;
- even when rules permit a no-death result through Soldier/Monk protection, the Storyteller should think about whether that produces the intended interaction rather than maximizing protection mechanically.

Potential downstream dimensions:

- role intent;
- interaction quality;
- kill-redirection value;
- protected-target choice;
- rules legality vs recommended play.

**E3 disposition:** generic policy guidance, not a historical same-state choice.

### C2-MAYOR-M02 — Mayor bounce should usually make the Demon pay for targeting Mayor

**Windows:** approximately `00:20:19–00:22:19` and `00:54:14–00:58:19`

Machine-understood meaning:

- unless there is a strong reason to let Mayor die, the default entertainment/policy preference is to preserve Mayor and redirect the kill;
- the speakers describe the Demon’s Mayor target as a choice that should usually have a meaningful cost;
- possible targets include a Minion, an already-spent or lower-value Good character, Ravenkeeper, Outsider, Soldier/Monk-protected target, or in some game states a stronger Good character;
- the best target depends on the current state rather than a fixed priority list.

Potential downstream dimensions:

- Demon-choice consequence;
- target utility;
- Good/Evil current strength;
- role remaining value;
- experiential payoff.

**E3 disposition:** strong bounded decision-policy guidance, but no historical complete candidate domain.

### C2-MAYOR-M03 — Mayor bounce target should adapt to current team strength, not always help Good maximally

**Window:** approximately `00:57:11–00:58:19`

Machine-understood meaning:

- if Evil has already lost both Minions early and is struggling, the Storyteller may let Mayor die or redirect onto a valuable Good player;
- in a less lopsided state, redirecting onto Evil, Ravenkeeper, an Outsider, or a spent first-night role may be more appropriate;
- protected targets can function as a comparatively neutral outcome;
- Mayor bounce therefore behaves like a state-sensitive balancing lever, but not an instruction to always rescue the weaker team.

Potential downstream dimensions:

- current team strength;
- remaining role value;
- target alignment;
- neutral vs swingy redirect;
- intervention strength.

**E3 disposition:** generic adaptive policy; no strict historical E3.

### C2-MAYOR-M04 — repeated Demon attacks on Mayor should be interpreted through intent/persistence, not a rigid retry rule

**Window:** approximately `00:54:55–00:56:23`

Machine-understood meaning:

- if the Demon repeatedly targets Mayor carelessly after already learning the likely interaction, the speakers lean toward continuing to punish that mistake with further bounces;
- if repeated targeting is clearly a deliberate strategic commitment and Evil is willingly spending multiple nights to remove Mayor, the Storyteller may eventually allow the kill;
- Storyteller policy should therefore distinguish repeated error from intentional investment.

Potential downstream dimensions:

- inferred player intent;
- repeated-action history;
- strategic commitment;
- learning from prior result;
- consequence consistency.

**E3 disposition:** strong policy principle, not a fixed historical case.

### C2-MAYOR-M05 — Drunk Mayor is player-experience sensitive: avoid it for beginners, but it can be fair for experienced groups

**Window:** approximately `00:51:18–00:52:48`

Machine-understood meaning:

- for beginner games, Roger recommends against making Mayor the Drunk because the deduction burden around Mayor/Poisoner/Drunk interactions is difficult;
- with experienced players who understand how to reason about impairment and Outsider counts, Drunk Mayor is considered fair;
- if Drunk Mayor is attacked at night, simply dying may itself provide a clue that they were impaired, so the weakening does not always remain invisible until final three.

Potential downstream dimensions:

- player experience;
- rules literacy;
- deduction burden;
- failure discoverability;
- beginner suitability.

**E3 disposition:** direct player-level policy guidance; not historical.

### C2-MAYOR-M06 — Mayor is a strong candidate for late-bound Drunk when seating creates excessive confirmation

**Window:** approximately `00:52:49–00:54:13`

Machine-understood meaning:

- the episode explicitly discusses choosing which Townsfolk is Drunk after the setup/seating is known;
- Andrew says he has heard official Storytellers recommend this timing because it allows the Storyteller to craft a better game without changing what players perceive at setup;
- concrete example: Mayor sits next to Empath whose other neighbor is Good; truthful Empath `0` strongly confirms Mayor and can create an overly easy Mayor path;
- one proposed response is to make Mayor the Drunk (or impair the Empath) to break the confirmation chain.

Potential downstream dimensions:

- setup-first Drunk binding;
- seat topology;
- confirmation-chain strength;
- Mayor endgame power;
- alternative impairment target.

**E3 disposition:** highly relevant supporting evidence for late-bound Drunk selection, but the recommendation is reported second-hand and hypothetical; do not promote automatically.

### C2-MAYOR-M07 — Washerwoman confirming Mayor can over-compress the game

**Window:** approximately `00:58:52–01:00:07`

Machine-understood meaning:

- if Washerwoman directly identifies Mayor, Mayor becomes both highly trusted and effectively knows they are not Drunk;
- the speakers consider that combination potentially too strong unless other setup elements, such as Poisoner or another Evil countermeasure, offset it;
- preferred default is often to keep Washerwoman in the game but show some other Townsfolk rather than Mayor.

Potential downstream dimensions:

- confirmation-strength budgeting;
- Mayor trust;
- Drunk exclusion;
- pair-information target choice;
- setup-wide counterplay.

**E3 disposition:** explicit candidate preference over another legal Washerwoman target class, but no historical complete same-state domain.

### C2-MAYOR-M08 — Investigator is a “moderate-strength” Mayor partner; Empath can become too confirmatory

**Window:** approximately `01:00:28–01:01:46`

Machine-understood meaning:

- Investigator is favored as a useful Mayor companion because information about whether Poisoner may be present helps Mayor reason about final-three safety without directly hard-confirming Mayor;
- Empath can become much stronger if seated next to Mayor and another Good player, because `0` may heavily confirm Mayor;
- the Storyteller should not necessarily exclude Empath, but should recognize the resulting confirmation chain and compensate if needed.

Potential downstream dimensions:

- information density;
- direct vs indirect confirmation;
- Poisoner detectability;
- seat topology;
- setup compensation.

**E3 disposition:** qualitative setup-ranking guidance.

### C2-MAYOR-M09 — Undertaker/Librarian/Chef/Ravenkeeper can change Mayor reliability by proving impairment structure

**Windows:** approximately `00:39:13–00:41:31` and `01:02:12–01:04:30`

Machine-understood meaning:

- Mayor’s actual strength depends heavily on whether town can establish that Poisoner is gone and whether Mayor is or is not Drunk;
- Undertaker can confirm executed Poisoner, Baron, Scarlet Woman or the Drunk and therefore narrow the impairment model;
- Librarian can identify another Drunk candidate and indirectly clear Mayor, or create ambiguity if Mayor is among the shown pair;
- Chef information can constrain final-three worlds based on adjacency;
- Ravenkeeper can confirm Mayor or serve as a high-value bounce target.

Potential downstream dimensions:

- impairment-model certainty;
- role-network topology;
- final-three world count;
- cross-role confirmation;
- bounce-target utility.

**E3 disposition:** system-level information-network guidance.

### C2-MAYOR-M10 — one-Minon Mayor setups should account for which Minion can actually counter Mayor

**Window:** approximately `01:05:28–01:10:46`

Machine-understood meaning:

- Poisoner directly disables Mayor;
- Baron can introduce Drunk uncertainty, and the speakers favor including a Drunk when Mayor and Baron coexist because uncertainty alone weakens Mayor confidence;
- Spy can identify Mayor immediately and actively undermine trust or manipulate Outsider count;
- Scarlet Woman has the weakest direct answer to Mayor: if town trusts Mayor, Demon uncertainty may not matter because Good can win by no execution;
- therefore a one-Minion setup with Mayor + Scarlet Woman may warrant extra ambiguity (for example a Drunk) and less direct Mayor confirmation from Empath/Washerwoman/Undertaker-style networks.

Potential downstream dimensions:

- Minion capability coverage;
- Mayor counterplay;
- Outsider uncertainty;
- setup synergy;
- one-Minion fragility.

**E3 disposition:** strong setup-composition policy, not historical.

### C2-MAYOR-M11 — real final-three poisoned-Mayor loss demonstrates a conditional risk chain, not a blanket anti-Mayor rule

**Window:** approximately `00:31:45–00:39:13`

Observed game narrative:

- a real Mayor was broadly trusted by town;
- the game reached final three;
- the Poisoner was still alive and poisoned Mayor on the preceding night;
- town chose no execution expecting the Mayor win;
- Mayor ability failed and Evil won.

Machine-understood lesson:

- the failure required Poisoner survival, correct target knowledge/timing, Mayor trust, and town acceptance of no execution;
- the speakers explicitly reject the simplistic conclusion that Mayor is therefore “bad” or unusable;
- this episode frames Mayor risk as conditional and reconstructable through game-state evidence.

Potential downstream dimensions:

- Poisoner alive;
- Mayor trust;
- final-three state;
- impairment confidence;
- risk-chain completeness;
- player experience/meta learning.

**E3 disposition:** concrete historical evidence, but the decisive poisoning choice belongs to the Evil player rather than Storyteller; useful for state/risk modeling, not strict Storyteller E3.

### C2-MAYOR-M12 — player experience and local meta change both Mayor setup value and Mayor bluff value

**Windows:** approximately `00:15:03–00:18:36`, `00:35:02–00:38:32`, and `00:42:02–00:47:58`

Machine-understood meaning:

- a group’s first failed Mayor attempt materially changed how players evaluated the role until later games corrected that impression;
- Mayor bluff strength also depends on whether the local meta already expects Evil to claim Mayor;
- experienced groups can reason about Poisoner/Drunk failure modes that beginners may treat as arbitrary;
- therefore player experience and local meta are relevant enrichment context both for setup construction and runtime recommendation.

Potential downstream dimensions:

- player level;
- local meta;
- prior group experience;
- bluff credibility;
- risk tolerance.

**E3 disposition:** qualitative context guidance.

## Strict E3 result

**No new strict E3 PASS is admitted from this episode.**

The strongest Storyteller-choice leads are:

1. **M06** — late-bound Drunk Mayor vs alternative impairment when seating creates an excessive Empath confirmation chain;
2. **M07** — avoid using Washerwoman to directly confirm Mayor unless the setup contains enough counter-pressure;
3. **M02/M03** — choose Mayor bounce target from current role value and team state rather than a fixed target ranking;
4. **M10** — choose Mayor-compatible Minion/setup structure based on whether Evil has credible Mayor counterplay.

However, these are generic/hypothetical policy discussions rather than one historical Storyteller decision with a fully recoverable exact state, legal candidate domain, committed outcome and same-state rejected alternatives.

## Product-facing triage

Most useful for future recommendation work:

1. **M05/M12** — player level should directly affect Drunk-Mayor suitability and explanation burden;
2. **M06** — late-bound Drunk assignment should consume seating/confirmation topology;
3. **M07/M08/M09** — Mayor strength is strongly multiplicative with confirmation networks, so setup evaluation must be global rather than per-role;
4. **M02/M03/M04** — Mayor bounce needs state, target utility, repeated-action history and inferred Demon intent;
5. **M10** — Minion selection should consider capability coverage against alternate win conditions, not only raw nominal power;
6. **M11** — final-three Mayor risk should be represented as a condition chain, not a fixed role penalty;
7. **M01** — rules legality and role-intent policy remain distinct.

No immediate primary-audio review is requested. The episode is especially valuable for recommendation-feature design, but no current Host production gate depends on promoting these findings to VERIFIED.
