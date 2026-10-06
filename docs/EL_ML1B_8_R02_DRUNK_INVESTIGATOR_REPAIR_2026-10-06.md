# EL-ML1B-8 — R02 Drunk-Investigator Repair — 2026-10-06

> Status: **COMPLETE / STRUCTURED SETUP RECOVERED / NOT PROMOTED — PRE-DECISION SETUP CHRONOLOGY STILL INCOMPLETE**
> Game: R02 — Jeff / @CryptCore + @Larrikin — Trouble Brewing — 2025-09-30
> ClockTracker ID: `de5f126b-89f5-4c78-a898-f5724a93430e`

## Known source-backed state

- 8 players;
- stable ClockTracker game ID;
- retained acquisition metadata previously names `@CryptCore` + `@Larrikin`; the live raw game record itself currently reports Storyteller `@Larrikin` and no co-Storytellers, so those provenance surfaces are retained rather than silently collapsed;
- Night 1 through Night 4 chronology;
- live CT-1 retrieval from GitHub Actions run `37393104471` recovered one eight-token grimoire page and the complete role map;
- order 0 Blackied = actual Drunk, related/shown role Investigator;
- order 1 Dave = Imp;
- order 2 VibesMcGee = Ravenkeeper;
- order 3 Jade = Undertaker with retained `Red Herring` reminder;
- order 4 John = Spy;
- order 5 Ludi = Fortune Teller with retained `Minion` reminder;
- order 6 Amy = Empath with retained `Wrong` reminder;
- order 7 Jake = Slayer with retained `No Ability` reminder;
- Demon bluffs = Washerwoman / Recluse / Mayor;
- Night-1 false Scarlet Woman clue is between Amy / Empath and Ludi / Fortune Teller;
- later Undertaker confirmation of Drunk;
- multi-night Fortune Teller history and later role succession.

## Canonicalization blocker

The complete circular role map and the Drunk / Investigator relation are no longer blockers.

The remaining blocker is **historical setup chronology**. The current raw game payload is a grimoire state, not a semantic setup event log. It does not establish the exact commitment order of the Drunk assignment, Red Herring, Demon bluffs and other setup information relative to the Night-1 Investigator clue.

The Notes establish the later Night-1 / multi-night information sequence, but they do not provide a complete pre-Investigator setup timeline. Later confirmation must not leak backward, and final-grimoire reminders must not be treated as timestamped setup events.

## Why this is an acquisition-channel blocker

ClockTracker upstream source confirms that public `fetchGame()` includes `player_count`, storyteller metadata, ordered grimoire tokens, token roles / related roles / reminders, and Demon bluffs.

The local Mini MCP / conversation runtime could not retrieve that public payload directly, but the bounded CT-1 GitHub Actions acquisition runtime successfully fetched and normalized the explicit R02 ID on 2026-10-06. This validates the structured-source route and closes the seating/role/bluff retrieval gap.

Disposition: **PARTIAL / SETUP_CHRONOLOGY_BLOCKED**.

No READY row is added. Do not infer the remaining setup order, rationale or alternatives from rules, final-grimoire state or later events.

## Route consequence

CT-1 has now succeeded on R02 and should be applied to R04 before further manual ClockTracker repair. The acquisition problem has shifted from raw-field access to reconstructing true historical event/setup chronology.
