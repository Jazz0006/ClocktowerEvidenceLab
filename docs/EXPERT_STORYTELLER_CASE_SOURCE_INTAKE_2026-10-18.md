# Expert Storyteller Decision Case Intake — 2026-10-18

> **Status: SOURCE-REVIEW CANDIDATES ONLY / NOT CANONICAL EVIDENCE / NOT BENCHMARK READY**
>
> This is a source-intake and screening note, **not** a replacement for the existing Source → Fragment → Assertion → Reconstruction/DecisionSlice pipeline. No new persistence schema, model policy, or legality engine is introduced.

## Purpose and routing

Collect **context → Storyteller-controllable choice → explicitly discussed alternatives → source-stated reason → potential inference effects** without making up a complete game where only a teaching example exists.

Routes:
1. Real game with provenance-backed setup, chronological decisions and events → existing EvidenceLab reconstruction, immutable event history, derived `botc.tb.game-snapshot` and historical-prefix DecisionSlice.
2. Designer/expert authored example with only local partial facts → keep as expert-guidance source and explicit bounded decision explanation. Unknown seats, roles, event chronology and actual outcome remain UNKNOWN.
3. Full artificial setup by a writer → keep as authored hypothetical, **never** label historical expert choice. If house rules deviate from official TB, exclude from standard-rule evaluation.
4. Video/podcast candidates → source ID, URL, timestamps, short paraphrase; machine transcription locators cannot become VERIFIED without primary review.

Do not treat `expert discussed option A` as `expert used A`, or `expert used A` as `expert rejected B`. Distinguish source-backed assertions from our interpretations. Only pre-decision historical prefix is model input; outcome / chosen result cannot leak into the input.

## New source intake — bounded first batch

### SCOUT-ST-01 — Poisoned Empath: truthful value can mislead

- **Source:** Here for Games, *Blood on the Clock Tower story teller tips*, 2025-03-23; tips credited on page to Danielle (@danielleisalwaysevil).
- **Locator:** https://herefor.games/knowledge/blood-on-the-clock-tower-story-teller-tips/ — paragraph beginning “When deciding whether to show a Droisoned player ...”.
- **Source kind:** Authored illustration, **not a documented played game**.
- **Local facts as stated:** Empath David between Baron Mark and Saint Jo receives `1` on Night 1. Mark is executed during Day 1. David's neighbours for Night 2 are Saint Jo and Imp Andy. David is poisoned on Night 2.
- **Choice family:** Impaired Empath information on Night 2; result is Storyteller-controlled after player Poisoner action, not a chance to replace the Poisoner's chosen target.
- **Explicitly contrasted alternatives:** give `0` (false in this example) to conceal the Imp; or give `1` (true here) to leave plausible blame on the Saint.
- **Source-stated explanatory factor:** inference/attribution, not simply whether a number is factually true. A true result may better advance an evil-world interpretation.
- **Not established:** actual historical choice, later player claims, full seating and role map, eventual outcome, individual player experience. **Do not assign a chosen winner to this comparison.**
- **Cross-reference:** Existing EvidenceLab `docs/EL_LRE_EM1_EMPATH_MISINFORMATION_VERIFIED_HANDOFF_2026-10-04.md` contains *independently sourced* podcast guidance about truthful 1 following a previous 0, and detectability versus misinformation. Avoid duplicating as a new historical benchmark; assess whether source independence adds useful comparative support.
- **Status:** text-source reviewed in research; `UNVERIFIED` EvidenceLab promotion.

### SCOUT-ST-02 — Spy: opposite registrations within one night

- **Source:** Blood on the Clocktower official Wiki, *Spy*, Examples.
- **Locator:** https://wiki.bloodontheclocktower.com/Spy — examples paragraph “The Spy neighbours the Imp and the Empath.”
- **Source kind:** Official rules/designer *illustrative example*, not an observed game.
- **Local facts as stated:** Spy is adjacent to Imp and Empath. Chef learns `1` when Spy is registered evil. Later in the same night, Empath learns `0` when Spy is registered good.
- **Explicit choices/results:** Interaction-local registration of Spy differs for Chef and Empath.
- **Demonstrated principle:** registrations are contextual rather than a permanent seat-level global property. Information between roles can intentionally create a puzzle.
- **Unknown:** identity/status of Empath's other alive neighbour, all other seats, whether the Storyteller selected this pair for balance, actual outcome.
- **Use:** Rules/strategic reasoning *example* after verified interpretation, **not** a real-game historical training label.
- **Status:** text-source reviewed in research; `UNVERIFIED` EvidenceLab promotion.

### SCOUT-ST-03 — Cross-information confirmation cascade (warning)

- **Source:** Steven Medway, official The Pandemonium Institute blog, *Behind the Curtain #7: Balance* (published 2024-08-15).
- **Locator:** https://bloodontheclocktower.com/blogs/news/behind-the-curtain-7-balance — “Storyteller Meddling”.
- **Source kind:** Designer's deliberately excessive/illustrative sequence, **not a verified actual game**.
- **Locally stated sequence:** Washerwoman is shown the Mayor; Ravenkeeper also learns Mayor's true character; Empath provides alignment-supporting information about the same Mayor; Fortune Teller excludes Mayor as Demon; when Mayor is attacked at the end, the Poisoner dies instead.
- **Designer’s point:** multiple individually defensible Storyteller-controlled choices can accumulate to unhelpful levels of confirmation, reducing a fair reasoning challenge.
- **Do not infer:** unique seats, actual order for earlier events, any numerical win probability, actual expert selection of this as a good configuration.
- **Use:** qualitatively test model reasoning about **whole-bundle confirmation**; avoid hard-coding prohibition against confirming a Mayor.
- **Status:** text-source reviewed in research; `UNVERIFIED` EvidenceLab promotion.

