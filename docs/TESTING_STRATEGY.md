# Testing Strategy

## 1. Goal

Protect evidence integrity and migration stability with fast, durable tests.

The most expensive defect in this project is not a UI bug. It is silently changing the meaning or provenance of historical evidence.

## 2. Priority test surfaces

### Tier 0 — domain invariants

Fast focused tests for:

- evidence derivation/verification enums;
- stable IDs;
- event ordering;
- decision boundary rules;
- source/evidence references;
- unknown preservation;
- reconstruction revision behavior.

### Tier 1 — persistence and serialization

- working-store repository round trips once the E1 store is selected;
- JSON/JSONL export/import round trips once the first durable export contract is frozen;
- schema version presence;
- migration determinism;
- no lossy conversion of provenance fields.

### Tier 2 — workflow integration

- create source;
- screen source;
- create game;
- add assertions/events;
- create decision slice;
- verify;
- export;
- re-import equivalent evidence.

### Tier 3 — real pilot corpus regression

A very small curated public pilot corpus may exercise end-to-end reconstruction semantics.

It must not become fixture-specific production logic.

## 3. Required invariants

At minimum, tests should eventually prove:

1. A decision boundary cannot refer to an event after the decision.
2. Later events are not included in exported decision prefixes.
3. `UNKNOWN` survives persistence and export.
4. `INFERRED` cannot silently become `OBSERVED`.
5. Verification status is preserved independently of derivation.
6. Raw evidence survives reconstruction revision unchanged.
7. A reconstruction revision is auditable.
8. Event order is deterministic.
9. Every material verified assertion has valid provenance.
10. GOLD qualification is derived from explicit evidence dimensions rather than free-form manual labeling.
11. Export/import preserves stable semantic IDs.
12. Working database row IDs are not required by the durable export contract.

## 4. Test-first policy

For a new stable invariant:

```text
define invariant
→ focused RED
→ implementation
→ focused GREEN
→ affected integration
```

For a behavior-preserving refactor, existing tests are valid test-first evidence.

Do not add brittle tests that assert internal source shape.

## 5. Migration policy

Persistence/schema changes are high-risk.

Every migration must have tests that cover:

- old-version input;
- migrated output;
- preservation of provenance and UNKNOWN values;
- deterministic repeated migration;
- export compatibility.

Do not silently rewrite old corpus files in place without an auditable migration path.

## 6. UI testing

UI tests are secondary to domain/storage integrity.

Test UI behavior only where it protects a real workflow contract, such as:

- user can leave a field UNKNOWN;
- evidence can be linked to a timestamp;
- verification does not overwrite derivation;
- partial reconstruction can be saved.

Do not make the domain model depend on a UI framework for testability.

## 7. Exact commands

E1 uses Python 3.12+ with the following local quality gate:

```bash
python -m pip install -e ".[dev]"
ruff check .
ruff format --check .
pytest
```

GitHub Actions runs the same lint/format/test gate for pull requests to `main` and after pushes to `main`.

A change that has not reached pytest because installation or linting failed is not a GREEN domain test result.
