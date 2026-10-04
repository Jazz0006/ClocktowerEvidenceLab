# C2 Machine Semantic Findings — Recluse — 2026-10-04

> Status: **MIXED — M08/M09/M10 PRIMARY-AUDIO HUMAN REVIEWED; OTHER FINDINGS REMAIN MACHINE SEMANTIC / NOT VERIFIED**
>
> Source: `Recluse (Trouble Brewing)`
>
> Source ID: `podcast:af87b5f5461c44e39a4fae6b7405c443`
>
> GUID: `e4b8704a-19d7-5c9f-e483-a659be61cc46`
>
> Guest: official Storyteller Ben Dance
>
> ASR: `small.en`, 2,841 timestamped segments, approximately 74 minutes.

This full-episode pass reviewed all 2,841 ASR segments. It prioritizes Storyteller-controlled Recluse registration, setup-wide information balance, confirmation chains, player experience, anti-meta, information topology and explicit choice-over-alternatives guidance.

## High-value machine-understood findings

### C2-RECLUSE-M01 — early Recluse execution value depends on player count, information topology and opportunity cost

**Window:** approximately `00:12:26–00:16:18`

Machine-understood meaning:

- simply executing a claimed Recluse to remove future registration ambiguity is not treated as a universal rule;
- larger games provide more execution slack, while smaller games make each execution more valuable;
- if an Empath sits beside the Recluse, executing the Recluse can simplify future Empath reads, but this can also create a sunk-cost trap where the town over-trusts the Empath afterward;
- if Undertaker is in play, spending an early execution on Recluse can waste one of the strongest opportunities to obtain high-value role-confirmation information;
- executing Recluse can itself generate further ambiguity because Undertaker may receive an Evil role instead of Recluse.

Potential downstream dimensions:

- player count;
- execution budget;
- information topology;
- confirmation opportunity cost;
- registration side effects.

**E3 disposition:** strong conditional policy dimensions; not a fixed historical Storyteller candidate comparison.

### C2-RECLUSE-M02 — Slayer-on-Recluse is a confirmation tradeoff, not an automatic “fun interaction”

**Window:** approximately `00:35:20–00:43:08`

Machine-understood meaning:

- killing Recluse with Slayer can strongly confirm the Slayer and can be more valuable than an uncertain Slayer shot elsewhere;
- the value depends on whether Slayer already has strong Demon-targeting information from roles such as Empath or Fortune Teller;
- in some group metas, Slayer shots almost never hit Demons, making confirmation through Recluse relatively more attractive;
- a final-four Recluse shot can potentially confirm both Slayer and Recluse while preserving the day's execution, but the speakers explicitly recognize tradeoffs in removing a Good player's later nomination agency;
- the choice is therefore state- and meta-dependent rather than “Slayer should always kill Recluse.”

Potential downstream dimensions:

- confirmation strength;
- remaining ability value;
- group meta;
- nomination/execution resources;
- late-game topology.

**E3 disposition:** explicit alternative-aware guidance, but no fully reconstructed historical production state.

### C2-RECLUSE-M03 — technically legal registration interactions can still be bad Storyteller choices

**Window:** approximately `00:56:36–01:01:08`

Machine-understood meaning:

- Recluse registering as Demon when dying to trigger Scarlet Woman, creating two living Evil Demons, is described as technically possible but strongly discouraged;
- Recluse receiving an Imp star-pass and becoming a Good Demon is likewise treated as something that normally should not be done;
- a rarer double-Demon case involving both Recluse and Scarlet Woman is described as only remotely defensible in an explicitly advanced/silly game where players are knowingly on board;
- the central principle is that legality is not equivalent to good Storyteller policy.

Potential downstream dimensions:

- legality vs desirability;
- game integrity;
- player consent/expectation;
- experience level;
- unusual-interaction risk.

**E3 disposition:** strong safety/policy boundary, not a ranking case.

### C2-RECLUSE-M04 — Storyteller decisions should optimize whole-table experience, not only direct balance correction

**Window:** approximately `00:57:58–00:58:41`

Machine-understood meaning:

- Ben explicitly says he evaluates how a Storyteller decision affects everyone, not only the directly affected team;
- the Mayor example illustrates that redirecting a kill onto a Minion may help balance but can make that Minion feel unfairly deprived of plans and agency;
- the same reasoning is positioned as relevant to Recluse registration choices;
- player enjoyment and retained agency are therefore legitimate Storyteller decision inputs alongside pure win-balance.

Potential downstream dimensions:

- whole-table utility;
- player agency;
- role enjoyment;
- balance correction cost;
- fairness perception.

**E3 disposition:** generic decision-objective guidance.

### C2-RECLUSE-M05 — Chef registration should consider whether a high number over-compresses the game

