# EL-LRE-RH1 — Red Herring Selection Verified Handoff — 2026-10-04

> Status: **PRIMARY-AUDIO HUMAN REVIEW COMPLETE / VERIFIED BOUNDED POLICY-DIMENSION EVIDENCE**
>
> Decision family: Trouble Brewing Fortune Teller Red Herring selection.
>
> Primary source: `Fortune Teller (Trouble Brewing)`
>
> This handoff records source-backed evidence only. It does not enumerate legal Red Herring candidates, assign weights, or define production policy.

## 1. Review scope

Primary audio was human-reviewed for the contiguous Fortune Teller discussion around:

- `00:31:45–00:34:20`;
- `00:32:06–00:33:20`;
- `00:33:20–00:33:50`;
- `00:34:21–00:35:29`.

All four machine-semantic interpretations were confirmed.

## 2. RH1-A — Red Herring should fit the existing information ecology

Window: `00:31:45–00:34:20`

Verification: **VERIFIED**

Relation: **EXPLICIT_PREFERENCE / bounded construction principle**

Human-confirmed meaning:

- Red Herring placement should be coordinated with the rest of the setup's information topology rather than treated as an isolated/random Good seat;
- the Chef example is correct: if Chef information already identifies one adjacent Evil pair, placing the Red Herring around that Evil cluster can preserve multiple plausible interpretations across Chef and Fortune Teller information;
- the design goal is coherent cross-role ambiguity, not independent noise.

Source-backed dimensions:

- information-topology coherence;
- Chef adjacency structure;
- cross-role world preservation;
- ambiguity quality;
- Red Herring placement.

## 3. RH1-B — player tendency can be bounded enrichment for Red Herring placement

Window: `00:32:06–00:33:20`

Verification: **VERIFIED**

Relation: **EXPLICIT CONTEXTUAL FACTOR / bounded preference input**

Human-confirmed meaning:

- Sophie explicitly considers who talks a lot, who appears suspicious, and who the Fortune Teller is likely to choose;
- this makes the Red Herring more likely to become an actually encountered false lead rather than an irrelevant token;
- player tendency / local meta is therefore a legitimate bounded input to Red Herring selection;
- the discussion remains contextual rather than a universal rule.

Source-backed dimensions:

- player tendency;
- social suspicion profile;
- expected target probability;
- local meta;
- enrichment-only context.

Do not infer:

- deterministic targeting of one personality type;
- a global rule that Red Herring should always be placed on the most suspicious player;
- heavy meta use without bounded context.

## 4. RH1-C — Drunk as Red Herring is a trajectory tradeoff, not an unconditional preference

Window: `00:33:20–00:33:50`

Verification: **VERIFIED DESCRIPTIVE TRADEOFF**

Relation: **NO UNCONDITIONAL PREFERENCE**

Human-confirmed meaning:

- a Drunk Red Herring can create a coherent and strong false narrative because the player's own information may already appear unreliable;
- this can benefit Evil;
- but if that player is executed early, the ongoing value of the Drunk's future misinformation disappears;
- therefore the downstream trajectory matters.

Source-backed dimensions:

- misinformation concentration;
- false-narrative coherence;
- expected lifespan;
- future-information harm;
- execution externality.

Required interpretation:

```text
Drunk-as-Red-Herring is neither intrinsically good nor intrinsically bad;
its value depends on expected downstream trajectory.
```

## 5. RH1-D — self-Red-Herring has an explicit player-count / strategy-conditioned preference

Window: `00:34:21–00:35:29`

Verification: **VERIFIED**

Relation: **EXPLICIT CONDITIONAL PREFERENCE / COMPARATIVE DIRECTION**

Human-confirmed meaning:

- in smaller games, making the Fortune Teller their own Red Herring can be preferred because it disrupts the efficient strategy of repeatedly choosing self + one other player and quickly scanning the table;
- in larger games, the speakers generally prefer **not** to spend the Red Herring on the Fortune Teller because broad coverage is already difficult;
- there is an explicit exception: if a known player strongly favors self-checking, self-Red-Herring can still be deliberately used as an anti-meta response even in a larger game.

Source-backed dimensions:

- player count;
- self-check propensity;
- search coverage rate;
- anti-meta value;
- information compression.

Bounded generalization:

```text
small game:
    self-Red-Herring may be preferred to preserve uncertainty against rapid self-check scanning

large game:
    generally prefer another Red Herring target

exception:
    known strong self-check tendency can restore self-Red-Herring value as bounded anti-meta
```

This is a genuine conditional comparison, not a universal self-Red-Herring rule.

## 6. What RH1 authorizes

Verified Red Herring evidence now supports:

1. **information-ecology-aware placement**
   - coordinate Red Herring with existing role information and topology;

2. **bounded player-tendency enrichment**
   - expected Fortune Teller target behavior can affect Red Herring usefulness;

3. **trajectory-aware Drunk interaction**
   - Drunk Red Herring value depends on false-narrative strength versus early-execution loss;

4. **player-count-conditioned self-Red-Herring policy direction**
   - small-game and large-game conditions legitimately point in different directions, with a bounded anti-meta exception.

## 7. Host downstream boundary

Host may independently:

- enumerate legal Red Herring candidates;
- project player count, Chef topology and known player-behavior features;
- define/version bounded Red Herring policy predicates;
- evaluate candidate placements through replay;
- decide cutover.

EvidenceLab must not invent candidate legality or convert legal-but-unchosen targets into rejection evidence.

## 8. Priority consequence

With RH1 verified, the original EL-LRE Priority-1 healthy first-night/setup review set now has verified bounded evidence across:

- Washerwoman;
- Investigator;
- Demon bluffs;
- Red Herring.

The next evidence-review work should move to Priority 2 impaired/misinformation decisions unless Host opens a narrower urgent gap.
