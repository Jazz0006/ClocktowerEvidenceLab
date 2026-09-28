# NEXT DEVELOPMENT HANDOFF — C1 Drunk Assignment Evidence Upgrade

> Current state: **C1A + C1B COMPLETE / C1C IN PROGRESS — bounded primary review queue ready**
>
> Current branch: `c1-drunk-assignment-evidence-upgrade`
>
> Do not merge without explicit project-owner authorization.

## 1. Read first

Read in this order:

1. `AGENTS.md`
2. `README.md`
3. `docs/ARCHITECTURE.md`
4. `docs/EVIDENCE_AND_PROVENANCE_STANDARD.md`
5. `docs/SOURCE_COLLECTION_STRATEGY.md`
6. `docs/TESTING_STRATEGY.md`
7. `docs/CURRENT_DEVELOPMENT_ROADMAP.md`
8. `docs/C1_DRUNK_ASSIGNMENT_EVIDENCE_UPGRADE_2026-09-28.md`
9. this file

Use older E0/E1/C0 artifacts as historical evidence/reconstruction records. Do not treat dated branch/PR status inside those artifacts as live repository instructions.

## 2. Live baseline at C1 planning start

Repository: `Jazz0006/ClocktowerEvidenceLab`.

Default branch: `main`.

E0 is merged.

E1/C0 checkpoint is merged.

PR #2 — `E1: domain and persistence foundation` — was squash-merged on 2026-09-23.

C1 planning baseline main commit:

`157a91f47112a7e4af02bc6e4c9e8613ef99d490`

C1 branch was created from that exact commit:

`c1-drunk-assignment-evidence-upgrade`

The first C1 branch work is documentation/contract synchronization only. Production/domain implementation has not started yet.

At the start of the next conversation, re-check live branch/HEAD/working state rather than assuming this checkpoint is unchanged.

## 3. Why the route changed

CampBoardGameHost now intends the setup/template layer to decide only whether a Drunk exists.

After shown roles/seating exist, the Storyteller Decision Engine will choose which shown Townsfolk seat is actually the Drunk.

Therefore the Evidence Lab must stop treating the selected Drunk identity only as fixed input and must preserve the setup-time expert decision itself.

Frozen semantic split:

```text
Drunk existence
    ≠
Drunk assignment
    ≠
Drunk misinformation
```

The current evidence gap is **Drunk assignment**.

## 4. Non-negotiable boundaries

Preserve these during implementation:

- whole-game history remains the primary collection unit;
- authoritative reconstruction history remains SetupCommitment + SemanticEvent;
- DecisionSlice is a derived analytical view, not a second history store;
- the Drunk-assignment decision prefix must stop before the resulting assignment commitment;
- later setup/events must not leak backward into that prefix;
- Evidence Lab may preserve explicit Storyteller rationale, considered alternatives and rejected alternatives when sourced;
- Evidence Lab must **not** enumerate legal Drunk candidates from BotC rules;
- CampBoardGameHost owns legality, candidate enumeration, SDE policy and replay evaluation;
- assignment rationale and later misinformation rationale must not be conflated;
- UNKNOWN is preferred over inferred motive;
- no persistence migration is justified merely because C1 introduces a new concept.

## 5. C1A completion checkpoint

C1A is complete. The smallest generic domain contract was implemented tests-first.

Implementation evidence:

- RED contract: `8ec9a22770eab30b428b5a9a97b302ab20aa6ec1`;
- formatting-only correction before meaningful RED: `8c80d80d997a89852c22eb77a350e86af6fb16aa`;
- quality run #120 reached pytest and failed as expected because `domain.decision` did not yet exist;
- GREEN implementation: `a44b6b16cd46939b8aef3db5dffb8e1d02b5c94e`;
- exact-audit cleanup: `01ef9d3f3df09581776d9ab6b052d0f1a64b318f`;
- quality run #122: PASS — Ruff check, Ruff format and 65 pytest tests.

Implemented generic domain contract:

Required concepts:

1. `HistoricalPrefixBoundary`
   - supports setup-prefix and ordinary event-prefix boundaries;
   - cannot ambiguously point to both;
   - must be compatible with deterministic historical ordering.

