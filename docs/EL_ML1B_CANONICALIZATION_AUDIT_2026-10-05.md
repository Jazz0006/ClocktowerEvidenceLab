# EL-ML1B-1B — Canonical Historical Decision Materialization Audit — 2026-10-05

> Status: **CANONICALIZATION AUDIT COMPLETE / DP-R01 + DP-R02 + DP-R05 MATERIALIZED**
>
> Scope: the six historical rows in `docs/EL_ML1B_READY_HISTORICAL_BENCHMARK_V1.json`.
>
> Authority: `AGENTS.md`, EL-ML1A, and the ML recommendation evidence readiness contract.

## 1. Purpose

EL-ML1B-1B asks a narrower question than EL-ML1A readiness:

> Does the repository contain enough evidence-backed canonical history and provenance to materialize a real `DecisionSlice + HistoricalPrefixBoundary` now, without inventing identifiers, setup chronology, missing state, or Host-owned legality?

A row may remain benchmark `READY` while still being `DOCUMENTED_READY`. Benchmark usefulness and canonical machine materialization are related but distinct states.

The hard gate for promotion is:

```text
source-backed game / reconstruction identity
+ authoritative setup/event history
+ evidence-backed decision boundary
+ DecisionSlice linked to its resulting history
+ observed-choice provenance
+ rationale / explicit-alternative provenance when present
+ source / game / Storyteller split grouping
+ executable no-hindsight materialization
= CANONICAL_SEED_MATERIALIZED
```

## 2. Six-row audit

| Benchmark | Current audit verdict | Materialization action | Evidence gap / reason |
| --- | --- | --- | --- |
| **DP-R01 — G01 Drunk assignment** | **SAFE / MATERIALIZED** | promote to `CANONICAL_SEED_MATERIALIZED` | The shared G01 reconstruction preserves the verified grouped nine-seat shown-role layout before the Drunk assignment and later Red Herring. Ben Burns is used only as the conservative split anchor; controller remains generic `STORYTELLER`, and no synthetic joint Ben+Adam identity or unsupported personal actor attribution is created. |
| **DP-R02 — G01 Drunk-Empath Night-1 = 0** | **SAFE / MATERIALIZED** | promote to `CANONICAL_SEED_MATERIALIZED` | The same G01 reconstruction preserves the verified setup, Red Herring, prior Chef `1`, observed `0`, explicit rationale, and explicit rejected `2`. Alternative `1` remains unmentioned/unknown rather than being converted into rejection evidence. |
| **DP-R03 — G05 Chef becomes Drunk** | **CANONICALIZATION BLOCKED** | keep `DOCUMENTED_READY` | Primary review proves that the complete player-role layout was fixed before the 03:32 Drunk assignment, but the current repository does not retain that complete seat/role map. Re-acquire only that bounded setup state; do not reconstruct it from later facts or rules. |
| **DP-R04 — G05 Red Herring = Lyra** | **CANONICALIZATION BLOCKED** | keep `DOCUMENTED_READY` | The Drunk -> Red Herring -> bluffs ordering and choice rationale are verified, but the retained canonical prefix still lacks the complete G05 setup map needed to materialize the state. Repair DP-R03/DP-R04 together from the same bounded setup source. |
| **DP-R05 — G10 Empath becomes Drunk** | **SAFE / MATERIALIZED** | promote to `CANONICAL_SEED_MATERIALIZED` | G10 retains the full nine-seat shown-role layout as one evidenced grouped setup commitment, the 16:29 assignment result, explicit Demon-adjacency rationale, source provenance, and stable Storyteller independence key. The unknown internal order of individual role selection remains unknown rather than being fabricated. |
| **DP-R06 — G10 Librarian pair** | **CANONICALIZATION BLOCKED PENDING PREFIX CHRONOLOGY** | keep `DOCUMENTED_READY` | The state, actual Drunk, observed pair, rationale, source and Storyteller are strong. However, the retained source chronology does not establish every setup commitment that had historically been committed before the 16:52 Librarian decision. In particular, the later-presented Demon bluffs cannot be moved into or out of the pre-Librarian prefix from video timestamps or BotC rules. The event-prefix materializer must not guess this setup chronology. |

