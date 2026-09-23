# NEXT DEVELOPMENT HANDOFF — E1 Domain / Persistence Foundation

## 1. Read first

Read in this order:

1. `AGENTS.md`
2. `README.md`
3. `docs/ARCHITECTURE.md`
4. `docs/EVIDENCE_AND_PROVENANCE_STANDARD.md`
5. `docs/SOURCE_COLLECTION_STRATEGY.md`
6. `docs/TESTING_STRATEGY.md`
7. `docs/CURRENT_DEVELOPMENT_ROADMAP.md`
8. this file

Also consult the relevant CampBoardGameHost D5F evidence documents only as research context. Do not copy its rules engine or policy implementation into this repository.

## 2. Current state

Bootstrap consistency review and the E0 evidence-contract pilot are complete and merged to `main`.

PR `#1` — `E0: evidence contract pilot — A Stud In Scarlet` — was squash-merged to `main` on 2026-09-22.

Merged `main` commit: `6a672a9dc6b7fa13f98aef8a7e6b1e616889d667`.

Current E1 working branch: `e1-domain-persistence-foundation`.

Draft PR: `#2` — `E1: domain and persistence foundation`.

Keep PR #2 draft during E1 implementation.

E1 implementation is active on `e1-domain-persistence-foundation`; do not reopen the merged E0 branch for implementation work.

E1-1 code/quality gate head: `95e933c87e694e9d11552a5f7aad8749ed3f3d72`.

E1-2 domain gate head: `ad8174e971d598b4ebc8f72287010c4dd99b689e`.

E1-3 migration gate head: `b643cd051942992b04bf7f36b0cb5ba82832cca4`.

E1-4 persistence gate head: `0d11e4c480754ba70d3965740c4de01238cab7ac`.

E1-5 interchange gate head: `7cfd032e15986e0b3247cb39210600dc14856bbd`.

E1-6 reconstruction identity domain gate head: `0fc9f37c73be0374162cc1e7bdf2c9718f782be4`.

PR #2 remains draft.

Read these two completion artifacts before starting E1:

- `docs/E0_EVIDENCE_CONTRACT_COMPLETION_AUDIT_2026-09-22.md`
- `docs/E1_DOMAIN_PERSISTENCE_PROPOSAL_2026-09-22.md`

## 2.0 Final PR consistency audit — 2026-09-22

Final audit result: **PASS**.

- PR #1 remains draft;
- branch is based cleanly on `main` with no behind commits at the audit point;
- changed files are documentation only;
- no application code, schema, database, UI or rules engine was introduced;
- E0 completion state is consistent across roadmap, pilot, completion audit and handoff;
- Chef=`1` is consistently recorded as a verified delivery event;
- Fortune Teller Recluse-as-Demon remains INFERRED reviewer interpretation while source-observed historical witness stays UNKNOWN;
- E1 proposal now includes stable Storyteller identity, game-scoped `GameSeat`, `ReconstructionRevision`, revision-scoped reconstructed entities and source screening/selection dimensions;
- Storyteller qualification uses the canonical `EvidenceAssertion` path rather than a parallel evidence subsystem;
- no GitHub Actions workflow/check is configured yet for this docs-only bootstrap stage.

When merge is explicitly authorized, prefer **squash merge** because the E0 branch contains many small documentation/audit commits that represent one semantic milestone.

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
