# C2 Machine Semantic Findings — Washerwoman — 2026-10-03

> Status: **MACHINE SEMANTIC REVIEW ONLY / NOT VERIFIED**
>
> Source: `11: Washerwoman (Trouble Brewing) - With Official Storyteller Reggie Collins!`
>
> Source ID: `podcast:81f82799d83c9572fff012de09bf2247`
>
> GUID: `c9618286-6096-43fe-b086-cd5e022596b5`
>
> ASR: `small.en`, 2,790 timestamped segments, approximately 61 minutes.

This full-episode pass prioritizes Storyteller-controlled pair-information construction, Spy registration, Drunk/poisoned Washerwoman handling, information-strength calibration, player-experience effects and explicit historical choice rationales.

## High-value machine-understood findings

### C2-WASHERWOMAN-M01 — pair information changes trust topology, not only role knowledge

**Window:** approximately `00:03:24–00:15:00`

Machine-understood meaning:

- Washerwoman information can create a bidirectional trust edge between the Washerwoman and the real Townsfolk;
- which role is shown changes the downstream cost of disclosure: revealing Undertaker/Fortune Teller/Monk can expose a high-value role to Evil, while Ravenkeeper-like roles may instead lose their intended Demon-bait function;
- the value of the pair therefore includes who can safely exchange later information, not merely whether the initial clue is correct.

Potential downstream dimensions:

- trust-network creation;
- role-exposure cost;
- information-routing value;
- recipient-role utility.

**E3 disposition:** strong feature-shape support, but this section is mainly player-strategy discussion rather than one fixed Storyteller decision.

### C2-WASHERWOMAN-M02 — avoid over-confirming Mayor when the confirmation collapses final-three uncertainty

**Window:** approximately `00:43:09–00:43:52`

Machine-understood meaning:

- Reggie explicitly says he is cautious about showing Mayor to Washerwoman;
- the reason is not that Mayor is weak, but the opposite: Washerwoman confirmation can make a late-game Mayor too trusted, especially if Mayor survives to final three;
- he compares this to an Empath sitting next to Mayor: too much independent confirmation can overweight Good's information strength and remove a desirable final uncertainty;
- Mayor is also described as a common Demon bluff, so direct Washerwoman support can eliminate a useful bluffing ambiguity.

Potential downstream dimensions:

- confirmation-chain strength;
- final-three uncertainty;
- role-information utility;
- bluff-space preservation;
- healthy-information ecology.

**E3 disposition:** explicit generic choice-over-alternatives guidance, but not tied to one reconstructable historical setup.

### C2-WASHERWOMAN-M03 — hidden or hard-to-believe roles can be especially useful Washerwoman targets

**Window:** approximately `00:43:53–00:45:22`

Machine-understood meaning:

- Reggie says he commonly likes Washerwoman to see roles such as Monk, Undertaker or Fortune Teller because they benefit from being able to share information through a trusted intermediary without immediately outing themselves;
- Soldier is also highlighted because it is often difficult for a Soldier to gain social credibility on its own;
- the pair can therefore serve as an information-distribution route or credibility support mechanism.

Potential downstream dimensions:

- information-routing value;
- role credibility deficit;
- exposure cost;
- trust-channel utility.

**E3 disposition:** generic Storyteller guidance only.

### C2-WASHERWOMAN-M04 — Washerwoman can effectively confirm that another information role is not the Drunk

**Window:** approximately `00:46:39–00:47:55`

Machine-understood meaning:

- when Washerwoman truthfully sees an information role, that clue can materially increase confidence that the seen player is sober;
- Reggie specifically notes this for roles that players often suspect of being the Drunk, including Investigator, Undertaker, Empath and Fortune Teller;
- this can be beneficial because it lets players act on otherwise heavily discounted information;
- it is also a source of information-strength amplification and should therefore be evaluated as more than a simple pair clue.

Potential downstream dimensions:

- Drunk-exclusion value;
- confirmation-chain strength;
- information-confidence amplification;
- role-information utility.

**E3 disposition:** strong descriptive feature support; no fixed historical alternative comparison.

### C2-WASHERWOMAN-M05 — historical poisoned-Washerwoman choice supports bluff-compatible misinformation over obviously broken misinformation

**Window:** approximately `00:48:53–00:50:10`

Machine-understood meaning:

- in a real game, the Poisoner hit the Washerwoman on night one;
- Andrew was the Demon;
- Reggie, as Storyteller, deliberately showed the poisoned Washerwoman a pair that included the Demon and one of the Demon's bluffs;
- Reggie explains that simply giving obviously incorrect information risked allowing the Washerwoman to diagnose a Poisoner and thereby causing the Minion hit to backfire;
- instead, he chose misinformation that Evil could directly exploit: if the information reached the Demon, the Demon would know the shown bluff was not actually in play and could safely adopt it;
- the plan worked: multiple players approached the Demon believing that bluff, the Demon accepted it, gained substantial trust and Evil benefited strongly.

