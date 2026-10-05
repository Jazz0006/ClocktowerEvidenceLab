# Clocktower Evidence Lab — Current Development Roadmap

> Status: **E0 COMPLETE / E1 COMPLETE / C0 COMPLETE / C1 COMPLETE / C2 ON-DEMAND / EL-LRE0 ALIGNED / C3 STAGE-1 HISTORICAL-SUPPORTING / EL-TBGS-0/1 CROSS-PROJECT ACCEPTED / EL-ML0 ACCEPTED / EL-ML1A BENCHMARK AUDIT COMPLETE / EL-ML1C SOURCE ACQUISITION AUDIT COMPLETE**
>
> Current task: **EL-ML1B benchmark manifest + whole-game decision-prefix repair**. EL-ML1C has pre-audited the next whole-game acquisition route but broad acquisition remains gated until existing-corpus repair is measured against the 20–30 READY pilot target. C2 and EL-LRE remain available as bounded on-demand evidence lanes; broad podcast policy mining, broad Drunk acquisition and broad C5/E3 hunting remain stopped.

## 1. Program objective

Build a durable evidence system that replaces ad-hoc synthetic judgment with provenance-backed external evidence.

The corpus has two complementary tracks:

```text
whole real games
    -> historical reconstruction / replay evidence

qualified expert guidance
    -> rationale / policy-dimension evidence
```

Whole-game history remains the primary historical collection unit. Expert guidance does not become replay evidence merely because the source is authoritative.

## 2. Frozen boundaries

- Evidence Lab owns evidence, reconstruction, provenance, verification and acquisition workflow.
- CampBoardGameHost owns BotC legality, legal alternatives, world solving and recommendation policy.
- UNKNOWN is first-class.
- Later history must not leak backward into earlier decisions.
- machine extraction is not equivalent to verified evidence.
- raw copyrighted media and full transcripts stay outside Git.
- expert choice/guidance is evidence, not a GOOD/BAD policy label.
- whole-game and expert-guidance corpora remain distinguishable even when they inform the same downstream feature.
- authoritative reconstruction remains setup commitments + semantic events; any TB Game Snapshot is a derived materialized/interchange view only.
- snapshot semantics must distinguish `UNCOMMITTED` from evidence `UNKNOWN`; provenance/verification remains outside the snapshot payload.
- ML-ready projections remain derived evidence packaging, not new truth or training labels; `OBSERVED_CHOICE`, `EXPLICIT_PREFERENCE`, `EXPLICIT_REJECTION`, `EXPLICIT_COMPARISON_LOSER`, downstream `LEGAL_UNCHOSEN`, and `SYNTHETIC_NEGATIVE` must remain distinct.
- future recommendation-model input may contain only state committed before the historical decision boundary; later decisions/events/outcome remain target/evaluation metadata.

## 3. Completed checkpoints

### E0 — evidence-contract pilot — COMPLETE

Established the source/evidence/reconstruction/verification contract using a real primary-source Trouble Brewing game.

### E1 — domain and persistence foundation — COMPLETE / MERGED

Established Python/Pydantic/SQLite/SQLAlchemy/Alembic/pytest/Ruff foundation, provenance entities, versioned interchange, reconstruction identity, setup/event history and durable evidence invariants.

### C0 — Trouble Brewing acquisition/reconstruction checkpoint — COMPLETE

Established a representative whole-game corpus and cross-project evidence handoff. Broad quota-driven corpus growth is no longer the default.

### C1 — Drunk Assignment Evidence Upgrade — COMPLETE

Established:

- Drunk existence != Drunk assignment != Drunk misinformation;
- setup-time historical-prefix contracts;
- 3/3 replayable assignment cases;
- 2 explicit historical assignment-rationale cases;
- successful G10 downstream replay in CampBoardGameHost.

C1 targeted acquisition is stopped unless a concrete downstream gap reopens it.

### EL-ML0 — ML Readiness Contract — COMPLETE / ARCHITECTURE ACCEPTED

The read-only audit accepted the three-layer boundary:

```text
EvidenceLab canonical evidence
    -> RecommendationEvidenceSeedV1 derived projection
    -> Host / future ModelLab enrichment
    -> RecommendationTrainingExampleV1
```

`DecisionSlice` remains the canonical historical-decision owner and already supplies the key anti-leakage boundary, observed choice, rationale references and source-backed explicit alternatives. A future seed exporter should compose it with verification, source assertion provenance and Storyteller independence metadata rather than duplicate it.

Q04 demonstrates a separate non-historical expert-comparative-guidance shape; a future `ExpertPreferenceEvidence` / `ComparativeGuidanceEvidence` durable type is likely useful, but implementation and any persistence migration are deferred until evidence volume or a concrete dataset-builder milestone justifies them.

Authority: `docs/ML_RECOMMENDATION_EVIDENCE_READINESS_CONTRACT_2026-10-03.md`.

### EL-ML1A — Decision Point Benchmark Corpus Audit — COMPLETE / CONTRACT ACCEPTED

EL-ML1A re-audited the existing corpus for the stronger model-backed recommendation goal rather than deterministic policy replacement. The conservative inventory is:

```text
READY historical decision points: 6
independent game groups:          3
Storyteller independence groups: approximately 2
high-value PARTIAL candidates:    >= 18
```

The main scarcity is now independent, leak-free whole-game decision states rather than generic expert principles. The accepted pilot target is 20–30 READY historical decision points across at least 8 games and 4 Storyteller independence groups, with at least 40% later-game/history-sensitive decisions.

Broad podcast policy mining is no longer the default marginal-value path. The next route is EL-ML1B: materialize the six READY benchmark seeds, repair G10/R04/FT1-A/WW2/UT1-A historical prefixes, then acquire new complete games only if existing repair cannot reach the pilot target.

Authority: `docs/EL_ML1A_DECISION_POINT_BENCHMARK_AUDIT_2026-10-05.md`.

### EL-ML1B-1 — Benchmark Manifest V1 — IMPLEMENTATION COMPLETE

The first machine-readable benchmark surface is implemented:

- versioned `DecisionPointBenchmarkManifestV1` / entry contract;
- deterministic JSON dump/load;
- explicit `READY / PARTIAL / NOT_USABLE` readiness;
- explicit `DOCUMENTED_READY` versus `CANONICAL_SEED_MATERIALIZED` state;
- game/source/Storyteller split-group keys;
- allowed evaluation-mode metadata;
- a checked-in six-row manifest at `docs/EL_ML1B_READY_HISTORICAL_BENCHMARK_V1.json`.

### EL-ML1B-1B — Canonical historical decision materialization — IN PROGRESS / 1 OF 6 MATERIALIZED

The six-row canonicalization audit is complete. It confirms that benchmark `READY` does not by itself justify a canonical machine seed.

The first real materialization is **DP-R05 — G10 Game 2 Drunk assignment**:

- generic derived `HistoricalDecisionSeedV1` contract;
- checked-in canonical seed at `docs/EL_ML1B_G10_DP_R05_CANONICAL_SEED_V1.json`;
- real `DecisionSlice` + evidenced grouped setup history + source/assertion provenance;
- executable `HistoricalPrefixBoundary` that yields only the pre-assignment shown-role layout;
- manifest state promoted to `CANONICAL_SEED_MATERIALIZED`;
- Host enrichment requirement reduced to `LEGAL_CANDIDATE_DOMAIN`.

The remaining five rows stay `DOCUMENTED_READY`. Current audit disposition:

- **G01 DP-R01/DP-R02:** strongest next pair; materialize together from one canonical G01 reconstruction, after resolving Storyteller/controller grouping without inventing a single Ben+Adam identity;
- **G05 DP-R03/DP-R04:** blocked because the repository currently records that the complete layout was fixed but does not retain the full seat/role map;
- **G10 DP-R06:** blocked until setup chronology/completeness at the Librarian decision boundary is evidence-backed; do not infer Demon-bluff prefix membership from video order or BotC rules.

