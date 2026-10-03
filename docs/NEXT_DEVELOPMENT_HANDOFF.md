# NEXT DEVELOPMENT HANDOFF — C2 Podcast Batch Ingestion + C3 Drunk Candidate Comparison

> Current state: **C2 ACTIVE / C3 STAGE-1 ACCEPTED / EL-TBGS-0/1 CROSS-PROJECT ACCEPTED / EL-ML0 ARCHITECTURE ACCEPTED**
>
> EL-ML0 docs branch at authoring: `docs/el-ml0-ml-readiness-contract-20261003`
>
> Repository: `Jazz0006/ClocktowerEvidenceLab`

## 1. Read first

Read in this order:

1. `AGENTS.md`
2. `README.md`
3. `docs/ARCHITECTURE.md`
4. `docs/EVIDENCE_AND_PROVENANCE_STANDARD.md`
5. `docs/ML_RECOMMENDATION_EVIDENCE_READINESS_CONTRACT_2026-10-03.md`
6. `docs/SOURCE_COLLECTION_STRATEGY.md`
7. `docs/TESTING_STRATEGY.md`
8. `docs/CURRENT_DEVELOPMENT_ROADMAP.md`
9. `docs/PODCAST_EXPERT_RATIONALE_ACQUISITION_WORKFLOW.md`
10. `docs/C2_TB_PODCAST_BATCH_INGESTION_2026-09-29.md`
11. `docs/C2D_PRIMARY_AUDIO_REVIEW_QUEUE_2026-09-30.md`
12. `docs/C3_DRUNK_CANDIDATE_COMPARISON_EVIDENCE_2026-09-30.md`
13. `docs/TB_GAME_SNAPSHOT_INTEROPERABILITY_ROUTE_2026-09-30.md`
14. `docs/EL_TBGS_0_1_MAPPING_AND_IMPLEMENTATION_AUDIT_2026-09-30.md`
15. this file

At the start of the next conversation, re-check live `main`, this branch, open PRs/checks and exact file state. Do not assume this handoff's branch status is still live.

## 2. Current baseline

C1 remains complete and broad Drunk-assignment acquisition remains stopped.

EL-ML0 is now **COMPLETE / ARCHITECTURE ACCEPTED**. The accepted ML-readiness boundary is canonical EvidenceLab evidence -> derived `RecommendationEvidenceSeedV1` -> Host/future ModelLab enrichment -> actual training example. Implementation is deferred. `DecisionSlice` remains the historical-decision owner; Q04-like non-historical comparative guidance will likely justify a future typed `ExpertPreferenceEvidence` / `ComparativeGuidanceEvidence`, but no schema migration or C2 workflow change is authorized now.

The EL-ML0 audit was based on live `origin/main` `1af0952dbee1c4804013c906dbe3505966ca10ba` before the docs-only branch was created. Future sessions must still re-check live state rather than relying on this checkpoint.

C2 has now completed three implementation slices:

- **C2A manifest — COMPLETE / GREEN**
  - live RSS parser + show/episode metadata;
  - stable source identity;
  - Trouble Brewing scope classification;
  - independent acquisition / ASR / extraction / human-review state;
  - stable-GUID deduplication of the retained Drunk, Librarian and Recluse scouts;
  - manifest CLI and bounded live-RSS validation.
- **C2B batch acquisition — IMPLEMENTATION COMPLETE / GREEN**
  - advertised-transcript-first planning;
  - audio + optional faster-whisper fallback;
  - explicit external work directory;
  - resumable payload download;
  - resumable ASR without needless retranscription;
  - blocked-locator preservation;
  - batch runner + CLI;
  - progress application that cannot promote extraction/human-review/verification state.

- **C2C structured candidate extraction — IMPLEMENTATION COMPLETE / GREEN**
  - timestamp-preserving lightweight candidate artifacts;
  - 13 C2 candidate categories;
  - concise machine summary/tags/confidence without transcript bodies;
  - zero-candidate episodes remain normal completed extraction;
  - human review remains independent from extraction completion;
  - adjacent-ASR-segment rationale matching with overlapping-window deduplication;
  - candidate CLI.

The latest C2C quality gate passed Install / Ruff check / Ruff format / Pytest.

