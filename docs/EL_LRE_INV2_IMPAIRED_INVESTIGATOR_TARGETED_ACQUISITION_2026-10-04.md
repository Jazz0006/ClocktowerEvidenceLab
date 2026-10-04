# EL-LRE-INV2 — Impaired Investigator Targeted Acquisition — 2026-10-04

> Status: **VERIFIED LEGAL-AXIS + HISTORICAL SUPPORT / COMPARATIVE PREFERENCE GAP REMAINS**
>
> Repository: `Jazz0006/ClocktowerEvidenceLab`
>
> Family: Drunk / Poisoned Investigator first-night misinformation.

## 1. Targeted question

Healthy Investigator pair construction is already covered by INV1. INV2 asks the narrower impaired-information question:

`when Investigator is Drunk or Poisoned, what false clue construction should the Storyteller prefer, and under what conditions?`

The most important missing comparison is:

- alter the candidate players;
- alter the shown Minion type;
- or alter both;

with an explicit reason for choosing one shape over another.

## 2. INV2-A — official rules establish two distinct misinformation axes

### Source

Official Blood on the Clocktower Wiki — Poisoner:
https://wiki.bloodontheclocktower.com/Poisoner

Direct written example for a poisoned Investigator:

- one option gives a Minion role between two players even though neither player is a Minion;
- the source separately notes that the Storyteller may instead use the correct players but show the wrong Minion type.

### Evidence semantics

- source type: **OFFICIAL_WRITTEN_RULE / EXAMPLE**
- verification: **DIRECT WRITTEN SOURCE**
- relation: **LEGAL_OPTION_TAXONOMY**, not a preference relation;
- policy meaning: impaired Investigator misinformation has at least two independent controllable axes — candidate-seat truth and shown-Minion-role truth.

### Boundary

This source does **not** say when to prefer:

- wrong players + false Minion type;
- right players + wrong Minion type;
- a partially truthful clue;
- or fully truthful information.

Therefore INV2-A belongs in Host legality / feature projection, not ranking authority.

## 3. INV2-B — published real game: false Investigator clue participates in a coherent Scarlet Woman world

### Source

The Pandemonium Institute — `Blood on the Clocktower is a Strategy Game`:
https://bloodontheclocktower.com/blogs/news/blood-on-the-clocktower-is-a-strategy-game

Author: Andrew Nathenson. The article describes the example as based on a real game he Storytold, simplified for exposition.

### Observed game shape

- the Good setup includes a Drunk who thinks they are the Investigator;
- that Investigator is shown Scarlet Woman between the Washerwoman and Undertaker;
- later, the Undertaker is poisoned and learns Scarlet Woman for the executed Washerwoman;
- the Ravenkeeper is poisoned when killed and learns that the Imp is Mayor;
- the article explicitly observes that the false information fit together well to support a world with a Scarlet Woman rather than a Poisoner;
- the article also explicitly notes that Storyteller choices determine exactly what false information players learn.

### Evidence semantics

- relation: **OBSERVED_CHOICE**;
- source type: **PUBLISHED_EXPERT_REAL_GAME_EXAMPLE**;
- verification: **DIRECT WRITTEN SOURCE**;
- source-backed descriptive dimension: **false-world / narrative coherence across multiple impaired information channels**;
- strict same-state alternative comparison: **NO**.

### What this supports

The example supports evaluating an impaired Investigator clue as part of the whole misinformation ecology rather than as an isolated false statement.

In particular, downstream evaluation may ask whether the chosen false Minion type and candidate pair:

- reinforce an existing plausible Evil-role world;
- remain compatible with other altered information;
- avoid immediately exposing Drunk / Poisoner;
- create a coherent but contestable execution path.

### What it does not support

It does not establish:

- Scarlet Woman as the preferred false Minion role;
- Washerwoman + Undertaker as a preferred candidate pair;
- `coherence` as always more important than discoverability;
- a ranking against other legal false clues.

## 4. INV2-C — primary-reviewed poisoned Investigator historical example

### Existing EvidenceLab source

`docs/C1C_TARGETED_DRUNK_ASSIGNMENT_ACQUISITION_2026-09-28.md`

Official Trouble Brewing February 2019 Game 2, Storyteller Steven Medway.

Bounded primary review preserves:

- Zach is Investigator;
- Brittany the Poisoner poisons Zach on Night 1;
- Zach falsely learns that Reggie or Evin is Scarlet Woman;
- Reggie, the healthy Empath, receives 0 on neighbours Zach and Evin.

### Evidence semantics