2. generic `DecisionSlice`
   - revision/game identity;
   - decision type;
   - Storyteller control ownership;
   - historical prefix boundary;
   - observed choice;
   - linkage to the resulting SetupCommitment or SemanticEvent;
   - optional source-backed rationale;
   - optional explicitly considered/rejected alternatives;
   - UNKNOWN-friendly representation.

Do not create Drunk-specific policy/rules classes when the generic contract is sufficient.

## 6. C1A test contract — SATISFIED

The focused C1A tests prove:

1. a setup-time decision prefix cannot include its own resulting SetupCommitment;
2. later setup commitments cannot leak into that earlier prefix;
3. later SemanticEvents cannot leak into that earlier prefix;
4. explicitly observed alternatives remain distinct from downstream-derived legal alternatives;
5. UNKNOWN rationale/alternatives are preserved;
6. the resulting historical state still lives in authoritative reconstruction history;
7. generic contracts can represent `DRUNK_ASSIGNMENT` without implementing Trouble Brewing legality.

Follow the normal sequence:

```text
define invariant
→ focused RED
→ minimal generic implementation
→ focused GREEN
→ full Ruff / pytest gate
→ exact diff review
```

## 7. C1B completion checkpoint

C1B is complete.

Re-audited cases:

- E0 `A Stud In Scarlet`;
- R02;
- R03;
- R04.

Detailed result:

- `docs/C1B_EXISTING_DRUNK_ASSIGNMENT_REAUDIT_2026-09-28.md`.

Key findings:

- 4 cases contain some assignment-result evidence;
- only E0 establishes both selected participant/visible seat and shown Townsfolk;
- none has an evidence-backed reconstructable pre-assignment prefix;
- none contains explicit assignment rationale or assignment alternatives;
- later Drunk misinformation/confirmation cannot backfill the assignment prefix;
- the historical E0 `DS-ASIS-001` terminology must not be silently upgraded into a replay-ready C1 Drunk-assignment DecisionSlice.

C1B also added the generic `SetupOrderBasis` guard after real corpus pressure exposed that deterministic setup ordering can be only canonical rather than historical.

Tests-first evidence:

- RED: `058be4254f60cf34330c2fe08d22d185e493c447`;
- quality #125 reached pytest and failed because `SetupOrderBasis` was absent;
- history contract: `2b63cb781b0804b8744e2c56322ac29f539c2c6b`;
- prefix guard: `d4aae665ebf291e3247df131183848130ffe2dba`;
- formatting-only follow-ups: `5adc2e191ef58ba2322d10083d17f372b6e8c9fc`, `03a52a15c5f6f3ad3bfbc2fae574e5ee2603b255`;
- quality #129: PASS.

**Stop here. C1C has not started. Do not proceed automatically; wait for explicit project-owner direction.**

### C1C — targeted acquisition — IN PROGRESS

Read:

- `docs/C1C_TARGETED_DRUNK_ASSIGNMENT_ACQUISITION_2026-09-28.md`.

Do not resume broad quota-driven collection.

Current review order:

1. E0 `A Stud In Scarlet` around the known setup conversation window;
2. `Live and Imp-Person` setup section;
3. Steven Medway Drunk podcast bounded assignment section for guidance verification only;
4. official 2019 Steven Medway / Jon Gjengset Trouble Brewing setup sections if needed.

Current target remains:

- at least 3 replayable Drunk-assignment cases;
- seek 1–2 explicit historical assignment-rationale cases if available.

Current achieved replay quota: **1 / 3**.

G01 E0 is now replayable:

~~~text
complete player role / shown-role layout fixed
    ↓
Sullivan selected as Drunk, shown Empath
    ↓
Red Herring = Sullivan selected later
~~~

Rationale and alternatives remain UNKNOWN.

G02 `Live and Imp-Person` has now been reviewed:

- Brooke = Drunk shown Undertaker: VERIFIED;
- pre-assignment prefix: UNKNOWN because the source presents an already-designed setup;
- assignment rationale / alternatives: UNKNOWN;
- assignment replay quota contribution: none;
- separate high-value evidence: Ben explicitly plans early correct Drunk information to preserve Brooke's role belief, then sustained incorrect information.

G03 official 2019 Game 2 has now been screened out for C1C because the primary setup contains no Drunk. Its Poisoner/Investigator/Empath Night-1 bundle is useful ancillary evidence only.

