# EL-LRE Verified Host Handoff Index — 2026-10-04

> Status: **HOST HANDOFF READY / VERIFIED BOUNDED EVIDENCE INDEX**
>
> Repository: `Jazz0006/ClocktowerEvidenceLab`
>
> Scope: consolidated downstream entry point for the 2026-10-04 EL-LRE primary-audio verification milestone.
>
> This index does **not** define BotC legality, legal candidate domains, policy weights, recommendation scores, replay acceptance, or production cutover. Those remain Host-owned.

## 1. Why this index exists

EvidenceLab now has enough primary-audio VERIFIED material that Host should not need to rediscover policy semantics across individual podcast findings.

The intended flow is:

```text
EvidenceLab verified bounded evidence
    -> Host legal candidate / Game State projection
    -> bounded versioned policy
    -> replay / evaluation
    -> production cutover
```

This document is a routing/index layer only. The individual handoff documents remain authoritative for exact wording, conditions, relation type, caveats and provenance.

## 2. Evidence semantics Host must preserve

Keep these distinctions intact:

```text
OBSERVED_CHOICE
EXPLICIT_PREFERENCE
EXPLICIT_REJECTION
EXPLICIT_COMPARISON_LOSER
LEGAL_UNCHOSEN
SYNTHETIC_NEGATIVE
```

Only the first four may be source-backed EvidenceLab relations.

Host may enumerate legal alternatives, but an unchosen legal candidate is **LEGAL_UNCHOSEN**, not source-backed rejection unless the source explicitly says so.

A descriptive dimension or clever design option is not automatically an explicit preference.

## 3. Priority 1 — healthy first-night / setup

### 3.1 Washerwoman — WW1

Authority:
`docs/EL_LRE_WW1_WASHERWOMAN_VERIFIED_HANDOFF_2026-10-04.md`

Status: **VERIFIED-DIMENSION / HOST-ENRICHMENT**

Host may use as policy dimensions:

- avoid direct Mayor confirmation when it would materially over-compress late-game uncertainty;
- positive target value for roles benefiting from trusted routing / credibility support, with Monk, Undertaker, Fortune Teller and Soldier as source-backed examples;
- vary decoy category to prevent fixed Storyteller Good/Evil meta.

Descriptive-only boundary:

- Drunk-exclusion amplification increases information strength, but is not itself a source-backed preference.

Do not infer:

- complete Washerwoman target ranking;
- deterministic Mayor exclusion;
- numeric target weights;
- rejection of every legal unchosen pair.

### 3.2 Investigator — INV1

Authority:
`docs/EL_LRE_INV1_INVESTIGATOR_PAIR_CONSTRUCTION_VERIFIED_HANDOFF_2026-10-04.md`

Status: **VERIFIED-DIMENSION / HOST-ENRICHMENT**

Host may use as bounded policy dimensions:

- when Empath topology already places strong pressure on the Demon, prefer an Investigator construction that preserves a plausible alternative world while still including the real Minion;
- when Good information is already unusually strong, Recluse registration can be used instead of exposing the real Minion directly;
- real Minion + Recluse is also a valid separate construction with a different deniability mechanism.

Critical boundary:

- these are distinct intents and must not be collapsed into one global pair ordering.

### 3.3 Demon bluffs — DB1

Authority:
`docs/EL_LRE_DB1_DEMON_BLUFF_VERIFIED_HANDOFF_2026-10-04.md`

Status: **VERIFIED-DIMENSION / HOST-ENRICHMENT**

Host may use:

- when Good has high healthy-information density, prefer bluff classes that materially help Evil operate against that information;
- bluff usefulness includes redistribution / Minion use, not only direct Demon use;
- local bluff rarity/meta may affect credibility as a descriptive context feature;
- omitted-role bluff surfaces can provide future flexibility.

Do not infer:

- Librarian globally outranks another named bluff;
- rarity alone creates a preference;
- a complete three-bluff ranking from this evidence.

### 3.4 Red Herring — RH1