- relation: **OBSERVED_CHOICE**;
- verification: **PRIMARY-REVIEWED HISTORICAL STATE**;
- value: a concrete temporary-Poisoner example where false Investigator pressure coexists with healthy adjacent information;
- explicit Storyteller rationale / rejected alternatives: **NOT RECOVERED**.

This is useful as a replay/evaluation fixture but cannot authorize a false-clue ranking.

## 5. INV2-D — second historical Drunk-Investigator Scarlet Woman clue

### Existing EvidenceLab source

`docs/C0_TB_RECONSTRUCTION_BATCH_01_2026-09-23.md`

Retained ordered event:

- Drunk, believing they are Investigator, is shown Scarlet Woman between Empath and Fortune Teller;
- that claimant is executed Day 1;
- Undertaker later learns Drunk;
- the game contains multiple interacting information narratives.

### Disposition

This is another **OBSERVED_CHOICE** only.

The repetition of Scarlet Woman across INV2-B/C/D is interesting but must **not** be converted into an inferred Storyteller preference. These examples are not a controlled sample and do not preserve the considered legal alternatives.

## 6. Existing Cult Investigator review material

Source:

`18: Investigator (Trouble Brewing)` — Andrew Nathenson with Brandon.

Stable source ID:
`podcast:90e5895f9886d0d14325f829f548182a`

Episode GUID recovered from the historical semantic-queue implementation:
`5722d8e8-b89d-4067-91ac-1550b8da428d`

Historical C2D review packet identifies potentially relevant windows:

- `00:48:44–00:48:51` — MISINFORMATION_POLICY / INFORMATION_STRENGTH;
- `00:52:56–00:53:03` — REGISTRATION_CHOICE;
- `00:53:53–00:54:01` — MISINFORMATION_POLICY / LONGITUDINAL_TRAJECTORY;
- `00:55:51–00:56:04` — REGISTRATION_CHOICE;
- `00:56:32–00:56:49` — MISINFORMATION_POLICY / PLAYER_AGENCY.

The old GitHub bounded artifact was recovered successfully, but it contains candidate metadata rather than the full temporary ASR. Full transcript/audio had correctly remained outside Git and was cleaned.

These windows remain a high-value reacquisition target; no semantic preference is inferred from the keyword categories alone.

## 7. Newly selected external source

Clocktower Academy — `Investigator (TB) w/ Firepfeiffer`, published 2026-04-17.

Host: Dylan DeAngelis. Guest: Firepfeiffer / Felt Side Up.

Public episode pages confirm the episode explicitly covers Investigator advanced considerations. A public indexed transcript has not yet been located.

INV2 review should target its Storyteller / impairment discussion for the exact missing question:

`wrong players vs wrong Minion type vs partially truthful clue — which construction is preferred under which game state, and why?`

Do not promote any conclusion from the episode description alone.

## 8. Additional direct-written impairment principles

Official Drunk guidance states that Drunk information is unreliable rather than obligatorily false: in most cases it will be wrong, but truthful information may be appropriate when false information would immediately reveal drunkenness.

This adds a third legal/policy axis relevant to INV2:

- false-player / false-role construction;
- versus selectively truthful information to preserve impairment ambiguity.

However, the official example demonstrating this principle is Ravenkeeper-specific, not Investigator-specific. Treat it as a generic impairment principle until an Investigator source applies it explicitly.

## 9. Current INV2 verdict

INV2 has advanced from a vague sparse gap to a structured evidence problem:

- **VERIFIED legality/taxonomy:** wrong-player and wrong-role-type misinformation are distinct legal axes;
- **VERIFIED historical/descriptive dimension:** impaired Investigator output should be evaluated within the broader false-world / information ecology;
- **two additional historical observed choices:** poisoned and Drunk Investigator false Scarlet Woman clues;
- **still missing:** explicit source-backed comparison selecting one false-clue construction over another in the same bounded state.

Therefore impaired Investigator is **not yet Host policy-ready as a ranking family**.

## 10. Next acquisition action

Priority order:

1. reacquire/review the Cult Investigator Storyteller windows around `00:48:44–00:56:49` using the known episode GUID;
2. review Clocktower Academy / Firepfeiffer for an explicit impaired-output comparison;
3. stop if neither source contains a real preference rather than broadening to low-authority community anecdotes.

If either source yields an explicit A-vs-B comparison with condition and rationale, promote it as the next `INV2` bounded primary-audio handoff. Otherwise record the preference gap as genuinely unsupported and leave Host fail-closed to Manual.