G04 official 2019 Game 1 has now also been screened out for C1C because the primary setup contains no Drunk.

Ancillary high-value evidence from G04:

- Nicole (Washerwoman) is shown Zach/Jordan -> Soldier;
- the primary video explicitly states Jordan the Spy is registering as Soldier for that interaction;
- this may be preserved as an observed historical registration witness rather than a downstream legality inference.

The G03/G04 pair is now exhausted for Drunk-assignment acquisition.

G05 `A Fond Farewell` has now passed primary review:

- complete role layout fixed before assignment;
- 03:32 — Chef selected as Drunk;
- explicit assignment rationale — support a deliberately extreme Chef misinformation narrative;
- no alternative Drunk candidates observed;
- 04:04 — Red Herring = Lyra;
- 04:47 — Demon bluffs;
- replay status: `PREFIX_RECONSTRUCTABLE`.

C1C quota is now **2 / 3 replayable assignments**, with **1 explicit historical assignment rationale**.

G06 `An Introduction to Blood on the Clocktower` has been rejected after primary review: it is an instructional/game-introduction video, not a recording of a real historical game. Do not use its illustrative lineup as corpus evidence.

Creator-guidance checkpoint complete:

- Cult of the Clocktower episode 16, 01:28:18–01:29:18, human-verified;
- Steven Medway confirmed as speaker;
- materially complete assignment guidance: player-first, role-first, whole-setup-first;
- classification: VERIFIED CREATOR-LEVEL ASSIGNMENT GUIDANCE / NOT_A_REPLAY_CASE.

Next action: continue targeted search for one new real Drunk-bearing primary game for replay case 3 / 3. Confirm “actual played game” status before spending time on setup chronology.

Do not enter C1D automatically; continue C1C until the replay package is sufficiently stable for downstream handoff.

### C1D — downstream replay handoff

Provide CampBoardGameHost one stable case containing:

- pre-assignment historical prefix;
- observed expert choice;
- provenance;
- source-backed rationale/alternatives where available.

CampBoardGameHost then derives legal candidates and runs the production Drunk-selection SDE.

Evidence Lab does not produce a winner/verdict.

### C1E — persistence only if justified

Only after C1A–D stabilise semantics should persistence/export expansion be considered.

## 8. C1 completion gate

C1 is complete when:

- generic setup-time DecisionSlice/domain boundary is stable;
- Drunk assignment is structurally separate from misinformation;
- hindsight leakage is prevented;
- Evidence Lab does not own legal candidate enumeration;
- existing Drunk corpus has been re-audited;
- at least 3 replayable assignment cases exist;
- explicit-rationale evidence is captured where available;
- one case crosses into CampBoardGameHost replay;
- authority docs remain synchronized.

Persistence is not itself required for C1 completion.

## 9. Historical handoff context

Everything below is retained for provenance/history. Dated live-status instructions below this point are superseded by the C1 sections above.

## 2.1 Final E0 state — 2026-09-22

Read the live pilot notebook before doing more reconstruction:

- `docs/E0_A_STUD_IN_SCARLET_EVIDENCE_CONTRACT_PILOT.md`
- `docs/E0_A_STUD_IN_SCARLET_PRIMARY_REVIEW_PACKET.md`

Completed:

- live repo/default branch/HEAD checked before work;
- all bootstrap files read;
- bootstrap consistency issue around prematurely frozen SQLite wording corrected;
- stable primary YouTube locator identified as video ID `qZBvRfM3Xow`;
- source record and bounded screening completed for E0 pilot scope;
- Ben qualification evidence sources recorded from official TPI material, still awaiting human verification status;
- prior D5F and public episode indexes demoted to locator-only leads rather than corpus facts;
- legacy D5F candidate code inspected directly and confirmed to be `PRIMARY_VERIFICATION_PENDING`;
- old D5F registration-witness statements identified as downstream rules projections, not primary historical observations.

New E0 model findings already recorded in the pilot notebook:

- secondary locator leads require a workflow state separate from corpus evidence;
- source-locator confirmation is not the same thing as primary-content verification;
- rules-derived compatible registration witnesses must never be imported as historical witness evidence;
- setup-time decisions such as Drunk shown identity need a committed-prefix boundary that is not limited to Night event sequence numbers;
- one short source fragment may support multiple distinct semantics: player action, Storyteller commitment, and information delivery.

