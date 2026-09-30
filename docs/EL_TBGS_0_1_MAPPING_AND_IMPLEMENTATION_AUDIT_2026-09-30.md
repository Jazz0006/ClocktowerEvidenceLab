# EL-TBGS-0/1 — Trouble Brewing Snapshot Mapping + G10 Interoperability Audit — 2026-09-30

> Status: **IMPLEMENTATION COMPLETE / LOCAL GREEN**
>
> Repository: `Jazz0006/ClocktowerEvidenceLab`
>
> Host authority: `Jazz0006/CampBoardGameHost` TBGS-0, accepted checkpoint `f367c0d3ec23ebf452c924ff7c0921cd978a800f`
>
> Scope: Trouble Brewing only; Drunk-assignment setup-precommit vertical slice only.

## 1. Result

EvidenceLab now implements the Host TBGS-0 V1 semantic contract without changing its event-sourced authority, persistence schema, acquisition logic, or BotC legality boundary.

Implemented path:

```text
Game + GameSeat
+ DecisionSlice
+ SetupCommitment / SemanticEvent history
+ non-evidence projection metadata
        |
        | materialize_historical_prefix()
        v
TroubleBrewingGameSnapshotV1
        |
        | deterministic compact JSON
        v
Host-compatible botc.tb.game-snapshot / schemaVersion=1
```

The first cross-project fixture is G10 Game 2 immediately before Drunk assignment.

## 2. Host V1 contract consumed

Host TBGS-0 freezes:

- `schemaId = "botc.tb.game-snapshot"`;
- `schemaVersion = 1`;
- `script = "trouble_brewing"`;
- four-state fields: `KNOWN / UNCOMMITTED / UNKNOWN / NOT_APPLICABLE`;
- position;
- ordered grimoire seats;
- shown/actual role state;
- alive/poisoned state;
- `hasDrunk`;
- `drunkAssignmentSeat`;
- deterministic JSON ordering.

EvidenceLab mirrors these semantics in `domain/tb_snapshot.py` and `interchange/tb_game_snapshot_v1.py`.

## 3. Mapping audit

| Host snapshot field | EvidenceLab source at G10 precommit | Mapping |
| --- | --- | --- |
| schema ID/version | V1 contract | constant |
| gameId | `Game.game_id` | direct |
| script | `Game.script` | must normalize to `trouble_brewing` |
| gameSeed | not a historical EvidenceLab fact | explicit projection metadata |
| stage | decision type + setup prefix | `SETUP_PRECOMMIT` |
| phase/round | not applicable before runtime | `NOT_APPLICABLE` |
| revisions | Host runtime freshness fields, absent historically | `NOT_APPLICABLE` |
| seat number | `GameSeat.seat_order` | direct, contiguous validation |
| shown role | `SHOWN_ROLE_LAYOUT` setup commitment | normalized external role ID |
| actual role | prefix + Drunk lifecycle semantics + supplied role type metadata | Townsfolk `UNCOMMITTED` when `hasDrunk=true`; other shown identities `KNOWN` |
| alive | setup-precommit semantic baseline | `KNOWN(true)` |
| poisoned | setup-precommit semantic baseline | `KNOWN(false)` |
| hasDrunk | explicit `SHOWN_ROLE_LAYOUT.value.has_drunk` | `KNOWN/UNKNOWN` |
| drunkAssignmentSeat | hasDrunk + decision boundary | `UNCOMMITTED / UNKNOWN / NOT_APPLICABLE` |

## 4. Important boundary findings

### 4.1 gameSeed is interchange/replay metadata, not historical evidence

The Host V1 schema requires `gameSeed: Long`, but a real external game normally does not expose the Host RNG seed.

EvidenceLab therefore does **not** create an EvidenceAssertion for it.

The materializer receives `TroubleBrewingSnapshotProjectionMetadata.game_seed` explicitly. For the shared G10 fixture this is `20260929`, matching the accepted Host golden fixture.

