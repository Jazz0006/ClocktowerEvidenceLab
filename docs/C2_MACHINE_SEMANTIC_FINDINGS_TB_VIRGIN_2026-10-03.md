# C2 Machine Semantic Findings — Virgin (Trouble Brewing) — 2026-10-03

> Status: **MACHINE SEMANTIC REVIEW ONLY / NOT VERIFIED**
>
> Source: `17: Virgin (Trouble Brewing) - Featuring Amy Hawkes from TPI!`
>
> Source ID: `podcast:b793dbc29ab95bd16c4f9fdc797c65e9`
>
> GUID: `9a414e33-f73d-4ddf-8ce0-a07c01f3781b`
>
> ASR: `small.en`, 1,344 timestamped segments, approximately 1h21m.
>
> Guest provenance: Amy Hawkes identifies herself as responsible for Clocktower online tooling including the website, script tool and wiki, and describes extensive involvement with the game's development and play. Per project-owner calibration, Cult of the Clocktower hosts/guests are trusted Storyteller clue sources. This machine pass does not itself promote any finding to VERIFIED.
>
> The complete transcript was reviewed in bounded time windows. Full audio and full ASR remain temporary external artifacts and are not committed to Git.

## High-value machine-understood findings

### C2-VIR-M01 — treat Virgin as a likely public confirmation event when evaluating setup strength

**Windows:** approximately `00:04:13–00:08:52` and `01:09:04–01:10:49`

Machine-understood meaning:

- the episode repeatedly frames a functioning Virgin as unusually strong because it can create a publicly trusted Good anchor;
- when a first-night-only Townsfolk such as Washerwoman, Librarian, Investigator or Chef triggers Virgin, the result can create a multi-player confirmation chain very early;
- in the Storyteller section, the guest explicitly recommends putting Virgin into a setup with the assumption that it is likely to activate rather than treating the activation as an exceptional upside;
- therefore setup evaluation should account for the expected downstream confirmation network, not just count Virgin as one ordinary Townsfolk.

Potential downstream dimensions:

- setup information budget;
- confirmation-chain density;
- public trust anchor;
- execution resource;
- early-game world reduction.

### C2-VIR-M02 — when Virgin is expected to confirm, Evil may need stronger or more versatile bluff support

**Window:** approximately `01:09:26–01:10:35`

Machine-understood meaning:

- a confirmed Virgin often gives Good a large early information advantage;
- the guest says they may compensate by choosing stronger/more versatile Demon bluffs than they otherwise would;
- they also suggest that setups with Virgin may benefit from more first-night information and fewer ongoing-information roles, because a confirmed Virgin paired with strong recurring information such as Undertaker can produce an overwhelming information engine;
- if Monk is in the setup, Storyteller should expect the confirmed Virgin to become a natural protection target and account for that interaction.

Potential downstream dimensions:

- Demon bluff selection;
- setup information distribution;
- ongoing-vs-front-loaded information balance;
- Monk/Virgin interaction;
- confirmation-network strength.

**Policy-sensitive:** this is contextual Storyteller balancing guidance, not a fixed setup formula.

### C2-VIR-M03 — Spy triggering Virgin should usually be allowed because the play already carries a large Evil-side cost

**Window:** approximately `01:10:49–01:14:14`

Machine-understood meaning:

- Spy is the principal Trouble Brewing exception to the intuition that a Virgin-triggered nominator is necessarily Good;
- both speakers favor allowing Spy to trigger Virgin most of the time when the Spy chooses that play;
- the stated rationale is that Spy sacrifices life and future grimoire access while also genuinely confirming the Virgin;
- therefore the registration choice should recognize the cost already paid by Evil rather than treating Spy-triggered Virgin as a free Evil benefit;
- the guest gives a strong informal tendency (“nine times out of ten”), but this should not be encoded as a numeric production probability.

Potential downstream dimensions:

- Spy registration;
- ability-sacrifice cost;
- information confirmation;
- anti-meta;
- player agency.

This independently reinforces the same direction found in the Spy episode.

### C2-VIR-M04 — Storyteller behavior around nominations should be deliberately consistent to avoid physical/meta leakage

**Window:** approximately `01:02:44–01:04:10`

Machine-understood meaning:

- Virgin is unusually sensitive to Storyteller reaction timing because a pause, grimoire check or visible surprise after a nomination can reveal whether the nomination matters mechanically;
- recommended practice is to check Virgin/Drunk/Poison state before nominations or deliberately use the same pause/check behavior on all nominations;
- the broader principle is that Storyteller physical timing and reaction should not become an unintended information channel.

Potential downstream dimensions:

- authoritative action UX;
- anti-meta;
- public timing normalization;
- hidden-state leakage prevention.

This aligns strongly with the earlier `Storytelling Like a Pro` timing/meta finding.

### C2-VIR-M05 — Storyteller may support risky player bluffs, especially for newer players, without turning support into game information

**Window:** approximately `01:04:26–01:08:49`

Machine-understood meaning:

- if a player is bluffing Virgin, the Storyteller may mirror the normal pause/check behavior rather than instantly revealing through body language that nothing can happen;
- the guest recommends leaning into risky plays by newer players so experimentation does not feel punished merely because the Storyteller reaction gives the bluff away;
- a broader example describes a Storyteller protecting a player from an out-of-game/mechanical-version mistake so the player is judged on in-game reasoning rather than an accidental rules mismatch;
- support should remain neutral in game-state semantics: players should reason from mechanics, not infer truth from the Storyteller's theatrical response.

