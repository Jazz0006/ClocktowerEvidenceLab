# NEXT DEVELOPMENT HANDOFF — E0 Evidence Contract Pilot

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

Bootstrap consistency review is complete and E0 is active on working branch `e0-evidence-contract-pilot`.

No application implementation is authorized yet beyond what is needed to perform and document the E0 pilot.

The first objective is to validate the evidence/reconstruction contract against one real expert primary source.

## 2.1 Current E0 progress — 2026-09-21

Read the live pilot notebook before doing more reconstruction:

- `docs/E0_A_STUD_IN_SCARLET_EVIDENCE_CONTRACT_PILOT.md`
- `docs/E0_A_STUD_IN_SCARLET_PRIMARY_REVIEW_PACKET.md`

Completed:

- live repo/default branch/HEAD checked before work;
- all bootstrap files read;
- bootstrap consistency issue around prematurely frozen SQLite wording corrected;
- stable primary YouTube locator identified as video ID `qZBvRfM3Xow`;
- source record and screening started;
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

The next action is now bounded: perform one direct primary-video pass using `docs/E0_A_STUD_IN_SCARLET_PRIMARY_REVIEW_PACKET.md`. Do not spend another round expanding secondary-source search unless the primary review exposes a specific missing locator.

Still required before E0 can admit a decision slice:

- direct/manual primary playback (or an equivalent primary caption path) to recover in-video timestamps for setup and Night 1;
- primary confirmation of setup/seating/shown identity;
- ordered player-action vs Storyteller-output boundaries;
- human verification pass after the timestamped primary extraction;
- explicit confirmation or UNKNOWN treatment of registration witness;
- explicit rationale/rejected alternatives only where the primary source truly contains them.

Do not import the prior D5F phrase `Fortune Teller YES via Recluse-as-Demon` as a verified witness. The visible result and the historical registration witness are separate evidence questions.

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
