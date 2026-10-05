# EL-ML1B-4 — FT1-A Historical Prefix Gate Audit — 2026-10-06

> Status: **COMPLETE / NOT PROMOTED / VERIFIED COMPARATIVE EVIDENCE RETAINED**
>
> Candidate: FT1-A — poisoned Fortune Teller NO versus explicit legal YES
>
> Primary evidence: Poisoner podcast episode, source ID podcast:89b7c25131dfeee739e66e329e975cc6, approximately 01:09:31–01:13:29.

## 1. Why FT1-A was tested

FT1-A is one of the strongest non-manifest historical candidates found by EL-ML1A because the human-verified source preserves all of the following:

- a real historical Storyteller choice;
- poisoned Fortune Teller selected their own Red Herring plus another Good player;
- ordinary healthy result would have been YES;
- poisoned legal domain included both YES and NO;
- actual choice was NO;
- contemporaneous rationale was explicit;
- the Storyteller expected continued Poisoner coverage and knew the Fortune Teller currently trusted the Demon;
- a future-chain payoff was explicitly intended;
- the external dependency failed on the following night;
- the speaker later explains a preference shift toward more robust immediate misinformation.

This is unusually rich comparative evidence and remains fully VERIFIED as such.

## 2. Canonical historical-seed gate

A HistoricalDecisionSeedV1 requires more than a strong observed choice:

    stable source-backed Game identity
    + reconstructable game/seat/setup state
    + exact historical setup/event prefix
    + observed choice
    + provenance
    = canonical historical seed

FT1-A currently satisfies the final two terms but not the first three.

### Missing canonical fields

The retained primary-audio review does not establish:

- a stable external or corpus identity for the historical game being discussed;
- player count;
- complete seat order;
- complete actual/shown role map;
- Fortune Teller seat/player identity;
- Red Herring seat/player identity;
- the other selected Good player's seat/role identity;
- Poisoner seat/player identity;
- exact night / phase within the game;
- previously delivered Fortune Teller checks;
- current living/dead state;
- prior public claims or executions;
- exact prior Poisoner target history;
- every setup/event commitment that precedes the NO decision.

The source does establish some decision-time beliefs — expected continued poisoning and Fortune Teller trust in the Demon — but those beliefs do not substitute for a canonical game-state prefix.

## 3. Why the missing fields cannot be inferred

Do not construct the prefix by:

- inventing seat IDs;
- treating “own Red Herring + another Good” as enough to identify the selected players;
- reconstructing a legal setup from Trouble Brewing distribution rules;
- assuming this was Night 1;
- treating the later failed continuation as if it were known at decision time;
- converting the explicit legal YES alternative into a complete Host legal-domain reconstruction.

The retrospective preference shift is **hindsight evidence**, not part of the historical decision prefix.

## 4. Disposition

    VERIFIED HISTORICAL COMPARATIVE EVIDENCE
    + EXPLICIT ALTERNATIVE
    + EXPLICIT CONTEMPORANEOUS RATIONALE
    + RETROSPECTIVE POLICY LEARNING
    - CANONICAL GAME STATE
    - EXACT HISTORICAL PREFIX
    = PARTIAL / NOT CANONICAL_SEED_MATERIALIZED

No new DP-R07 row is added to the READY manifest.

This is not a downgrade of FT1. The existing verified handoff remains authoritative for retrieval, preference/ranking supervision and rationale evaluation. It simply must not be used as a full-state benchmark example until the original game can be independently identified and reconstructed.

## 5. Dataset consequence

FT1-A demonstrates that EvidenceLab needs at least two separate future projection lanes:

1. **full-state historical benchmark examples** — canonical GameState/prefix required;
2. **comparative expert-decision evidence** — source-backed choice/alternative/rationale can remain useful even when the entire game cannot be reconstructed.

Do not discard lane 2 merely because it cannot enter lane 1.

## 6. Next action

Continue EL-ML1B repair with **WW2**, then UT1-A.

Apply the same gate: if the historical source exposes a reconstructable game identity and exact pre-decision state, materialize it; otherwise retain the verified decision/rationale relation without fabricating a canonical prefix.