### SCOUT-ST-04 — Detailed setup example with NONSTANDARD distribution (quarantine)

- **Source:** 蒹葭, 游民星空转载 *《血染钟楼》说书人手册 — 组合与配牌*, 2022-04-28.
- **Locator:** https://www.gamersky.com/handbook/202204/1478895_5.shtml — “2、邪恶说书人”.
- **Source kind:** Author-created hypothetical 10-seat setup, NOT a played game. The article explicitly encourages a 10-player **6/1/2/1** baseline instead of standard **7/0/2/1**.
- **Seating in source:** 1 Monk, 2 Baron, 3 Drunk shown Undertaker, 4 Recluse, 5 Investigator, 6 Poisoner, 7 Slayer, 8 Saint, 9 Chef, 10 Imp.
- **Initial described information:** Investigator learns “4 or 9 is Baron” using a Recluse registration; Chef receives `0`. Demon bluffs: Fortune Teller / Soldier / Butler.
- **Actual category counts in this constructed example:** 4 Townsfolk / 3 Outsiders (Drunk, Recluse, Saint) / 2 Minions (Baron, Poisoner) / 1 Demon. This follows a modified 6/1/2/1 starting point and Baron +2 Outsiders; it **does not** follow strict official ten-player TB distribution with Baron (5/2/2/1).
- **Meaning:** Author proposes an unusually harsh evil-favouring construction and explains its impact on role narratives and available counterplay.
- **Admission:** `HOUSE_RULE_VARIANT; EXCLUDE_FROM_STANDARD_TB_CANONICAL_REPLAY_AND_POSITIVE_TRAINING`. Retain rationale as **unverified author opinion**, not official expert preference or game outcome.
- **Status:** text-source reviewed in research; **QUARANTINED for strict-TB decision training**.

### SCOUT-ST-05 — Recluse can change interpretation across nights

- **Source:** Blood on the Clocktower official Wiki, *Recluse*, Examples.
- **Locator:** https://wiki.bloodontheclocktower.com/Recluse — examples section.
- **Source kind:** Official illustrative examples, not actual recorded game.
- **Local facts:** An Empath neighbouring Recluse and Monk learns `1`, then learns `0` on the following night (illustrating differing Recluse registration); a separate Investigator example presents Recluse or Saint as Scarlet Woman.
- **Principle:** Registration decisions are interaction-local and can change between nights; such changes can influence players' ability to reason.
- **Not established:** full histories, storyteller motives, player claims or outcome. The two Wiki examples must **not** be combined into one game.
- **Status:** text-source reviewed in research; `UNVERIFIED` EvidenceLab promotion.

## Existing REAL-game seeds — reuse rather than recreate

Current source-of-truth in this repo:
- `docs/EL_ML1B_READY_HISTORICAL_BENCHMARK_V1.json`: 8 canonical historical decision seeds across 4 game groups; do **not** duplicate under SCOUT IDs.
- `docs/EL_ML1B_R04_D04_CANONICAL_SEED_V1.json`: R04 ClockTracker Drunk-Empath Night-1, recovered chronological setup and Night-1 evidence.
- `docs/EL_ML1B_G01_DP_R02_CANONICAL_SEED_V1.json`: Ben Burns Drunk-Empath information and explicit alternate rejection as source-backed historical evidence.
- `docs/EL_LRE_EM1_EMPATH_MISINFORMATION_VERIFIED_HANDOFF_2026-10-04.md`: already VERIFIED podcast-derived rationales; not the same evidential category as the five authored illustrations above.

Do **not** relabel the 5 SCOUT items as 5 READY complete-game decision points. At present they are 5 carefully bounded *source-local cases*, 0 new full-game historical reconstructions and 0 promoted verified DecisionSlices.

## Next operational steps (no schema change)

1. Use the existing Source / EvidenceFragment / EvidenceAssertion pipeline to register source URLs and bounded observations **only after checking for duplicate Source records**. No ad-hoc second schema/database.
2. For case candidates with actual game video or ClockTracker IDs, prioritize whole-game setup, timestamped ordered choices/events, historical prefix and explicit rationale; materialize standard V1 state only from verifiable facts.
3. For guides/videos, use short article paragraphs or timestamped review windows; classify actual decision vs suggested option vs cautionary counterexample; promote only after appropriate primary-source verification.
4. Prioritize **new historical whole-game** evidence over more principle-only prose: R04-D05 repair, then existing partial prefixes, then bounded ClockTracker acquisition if justified by existing roadmap.
5. Host/ModelLab may assemble decision/prefix + expert guidance for an LLM blind study; **Host does not need pre-enumerated legal candidates to make an AI recommendation**. Never score or label choices as good/bad at EvidenceLab ingestion.

## Copyright

Store URLs, document anchors, short factual paraphrases and tiny necessary quotes only. No wholesale mirrored articles or complete copyrighted video transcripts in Git.