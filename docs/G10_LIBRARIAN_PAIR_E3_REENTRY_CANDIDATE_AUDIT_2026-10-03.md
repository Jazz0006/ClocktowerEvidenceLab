# G10 Librarian Pair E3 Re-entry Candidate Audit — 2026-10-03

> Status: **E3 PASS — BOUNDED PAIR-INFORMATION FUTURE-FLEXIBILITY PREDICATE / C5 RE-ENTRY REQUIRED / E4 NOT MET**
>
> Decision window: approximately `16:52`
>
> Source: The Megavoid — `Storytelling Tips & Tricks - BLOOD ON THE CLOCKTOWER (+ game playthrough!)`
>
> YouTube ID: `G9z25aM9u7s`

## Why this candidate was reopened

The authoritative Host E3/E4 qualification audit was written on 2026-09-27. G10 Game 2 received its bounded human reconstruction afterward.

The C1 work correctly kept the `16:52` Librarian decision separate from the earlier Drunk-assignment prefix, but that meant the later first-night information decision was never independently re-audited as a possible C5/E3 pair-information preference case.

## Primary-verified historical state

Human primary review already establishes the complete nine-seat shown-role layout before this decision:

1. Empath — actual Drunk;
2. Imp;
3. Undertaker;
4. Librarian;
5. Spy;
6. Monk;
7. Mayor;
8. Virgin;
9. Butler.

The Drunk assignment has already occurred. At approximately `16:52`:

- the functioning Librarian is shown the Drunk-Empath seat and the Undertaker seat;
- the Librarian learns that one of those two players is the Drunk;
- the Storyteller explicitly explains choosing the Undertaker because both Empath and Undertaker are recurring information roles;
- the stated intended effect is that uncertainty over which role is Drunk materially affects how both ongoing information streams are trusted.

This is an observed historical Storyteller choice, not creator-level hypothetical guidance.

## Candidate generic predicate

A bounded generic interpretation is:

```text
when constructing legal pair information around an actual Outsider,
a decoy whose role creates a meaningful competing information narrative
may be preferred over a low-consequence decoy,
because uncertainty then propagates into interpretation of future information
rather than resolving immediately.
```

This maps to existing Host descriptive dimensions such as:

- confirmation-chain impact;
- role-information utility;
- narrative-route diversity;
- future flexibility;
- healthy-information ecology.

It must **not** become an Undertaker-specific bonus.

## E3 admission matrix

| Requirement | Current state | Assessment |
| --- | --- | --- |
| qualified independent Storyteller/source | The Megavoid is a stable independent public creator; independent Storyteller-resource curation and multiple community recommendations specifically point to the channel's Storyteller teaching material | **YES — `EXPERIENCED` / INDEPENDENT** |
| decision-time committed state | complete nine-seat shown-role layout + actual Drunk identity already human-reconstructed before the Librarian decision | **YES** |
| observed Storyteller-controlled choice | Librarian pair = Drunk-Empath + Undertaker, showing Drunk | **YES / HUMAN PRIMARY-REVIEWED** |
| production-recoverable legal alternatives | direct audit of current Host production owners confirms the observed `Drunk + {1,3}` outcome is legal and the functioning Librarian domain contains 40 truthful player-visible outcomes for this exact nine-seat state | **YES / PRODUCTION-RECOVERABLE** |
| explicit rationale | Undertaker selected because both candidate roles generate recurring information and uncertainty over which is Drunk changes trust in those information streams | **YES / HUMAN PRIMARY-REVIEWED** |
| generic typed feature mapping | the rationale is prospective: preserve meaningful ambiguity across two recurring future information streams. This maps generically to the Host's already-declared first-class `future flexibility` axis / typed `FutureFlexibilityFeatures` surface, rather than an Undertaker-specific rule | **YES — GENERIC PREDICATE MAPPED** |

## Storyteller qualification evidence

EvidenceLab's descriptive qualification recommendation is **`EXPERIENCED`**, not `VERIFIED_EXPERT_OR_TRUSTED`.

Independent public support includes:

- Bakery by the Clocktower, an independent curated BotC advice/resource index, lists **The Megavoid YouTube Series** under `Additional Comprehensive Storyteller Advice`: `https://sites.google.com/view/bakerybytheclocktower/advice/additional-comprehensive-st-advice`;
- a 2026 community resource discussion explicitly recommends The Megavoid's recent videos for improving Storytelling: `https://www.reddit.com/r/BloodOnTheClocktower/comments/1re4wnd/what_are_the_best_resources_youve_found_to/`;
- a separate 2026 discussion independently describes the channel as having several strong tutorials on how to Storytell scripts: `https://www.reddit.com/r/BloodOnTheClocktower/comments/1rp8kc5/new_in_person_botc_stream/`.

