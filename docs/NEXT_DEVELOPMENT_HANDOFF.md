# NEXT DEVELOPMENT HANDOFF — EL-ML1B Decision Benchmark Build

> Current state: **EL-ML1A COMPLETE / EL-ML1B-1 MANIFEST COMPLETE / EL-ML1B-1B IN PROGRESS / DP-R05 G10 CANONICAL SEED MATERIALIZED / 5 DOCUMENTED_READY ROWS REMAIN / >=18 PARTIAL CANDIDATES / C2 ON-DEMAND / EL-LRE VERIFIED BUNDLE RETAINED / EL-TBGS-0/1 ACCEPTED / EL-ML0 ACCEPTED**
>
> Repository: `Jazz0006/ClocktowerEvidenceLab`
>
> Re-check live branch / HEAD / working tree / PR state at the start of the next conversation.

## 1. Read first

1. `AGENTS.md`
2. `README.md`
3. `docs/CURRENT_DEVELOPMENT_ROADMAP.md`
4. `docs/EL_ML1A_DECISION_POINT_BENCHMARK_AUDIT_2026-10-05.md`
5. `docs/EL_ML1B_CANONICALIZATION_AUDIT_2026-10-05.md`
6. `docs/EL_ML1B_READY_HISTORICAL_BENCHMARK_V1.json`
7. `docs/EL_ML1B_G10_DP_R05_CANONICAL_SEED_V1.json`
8. `docs/ML_RECOMMENDATION_EVIDENCE_READINESS_CONTRACT_2026-10-03.md`
9. `docs/EL_LRE_VERIFIED_HOST_HANDOFF_INDEX_2026-10-04.md`
10. `docs/EL_LRE_REPLACEMENT_POLICY_EVIDENCE_ALIGNMENT_2026-10-04.md`
11. `docs/C2_TB_PODCAST_BATCH_INGESTION_2026-09-29.md`
12. `docs/PODCAST_EXPERT_RATIONALE_ACQUISITION_WORKFLOW.md`
13. `docs/C3_DRUNK_CANDIDATE_COMPARISON_EVIDENCE_2026-09-30.md`
14. this file

The detailed pre-LRE C5/E3 continuation snapshot is archived at:
`docs/archive/PRE_LRE_NEXT_DEVELOPMENT_HANDOFF_2026-10-04.md`.

## 2. Current authority

EvidenceLab's active route is now **EL-ML1B benchmark construction / historical-prefix repair**. C2 and EL-LRE remain bounded on-demand evidence lanes rather than the default continuation.

The benchmark route must preserve the same authority boundary: EvidenceLab owns historical evidence, prefixes, provenance and benchmark export; Host owns legality, legal candidates, policy scoring, replay and production cutover.

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

The current EvidenceLab milestone is **EL-ML1B — benchmark manifest + whole-game decision-prefix repair**.

EL-ML1A established a conservative current inventory of 6 READY historical decision points across only 3 game groups and roughly 2 Storyteller independence groups, plus at least 18 high-value PARTIAL candidates. The main bottleneck is therefore independent complete historical decision states, especially later-game/history-sensitive prefixes, not additional generic policy dimensions.

Immediate route:

```text
EL-ML1B-1B DP-R05 G10 canonical seed          COMPLETE / GREEN locally
-> canonicalize G01 DP-R01 + DP-R02 together NEXT
-> repair G05 full setup map for DP-R03/R04
-> recover G10 later-decision prefixes only with evidence-backed setup chronology
-> close R04 blockers
-> recover FT1-A / WW2 / UT1-A historical prefixes
-> repair R01/R02/R03 and Investigator/Ravenkeeper candidates
-> acquire new complete TB games only if READY still < 20
```

`docs/EL_ML1B_READY_HISTORICAL_BENCHMARK_V1.json` is the current machine-readable manifest. DP-R05 now has real canonical decision/prefix refs backed by `docs/EL_ML1B_G10_DP_R05_CANONICAL_SEED_V1.json`; the other five rows intentionally remain `DOCUMENTED_READY` with null canonical refs. Do not fill those fields until their own canonical materialization succeeds.

Pilot target: 20–30 READY historical decision points, at least 8 games, at least 4 Storyteller independence groups, and at least 40% later-game/history-sensitive decisions.

C2 and EL-LRE remain bounded on-demand lanes for gaps exposed by benchmark construction. Do not reopen broad Drunk acquisition, broad E3/C5 hunting, broad podcast policy mining, or recommendation policy inside EvidenceLab.

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

## 6. Benchmark build priority

### EL-ML1B priority