**Window:** approximately `01:03:49–01:04:56`

Machine-understood meaning:

- Ben gives a specific hypothetical where Recluse is adjacent to two Evil players;
- registering Recluse as Evil could produce a Chef `3`, but he says the Storyteller should think carefully before doing so;
- the decision depends on whether Chef is likely to reveal early and whether the group will trust/use that information;
- giving `0` or otherwise avoiding the maximum registration can preserve a more normal game and prevent the Recluse from becoming an overly strong anchor that immediately exposes adjacent Evil players.

Potential downstream dimensions:

- truthful-registration strength;
- world compression;
- reveal likelihood;
- group trust;
- setup-wide information budget.

**E3 disposition:** unusually strong explicit same-hypothetical A-vs-B guidance, but still not an observed historical decision with a reconstructed production state/domain.

### C2-RECLUSE-M06 — Empath misinformation with Recluse should avoid instantly exposing the adjacent Minion

**Window:** approximately `01:04:57–01:06:17`

Machine-understood meaning:

- for Empath seated between Recluse and an actual Evil player, immediately showing `2` is described as potentially making the game much less fun for the Evil player;
- Ben specifically emphasizes the experience cost when a player rarely gets an Evil role and loses it quickly due to an aggressive Recluse registration;
- the proposed alternative is to show `1`;
- if the Evil neighbour is later executed, the Storyteller may continue showing `1`, using Recluse registration to keep the Empath uncertain rather than letting the sequence perfectly confirm the removed Evil player;
- the stated default is that an Outsider should generally impose a cost on Good rather than become a giant free clue.

Potential downstream dimensions:

- misinformation trajectory;
- Evil-player agency;
- outsider burden;
- information strength;
- longitudinal consistency.

**E3 disposition:** very strong explicit candidate/output preference, but no historical fixed state.

### C2-RECLUSE-M07 — Recluse can deliberately shape Fortune Teller confidence, including Red Herring interpretation

**Window:** approximately `01:06:19–01:06:54`

Machine-understood meaning:

- Recluse can be used so a Fortune Teller interprets a `YES` as likely Red Herring behavior rather than as a Demon hit;
- the Storyteller can even place Red Herring on the Recluse, creating additional ambiguity about why `YES` results occur;
- the resulting design target is not merely “false information,” but uncertainty about which mechanism caused the information.

Potential downstream dimensions:

- causal ambiguity;
- Red Herring interaction;
- confidence calibration;
- misinformation mechanism overlap;
- world multiplicity.

**E3 disposition:** generic mechanism-combination guidance.

### C2-RECLUSE-M08 — Investigator may be routed to Recluse instead of the real Minion when the setup is already too strong for Good

**Window:** approximately `01:06:54–01:07:57`

Machine-understood meaning:

- Ben explicitly says the Investigator can be shown a Minion role between a Townsfolk and the Recluse, with neither candidate actually being the real Minion;
- he presents this as particularly useful when another role such as Empath already has an unusually strong starting position, for example sitting next to two Evil players;
- this trades away Investigator's direct Minion-finding power to avoid compounding already-strong Good information;
- he notes this is something he personally does not use often, but sees as a viable Storyteller tool.

Potential downstream dimensions:

- cross-role information budget;
- setup strength compensation;
- Minion concealment;
- registration;
- marginal information value.

**Verification / LRE disposition:** **VERIFIED** by bounded primary-audio review on 2026-10-04. Human review confirmed this is an `EXPLICIT_PREFERENCE` under the stated condition: when Good already has unusually strong information (including the explicit example of Empath adjacent to two Evil players), using Recluse registration to avoid exposing the real Minion is a recommended Storyteller construction, not merely a legal possibility. It is not a universal Recluse default.

### C2-RECLUSE-M09 — Investigator can instead be shown the real Minion plus Recluse, using truthful information to create deniability

**Window:** approximately `01:07:57–01:08:37`

Machine-understood meaning:

- the speakers describe another applicable construction: showing Investigator the real Minion and the Recluse as the two candidates;
- once Recluse comes out, Investigator may incorrectly attribute the Minion ping to Recluse registration and discount the real Minion;
- the information can therefore remain technically truthful while still giving Evil useful cover;
- this is a clear example of preserving information validity while controlling how strongly the table can act on it.

Potential downstream dimensions:

- truthful ambiguity;
- candidate-pair construction;
- Minion deniability;
- information interpretation;
- confirmation suppression.

**Verification / LRE disposition:** **VERIFIED BOUNDED DESIGN OPTION / RATIONALE** by primary-audio review on 2026-10-04. Human review confirmed the real-Minion + Recluse construction and its deniability rationale, but corrected the machine inference that it was an explicit comparison with M08. There is **no source-backed ordering or loser relation between M08 and M09**; both can be appropriate depending on actual game state.