This evidence supports the stable independence key `st-the-megavoid` and an `EXPERIENCED` classification, which satisfies the Host target-source requirement for an experienced/trusted Storyteller without claiming TPI affiliation, official status, or parity with Steven Medway / Ben Burns.

## Host production-domain audit

Current CampBoardGameHost production code was audited on 2026-10-03 without modifying the Host working tree.

For the exact G10 state:

- source seat = `4` / Librarian;
- actual Outsiders = seat `1` / Drunk and seat `9` / Butler;
- Spy = seat `5`;
- full Trouble Brewing role definitions contain four Outsider display roles: Butler, Drunk, Recluse and Saint;
- `NaturalPairInformationCandidateGenerator` produces seven natural decoys for each actual Outsider, for **14 natural truthful outcomes**;
- Spy registration can produce the four Outsider roles against seven decoys; the `Drunk + {1,5}` and `Butler + {5,9}` player-visible outcomes duplicate natural outcomes and are canonicalized away, leaving **26 additional registered-truth outcomes**;
- therefore `PairInformationLegalDomain` yields **40 functioning-Librarian truthful player-visible outcomes** for this state;
- the observed `Drunk + {1,3}` pair is one of the natural truthful outcomes.

The legal-alternative part of the E3 contract is therefore closed. EvidenceLab does not assign value to the 39 unchosen outcomes.

The source rationale concerns **prospective persistence of uncertainty across future recurring information**, not merely immediate world reduction or confirmation against already-committed observations. The Host evidence contract explicitly lists `future flexibility` as a first-class generic policy axis, and `DecisionFeatures` already contains typed `FutureFlexibilityFeatures`. The fact that the architecture audit still records the canonical future-flexibility projector as an implementation gap does **not** make the evidence fail E3: the E3 stop rule requires explicit rationale mapped to a generic feature/predicate, not a pre-existing production projector. Projector implementation is downstream C5 engineering after evidence re-entry, not an acquisition prerequisite.

## Relationship to the old gaps

This is not a Gap-B impaired-output case; it is a **healthy functioning Librarian pair-information choice**.

It is also not the exact old Gap-C `Librarian -> Recluse` exposure scenario.

Its significance is broader: the Host C5 re-entry rule requires at least one concrete predicate satisfying E3. The 2026-09-27 matrix marked **confirmation-chain impact** as E1/E2 support but E3 FAIL for candidate ordering. This later G10 decision appears to supply exactly the missing historical choice + rationale shape for a confirmation-chain / information-utility preference.

## E3 decision and next Host work

This case now satisfies the preserved E3 re-entry formula:

```text
qualified independent experienced Storyteller
+ reconstructable committed state
+ observed Storyteller-controlled choice
+ production-recoverable legal alternatives
+ explicit choice-specific rationale
+ generic future-flexibility predicate mapping
= E3 PASS
```

The bounded predicate is **not** “prefer Undertaker.” It is the generic direction that, when choosing among legal pair-information decoys, a decoy can be preferred when it preserves a meaningful ambiguity across recurring future information routes rather than producing a low-consequence ambiguity.

This result should trigger a CampBoardGameHost **C5 re-entry audit**, not immediate production-policy cutover. Host next work is to:

1. register `st-the-megavoid` and this historical decision in the evidence catalog;
2. define/project the generic prospective-information / future-flexibility feature without role-name policy;
3. add a bounded shadow predicate and replay this exact case against the full legal domain;
4. preserve V1 behavior outside the new evidence-backed predicate until independent acceptance tests pass.

**E4 remains FAIL / not established.** One case does not justify numeric weights, scalar scoring, player-count thresholds, or a global decoy-role ordering.

## Boundary

The evidence says why the Storyteller chose the Undertaker in this game. It does not prove:

- Undertaker should generally be preferred as a Librarian decoy;
- recurring-information roles should always be paired;
- maximum uncertainty is always desirable;
- any scalar confirmation-chain weight;
- any rule about the earlier Drunk assignment.

The production policy, if admitted, must stay generic and context-sensitive.
