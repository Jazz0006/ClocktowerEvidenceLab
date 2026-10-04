# NEXT DEVELOPMENT HANDOFF — C2 + EL-LRE Replacement-Policy Evidence

> Current state: **C2 FIXED TB PODCAST QUEUE EXHAUSTED / EL-LRE PRIORITY-1 VERIFIED / EL-LRE PRIORITY-2 MAJOR BATCH VERIFIED / HOST HANDOFF READY / C3 STAGE-1 HISTORICAL-SUPPORTING / EL-TBGS-0/1 ACCEPTED / EL-ML0 ACCEPTED**
>
> Repository: `Jazz0006/ClocktowerEvidenceLab`
>
> Re-check live branch / HEAD / working tree / PR state at the start of the next conversation.

## 1. Read first

1. `AGENTS.md`
2. `README.md`
3. `docs/CURRENT_DEVELOPMENT_ROADMAP.md`
4. `docs/EL_LRE_VERIFIED_HOST_HANDOFF_INDEX_2026-10-04.md`
5. `docs/EL_LRE_REPLACEMENT_POLICY_EVIDENCE_ALIGNMENT_2026-10-04.md`
6. `docs/ML_RECOMMENDATION_EVIDENCE_READINESS_CONTRACT_2026-10-03.md`
7. `docs/C2_TB_PODCAST_BATCH_INGESTION_2026-09-29.md`
8. `docs/PODCAST_EXPERT_RATIONALE_ACQUISITION_WORKFLOW.md`
9. `docs/C3_DRUNK_CANDIDATE_COMPARISON_EVIDENCE_2026-09-30.md`
10. this file

The detailed pre-LRE C5/E3 continuation snapshot is archived at:
`docs/archive/PRE_LRE_NEXT_DEVELOPMENT_HANDOFF_2026-10-04.md`.

## 2. Current authority

EvidenceLab now operates two complementary lanes:

```text
C2 automatic podcast semantic collection
        +
Host LRE bounded evidence requests
```

C2 remains the acquisition engine. EL-LRE controls Host-facing triage.

Host's production replacement invariant is:

```text
one legal result
    -> RULE_DETERMINISTIC

multiple legal results + accepted versioned policy
    -> POLICY_READY

multiple legal results + no mature policy
    -> MANUAL_REQUIRED / POLICY_DEFERRED
```

EvidenceLab does not own legality, candidate enumeration, scoring, policy versioning, replay, or cutover.

## 3. Required evidence semantics

Keep these distinct:

```text
OBSERVED_CHOICE
EXPLICIT_PREFERENCE
EXPLICIT_REJECTION
EXPLICIT_COMPARISON_LOSER
LEGAL_UNCHOSEN
SYNTHETIC_NEGATIVE
```

Only the first four may be source-backed EvidenceLab relations.

`LEGAL_UNCHOSEN` is downstream Host enrichment. It must never be silently reclassified as rejection.

`SYNTHETIC_NEGATIVE` is downstream dataset/evaluation material and is never historical evidence.

## 4. Current task

The current EvidenceLab milestone is **HOST HANDOFF READY**.

Immediate work is no longer broad feed traversal. The fixed Trouble Brewing semantic-eligible podcast queue has been exhausted, and the 2026-10-04 verification batch has closed all four Priority-1 healthy/setup families plus six major Priority-2 families.

Preferred next action:

```text
consume docs/EL_LRE_VERIFIED_HOST_HANDOFF_INDEX_2026-10-04.md in CampBoardGameHost
-> map source-backed dimensions to Host-owned legal candidate domains / Game State features
-> define bounded versioned policy per decision family
-> replay / evaluate
-> cut over only after Host acceptance gates pass
```

EvidenceLab should resume acquisition/review only when Host opens a bounded evidence gap or source scope is deliberately broadened.

Do not reopen broad Drunk acquisition, broad E3/C5 hunting, or implement recommendation policy inside EvidenceLab.

