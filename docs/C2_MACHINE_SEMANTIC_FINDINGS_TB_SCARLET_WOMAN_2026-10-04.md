# C2 Machine Semantic Findings — Scarlet Woman — 2026-10-04

> Status: **MIXED — M02 PRIMARY-AUDIO HUMAN REVIEWED; OTHER FINDINGS REMAIN MACHINE SEMANTIC / NOT VERIFIED**
>
> Source: `Scarlet Woman (Trouble Brewing)`
>
> Source ID: `podcast:f032267028e0b2aae8c51bc74097d6e7`
>
> GUID: `7318fc50-8468-2822-eb62-22cae200d644`
>
> Guest: official Storyteller / rules-focused contributor John
>
> ASR: `small.en`, 1,562 timestamped segments, approximately 63 minutes.

This full-episode pass reviewed all 1,562 ASR segments. It prioritizes Storyteller-controlled setup composition, bluff availability, misinformation design, player-experience calibration, intervention boundaries and Scarlet-Woman-specific state transitions.

## High-value machine-understood findings

### C2-SCARLET-WOMAN-M01 — Scarlet Woman is a useful setup stabilizer when Evil may contain inexperienced players

**Window:** approximately `00:40:16–00:42:19`

Machine-understood meaning:

- John recommends Scarlet Woman as a strong Minion choice when a group mixes experienced and inexperienced players;
- the Storyteller does not control who draws the Imp, so a setup can accidentally put a new player on Evil against a highly experienced Good team;
- Scarlet Woman supplies redundancy if the Demon is found early and is mechanically easier for a new Minion to understand than Poisoner or Spy;
- its baseline value exists even when the player does not exploit the role strategically, because it can still catch an Imp death.

Potential downstream dimensions:

- player experience distribution;
- Evil-team resilience;
- role cognitive load;
- beginner suitability;
- setup stability.

**E3 disposition:** strong setup-policy guidance, not a fixed historical candidate comparison.

### C2-SCARLET-WOMAN-M02 — setup design should reserve useful bluff surfaces for Evil, not only select strong in-play roles

**Window:** approximately `00:42:50–00:43:53`

Machine-understood meaning:

- Investigator is highlighted as a particularly valuable Scarlet Woman bluff because the Scarlet Woman can point at the real Demon as a supposed Minion, gain credibility after the Demon dies, and shape the table's model of which Minion was removed;
- for the Storyteller, enabling that play means **not** putting Investigator in the bag;
- John explicitly frames Evil bluff design as partly about what the Storyteller leaves out of the setup;
- the Storyteller can additionally give Investigator as a Demon bluff, hoping it will be coordinated onward to the Scarlet Woman.

Potential downstream dimensions:

- bluff availability;
- omitted-role value;
- Evil coordination support;
- setup composition;
- future-flexibility value.

**Verification / LRE disposition:** **VERIFIED BOUNDED DESIGN OPTION / POSITIVE EXAMPLE** by primary-audio review on 2026-10-04. Human review confirmed Investigator as a valuable Scarlet-Woman bluff surface, the option of leaving Investigator out of the bag, and the possible play of supplying Investigator as a Demon bluff for Evil coordination. The source does **not** establish this as globally preferable to other interesting bluff constructions. The project owner's separate view that the play is worth recommending is design opinion, not source evidence.

### C2-SCARLET-WOMAN-M03 — Red Herring placement can account for known Fortune Teller selection habits, but this is an advanced/meta-sensitive lever

**Window:** approximately `00:43:53–00:44:37`

Machine-understood meaning:

- Scarlet Woman benefits if Fortune Teller checks them early and receives a negative Demon result;
- a Storyteller who knows a group's habits may place the Red Herring to reduce the chance that the Fortune Teller gets a distracting `YES` involving Scarlet Woman;
- the speakers explicitly caution that this is deeper meta-driven Storytelling and is probably not worth doing unless the Storyteller knows the group well.

Potential downstream dimensions:

- player tendency/meta;
- Red Herring placement;
- Scarlet Woman future deniability;
- confidence shaping;
- intervention complexity.

