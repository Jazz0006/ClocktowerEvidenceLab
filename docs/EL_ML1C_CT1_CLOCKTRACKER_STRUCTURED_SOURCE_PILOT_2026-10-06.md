# EL-ML1C CT-1 — ClockTracker Structured-Source Pilot Foundation — 2026-10-06

> Status: **FOUNDATION IMPLEMENTED / LOCAL QUALITY GREEN / LIVE R02 PROBE SUCCESS VIA GITHUB ACTIONS / R04 NEXT**
>
> Scope: one explicitly supplied public ClockTracker game ID at a time. No UUID enumeration and no broad crawler.

## 1. Why CT-1 is now active

EL-ML1B repair repeatedly reaches the same boundary:

- R04 chronology and circular order are recoverable, while exact role map / bluff IDs remain behind raw structured fields;
- R02 has strong multi-night chronology and stable game identity, while complete seats / roles and the exact Night-1 setup boundary remain unmaterialized;
- ClockTracker upstream source explicitly includes those missing fields in the public single-game payload.

Continuing rendered-page/manual reconstruction is therefore lower leverage than a bounded structured-source adapter.

## 2. Upstream contract checked

ClockTracker upstream commit inspected:

`ddd69b48e54a974c093039333a53ef7f9517bb6d`

Relevant source:

- `server/api/games/[id].get.ts` -> public single-game handler calls `fetchGame(gameId, me)`;
- `server/utils/fetchGames.ts` -> `fetchGame()` includes grimoire tokens, role / related-role data, reminders, storyteller metadata and Demon bluffs;
- `server/utils/anonymizeGame.ts` -> privacy handling may shorten names in some cases but does not remove role-structure fields;
- `prisma/schema.prisma` -> persisted token `order`, role IDs, related role IDs, alignment, death/ghost-vote state, reminders, game metadata and Demon bluffs are explicit fields.

This is capability evidence for acquisition tooling. It is not evidence about any particular Blood on the Clocktower decision.

## 3. Implemented EvidenceLab foundation

New source-normalization module:

`src/clocktower_evidence_lab/acquisition/clocktracker.py`

It provides:

- strict single-game API URL construction from an explicit UUID;
- parsing of one raw ClockTracker game JSON payload;
- preservation of game metadata, notes, Storyteller fields and Demon bluffs;
- separate preservation of every grimoire page;
- token ordering by persisted `token.order`;
- preservation of player name/ID, role ID/name, related role ID/name, alignment, death state, ghost-vote state and reminders;
- explicit completeness helper for a one-page role map;
- rejection of duplicate token-order values;
- no guessing when a role or other field is absent.

New probe:

`src/clocktower_evidence_lab/acquisition/clocktracker_probe.py`

CLI:

`clocktower-clocktracker-probe GAME_ID`

or, for a captured payload with no network dependency:

`clocktower-clocktracker-probe GAME_ID --input-json PATH`

The probe verifies that a captured payload's game ID matches the requested game.

## 4. Safety / authority boundary

The CT-1 foundation:

- normalizes source data only;
- does not create EvidenceAssertions;
- does not mark any field VERIFIED;
- does not infer missing roles or seat IDs;
- does not enumerate legal Storyteller candidates;
- does not apply recommendation policy;
- does not enumerate ClockTracker UUIDs or crawl the corpus.

Human/source-level acceptance remains separate.

## 5. Test coverage

Fixture tests verify:

- persisted circular order is normalized from `token.order` even when payload token order is shuffled;
- role / related-role / reminder / Demon-bluff fields survive normalization;
- missing role remains missing and fails the complete-role-map check;
- multiple grimoire pages remain separate instead of being flattened;
- duplicate `token.order` values are rejected;
- invalid game IDs are rejected;
- a captured payload can be parsed through the CLI without network;
- mismatched requested/payload game IDs are rejected.

Full local quality after implementation:

`168 tests passed`

## 6. Live pilot status

The local Mini MCP / conversation execution environments cannot directly reach the public ClockTracker API, but the repository already uses GitHub Actions as a network-capable acquisition runtime for C2. A bounded one-shot branch workflow therefore ran the same parser against explicit R02 ID `de5f126b-89f5-4c78-a898-f5724a93430e`.

GitHub Actions run `37393104471` succeeded and recovered:

- one grimoire page with 8 ordered tokens;
- order 0 Blackied = Drunk, related/shown Investigator;
- order 1 Dave = Imp;
- order 2 VibesMcGee = Ravenkeeper;
- order 3 Jade = Undertaker + `Red Herring` reminder;
- order 4 John = Spy;
- order 5 Ludi = Fortune Teller + `Minion` reminder;
- order 6 Amy = Empath + `Wrong` reminder;
- order 7 Jake = Slayer + `No Ability` reminder;
- Demon bluffs: Washerwoman / Recluse / Mayor;
- current raw record Storyteller field = `@Larrikin`.

This closes R02's raw seat/role/bluff retrieval gap. It does **not** by itself prove the semantic setup commitment order before the Night-1 Investigator misinformation, so R02 remains unpromoted under the no-hindsight gate.

## 7. First live acceptance targets

The first explicit-ID live target is complete:

1. R02 — `de5f126b-89f5-4c78-a898-f5724a93430e` — **LIVE PROBE SUCCESS**.

Next:

2. R04 — `ffb40a93-3d7b-42c4-bba8-bc9c363dcd30`.

For each, measure:

- single/multiple grimoire page count;
- complete ordered seat-role coverage;
- related-role coverage needed for Drunk shown-role recovery;
- Demon bluff completeness;
- match against already-retained Notes chronology;
- whether the historical decision prefix can be materialized without hindsight.

Only after those two explicit known cases work should CT-1 expand to the bounded 25-game screening batch defined by EL-ML1C.

## 8. Current route consequence

R02 is now **PARTIAL / SETUP_CHRONOLOGY_BLOCKED**, not raw-payload blocked.

The live acquisition path is validated: GitHub Actions can provide the public structured payload even when the local execution runtime has no external network route.

Use the same bounded route for R04 next. Do not return to manual rendered-page role reconstruction unless the structured source contradicts or omits a required field.
