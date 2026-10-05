# EL-ML1B-1B — Canonical Historical Decision Materialization Audit — 2026-10-05

> Status: **CANONICALIZATION AUDIT COMPLETE / DP-R01 THROUGH DP-R05 MATERIALIZED / DP-R06 REMAINS BLOCKED**
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
| **DP-R03 — G05 Chef becomes Drunk** | **SAFE / MATERIALIZED** | promote to `CANONICAL_SEED_MATERIALIZED` | The previously missing 20-seat map was recovered from the earlier primary-video/full-grimoire reconstruction. The prefix preserves all base roles plus five Traveller roles/alignments already committed before the Drunk choice, while keeping the internal role-selection order unknown. |
| **DP-R04 — G05 Red Herring = Lyra** | **SAFE / MATERIALIZED** | promote to `CANONICAL_SEED_MATERIALIZED` | The same reconstruction establishes a stricter prefix than the earlier audit knew: after the Drunk assignment and before Red Herring, the Washerwoman information pair had already been selected. DP-R04 therefore includes that intermediate commitment and excludes the later Demon bluffs. |
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

### 3.2 G05 DP-R03 + DP-R04 shared reconstruction materialization

The missing G05 setup state was recovered without re-inference from rules or later gameplay. The bounded recovery is recorded at:

`docs/G05_A_FOND_FAREWELL_SETUP_RECOVERY_2026-10-05.md`

It reuses the earlier primary-video/full-grimoire reconstruction retained in the sibling Host repository and restores the complete 20-seat table: 15 base players plus five Travellers, including source-backed Traveller alignments.

Two new seeds share one G05 reconstruction:

- `docs/EL_ML1B_G05_DP_R03_CANONICAL_SEED_V1.json`;
- `docs/EL_ML1B_G05_DP_R04_CANONICAL_SEED_V1.json`.

DP-R03 materializes:

```text
historical prefix
    = setup:g05:pre-drunk-state
      (complete 20-seat shown/public role state + Traveller alignments)

excluded
    = setup:g05:drunk-assignment
    = setup:g05:washerwoman-info
    = setup:g05:red-herring
    = later Demon bluffs / Night-1 history
```

DP-R04 materializes:

```text
historical prefix
    = setup:g05:pre-drunk-state
    + setup:g05:drunk-assignment
    + setup:g05:washerwoman-info

excluded
    = setup:g05:red-herring
    = later Demon bluffs / Night-1 history
```

The intermediate Washerwoman commitment is important: the older primary reconstruction places its information selection between the Drunk choice and the Red Herring choice. Leaving it out would make the DP-R04 historical prefix incomplete.

The source has two bounded review locator sets for the same setup commitments: the later EvidenceLab review records the Drunk/Red-Herring decision commitments around `03:32` / `04:04`, while the older Host reconstruction records later grimoire-state markings around `03:43` / `04:17`. The canonical seeds preserve the semantic order without pretending those locator timestamps are one total historical clock.

Traveller presence does not prevent EvidenceLab from preserving historical state. It remains a downstream Host enrichment requirement for legal-candidate/counterfactual execution; the 20-seat circle must never be compressed into 15 base seats.

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

Continue EL-ML1B-1B with **G10 DP-R06 bounded prefix-chronology recovery**.

Five of the six READY rows are now canonical historical seeds. The only remaining row is DP-R06.

Next bounded action:

1. recover only the setup commitments that were historically committed before the G10 Librarian decision at 16:52;
2. determine whether any Demon-bluff or other setup commitment belongs before that boundary from source evidence, not from presentation order or BotC rules;
3. materialize DP-R06 only if the exact event/setup prefix can be represented without guessing;
4. if that bounded chronology cannot be recovered, keep DP-R06 `DOCUMENTED_READY` and move to the existing PARTIAL-candidate repair queue rather than weakening the no-hindsight gate.

No broad new acquisition is justified yet.