Authority:
`docs/EL_LRE_RH1_RED_HERRING_VERIFIED_HANDOFF_2026-10-04.md`

Status: **VERIFIED-DIMENSION / HOST-ENRICHMENT**

Host may use:

- coordinate Red Herring placement with existing information topology rather than treating it as isolated/random noise;
- bounded player-tendency / expected Fortune Teller targeting can be enrichment context;
- Drunk-as-Red-Herring is a trajectory tradeoff involving false-narrative strength versus early-execution loss;
- self-Red-Herring has an explicit player-count / self-check-conditioned preference direction.

Do not infer:

- always choose the most suspicious player;
- heavy player-meta dependence;
- Drunk is inherently better/worse as Red Herring;
- universal self-Red-Herring policy.

## 4. Priority 2 — impaired / misinformation

### 4.1 Fortune Teller — FT1

Authority:
`docs/EL_LRE_FT1_FORTUNE_TELLER_IMPAIRMENT_VERIFIED_HANDOFF_2026-10-04.md`

Status: **VERIFIED HISTORICAL + VERIFIED-DIMENSION / HOST-ENRICHMENT**

Host may use:

- historical immediate-value vs future-chain robustness tradeoff for poisoned Fortune Teller;
- coherent longitudinal false-world construction for Drunk Fortune Teller;
- impairment discoverability may be intentionally increased or decreased according to bounded game-state needs;
- truthful and false impaired results should be mixed so the channel cannot be solved by simple inversion.

Critical boundary:

- no global YES-vs-NO preference;
- hindsight outcome alone must not define policy quality.

### 4.2 Impaired Washerwoman — WW2

Authority:
`docs/EL_LRE_WW2_IMPAIRED_WASHERWOMAN_VERIFIED_HANDOFF_2026-10-04.md`

Status: **VERIFIED HISTORICAL / HOST-ENRICHMENT**

Host may use:

- prefer believable / exploitable misinformation over conspicuously broken information that merely exposes poisoning;
- bluff compatibility and Evil exploitability are legitimate dimensions.

Historical positive example:

- Demon + Demon bluff false pair after a successful Poisoner hit.

Do not infer:

- Demon + bluff is always the best false pair;
- every poisoned Washerwoman should directly support the Demon.

### 4.3 Chef — CHEF1

Authority:
`docs/EL_LRE_CHEF1_CHEF_MISINFORMATION_REGISTRATION_VERIFIED_HANDOFF_2026-10-04.md`

Status: **VERIFIED-DIMENSION / HOST-ENRICHMENT**

Host may use:

- believable misinformation and discoverable misinformation are distinct objectives;
- start from an intuitive/simple Spy/Recluse registration baseline and depart for a concrete game-state reason;
- accidental confirmation leakage is a real policy cost;
- higher legal Chef numbers generally provide stronger Good information and therefore represent a power consideration.

Do not infer:

- low Chef number is always preferable;
- high false number is the preferred misinformation;
- numeric weights from these qualitative dimensions.

### 4.4 Empath — EM1

Authority:
`docs/EL_LRE_EM1_EMPATH_MISINFORMATION_VERIFIED_HANDOFF_2026-10-04.md`

Status: **VERIFIED-DIMENSION / HOST-ENRICHMENT**

Host may use:

- truthful later information can sustain a false longitudinal inference;
- poisoned Empath output explicitly trades immediate misinformation impact against concealment of the Poisoner hit;
- cross-night history is required context for output quality.

Critical boundary:

- the cross-night `0 -> 1` example is a clever bounded design option, not a universal preference;
- the impact-vs-concealment tradeoff has no source-backed fixed winner.

### 4.5 Undertaker — UT1

Authority:
`docs/EL_LRE_UT1_UNDERTAKER_MISINFORMATION_REGISTRATION_VERIFIED_HANDOFF_2026-10-04.md`

Status: **VERIFIED HISTORICAL + VERIFIED-DIMENSION / HOST-ENRICHMENT**

Host may use:

- truthful information can function as socially difficult misinformation when public narrative makes it hard to believe;
- Recluse Undertaker registration should be selected from live world-model consequences;
- no fixed Spy-vs-Imp display ordering is source-backed.

Descriptive-only boundary:

- truthful precedent has anti-meta/future-flexibility value, but the reviewed passage did not explicitly recommend making that a policy default.

### 4.6 Librarian — LIB1

Authority:
`docs/EL_LRE_LIB1_LIBRARIAN_VERIFIED_HANDOFF_2026-10-04.md`

Status: **VERIFIED-DIMENSION / HOST-ENRICHMENT**

Host may use:

- player experience and Storyteller facilitation affect the value of Librarian zero information;
- repeated favorite interactions create anti-meta cost;
- role-impact asymmetry can be an informative pair-construction feature;
- later altered information should remain coherent with an established bluff / narrative.

Critical boundary:

- expert views on Librarian zero for beginners genuinely differ; do not collapse them into one global rule;
- low-impact real Drunk + high-impact decoy is a bounded design option, not a source-backed global preference.

## 5. Remaining EvidenceLab gaps

The fixed Trouble Brewing podcast semantic queue is exhausted. EvidenceLab should not continue broad collection merely because acquisition infrastructure exists.

If Host does not open a more urgent bounded gap, the default remaining evidence order is:

1. **Ravenkeeper misinformation / registration — RK1 targeted acquisition active**
   - official Storyteller Advice now supplies a direct-written VERIFIED bluff-support Spy-registration predicate;
   - Clocktower Academy / Beardy public transcript supplies the previously missing early/Night-2 bluff-support vs near-Final-3 direct-Spy A/B comparison;
   - bounded primary-audio review is still required before promoting that stage-sensitive comparison to VERIFIED;
   - authority: `docs/EL_LRE_RK1_RAVENKEEPER_TARGETED_ACQUISITION_2026-10-04.md`.

2. **Impaired Investigator**
   - healthy Investigator construction is covered by INV1;
   - remaining need is impaired-output comparison.

3. **Spy / Recluse registration**
   - rich machine-semantic material exists;
   - verify separate legitimate intents rather than create a fixed Good/Evil default.

4. **Mayor redirect**
   - verify state-sensitive target classes / intent;
   - avoid a generic “help the losing team” heuristic.

5. **Demon succession**
   - first distinguish Storyteller discretion from player-controlled Imp self-kill and automatic/forced Scarlet Woman transitions.

## 6. Recommended Host re-entry

If Host has no dependency forcing another order, use this sequence:

```text
INV1 Investigator
-> DB1 Demon bluffs
-> RH1 Red Herring
-> integrate WW1 into the same Priority-1 evaluation suite
-> choose next Priority-2 family by Host runtime readiness
```

Why:

- Priority-1 source verification is complete;
- these families already have bounded explicit preferences / contextual dimensions;
- remaining missing pieces are Host-owned legality, state projection, versioned policy definition and replay;
- additional EvidenceLab review is unlikely to be the highest-value blocker before Host attempts mapping/evaluation.

## 7. Host acceptance checklist per family

Before production cutover, Host should independently establish:

```text
1. exact decision boundary
2. legal candidate domain
3. required Game State features
4. source-backed predicates / dimensions only
5. explicit policy version
6. replay / regression fixtures
7. comparison against old heuristic authority
8. production acceptance gate
9. retirement of old heuristic authority for the cut-over scope
```

EvidenceLab should be re-entered only if one of those steps exposes a specific evidence ambiguity or missing policy dimension.

## 8. Scope boundary

This milestone does **not** mean:

- all Trouble Brewing Storyteller decisions are solved;
- every legal candidate can be ranked;
- qualitative evidence has numeric weights;
- machine-only findings are VERIFIED;
- old Host heuristics may be silently retained as fallback policy;
- EvidenceLab should implement Host recommendation logic.

It means the project now has a sufficiently mature VERIFIED evidence bundle for Host to attempt the next staged policy replacements instead of continuing broad evidence collection first.