Authority: `docs/EL_ML1B_CANONICALIZATION_AUDIT_2026-10-05.md`.

No persistence migration, Host legality, legal-candidate enumeration, recommendation scoring, or inferred rejection semantics were added.

### EL-ML1C — Whole-Game Source Acquisition Audit — COMPLETE / PILOT GATED

EL-ML1C pre-audited how new complete Trouble Brewing games should be acquired if EL-ML1B repair cannot reach the pilot target.

Accepted source order:

```text
ClockTracker public complete-game records
    + matching Storyteller-POV YouTube where available
    -> preferred near-term cross-source reconstruction

explicit digital-grimoire event export / read API
    -> future highest-value structured external lane once stable/permitted

Twitch / actual-play audio
    -> supporting whole-game sources

expert role / Storyteller podcasts
    -> rationale/gap-filling lane, not default corpus growth
```

The audit confirms that ClockTracker public records can sometimes contain detailed Night/Day chronological Notes, while its internal GrimoireSnapshot history is save/edit history and owner-authenticated rather than a public semantic gameplay event stream. Storyteller-POV video remains the strongest chronology/rationale complement. Machine discovery, screening, draft reconstruction and rules-independent consistency checks should be automated; VERIFIED promotion remains human-gated for ambiguous/high-value evidence.

If new acquisition is triggered, run the bounded `CT-1 + YT-1 + DG-1` pilot defined in `docs/EL_ML1C_WHOLE_GAME_SOURCE_ACQUISITION_AUDIT_2026-10-05.md` before building any broad crawler or new persistence layer.

### EL-LRE0 — Host LRE Evidence Alignment — AUDIT COMPLETE / ACTIVE ROUTE

EL-LRE0 aligned EvidenceLab with Host's staged recommendation replacement route without changing the canonical evidence model or C2 ingestion architecture.

The retained EL-LRE relationship is:

```text
on-demand C2 acquisition / review
        +
Host LRE bounded evidence requests
        ↓
EvidenceLab verified comparative evidence
        ↓
Host versioned policy / retrieval evidence
        ↓
Host replay / evaluation
```

EvidenceLab records source-backed choices, preferences, rejections, comparison losers, rationale, conditions and provenance. Host owns legal alternatives, `LEGAL_UNCHOSEN`, policy scoring/versioning, replay and production authority.

No SQLite/Alembic migration is required. EL-ML0 remains accepted unchanged; EL-ML1B may add only the smallest derived benchmark/export projection required by the concrete benchmark consumer.

Authority: `docs/EL_LRE_REPLACEMENT_POLICY_EVIDENCE_ALIGNMENT_2026-10-04.md`.

## 4. C2 Podcast Batch Ingestion — Operational Background

The earlier podcast pilot proved the route:

```text
RSS -> audio locator -> ASR -> timestamped candidates -> bounded human review
```

Reusable RSS/ASR tooling and Drunk/Librarian/Recluse scout artifacts are already on main.

C2 now turns that one-off path into a batch pipeline for the remaining Trouble Brewing-relevant episodes of the same expert series.

### C2A — manifest — COMPLETE / GREEN

Live RSS inventory, stable source identity, Trouble Brewing scope classification, independent workflow states and Drunk/Librarian/Recluse prior-scout deduplication are implemented and covered by deterministic tests plus a bounded live RSS validation.

### C2B — batch acquisition — IMPLEMENTATION COMPLETE / GREEN

The batch planner/runner and CLI now:

- prefer advertised transcript locators when present;
- otherwise acquire public audio into an explicit external work directory;
- run timestamped ASR through the retained optional adapter;
- reuse existing payload and ASR artifacts after interruption;
- preserve blocked/missing-locator items explicitly;
- write only lightweight progress/updated-manifest metadata alongside external artifacts;
- never promote ASR completion into human review or evidence verification.

A bounded real two-episode operational validation has completed successfully for Investigator and Imp. This proves the C2B acquisition path on real inputs but does not mean the resulting candidates have been human-reviewed or promoted.

