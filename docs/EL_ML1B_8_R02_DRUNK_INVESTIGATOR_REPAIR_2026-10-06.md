# EL-ML1B-8 — R02 Drunk-Investigator Repair — 2026-10-06

> Status: **COMPLETE / NOT PROMOTED / RAW CLOCKTRACKER PAYLOAD REQUIRED**
> Game: R02 — Jeff / @CryptCore + @Larrikin — Trouble Brewing — 2025-09-30
> ClockTracker ID: `de5f126b-89f5-4c78-a898-f5724a93430e`

## Known source-backed state

- 8 players;
- Storytellers `@CryptCore` and `@Larrikin`;
- stable ClockTracker game ID;
- Night 1 through Night 4 chronology;
- actual Drunk believes they are Investigator;
- Night-1 false Scarlet Woman clue between Empath and Fortune Teller;
- later Undertaker confirmation of Drunk;
- multi-night Fortune Teller history and later role succession.

## Canonicalization blocker

The repository still lacks the complete circular seating / actual-role map and therefore cannot identify the Drunk-Investigator, Empath and Fortune Teller seats with source-backed identifiers.

The exact setup commitments and first-night ordering before the Investigator clue are also incomplete. Later confirmation must not leak backward.

## Why this is an acquisition-channel blocker

ClockTracker upstream source confirms that public `fetchGame()` includes `player_count`, storyteller metadata, ordered grimoire tokens, token roles / related roles / reminders, and Demon bluffs.

Those fields are therefore available in the source model, but the current EvidenceLab runtime cannot retrieve the raw public payload. Search/render surfaces do not expose all token-role fields, and the local execution environment has no external network path.

Disposition: **PARTIAL / RAW_STRUCTURED_SOURCE_BLOCKED**.

No READY row is added. Do not infer the missing seats, roles, setup order, rationale or alternatives from rules or later events.

## Route consequence

R02 and R04 now share the same repeated blocker. The next higher-leverage action is the bounded EL-ML1C ClockTracker structured-source pilot rather than another manual one-off reconstruction.