## 5. Verified milestone

### Priority 1 — COMPLETE / VERIFIED for bounded dimensions

- Washerwoman — `WW1`;
- Investigator — `INV1`;
- Demon bluffs — `DB1`;
- Red Herring — `RH1`.

All four are ready for Host mapping/evaluation. None authorizes a complete family-wide ranking or numeric weights.

### Priority 2 — major verified batch complete

Verified handoffs now exist for:

- Fortune Teller impairment — `FT1`;
- impaired Washerwoman — `WW2`;
- Chef misinformation / registration — `CHEF1`;
- Empath misinformation — `EM1`;
- Undertaker display / registration — `UT1`;
- Librarian bounded evidence — `LIB1`.

Use `docs/EL_LRE_VERIFIED_HOST_HANDOFF_INDEX_2026-10-04.md` as the consolidated downstream entry point.

## 6. Current family priority

### Host consumption priority

1. **Priority-1 verified set:** Washerwoman -> Investigator -> Demon bluffs -> Red Herring.
2. **Priority-2 verified set:** Fortune Teller -> impaired Washerwoman -> Chef -> Empath -> Undertaker -> Librarian, selected according to Host implementation readiness rather than EvidenceLab review order.

### Remaining EvidenceLab-first gaps

1. Ravenkeeper misinformation / registration — **RK1 targeted acquisition now PARTIAL VERIFIED-DIMENSION**; official bluff-support Spy registration is direct-written VERIFIED and the early-vs-Final-3 Spy A/B comparison is ready for bounded primary-audio review;
2. impaired Investigator — **INV2 targeted acquisition now structures the gap**: official rules distinguish wrong-seat vs wrong-Minion-type misinformation, and direct historical sources support false-world coherence, but no source-backed A-vs-B preference has yet been found;
3. Spy / Recluse registration — **SR1 targeted acquisition now PARTIAL VERIFIED-DIMENSION / CONDITIONAL PARTITION READY**; official Chef/Recluse over-compression and Spy bluff-support predicates plus several primary-audio VERIFIED Investigator/Undertaker cases already reject a global registration default; Empath/Librarian/info-ecology partitions remain audio-ready;
4. Mayor redirect — **MR1 targeted acquisition now PARTIAL VERIFIED-DIMENSION / TARGET-CLASS MODEL READY**; official sources verify the Mayor-survival default, early hard-confirmation exception, Evil-dominant Minion-redirect option, and legal no-death class; target severity / repeated-attack / succession refinements remain audio-ready;
5. Demon succession — distinguish discretionary Storyteller choice from player-controlled / forced transitions before promotion.

For the family-by-family evidence/gap/review/reconstruction/Host-enrichment matrix, use:
`docs/EL_LRE_REPLACEMENT_POLICY_EVIDENCE_ALIGNMENT_2026-10-04.md`.

## 7. Strongest remaining EvidenceLab leads

Do not spend more human-review effort on already-complete families unless Host identifies a concrete ambiguity.

Default remaining lead order if Host does not request something narrower:

1. **Ravenkeeper misinformation / registration — RK1 ACTIVE**
   - `docs/EL_LRE_RK1_RAVENKEEPER_TARGETED_ACQUISITION_2026-10-04.md` now records an official direct-written bluff-support Spy-registration preference;
   - Clocktower Academy / Beardy public transcript supplies the previously missing A/B shape: early/Night-2 Spy bluff support versus near-Final-3 direct Spy exposure for a healthy Ravenkeeper;
   - next action is bounded primary-audio confirmation of that Beardy comparison; do not fabricate timestamps from the transcript;
   - existing poisoned-Ravenkeeper whole-game cases remain supporting historical examples, not role-token rankings.

