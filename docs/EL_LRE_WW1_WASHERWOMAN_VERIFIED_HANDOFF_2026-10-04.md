# EL-LRE-WW1 — Washerwoman Healthy-Information Verified Handoff — 2026-10-04

> Status: **PRIMARY-AUDIO HUMAN REVIEW COMPLETE / VERIFIED BOUNDED POLICY-DIMENSION EVIDENCE**
>
> Decision family: healthy first-night Washerwoman pair / target construction.
>
> Source: `11: Washerwoman (Trouble Brewing) - With Official Storyteller Reggie Collins!`
>
> Source ID: `podcast:81f82799d83c9572fff012de09bf2247`
>
> This handoff records source-supported evidence only. It does not enumerate legal Washerwoman pairs, define policy weights, or authorize production cutover.

## 1. Review method

The project owner reviewed the primary audio for the four bounded EL-LRE-WW1 windows on 2026-10-04 and confirmed/corrected the machine-semantic interpretation.

Reviewed windows:

- `00:43:09–00:43:52`;
- `00:43:53–00:45:22`;
- `00:46:39–00:47:55`;
- `00:52:51–00:53:42`.

The resulting evidence is intentionally split by relation type so descriptive information-strength analysis is not promoted into preference evidence.

## 2. WW1-A — avoid over-confirming Mayor

Window: `00:43:09–00:43:52`

Verification: **VERIFIED**

Relation: **EXPLICIT_PREFERENCE / bounded avoidance**, not a universal prohibition.

Human-confirmed meaning:

- Reggie explicitly advises caution / avoidance when choosing Mayor as the Townsfolk shown by a functioning Washerwoman;
- the reason is excessive confirmation strength: Washerwoman support can make a late-game Mayor too trusted and remove valuable final-three uncertainty;
- the reviewed segment contains no additional qualification or exception beyond that stated rationale.

Source-backed dimensions:

- confirmation-chain strength;
- final-three uncertainty;
- healthy-information ecology;
- bluff-space preservation.

Bounded generalization:

```text
when direct Washerwoman confirmation of Mayor would materially over-confirm the Mayor
and compress late-game uncertainty,
prefer another suitable Washerwoman target over Mayor
```

Do not infer:

- Mayor is always a bad Washerwoman target;
- a numeric penalty for Mayor;
- Mayor ranks below every other legal target;
- any legal pair domain not stated by the source.

## 3. WW1-B — favor roles that benefit from trusted information routing / credibility support

Window: `00:43:53–00:45:22`

Verification: **VERIFIED**

Relation: **EXPLICIT_PREFERENCE**, with named positive examples but no explicit comparison loser.

Human-confirmed meaning:

- Reggie explicitly gives Monk, Undertaker and Fortune Teller as roles he likes Washerwoman to see because the Washerwoman can act as a trusted intermediary, allowing those roles to share useful information without immediately outing themselves;
- Soldier is also highlighted because it can otherwise struggle to establish credibility;
- the reason is information routing / credibility support, not simply maximizing raw Good information strength;
- no additional qualification was identified in the reviewed segment.

Source-backed dimensions:

- information-routing value;
- role exposure cost;
- credibility deficit;
- trusted-intermediary value.

Bounded generalization:

```text
when a healthy Townsfolk gains meaningful value from trusted information routing
or credibility support,
that role can be a preferred Washerwoman target
```

Do not infer:

- Monk > Undertaker > Fortune Teller > Soldier;
- the named roles form an exhaustive preferred set;
- those roles should always be shown;
- unmentioned legal targets were rejected.

## 4. WW1-C — Washerwoman confirmation can exclude Drunk worlds

Window: `00:46:39–00:47:55`

Verification: **VERIFIED DESCRIPTIVE POLICY-DIMENSION EVIDENCE**

Relation: **NO EXPLICIT PREFERENCE / NO EXPLICIT REJECTION**

Human correction:

- the semantic content is correct;
- the passage is **describing information strength**, not recommending that the Storyteller prefer or avoid a particular target.

Human-confirmed meaning:

- truthfully showing another information role can materially increase confidence that the seen player is not the Drunk;
- this can amplify the downstream value of that player's information beyond the immediate Washerwoman pair clue.

Source-backed dimensions:

- Drunk-exclusion value;
- confirmation-chain strength;
- information-confidence amplification.

Required interpretation:

```text
this is a feature / consequence to evaluate,
not a source-backed ranking direction
```

This item must not be exported as `EXPLICIT_PREFERENCE`, `EXPLICIT_REJECTION`, or `EXPLICIT_COMPARISON_LOSER`.

## 5. WW1-D — vary decoy category to prevent Storyteller meta

Window: `00:52:51–00:53:42`

Verification: **VERIFIED**

Relation:

- **EXPLICIT_PREFERENCE** for variation;
- **EXPLICIT_REJECTION** of a fixed Good-only or Evil-only decoy-pattern policy;
- not a rejection of any specific legal player/candidate.

Human-confirmed meaning:

- the speakers recommend varying the second/decoy player's category rather than repeatedly following one Good/Evil pattern;
- the purpose is to prevent players learning a stable Storyteller meta and inferring alignment from presentation pattern rather than game evidence;
- the Outsider point is also confirmed: using an Outsider as the decoy can sometimes simplify the Washerwoman deduction if that Outsider publicly claims.

Source-backed dimensions:

- anti-meta variation;
- decoy alignment/category;
- deduction compression;
- public-claim interaction.

Bounded generalization:

```text
avoid a stable decoy-category pattern that players can exploit as Storyteller meta;
vary decoy category across appropriate legal choices
```

Do not infer:

- a required Good/Evil alternation schedule;
- any probability distribution;
- that Outsiders should never be decoys;
- rejection of any specific candidate solely because of alignment/category.

## 6. What WW1 now authorizes as evidence

EL-LRE-WW1 now provides VERIFIED evidence for three distinct Host-consumable dimensions:

1. **over-confirmation avoidance**
   - direct Mayor confirmation can be undesirable when it collapses late-game uncertainty;

2. **trusted information-routing / credibility support**
   - some roles are positively preferred Washerwoman targets because the pair relationship helps them communicate or be believed;

3. **anti-meta decoy variation**
   - fixed decoy-category habits should be avoided because players can learn Storyteller patterns.

It also provides one VERIFIED descriptive feature:

4. **Drunk-exclusion amplification**
   - a truthful Washerwoman result can make another information role substantially more trusted by excluding Drunk worlds.

## 7. What WW1 does not authorize

WW1 does **not** authorize:

- a complete Washerwoman target ranking;
- numeric weights;
- a deterministic Mayor exclusion;
- a fixed preferred-role whitelist;
- treating all unmentioned legal targets as losers;
- converting Host `LEGAL_UNCHOSEN` pairs into source-backed rejection;
- production cutover by EvidenceLab.

## 8. Host downstream handoff

Host may now independently:

1. enumerate legal healthy Washerwoman outputs for a canonical state;
2. project bounded features such as:
   - Mayor over-confirmation / final-three compression;
   - trusted information-routing value;
   - role credibility deficit;
   - Drunk-exclusion amplification;
   - decoy-pattern / anti-meta context;
3. define a versioned policy candidate using only evidence-supported scope;
4. replay/evaluate that policy;
5. decide whether it is sufficient for production cutover.

EvidenceLab should not supply the legal candidate domain or assign weights.

## 9. Next EvidenceLab target

With WW1 verified, the next Priority-1 bounded review target is **Investigator pair construction**:

- Empath episode `00:38:47–00:39:20`;
- Recluse episode `01:06:54–01:08:37`.

The review should determine exactly which pair-construction alternatives are explicitly preferred, compared or conditionally selected, while preserving distinct intents such as Demon deniability, Recluse registration ambiguity and real-Minion exposure.
