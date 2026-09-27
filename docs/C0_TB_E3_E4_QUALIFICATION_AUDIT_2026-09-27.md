# C0 Trouble Brewing E3/E4 Qualification Audit — 2026-09-27

## 1. Purpose

Re-evaluate the current Trouble Brewing evidence corpus against CampBoardGameHost's post-RH-E evidence gate before any C5 / BEGINNER_CONSERVATIVE_V2 implementation.

This document does not create recommendation policy. Evidence Lab remains the evidence/provenance owner; CampBoardGameHost remains the policy owner.

## 2. Baselines checked

Evidence Lab:

- live main: `157a91f47112a7e4af02bc6e4c9e8613ef99d490`;
- PR #2 is merged;
- current corpus/handoff material remains the six representative TB reconstructions plus the targeted rationale search and R04 replay package.

CampBoardGameHost gate:

- E3 = qualitative evidence strong enough to authorize a concrete typed preference/reason;
- E4 = quantitative evidence required only when a policy needs numeric strength;
- observed expert choice without adequate rationale is not a policy label;
- legal alternatives and decision-time committed state must be recoverable through production owners;
- BEGINNER_CONSERVATIVE_V1 is immutable.

## 3. Qualification result

**No current candidate passes E3. No candidate passes E4.**

Current evidence is strong enough for descriptive feature surfaces and semantic regression in several dimensions, but not for a new candidate ordering/rejection.

| Candidate dimension | Current evidence | Qualification |
| --- | --- | --- |
| Healthy-information floor / middle band | whole-game bundle observations + general expert/official balance guidance | **E3 FAIL** — no qualified decision case with reconstructable bundle, explicit rationale, and recoverable alternatives; **E4 FAIL** |
| Impaired-information believability / continuity | Ben choice-specific rationale; R02/R04/R06 trajectories; Beardy contextual examples | **E3 FAIL** for new preference — independent replayable GOLD choice-over-alternatives case still missing; **E4 FAIL** |
| Confirmation-chain impact | R02/R04 structure + Beardy explicit contextual guidance | **E1/E2 SUPPORT**, **E3 FAIL** — importance is established, but no generic direction strong enough to order candidates |
| Role-function exposure | Beardy says Spy reveal/misregistration is lifecycle/context dependent | **E3 FAIL** — no complete expert game with the targeted functioning Librarian/Investigator + Spy/Recluse + healthy legal alternative + explicit considered/rejected rationale |
| Truth danger / Red Herring credibility disruption | Evin GOLD rationale + Ben contextual rationale + SILVER support | **E1/E2 STRONG**, **E3 FAIL** — supports contextual descriptive features, not "prefer strongest information role", Chef preference, scalar threshold, or deterministic suppression |
| Demon-bluff triplet quality | authentic triplets + general bluff usability guidance | **E3 FAIL** — no qualified expert choice-over-legal-alternatives rationale |
| Multi-axis tradeoff / weights | multiple qualitative axes visible | **E4 FAIL** — corpus lacks repeated executable choices with complete alternatives and tradeoff direction |

## 4. New narrow search result

A 2026-09-27 targeted search found official/public Storyteller guidance reinforcing two already-known qualitative principles:

- official Storyteller Advice recommends changing discretionary drunk/poison information according to the current balance of the game and explicitly describes supporting an evil player's bluff through Spy registration;
- official Pandemonium Institute background explains that misinformation exists to prevent Good from accumulating an entirely reliable fact chain and emphasizes situation-specific misinformation.

These sources strengthen **dimension validity** but do not satisfy the current E3 admission contract because they are general guidance rather than a reconstructable Storyteller decision with complete committed state, observed choice, legal alternatives, and decision-specific rationale.

Useful locators:

- https://wiki.bloodontheclocktower.com/Storyteller_Advice
- https://bloodontheclocktower.com/blogs/news/behind-the-curtain-1-total-chaos-sort-of

Do not promote them to GOLD whole-game cases.

## 5. Highest-value next acquisition targets

Do not resume broad TB corpus growth.

### Target A — healthy-information floor

Find an independently qualified Storyteller in a reconstructable beginner/mixed TB game who explicitly says a legal alternative was rejected or softened because Good would otherwise have too little or too much actionable healthy information.

Required minimum:

- full setup / seat-role map;
- Night-1 bundle;
- Drunk shown role / Poisoner target / Red Herring / Demon bluffs where applicable;
- explicit rationale;
- production-recoverable legal alternatives.

### Target B — independent impaired-information believability

Find a non-Ben expert case with Drunk/poisoned information where the Storyteller explicitly explains why one legal result is believable/coherent and another would be too obvious, contradictory, or destructive.

Highest value: recurring multi-night information with explicit continuity rationale.

### Target C — role-function exposure

Find a functioning Librarian/Investigator interaction involving Spy/Recluse where at least one healthy legal alternative exists and the Storyteller explicitly discusses choosing or rejecting direct exposure.

Ravenkeeper/Spy generic guidance alone does not close this gap.

### Target D — Demon-bluff triplet

Find an experienced Storyteller explicitly comparing one legal bluff set with another, preferably for beginner tables, with rationale around claim burden, route diversity, collision, misinformation support or fallback.

## 6. Stop rule

A candidate source should be abandoned for E3 purposes once it lacks one of:

- attributable qualified Storyteller identity;
- reconstructable committed decision state;
- observed Storyteller-controlled choice;
- production-recoverable legal alternatives;
- explicit rationale that maps to a generic SDE feature/predicate.

It may still be retained as qualitative guidance, but it must not unblock C5.

## 7. Cross-project consequence

CampBoardGameHost should **not** create BEGINNER_CONSERVATIVE_V2 from the current evidence set.

Next route:

```text
targeted source acquisition
-> evidence/provenance capture
-> production legal-alternative reconstruction
-> E3 qualification review
-> only then define the smallest C5 policy delta
```

If a candidate requires numeric magnitude or cross-player-count thresholds, E4 remains a separate later gate.