2. **Impaired Investigator — INV2 ACTIVE**
   - `docs/EL_LRE_INV2_IMPAIRED_INVESTIGATOR_TARGETED_ACQUISITION_2026-10-04.md` now separates verified legal misinformation axes from historical observed choices;
   - official rules permit changing the candidate seats, changing the shown Minion type, or both, but do not rank those choices;
   - direct historical examples support false-world coherence without supplying the missing same-state A/B preference;
   - next targeted review is the Cult Investigator Storyteller block around `00:48:44–00:56:49`, followed by Clocktower Academy / Firepfeiffer if needed.

3. **Spy / Recluse registration — SR1 ACTIVE**
   - `docs/EL_LRE_SR1_SPY_RECLUSE_REGISTRATION_TARGETED_ACQUISITION_2026-10-04.md` partitions registration by information ecology, over-compression, bluff support, deniability, world-model disruption, truth-as-misinformation and anti-meta intent;
   - direct official / primary-audio VERIFIED evidence already supports Chef, active Spy bluff, Investigator and Undertaker predicates;
   - next bounded reviews: Recluse/Empath `01:04:57–01:06:17`, Spy/Empath `01:49:40–01:50:24`, Recluse/Librarian `01:10:21–01:11:39`, Spy information ecology `01:43:27–01:46:20`;
   - never reduce this family to a global `register Good` / `register Evil` probability.

4. **Mayor redirect — MR1 ACTIVE**
   - `docs/EL_LRE_MR1_MAYOR_REDIRECT_TARGETED_ACQUISITION_2026-10-04.md` now records direct official Mayor-survival / early-hard-confirmation guidance and the Evil-dominant Minion-redirect option;
   - the legal no-death redirect class is separated from preference evidence;
   - next bounded reviews: Mayor `00:54:14–00:58:19` target classes and repeated attack intent, Saint `00:34:01–00:35:04` moderate severity, Undertaker `00:39:45–00:40:25` high-value Good target, Scarlet Woman `00:53:11–00:54:31` succession-forcing special case;
   - never turn the family into a generic losing-team rescue score.

5. **Demon succession**
   - verify control/legality boundary first.

## 8. Already-consumed / historical evidence

- C3 Q04 remains VERIFIED and historically important, but C3 is no longer the general active evidence lane.
- Broad Drunk scouting remains closed.
- G10 functioning-Librarian evidence has already been consumed by Host's functioning Librarian V2 route; it remains corpus evidence rather than a current blocker.
- EL-TBGS-0/1 remains accepted.
- EL-ML0 remains accepted; no new schema migration is authorized by EL-LRE0.
- Existing C5/E3 finding documents remain useful historical records and locator sources, but they no longer define global continuation priority.

## 9. C2 operational boundary

The fixed TB feed queue is exhausted. Do not keep polling `prepare-next` against the unchanged queue.

Future C2 work begins only when:

```text
Host opens a bounded evidence gap
OR an explicitly approved new source / queue scope is added
```

Then reuse the existing acquisition -> ASR -> semantic review -> targeted primary-audio verification pipeline. Machine output remains NOT VERIFIED until primary-audio promotion, and full audio/transcripts remain outside Git.

## 10. When to reconstruct more history

Invest in whole-game reconstruction when:

- an observed historical choice is close to policy-authorizing evidence;
- the exact pre-decision state changes the interpretation;
- Host wants exact replay/evaluation;
- legal-domain enrichment requires a precise historical prefix.

Do not reconstruct a whole game merely to turn generic expert guidance into a historical case.

## 11. Do not do

- do not implement Host recommendation policies;
- do not add BotC legality;
- do not enumerate legal candidates;
- do not create GOOD/BAD labels;
- do not convert legal-unchosen alternatives into rejection evidence;
- do not reopen broad Drunk acquisition;
- do not restart broad C5/E3 hunting;
- do not add SQLite/Alembic migration for EL-LRE0;
- do not redesign EL-ML0;
- do not broaden the exhausted C2 queue implicitly; any new source scope must be deliberate and documented.