A bounded real two-episode C2B -> C2C validation has completed successfully for **Investigator + Imp**. Full audio/transcript artifacts remained outside Git; the workflow uploaded lightweight validation artifacts only. This is acquisition/extraction validation, not reviewed evidence.

C2D implementation is now GREEN. `podcast_review.py`, focused tests and `podcast_review_cli.py` define deterministic merging, review priorities, review-time/window budgets, a lightweight packet writer and the `clocktower-podcast-review` entry point.

The successful real Investigator/Imp candidate artifacts from bounded validation run #4 were reused directly with no retranscription and converted into real C2D review packets:

- Investigator: 63 candidates -> 53 merged windows -> 12 selected windows / 16 selected candidate hits / 127.32 seconds;
- Imp: 61 candidates -> 50 merged windows -> 12 selected windows / 17 selected candidate hits / 258.28 seconds;
- combined: 24 windows / 385.60 seconds (6m25.6s).

Both packets remain `human_review_state=NOT_STARTED`; no candidate has been promoted to verified evidence. The durable per-window human-review queue is `docs/C2D_PRIMARY_AUDIO_REVIEW_QUEUE_2026-09-30.md`.

C2D-S full-transcript semantic review is now **accepted for machine-first review assistance** after the Investigator benchmark. The Oracle VM produced a complete 2,156-segment `small.en` ASR, the semantic reviewer read the full transcript, timestamps were independently corrected against raw ASR, and the user confirmed the extracted Storyteller guidance was materially correct based on a prior full-episode listen.

One human correction is retained as a regression/QA example: the machine over-generalized the Spy discussion. The user's interpretation is that a one-Minion Spy + Investigator setup is comparatively uncommon because direct exposure reduces Spy operating room; if that exact setup exists, the Storyteller may have little alternative about which actual Minion can be identified.

The default clear-podcast path is therefore complete ASR -> full-transcript semantic extraction -> targeted human verification -> VERIFIED promotion. Full-episode human listening is reserved for low-confidence ASR, attribution/semantic conflicts, or sampled QA. Full audio/transcripts remain temporary and outside Git.

The per-episode Mini MCP task experiment has now been replaced by a fixed EvidenceLab semantic queue contract. EvidenceLab owns episode selection from the fixed Cult of the Clocktower feed and Trouble Brewing scope; Mini MCP only needs reusable `semantic:podcast:prepare-next`, `semantic:podcast:render-current`, and `semantic:podcast:cleanup-current` tasks bound to one external queue root. This removes the need to add Mini MCP task names or restart Mini MCP for each new episode.

The cross-project **C3 — Drunk Candidate Comparison / Rejection Evidence** dependency has now satisfied its first acceptance gate. Q04 is primary-audio VERIFIED with a reconstructable assignment-time condition, Monk vs Empath conditional preference, explicit rationale and trusted provenance. C3 remains available for long-term Drunk evidence, but it no longer stops C2 or blocks the current Host implementation.

The C2C/C2D audit found no need for a new evidence schema or ranking subsystem: `EXPLICIT_ALTERNATIVE` is already P0. Conservative locator coverage for explicit rejection, explicit preference and conditional Drunk-assignment expressions remains useful for future corpus growth.

The TB snapshot interoperability dependency is closed for the current Drunk surface. Host TBGS-1 accepted the EvidenceLab materializer/fixture and independently confirmed the G10 V1 payload byte-for-byte. Host has also completed its re-entry audit after Q04; the EvidenceLab blocker is cleared and Host now owns `DRUNK_ASSIGNMENT_Q04_V1 -> replay -> cutover gate re-run`.

Latest live baseline at the EL-ML0 audit start:
- `origin/main`: `1af0952dbee1c4804013c906dbe3505966ca10ba`;
- EL-ML0 docs branch was created directly from that exact main;
- working tree was clean before EL-ML0 edits;
- local `quality` after the docs-only audit: PASS, 139 tests;
- the earlier bounded C2 Investigator/Imp validation run #4 remains historical acquisition evidence, not the current Git checkpoint.

## 3. Current task

Resume **C2 as the primary lane**. EL-ML0 is a completed architecture checkpoint and does not compete with C2. C3 Stage 1 is accepted and no longer blocks Host:

