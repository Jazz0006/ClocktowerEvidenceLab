# EL-ML1B-3 — R04 direct-source blocker repair — 2026-10-06

> Status: **BOUNDED REPAIR COMPLETE / 5 OF 5 ORIGINAL SOURCE-DATA BLOCKERS CLOSED / HISTORICAL PREFIX CHRONOLOGY REMAINS SEPARATE**
>
> Game: R04 / ClockTracker `ffb40a93-3d7b-42c4-bba8-bc9c363dcd30`
>
> Storyteller: Scott / `@sancho`
>
> Scope: re-open only the five blockers listed in `docs/C0_TB_R04_REPLAY_PREPARATION_2026-09-23.md` after a new direct public ClockTracker access path became available.

## 1. Why re-entry is now justified

The 2026-09-23 R04 preparation explicitly said not to repeat broad search unless a new direct-source access path became available.

That condition is now met:

- the original public ClockTracker game page is accessible again;
- its indexed page exposes the retained Notes plus the complete 14-player rendered grimoire sequence;
- the current open-source ClockTracker implementation can be inspected directly.

This is therefore a bounded source re-entry, not a repeat of the old blind search.

## 2. Blocker #1 — circular seat order — CLOSED

The old candidate sequence was:

```text
Hollie
Reyzant
Maddox
Victor
Rhonda
caspian3787
Nico
Hylinn
Deonna
Sarah
Brian
Chris
Josh
Andrew
```

Previously this had to remain only `source_render_order_candidate` because EvidenceLab did not know whether the public DOM/render sequence represented canonical grimoire seat order.

ClockTracker source now closes that uncertainty.

At current upstream commit `ddd69b48e54a974c093039333a53ef7f9517bb6d`, `components/Grimoire.vue` defines:

```ts
const orderedTokens = computed(() =>
  props.tokens
    .sort((a, b) => a.order - b.order)
    .filter((t) => !props.readonly || t.role || t.player_name)
);
```

The template then renders `orderedTokens` with `v-for="(token, index) in orderedTokens"`. Its circular position is computed from that index:

```css
--az: calc((var(--i) - var(--offset)) * 1turn / var(--m));
transform: rotate(var(--az)) translate(var(--r)) rotate(calc(-1 * var(--az)));
```

Therefore the public grimoire sequence is not an arbitrary DOM list: it is the persisted `token.order` sequence used to place seats around the circle.

For EvidenceLab, preserve the sequence above as the source-backed circular order. A derived seat number may use the first rendered token as seat 1 solely as an analysis identifier; the source does not claim a special semantic seat-1 origin.

### R04 circular order V1

| Derived seat | ClockTracker token/player |
| ---: | --- |
| 1 | Hollie |
| 2 | Reyzant |
| 3 | Maddox |
| 4 | Victor |
| 5 | Rhonda |
| 6 | caspian3787 |
| 7 | Nico |
| 8 | Hylinn |
| 9 | Deonna |
| 10 | Sarah |
| 11 | Brian |
| 12 | Chris |
| 13 | Josh |
| 14 | Andrew |

Adjacency-sensitive historical reconstruction may now use this circular sequence. The still-inferred aliases `Reyzant ↔ Paul` and `caspian3787 ↔ Wesley` must remain separately marked INFERRED until directly linked.

## 3. What the public ClockTracker implementation proves about the missing raw fields

ClockTracker's current `server/utils/fetchGames.ts` public `fetchGame()` query includes full grimoire token data:

- `role`;
- `related_role`;
- `alignment`;
- `order`;
- `player_name` / player identity;
- reminder tokens.

The same game object also includes `demon_bluffs` with their `role` / `role_id`.

The public page's Demon Bluffs section iterates `game.data.demon_bluffs` and links each item to the corresponding role page.

Those fields were subsequently retrieved through the bounded EL-ML1C CT-1 GitHub Actions acquisition runtime. Raw R04 inspection run `37447792091` recovered 14 grimoire snapshots; parser-validation run `37448212336` successfully normalized all 14 after duplicate-order handling was made explicit.

The earliest returned snapshot (`79346`) contains a complete 14-token role map. One later snapshot (`79349`) contains a malformed/ambiguous persisted order (14 tokens, duplicate order 2, no order 0). The parser now preserves that page with `orders_unique=false` instead of rejecting the whole game or silently repairing it.

## 4. Five-blocker disposition

| Original blocker | 2026-10-06 disposition | Reason |
| --- | --- | --- |
| verified circular seat order | **CLOSED** | public R04 render + persisted `token.order`; structured snapshots independently confirm the 14-seat circle except one explicitly flagged malformed intermediate snapshot |
| full actual/shown role map | **CLOSED** | snapshot `79346` exposes all 14 actual roles; Drunk related-role metadata exposes shown role |
| Hylinn shown role | **CLOSED** | Hylinn = actual `drunk`, `related_role_id = empath` |
| Brian exact actual/shown information role | **CLOSED** | Brian = `librarian` in structured grimoire |
| direct Demon bluff triplet confirmation | **CLOSED** | raw game metadata = `chef / investigator / saint` |

## 5. Evidence that remains usable now

The new source access strengthens R04 without making it benchmark-ready:

- the 14-player circular order is now source-backed;
- existing Notes chronology remains source-backed;
- Sarah = Monk and Sarah as Rhonda's Red Herring remain observed;
- Hylinn = actual Drunk remains observed;
- poison / kill / information / execution chronology remains retained as before.

Structured source now directly supports the initial returned role map:

- Hollie = Scarlet Woman;
- Reyzant = Undertaker;
- Maddox = Soldier;
- Victor = Ravenkeeper;
- Rhonda = Fortune Teller;
- caspian3787 = Imp;
- Nico = Slayer;
- Hylinn = Drunk shown Empath;
- Deonna = Poisoner;
- Sarah = Monk;
- Brian = Librarian;
- Chris = Spy;
- Josh = Washerwoman;
- Andrew = Virgin;
- Demon bluffs = Chef / Investigator / Saint.

The Notes aliases `Reyzant ↔ Paul` and `caspian3787 ↔ Wesley` remain INFERRED name mappings; structured role recovery does not by itself make those aliases source-authored.

## 6. Product / acquisition implication

This repair is also a concrete validation of EL-ML1C.

ClockTracker can supply exactly the structured fields EvidenceLab needs for efficient complete-game acquisition: ordered grimoire tokens, roles, related roles, reminders and Demon bluffs. The high-value engineering task is therefore a bounded machine fetch/parser for the public game payload, rather than repeated manual reading of rendered game pages.

Do **not** implement that broad fetcher inside this R04 slice. EL-ML1C remains the owner of source-pilot / acquisition-tooling work if existing-corpus repair later requires it.

## 7. Next action

The original five source-data blockers are closed. R04 is no longer raw-grimoire blocked.

R04 still should not be promoted wholesale to benchmark truth until each candidate decision is checked against exact historical-prefix chronology. The ClockTracker payload is a sequence of saved grimoire snapshots, not a semantic event log; final/reminder state must not be moved backward automatically.

Use the recovered role map together with the retained Notes chronology to re-audit specific R04 decision boundaries. The strongest candidate remains the later-game poisoned-Undertaker display because its pre-decision event chain is already substantially reconstructed.