### C2C — structured extraction — IMPLEMENTATION COMPLETE / GREEN

The extractor now provides timestamp-preserving lightweight candidate artifacts across the C2 category set, including Storyteller decisions/rationale, setup reasoning, misinformation, registration, Demon bluff reasoning, player experience/agency, information strength, confirmation chains, longitudinal trajectories, explicit alternatives and real-game examples.

The extractor:
- preserves stable source identity and start/end timestamps;
- stores concise machine summaries/tags/confidence without transcript bodies;
- treats zero useful candidates as a normal completed extraction;
- keeps human-review state independent from extraction completion;
- matches rationale terms across adjacent ASR segments and merges overlapping windows to avoid duplicate review packets.

A bounded real two-episode C2B -> C2C validation has completed successfully for Investigator and Imp.

### C2D — bounded human review — IMPLEMENTATION GREEN / REAL REVIEW QUEUE READY

The review-packet model, deterministic candidate merge/ranking, time/window budgets, lightweight writer and `clocktower-podcast-review` CLI are implemented and GREEN. P0/P1/P2 remain review-triage priorities only and do not score Storyteller choices.

The successful bounded Investigator/Imp run #4 artifacts have now been passed through C2D without retranscription:

- Investigator: 63 machine candidates -> 53 merged windows -> 12 selected review windows covering 16 candidate hits; 127.32 seconds total review time.
- Imp: 61 machine candidates -> 50 merged windows -> 12 selected review windows covering 17 candidate hits; 258.28 seconds total review time.
- Combined bounded primary-audio queue: 24 windows / 385.60 seconds (6m25.6s).

Both review packets retain `human_review_state=NOT_STARTED`. Packet generation is acquisition assistance, not evidence verification. The next gate is actual human primary-audio review of those bounded windows.

### C2D-S — full-transcript semantic review — INVESTIGATOR BENCHMARK ACCEPTED

The first machine-first full-transcript benchmark has completed for **18: Investigator (Trouble Brewing)**. The Oracle VM produced a complete `small.en` ASR with 2,156 timestamped segments, the semantic reviewer read the complete transcript, and the user independently compared the extracted Storyteller guidance against a prior full-episode listen.

The semantic extraction was accepted as materially correct. It recovered experience-dependent setup choices, whole-setup information-density considerations, Drunk/Investigator discoverability, Recluse registration options, non-Minion target rationale, and multi-role information topology that the earlier keyword locator could not reliably reconstruct.

One human correction is retained as a QA example: the machine summary over-generalized the Spy discussion. The user's full-episode interpretation is that a one-Minion Spy + Investigator setup is comparatively uncommon because direct Investigator exposure reduces the Spy's room to operate; when that exact setup exists, the Storyteller may have little choice about which actual Minion can be identified. This is evidence that semantic review is useful but still benefits from targeted human verification.

The accepted default path for clear expert-podcast audio is now:

```text
Oracle VM temporary audio
    -> complete timestamped ASR
    -> full-transcript semantic reading
    -> Storyteller considerations / rationale / conditions / alternatives
    -> targeted human verification of extracted findings and ambiguities
    -> VERIFIED promotion only after human confirmation
    -> delete temporary audio + transcript
```

Full-episode human listening is no longer the default for every clear podcast episode. It remains available for low-confidence ASR, attribution problems, semantic conflicts, or sampled QA.