**E3 disposition:** generic conditional guidance with an explicit overfitting/meta caution.

### C2-SCARLET-WOMAN-M04 — Fortune Teller misinformation should be longitudinally stateful, especially across a Scarlet Woman jump

**Window:** approximately `00:44:38–00:45:55`

Machine-understood meaning:

- drunk/poisoned Fortune Teller information can be shaped around the Scarlet Woman state;
- if Good is badly behind, the Storyteller may sometimes choose misinformation that gives Good a useful lead rather than compounding the runaway state, but the speakers also restate the normal constraint that impairment should harm that player's team;
- John describes recording every target the Fortune Teller has checked so later misinformation can remain coherent with the player's history;
- the operative Storyteller object is therefore not a single isolated `YES/NO`, but the **narrative created by the sequence of prior checks**.

Potential downstream dimensions:

- longitudinal state;
- prior target history;
- misinformation coherence;
- game-balance context;
- impairment intent.

**E3 disposition:** high-value recommendation context; no historical fixed same-state alternative set.

### C2-SCARLET-WOMAN-M05 — Mayor bounce can force an Imp-to-Scarlet-Woman transition, but direct balance intervention has a legitimacy cost

**Window:** approximately `00:53:11–00:54:31`

Machine-understood meaning:

- when an Imp attacks a Mayor, the Storyteller may redirect the death onto the Imp;
- with Scarlet Woman in play, this can intentionally force the Demon to transfer to Scarlet Woman;
- a possible justification is that Good is already close to solving the current Demon while Scarlet Woman has a better-established bluff, so the transfer restores uncertainty;
- the speakers explicitly flag this as a highly involved Storyteller move that may feel like “tipping the scales”;
- whether it is acceptable depends partly on the group's tolerance for visible Storyteller control.

Potential downstream dimensions:

- adaptive balance intervention;
- current Demon suspicion;
- successor bluff quality;
- player expectation;
- Storyteller-control tolerance;
- intervention legitimacy.

**E3 disposition:** unusually explicit choice/rationale pair, but still hypothetical/general rather than a reconstructed historical production decision.

### C2-SCARLET-WOMAN-M06 — adding Drunk can increase causal ambiguity in Scarlet Woman games

**Window:** approximately `00:54:41–00:55:07`

Machine-understood meaning:

- Scarlet Woman already creates apparently contradictory events without Poisoner/Drunk, such as a Demon dying while the game continues;
- adding Drunk can broaden the set of plausible explanations for strange information;
- the speakers describe this as useful because Evil can exploit the uncertainty, including bluffing impairment and inviting execution when Scarlet Woman provides the backup.

Potential downstream dimensions:

- setup ambiguity;
- causal multiplicity;
- Drunk inclusion value;
- Evil bluff support;
- world diversity.

**E3 disposition:** setup-composition guidance, no historical comparison.

### C2-SCARLET-WOMAN-M07 — Scarlet Woman changes the value of risky Demon bluffs and sacrifice plays

**Windows:** approximately `00:05:21–00:13:40`, `00:50:00–00:53:11`, and `00:55:10–00:56:23`

Machine-understood meaning:

- because the Demon can die without immediately losing while Scarlet Woman is active, Evil can deliberately use plays normally too dangerous for the Demon;
- examples include giving true information that exposes the Demon, nominating Virgin, taking a failed Slayer bluff, double-claiming late, or claiming Saint;
- the Storyteller should therefore evaluate Scarlet Woman partly as a role that changes the **risk budget** of the entire Evil team, not only as a simple resurrection effect;
- late-game timing matters because many of these plays aim to preserve a transfer until around five or six living players.

Potential downstream dimensions:

- Evil risk tolerance;
- bluff payoff/risk;
- sacrifice value;
- living-player threshold;
- team-wide role synergy.

**E3 disposition:** product-facing setup/value dimension; much of the content is player strategy rather than direct Storyteller choice.

### C2-SCARLET-WOMAN-M08 — Recluse-triggered duplicate Evil Demon states are rules-possible but bad policy

**Window:** approximately `00:37:00–00:40:14`

Machine-understood meaning:

- if a dying Recluse registers as the Imp, Scarlet Woman can technically trigger and become an Imp while the original Evil Demon remains alive;
- the speakers strongly recommend never doing this in normal Trouble Brewing because two living Evil Demons make the game effectively unwinnable for Good;
- this is another clear instance where rules legality must not be treated as production-policy endorsement.

Potential downstream dimensions:

- legality vs desirability;
- game solvability;
- pathological interactions;
- safety boundary;
- Storyteller restraint.

**E3 disposition:** strong policy prohibition, not ranking evidence.

### C2-SCARLET-WOMAN-M09 — new-player rules comprehension is part of Scarlet Woman interaction quality

**Window:** approximately `00:58:18–01:00:37`

Machine-understood meaning:

- Scarlet Woman + Slayer can confuse new players because they have learned the simple rule that “if the Demon dies, Good wins,” yet the game continues;
- John describes taking over briefly to explain the complete possibility space — e.g. Slayer is confirmed, and either Recluse died or the Imp died and Scarlet Woman took over — without revealing which world is true;
- the same issue can arise when a new Undertaker sees an Imp token after execution;
- Storyteller explanation can therefore preserve player comprehension without collapsing hidden information.

Potential downstream dimensions:

- player experience;
- explanation burden;
- rules comprehension;
- information-preserving clarification;
- interaction complexity.

**E3 disposition:** player-experience/run-quality guidance only.

### C2-SCARLET-WOMAN-M10 — Scarlet Woman setup value should include downstream information-network effects, not only its own ability

**Windows:** approximately `00:45:55–00:49:15`, `00:57:17–00:58:18`, and `01:00:49–01:02:29`

Machine-understood meaning:

- Undertaker, Monk, Ravenkeeper, Slayer, Spy and Butler all change how a Scarlet Woman game can unfold;
- Scarlet Woman can make normally contradictory information legitimate, can create a known destination for an Imp self-kill, and can make certain confirmations or delayed tests more valuable;
- Spy particularly increases Scarlet Woman coordination quality by revealing whether Investigator saw Scarlet Woman, whether Fortune Teller exists/is impaired, and what bluff pair is safest;
- these interactions argue for evaluating Scarlet Woman as part of an **information network / setup topology**, not in isolation.

Potential downstream dimensions:

- role-interaction topology;
- confirmation pathways;
- transfer detectability;
- Evil coordination;
- setup-level synergy.

**E3 disposition:** broad qualitative setup guidance, no strict historical comparison.

## Strict E3 result

**No new E3 PASS is admitted from this episode.**

The strongest bounded Storyteller-choice leads are:

- **M05:** Mayor bounce onto the current Imp to force a Scarlet-Woman transition when Good is close to solving the current Demon and Scarlet Woman has the stronger bluff;
- **M03:** Red Herring placement informed by known Fortune Teller selection habits;
- **M04:** Fortune Teller misinformation selected from the history of prior checks and the current Scarlet-Woman state;
- **M02:** leaving Investigator out / giving it as a bluff in order to preserve a high-value Scarlet Woman line.

However, the episode presents these as generic or hypothetical policy guidance. It does not preserve one historical decision with a complete production-time state, legal candidate domain, chosen outcome and same-state alternatives under the strict E3 contract.

## Product-facing triage

Most useful for future recommendation work:

1. **M01** — player experience distribution and Minion cognitive load belong in setup evaluation;
2. **M05** — direct balance interventions need an explicit “intervention legitimacy / player expectation” dimension, not merely a win-balance objective;
3. **M04** — misinformation should consume longitudinal history rather than only the current check;
4. **M02** — omitted roles have positive setup value because they create Evil bluff surfaces;
5. **M03** — player tendency/meta can be enrichment context, but should be bounded to avoid overfitting;
6. **M09** — player comprehension and information-preserving explanation are legitimate runtime concerns;
7. **M08** — legality must remain separate from recommended policy;
8. **M07/M10** — Minion setup value includes team-wide risk budget and interaction topology.

No immediate primary-audio review is requested. The episode is valuable as qualitative recommendation-policy evidence, but no current Host production gate depends on promoting these findings to VERIFIED.
