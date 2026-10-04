# EL-LRE-FT1 — Fortune Teller Impairment Verified Handoff — 2026-10-04

> Status: **PRIMARY-AUDIO HUMAN REVIEW COMPLETE / VERIFIED HISTORICAL + POLICY-DIMENSION EVIDENCE**
>
> Decision family: poisoned / Drunk Fortune Teller misinformation.
>
> Sources:
> - Poisoner episode — source ID `podcast:89b7c25131dfeee739e66e329e975cc6`
> - Fortune Teller episode — source ID `podcast:1ae2e0178f68f8bf3566526c3e9ad1a8`
>
> This handoff records source-backed evidence only. It does not define production policy or legal candidate domains.

## 1. FT1-A — historical poisoned Fortune Teller: immediate-value vs future-chain tradeoff

Source/window: Poisoner `01:09:31–01:13:29`

Verification: **VERIFIED**

Relation: **OBSERVED_CHOICE + EXPLICIT ALTERNATIVE + EXPLICIT RATIONALE + RETROSPECTIVE PREFERENCE SHIFT**

Human-confirmed historical meaning:

- a poisoned Fortune Teller selected their own Red Herring plus another Good player;
- absent poisoning, the normal result would have been `YES`;
- the Storyteller could legally give either `YES` or `NO` because the Fortune Teller was poisoned;
- the actual Storyteller choice was `NO`;
- the choice depended on two expectations:
  1. the Storyteller believed the Poisoner knew they had hit the Fortune Teller and would continue poisoning them;
  2. the Fortune Teller currently trusted the Demon;
- the planned long-chain payoff was that the Fortune Teller might later treat the prior `NO` Red Herring as a trusted control point and build stronger false conclusions from it;
- the plan failed because the Poisoner had hit the Fortune Teller randomly and moved elsewhere the next night;
- in hindsight, the speaker says they have since leaned more toward taking reliable immediate misinformation value on the current night rather than depending on a fragile future chain;
- this does not make the original `NO` choice intrinsically wrong: it had higher potential upside if its future dependencies had actually materialized.

Source-backed dimensions:

- immediate misinformation value;
- continuation probability;
- recipient belief state;
- future-chain upside;
- dependency risk;
- plan robustness;
- hindsight-separated policy learning.

Bounded generalization:

```text
prefer robust immediate misinformation when the future chain depends on uncertain external continuation;
accept a higher-upside delayed line when continuation probability is genuinely strong
```

Do not infer:

- always give immediate-value misinformation;
- always prefer `YES` or `NO`;
- that hindsight outcome alone defines the better policy.

## 2. FT1-B — Drunk Fortune Teller misinformation should form a coherent longitudinal story

Source/window: Fortune Teller `00:35:44–00:37:12`

Verification: **VERIFIED**

Relation: **EXPLICIT_PREFERENCE**

Human-confirmed meaning:

- Storyteller should usually keep an informal model of the false world being presented to a Drunk Fortune Teller;
- independent night-by-night improvisation risks producing an obviously incoherent pattern;
- longitudinal consistency makes the misinformation believable;
- improvisation remains appropriate when a player's actual choice creates a particularly useful narrative opportunity.

Source-backed dimensions:

- longitudinal misinformation;
- prior check history;
- narrative consistency;
- target-history state;
- bounded improvisation.

## 3. FT1-C — impairment discoverability can be deliberately adjusted

Source/window: Fortune Teller `00:36:15–00:37:30`

Verification: **VERIFIED**

Relation: **EXPLICIT CONDITIONAL PREFERENCE**

Human-confirmed meaning:

- when Good is doing poorly, Storyteller may intentionally make the Drunk Fortune Teller's information pattern easier to diagnose as impaired;
- when Good is doing well, Storyteller may preserve the misleading narrative more carefully;
- this can require intentionally breaking previously coherent misinformation;
- the relevant concept is impairment discoverability, not a simplistic rule to make the losing team's information correct.

Source-backed dimensions:

- impairment discoverability;
- current team state;
- adaptive difficulty;
- narrative-break cost;
- clue visibility.

## 4. FT1-D — mix true and false results to prevent channel inversion

Source/window: Fortune Teller `00:38:20–00:39:16`

Verification: **VERIFIED**

Relation: **EXPLICIT PREFERENCE / ANTI-INVERSION PRINCIPLE**

Human-confirmed meaning:

- if a Drunk Fortune Teller suspects impairment, systematic false information can become exploitable by simply inverting every result;
- giving truthful results while impaired is legal and strategically useful;
- mixing true and false results preserves uncertainty about the reliability of each individual check;
- anti-inversion is an explicit reason for this design.

Source-backed dimensions:

- truth/false mixture;
- anti-inversion;
- player expectation;
- discoverability;
- misinformation entropy.

## 5. What FT1 authorizes

FT1 supplies one unusually strong historical comparative case plus three verified generic policy dimensions:

1. robust immediate value vs dependency-heavy future-chain upside;
2. longitudinal misinformation coherence;
3. adaptive impairment discoverability;
4. anti-inversion through truth/false mixing.

The historical case is especially suitable for later Host replay/evaluation because it preserves the actual choice, explicit alternative, decision-time rationale, failed dependency and retrospective preference shift.

## 6. Host downstream boundary

Host may independently:

- reconstruct the exact canonical historical prefix if replay requires it;
- recover the legal poisoned-output domain;
- model continuation probability and current belief-state features;
- define/version bounded misinformation policy;
- replay/evaluate immediate-value vs future-chain choices.

EvidenceLab must preserve the distinction between contemporaneous rationale and hindsight preference rather than rewriting history as if the later preference had existed at decision time.

## 7. Next EvidenceLab target

Next Priority-2 bounded review target: **impaired Washerwoman bluff-compatible misinformation**, source window `00:48:53–00:50:10`.