Potential downstream dimensions:

- new-player handling;
- bluff support;
- meta suppression;
- Storyteller neutrality;
- player agency.

**Policy-sensitive:** production UI should preserve neutral authoritative semantics; this finding should not authorize misleading factual rules statements.

### C2-VIR-M06 — rules clarification for new players should give the exact legal inference without over-emphasizing exotic alternatives

**Window:** approximately `01:14:47–01:18:26`

Machine-understood meaning:

- after Virgin triggers, a new player may need explicit clarification that the Virgin is confirmed and that the executed nominator is a Townsfolk or may be a registering Spy;
- one speaker favors stating this for inexperienced groups so they have the information the rules entitle them to;
- the guest warns that proactively emphasizing “it could be Spy” can create confirmation bias, because players may interpret a Storyteller reminder as a hint rather than a neutral rules explanation;
- for experienced groups, both speakers agree no reminder is needed;
- if a player directly asks a rules question, Storyteller should answer accurately.

Potential downstream dimensions:

- player experience;
- rules explanation;
- information neutrality;
- confirmation-bias prevention;
- onboarding.

### C2-VIR-M07 — Drunk Virgin has unusually high public-state impact and should be evaluated as a whole-table misinformation choice

**Window:** approximately `01:18:32–01:20:15`

Machine-understood meaning:

- Virgin naturally tends to dominate public discussion because activation/failure is visible and strategically important;
- making Virgin the Drunk therefore creates a high-impact public misinformation state rather than merely corrupting one private information stream;
- a failed Virgin trigger can put suspicion on both the Virgin and the nominator, often two Good players;
- a talkative/strong player who believes they are Virgin may spend substantial public attention explaining why the ability failed;
- downside: because Drunk is spent on Virgin, no information-gathering Townsfolk is Drunk; if the table correctly identifies Drunk Virgin, other information may become more trustworthy.

Potential downstream dimensions:

- Drunk assignment;
- public-information impact;
- player communication level;
- misinformation breadth;
- information-budget tradeoff.

This is useful long-term Drunk-assignment evidence, but not an E3-qualified historical choice by itself.

### C2-VIR-M08 — Virgin confirmation changes the value of remaining executions and information nights

**Window:** approximately `00:14:31–00:17:37`

Machine-understood meaning:

- Virgin activation consumes an execution, which matters especially in small games with very few execution opportunities;
- therefore the value of activating Virgin depends partly on what additional confirmation is obtained from the nominator and their information;
- the host notes that in a small one-Minion game with a confirmed Virgin and useful ongoing information, skipping a later execution can sometimes be worth considering to gain another night of information;
- the source explicitly presents this as situational rather than a universal execution policy.

Potential downstream dimensions:

- execution budget;
- player count;
- confirmed-Good anchor;
- ongoing information value;
- temporal decision tradeoff.

### C2-VIR-M09 — a failed Virgin trigger creates a bounded diagnostic tree that should be preserved rather than prematurely resolved

**Window:** approximately `00:27:47–00:36:44`

Machine-understood meaning:

- when a claimed Virgin is nominated and nothing happens, the key live explanations include the Virgin being Drunk/poisoned, the nominator being the Drunk, or the nominator being Evil;
- self-nomination can remove the nominator variable and more directly test whether Virgin's own ability is unavailable;
- the guest emphasizes using other information to determine where the fault lies rather than immediately tunnel-visioning on one player;
- a failed Virgin can therefore still create useful structured information about Drunk/Poison/Evil worlds.

Potential downstream dimensions:

- failed-ability diagnosis;
- world preservation;
- Drunk/Poison inference;
- execution recommendation context;
- uncertainty representation.

This supports preserving multiple live worlds rather than collapsing a failed public ability into a single explanation.

## Triage

### Strongest product-facing findings

1. **M01/M02 — model Virgin as a likely confirmation network when evaluating setup and Demon bluffs**
2. **M03 — Spy-triggered Virgin should account for the Spy's sacrifice rather than using a fixed registration default**
3. **M04 — normalize Storyteller public timing/reaction to prevent hidden-state leakage**
4. **M06 — player-experience-sensitive rules clarification without confirmation-bias leakage**
5. **M07 — Drunk Virgin is a high-breadth public misinformation choice**
6. **M09 — preserve the diagnostic world tree after a failed Virgin trigger**

### E3 re-entry disposition

This pass found useful examples and general principles but **no new bounded historical Storyteller decision that independently satisfies the strict E3 contract** with all of:

- exact committed decision-time state;
- recoverable legal alternative domain;
- observed Storyteller choice;
- source-backed same-state alternative comparison or rationale;
- generic Host feature mapping.

The Virgin pass therefore does not replace or outrank the existing G10 `16:52` Librarian E3 PASS.

## Verification disposition

No immediate human audio review is required merely to retain these findings.

Human primary-audio confirmation is required before:

- M02 becomes a production setup/bluff-strength preference;
- M03 becomes any numeric Spy-registration tendency;
- M05 is used to define product behavior that intentionally simulates Storyteller uncertainty;
- M06 is turned into a scripted onboarding message;
- M07 is used to rank Virgin as a Drunk candidate against other Townsfolk;
- any item is promoted to VERIFIED evidence.

The temporary full audio and ASR workspace may be cleaned after this lightweight record is safely committed.
