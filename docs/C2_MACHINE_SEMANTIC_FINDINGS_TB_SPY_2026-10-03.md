# C2 Machine Semantic Findings — Spy (Trouble Brewing) — 2026-10-03

> Status: **MIXED — M09/M10 PRIMARY-AUDIO HUMAN REVIEWED; OTHER FINDINGS REMAIN MACHINE SEMANTIC / NOT VERIFIED**
>
> Source: `Spy (Trouble Brewing)`
>
> Source ID: `podcast:13143913be3fd5fd1ff9d20e7019fee0`
>
> GUID: `afb44bf4-6d85-4831-935c-24f2d4c657e6`
>
> ASR: `small.en`, 2,467 timestamped segments, approximately 2h02m.
>
> Guest provenance: Ed Gabriel describes himself in the episode as a TPI “minion”, convention Storyteller and playtest participant. Per project-owner calibration, Cult of the Clocktower hosts/guests are trusted Storyteller clue sources. This machine pass does not itself promote any finding to VERIFIED.
>
> The complete transcript was reviewed in bounded time windows. Full audio and full ASR remain temporary external artifacts and are not committed to Git.

## High-value machine-understood findings

### C2-SPY-M01 — when Evil is already dominating, Storyteller may choose to let Spy register Evil rather than continue protecting the Spy

**Window:** approximately `00:14:59–00:15:49`

Machine-understood meaning:

- the guest recounts a game in which a Spy had established a convincing Washerwoman bluff;
- after a neighboring player died and the Spy became adjacent to an Empath, the Storyteller chose to have the Empath read the Spy as Evil;
- the explicit contextual reason is that Evil was already “stomping”, so continuing to make the Spy look Good was not necessary;
- the Spy immediately adapted by switching from the Washerwoman bluff to a Recluse claim.

Potential downstream dimensions:

- registration choice;
- current team-state context;
- player adaptability;
- balance intervention;
- public narrative.

**E3 disposition:** promising concrete historical Storyteller choice, but this pass does not recover enough exact committed game state and legal alternative detail to call it E3 PASS. Retain as a re-audit candidate if Host later needs Empath/Spy registration evidence.

### C2-SPY-M02 — Spy triggering Virgin is often worth allowing because the Evil sacrifice itself is a meaningful cost

**Window:** approximately `00:29:49–00:32:23`

Machine-understood meaning:

- the guest strongly favors allowing Spy to trigger Virgin at least some of the time;
- rationale: Spy gives up both life and ongoing grimoire access in exchange for appearing strongly Good, so the play already contains a meaningful Evil-side cost;
- doing this occasionally also prevents a stable meta where “Virgin-triggered execution proves the nominator cannot be Spy”;
- the source does not claim “always trigger”; later discussion explicitly notes situational exceptions.

Potential downstream dimensions:

- registration;
- anti-meta;
- ability preservation vs sacrifice;
- player agency;
- information strength.

### C2-SPY-M03 — Evil players telling Storyteller their current bluff can enable coherent downstream registration/information choices

**Window:** approximately `00:59:31–01:00:43`

Machine-understood meaning:

- if Spy is going to nominate Virgin and an Undertaker may see the executed character, the Storyteller may otherwise have to guess what identity would best support or challenge the Spy's current narrative;
- the guest recommends that players sometimes privately tell the Storyteller what they are bluffing;
- this does not compel the Storyteller to support the bluff, but it converts an accidental mismatch into an intentional Storyteller choice.

Potential downstream dimensions:

- Evil-side claimed role as enrichment context;
- Undertaker / Ravenkeeper output choice;
- narrative continuity;
- DecisionTrace context.

This directly supports the project's long-term decision-context model including Evil-side claims as optional enrichment input.

### C2-SPY-M04 — Spy registration should preserve a healthy information ecology; do not contaminate every Good information source at once

**Window:** approximately `01:43:27–01:46:20`

Machine-understood meaning:

- the speakers reject a fixed rule for how often first-night roles should see Spy as Good/Townsfolk/Outsider;
- if Good already has very little reliable information, for example a Drunk ongoing-information role plus only a few first-night sources, they prefer preserving real first-night information more often;
- if Good is otherwise in a strong informational position, Storyteller has more room to use Spy registration as misinformation;
- the stated goal is to ensure there remains enough meaningful information for Good to reason with rather than constructing a game where all apparent information is false.

Potential downstream dimensions:

- healthy-information ecology;
- misinformation strength;
- confirmation-chain density;
- current setup information budget;
- registration policy.

This is one of the strongest product-facing findings in the episode.

### C2-SPY-M05 — first-night Spy registration can be adjusted for player experience and bluffing difficulty

**Window:** approximately `01:43:43–01:45:09`

Machine-understood meaning:

- a Spy player who is socially regarded as suspicious may benefit from being seen by Washerwoman so their bluff has some support;
- a player who struggles to bluff may benefit from Librarian information such as a Drunk registration that gives them a plausible escape route;
- the guest warns against doing this reliably enough to create a group meta;
- player experience and social perception therefore act as context for registration decisions, not as global role bonuses.

Potential downstream dimensions:

- player experience;
- social trust baseline;
- registration;
- anti-meta;
- narrative-route diversity.

### C2-SPY-M06 — setup can include redundant detection paths when Spy strength and player experience create a large imbalance risk

**Window:** approximately `01:38:12–01:39:57`

Machine-understood meaning:

- the guest says Trouble Brewing usually works well without highly engineered setups;
- however, in an imbalanced group, they may include both Investigator and Recluse so that the Investigator can point at Recluse when a new player draws Spy, or point at the actual Spy when an experienced player draws it;
- they may also allow another first-night role to see the Spy when they judge the Evil side would otherwise be too strong;
- this is explicitly adaptive setup design based on expected player performance.

Potential downstream dimensions:

- setup reasoning;
- player experience;
- confirmation redundancy;
- expected team strength.

**Policy-sensitive:** this is a general Storyteller practice, not authorization for a deterministic player-skill balancing formula.

### C2-SPY-M07 — Chef information with Spy/Recluse need not default toward the smallest possible number

**Window:** approximately `01:46:54–01:49:04`

Machine-understood meaning:

- the guest describes a large-game situation with Recluse and multiple Evil players adjacent;
- rather than automatically using Spy/Recluse registration to minimize Chef's number, they argue that a large truthful-or-legally-supported number can create a stronger and more interesting information puzzle;
- a large Chef number can force both Good and Evil to meaningfully adapt from day one;
- the preferred value depends on the narrative/information consequences, not a blanket “lower is safer” rule.

Potential downstream dimensions:

- registration;
- information strength;
- early-game world reduction;
- Evil bluff pressure;
- narrative-route diversity.

### C2-SPY-M08 — Empath usually reading Spy as Good is a tendency, not a rule; adjacency structure can justify an Evil registration

**Window:** approximately `01:49:40–01:50:24`

Machine-understood meaning:

- the guest says they would register a Spy as Good to an Empath more often than not;
- however, when Spy and Imp are both adjacent to a sober Empath, they regard multiple legal outputs as potentially interesting and tense;
- the choice should follow the narrative and information consequences of the exact neighborhood rather than a hard default.

Potential downstream dimensions:

- Empath registration;
- adjacency topology;
- information strength;
- narrative consequence.

### C2-SPY-M09 — exact-Spy display to Undertaker can be best when the truth itself creates a harder social puzzle

**Window:** approximately `01:51:22–01:52:43`

Machine-understood meaning:

- a concrete historical example has Spy bluffing Investigator and accusing either Undertaker or Fortune Teller of being Spy;
- after the Spy is executed, the Storyteller chooses to show the actual Spy token to the real Undertaker;
- rationale: the Undertaker already knows they themselves are not Evil, so giving the true Spy result creates a socially difficult but meaningful position where the Undertaker must publicly insist that the accuser really was Spy while already under suspicion;
- the value comes from the interaction between mechanically correct information and the existing public narrative, not from simply helping or hurting one team.

Potential downstream dimensions:

- Undertaker registration;
- public narrative;
- information believability;
- social credibility;
- truth-as-misinformation.

**Verification / LRE disposition:** **VERIFIED HISTORICAL CHOICE + RATIONALE** by primary-audio review on 2026-10-04. Human review confirmed the historical truthful Spy display and the explicit social-narrative rationale. No explicit alternate token was discussed, so this is not a source-backed pairwise comparison. The project owner's view that this is an interesting play pattern is separate design opinion.

### C2-SPY-M10 — sometimes establish a truthful Spy/Undertaker precedent to preserve later poisoned/drunk Undertaker ambiguity

**Window:** approximately `01:52:46–01:53:31`

Machine-understood meaning:

- the guest notes that having a Spy trigger Virgin and then showing Spy to a healthy Undertaker can establish a precedent;
- later, if a Drunk or poisoned Undertaker sees “Spy” after a Virgin-triggered execution, the table cannot safely treat that exact pattern as mechanically impossible or Storyteller-uncharacteristic;
- occasional truthful registration choices therefore have future anti-meta value beyond the immediate night.

Potential downstream dimensions:

- cross-game / group meta;
- registration precedent;
- misinformation believability;
- anti-meta;
- future flexibility.

**Verification / LRE disposition:** **VERIFIED DESCRIPTIVE POLICY-DIMENSION EVIDENCE** by primary-audio review on 2026-10-04. Human review confirmed the anti-meta / precedent rationale, but not an explicit Storyteller recommendation.

### C2-SPY-M11 — Star Pass target should consider the support network and player experience, not only which Minion is most trusted

**Window:** approximately `01:53:33–01:56:28`

Machine-understood meaning:

- the speakers call Star Pass highly situational and often favor the Minion in the strongest position;
- the guest gives a concrete counterexample: they passed Demonhood to a less-trusted Baron instead of the well-trusted Spy because the Spy was already in a strong position to support the new Demon;
- player experience/fun also influenced the choice: the Baron player had recently had low-agency or difficult games;
- the resulting Spy + new-Demon support structure produced a close, successful game.

Potential downstream dimensions:

- Star Pass;
- Evil support topology;
- player experience;
- trusted-helper value;
- narrative quality.

**Verification / LRE disposition:** **PRIMARY-AUDIO HUMAN VERIFIED on 2026-10-05.** Human review confirmed both parts of the source meaning: (1) choosing the Minion in the strongest / most trusted position is a common Star Pass tendency, and (2) this historical case is a counterexample, not a reversal of that tendency. The Storyteller owned the successor choice, compared a less-trusted Baron with a well-trusted Spy, and chose Baron because retaining the trusted Spy as support for the new Demon had higher value in that particular state. Player experience/fun was also a real secondary consideration. Relation: **OBSERVED_CHOICE + EXPLICIT RATIONALE + SAME-STATE ALTERNATIVE**. This supports `do not always choose the most trusted Minion`; it does **not** support `prefer the less-trusted Minion`.

### C2-SPY-M12 — poisoned Spy misinformation should remain bounded by actual legal semantics, even when used theatrically

**Window:** approximately `01:56:31–02:01:16`

Machine-understood meaning:

- the episode discusses playful ways to alter what a poisoned Spy sees;
- the hosts explicitly surface a rules boundary: even when poisoned, the Storyteller should stay within what the game legally permits rather than importing arbitrary material from another script;
- one speaker favors a more permissive “rules is fun” approach, so this segment contains disagreement rather than a stable policy recommendation.

Potential downstream dimensions:

- impaired information;
- legality boundary;
- Storyteller theater;
- rules-vs-style distinction.

This should remain descriptive and should not drive production policy without a separate current-rules audit.

## Triage

### Strongest product-facing findings

1. **M04 — preserve a healthy information ecology when deciding Spy registration**
2. **M05 — player experience/social trust can be optional enrichment context**
3. **M07 — registration should optimize information consequence, not mechanically minimize output**
4. **M08 — Empath/Spy registration depends on exact adjacency topology**
5. **M09/M10 — truthful Spy registration can itself be misleading and can preserve future ambiguity**
6. **M11 — Star Pass should consider support topology, not only recipient trust**

### Possible future E3 re-audit leads

The following are worth retaining for later, but do **not** currently satisfy strict E3 in this machine pass:

- M01 — Spy deliberately registered Evil to Empath because Evil was already dominating;
- M09 — exact Spy shown to Undertaker in a socially adversarial bluff context;
- M11 — Demonhood passed to a less-trusted Baron while trusted Spy remained as support.

A future re-audit would need the exact decision-time state, recoverable legal alternatives, and a generic Host feature mapping.

## Verification disposition

No immediate human audio review is required merely to retain these findings.

Human primary-audio confirmation is required before:

- M01 becomes a team-balance registration policy;
- M04/M05/M07/M08 are converted into production preference weights;
- M09/M11 are proposed as E3-qualified historical cases;
- any item is promoted to VERIFIED evidence.

The temporary full audio and ASR workspace may be cleaned after this lightweight record is safely committed.
