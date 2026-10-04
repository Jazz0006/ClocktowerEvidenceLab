# C2 Machine Semantic Findings — Fortune Teller — 2026-10-04

> Status: **MACHINE SEMANTIC REVIEW ONLY / NOT VERIFIED**
>
> Source: `Fortune Teller (Trouble Brewing)`
>
> Source ID: `podcast:1ae2e0178f68f8bf3566526c3e9ad1a8`
>
> GUID: `58598788-302a-d337-4dee-d5ccfa850b4a`
>
> ASR: `small.en`, 1,549 timestamped segments, approximately 41 minutes.

This full-episode pass reviewed all 1,549 ASR segments. It prioritizes Red Herring selection, Drunk/Poisoned misinformation trajectories, player/meta enrichment, information-network interactions and Storyteller-visible signs that impairment is becoming too obvious.

## High-value machine-understood findings

### C2-FORTUNE-TELLER-M01 — Red Herring should be selected from the information ecology, not as an isolated/random seat

**Window:** approximately `00:31:45–00:34:20`

Machine-understood meaning:

- the discussion explicitly frames Red Herring choice as something that can be coordinated with other roles' information;
- example: if Chef learns one adjacent Evil pair, place the Red Herring adjacent to that Evil cluster so Fortune Teller uncertainty preserves more than one plausible interpretation of the Chef topology;
- the Storyteller can therefore use Red Herring placement to create coherent cross-role ambiguity rather than independent noise.

Potential downstream dimensions:

- information-topology coherence;
- Chef adjacency structure;
- cross-role world preservation;
- ambiguity quality;
- Red Herring placement.

**LRE relevance:** high for the current Red Herring decision family.

### C2-FORTUNE-TELLER-M02 — player tendencies/meta can be bounded enrichment context for Red Herring placement

**Window:** approximately `00:32:06–00:33:20`

Machine-understood meaning:

- Sophie describes considering who tends to talk a lot, who tends to appear suspicious, and who the Fortune Teller is likely to focus on;
- this can make a Red Herring more likely to become a meaningful false lead rather than an irrelevant token;
- the discussion treats this as contextual judgment, not a fixed rule.

Potential downstream dimensions:

- player tendency;
- social suspicion profile;
- expected target probability;
- local meta;
- enrichment-only context.

**LRE relevance:** useful bounded player-context dimension, but should not become a universal/meta-heavy rule.

### C2-FORTUNE-TELLER-M03 — making Drunk the Red Herring can create a coherent but double-edged false narrative

**Window:** approximately `00:33:20–00:33:50`

Machine-understood meaning:

- a Drunk Red Herring can look especially suspicious because their own information may already be unreliable;
- this can help Evil by building a strong false narrative around one Good player;
- but it can also help Good if that player is executed early, because their ongoing false information stops influencing the game;
- therefore “Drunk as Red Herring” is not intrinsically good or bad; downstream trajectory matters.

Potential downstream dimensions:

- misinformation concentration;
- false-narrative coherence;
- expected lifespan;
- future information harm;
- execution externality.

**LRE relevance:** comparison dimension for Red Herring selection, not an unconditional preference.

### C2-FORTUNE-TELLER-M04 — self-Red-Herring value depends on player count and known Fortune Teller strategy

**Window:** approximately `00:34:21–00:35:29`

Machine-understood meaning:

- in smaller games, making the Fortune Teller their own Red Herring can punish the otherwise efficient strategy of repeatedly choosing oneself plus one other player to isolate results;
- smaller games let Fortune Teller cover the circle quickly, so self-Red-Herring can preserve uncertainty;
- in larger games, the speakers generally prefer not to spend the Red Herring on the Fortune Teller because broad coverage is already difficult;
- exception: if a known player strongly favors the self-check strategy, self-Red-Herring can still be an intentional anti-meta choice.

Potential downstream dimensions:

- player count;
- self-check propensity;
- search coverage rate;
- anti-meta value;
- information compression.

**LRE relevance:** unusually explicit conditional comparison for Red Herring policy; strong bounded primary-audio candidate.

### C2-FORTUNE-TELLER-M05 — Drunk Fortune Teller should usually receive a coherent longitudinal misinformation story

**Window:** approximately `00:35:44–00:37:12`

Machine-understood meaning:

- because the Storyteller cannot know the Fortune Teller's next targets in advance, improvising each result independently risks producing an obviously incoherent pattern;
- the speakers recommend having an informal model in mind for which players will “register” to the Drunk Fortune Teller so results form a believable story across nights;
- improvisation remains allowed when a player choice opens a particularly useful narrative branch.

Potential downstream dimensions:

- longitudinal misinformation;
- prior check history;
- narrative consistency;
- target-history state;
- improvisation budget.

**LRE relevance:** strong for impaired-information families and future policy/evaluation design.

### C2-FORTUNE-TELLER-M06 — consistency should be breakable when Good needs a discoverable impairment clue

**Window:** approximately `00:36:15–00:37:30`

Machine-understood meaning:

- if Good is doing poorly, the Storyteller may intentionally make the Drunk Fortune Teller's information pattern easier to recognize as impaired;
- if Good is doing well, the Storyteller may preserve the misleading narrative more carefully;
- the speakers explicitly describe breaking from the normal misinformation story when the player needs a hint that they may be Drunk.

Potential downstream dimensions:

- impairment discoverability;
- current team state;
- adaptive difficulty;
- narrative break cost;
- clue visibility.

**LRE relevance:** adaptive misinformation-policy dimension; not a blanket “balance the losing team” rule.

### C2-FORTUNE-TELLER-M07 — true information is an important part of Drunk misinformation because otherwise players can invert the channel

**Window:** approximately `00:38:20–00:39:16`

Machine-understood meaning:

- when a Drunk Fortune Teller suspects impairment, giving a truthful result can be more confusing than giving the expected false result;
- the episode explicitly links the legality of giving true information while impaired to preventing a simple “invert every result” strategy;
- therefore a healthy misinformation policy should preserve uncertainty about whether each individual result is true, rather than enforce systematic falsity.

Potential downstream dimensions:

- truth/false mixture;
- anti-inversion property;
- player expectation;
- discoverability;
- misinformation entropy.

**LRE relevance:** high-value policy boundary for Drunk/Poisoned information.

### C2-FORTUNE-TELLER-M08 — too many independent YES results can expose impairment; Storyteller should account for contradiction accumulation

**Windows:** approximately `00:17:25–00:18:31` and `00:37:15–00:38:20`

Machine-understood meaning:

- the speakers recount a game where a Fortune Teller accumulated several unrelated positive reads and should have begun suspecting impairment;
- repeatedly saying YES to whatever the player already suspects can collapse the misinformation by making Drunk/Poisoned status obvious;
- a Storyteller therefore needs to track not just the current result but the cumulative plausibility of the entire result history.

Potential downstream dimensions:

- contradiction accumulation;
- number of independent positive clusters;
- impairment detectability;
- longitudinal plausibility;
- suspicion reinforcement cost.

**LRE relevance:** useful evaluation signal for misinformation trajectory quality.

### C2-FORTUNE-TELLER-M09 — a real long-lived poisoned Fortune Teller shows that survival itself can become evidence about information reliability

**Window:** approximately `00:15:14–00:15:49`

Observed game narrative:

- a real Fortune Teller survived unusually late;
- they had been poisoned for a long period;
- Evil had little reason to kill them because their information was already neutralized;
- other players found the prolonged survival suspicious.

Machine-understood lesson:

- continued survival of a nominally high-priority information role can be part of the public evidence ecology;
- impairment can change not only the content of information, but also Evil's incentives about whether to kill the source.

Potential downstream dimensions:

- role survival time;
- Evil kill incentive;
- public suspicion;
- impairment plausibility;
- information-source threat value.

**LRE relevance:** contextual/evaluation evidence, not a direct Storyteller candidate comparison.

### C2-FORTUNE-TELLER-M10 — Red Herring and Drunk policy should avoid collapsing into a fixed “maximum misinformation” objective

**Windows:** approximately `00:31:45–00:39:16`

Machine-understood meaning:

- several choices that appear maximally harmful to Good can backfire by making the false mechanism too visible;
- Drunk Red Herring can cause early self-cleansing;
- too many suspicious YES results can reveal impairment;
- perfectly systematic false information is invertible;
- the recurring objective is **believable, durable uncertainty**, not maximum immediate falsehood.

Potential downstream dimensions:

- misinformation durability;
- detectability;
- immediate impact vs future credibility;
- world preservation;
- policy restraint.

**LRE relevance:** general qualitative policy principle across Red Herring and impaired-information families.

## Strict historical-evidence result

**No new strict historical same-state policy case is promoted from this episode.**

The strongest bounded policy candidates are:

1. **M04** — self-Red-Herring vs another Good player conditioned by player count and known self-check behavior;
2. **M01** — Red Herring placement that preserves ambiguity with Chef topology;
3. **M05/M06/M07/M08** — longitudinal Drunk Fortune Teller misinformation design.

These are explicit generic preferences/conditions, but the episode does not preserve a single historical Storyteller decision with the exact production state plus complete same-state candidate domain. Under EL-LRE semantics, they remain source-backed qualitative dimensions / review targets rather than inferred rankings over all legal candidates.

## LRE-aware triage

This episode materially strengthens the **Red Herring** family, which is already Priority 1 in the current EL-LRE matrix.

Strongest future bounded primary-audio windows:

- `00:32:06–00:34:20` — player tendency + Drunk + Chef-topology Red Herring construction;
- `00:34:21–00:35:29` — self-Red-Herring preference in small games and anti-meta condition;
- `00:35:44–00:39:16` — coherent Drunk Fortune Teller misinformation, adaptive discoverability, truthful-result mixing and anti-inversion logic.

No immediate promotion is made automatically. The current EL-LRE-WW1 Washerwoman review remains the immediate bounded review target; these Fortune Teller windows should be added to the already-located Red Herring / impaired-information lead pool without displacing WW1.
