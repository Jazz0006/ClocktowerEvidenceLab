# NEXT DEVELOPMENT HANDOFF — EL-ML1B Decision Benchmark Build

> Current state: **EL-ML1A COMPLETE / EL-ML1B READY INVENTORY EXPANDED TO 8 CANONICAL SEEDS ACROSS 4 GAME GROUPS / DP-R07 R04 POISONED-LIBRARIAN + DP-R08 R04 DRUNK-EMPATH MATERIALIZED / EL-ML1B-2 G10 LONGITUDINAL COMPLETE — 0 OF 3 PROMOTED / EL-ML1B-3 R04 SOURCE-DATA REPAIR COMPLETE — 5 OF 5 ORIGINAL BLOCKERS CLOSED / EL-ML1B-4 FT1-A + EL-ML1B-5 WW2 + EL-ML1B-6 UT1-A NOT PROMOTED / EL-ML1B-7 R06 RAVENKEEPER NOT PROMOTED / EL-ML1B-8 R02 STRUCTURED SETUP RECOVERED BUT SETUP-CHRONOLOGY BLOCKED / EL-ML1C CT-1 FOUNDATION LIVE-VALIDATED ON R02 + R04 / NEXT EL-ML1B-10 R04-D05 LATER-GAME PREFIX AUDIT / C2 ON-DEMAND / EL-LRE VERIFIED BUNDLE RETAINED / EL-TBGS-0/1 ACCEPTED / EL-ML0 ACCEPTED**
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
8. `docs/EL_ML1B_G01_DP_R01_CANONICAL_SEED_V1.json`
9. `docs/EL_ML1B_G01_DP_R02_CANONICAL_SEED_V1.json`
10. `docs/G05_A_FOND_FAREWELL_SETUP_RECOVERY_2026-10-05.md`
11. `docs/EL_ML1B_G05_DP_R03_CANONICAL_SEED_V1.json`
12. `docs/EL_ML1B_G05_DP_R04_CANONICAL_SEED_V1.json`
13. `docs/G10_DP_R06_LIBRARIAN_PREFIX_RECOVERY_2026-10-05.md`
14. `docs/EL_ML1B_G10_DP_R06_CANONICAL_SEED_V1.json`
15. `docs/EL_ML1B_2_G10_LONGITUDINAL_PREFIX_AUDIT_2026-10-06.md`
16. `docs/EL_ML1B_3_R04_DIRECT_SOURCE_REPAIR_2026-10-06.md`
17. `docs/C0_TB_R04_REPLAY_PREPARATION_2026-09-23.md`
18. `docs/EL_ML1B_4_FT1A_PREFIX_AUDIT_2026-10-06.md`
19. `docs/EL_ML1B_5_WW2_PREFIX_AUDIT_2026-10-06.md`
20. `docs/EL_ML1B_6_UT1A_PREFIX_AUDIT_2026-10-06.md`
21. `docs/EL_ML1B_7_R06_RAVENKEEPER_PREFIX_AUDIT_2026-10-06.md`
22. `docs/EL_ML1B_8_R02_DRUNK_INVESTIGATOR_REPAIR_2026-10-06.md`
23. `docs/EL_ML1C_CT1_CLOCKTRACKER_STRUCTURED_SOURCE_PILOT_2026-10-06.md`
24. `docs/EL_ML1B_R04_D03_CANONICAL_SEED_V1.json`
25. `docs/EL_ML1B_R04_D04_CANONICAL_SEED_V1.json`
26. `docs/ML_RECOMMENDATION_EVIDENCE_READINESS_CONTRACT_2026-10-03.md`
27. `docs/EL_ML1C_WHOLE_GAME_SOURCE_ACQUISITION_AUDIT_2026-10-05.md`
28. `docs/EL_LRE_VERIFIED_HOST_HANDOFF_INDEX_2026-10-04.md`
29. `docs/EL_LRE_REPLACEMENT_POLICY_EVIDENCE_ALIGNMENT_2026-10-04.md`
30. `docs/C2_TB_PODCAST_BATCH_INGESTION_2026-09-29.md`
31. `docs/PODCAST_EXPERT_RATIONALE_ACQUISITION_WORKFLOW.md`
32. `docs/C3_DRUNK_CANDIDATE_COMPARISON_EVIDENCE_2026-09-30.md`
33. this file

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

EL-ML1A originally established 6 READY historical decision points across 3 game groups and roughly 2 Storyteller independence groups. EL-ML1B repair has now expanded the live manifest to **8 READY points across 4 game groups** by adding two R04 Night-1 decisions after CT-1 structured recovery. The remaining bottleneck is still independent complete historical decision states, especially later-game/history-sensitive prefixes, not additional generic policy dimensions.

Immediate route:

```text
EL-ML1B-1B DP-R01..R06 canonical seeds         COMPLETE
-> EL-ML1B-2 G10 longitudinal audit              COMPLETE / 0 OF 3 PROMOTED
-> EL-ML1B-3 R04 source-data repair              COMPLETE / 5 OF 5 ORIGINAL BLOCKERS CLOSED
-> EL-ML1B-4 FT1-A / 5 WW2 / 6 UT1-A            COMPLETE / NOT PROMOTED
-> EL-ML1B-7 R06 poisoned-Ravenkeeper audit      COMPLETE / NOT PROMOTED
-> EL-ML1B-8 R02 structured repair               COMPLETE / SETUP-CHRONOLOGY BLOCKED
-> EL-ML1B-9 R04 D03 + D04 canonical seeds       COMPLETE / DP-R07 + DP-R08
-> EL-ML1B-10 R04-D05 later-game prefix audit    NEXT
-> repair R01/R03 and remaining whole-game candidates
-> bounded CT-1 25-game screening only if repair yield drops
```

`docs/EL_ML1B_READY_HISTORICAL_BENCHMARK_V1.json` is the current machine-readable manifest. All **eight** READY rows DP-R01 through DP-R08 have real canonical decision/prefix refs backed by checked-in `HistoricalDecisionSeedV1` artifacts.

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

1. **R04-D05 later-game prefix audit next:** use the now-complete structured setup plus Notes chronology through Night 4 and test the poisoned Undertaker -> Scarlet Woman display against the no-hindsight gate.
2. **R02 remains PARTIAL / SETUP_CHRONOLOGY_BLOCKED:** raw role/bluff recovery is complete; do not promote from final grimoire state alone.
3. **R06 poisoned-Ravenkeeper remains PARTIAL:** the Night-4 local chain is strong, but Night 1–3 and complete setup are missing.
4. **FT1-A, WW2 and UT1-A remain verified comparative/rationale evidence, not full-state seeds.**
5. **G10 longitudinal audit remains closed for now:** later decisions still lack complete chronological state.
6. **After R04-D05:** repair R01/R03 and remaining Investigator/Ravenkeeper whole-game cases.
7. **New complete games only if needed:** if existing repair still cannot approach 20 READY points or diversity/later-game targets, start the bounded 25-game CT-1 screen, then YT-1 / DG-1 as needed.

The existing Priority-1/Priority-2 EL-LRE verified set remains retrieval/evaluation evidence and may still be consumed by Host, but it no longer defines EvidenceLab's default continuation order.

EL-ML1C is already audited but **not yet a broad ingestion campaign**. Its purpose is to prevent ad-hoc source hunting if new whole games become necessary. Machine discovery/screening/draft reconstruction should be the default; ambiguous or benchmark-grade decisions remain human verification gates.

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