The semantic workflow is queue-owned by EvidenceLab rather than episode-owned by Mini MCP. A fixed external queue root stores completed GUIDs plus a two-slot `current`/`prefetch` pipeline: while `current` is being semantically reviewed, `prepare-next` may acquire and transcribe the next episode into `prefetch`; `cleanup-current` promotes a ready prefetch atomically, while leaving an in-flight prefetch untouched; `render-current` can promote a ready prefetch if no current workspace exists. Completed passes now include Investigator, Imp, `4.1: Trouble Brewing Revisited`, Drunk, Soldier, Monk, Ravenkeeper, Travelers Part 2, the curated `4.2: Storytelling Like a Pro`, Beggar/Gunslinger, the Trouble Brewing wrap-up, Saint, Butler, Spy, Virgin, Chef, Poisoner, Washerwoman, Baron, Librarian, Empath, Recluse, Scarlet Woman, Mayor, Fortune Teller, Undertaker, and Slayer. The fixed Trouble Brewing semantic-eligible podcast queue is now **EXHAUSTED**: after Slayer, `prepare-next` returned `no unprocessed Trouble Brewing podcast episodes remain`. Q04 in the Monk episode remains human-verified and Stage-1 accepted. C2 therefore shifts from feed traversal to on-demand acquisition/review only when a new bounded Host evidence gap or deliberately broadened source scope is authorized.

### C2E — evidence promotion

After primary-audio review, save concise provenance-backed expert-guidance evidence. Do not commit full transcripts.

Authority: `docs/C2_TB_PODCAST_BATCH_INGESTION_2026-09-29.md`.

## 5. EL-LRE — replacement-policy evidence lane — ACTIVE

EL-LRE generalizes the successful C3 comparison pattern across Host decision families. It reuses C2 rather than creating another acquisition stack.

Highest-value evidence shape:

```text
fixed / bounded decision context
+ observed or explicitly preferred candidate A
+ explicit alternative B / rejected candidate / comparison loser
+ source-backed rationale
+ conditions / limitations
+ provenance / verification
```

A historical full-domain case is valuable but is not mandatory for every policy dimension. Verified generic expert comparative guidance may support a narrow Host predicate when its scope is explicit.

Current milestone state:

1. **Priority 1 healthy first-night/setup is VERIFIED for bounded dimensions:** Washerwoman (`WW1`), Investigator (`INV1`), Demon bluffs (`DB1`), and Red Herring (`RH1`) are ready for Host legal-domain mapping, versioned policy design, replay/evaluation and cutover work. None authorizes a complete family-wide ranking.
2. **Priority 2 has a substantial VERIFIED set:** Fortune Teller impairment (`FT1`), impaired Washerwoman (`WW2`), Chef (`CHEF1`), Empath (`EM1`), Undertaker (`UT1`), and Librarian (`LIB1`). These provide bounded preferences, tradeoffs, historical choices and descriptive dimensions; Host still owns candidate legality, policy scope and replay.
3. **Remaining EvidenceLab-first gaps:** Ravenkeeper is **RK1 PARTIAL VERIFIED-DIMENSION**; impaired Investigator is **INV2 VERIFIED LEGAL-AXIS + HISTORICAL SUPPORT / PREFERENCE GAP**; Spy/Recluse registration is **SR1 PARTIAL VERIFIED-DIMENSION / CONDITIONAL PARTITION READY**; Mayor redirect is **MR1 PARTIAL VERIFIED-DIMENSION / TARGET-CLASS MODEL READY**; and Demon succession is now **DS1 VERIFIED CONTROL + VERIFIED SUCCESSOR COMPARISON / HOST-ENRICHMENT**. Primary-audio review confirmed Spy M11: in ordinary Star Pass, choosing the strongest / most trusted Minion is a common tendency, but it must not become an absolute rule; in the verified counterexample, retaining a highly trusted Spy as support for the new Demon made a less-trusted Baron the situational choice. DS1 no longer has an immediate EvidenceLab blocker for a bounded Host experiment.

The consolidated Host-facing index is `docs/EL_LRE_VERIFIED_HOST_HANDOFF_INDEX_2026-10-04.md`. It is the preferred entry point for downstream consumption; individual verified handoffs remain the source of detail.

C3-Q04 remains VERIFIED historical/supporting evidence and proves this acquisition shape works. It is no longer the general continuation lane. Host has already cut over `DRUNK_ASSIGNMENT_Q04_V1`; broad Drunk scouting stays closed.

Authority: `docs/EL_LRE_REPLACEMENT_POLICY_EVIDENCE_ALIGNMENT_2026-10-04.md`.

## 6. TB Game Snapshot interoperability — EL-TBGS-0/1 CROSS-PROJECT ACCEPTED