The bounded primary-video pass is complete. Do not spend another round expanding this one case unless a later audit needs a specific missing locator.

Primary review 1 has now admitted three non-GOLD E0 DecisionSlices:

1. Drunk shown identity = Empath;
2. Red Herring = Sullivan;
3. Drunk-as-Empath Night-1 information = 0, with explicit rationale and rejected alternative 2.

The 15:18 Fortune Teller interaction is primary-verified as player targets Tom+Elliott plus delivered YES, but remains an output-event / DecisionSlice candidate because the historical registration witness and discretionary-choice basis are not primary-evidenced.

Final bounded primary-review state:

- Chef=1 verified at 11:53;
- Drunk-as-Empath=0 verified at 12:41 with explicit rationale and rejected alternative 2;
- Fortune Teller Tom+Elliott -> YES verified at 15:18;
- Recluse-as-Demon retained only as INFERRED reviewer interpretation; source-observed historical registration witness remains UNKNOWN;
- beginner/new-player game context verified at game level;
- optional screenshot/sub-timestamp precision may be added later but does not block E1.

Do not import the prior D5F phrase `Fortune Teller YES via Recluse-as-Demon` as a verified witness. The visible result and the historical registration witness are separate evidence questions.

## 2.2 E1 current implementation state

E1-1 is complete.

Frozen foundation:

- Python 3.12+;
- Pydantic v2;
- SQLite;
- SQLAlchemy 2.x Core;
- Alembic;
- pytest;
- Ruff;
- versioned JSON / JSONL.

Implemented:

- `pyproject.toml` and Python package skeleton;
- PR quality workflow;
- `SemanticId` validation with no database-row coupling;
- independent `Derivation` and `Verification` enums.

Tests-first evidence:

- the initial quality setup exposed packaging/lint prerequisites and they were corrected without weakening the test;
- the meaningful domain RED reached pytest with `ModuleNotFoundError` for the not-yet-implemented primitives;
- implementation then reached full GREEN: install, `ruff check .`, `ruff format --check .`, and `pytest` all passed.

E1-start architecture audit also tightened ownership:

- `Game.current_reconstruction_revision_id` is the sole current-revision owner;
- `VerificationRecord` owns verification transitions; current target verification is a projection;
- reconstruction-dependent assertions must carry revision identity;
- direct EvidenceFragment-to-event links do not replace assertion derivation/verification.

## 2.3 E1-2 provenance entities — COMPLETE

Implemented tests-first:

- `Source`;
- `EvidenceFragment`;
- `EvidenceAssertion`;
- source workflow enums;
- source locator kinds;
- reviewer inference provenance;
- explicit assertion scope.

Frozen E1-2 boundaries:

- Source owns stable identity/locator and collection-workflow state only.
- Source title/publisher/publication-date claims with derivation/verification use Source-subject EvidenceAssertions rather than duplicated Source fields.
- source timestamp/range is source-location evidence only, never historical semantic time.
- fragment/assertion provenance is N:M.
- reviewer inference stays INFERRED.
- Verification is not writable on EvidenceAssertion; VerificationRecord remains the future audit owner.
- assertion derivation and reconstruction-revision scope are independent dimensions.
- reconstruction-scoped assertions require a revision ID; evidence-scoped assertions cannot silently carry one.
- no legality, registration-witness enumeration, policy scoring, Game entity, DecisionSlice or UI was introduced.

Final E1-2 gate: install + Ruff check + Ruff format + pytest all GREEN.

## 2.4 E1-3 SQLite schema v1 — COMPLETE

Implemented tests-first:

- SQLAlchemy Core current metadata for the provenance core;
- Alembic environment and explicit initial migration;
- migration revision `0001_provenance_core`;
- migration determinism and metadata-equivalence tests.

Frozen E1-3 boundaries:

- semantic IDs are SQL primary keys; no database row ID is used as corpus identity;
- Alembic owns working-store migration position; there is no parallel mutable schema-version table;
- historical migration code explicitly creates v1 and does not delegate table creation to current metadata;
- Source evidentiary metadata remains assertion-owned rather than duplicated as source columns;
- source timestamps remain source-locator columns only;
- N:M assertion-fragment links preserve fragment order;
- assertion structured values use SQLite/SQLAlchemy JSON;
- assertion revision scope is persisted without a premature FK to ReconstructionRevision, which is not implemented yet;
- EvidenceAssertion has no verification column;
- Storyteller/Game/DecisionSlice tables remain absent.

Final E1-3 gate: migration from empty DB, deterministic schema comparison, migrated-vs-current metadata equality, Ruff and full pytest all GREEN.

## 2.5 E1-4 persistence round trip — COMPLETE

Implemented tests-first:

- application SQLite engine owner with foreign-key enforcement;
- append-only SQLAlchemy Core provenance store;
- Source insert/get;
- EvidenceFragment insert/get;
- EvidenceAssertion + ordered N:M provenance insert/get.

Frozen E1-4 boundaries:

- persistence adapters reconstruct domain models rather than returning SQL rows as the domain API;
- no update/delete/upsert behavior exists;
- assertion + fragment links are one transaction;
- foreign keys are actually enabled on application-owned SQLite connections;
- structured JSON and UNKNOWN survive round-trip;
- reviewer inference remains INFERRED with reviewer provenance;
- derivation and reconstruction scope remain independent;
- fragment ordering is preserved without treating that order as historical semantic event order.

Final E1-4 gate: install + Ruff check + Ruff format + full pytest all GREEN.

## 2.6 E1-5 versioned provenance interchange — COMPLETE

Implemented tests-first:

- versioned JSON bundle for Source / EvidenceFragment / EvidenceAssertion;
- explicit `schema_name` and schema version 1;
- deterministic canonical ordering by semantic IDs;
- strict Pydantic import validation;
- bundle-level Source → Fragment and Assertion → Fragment referential integrity.

Frozen E1-5 boundaries:

- durable export uses domain field names, not SQLite storage names such as `value_json` or link-table ordering columns;
- input collection order does not change canonical JSON output;
- assertion `fragment_ids` order remains durable provenance order;
- UNKNOWN and INFERRED remain distinct;
- reviewer inference provenance survives export/import;
- source timestamps remain source locator fields only;
- duplicate semantic IDs and orphan references are rejected;
- export contains only domain entities that actually exist; no placeholder Game/Storyteller/Decision rows were introduced.

Final E1-5 gate: install + Ruff check + Ruff format + full pytest all GREEN at `7cfd032e15986e0b3247cb39210600dc14856bbd`.

## 2.7 E1-6 reconstruction identity layer — COMPLETE

Implemented tests-first:

- `Storyteller`;
- `StorytellerAssignment`;
- `Game`;
- `GameSeat`;
- `ReconstructionRevision`;
- `ReconstructionStatus`.

Frozen E1-6 boundaries:

- Storyteller identity/independence is descriptive identity only; no qualification score is stored on Storyteller;
- qualification evidence remains ordinary Storyteller-subject EvidenceAssertions;
- GameSeat is game-scoped and has no global player ID;
- evidence-backed player experience may be retained as raw game-scoped metadata rather than guessed coarse labels;
- Game is the sole owner of `current_reconstruction_revision_id`;
- ReconstructionRevision has no writable current/superseded flag;
- revisions require timezone-aware creation time and cannot parent themselves;
- duplicate Storyteller assignments are rejected;
- cross-entity same-game referential checks are intentionally deferred to the persistence/bundle boundary where all referenced entities are available;
- no setup/event/decision/rules logic was introduced.

Final E1-6 gate: install + Ruff check + Ruff format + full pytest all GREEN at `0fc9f37c73be0374162cc1e7bdf2c9718f782be4`.

## 2.8 Next action — C0 Trouble Brewing evidence-acquisition sprint

C0 is now deliberately narrow.

The current Storyteller App supports **Trouble Brewing only**, so do not spend the next pass on other scripts or on estimating ClockTracker-wide corpus quality.

Primary objective:

~~~text
find enough high-value Trouble Brewing real games
    → reconstruct whole-game information bundles
    → improve/calibrate the current Storyteller recommendation algorithm
~~~

Current sprint target:

- roughly 20–30 usable public Trouble Brewing whole games;
- roughly 10–15 A-grade records if available;
- at least 2–3 independent Storytellers;
- several games with multi-night information evolution;
- 1–2 same-game ClockTracker + primary-video pairs.