No row is downgraded from EL-ML1A benchmark `READY` in this audit. The blocked rows remain useful documented benchmark decisions; only their machine-canonical materialization is deferred.

## 3. DP-R05 canonical materialization

The first checked-in canonical historical seed is:

`docs/EL_ML1B_G10_DP_R05_CANONICAL_SEED_V1.json`

It is validated by the generic derived interchange contract:

`HistoricalDecisionSeedV1`

The seed preserves:

- game: `evidence:c1d:g10-game2`;
- reconstruction revision: `revision:g10:1`;
- Storyteller independence: `st-the-megavoid`;
- source: YouTube `G9z25aM9u7s`;
- evidenced setup order 1: complete grouped `SHOWN_ROLE_LAYOUT`;
- decision boundary: after setup order 1;
- resulting setup order 2: `DRUNK_ASSIGNMENT`;
- observed choice: seat 1 / shown Empath -> actual Drunk;
- explicit rationale: Empath adjacent to the Demon;
- field/history-level evidence assertion links.

The grouped layout does **not** assert an internal order for how its nine individual roles were selected.

Executable materialization yields:

```text
historical prefix
    = setup:g10:shown-layout

excluded
    = setup:g10:drunk-assignment
    = later Red Herring / Librarian / Demon bluff / night information
    = later game history
```

The IDs previously used only by the G10 TBGS regression fixture are now backed by this checked-in non-test canonical seed instead of being used as unsupported manifest references.

### 3.1 G01 DP-R01 + DP-R02 shared reconstruction materialization

Two additional checked-in seeds now share one canonical G01 identity:

- `docs/EL_ML1B_G01_DP_R01_CANONICAL_SEED_V1.json`;
- `docs/EL_ML1B_G01_DP_R02_CANONICAL_SEED_V1.json`.

Both use:

- game: `evidence:e0:g01-a-stud-in-scarlet`;
- reconstruction revision: `revision:g01:1`;
- source group: `source-group:g01-a-stud-in-scarlet`;
- conservative split anchor: `st-ben-burns`.

The split anchor does **not** assert that Ben personally made every decision. The retained source also contains co-Storyteller/assistant context involving Adam, but the canonical seed does not fabricate a synthetic joint identity or an unsupported stable Adam identity.

DP-R01 materializes:

```text
historical prefix
    = setup:g01:shown-layout

excluded
    = setup:g01:drunk-assignment
    = setup:g01:red-herring
    = Night-1 history
```

DP-R02 materializes:

```text
historical prefix
    = complete bounded setup history
    + event:g01:n1-chef-info = 1

excluded
    = event:g01:n1-drunk-empath-info = 0
    = later Fortune Teller / later game history
```

The DP-R02 source-backed negative evidence is intentionally narrow: only `2` is explicitly rejected as less believable. Unmentioned `1` is not treated as considered, rejected, or inferior.

Demon bluffs remain retained elsewhere as evidence, but are intentionally omitted from these bounded canonical seeds because their exact setup chronology relative to DP-R01 is not evidence-backed.

## 4. Authority boundaries preserved

This slice does not contain:

- BotC legal-candidate enumeration;
- Host policy scoring;
- GOOD/BAD labels;
- inferred rejected candidates;
- `LEGAL_UNCHOSEN` conversion;
- a SQLite/Alembic migration;
- a new canonical persistence owner.

The seed is a versioned **derived interchange artifact** over existing EvidenceLab domain semantics. Host remains responsible for recovering the legal candidate domain.

## 5. Next bounded action

Continue EL-ML1B-1B with **G05 bounded setup-map recovery for DP-R03 + DP-R04**.

Next bounded action:

1. re-acquire only the missing complete G05 seat/role map from the already-known primary source;
2. preserve the already-verified ordering Drunk assignment -> Red Herring -> later bluffs without importing rules or later facts backward;
3. materialize DP-R03 and DP-R04 together only if the full pre-decision setup can be source-backed;
4. leave G10 DP-R06 blocked until its setup chronology at the Librarian boundary is evidence-backed.

No broad new acquisition is justified yet.