### C2-RECLUSE-M10 — Undertaker Recluse registration should react to the evolving game state and world model

**Window:** approximately `01:08:38–01:10:20`

Machine-understood meaning:

- if Good is solving too easily, the Storyteller may show executed Recluse as Spy to reopen doubt about apparently trustworthy players;
- showing Recluse as Imp can imply that the live Minion must be Scarlet Woman and can alter deductions about Baron or Outsider count;
- in smaller games it can also change whether players believe Poisoner is possible, affecting how they assess the reliability of multiple prior information chains;
- Ben describes this as a way to “throw a bone” to Evil when needed, not as a fixed Recluse registration default.

Potential downstream dimensions:

- adaptive balance;
- world-model disruption;
- role-existence inference;
- longitudinal information ecology;
- dynamic game state.

**Verification / LRE disposition:** **VERIFIED EXPLICIT STATE-DEPENDENT GUIDANCE** by primary-audio review on 2026-10-04. Human review confirmed that Spy/Imp and other Recluse Undertaker registrations should be selected from the live world-model consequences, with no fixed ordering between Spy and Imp.

### C2-RECLUSE-M11 — Librarian can either reinforce Recluse trust or conceal Recluse existence, depending on the goal

**Window:** approximately `01:10:21–01:11:39`

Machine-understood meaning:

- if the local meta automatically executes Recluse, a Librarian can be given Recluse information to make the claim more credible and help the player survive, explicitly changing that meta;
- the opposite option is also discussed: Librarian can be shown `0` Outsiders even when Recluse is in play by having Recluse register differently at that moment;
- that zero result can itself become a soft confirmation path for Recluse under the expected Outsider count, while preserving Drunk/Poisoner alternatives;
- Librarian/Recluse registration therefore supports opposite intents: **trust support** versus **world concealment/ambiguity**.

Potential downstream dimensions:

- trust support;
- meta correction;
- outsider-count ambiguity;
- opposite valid intents;
- setup information routing.

**E3 disposition:** explicit alternative intents, but not a reconstructed historical same-state decision.

### C2-RECLUSE-M12 — player experience should affect both registration severity and Storyteller explanation

**Windows:** approximately `00:34:10–00:35:00`, `01:05:08–01:05:41`, and `01:10:06–01:12:47`

Machine-understood meaning:

- Ben distinguishes what he explains to brand-new players from what he expects experienced players to infer about registration;
- he is concerned about aggressively outing a newly Evil player's role through Recluse interactions before that player gets meaningful agency;
- when a new player is Recluse, he may privately explain what kinds of registration interactions are possible so the player can help their team reason about confusing outcomes;
- highly exotic interactions are reserved for groups experienced enough to understand and consent to them.

Potential downstream dimensions:

- player experience;
- explanation need;
- role enjoyment;
- complexity calibration;
- acceptable surprise.

**E3 disposition:** player-experience policy guidance only.

## Strict E3 result

**No new E3 PASS is admitted from this episode.**

This episode contains several unusually strong generic candidate comparisons:

- **M05:** Chef `3` vs less revealing outputs when Recluse sits with Evil players;
- **M06:** Empath `2` vs `1`, and later maintaining `1` after the Evil neighbour dies;
- **M08/M09:** Investigator routed entirely to Recluse vs real-Minion-plus-Recluse;
- **M11:** Librarian explicitly supporting Recluse credibility vs hiding Recluse through a zero-Outsider result.

However, these are presented as hypotheticals/general Storyteller guidance, not as one historical decision with the complete production-time game state, legal candidate domain, selected outcome and same-state alternative set required by the strict E3 contract.

## Product-facing triage

Most useful for future recommendation work:

1. **M06** — Recluse registration should preserve Outsider burden and Evil-player agency rather than maximizing raw information;
2. **M05** — Chef information strength should be limited when truthful registration would over-compress worlds;
3. **M08/M09** — Investigator has multiple legitimate Recluse-aware pair-construction intents depending on the rest of the information ecology;
4. **M10** — Undertaker registration is a dynamic game-state lever whose value depends on the worlds currently believed by town;
5. **M11** — Recluse registration can intentionally support trust or conceal worlds, with no universal direction;
6. **M04/M12** — player agency, enjoyment, experience and explanation burden belong in the decision context;
7. **M03** — legality and good Storyteller policy must remain separate;
8. **M02** — confirmation interactions should be valued relative to remaining ability value and group meta.

No immediate primary-audio review is requested. The episode is highly valuable for qualitative recommendation dimensions, but no current production gate depends on promoting these generic statements to VERIFIED. Human review should be requested only if Host opens a bounded policy/ranking question around one of these exact dimensions.
