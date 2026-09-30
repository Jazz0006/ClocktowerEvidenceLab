# Trouble Brewing Game Snapshot Interoperability Route — 2026-09-30

> Date: 2026-09-30 Australia/Sydney  
> Repository: `Jazz0006/ClocktowerEvidenceLab`  
> Status: **EL-TBGS-0/1 IMPLEMENTED / LOCAL GREEN / TB ONLY**  
> Upstream semantic contract owner: `Jazz0006/CampBoardGameHost` TBGS-0 / `TroubleBrewingGameSnapshotV1`  
> Scope: derive a standard Trouble Brewing decision-time game snapshot from EvidenceLab historical prefixes without changing EvidenceLab's event-sourced authority or adding BotC legality/policy.

## 1. Decision

EvidenceLab will support the same **domain semantics** as CampBoardGameHost's `TroubleBrewingGameSnapshotV1`, but it will not reuse Host runtime ownership or become a second game engine.

The EvidenceLab path is:

```text
Evidence assertions
    -> reconstruction revision
    -> SetupCommitment + SemanticEvent history
    -> DecisionSlice historical prefix
    -> pure TB snapshot materializer
    -> TroubleBrewingGameSnapshotV1-compatible interchange
```

The authoritative historical record remains setup commitments + semantic events + provenance. The snapshot is a disposable/versioned materialized view.

## 2. Why this belongs in EvidenceLab

The same decision-time state should be consumable from two origins:

```text
live Host canonical owners
        -> TB snapshot

historical EvidenceLab prefix
        -> TB snapshot
```

Downstream Host rules/recommendation code can then consume a stable semantic object without special-case mapping for every real-game fixture.

This makes expert decisions and algorithm recommendations comparable at the same historical boundary while preserving the rule that the observed expert choice is evidence rather than an oracle.

## 3. State-value semantics

The interoperability contract must distinguish:

```text
KNOWN(value)
UNCOMMITTED
UNKNOWN
NOT_APPLICABLE
```

EvidenceLab interpretation:

- `KNOWN(value)`: the historical prefix establishes the value strongly enough for the snapshot projection;
- `UNCOMMITTED`: at this decision boundary, the historical choice that would create this value has not happened yet;
- `UNKNOWN`: the value is historically relevant/existing but the evidence/reconstruction cannot establish it;
- `NOT_APPLICABLE`: the field does not apply.

This semantic state is separate from EvidenceLab provenance axes:

```text
derivation: OBSERVED / RECONSTRUCTED / INFERRED / UNKNOWN / NOT_APPLICABLE
verification: UNVERIFIED / VERIFIED / DISPUTED
```

Do not collapse provenance/verification into snapshot state.

## 4. Authority boundary

EvidenceLab continues to own:

- source/provenance;
- evidence assertions;
- reconstruction revision;
- setup/event chronology;
- decision boundaries;
- observed expert choices/rationale/explicit alternatives;
- uncertainty and verification.

CampBoardGameHost continues to own:

- BotC legality;
- legal candidate enumeration;
- role/rules interpretation needed to derive candidate domains;
- recommendation features/policy;
- production state transitions.

The snapshot materializer may project evidence-backed historical facts. It must not call or copy Host legality rules to fill gaps.

## 5. TB-only V1 scope

Do not generalize to other scripts now.

The first EvidenceLab implementation should support only the bounded fields required by the first Host TBGS vertical slice, expected to include:

- snapshot stage / decision boundary identity;
- stable seats;
- shown role by seat;
- actual role state where historically committed;
- Drunk-presence state;
- Drunk-assignment state;
- the minimal history prefix required by the Drunk decision fixture.

Red Herring, Demon bluffs, poison/protection/runtime state and broader information history should be added only when a real TB decision consumer requires them.

## 6. First cross-project golden fixture

Use the already accepted G10 Game 2 Drunk-assignment case.

At the historical boundary immediately before the Drunk choice:

- complete shown-seat layout is known;
- the setup requires a Drunk;
- the actual Drunk seat is `UNCOMMITTED`;
- later Drunk result, Red Herring, Demon bluffs and first-night information are outside the prefix.

Expected flow:

```text
G10 reconstruction revision
    + DRUNK_ASSIGNMENT DecisionSlice prefix
        -> EvidenceLab TB snapshot materializer
        -> V1 snapshot interchange
        -> CampBoardGameHost importer/fixture
        -> Host independently derives legal Drunk candidates
        -> historical selected Empath maps into that domain
```

The historical selected candidate and rationale remain separate from the snapshot.

## 7. Storage and export policy

Do **not** add a persistence migration merely for this route.

Initial implementation should be a pure projection over existing domain models and may emit a versioned JSON fixture/export.

The durable interchange contract should be versioned independently from the SQLite schema.

Possible conceptual artifact:

```text
tb_game_snapshot_v1.json
decision.json
provenance references
```

The snapshot itself must not embed source timestamps, evidence assertion IDs or verification records unless a separate EvidenceLab wrapper explicitly carries them.

## 8. Relationship to C2 and C3

This route must not stop or replace current acquisition.

```text
C2 podcast batch ingestion                 continues
C3 Drunk comparison/rejection acquisition continues
TB snapshot interoperability               proceeds as a narrow parallel architecture lane
```

Host TBGS-0 is now COMPLETE / ACCEPTED. EvidenceLab has implemented the matching pure materializer, deterministic V1 codec, and G10 golden fixture. C2/C3 continue independently.

C3 Stage-1 remains an evidence gate for production Drunk ordering semantics. A working snapshot interchange does not authorize a recommendation preference.

## 9. Implementation sequence

```text
Host TBGS-0 contract frozen                         COMPLETE / ACCEPTED
-> EL-TBGS-0 mapping audit                         COMPLETE
-> EL-TBGS-1 pure materializer + V1 serialization COMPLETE / LOCAL GREEN
-> G10 pre-Drunk golden fixture                    COMPLETE / byte-for-byte Host match
-> Host TBGS-1 cross-project consumption           NEXT HOST COORDINATION POINT
-> use the same snapshot projection for future C3 handoffs where enough prefix data exists
```

Implementation/audit record: `docs/EL_TBGS_0_1_MAPPING_AND_IMPLEMENTATION_AUDIT_2026-09-30.md`.

Do not block C2D/C2E human review while waiting for this sequence.

## 10. Acceptance criteria

The first EvidenceLab snapshot slice is accepted when:

1. it derives only from one reconstruction revision and the selected historical prefix;
2. no resulting decision or later event leaks backward;
3. `UNCOMMITTED` and `UNKNOWN` are independently testable;
4. provenance remains outside the snapshot and remains recoverable from the authoritative evidence record;
5. deterministic serialization round-trips;
6. the G10 fixture matches the Host TBGS-0 semantic contract;
7. Host can derive legal alternatives independently;
8. no recommendation score, legality enumeration or policy verdict is added to EvidenceLab;
9. no database migration is required for the first slice.

## 11. Non-goals

Do not:

- replace SetupCommitment/SemanticEvent event sourcing with snapshots;
- make snapshots a second canonical history store;
- copy Host rules into EvidenceLab;
- encode legal Drunk candidates in historical evidence;
- infer unknown actual roles solely to satisfy the snapshot;
- put expert observed choice into the pre-decision snapshot;
- generalize to Sects & Violets / Bad Moon Rising;
- redesign C2/C3 acquisition around the snapshot;
- create a broad universal GameState abstraction before the TB fixture proves the contract.
