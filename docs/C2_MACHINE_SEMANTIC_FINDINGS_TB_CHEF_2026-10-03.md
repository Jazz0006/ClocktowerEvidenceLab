# C2 Machine Semantic Findings — Chef (Trouble Brewing) — 2026-10-03

> Status: **MIXED — M04/M06/M07/M08/M09 PRIMARY-AUDIO HUMAN REVIEWED; OTHER FINDINGS REMAIN MACHINE SEMANTIC / NOT VERIFIED**
>
> Source: `Chef (Trouble Brewing)`
>
> Source ID: `podcast:707af3130f8950f4655241f701e7a794`
>
> GUID: `3bf24d7c-b0ac-40a4-885c-4ebc07184228`
>
> ASR: `small.en`, 1,490 timestamped segments, approximately 54m.
>
> The complete transcript was reviewed in bounded time windows. Full audio and full ASR remain temporary external artifacts and are not committed to Git.

## High-value machine-understood findings

### C2-CHEF-M01 — Chef information is primarily a combination amplifier, so its value depends on the rest of the information topology

**Windows:** approximately `00:01:30–00:12:30` and `00:18:43–00:20:02`

Machine-understood meaning:

- Chef information is described as relatively weak in isolation but disproportionately useful when combined with Empath, Investigator, Undertaker, Washerwoman, Librarian, or confirmed-Good anchor points;
- a Chef 0 can exonerate neighbors of a player later known to be Evil;
- a Chef 1 can make otherwise weak positional evidence more useful;
- confirmed Good points around the circle shrink the legal placement space for Evil pairs.

Potential downstream dimensions:

- information-topology interaction;
- confirmation-chain density;
- adjacency structure;
- world-reduction value;
- prospective information synergy.

This supports evaluating Chef information strength from the surrounding information graph rather than from the numeric result alone.

### C2-CHEF-M02 — Chef is a comparatively weak Drunk target when the goal is precise Storyteller control over a narrative

**Window:** approximately `00:21:41–00:22:43`

Machine-understood meaning:

- the speakers describe Drunk Chef as less common than Drunk Washerwoman/Librarian because Storyteller has less direct control over the downstream narrative;
- changing one Chef number may or may not produce the intended later effect because the rest of the game can fan out unpredictably;
- by contrast, pair-information misinformation can more directly make a specific player suspicious or support a specific Evil bluff.

Potential downstream dimensions:

- Drunk assignment;
- controllability of misinformation;
- future-flexibility;
- narrative precision;
- information breadth.

This is useful comparative Drunk-candidate guidance but is not a global ranking.

### C2-CHEF-M03 — Chef can still be a strong Drunk candidate when the truthful number would be unusually constraining

**Window:** approximately `00:43:52–00:44:31`

Machine-understood meaning:

- one speaker gives a concrete Storyteller pattern: when all Evil players are seated in a row, making Chef the Drunk can prevent an unusually powerful truthful high Chef number;
- the example specifically mentions that a Chef 2 in a roughly 10-player game can sharply constrain where Evil must be;
- therefore the strength of the truthful Chef result is relevant when considering whether Chef should be Drunk.

Potential downstream dimensions:

- Drunk assignment;
- setup adjacency;
- truthful-information strength;
- world-space compression.

**E3 disposition:** promising historical/practice lead, but the passage does not preserve enough exact committed game state and same-state alternatives for strict E3 qualification.

### C2-CHEF-M04 — for Drunk Chef misinformation, “believable” and “discoverable” are different objectives

**Window:** approximately `00:44:21–00:47:11`

Machine-understood meaning:

- a believable false Chef result will often be 0 or 1;
- a deliberately higher number can be more interesting because it may cause the Chef to consider Recluse, Drunkenness, or poisoning rather than accept the result uncritically;
- the speakers express a preference for Drunkenness being discoverable rather than leaving a player completely deceived with no path to suspect it;
- therefore a larger false number can sometimes be preferable even though it is less superficially plausible.

Potential downstream dimensions:

- misinformation believability;
- misinformation discoverability;
- player agency;
- Drunk self-diagnosis;
- puzzle quality.

**Verification / LRE disposition:** **VERIFIED BOUNDED DESIGN OPTION / TRADEOFF** by primary-audio review on 2026-10-04. Human review confirmed the distinction between believable and discoverable misinformation, but corrected the machine inference that a larger false Chef number is preferred. A higher false number is a more unusual but sometimes more interesting option because it can create an impairment-diagnosis path; it is not the source-backed default.

### C2-CHEF-M05 — group meta can justify making Chef Drunk when Chef is routinely used to trigger Virgin

**Window:** approximately `00:45:15–00:46:10`

Machine-understood meaning:

- if a group has developed a strong meta where Chef is routinely the preferred Virgin nominator, making Chef the Drunk can disrupt that predictable confirmation route;
- the result creates ambiguity over whether Chef or Virgin is the Drunk when the expected Virgin activation fails;
- the source frames this as adding drama and avoiding stale predictable play, not as a universal recommendation.

Potential downstream dimensions:

- Drunk assignment;
- group meta;
- public confirmation chains;
- anti-meta;
- player expectation.

**Policy-sensitive:** this should remain conditional on an observed local meta.

### C2-CHEF-M06 — Recluse registration to Chef should start from a simple baseline and diverge only for a reason

**Window:** approximately `00:47:16–00:50:53`

Machine-understood meaning:

- the speakers note that Recluse may legally register differently across adjacent pair evaluations, creating multiple legal Chef numbers;
- one speaker's baseline is to treat Recluse as Evil and Spy as Good, then deliberately diverge when a concrete game reason justifies it;
- a mixed-registration middle result can be interesting but is described as unintuitive;
- if players are not aware such a result is possible, they may feel that the result was arbitrary or unfair.

Potential downstream dimensions:

- registration baseline;
- rules intuitiveness;
- player experience;
- legal-alternative selection;
- narrative consequence.

**Verification / LRE disposition:** **VERIFIED EXPLICIT PREFERENCE / BASELINE + REASONED DEVIATION** by primary-audio review on 2026-10-04. The speaker explicitly uses Recluse-as-Evil / Spy-as-Good as a simple personal baseline and prefers departing from it only for a concrete game-state reason. Player comprehension and intuitiveness are part of the decision; this is not a legality rule.

### C2-CHEF-M07 — avoid registration choices that accidentally over-confirm Recluse unless that consequence is intentional

**Window:** approximately `00:52:19–00:52:50`

Machine-understood meaning:

- a Chef number that is only explainable through Recluse registration, Drunkenness, or poisoning may indirectly confirm that one of those states exists;
- the speakers specifically warn that such a number can make Recluse more confirmed than intended;
- therefore legal registration outputs should be evaluated for what worlds they eliminate, not only whether the number is interesting in isolation.

Potential downstream dimensions:

- registration;
- confirmation leakage;
- world elimination;
- Outsider discoverability;
- information strength.

**Verification / LRE disposition:** **VERIFIED EXPLICIT WARNING / POLICY CONSIDERATION** by primary-audio review on 2026-10-04. Human review confirmed that Storyteller should account for accidental confirmation leakage: a legal Chef result can over-confirm Recluse/impairment worlds by eliminating too many alternatives.

### C2-CHEF-M08 — Spy may register Evil to Chef when that creates useful cross-information ambiguity, but the cost to Evil must be considered

**Window:** approximately `00:51:11–00:52:29`

Machine-understood meaning:

- if Spy registers Evil to Chef but Good to another information source later, the mismatch can suggest poisoning or other explanations rather than immediately exposing Spy;
- this can increase uncertainty around the actual Minion type;
- however, if Spy is adjacent to Demon, using an Evil registration may create a strong Chef number that places too much heat on Evil;
- the choice therefore depends on the information consequence and current Evil exposure.

Potential downstream dimensions:

- Spy registration;
- cross-source inconsistency;
- Minion-type ambiguity;
- Evil exposure;
- information strength.

