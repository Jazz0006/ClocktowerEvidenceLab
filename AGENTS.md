# Clocktower Evidence Lab — AI Development Instructions

> Role: **NORMATIVE PROJECT-LEVEL WORKING AGREEMENT**
>
> Applies to ChatGPT, Codex and other implementation agents working on this repository.

## 1. Mission

Build a durable evidence system for reconstructing real Blood on the Clocktower games and Storyteller decisions from external sources.

The primary product is trustworthy evidence, not an evaluator.

The system must preserve enough historical context that another program can later reconstruct what was known and committed at the time of a Storyteller decision without leaking later events backward.

## 2. Authority boundaries

### Evidence Lab owns

- source inventory;
- source screening and inclusion/rejection metadata;
- raw evidence references;
- evidence assertions;
- reconstructed game facts and semantic timeline;
- decision boundaries;
- verification/provenance;
- corpus schema and migration;
- import/export.

### Evidence Lab does **not** own

- Blood on the Clocktower legality;
- legal alternative enumeration;
- exact world solving;
- strategic topology scoring;
- Storyteller policy scoring;
- labels such as GOOD/BAD;
- conclusions that an unchosen alternative was bad.

Those belong to downstream consumers such as CampBoardGameHost.

Do not copy production rules from CampBoardGameHost into this project merely to make a reconstruction convenient.

## 3. Evidence invariants

These are hard invariants.

### 3.1 Facts, reconstructions and inference are distinct

Never silently convert an inference into an observation.

Evidence derivation and verification are separate dimensions.

At minimum support:

```text
derivation:
    OBSERVED
    RECONSTRUCTED
    INFERRED
    UNKNOWN
    NOT_APPLICABLE

verification:
    UNVERIFIED
    VERIFIED
    DISPUTED
```

`UNKNOWN` is a valid durable value and is preferred over guessing.

### 3.2 Provenance is field/event level

Whole-game confidence is insufficient.

Material reconstructed facts and events must be traceable to source evidence, normally including a source identifier and timestamp/range for video evidence.

### 3.3 Raw evidence is immutable

Source records and raw evidence references are append-only except for explicit metadata correction with history.

A later algorithm, reconstruction revision or policy interpretation must not rewrite what the primary source was.

### 3.4 Reconstruction is versioned

Canonical reconstruction means “the current best evidence-backed reconstruction,” not infallible historical truth.

Corrections create a new reconstruction revision or auditable migration. Never erase uncertainty or provenance.

### 3.5 Decision-time prefix is first-class

A Storyteller decision must identify its boundary in the event sequence.

Downstream analysis must be able to reconstruct only the prefix that was committed when the decision occurred.

Later Storyteller choices and later game outcomes must not be frozen into earlier counterfactual analysis.

### 3.6 Player-controlled and Storyteller-controlled choices are distinct

Examples:

- Poisoner target: player-controlled.
- Fortune Teller chosen pair: player-controlled.
- Storyteller information result when controllable: Storyteller-controlled.
- Demon bluffs / Red Herring: Storyteller-controlled setup commitments.

Ownership matters because committed player choices must remain fixed during later counterfactual reconstruction.

### 3.7 Registration witness is never fabricated

If the source explicitly establishes an interaction-local Spy/Recluse registration, record it as observed/reconstructed as appropriate.

If only the visible result is known and several legal witnesses could explain it, the registration witness remains `UNKNOWN`.

A downstream rules engine may later derive the compatible witness set.

### 3.8 Expert choice is evidence, not a label

`expert chose A` does not imply `B/C/D bad`.

Final winner is historical metadata, not a Storyteller-decision-quality label.

Explicit rationale, explicit rejected alternatives, repeated comparable choices and independent Storytellers are stronger evidence than a silent observed choice.

### 3.9 GOLD is decision-level and derived

Do not hand-author a single opaque `gold=true` fact as the primary evidence model.

GOLD qualification should be derivable from independent dimensions such as:

- Storyteller qualification;
- source fidelity;
- decision-prefix completeness;
- observed-choice verification;
- reconstruction completeness.

A game may contain GOLD-qualified decisions while later phases remain partial or unknown.

### 3.10 Real corpus and regression fixtures are separate assets

Production or analysis code must never branch on a known corpus case ID, exact seating, named video or calibration fixture.

