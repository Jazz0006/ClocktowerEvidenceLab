# EL-LRE-INV1 — Investigator Pair-Construction Verified Handoff — 2026-10-04

> Status: **PRIMARY-AUDIO HUMAN REVIEW COMPLETE / VERIFIED BOUNDED POLICY-DIMENSION EVIDENCE**
>
> Decision family: healthy first-night Investigator pair construction.
>
> Sources:
> - `Empath (Trouble Brewing)` — source ID `podcast:122f2a963af3cf04f7c8bae43e02c875`
> - `Recluse (Trouble Brewing)` — source ID `podcast:af87b5f5461c44e39a4fae6b7405c443`
>
> This handoff records source-supported preference/rationale only. It does not enumerate Investigator legal candidates, define weights, or impose a global pair ranking.

## 1. Human review scope

Primary audio was reviewed for:

- Empath `00:38:47–00:39:20`;
- Recluse `01:06:54–01:07:57`;
- Recluse `01:07:57–01:08:37`.

The review confirms two explicit preference directions plus one independently useful pair-construction option. The third item is **not** an explicit comparison against the preceding option.

## 2. INV1-A — use Investigator construction to preserve Demon deniability when Empath topology is already informative

Source/window: Empath `00:38:47–00:39:20`

Verification: **VERIFIED**

Relation: **EXPLICIT_PREFERENCE**

Human-confirmed meaning:

- when an Empath is seated next to the Demon and a Townsfolk, the Investigator clue can be constructed using the Townsfolk neighbour plus the real Minion;
- this avoids reinforcing the Empath information directly against the Demon;
- the Townsfolk neighbour remains a plausible Minion world, giving the Demon deniability;
- Investigator still receives a real Minion candidate, so the clue retains genuine information value;
- the speaker presents this as a recommended/recurring Storyteller tactic, not merely a theoretical possibility.

Source-backed dimensions:

- cross-role information interaction;
- Demon deniability;
- truthful-clue ambiguity;
- confirmation-strength budgeting;
- pair construction.

Bounded generalization:

```text
when Empath topology already places unusually strong pressure on the Demon,
prefer an Investigator pair construction that preserves a plausible alternative world
while still including the real Minion
```

Do not infer:

- that this pattern is always preferable;
- that the Townsfolk neighbour must always be used;
- a global Investigator pair ranking.

## 3. INV1-B — when Good information is already unusually strong, Investigator may route through Recluse instead of the real Minion

Source/window: Recluse `01:06:54–01:07:57`

Verification: **VERIFIED**

Relation: **EXPLICIT_PREFERENCE / conditional**

Human-confirmed meaning:

- Ben explicitly recommends that, when the setup is already unusually strong for Good, Investigator information may identify a Minion role between a Townsfolk and the Recluse even though neither candidate is the actual Minion;
- the explicit example is an Empath with an unusually strong starting position, such as being adjacent to two Evil players;
- Recluse registration is used to avoid compounding already-strong Good information with another direct Minion-finding clue;
- this is a conditional recommendation, not merely a statement that the interaction is legal;
- the machine summary's note that Ben does not use the technique often does not cancel the preference under the stated condition.

Source-backed dimensions:

- cross-role information budget;
- setup-strength compensation;
- Minion concealment;
- Recluse registration;
- marginal information value.

Bounded generalization:

```text
when the setup already gives Good unusually strong information,
a Recluse-based Investigator result that does not expose the real Minion
can be preferred to adding another direct Minion-finding clue
```

Do not infer:

- that Recluse should generally replace the real Minion;
- that all strong-Good setups require this treatment;
- a numeric setup-strength threshold.

## 4. INV1-C — real Minion + Recluse can preserve truthful information while creating deniability

Source/window: Recluse `01:07:57–01:08:37`

Verification: **VERIFIED**

Relation: **BOUNDED DESIGN OPTION / RATIONALE; NO EXPLICIT COMPARISON LOSER**

Human correction:

- the semantic content is correct;
- this passage is **not** an explicit comparison with INV1-B;
- there is no source-backed claim that one of the two Recluse constructions is globally better;
- both may be appropriate depending on actual game state.

Human-confirmed meaning:

- Investigator can be shown the real Minion plus Recluse;
- once Recluse is known or claimed, players may attribute the Minion ping to Recluse registration and discount the real Minion;
- the information remains truthful while still giving the real Minion useful deniability;
- this construction is applicable in different real-game conditions from the stronger information-suppression construction above.

Source-backed dimensions:

- truthful ambiguity;
- Minion deniability;
- registration ambiguity;
- information validity;
- candidate-pair construction.

Required interpretation:

```text
INV1-B and INV1-C are parallel conditional design directions.
Do not derive an ordering between them unless a source explicitly compares them.
```

This item must not be exported as `EXPLICIT_COMPARISON_LOSER` for either construction.

## 5. What INV1 now authorizes

The verified Investigator evidence supports at least three bounded Host-facing dimensions:

1. **cross-role confirmation budgeting**
   - avoid stacking Investigator information directly on top of already-strong Empath pressure when a more ambiguous truthful construction is available;

2. **setup-strength compensation through Recluse registration**
   - when Good is already unusually strong, a Recluse-based result may legitimately avoid exposing the real Minion;

3. **truthful deniability through real Minion + Recluse**
   - a true Investigator pair can still preserve Evil cover because Recluse registration creates an alternative explanation.

The evidence does **not** establish a total ordering among those constructions.

## 6. Host downstream boundary

Host may independently:

- enumerate legal Investigator output pairs;
- determine whether Recluse registration makes a candidate legal;
- derive canonical setup-strength and cross-role topology features;
- define/version policy predicates;
- replay/evaluate competing bounded policies;
- decide production cutover.

EvidenceLab must not turn unchosen legal pairs into rejection evidence or assign policy weights.

## 7. Next EvidenceLab target

With INV1 verified, the next Priority-1 LRE target should move to **Demon bluffs**, followed by **Red Herring**, while C2 semantic collection continues independently.
