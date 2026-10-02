# C3-Q04 Verified Monk Conditional Preference Handoff — 2026-10-02

> Status: **VERIFIED / C3 STAGE-1 ACCEPTED**
>
> Source: `12: Monk (Trouble Brewing)`
>
> Source ID: `podcast:91574d66c261bb0dd8bcb08469531a9c`
>
> GUID: `e8241f55-824b-4dc5-8314-db398b5ece55`
>
> Primary-audio window: `00:43:28–00:44:30`
>
> Verification: **human-confirmed from primary audio on 2026-10-02**
>
> Scope: one bounded Drunk-assignment conditional preference. This is not a global role ranking.

## 1. Verified source meaning

The human primary-audio review confirms the machine-located semantic interpretation:

1. the Storyteller does not choose which shown Townsfolk is the Drunk until after inspecting the seated layout;
2. the source gives a concrete assignment-time condition in which an Empath is seated between two Good players and is away from the Demon;
3. under that condition, the Storyteller says a Drunk Monk can be the best place to assign the Drunk;
4. the stated tradeoff is to preserve healthy information for the information roles, including the named Empath, while using Monk as the Drunk candidate instead.

The project owner has separately calibrated `Cult of the Clocktower` hosts and episode guests as trusted expert/Storyteller clue sources. No separate creator/official title is required for C3 source qualification.

## 2. C3 Stage-1 structure

This item satisfies the accepted conditional-preference evidence shape:

```text
reconstructable assignment-time condition
+ candidate A = Monk
+ candidate B = Empath
+ explicit preference = use Monk as the Drunk instead
+ source-backed rationale = preserve healthy Empath / information-role information
+ trusted primary-source provenance
+ human verification
```

The assignment-time condition is bounded to the source-described layout. It must not be generalized into a universal claim that Monk is a better Drunk than Empath.

## 3. Downstream policy boundary

The narrow evidence-authorized Host predicate is:

```text
IF
  the setup and seating are already fixed,
  Monk and Empath are both legal Drunk candidates,
  the Empath is seated between two Good players,
  and the Empath is away from the Demon such that preserving healthy Empath information is useful,
THEN
  Monk may be preferred over Empath as the Drunk candidate
BECAUSE
  this preserves the Empath's healthy information while assigning the Drunk cost to Monk.
```

This handoff does **not** authorize:

- a global Monk > Empath ranking;
- a general preference for non-information roles over information roles;
- arbitrary inference about unmentioned candidates;
- mutation of `BEGINNER_CONSERVATIVE_V1`;
- promotion of any other machine-located C3 candidate to VERIFIED.

## 4. Host re-entry consequence

C3 Stage 1 is now satisfied by one VERIFIED item. Per the existing cross-project contract, CampBoardGameHost may now:

1. map this bounded condition onto the accepted Trouble Brewing snapshot / Drunk decision context;
2. define a first explicitly versioned production-capable Drunk preference predicate;
3. replay it against reconstructable cases;
4. rerun the Drunk production-cutover gate.

EvidenceLab does not decide whether the Host cutover passes. It supplies the verified semantic permission boundary above.
