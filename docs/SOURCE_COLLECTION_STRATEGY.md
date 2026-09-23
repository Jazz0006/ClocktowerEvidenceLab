# External Source Collection Strategy

## 1. Goal

Build a broad but provenance-aware corpus of **whole real games** that can become the primary empirical reference for Storyteller research.

The acquisition target is not an isolated clue and not a preselected Storyteller decision.

The target is a reconstructable game history that preserves enough setup, information, state changes and outcome context to study how multiple clues interact across time.

Decision slices may later be derived from that history, but they are not the primary source-selection unit.

The first objective is not maximum volume. It is a repeatable process with low enough human cost that the corpus can grow continuously without discarding provenance or uncertainty.

## 2. Current source priority

Source priority is based on **whole-game reconstructability and expert relevance**, not platform prestige alone.

### Tier A — high-fidelity structured real-game records

Highest immediate research priority.

The main candidate is public ClockTracker records, especially games recorded by independently verifiable experienced/trusted Storytellers.

A strong Tier-A record may include:

- Storyteller identity;
- script and player count;
- full seating / role grimoire;
- related/shown roles where applicable;
- Demon bluffs;
- reminder tokens such as Drunk / Poisoned / Red Herring;
- alignment and role changes;
- death / ghost-vote state;
- multiple grimoire pages representing successive states;
- detailed Notes containing night actions, delivered information, nominations/executions or post-game explanation;
- final result.

ClockTracker quality is heterogeneous. Platform membership alone does not make a record Tier A; the record must pass screening.

### Tier B — expert/trusted Storyteller primary recordings

Examples include official TPI games and games run by independently verifiable experienced/trusted Storytellers.

Their main value is enrichment and verification where structured records are incomplete:

- spoken Storyteller rationale;
- player claims and bluff development;
- table belief / social state;
- exact timing of actions and information;
- context omitted from structured notes.

A primary recording may still be the best source for a game when no high-fidelity structured record exists.

### Tier C — other high-fidelity primary real-game recordings

Useful for real-game generalization and later user-population research even when Storyteller expertise is not independently established.

### Tier D — community reports / postmortems / discussions

Useful for:

- explicit rationale;
- unusual interaction discovery;
- source leads;
- locating stronger primary or structured records.

Do not treat them as equivalent to a reconstructable primary game.

## 3. ClockTracker suitability gate

The current product scope is **Trouble Brewing only**. Other scripts are outside the present Storyteller App capability and must not consume C0 screening effort.

C0 is therefore no longer a platform-wide 50–100 game prevalence study. It is a bounded **Trouble Brewing evidence-acquisition sprint** whose purpose is to find enough high-value real games to improve the current Storyteller recommendation algorithm quickly.

Immediate target:

- discover roughly 20–30 usable public Trouble Brewing whole-game records;
- promote roughly 10–15 to A-grade if the public corpus supports it;
- cover at least 2–3 independent Storytellers when identity can be established;
- include several games with multi-night information evolution;
- seek 1–2 same-game ClockTracker + primary-video pairs for enrichment workflow validation.

Records from unsupported scripts are screened out immediately with a scope reason such as `UNSUPPORTED_SCRIPT_CURRENT_SCOPE`; they are not reconstructed.

Classify Trouble Brewing candidates approximately as:

~~~text
A
  full/near-full grimoire
  + detailed ordered Notes or equivalent event history
  + enough information to reconstruct interacting clues

B
  strong grimoire state
  + reminders / bluffs / multi-page state where present
  + incomplete event Notes

C
  setup/final state/result only
  or too little process detail for whole-game reconstruction
~~~

Prioritize games where several information mechanisms interact, for example:

- Chef / Empath / Fortune Teller / Investigator / Washerwoman;
- Drunk;
- Red Herring;
- Poisoner;
- Spy / Recluse registration effects;
- Demon bluffs;
- information that evolves across multiple nights.

Do not return to isolated-clue cherry-picking. The desired unit is still the whole game and its interacting information bundle.