1. **Canonicalize G01 next:** materialize DP-R01 + DP-R02 from one shared reconstruction; preserve Ben Burns + Adam controller/independence uncertainty rather than inventing one identity.
2. **Repair G05 bounded setup state:** recover the missing full seat/role map before DP-R03 or DP-R04 can become canonical seeds.
3. **Same-game longitudinal test:** materialize later G10 decisions only after the exact historical prefix—including setup chronology needed by event-prefix materialization—is evidence-backed.
4. **High-leverage repair:** close R04 blockers because one repaired game may unlock several early- and later-night decision points.
5. **Rationale-rich prefix recovery:** FT1-A -> WW2 -> UT1-A.
6. **Diversity repair:** R01/R02/R03 plus existing Investigator/Ravenkeeper historical cases.
7. **New complete games only if needed:** prefer new Storyteller independence and grimoire visibility.

The existing Priority-1/Priority-2 EL-LRE verified set remains retrieval/evaluation evidence and may still be consumed by Host, but it no longer defines EvidenceLab's default continuation order.

### On-demand EvidenceLab gaps retained

1. Ravenkeeper misinformation / registration — **RK1 targeted acquisition now PARTIAL VERIFIED-DIMENSION**; official bluff-support Spy registration is direct-written VERIFIED and the early-vs-Final-3 Spy A/B comparison is ready for bounded primary-audio review;
2. impaired Investigator — **INV2 targeted acquisition now structures the gap**: official rules distinguish wrong-seat vs wrong-Minion-type misinformation, and direct historical sources support false-world coherence, but no source-backed A-vs-B preference has yet been found;
3. Spy / Recluse registration — **SR1 targeted acquisition now PARTIAL VERIFIED-DIMENSION / CONDITIONAL PARTITION READY**; official Chef/Recluse over-compression and Spy bluff-support predicates plus several primary-audio VERIFIED Investigator/Undertaker cases already reject a global registration default; Empath/Librarian/info-ecology partitions remain audio-ready;
4. Mayor redirect — **MR1 targeted acquisition now PARTIAL VERIFIED-DIMENSION / TARGET-CLASS MODEL READY**; official sources verify the Mayor-survival default, early hard-confirmation exception, Evil-dominant Minion-redirect option, and legal no-death class; target severity / repeated-attack / succession refinements remain audio-ready;
5. Demon succession — **DS1 control boundary is now verified**: Imp self-kill is player-controlled, ordinary successor choice is Storyteller-controlled, active Scarlet Woman succession is forced, Mayor-bounce-to-Imp controls only the trigger, and exotic Recluse succession is officially cautionary; the next evidence target is Spy M11 successor choice/rationale.

For the family-by-family evidence/gap/review/reconstruction/Host-enrichment matrix, use:
`docs/EL_LRE_REPLACEMENT_POLICY_EVIDENCE_ALIGNMENT_2026-10-04.md`.

## 7. On-demand EvidenceLab leads — not default continuation

Do not spend more human-review effort on these policy families merely because review material exists. Re-enter them only when EL-ML1B benchmark construction or Host evaluation exposes a concrete missing comparison/context field.

When such a bounded gap exists, the retained lead order is:

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

5. **Demon succession — DS1 M11 VERIFIED / HOST-READY BOUNDED DIMENSION**
   - `docs/EL_LRE_DS1_DEMON_SUCCESSION_VERIFIED_HANDOFF_2026-10-05.md` is now the preferred downstream authority;
   - control taxonomy remains: Imp self-kill is player-controlled, ordinary multi-Minion successor choice is Storyteller-controlled, active Scarlet Woman is forced, and exotic Recluse succession is officially cautionary;
   - primary-audio review confirmed Spy M11 `01:53:33–01:56:28`: the source describes choosing the strongest / most trusted Minion as a common tendency, then gives a counterexample where Storyteller chose less-trusted Baron instead of well-trusted Spy because retaining Spy as support for the new Demon was more valuable in that state;
   - player experience/fun was also a genuine secondary factor;
   - Host may now test a bounded policy where trust/survivability remains a positive factor but is not absolute; R04/R06 remain replay fixtures only.

## 8. Already-consumed / historical evidence

- C3 Q04 remains VERIFIED and historically important, but C3 is no longer the general active evidence lane.
- Broad Drunk scouting remains closed.
- G10 functioning-Librarian evidence has already been consumed by Host's functioning Librarian V2 route; it remains corpus evidence rather than a current blocker.
- EL-TBGS-0/1 remains accepted.
- EL-ML0 remains accepted; EL-ML1B authorizes only the smallest derived benchmark/export projection and still does **not** authorize a new persistence/schema migration.
- Existing C5/E3 finding documents remain useful historical records, retrieval evidence and locator sources, but they no longer define global continuation priority.

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