A regression fixture may be copied/projected from real evidence, but the real corpus itself is not production logic.

### 3.11 Whole-game context is the primary collection unit

The acquisition target is a reconstructable real game, not an isolated clue or isolated Storyteller choice.

Preserve enough setup, ordered information, player-controlled actions, Storyteller-controlled outputs, state changes and outcome context to study how multiple clues interact across the game.

Decision slices are derived analytical views over the reconstructed game history. Do not optimize source collection around single decisions when the surrounding game can be preserved.

## 4. Source and copyright policy

For public video/audio sources:

- store URL/platform/source ID;
- store timestamps or timestamp ranges;
- store concise factual paraphrases;
- store only minimal quotation where evidentially necessary;
- do not archive or commit full copyrighted video/audio;
- do not commit long transcript reproductions.

Initial scope is public external material. Private/community-submitted material requires an explicit privacy/consent design before ingestion.

## 5. Storyteller and player identity

Retain a stable Storyteller identity / independence key when public identity is relevant to expert-evidence aggregation.

Do not build unnecessary persistent personal profiles for ordinary players.

Prefer game-scoped player/seat identity. Player experience should be represented as evidence-backed metadata or ranges, not guessed categorical labels.

## 6. Selection-bias control

Every source/game admitted to or rejected from the collection workflow must preserve an inclusion path or rejection reason when practical.

Recommended inclusion reasons include:

```text
EXPERT_SOURCE_CENSUS
SYSTEMATIC_SAMPLE
RANDOM_SAMPLE
TARGETED_RESEARCH_CASE
COMMUNITY_SUBMISSION
ALGORITHM_FAILURE_REPORT
OTHER
```

Do not retain only spectacular games, unusual games or algorithm failures and later treat the collection as representative.

## 7. Software-engineering rules

### 7.1 Architecture before UI

The durable domain model and export contract are more important than a first UI framework.

Do not couple canonical evidence semantics to widget names, screen routes, database row IDs or one platform.

### 7.2 Stable semantic IDs

Use stable semantic identifiers in persisted/exported data.

Do not persist language enum ordinals, UI indexes or implementation-specific object names as long-lived identities.

### 7.3 Schema versioning from the first persisted record

Every durable export must carry a schema version.

Migrations must be deterministic and auditable.

Never require “current code happens to understand an old file” as the migration strategy.

### 7.4 Event history is authoritative; snapshots are derived

The canonical historical model is an ordered semantic event stream plus setup commitments and provenance.

Snapshots/checkpoints may be materialized for speed, but must be reproducible from the authoritative record.

### 7.5 No speculative generality without evidence

The model must support complete games and later-night decisions, but do not implement broad abstractions merely because a future script might theoretically need them.

Add semantic generality when the evidence model requires it; do not create role-specific policy hacks.

### 7.6 Unknown-friendly APIs

APIs, schemas and UI must make `UNKNOWN` easy to represent.

A workflow that pressures the reviewer to guess is a data-quality defect.

## 8. Development process

Use evidence-first, test-first development at durable boundaries.

For new stable behavior:

```text
define invariant
→ smallest durable test
→ meaningful RED where applicable
→ implementation
→ GREEN
→ broader affected validation
→ exact diff review
```

For pure refactors:

```text
identify existing owning tests
→ establish baseline
→ refactor
→ rerun affected tests
→ exact diff review
```

Do not manufacture failing tests for mechanical edits.

## 9. Testing priorities

Highest-value early tests include:

- schema serialization round trip;
- migration determinism;
- event ordering;
- decision boundary cannot reference future events;
- source/evidence referential integrity;
- observed vs inferred status preservation;
- unknown preservation;
- reconstruction revisions do not rewrite raw evidence;
- export/import equivalence;
- GOLD qualification derivation from independent fields;
- fixture/corpus separation.

See `docs/TESTING_STRATEGY.md`.

## 10. Change discipline

Until the first pilot reconstruction is complete:

- do not build recommendation logic;
- do not implement Blood on the Clocktower legality;
- do not optimize for large-corpus scale;
- do not create cloud/backend infrastructure;
- do not build AI auto-judgment of Storyteller quality;
- do not ingest large volumes before the reconstruction workflow is validated.

The first implementation target is a reliable path from one real primary source to a verified decision slice.