The gate is satisfied when the project has a sufficiently useful Trouble Brewing corpus for algorithm calibration; it does **not** require estimating ClockTracker-wide A/B/C prevalence.

Important implementation finding already established from ClockTracker's current public code:

- the grimoire supports multiple pages and a new page clones the prior page before independent edits;
- `GrimoireSnapshot` is edit/restore history, **not** an automatic semantic Night-1/Night-2 timeline;
- there is no confirmed canonical structured night-action/event-log model in the inspected code;
- detailed Notes therefore remain important for reconstructing chronological actions and delivered information.


## 4. Source census before cherry-picking

For priority Storytellers and structured collections, maintain a census or reproducible sample frame rather than searching only for cases matching a current hypothesis.

A source inventory record should preserve:

- discovered;
- screened;
- reconstructable;
- selected;
- rejected;
- rejection reason;
- collection/sampling path.

This creates a denominator and makes selection bias visible.

## 5. Screening pass

Do not fully reconstruct every discovered game.

A cheap screening pass should determine:

- Storyteller identity and whether expertise/trust can be evidenced;
- script and approximate player count;
- whether setup/seating is recoverable;
- whether Demon bluffs and setup modifiers are present;
- whether ordered night decisions and delivered information are recoverable;
- whether multiple grimoire states are available;
- whether detailed Notes exist;
- whether Storyteller commentary/rationale exists;
- whether player/table context can be established;
- which phases are reconstructable.

The screening grade measures reconstruction value/cost only. It is not a Storyteller-quality score.

## 6. Reconstruction selection

Prefer a balanced queue and preserve whole-game bundles.

Do not retain only:

- spectacular games;
- controversial games;
- algorithm failures;
- strange role interactions;
- games containing one desired clue.

Track selection reason.

Recommended reasons:

~~~text
EXPERT_SOURCE_CENSUS
SYSTEMATIC_SAMPLE
RANDOM_SAMPLE
TARGETED_RESEARCH_CASE
COMMUNITY_SUBMISSION
ALGORITHM_FAILURE_REPORT
OTHER
~~~

## 7. Multi-source enrichment

When the same game has both a structured record and a primary recording, prefer linking them rather than choosing one and discarding the other.

A practical enrichment model is:

~~~text
ClockTracker / structured record
    → mechanical game state and concise ordered notes

primary video/audio
    → missing timing
    → spoken rationale
    → claims / bluff development
    → table belief and social context
~~~

Conflicts between sources remain explicit evidence disagreements; one source must not silently overwrite another.

## 8. Initial expert coverage strategy

The first useful corpus should contain multiple independent Storytellers before drawing strong policy conclusions.

After the ClockTracker suitability gate, choose several **whole games** from at least two independently evidenced experienced/trusted Storytellers.

Selection should favor games where multiple information sources interact over time, not games chosen because one isolated decision is interesting.

The purpose is schema/workflow validation and expert independence, not statistical representativeness.

## 9. Human-in-the-loop automation

AI/tooling may assist with:

- ClockTracker record screening;
- structured-field extraction;
- Notes parsing;
- transcript keyword search;
- candidate timestamp discovery;
- proposed semantic event extraction;
- duplicate/cross-source game detection;
- source metadata normalization.

AI proposals are not evidence by themselves.

Human verification remains required for evidence promoted to VERIFIED/GOLD.

## 10. Collection success metrics

Track:

- records discovered;
- records screened;
- A/B/C reconstructability distribution;
- whole games reconstructable to useful depth;
- games with ordered multi-clue information history;
- expert Storyteller independence count;
- script and player-count coverage;
- games with linked structured + video sources;
- verified decisions derivable from reconstructed games;
- average human effort per reconstructable whole game;
- average incremental effort to enrich a structured record with video evidence.

The primary collection metric is no longer raw decision count. It is the number and diversity of **trustworthy whole-game reconstructions** that preserve interacting information over time.
