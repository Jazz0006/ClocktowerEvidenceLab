# EL-ML1B-5 — WW2 Historical Prefix Gate Audit — 2026-10-06

> Status: **COMPLETE / NOT PROMOTED / VERIFIED HISTORICAL COMPARATIVE EVIDENCE RETAINED**
>
> Candidate: WW2 — poisoned Washerwoman false pair built from the Demon + one Demon bluff
>
> Primary evidence: Washerwoman podcast episode, source ID `podcast:81f82799d83c9572fff012de09bf2247`, approximately `00:48:53–00:50:10`.

## 1. Why WW2 was tested

WW2 is unusually strong historical evidence because bounded human review verifies:

- a real game;
- Night 1;
- the Poisoner hit the Washerwoman;
- Andrew was the Demon;
- the Storyteller deliberately gave the poisoned Washerwoman a false pair containing the Demon plus one of the Demon's bluffs;
- the Storyteller explicitly rejected conspicuously broken misinformation as a failure mode because it could reveal poisoning;
- the stated intent was to give Evil an immediately exploitable false narrative;
- the downstream plan actually worked: players approached Andrew, he adopted the supported bluff, and the false information materially increased his credibility.

This is valid OBSERVED_CHOICE + EXPLICITLY REJECTED FAILURE MODE + EXPLICIT RATIONALE + OBSERVED DOWNSTREAM EFFECT evidence.

## 2. Canonical historical-seed gate

A full-state historical seed requires a source-backed Game identity and every relevant commitment before the Storyteller decision.

WW2 does not currently expose enough state to create that prefix without invention.

### Known decision-time state

The source establishes:

- phase: Night 1;
- impairment source: Poisoner;
- recipient role: Washerwoman;
- the Poisoner hit that recipient;
- Andrew = Demon;
- chosen false construction includes Andrew plus one Demon bluff;
- the shown role is the bluff role;
- decision intent: believable, Evil-exploitable misinformation rather than conspicuously broken information.

### Missing canonical fields

The retained source does not establish:

- a stable external/corpus ID for the historical game;
- player count;
- complete seat order;
- complete actual/shown role map;
- Washerwoman player/seat identity;
- Poisoner player/seat identity;
- Andrew's seat;
- the exact Demon bluff role used in the false pair;
- the second displayed player's identity/seat independently from the conceptual “Demon bluff” description;
- full Demon bluff triplet;
- all setup commitments preceding the misinformation choice;
- the exact Night-1 action order before the Washerwoman information;
- whether other first-night actions/information had already occurred and formed part of the decision-time state.

The observed downstream success occurs later and must not be moved backward into the historical prefix.

## 3. Rejected failure mode is not a complete candidate set

The source-backed rejection is semantic:

> do not choose obviously broken misinformation that immediately exposes poisoning.

It is not an enumerated historical alternative pair.

EvidenceLab must therefore not:

- invent a specific “bad pair”;
- convert all other legal poisoned-Washerwoman outputs into rejected candidates;
- infer a complete Host legal domain;
- conclude that Demon + bluff is universally optimal.

## 4. Disposition

```text
VERIFIED HISTORICAL COMPARATIVE EVIDENCE
+ OBSERVED FALSE-PAIR CONSTRUCTION
+ EXPLICIT REJECTED FAILURE MODE
+ EXPLICIT CONTEMPORANEOUS RATIONALE
+ OBSERVED DOWNSTREAM EFFECT
- STABLE GAME IDENTITY
- COMPLETE SETUP
- EXACT PRE-DECISION PREFIX
= PARTIAL / NOT CANONICAL_SEED_MATERIALIZED
```

No new READY manifest row is added.

WW2 remains fully useful for comparative/rationale training and evaluation. It is simply not a full-state trajectory example.

## 5. Cross-check against FT1-A

FT1-A and WW2 now demonstrate the same evidence-architecture distinction from two different role families:

- expert recollection can preserve excellent choice/rationale/comparison evidence;
- that does not imply the underlying GameState can be reconstructed;
- such records belong in the comparative expert-decision lane unless independently matched to a complete game source.

WW2 contains more bounded state than FT1-A (Night 1 and Andrew/Demon are known), but not enough to cross the canonical-prefix gate.

## 6. Next action

Continue EL-ML1B repair with **UT1-A**.

Apply the same strict gate. Do not spend acquisition effort trying to reverse-engineer the anonymous WW2 game from names/rules unless an independent source link or stable game identifier appears.