Host TBGS-0 is COMPLETE / ACCEPTED. EvidenceLab now implements the same immutable `TroubleBrewingGameSnapshotV1` semantics as a pure projection from one reconstruction revision + one historical prefix.

Completed locally:

```text
Host TBGS-0 contract                           COMPLETE / ACCEPTED
-> EvidenceLab mapping audit                  COMPLETE
-> pure materializer + deterministic V1 JSON COMPLETE / GREEN
-> G10 pre-Drunk golden fixture               COMPLETE / exact Host match
```

The implementation preserves event sourcing as authority, adds no legality/policy, and requires no persistence migration. The historical expert choice/rationale/provenance stays outside the pre-decision snapshot. `gameSeed` and role-type classification are explicit non-evidence projection metadata rather than invented historical facts or EvidenceLab-owned legality.

Host TBGS-1 has consumed/validated the same G10 V1 semantics, independently derived the legal Drunk domain, and accepted the cross-project seam. That interoperability work is closed for the current scope. Host has since cut over `DRUNK_ASSIGNMENT_Q04_V1` and functioning Librarian V2 as new-policy islands; EvidenceLab retains their source evidence but does not reopen those scopes without a new bounded Host evidence request.

Authorities:

- `docs/TB_GAME_SNAPSHOT_INTEROPERABILITY_ROUTE_2026-09-30.md`;
- `docs/EL_TBGS_0_1_MAPPING_AND_IMPLEMENTATION_AUDIT_2026-09-30.md`.

## 7. C2 implementation constraints

- do not block C2 on YouTube automation;
- do not retranscribe already-processed stable episode identities unnecessarily;
- do not add a database migration merely to store temporary ASR output;
- keep full audio/transcripts outside Git;
- test stable manifest/extraction contracts and pure transformations;
- preserve machine-vs-human verification state explicitly;
- allow an episode to yield no useful candidate without treating that as failure.

## 8. Immediate next action

Run **EL-ML1B — canonical benchmark materialization + existing-corpus prefix repair**:

1. **EL-ML1B-1B:** convert the six checked-in `DOCUMENTED_READY` rows into genuine canonical historical decision seeds only where `DecisionSlice + prefix + provenance` can be materialized without guessing; begin with G10/G01/G05;
2. materialize bounded prefixes for the three later G10 decisions, keeping every G10 point in one split group;
3. close the known R04 replay blockers before searching for another whole game;
4. reconstruct exact pre-decision prefixes for FT1-A, WW2 and UT1-A because rationale evidence is already strong;
5. repair R01/R02/R03 and the existing Investigator/Ravenkeeper whole-game candidates as source access permits;
6. only if READY remains below 20 after repair, trigger EL-ML1C's bounded `CT-1 + YT-1 + DG-1` source pilot, then acquire new complete Trouble Brewing games from the highest-yield lane with Storyteller/grimoire visibility, later-game coverage and greater Storyteller independence.

C2 and EL-LRE remain bounded on-demand lanes for benchmark-discovered evidence gaps. Keep broad quota-driven C1 scouting, broad Drunk acquisition, broad C5/E3 hunting and broad podcast policy mining stopped.

## 9. Deferred

- broad non-Trouble-Brewing acquisition or generalized cross-script GameState design;
- Storyteller-app telemetry;
- UI expansion;
- new persistence migrations without demonstrated need, including any EL-LRE0-only migration;
- policy scoring inside Evidence Lab;
- fully automated verification with no human promotion gate;
- YouTube-specific batch automation as a dependency of C2;
- durable persistence/schema migration for `RecommendationEvidenceSeedV1`; EL-ML1B authorizes only the smallest derived benchmark/export projection needed by the concrete benchmark consumer;
- durable `ExpertPreferenceEvidence` / `ComparativeGuidanceEvidence` until verified comparative-guidance volume justifies a typed entity;
- generalized training-example schemas, SFT/DPO/QLoRA pipelines, negative-sampling recipes and model training inside EvidenceLab.