- treat the Investigator C2D-S benchmark as accepted for machine-first semantic review assistance;
- treat the completed Drunk semantic pass as machine review assistance only: Q01 gives strong new-player Monk/Soldier-vs-Ravenkeeper conditional guidance, Q02 gives Empath rejection guidance, and Q03 gives a fixed Chef example, but none alone supplies the strict same-prefix A-vs-B comparison required for Stage 1;
- treat `Cult of the Clocktower` hosts and episode guests as trusted expert/Storyteller clue sources per project-owner calibration; do not require a separate creator/official title;
- keep VERIFIED evidence promotion human-confirmed; semantic output remains review assistance rather than automatic evidence promotion;
- continue automatic C2 batch ingestion without pausing for C3;
- the targeted `Soldier -> Monk -> Ravenkeeper` role-cluster semantic pass is complete;
- Q04 (`Monk`, `00:43:28-00:44:30`) was human-confirmed from primary audio on 2026-10-02 and is now **VERIFIED / C3 Stage-1 accepted**;
- the semantic pass for `25: Thief, Bureaucrat, and Scapegoat (Trouble Brewing Travelers Part 2)` completed with 1,559 `small.en` segments; eight NOT VERIFIED machine Storyteller findings are retained in `docs/C2_MACHINE_SEMANTIC_FINDINGS_TB_TRAVELERS_PART2_2026-10-03.md`, and its temporary audio/ASR workspace has been cleaned;
- `4.2: Storytelling Like a Pro` has now completed a full 1,345-segment machine semantic pass; twelve NOT VERIFIED findings are retained in `docs/C2_MACHINE_SEMANTIC_FINDINGS_STORYTELLING_LIKE_A_PRO_2026-10-03.md`; the strongest product-facing themes are night-choice confirmation loops, player narrative as enrichment context, adaptive pace as context, Storyteller-speech information leakage, and decision-rationale preservation;
- `Beggar and Gunslinger (Trouble Brewing Travelers Part 1)` has now completed a full 1,662-segment machine semantic pass; eight NOT VERIFIED findings are retained in `docs/C2_MACHINE_SEMANTIC_FINDINGS_TB_BEGGAR_GUNSLINGER_2026-10-03.md`; this pass adds a strong new Traveler-assignment direction: role choice should consider current game state, intrinsic role swing/bias, arrival timing, town belief quality, and bounded player choice rather than only Traveler alignment;
- the next 788-segment Trouble Brewing wrap-up semantic pass was screened specifically against the Host C5/E3 gate; `docs/C2_MACHINE_SEMANTIC_FINDINGS_TB_WRAPUP_E3_PASS_2026-10-03.md` retains four useful NOT VERIFIED findings, including believable Drunk-Empath misinformation and Storyteller bluff-support/meta-suppression guidance, but **no E3 re-entry candidate** because no concrete observed Storyteller choice had both recoverable alternatives and committed state;
- `Saint (Trouble Brewing)` has now completed a 677-segment E3-targeted semantic pass; `docs/C2_MACHINE_SEMANTIC_FINDINGS_TB_SAINT_E3_PASS_2026-10-03.md` retains useful setup/Red-Herring/Mayor-bounce/meta guidance but **no E3 re-entry candidate**, so no C5 human-audio review is requested;
- a post-2026-09-27 re-audit of G10 Game 2 around `18:05` confirmed strong supporting Gap-B evidence but **E3 FAIL under the strict contract**: the historical Drunk Empath receives `1`, explicitly described as actually true but deliberately chosen to redirect suspicion toward the new neighbour, yet retained review context still lacks the exact 18:05 living-neighbour state and any same-state source-backed `1`-vs-`0/2` contrast; see `docs/G10_DRUNK_EMPATH_E3_REENTRY_CANDIDATE_AUDIT_2026-10-03.md`; do not spend more acquisition bandwidth on G10 unless new primary-source material exposes those missing fields;
- `Butler (Trouble Brewing)` has now completed a 1,271-segment E3-targeted semantic pass; `docs/C2_MACHINE_SEMANTIC_FINDINGS_TB_BUTLER_E3_PASS_2026-10-03.md` retains an explicit general preference to avoid showing Butler to Librarian when other Outsider-display choices exist because that can over-simplify the Butler trust puzzle, plus Demon-bluff comparison guidance, but **no historical E3 re-entry case**;
- `Spy (Trouble Brewing)` has now completed a full 2,467-segment semantic pass; `docs/C2_MACHINE_SEMANTIC_FINDINGS_TB_SPY_2026-10-03.md` retains twelve NOT VERIFIED findings. The strongest product-facing direction is that Spy registration should be chosen from the exact information ecology, adjacency, player experience and narrative consequences rather than from a fixed “Spy should look Good” default; three concrete historical choices are retained as future bounded E3 re-audit leads, but none is promoted by this machine pass;
- `17: Virgin (Trouble Brewing) - Featuring Amy Hawkes from TPI!` has now completed a full 1,344-segment semantic pass; `docs/C2_MACHINE_SEMANTIC_FINDINGS_TB_VIRGIN_2026-10-03.md` retains nine NOT VERIFIED findings. The strongest product-facing directions are to budget setup strength around Virgin's likely public confirmation network, let Spy-triggered Virgin account for the Spy's real sacrifice, normalize Storyteller nomination timing to prevent meta leakage, tailor rules clarification to player experience without creating confirmation bias, and treat Drunk Virgin as a high-breadth public misinformation choice; no new strict E3 historical case was found;
- `Chef (Trouble Brewing)` has now completed a full 1,490-segment semantic pass; `docs/C2_MACHINE_SEMANTIC_FINDINGS_TB_CHEF_2026-10-03.md` retains eleven NOT VERIFIED findings. The strongest product-facing directions are that Chef misinformation value depends on surrounding information topology, Chef can be a Drunk candidate when the truthful number would over-compress worlds, believable vs discoverable misinformation are separate objectives, and Spy/Recluse Chef registration should consider confirmation leakage and information strength rather than fixed defaults; one Drunk-Chef practice is retained as a future E3 re-audit lead but no strict E3 PASS is created;
- `14: Poisoner (Trouble Brewing)` has now completed a full 2,217-segment semantic pass; `docs/C2_MACHINE_SEMANTIC_FINDINGS_TB_POISONER_2026-10-03.md` retains seven NOT VERIFIED findings. The strongest product-facing directions are immediate misinformation value vs fragile future-chain upside, distinguishing active Poisoner agency from passive Drunk impairment, discounting clever bluff-support plans by Evil coordination risk, and treating misinformation as a longitudinal trajectory. A real poisoned-Fortune-Teller `YES`-vs-`NO` historical choice is retained as a high-priority future E3 lead, but complete decision-time state / production legal-domain reconstruction is not yet present, so no strict E3 PASS is created;
- a second post-audit found a substantially stronger G10 historical decision at approximately `16:52`: the functioning Librarian is shown the actual Drunk-Empath plus Undertaker, with human-confirmed rationale that both seats are recurring information roles and uncertainty over which is Drunk changes how both future information streams are trusted; current Host production owners prove the observed pair legal and recover **40** truthful player-visible Librarian outcomes for the exact nine-seat state; see `docs/G10_LIBRARIAN_PAIR_E3_REENTRY_CANDIDATE_AUDIT_2026-10-03.md`;
- **G10 `16:52` is now EvidenceLab E3 PASS for one bounded generic pair-information future-flexibility predicate**: The Megavoid is classified `EXPERIENCED` / independent from independent public qualification evidence; the state, observed choice, legal alternatives, explicit rationale and generic predicate mapping are all present. The rationale maps to the Host-declared `future flexibility` axis; lack of a canonical projector is downstream C5 engineering, not an acquisition failure;
- this E3 PASS should trigger a Host **C5 re-entry audit**, not an immediate `BEGINNER_CONSERVATIVE_V2` cutover. E4 remains unproven: no numeric weights, scalar score, player-count gate or global Undertaker/recurring-information role ranking is authorized;
- C2 automatic podcast ingestion continues in parallel, but broad new E3 discovery is no longer the primary blocker until Host evaluates this re-entry handoff. Continue collecting high-value evidence without spending human-review bandwidth on ordinary qualitative guidance;
- use complete ASR -> full-transcript semantic understanding -> high-value timestamped findings -> targeted human confirmation only where ambiguity, downstream policy weighting/ranking, or product judgment makes confirmation necessary;
- use only the bounded Q04 conditional preference in the Host handoff: under the source-described seating/layout condition, Monk may be preferred over the named Empath so healthy Empath information is preserved; do not infer a global role ranking;
- Q05 (`Ravenkeeper`, `01:06:24-01:06:38`) remains supporting machine-located rejection evidence, not independently Stage-1 qualifying;
- treat EL-TBGS-0/1 as accepted/closed unless a later bounded TB surface requires another field.

