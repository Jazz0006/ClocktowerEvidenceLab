# Evidence and Provenance Standard

## 1. Purpose

This document defines how the project distinguishes historical evidence from reconstruction and inference.

The standard exists to prevent hindsight leakage, silent guessing and later policy analysis from contaminating source history.

## 2. Two-axis evidence status

### Derivation

`OBSERVED`
: Directly visible/audible in a primary source or directly present in a structured authoritative record.

`RECONSTRUCTED`
: Derived by combining multiple pieces of evidence into a concrete historical fact.

`INFERRED`
: Not directly established by the source; inferred from constraints or interpretation.

`UNKNOWN`
: Not established.

`NOT_APPLICABLE`
: The field does not apply to this game/decision.

### Verification

`UNVERIFIED`
: Initial extraction/reconstruction has not received a verification pass.

`VERIFIED`
: A verification pass confirmed the evidence and provenance are sufficient for the stated fact.

`DISPUTED`
: Available evidence conflicts or reviewers disagree.

Do not collapse these axes into a single confidence label.

## 3. Evidence fragments

A material assertion should link to one or more source fragments.

For video evidence, a fragment should normally include:

- source ID;
- start timestamp;
- optional end timestamp;
- concise description;
- optional minimal quotation only when necessary.

Do not copy long transcripts.

## 3.1 Source metadata provenance

Stable source identity and locator fields belong on the Source record.

Descriptive metadata whose truth itself must be evidenced—such as a title, publisher/channel or publication date reconstructed from indexes—uses the normal EvidenceAssertion path with the Source as subject. Do not maintain a second derivation/verification mechanism inside Source metadata fields.

Assertion derivation and reconstruction-revision membership are independent dimensions. A RECONSTRUCTED source-metadata claim need not belong to a game ReconstructionRevision; conversely an INFERRED interpretation may be explicitly scoped to one reconstruction revision.

## 4. Reconstruction completeness

Track completeness by region or phase, not only by whole game.

Example:

```text
SETUP      VERIFIED
NIGHT_1    VERIFIED
DAY_1      PARTIAL
NIGHT_2    UNKNOWN
LATER      NOT_RECONSTRUCTED
```

A verified Night-1 decision can be usable even when the full game is not reconstructed.

## 5. Decision evidence strength

Observed Storyteller choice is one evidence type.

Stronger additional evidence includes:

- choice-specific explicit rationale;
- explicit rejected alternative;
- repeated comparable pattern by the same Storyteller;
- comparable evidence from independent Storytellers.

Keep these separate. Do not synthesize a quality label at ingestion time.

## 6. Storyteller qualification

Maintain Storyteller-qualification facts separately from game reconstruction semantics, but do **not** create a second evidence subsystem.

Qualification evidence uses the ordinary evidence path:

```text
Storyteller subject
    ← EvidenceAssertion
    ← EvidenceFragment
    ← Source
    + VerificationRecord audit trail
```

A later qualification summary/status may be a derived projection. Its underlying evidence remains ordinary EvidenceAssertion data.

Suggested descriptive levels:

```text
VERIFIED_EXPERT_OR_TRUSTED
EXPERIENCED
UNVERIFIED
UNKNOWN
```

The exact labels may be refined later.

Qualification should cite independent public evidence where possible.

## 7. GOLD qualification

GOLD is a derived decision-slice qualification.

A candidate GOLD decision normally requires:

- sufficiently qualified Storyteller;
- primary/high-fidelity source;
- reconstructable committed prefix;
- observed choice verified;
- no material unresolved ambiguity that changes the decision context.

Explicit rationale is preferred but not mandatory.

Do not count multiple games by one Storyteller as independent experts.

## 8. Registration witness policy

Registration is interaction-local.

Record a specific witness only when evidence supports it.

If several legal registration witnesses can explain the same visible information and the Storyteller's actual witness is not evidenced:

```text
observed visible result = known
actual registration witness = UNKNOWN
```

Compatible witnesses are downstream derived analysis.

## 9. Player experience

Do not guess a coarse category if better raw metadata is available.

Prefer evidence such as:

- explicit “first game” statement;
- known prior game count;
- approximate range;
- table-level description from the source.

Later analysis can map raw experience metadata into cohorts such as BEGINNER or EXPERIENCED.

## 10. Outcome

Record the game winner/outcome when known because it is historical fact.

Never automatically use outcome as a Storyteller decision-quality label.

## 11. Revision policy

A correction must preserve history.

Recommended model:

```text
reconstruction_revision 1
    superseded_by
reconstruction_revision 2
```

A revision note should explain the evidence that changed the reconstruction.

Raw source/evidence records are not rewritten merely because a reconstruction changed.
