# ClockTracker clue extraction — extractor prompt V1

Used with `python -m clocktower_evidence_lab.acquisition.clocktracker_clues input <prepared.json>`.
Send the instructions below plus that input JSON to the extractor. The answer must be one JSON
object valid against `interchange/clocktracker_clue_extraction_v1.py` (`ClueExtraction`), then
checked with `... clocktracker_clues check <prepared.json> <extraction.json>`.

---

You are extracting what a Blood on the Clocktower storyteller wrote down about the information
players received in one Trouble Brewing game. You record the notes faithfully. You do not judge
whether any information was true, legal or a good choice.

**Input.** `roster`: seats `1..n` with the true role (`role_id`), the role a Drunk believes they are
(`related_role_id`), alignment and grimoire reminders. `lines`: the storyteller's notes, one entry
per line, with a `line_id` (`N2.3` = night 2, line 3; `D1.1` = day 1; `SETUP.1`; `PRE.1` = before
any heading). Player names are already replaced: `S<n>` is seat n; `P<n>` is a name that is not on
the grimoire.

**1. Resolve every `P<n>`** that appears in a line you use, into `names`:
- `ROLE_EVIDENCE` with the seat, when the notes show that name acting as one role (e.g. "P1 kills
  S4" makes P1 the Imp seat; "P3 undertakes Soldier" makes P3 the Undertaker seat). List the
  evidence `line_id`s.
- `NAME_VARIANT` with the seat, when it is a spelling of a grimoire name and the context fits.
- `NOT_A_PLAYER` (e.g. the storyteller), or `UNRESOLVED` when you cannot tell. Never guess.

**2. One `clues` entry per piece of information a player received at night** from these abilities:
washerwoman, librarian, investigator, chef, empath, fortune_teller, undertaker, ravenkeeper.
- `recipient_seat`: the player who received it. Lines may name the role instead of the player
  ("The Empath learns a 0"): use the roster seat with that role, or the Drunk whose
  `related_role_id` is that role. `ability` is the ability as the recipient experienced it
  (a Drunk who thinks they are the Investigator has ability `investigator`).
- `chosen_seats`: the players the recipient picked (Fortune Teller, Ravenkeeper), only if stated.
- `shown`: exactly what was shown — `seats` (the pair, or one seat), `role_id` (snake_case, e.g.
  `scarlet_woman`), `number` (Chef, Empath), `answer` `YES`/`NO` (Fortune Teller),
  `no_outsiders` (Librarian shown no Outsiders).
- `note_annotations`: the storyteller's own remarks on that line, copied as written without
  brackets, e.g. `drunk`, `poisoned`, `Red Herring`, `Spy`. Do not add your own.
- `quote`: the exact text of the line (or the part about this clue), copied from the input.
- Leave a field empty when the notes do not state it. Do not fill it from the grimoire.

**3. `setup_choices`** for storyteller setup decisions the notes state: `RED_HERRING` (seat),
`DRUNK` (seat, thinks-as role), `DEMON_BLUFFS` (the three roles, e.g. "P1 sees Chef/Investigator/
Saint" for the Demon), `OTHER`. Same `quote` rule.

**4. `skipped`**: a night line that seems to report information but cannot be recorded reliably,
with a short reason. Do not list kills, poisons, protections or day events.

Set `game_id` from the input, `extractor` to a short label for who or what extracted, and answer
with the JSON object only.
