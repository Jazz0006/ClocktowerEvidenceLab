# C2 Machine Semantic Findings — Slayer — 2026-10-04

> Status: **MACHINE SEMANTIC REVIEW ONLY / NOT VERIFIED**
>
> Source: Slayer (Trouble Brewing)
>
> Source ID: podcast:5c1ea94be8e2bd778350a41bcd7cce32
>
> GUID: a69e9973-261c-376c-066b-35bc7fcc7867
>
> ASR: small.en, 2,387 timestamped segments, approximately 57 minutes.

This full-episode pass reviewed all 2,387 ASR segments. It prioritizes Slayer setup-strength modulation, Recluse registration, Scarlet Woman protection against abrupt game endings, information-role synergies, player-experience suitability, and the reliability limits of Slayer-derived information.

## High-value machine-understood findings

### C2-SLAYER-M01 — Slayer power is also information; timing trades certainty against survival risk

Window: approximately 00:04:44–00:10:39

- A failed Slayer shot is treated as information, not merely a failed win attempt.
- Earlier use lowers hit probability but lets the result inform more of the later game.
- Waiting increases raw hit probability but risks dying before the power is used.
- High-impact claimants such as Empath, Saint, or Mayor can be rational targets even when the shot is mainly informative.

### C2-SLAYER-M02 — real Poisoner coordination can turn a correct Slayer target into false exoneration

Window: approximately 00:13:46–00:15:24

Observed game narrative:
- a real Slayer privately trusted an Evil player;
- Evil coordinated with Poisoner;
- Slayer was steered onto the actual Demon while poisoned;
- the correct shot failed, causing the Demon to appear safer for much of the game;
- Evil ultimately won.

Lesson: failed Slayer information must distinguish wrong target from impaired ability.

### C2-SLAYER-M03 — Recluse is a deliberate Slayer uncertainty lever, and the episode generally favors allowing Slayer to kill Recluse

Window: approximately 00:44:03–00:47:29

- Slayer targeting Recluse creates a genuine Storyteller-controlled choice.
- Andrew states that most of the time he would let Slayer kill Recluse.
- Rationale includes preserving consequences of risky play and preserving Recluse's disruptive purpose.
- Named exceptions include a prior Storyteller mistake that already severely hurt Good, or a game where Good is doing very badly and needs relief.
- If Evil is struggling and an unrevealed Recluse has taken a risky bluffing line, allowing the death can create useful ambiguity and help Evil.

LRE relevance: very high; explicit preference + conditions + alternatives.

### C2-SLAYER-M04 — Storyteller intervention should preserve consequences of player risk rather than erase them automatically

Window: approximately 00:47:10–00:47:42

- Hidden-Recluse play is framed as a legitimate player risk.
- If that risk later causes a harmful Slayer interaction, the Storyteller should generally allow the consequence rather than rescue the player automatically.
- They distinguish rewarding good play from protecting players from a failed gamble.

### C2-SLAYER-M05 — Recluse and Scarlet Woman are explicit setup tools for reducing Slayer strength

Window: approximately 00:47:43–00:51:32

- Recluse is described as a strong pairing when the Storyteller wants a trap or uncertainty around Slayer.
- Scarlet Woman reduces the chance that an early lucky Slayer shot immediately ends the game.
- The episode explicitly groups Recluse and Scarlet Woman as ways to make Slayer less powerful when Good's setup is otherwise strong.

### C2-SLAYER-M06 — Washerwoman can deliberately strengthen Slayer by establishing early trusted identity

Window: approximately 00:51:17–00:52:24

- If Storyteller wants Slayer stronger, Washerwoman can identify a pair containing Slayer.
- This creates an early trust relationship and gives Slayer someone safe to confide in.
- It lets Slayer bluff publicly while retaining a credible witness for later role reveal.
- The discussion explicitly contrasts this strengthening effect with Recluse / Scarlet Woman weakening effects.

### C2-SLAYER-M07 — Fortune Teller is explicitly described as the role that most increases Slayer power

Window: approximately 00:52:23–00:53:18

- Andrew explicitly says Fortune Teller is the role that most makes Slayer more powerful.
- Rationale: if Fortune Teller narrows the Demon world to real Demon plus Red Herring, Slayer gets a direct 50/50 game-winning shot.
- This is stronger than generic more-information-is-good because it identifies a particular topology that compresses the target domain especially efficiently.

### C2-SLAYER-M08 — Slayer setup strength should be considered in the context of the whole Good information network

Window: approximately 00:53:20–00:54:38

- The speakers discuss adding Poisoner or Drunk when a setup contains many strong information roles.
- Slayer is treated as both a mid-tier information role and a potentially powerful action role.
- Inclusion should therefore depend on existing information density and uncertainty budget rather than Slayer in isolation.
- Andrew cautions that Trouble Brewing is resilient enough that this should not become over-engineered deterministic balancing.

### C2-SLAYER-M09 — Slayer is explicitly considered beginner-friendly

Window: approximately 00:55:05–00:56:06

- Both speakers consider Slayer a strong fit for beginner-heavy games.
- Ability semantics are easy to understand.
- It exposes meaningful strategy without requiring mastery of highly opaque interactions.
- They contrast this with Spy and, to a lesser degree, Fortune Teller / Red Herring complexity.

### C2-SLAYER-M10 — setup design can intentionally strengthen or weaken Slayer rather than maximize all role synergies

Windows: approximately 00:47:43–00:55:48

Synthesis:
- weaken Slayer: Recluse, Scarlet Woman;
- strengthen Slayer: Washerwoman;
- strongest stated synergy: Fortune Teller;
- beginner suitability can independently favor Slayer even when raw setup strength is not the main concern;
- setup construction is therefore about choosing the desired shape of the game, not maximizing every Good role's effectiveness.

## Strict historical-evidence result

No new strict historical same-state Storyteller policy case is promoted automatically.

Strongest bounded review targets:
1. M03 — explicit most-of-the-time kill-Recluse preference with Good-losing / prior-ST-error exceptions;
2. M06 — explicit Washerwoman -> Slayer strengthening rationale;
3. M07 — explicit Fortune Teller as strongest Slayer synergy;
4. M05 — Recluse + Scarlet Woman as deliberate Slayer-attenuation tools.

M03 is especially promising for EL-LRE because it contains a genuine legal Storyteller choice, an explicit default preference, named exceptions, and rationale. It remains MACHINE SEMANTIC REVIEW ONLY until primary-audio verification.

## Queue status after this pass

After Slayer became current and the pipeline attempted to fill the next prefetch slot, the queue returned:

no unprocessed Trouble Brewing podcast episodes remain

Therefore this pass reaches the end of the currently fixed Trouble Brewing semantic-eligible podcast queue. This does not imply all evidence gaps are closed; it means the current C2 feed-backed automatic acquisition set has been exhausted.
