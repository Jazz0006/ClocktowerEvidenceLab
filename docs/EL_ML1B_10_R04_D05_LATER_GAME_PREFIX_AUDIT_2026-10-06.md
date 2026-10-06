# EL-ML1B-10 — R04-D05 Later-Game Prefix Audit — 2026-10-06

> Status: **COMPLETE / NOT PROMOTED / MECHANICAL PREFIX READY / SOCIAL PREFIX INCOMPLETE**
>
> Candidate: R04-D05 — poisoned Undertaker Night-4 display = Scarlet Woman
>
> Game: ClockTracker `ffb40a93-3d7b-42c4-bba8-bc9c363dcd30` / Scott `@sancho` / Trouble Brewing

## 1. Why D05 was re-audited

CT-1 structured recovery closed the old R04 setup-data blockers and promoted two Night-1 decisions to DP-R07 / DP-R08. D05 is the strongest remaining R04 candidate because the retained Notes already preserve a multi-night mechanical chain through the Night-4 Undertaker decision.

## 2. Source-backed mechanical prefix

The structured source now provides the complete initial role map and setup state. The retained Notes provide the following ordered history before D05:

- Night 1: Poisoner target, Washerwoman information, poisoned Librarian information, Drunk-Empath information, Fortune Teller check;
- Day 1: nominations/votes retained in the original Notes; Maddox executed;
- Night 2: Poisoner target, Monk protection, Demon kill, Ravenkeeper information, Undertaker information, Drunk-Empath information, Fortune Teller information;
- Day 2: nomination/vote record;
- Night 3: Poisoner target, Monk protection, Demon kill, Fortune Teller information;
- Day 3: nomination/vote records, Slayer action, Sarah execution;
- Night 4 before D05: Deonna poisons the Undertaker, the current Imp self-kills, and Hollie becomes the Imp.

The observed D05 result is then:

`poisoned Undertaker -> Scarlet Woman`.

The role cross-walk is mechanically coherent with structured source state: the structured grimoire identifies Reyzant as Undertaker, while the Notes use the name Wesley for the Undertaker actions. This alias remains RECONSTRUCTED rather than source-authored.

## 3. Full Notes audit

A bounded CT-1 GitHub Actions read of the complete public R04 Notes was performed in run `37450853355`.

The Notes include:

- setup summary;
- Night/Day mechanical actions;
- information outputs;
- deaths/executions;
- nominations and vote counts;
- Demon succession.

They do **not** include:

- role claims made in discussion;
- bluff/claim chronology by player;
- private conversation content;
- table trust/suspicion state;
- Storyteller rationale for choosing Scarlet Woman.

## 4. Why the missing social state matters here

D03 and D04 occur on Night 1 before any daytime social history exists, so a grouped initial setup plus exact first-night event prefix is sufficient for their benchmark purpose.

D05 occurs on Night 4 after three days of discussion, claims, nominations, executions and revealed information. The Storyteller's misinformation choice may reasonably depend on that accumulated public narrative even though the source does not preserve a rationale.

Treating missing claims as an empty claim set would create a synthetic decision state rather than the historical one.

Therefore the correct disposition is:

```text
COMPLETE STRUCTURED SETUP
+ COMPLETE MECHANICAL NIGHT/DAY PREFIX FROM NOTES
+ OBSERVED POISONED UNDERTAKER OUTPUT
- PUBLIC CLAIM / TABLE-BELIEF CHRONOLOGY
- STORYTELLER RATIONALE
= PARTIAL / NOT CANONICAL_SEED_MATERIALIZED
```

Rationale is not required for READY by itself; the blocker is the missing decision-time social state, not the absence of rationale.

## 5. Acquisition consequence

R04-D05 demonstrates the boundary between the two strongest near-term source types:

- ClockTracker supplies structured grimoire state and concise mechanical chronology;
- Storyteller-POV / table video is needed to recover the public narrative and discussion state for later-game recommendation benchmarks.

This directly validates the EL-ML1C preferred join:

`ClockTracker structured record + matching Storyteller/table video`.

## 6. Next action

Do not promote D05 from ClockTracker alone.

Continue existing-corpus repair for additional early/setup decisions, but treat later-game benchmark growth as requiring a chronology/social-context source. The next acquisition-focused step should prioritize YT-1 matching or equivalent complete-game video for ClockTracker games with strong structured records, while broad CT-1 screening remains bounded.
