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
13. A setup-time decision prefix cannot contain its own resulting setup commitment.
14. Later setup commitments and later semantic events cannot leak backward into an earlier decision prefix.
15. Explicitly observed considered/rejected alternatives remain distinct from downstream-derived legal alternatives.
16. UNKNOWN setup-choice rationale and alternatives survive domain/persistence/export boundaries without being guessed.
17. Canonical-only setup ordering cannot be used to materialize a setup-time decision prefix, while event-time decisions may still consume the complete setup state after setup is committed.


## 3.1 C2 acquisition-contract tests

The podcast batch route adds workflow state that must not be confused with evidence verification.

Focused tests should cover:

1. stable RSS episode identity across repeated feed reads;
2. deduplication that does not depend only on mutable title text;
3. missing feed transcript remains a normal state and may trigger ASR;
4. already-processed episodes can be recognized without retranscription;
5. acquisition/ASR/extraction/human-review states remain independent;
6. ASR complete or extraction complete never implies VERIFIED evidence;
7. out-of-scope episodes can remain inventoried without entering the active queue;
8. full media/transcript payloads are excluded from Git-managed manifest serialization;
9. an in-scope episode may yield zero useful candidates without becoming an error;
10. candidate timestamps/categories survive serialization deterministically;
11. review-packet merge/ranking/budget behavior is deterministic;
12. C2D P0/P1/P2 values are acquisition-review priorities only and never become Storyteller decision-quality labels;
13. review-packet generation keeps human review at NOT_STARTED until primary-source review actually occurs;
14. review packets do not embed full transcript text or source media payloads.

Live RSS/network probing should not replace deterministic parser/domain tests. Keep network-dependent checks as bounded acquisition validation, not the core unit-test contract.

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

## 7. Exact commands and acceptance layers

E1 uses Python 3.12+ with the following local quality gate:

```bash
python -m pip install -e ".[dev]"
ruff check .
ruff format --check --diff .
pytest
```

The configured Mini MCP repository alias is `evidence`. Normal local iteration should use the allow-listed tasks:

```text
ruff-check
ruff-format-check
pytest
quality
```

`quality` is the default logical-checkpoint gate and currently covers:

```text
ruff check .
ruff format --check --diff .
pytest
```

Use focused local validation during a bounded implementation slice, then run `quality` before committing and pushing the logical checkpoint. Do not push solely to obtain routine lint/test feedback that is already available locally.

GitHub Actions is the independent acceptance layer. After the logical checkpoint is committed and pushed:

1. use Mini MCP `github_pr_audit` to verify the live PR, exact head SHA, required checks, review state and mergeability;
2. require the GitHub Actions lint/format/test gate to pass on that exact pushed HEAD;
3. merge only after the remote acceptance gates required by repository policy are satisfied.

Local GREEN and GitHub GREEN have different roles:

- **local GREEN** enables efficient implementation and checkpoint formation;
- **GitHub GREEN on exact HEAD** provides independent remote acceptance before merge.

A change that has not reached pytest because installation or linting failed is not a GREEN domain test result. A locally GREEN change is not merge-ready until the required GitHub acceptance also passes on the exact checkpoint HEAD.