Goal:

```text
external feed transcript / ASR artifact
    -> timestamp-preserving machine candidate extraction
    -> lightweight candidate records
    -> zero-or-more candidates per episode
    -> later relevance ranking / bounded human review
```

Do not start by manually listening to whole episodes.

## 4. C2C minimum contract

Each candidate should preserve at least:

- stable episode/source ID;
- start/end timestamp;
- candidate category;
- concise machine summary;
- optional role/mechanism tags;
- machine extraction quality/confidence when useful;
- human-review state.

Initial categories remain those defined in the C2 authority document, including Storyteller decision/rationale, setup reasoning, misinformation, registration, Demon bluff reasoning, player experience/agency, information strength, confirmation chains, longitudinal trajectories, explicit alternatives and real-game examples.

Do not put the complete transcript text into Git-managed candidate artifacts.

## 5. Required invariants

1. extraction is a locator/triage layer, not evidence verification;
2. candidate timestamps survive deterministic serialization;
3. extraction complete does not imply human review complete;
4. ASR complete does not imply extraction complete;
5. an in-scope episode may validly yield zero useful candidates;
6. candidate records do not embed full copyrighted transcript payloads;
7. source identity is stable and inherited from the C2A manifest;
8. C2C remains source-generic enough to accept feed transcripts or ASR segments without creating a second evidence subsystem.

