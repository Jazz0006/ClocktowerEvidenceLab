# C2 Machine Semantic Findings — Poisoner — 2026-10-03

> Status: **MIXED — M05 PRIMARY-AUDIO HUMAN REVIEWED; OTHER FINDINGS REMAIN MACHINE SEMANTIC / NOT VERIFIED**
>
> Source: `14: Poisoner (Trouble Brewing)`
>
> Source ID: `podcast:89b7c25131dfeee739e66e329e975cc6`
>
> GUID: `5bb20ab2-f523-4609-96dc-d26c20733214`
>
> ASR: `small.en`, 2,217 timestamped segments, approximately 85 minutes.

This full-episode pass prioritizes Storyteller-controlled misinformation choices, player-experience context, longitudinal information trajectories, Evil-side narrative support, and concrete choice-over-alternatives examples.

## High-value machine-understood findings

### C2-POISONER-M01 — player influence and experience change the expected impact of misinformation

**Window:** approximately `00:05:40–00:10:15` and `00:20:30–00:21:16`

Machine-understood meaning:

- the speakers distinguish socially influential / highly experienced players from players who already distrust most information;
- poisoning or misleading a persuasive player can have greater downstream effect because that player may propagate the resulting false world to the group;
- the same strategic assumptions change materially between inexperienced and experienced groups;
- the discussion therefore supports treating player experience, table influence and information-skepticism as contextual features rather than assuming identical information impact for every recipient.

Potential downstream dimensions:

- player experience;
- social influence / information propagation;
- recipient susceptibility;
- group meta.

**E3 disposition:** context/rationale support only. This is player-strategy guidance rather than a reconstructable Storyteller choice over legal outputs.

### C2-POISONER-M02 — misinformation value is longitudinal, not only local to one night

**Window:** approximately `00:24:03–00:27:18` and `00:55:16–00:56:48`

Machine-understood meaning:

- repeatedly poisoning one information role can approximate a stable Drunk-like trajectory, while switching targets can make the resulting world harder to diagnose;
- the Empath example shows that alternating poisoned and healthy nights can deliberately shape which neighbour appears suspicious as seating changes;
- the discussion repeatedly evaluates one night's information by how it affects later deductions and confirmation chains, not merely by whether the current output is false.

Potential downstream dimensions:

- longitudinal trajectory;
- confirmation-chain impact;
- information-history consistency;
- future flexibility.

**E3 disposition:** strong feature-shape support but no fixed Storyteller decision state. Do not infer a general preference for switching or continuity.

### C2-POISONER-M03 — Evil narrative state can determine whether misinformation actually has value

**Window:** approximately `00:33:40–00:35:16`

Machine-understood meaning:

- a historical game is described where a night-one poisoned Washerwoman was shown the Demon and Poisoner under a false role presentation;
- public Outsider / Baron claims and later executions caused the Washerwoman to conclude that the original information failure was explained by being the Drunk;
- continued poisoning of the Fortune Teller then became more credible inside that public narrative;
- the important signal is that the practical value of a misleading output depends on what Evil can plausibly claim and what public explanation already exists.

Potential downstream dimensions:

- Evil claim state;
- bluff compatibility;
- public narrative continuity;
- misinformation believability.

**E3 disposition:** useful historical narrative evidence, but the passage does not reconstruct the full committed state or enumerate the Storyteller's legal alternatives.

### C2-POISONER-M04 — Storyteller should be cautious about over-planning player reactions

**Window:** approximately `01:07:17–01:09:13`

Machine-understood meaning:

- both speakers describe difficulty predicting how players will react to deliberately constructed misinformation;
- a Librarian example illustrates that an intended Spy suspicion chain may simply be ignored by the recipient;
- one speaker says they have increasingly preferred an in-the-moment approach: choose misinformation that has useful impact now rather than relying on a complex future chain whose later player behaviour is uncertain;
- this is not an absolute rejection of long-term planning, but it explicitly identifies player-response uncertainty as a cost of elaborate Storyteller plans.

Potential downstream dimensions:

- immediate impact;
- future-flexibility uncertainty;
- player-response uncertainty;
- plan robustness.

**E3 disposition:** generic Storyteller preference, not a fixed historical decision.

### C2-POISONER-M05 — historical Fortune Teller choice exposes immediate-value vs long-chain tradeoff

**Window:** approximately `01:09:31–01:13:29`

Machine-understood meaning:

- in a real game, a poisoned Fortune Teller selected their own Red Herring plus another Good player;
- the Storyteller had a legal choice between preserving the ordinary `YES` result or using poisoning to give `NO`;
- the Storyteller chose `NO` because they believed the Poisoner knew the Fortune Teller and would continue poisoning them, and because the Fortune Teller currently trusted the Demon;
- the intended future line was that the Fortune Teller might later use that Red Herring as a trusted control point, potentially producing a stronger false conclusion;
- the plan failed because the Poisoner had hit the Fortune Teller randomly and moved elsewhere the next night;
- reflecting on the outcome, the speaker says they have since leaned more toward giving the immediately useful misinformation in the current night because it is safer, while acknowledging that the `NO` line can have higher upside if the future chain actually materializes.

Potential downstream dimensions:

- immediate misinformation value;
- expected continuation probability;
- recipient belief state;
- future-chain upside;
- plan robustness / dependency risk;
- hindsight-separated rationale.

**Verification / LRE disposition:** **VERIFIED HISTORICAL COMPARATIVE EVIDENCE** by bounded primary-audio review on 2026-10-04. Human review confirmed the observed `NO` choice, the legal `YES` alternative, the contemporaneous rationale (expected continued poisoning + Fortune Teller trust in the Demon), the failed future dependency, and the later preference shift toward more robust immediate misinformation. The original `NO` is not reclassified as intrinsically wrong: it retained higher upside if the continuation chain had materialized. Exact full-prefix reconstruction remains optional downstream work for Host replay/evaluation.

### C2-POISONER-M06 — Poisoner-caused impairment is treated differently from passive Drunk impairment

**Window:** approximately `01:13:42–01:18:18`

Machine-understood meaning:

- the speakers explicitly distinguish impairment caused by an active Evil player's nightly Poisoner choice from the Drunk's passive setup condition;
- one speaker says they generally try to make a Poisoner hit have an effect when possible because changing information is the Minion player's active ability and strategic investment;
- when Evil is already strongly ahead, the suggested balancing response is not necessarily to make poisoned information fully helpful, but potentially to make the misinformation conspicuously bad so the Good player can diagnose impairment;
- the discussion therefore separates `source of impairment`, `player agency behind the impairment`, and `current team pressure` as potentially relevant Storyteller context.

Potential downstream dimensions:

- ability-owner agency;
- current team pressure;
- misinformation strength;
- impairment source;
- player-experience fairness.

**E3 disposition:** high-value policy guidance but strongly policy-sensitive. It is not a single fixed-state historical choice and must not become an unconditional rule that every Poisoner hit receives maximally harmful misinformation.

### C2-POISONER-M07 — first-night poisoned pair information has a coordination-risk tradeoff

**Window:** approximately `01:20:26–01:24:08`

Machine-understood meaning:

- for a poisoned Washerwoman or Librarian, the speakers compare two broad approaches: give obviously disconnected nonsense, or give information that could support an Evil player's bluff;
- they do not establish a universal preference between those approaches;
- they explicitly warn that trying to support a clever Demon bluff can accidentally handicap Evil because the Evil player does not know the Storyteller's hidden plan and may already have prepared another bluff;
- this creates a generic coordination-risk dimension: an output that is theoretically strong for Evil can be worse if it requires uncommunicated cooperation from the Evil player.

Potential downstream dimensions:

- bluff compatibility;
- coordination risk;
- hidden-plan dependency;
- recipient inference;
- player agency.

**E3 disposition:** strong generic rationale support but no fixed historical state with recoverable legal alternatives.

## Strict E3 result

**No new E3 re-entry case is admitted from this episode.**

The strongest passage is **C2-POISONER-M05** because it contains:

- a real Storyteller-controlled choice;
- an explicit `YES` versus `NO` alternative;
- a choice-specific rationale;
- a documented downstream outcome and retrospective update in policy preference.

However, the current retained material does not reconstruct the complete decision-time game state or production legal domain, so it must remain a machine-understood historical candidate rather than be promoted to E3.

## Product-facing triage

Most useful for future recommendation work:

1. **M05** — immediate-value vs future-chain tradeoff with explicit historical alternative;
2. **M06** — active Poisoner agency vs passive Drunk impairment;
3. **M07** — bluff-support value must be discounted by coordination risk;
4. **M04** — long-chain plans should account for player-response uncertainty;
5. **M02** — misinformation should be evaluated as a longitudinal trajectory.

No immediate primary-audio review is requested unless Host opens a bounded gap around misinformation choice, future-chain robustness, or coordination risk.