Screen other scripts out immediately as current product-scope rejects.

Continue to grade Trouble Brewing records A/B/C, but use the grade only to control effort:

- A: reconstruct now;
- B: retain the strong mechanical backbone and enrich selectively when useful;
- C: normally stop unless a special external source makes the game unusually valuable.

Prioritize multi-clue interaction rather than isolated decisions. Especially useful TB bundles may include combinations of Chef, Empath, Fortune Teller, Investigator, Washerwoman, Drunk, Red Herring, Poisoner, Spy/Recluse registration, Demon bluffs and multi-night information changes.

Initial research status:

- public indexed ClockTracker pages expose a substantial Trouble Brewing candidate pool;
- one strong A-grade game is already confirmed: Scott/@sancho, Trouble Brewing, 2025-09-10, 14 players, public ClockTracker game `ffb40a93-3d7b-42c4-bba8-bc9c363dcd30`;
- its Notes reconstruct setup and Night/Day history through Night 7 and include Poisoner targets, Drunk information, Red Herring, Spy registration, Ravenkeeper/Undertaker/Fortune Teller information, executions, deaths and Imp transitions;
- several additional exact public Trouble Brewing game URLs have been discovered and are queued for screening;
- cross-source ClockTracker + matching primary-video validation remains pending.

Use `docs/C0_TROUBLE_BREWING_ACQUISITION_SPRINT_2026-09-23.md` as the active C0 research log.

The acquisition threshold has now been reached and formal reconstruction is active.

Read next:

- `docs/C0_TB_RECONSTRUCTION_BATCH_01_2026-09-23.md`;
- `docs/C0_TB_CROSS_GAME_ALGORITHM_FINDINGS_2026-09-23.md`.

The first reconstructed batch has exposed a blocking domain correction before persistence resumes:

1. many-to-one Source → logical Game linkage / duplicate-match state;
2. SetupCommitment;
3. ordered SemanticEvent / information-delivery history.

Do not resume the old E1-7 sequence unchanged.


## 2.9 C0-driven whole-game contract correction — COMPLETE

C0 exposed and has now corrected the minimum blocking domain gap.

Implemented tests-first in `src/clocktower_evidence_lab/domain/history.py`:

1. `SourceGameLink`
   - multiple Source records can refer to one logical Game;
   - match state is explicit: unresolved / candidate / verified-same / verified-different;
   - no silent UUID→Game identity collapse.

2. `SetupCommitment`
   - reconstruction-revision scoped;
   - deterministic setup order;
   - generic controller/subject/targets/value;
   - no TB-specific policy branching.

3. `SemanticEvent`
   - reconstruction-revision scoped;
   - deterministic global event order plus phase label;
   - generic actor/subject/targets/value;
   - UNKNOWN-friendly optional actor/value;
   - source locator timestamps are rejected as semantic historical time.

Test-first evidence:

- RED: `cd8c9fa3a4dbf38f8e8fabbae451b1641efe3247`;
- GREEN: `7c245da6692b2dd33cec2f8599a7dd96487abcb0`;
- GitHub Actions quality run #58: PASS.

### Immediate next action

Do **not** expand infrastructure by default.

The representative set is six reconstructed Trouble Brewing games and the first live product audit / cross-project handoff is complete.

Read next:

- `docs/C0_TB_STORYTELLER_APP_ALGORITHM_GAP_AUDIT_2026-09-23.md`;
- `docs/C0_TB_R04_REPLAY_PREPARATION_2026-09-23.md`;
- `docs/C0_TB_TARGETED_RATIONALE_SEARCH_2026-09-23.md`;
- `docs/C0_TB_TO_CAMPBOARDGAMEHOST_SDE_HANDOFF_2026-09-23.md`.

Live CampBoardGameHost recheck:

- PR #152 is MERGED;
- `main` observed at `2a9051f1b0282bd25d01d46d36fe797857cc429d`;
- PR #153 `SDE-3B: implement BEGINNER_CONSERVATIVE_V1 policy` is OPEN / DRAFT.

PR #153 already handles the two most important Evidence Lab warnings correctly:

- unavailable features remain explicit limitations/deferrals rather than neutral/zero evidence;
- no unsupported numeric soft thresholds are introduced; non-zero survivors remain equivalent until richer projectors exist.

Therefore do not interrupt SDE-3B with a redesign request.

R04 replay preparation is `REPLAY_PREP_PARTIAL / BLOCKED_ON_DIRECT_GRIMOIRE`; the remaining seat/role/shown-role fields could not be recovered from the current search/API/mirror access path. Do not repeat broad searches for those same fields unless a new direct-source access path appears.

Next Evidence Lab work should occur only when it closes a concrete gap:

1. a new direct ClockTracker/grimoire access path becomes available → close R04 replay blockers;
2. a qualified Storyteller source contains explicit rationale for healthy-information strength, persistent impaired narrative, role exposure or bluff triplets → capture it;
3. a new TB whole game adds a genuinely missing evidence shape → reconstruct it.

Do not expand raw corpus count for its own sake.

Persistence remains deferred until replay preparation is materially blocked by lack of durable storage.

If/when persistence is required, implement tests-first for:

- Storyteller / Game / StorytellerAssignment / GameSeat / ReconstructionRevision;
- SourceGameLink;
- SetupCommitment;
- SemanticEvent.

Preserve:

- Game as the sole current-revision owner;
- append-only persistence style;
- semantic IDs as corpus identity;
- UNKNOWN / INFERRED distinction;
- no BotC legality or recommendation scoring.

DecisionSlice / VerificationRecord remain deferred until the historical whole-game model round-trips cleanly.

## 3. First pilot case

Preferred case:

**Ben Burns — `A Stud In Scarlet`**

Existing CampBoardGameHost research indicates this case is promising because it contains a reconstructable first-night bundle involving Drunk information, Fortune Teller/Recluse interaction and Chef information.

Do not trust prior secondary reconstruction as final truth.

Primary-video verification is required.

## 4. E0 procedure

### Step 1 — source record

Capture:

- stable source ID;
- title;
- URL/platform ID;
- Storyteller;
- script;
- publication/date metadata when known;
- source fidelity;
- discovery/inclusion reason.

### Step 2 — screening

Determine:

- setup recoverability;
- Night-1 visibility;
- grimoire visibility;
- rationale availability;
- editing gaps;
- likely reconstructable phases.

### Step 3 — primary evidence extraction

Use primary-video timestamps.

Record only concise paraphrases/minimal quotes.

Do not copy long transcripts.

### Step 4 — reconstruction

Reconstruct only what evidence supports.

UNKNOWN is preferred over guesswork.

Produce:

- seating/setup commitments;
- shown-role facts;
- Demon bluffs / Red Herring / other setup commitments when established;
- player-controlled Night-1 actions;
- ordered semantic events;
- Storyteller-controlled outputs.

### Step 5 — decision slices

Extract at least three useful Storyteller decisions.

For each:

- decision type;
- boundary event sequence;
- observed choice;
- source evidence;
- derivation;
- verification;
- optional explicit rationale;
- optional explicitly rejected alternatives.

Do not enumerate legal alternatives in Evidence Lab.

### Step 6 — verification pass

Re-check:

- timestamps;
- seats/roles;
- event order;
- observed vs inferred distinctions;
- decision boundaries;
- unresolved ambiguities.

### Step 7 — model audit

Before coding a generic application, list:

- fields that were actually needed;
- fields that were impossible to obtain;
- repeated manual work;
- ambiguous concepts;
- schema assumptions that failed.

### Step 8 — E1 proposal

Only after the pilot, freeze:

- first persisted schema;
- first exact repository layout;
- implementation language/framework;
- exact test commands;
- migration tooling.

## 5. Hard stop conditions

Stop and report rather than inventing data if:

- primary evidence cannot establish a material fact;
- decision timing cannot be bounded;
- multiple historical interpretations remain plausible;
- a registration witness is not evidenced;
- prior secondary notes conflict with the primary source.

Ambiguity is useful data.

## 6. E0 success condition

The pilot is complete when one real expert primary-source game yields a small set of fully traceable decision slices and exposes enough real workflow pressure to justify the E1 persisted schema.

The goal is not to prove any D5F policy hypothesis.

The goal is to prove that the Evidence Lab can create trustworthy evidence.
