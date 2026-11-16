# EL-CT2 — ClockTracker collection: candidate list and maintainer request — 2026-11-16

Target: 100 high-quality Trouble Brewing whole-game records (storyteller-recorded, detailed night-by-night notes, full grimoire).

## 1. Current candidate list

`EL_CT2_CLOCKTRACKER_CANDIDATES_2026-11-16.tsv` — 38 public game IDs, no player names.

| Status | Count | Meaning |
|---|---|---|
| fetched | 2 | full record fetched by ID (R02, R04) |
| reconstructed | 4 | reconstructed in C0 Batch 01 |
| indexed-only | 6 | graded A or A/B in the C0 sprint from search-visible notes; not fetched |
| duplicate | 3 | another record of a game already listed |
| unscreened | 23 | ID known, quality unknown (8 from C0, 15 new from 2026-11-16 web search) |

Usable distinct games so far: 12 graded A or A/B, plus 23 unscreened.

## 2. What changed since the C0 sprint

- 2026-11-16 web searches restricted to clocktracker.app return game pages with a title and date only. Notes are no longer visible in search results, so search can no longer grade quality; it only yields IDs.
- The public `/game/<id>` page as served does not contain notes or grimoire; both load from `/api/games/<id>`.
- `robots.txt` disallows `/api/` and `/search` for automated clients (`Crawl-delay: 5`). Fetching a few known IDs by hand is what CT-1 did; screening dozens or hundreds of unscreened IDs through `/api/` would be automated collection on a disallowed path.
- ClockTracker's Trouble Brewing script page reports about 31,000 TB games and about 284 per week, so supply is not the constraint; finding storyteller-recorded games with detailed notes is.

Consequence: further screening waits for the maintainer's answer (section 3). Do not build a crawler against `/api/` or `/search`.

## 3. Message to the ClockTracker maintainer (draft)

Channel: the project's GitHub repository (`lindsaykwardell/clocktracker`), as an issue or discussion, or the maintainer's preferred contact if listed there. Fill the bracketed parts before sending.

> **Subject: Request: research access to public Trouble Brewing game records**
>
> Hi! I'm [name], a Blood on the Clocktower player building a storyteller-assistant app for my own group. Its AI suggests night information (e.g. what the Empath or a Drunk Investigator learns), and I'm trying to make sure it avoids bad clues — ones that are useless, implausible, or so strong that evil has nowhere to hide.
>
> ClockTracker's public games are the best real-world reference I've found: storyteller notes plus the grimoire show what each player was told and the true state behind it. I've looked at a couple of public games by hand, and I noticed `robots.txt` asks bots not to use `/api/`, so I'd rather ask than automate anything.
>
> Would one of these be acceptable to you?
>
> 1. **Permission to fetch a fixed list of public games** through `/api/games/<id>` at a slow rate (one request every 10+ seconds, roughly 150–200 games in total), or
> 2. **A one-off export** of public Trouble Brewing games where the uploader was the storyteller and the notes are non-empty — or simply a list of such game IDs.
>
> What I'd commit to:
> - public games only;
> - player names and user IDs removed before anything is stored; raw records not redistributed;
> - research use for [non-commercial / personal] storyteller tooling;
> - credit to ClockTracker wherever the data is described;
> - stop immediately and delete the data on request.
>
> If a small read-only export endpoint would be useful to you or others, I'd be glad to contribute a pull request for it.
>
> Thanks for building ClockTracker!
> [name / contact]

## 4. Next steps

1. Owner sends the message (section 3).
2. Meanwhile, optional: extend the unscreened list by hand from ClockTracker profiles and communities the owner trusts (storytellers who write detailed notes).
3. After approval: one bounded fetch run over the list, raw JSON outside Git, names removed on ingest; automatic A/B/C screening by notes coverage, grimoire pages and storyteller upload; duplicate removal; then clue extraction from notes with human spot checks.
