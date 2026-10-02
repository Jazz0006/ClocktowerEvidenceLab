# Clocktower Evidence Lab — Current Development Roadmap

> Status: **E0 COMPLETE / E1 COMPLETE / C0 COMPLETE / C1 COMPLETE / C2 ACTIVE / C3 STAGE-1 ACCEPTED / EL-TBGS-0/1 CROSS-PROJECT ACCEPTED**
>
> Current task: **C2 — Trouble Brewing Podcast Batch Ingestion** is again the primary EvidenceLab lane. C3-Q04 is VERIFIED / Stage-1 accepted and has already cleared the current Host evidence blocker; additional Drunk guidance remains valuable corpus material but no longer blocks Host development.

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

## 4. Current checkpoint — C2 Podcast Batch Ingestion

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

The semantic workflow is now queue-owned by EvidenceLab rather than episode-owned by Mini MCP. A fixed external queue root stores only completed GUIDs plus one marker-gated `current` workspace. `prepare-next` selects the next semantic-eligible episode from the fixed feed, `render-current` streams its complete transcript, and `cleanup-current` deletes the temporary media/ASR before advancing the lightweight queue state. Investigator, Imp, `4.1: Trouble Brewing Revisited`, Drunk, Soldier, Monk, and Ravenkeeper semantic passes are complete. Q04 in the Monk episode is now human-verified and Stage-1 accepted. With the Host blocker cleared, the queue returns to high-value C2 collection; the explicitly curated general episode `4.2: Storytelling Like a Pro` is prioritized when unprocessed because it is Storyteller-focused despite lacking a Trouble Brewing label. This is a narrow curated exception, not a general cross-script scope expansion.

### C2E — evidence promotion

After primary-audio review, save concise provenance-backed expert-guidance evidence. Do not commit full transcripts.

Authority: `docs/C2_TB_PODCAST_BATCH_INGESTION_2026-09-29.md`.

## 5. C3 — Drunk Candidate Comparison / Rejection Evidence — STAGE-1 ACCEPTED

CampBoardGameHost's Drunk-assignment production cutover audit established a concrete downstream gap: execution infrastructure is ready, but Beginner automatic assignment still lacks source-backed semantics for comparing or rejecting legal Drunk candidates under one fixed setup/history prefix.

C3 therefore reuses C2 rather than creating new acquisition infrastructure:

```text
RSS / audio
    -> ASR
    -> C2C candidate extraction
    -> C2D bounded review
    -> human primary-audio verification
    -> verified comparison evidence
```

The C2C/C2D audit found that `EXPLICIT_ALTERNATIVE` is already the correct semantic bucket and already receives P0 review priority. The narrow implementation gap is locator vocabulary: explicit rejection, explicit preference and conditional Drunk-assignment language must be discoverable even when the speaker does not say “Storyteller”.

C3 Stage-1 acceptance is **not a quota**. It is one VERIFIED item with:

```text
fixed setup/history prefix
+ candidate A vs candidate B
+ explicit preference/rejection
+ rationale
+ reconstructable assignment-time context
```

**C3 Stage 1 is now SATISFIED** by Q04 (`12: Monk`, `00:43:28–00:44:30`), human-confirmed from primary audio on 2026-10-02. The bounded evidence authorizes only the described conditional preference: under the source-described seating/layout condition, prefer Monk over the named Empath as the Drunk so healthy Empath information is preserved. It does not authorize a global Monk > Empath ranking.

The EvidenceLab -> CampBoardGameHost handoff is recorded in `docs/C3_Q04_VERIFIED_MONK_CONDITIONAL_PREFERENCE_HANDOFF_2026-10-02.md`; Host may now test a first bounded, versioned Drunk production-policy predicate and rerun its cutover gate.

Do not infer rankings over unmentioned candidates, do not infer rules from outcomes, and do not encode legality or recommendation policy here. C5 / `BEGINNER_CONSERVATIVE_V2` remains a separate gate.

Authority: `docs/C3_DRUNK_CANDIDATE_COMPARISON_EVIDENCE_2026-09-30.md`.

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

Host TBGS-1 has now consumed/validated the same G10 V1 semantics, independently derived the legal Drunk domain, and accepted the cross-project seam. The former evidence blocker is now cleared by VERIFIED C3-Q04. EvidenceLab has handed off one bounded conditional preference; Host must independently map it onto the accepted decision context, define a versioned predicate, replay it, and rerun the production cutover gate before any automatic authority changes.

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

Resume C2 as the primary collection lane:

1. if `4.2: Storytelling Like a Pro` has not yet been processed, acquire its full audio/ASR into the external temporary workspace and run full-transcript machine semantic review first;
2. extract high-value Storyteller guidance across setup/role assignment, misinformation, registration, Demon bluffs, information strength, cross-night consistency, player experience, star pass / ability preservation, public claims / evil narrative, and explicit alternatives/rejected choices;
3. ask for bounded human primary-audio confirmation only where meaning is ambiguous, would materially alter downstream policy weighting/ranking, or requires product-goal judgment;
4. clean the full audio/transcript workspace after analysis and retain only lightweight provenance-backed findings in Git;
5. continue with the remaining high-density Trouble Brewing-relevant episodes after `4.2`, while allowing new Drunk guidance to enter the long-term corpus without blocking Host;
6. treat EL-TBGS-0/1 and C3 Stage 1 as accepted/closed for the current Host blocker unless a new bounded downstream gap appears.

Keep broad quota-driven C1 scouting stopped. Additional Drunk evidence is welcome as ordinary corpus growth, not as a reason to pause C2. Snapshot interoperability is an architecture/export lane, not an evidence-quality shortcut.

## 9. Deferred

- broad non-Trouble-Brewing acquisition or generalized cross-script GameState design;
- Storyteller-app telemetry;
- UI expansion;
- new persistence migrations without demonstrated need;
- policy scoring inside Evidence Lab;
- fully automated verification with no human promotion gate;
- YouTube-specific batch automation as a dependency of C2.