## 6. Implementation sequence

Completed:

```text
C2A manifest
    -> C2B batch acquisition
    -> C2C candidate extraction
    -> bounded real Investigator/Imp validation
```

Current:

```text
C2D model/writer/CLI GREEN
    -> real Investigator/Imp review packets GENERATED
    -> bounded primary-audio review (24 windows / 6m25.6s)
    -> C2E verified guidance promotion

in parallel:
Host TBGS-0 contract                         COMPLETE / ACCEPTED
    -> EvidenceLab TB snapshot mapping audit COMPLETE
    -> pure materializer + deterministic V1 serialization COMPLETE / GREEN
    -> G10 cross-project golden fixture      COMPLETE / exact Host match
    -> Host TBGS-1 consumption               COMPLETE / ACCEPTED
    -> C3-Q04 evidence re-entry               COMPLETE / BLOCKER CLEARED
    -> Host Q04 predicate/replay/cutover      OWNED BY HOST
```

Use the existing manifest, batch runner and ASR adapter. Do not add a persistence migration merely for snapshot interoperability or temporary acquisition artifacts.

## 7. Evidence boundary

Machine transcript/candidate extraction is acquisition assistance only.

Promotion requires primary-audio review confirming speaker, meaning, context and timestamp.

Keep full copyrighted audio/transcripts outside Git.

## 8. Do not do

- do not reopen broad C1 Drunk acquisition;
- do not switch back to quota-driven whole-game collection;
- do not implement BotC legality or policy scoring;
- do not add persistence migrations without a demonstrated batch-workflow need;
- do not make YouTube automation a prerequisite for C2;
- do not treat machine confidence as verification;
- do not make the TB snapshot a second canonical reconstruction store;
- do not copy Host legality or legal-candidate enumeration into EvidenceLab;
- do not generalize the snapshot contract beyond Trouble Brewing before a real second-script need exists;
- do not implement ML training, recommendation scoring, or legal-candidate enumeration in EvidenceLab;
- do not convert `LEGAL_UNCHOSEN` candidates into source-backed rejection labels or automatic DPO rejected samples;
- do not force Q04-like general expert guidance into a fabricated historical `DecisionSlice`;
- do not add an ML-readiness persistence migration until evidence volume or a concrete dataset-builder need justifies it.

## 9. Historical documents

The pre-C2 roadmap/source-strategy/C1 handoff snapshots were moved under `docs/archive/` so they remain available for provenance without competing with the current authority.

Current authority is the C2 document set listed in section 1.
