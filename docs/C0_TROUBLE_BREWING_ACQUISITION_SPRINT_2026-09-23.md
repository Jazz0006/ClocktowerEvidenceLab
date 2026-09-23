# C0 Trouble Brewing Acquisition Sprint — 2026-09-23

## 1. Purpose

C0 is no longer a broad ClockTracker prevalence study.

The current Storyteller App supports Trouble Brewing only, so the research objective is to acquire enough high-value real Trouble Brewing whole games to improve and calibrate the current recommendation algorithm quickly.

Whole-game interaction remains the unit of value. DecisionSlices are derived later.

## 2. Stop condition

The sprint is considered sufficient for the current product phase when it has approximately:

- 20–30 usable public Trouble Brewing whole-game records;
- 10–15 A-grade records if the corpus supports it;
- evidence from at least 2–3 independent Storytellers;
- several games with multi-night information evolution;
- 1–2 matching ClockTracker + primary-video pairs.

These are working acquisition targets, not statistical claims.

## 3. Screening rule

### A

- full/near-full grimoire;
- detailed ordered Notes/event history;
- sufficient multi-clue context for whole-game reconstruction.

### B

- strong grimoire/reminders/bluffs/multi-page state;
- incomplete process Notes.

### C

- setup/final/result only;
- insufficient process detail for current reconstruction goals.

Unsupported scripts are rejected immediately for current scope.

## 4. Research priority

Prefer Trouble Brewing games where several of the following interact:

- Chef;
- Empath;
- Fortune Teller;
- Investigator;
- Washerwoman;
- Drunk;
- Red Herring;
- Poisoner;
- Spy/Recluse registration;
- Demon bluffs;
- information changes across multiple nights.

Do not search for one isolated clue merely because it matches a current hypothesis.

## 5. Initial discovery result

Public search/index results show that Trouble Brewing supply is abundant across ClockTracker profiles and communities. Quantity is not currently the main concern; detailed Notes and whole-game reconstructability are.

### Confirmed strong A candidate

ClockTracker game:

- recorder / Storyteller presentation: Scott / @sancho;
- script: Trouble Brewing;
- date: 2025-09-10;
- players: 14;
- game ID: `ffb40a93-3d7b-42c4-bba8-bc9c363dcd30`;
- public locator: https://clocktracker.app/game/ffb40a93-3d7b-42c4-bba8-bc9c363dcd30

The indexed public record exposes detailed setup plus Night/Day chronology through Night 7. It includes:

- Red Herring setup;
- Poisoner targets;
- Spy registration;
- poisoned information;
- Drunk Empath information;
- Fortune Teller selections/results;
- Ravenkeeper information;
- Undertaker information;
- Monk protection and poison interaction;
- Slayer action;
- executions/deaths;
- Imp self-kill / Scarlet Woman transition;
- later starpass-like Imp transition.

This is already sufficient to demonstrate the kind of multi-clue whole-game evidence the project needs.

### Additional exact Trouble Brewing public candidates queued for screening

- `72d771f4-e866-44cc-8c92-803955ce33e3` — Scott
- `b6e1d72d-dafa-45a0-af3d-e3caac6bf591` — Scott
- `44aaab56-2141-4275-b901-b457f3b43135` — Dennis | Bremen
- `0188b9d3-7d64-4a7d-8592-c4f82944ff68` — Lewis
- `d3acfcd3-b38c-44c2-8e57-e10e6df86f9b` — Sun
- `3036a587-0e7c-45d8-b51d-c209014ea7d4` — dwar
- `c2db54b5-9a1c-4310-aec4-95cf700fd48e` — LucyH
- `1ff1104c-3c3b-495c-afe3-94ac6d4bd6ad` — Brian
- `892cab15-190a-48e2-9182-2643ae91d89c` — Immortal Jack

These are discovery candidates only until field-level screening is completed.

## 6. Larger discovery pools

Indexed profile/search surfaces show multiple Trouble Brewing games in:

- Grim Scenarios-associated records, including many entries visible on the Titus profile;
- Tabletop Manchester-associated records, with many TB games visible across 2024–2025 on the Ctrl4ltMe/Nyx Stocks profile;
- BOTC Everywhere / Chill Clocktower / related communities visible in the kirabajira profile.

Profile membership is only a discovery route. It does not by itself establish who Storytold a particular game or whether the game is A/B/C.

## 7. Current constraint

The current research environment can discover and inspect search-indexed public ClockTracker pages, but direct ClockTracker API access is not available through the current web tooling. Some indexed game pages expose rich Notes while others expose only the app shell.

Therefore:

- do not infer missing fields from index absence;
- preserve exact public game IDs/URLs;
- treat search-visible detail as a lower bound until the record is directly screened;
- avoid pretending that the current candidate list is a representative random sample.

This constraint does not block the narrowed sprint because the product goal is to find enough strong Trouble Brewing games, not estimate platform-wide prevalence.

## 8. Cross-source status

A matching persistent ClockTracker game ID + exact same primary YouTube/VOD has not yet been verified.

This remains a sprint target because it validates the intended enrichment workflow:

~~~text
ClockTracker mechanical backbone
    → selective primary-video enrichment
    → rationale / social context / exact timing
~~~

## 9. Next research action

Continue screening the exact Trouble Brewing candidates first.

Promote A records immediately into the reconstruction queue, retain useful B records for selective enrichment, and normally stop on C records.

Once the usable/A-grade target is reached, stop corpus scouting and return to algorithm-facing reconstruction and calibration work.