**Verification / LRE disposition:** **VERIFIED STATE-DEPENDENT GUIDANCE** by primary-audio review on 2026-10-04. Human review confirmed that fixed Spy registration is undesirable; the choice should respond to actual information consequences and Evil exposure. This is analogous to the simple-baseline + reasoned-deviation guidance above.

### C2-CHEF-M09 — higher legal Chef numbers are generally stronger Good information and should be treated as a power decision

**Windows:** approximately `00:42:14–00:42:48` and `00:52:19–00:52:29`

Machine-understood meaning:

- larger Chef numbers are described as more constraining because they substantially reduce the number of compatible Evil placements;
- when Storyteller has registration freedom, choosing a higher legal number therefore often strengthens Good;
- this should be considered alongside whether that stronger information creates the more interesting and fair puzzle.

Potential downstream dimensions:

- information strength;
- world-space compression;
- registration choice;
- team-state balance.

**Verification / LRE disposition:** **VERIFIED INFORMATION-STRENGTH PRINCIPLE** by primary-audio review on 2026-10-04. Human review confirmed that higher legal Chef numbers generally provide stronger Good information by compressing compatible Evil worlds. This is a power consideration to include when choosing among legal outcomes, not a blanket preference for lower numbers.

### C2-CHEF-M10 — Chef can serve as low-interference “setup bubble wrap” around more experimental interactions

**Window:** approximately `00:40:19–00:41:43`

Machine-understood meaning:

- Chef is described as broadly compatible with most Trouble Brewing setups and unlikely to disrupt another planned interaction;
- because it has no active setup dependency, it can fill a Townsfolk slot without adding another highly coupled mechanic;
- this makes Chef useful when Storyteller wants another specific setup interaction to remain the main focus.

Potential downstream dimensions:

- setup construction;
- interaction density;
- complexity budget;
- role coupling.

### C2-CHEF-M11 — player experience can matter when assigning low-agency first-night-only roles such as Chef

**Window:** approximately `00:41:45–00:42:20`

Machine-understood meaning:

- the speakers describe a newer player receiving Chef repeatedly and finding Chef 0 underwhelming;
- while Chef 0 is mechanically meaningful, it can feel like “nothing” to someone who has not yet learned how to combine information;
- therefore player experience and recent-role history can matter when selecting setup roles, even when the role is balanced mechanically.

Potential downstream dimensions:

- player experience;
- recent-role history;
- perceived agency;
- setup variety.

## Triage

### Strongest product-facing findings

1. **M02/M03 — Drunk-candidate choice should account for misinformation controllability and truthful Chef strength**
2. **M04 — distinguish believable misinformation from discoverable misinformation**
3. **M06/M07 — registration should consider intuitiveness and accidental confirmation leakage**
4. **M08/M09 — Spy/Recluse Chef registration is an information-strength decision, not a fixed default**
5. **M01 — information topology materially changes the value of Chef information**
6. **M11 — player experience/recent-role history can be optional setup context**

### E3 re-entry disposition

M03 is a useful future re-audit lead because it describes a Storyteller practice of making Chef Drunk when Evil seating would otherwise yield an unusually strong number. This machine pass does **not** provide the exact decision-time setup, observed alternative set, and historical choice details needed for strict E3.

No new strict E3 PASS is created by this episode.

## ML-readiness note

Per EL-ML0, these findings remain canonical source-backed semantic guidance only. They do not imply GOOD/BAD labels, numeric preference weights, or negative labels for unchosen legal Chef numbers. Any future ML-ready projection must preserve the difference between:

- observed historical choice;
- expert preference;
- legal unchosen alternative;
- explicitly rejected alternative.

## Verification disposition

No immediate human audio review is required merely to retain these findings.

Human primary-audio confirmation is required before:

- M02/M03 are used to rank Chef against other Drunk candidates;
- M04 becomes a production misinformation-quality preference;
- M06/M07/M08/M09 are converted into registration-policy weights;
- M11 affects setup role assignment by player experience;
- any item is promoted to VERIFIED evidence.

The temporary full audio and ASR workspace may be cleaned after this lightweight record is safely committed.
