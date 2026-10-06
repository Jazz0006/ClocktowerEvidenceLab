# EL-ML1C CT-1 — ClockTracker Structured-Source Pilot Foundation — 2026-10-06

> Status: **FOUNDATION IMPLEMENTED / LOCAL QUALITY GREEN / LIVE R02 + R04 PROBES SUCCESS VIA GITHUB ACTIONS / STRUCTURED SOURCE LANE VALIDATED**
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
- token ordering by persisted `token.order` with original source index as a stable tie-breaker;
- preservation of player name/ID, role ID/name, related role ID/name, alignment, death state, ghost-vote state and reminders;
- explicit completeness helper for a one-page role map;
- explicit `orders_unique` flag for malformed/ambiguous snapshots rather than silent repair or whole-game rejection;
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
- duplicate `token.order` values are preserved deterministically and flagged `orders_unique=false`;
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

R04 was then probed with explicit ID `ffb40a93-3d7b-42c4-bba8-bc9c363dcd30`.

- raw-inspection run `37447792091` recovered 14 historical grimoire snapshots plus Demon bluffs;
- initial returned snapshot `79346` has a complete 14-token role map;
- Hylinn = Drunk with related/shown Empath;
- Brian = Librarian;
- Josh = Washerwoman;
- Chris = Spy;
- Hollie = Scarlet Woman in the initial returned snapshot;
- Demon bluffs = Chef / Investigator / Saint;
- only snapshot `79349` has ambiguous duplicate persisted order (14 tokens, duplicate order 2, no order 0);
- live parser-validation run `37448212336` succeeded after the parser was changed to preserve and flag that ambiguity rather than reject the entire game.

This closes all five original R04 source-data blockers. R04 remains subject to per-decision historical-prefix chronology gates.

## 7. First live acceptance targets

The two explicit-ID live acceptance targets are complete:

1. R02 — `de5f126b-89f5-4c78-a898-f5724a93430e` — **LIVE PROBE SUCCESS**;
2. R04 — `ffb40a93-3d7b-42c4-bba8-bc9c363dcd30` — **LIVE PROBE + MULTI-SNAPSHOT PARSER SUCCESS**.

For each, measure:

- single/multiple grimoire page count;
- complete ordered seat-role coverage;
- related-role coverage needed for Drunk shown-role recovery;
- Demon bluff completeness;
- match against already-retained Notes chronology;
- whether the historical decision prefix can be materialized without hindsight.

Both explicit known cases now work. The parser/probe foundation is therefore ready for the bounded 25-game CT-1 screening batch when the route reaches the acquisition gate. Do not start broad screening merely because the adapter works; EL-ML1B prefix repair remains the immediate consumer.

## 8. Current route consequence

R02 is now **PARTIAL / SETUP_CHRONOLOGY_BLOCKED**, not raw-payload blocked. R04's original raw-field blockers are closed; its remaining work is per-decision prefix chronology.

The live acquisition path is validated: GitHub Actions can provide the public structured payload even when the local execution runtime has no external network route.

A reusable manual workflow, `.github/workflows/clocktracker-single-game-probe.yml`, exposes the same explicit-ID probe without leaving R02/R04-specific one-shot workflows in main.