Potential downstream dimensions:

- bluff compatibility;
- Poisoner-agency payoff;
- misinformation detectability;
- immediate exploitability by Evil;
- coordination probability;
- narrative support.

**E3 disposition:** **strongest historical candidate in this episode, but not yet E3 PASS.** The observed Storyteller choice and explicit rationale are present, but the complete committed decision-time state and production-recoverable legal output domain are not yet reconstructed.

### C2-WASHERWOMAN-M06 — Drunk Washerwoman is described as a relatively rare choice because it can self-diagnose

**Window:** approximately `00:51:00–00:52:16`

Machine-understood meaning:

- Reggie says he would use Drunk Washerwoman only occasionally;
- his reason is that failed pair confirmation can make the Washerwoman infer that they are the Drunk, which can actually help Good by locating the Outsider and clearing other players from being Drunk;
- he nevertheless says it should happen sometimes so Washerwoman players cannot safely assume they are always sober;
- a Librarian showing Washerwoman + Investigator as the Drunk pair is described as a way to preserve uncertainty over which apparently informative role is actually impaired.

Potential downstream dimensions:

- self-diagnosis risk;
- Outsider-location leakage;
- role expectation / meta suppression;
- Drunk-placement ambiguity;
- player-experience calibration.

**E3 disposition:** explicit generic Drunk-selection rationale, but not one fixed same-state candidate comparison.

### C2-WASHERWOMAN-M07 — misinformation choice should account for player experience

**Window:** approximately `00:52:08–00:52:45`

Machine-understood meaning:

- when discussing Drunk Washerwoman misinformation, the speakers distinguish experienced players from players more likely to accept a Demon/bluff trap;
- the same misleading pair may be too easy for experienced players to diagnose;
- in those cases, a different misinformation construction may be required if the goal is to generate meaningful uncertainty rather than immediate detection.

Potential downstream dimensions:

- player experience;
- misinformation detectability;
- recipient inference skill;
- puzzle difficulty.

**E3 disposition:** context/rationale support only.

### C2-WASHERWOMAN-M08 — the decoy player's category should not become a fixed Storyteller pattern

**Window:** approximately `00:52:51–00:53:42`

Machine-understood meaning:

- the speakers explicitly warn against falling into a fixed habit where the second shown player is always Good or always Evil;
- varying the decoy category avoids Storyteller meta that would let experienced players infer alignment from the shape of the pair rather than from game evidence;
- they also note that showing an Outsider as the second player can simplify the Washerwoman's deduction if that Outsider publicly claims, increasing the effective strength of the clue.

Potential downstream dimensions:

- anti-meta variation;
- decoy alignment/category;
- deduction compression;
- public-claim interaction.

**E3 disposition:** generic pair-construction guidance, not a historical fixed-state choice.

### C2-WASHERWOMAN-M09 — new-player rules comprehension is part of effective information delivery

**Window:** approximately `00:55:05–00:57:48`

Machine-understood meaning:

- Reggie says Washerwoman, Librarian and Investigator are frequently misunderstood by new players;
- he often gives a short pre-game explanation of how the one-token/two-player information format works, including the possibility of Drunk/poisoned information;
- correcting a misunderstanding later can leak confirmation because pulling one player aside may itself reveal that the Storyteller is correcting real information;
- when correction is necessary, calling several players over can mask which information is being repaired.

Potential downstream dimensions:

- player experience;
- explanation need;
- information-delivery reliability;
- correction leakage;
- meta suppression.

**E3 disposition:** operational Storyteller guidance, not recommendation-ranking evidence.

## Strict E3 result

**No new E3 PASS is admitted from this episode.**

The strongest candidate is **C2-WASHERWOMAN-M05** because it contains:

- a real historical Storyteller-controlled misinformation choice;
- a concrete Poisoner-hit Washerwoman context;
- a clearly stated rejected failure mode (obviously broken misinformation that exposes poisoning);
- a positive rationale for the chosen Demon + Demon-bluff construction;
- an observed downstream consequence showing why the choice mattered.

However, the current retained material does not reconstruct the complete committed game state or the full production legal domain at that exact decision point. It therefore remains a high-priority historical E3 lead rather than an accepted E3 case.

## Product-facing triage

Most useful for future recommendation work:

1. **M05** — bluff-compatible misinformation vs detectably broken misinformation;
2. **M02** — confirmation strength can be too high, especially around Mayor/final-three;
3. **M04** — pair information can amplify confidence by excluding Drunk worlds;
4. **M08** — decoy-category variation is needed to suppress Storyteller meta;
5. **M06** — Drunk Washerwoman carries self-diagnosis / Outsider-location leakage risk;
6. **M03** — pair information can function as a safe information-routing channel;
7. **M09** — player experience changes whether the information is delivered reliably at all.

No immediate primary-audio review is requested unless Host opens a bounded gap around pair-information strength, misinformation detectability, bluff compatibility, or Drunk self-diagnosis.