This value must not be interpreted as a reconstructed fact about the real game.

### 4.2 Role type metadata is projection metadata, not EvidenceLab legality

To match Host setup-precommit semantics, the projector must know whether a shown role is Townsfolk. That classification determines whether its actual role is still `UNCOMMITTED` while the Drunk seat is unresolved.

EvidenceLab deliberately does not hard-code or derive legal Drunk candidates.

Instead, `TroubleBrewingSnapshotProjectionMetadata.role_types_by_external_id` supplies static role-type metadata to the pure projector. Missing metadata fails closed.

This preserves:

```text
EvidenceLab: historical facts + projection
Host: legality + legal candidate enumeration + recommendation policy
```

### 4.3 hasDrunk must come from the historical prefix

The materializer requires `has_drunk` to be explicit in the pre-decision shown-layout projection.

It refuses to backfill `hasDrunk=true` merely because the resulting later history contains `DRUNK_ASSIGNMENT`.

That prevents future history from leaking backward.

## 5. G10 golden equivalence

The EvidenceLab G10 fixture uses the same semantic state as the Host TBGS-0 fixture:

```text
seat 1  Empath       actual UNCOMMITTED
seat 2  Imp          actual KNOWN Imp
seat 3  Undertaker   actual UNCOMMITTED
seat 4  Librarian    actual UNCOMMITTED
seat 5  Spy          actual KNOWN Spy
seat 6  Monk         actual UNCOMMITTED
seat 7  Mayor        actual UNCOMMITTED
seat 8  Virgin       actual UNCOMMITTED
seat 9  Butler       actual KNOWN Butler

hasDrunk            KNOWN(true)
drunkAssignmentSeat UNCOMMITTED
```

The later historical choice (seat 1 Empath -> Drunk), Red Herring and first-night information exist in test history but are excluded by the DecisionSlice prefix.

The test compares EvidenceLab serialization directly with the Host golden JSON string.

## 6. Files

Implementation:

- `src/clocktower_evidence_lab/domain/tb_snapshot.py`;
- `src/clocktower_evidence_lab/domain/tb_snapshot_materializer.py`;
- `src/clocktower_evidence_lab/interchange/tb_game_snapshot_v1.py`.

Contract tests / fixture:

- `tests/domain/test_tb_snapshot_materializer.py`;
- `tests/domain/g10-game2-precommit-tbgs-v1.json`.

No Alembic migration or SQLite schema change is required.

## 7. Validation

Local validation after implementation:

- `ruff-check`: PASS;
- `ruff-format-check`: PASS — 89 files already formatted;
- `quality`: PASS;
- pytest: PASS — 127 tests;
- Host G10 golden JSON byte-for-byte equality: PASS;
- V1 JSON round-trip: PASS;
- `UNCOMMITTED` vs `UNKNOWN`: independently tested;
- future-result backfill protection: tested;
- missing projection role metadata fails closed: tested.

## 8. Next cross-project step

EvidenceLab's required side of the first TBGS interoperability seam is now implemented.

Next coordination:

```text
EvidenceLab G10 V1 fixture GREEN
        |
        v
Host TBGS-1 Drunk vertical slice
        |
        +-> consume/compare the same V1 semantics
        +-> independently derive legal Drunk candidates
        +-> map historical Empath choice into legal domain
```

C2/C3 acquisition continues independently.

Future C3 handoffs may include the V1 snapshot when their historical prefix is sufficiently reconstructed, but snapshot availability must not become a prerequisite for promoting otherwise valid evidence.

## 9. Deferred

Do not yet implement:

- committed/runtime snapshot materializers unless a current EvidenceLab consumer needs them;
- Red Herring or Demon-bluff snapshot fields beyond Host V1;
- generalized cross-script snapshots;
- database persistence for snapshots;
- Host legality/candidate enumeration;
- recommendation scoring/policy.
