# E0 Evidence Contract Completion Audit — 2026-09-22

> Status: **E0 CONTRACT PILOT COMPLETE**
>
> Case: Ben Burns — `A Stud In Scarlet`
>
> Scope: evidence-contract validation only. No recommendation/policy engine, BotC legality engine, persisted application schema or UI was implemented.

## 1. Completion decision

E0 is complete enough to justify E1.

The pilot has produced:

- a stable source record and screening record;
- primary-supported setup reconstruction;
- bounded primary-reviewed Night-1 timeline;
- primary evidence fragments with timestamps;
- three traceable Storyteller DecisionSlices;
- explicit OBSERVED / RECONSTRUCTED / INFERRED / UNKNOWN distinctions;
- verification status independent from derivation;
- real examples of setup-prefix, compound-event, partial-order and registration-witness ambiguity;
- a draft export pressure model;
- a concrete list of schema/workflow failures exposed by real evidence.

No GOLD-qualified decision is required for E0 completion.

GOLD remains a later derived qualification. The pilot's purpose was to prove trustworthy evidence reconstruction, not to force every useful observation into GOLD.

## 2. E0 deliverables audit

| Deliverable | Result |
|---|---|
| source record | COMPLETE for pilot use |
| screening record | COMPLETE |
| setup reconstruction | COMPLETE for bounded E0 scope |
| ordered Night-1 timeline | COMPLETE for Chef / Drunk-Empath / Fortune Teller interactions |
| at least 3 Storyteller decision slices | COMPLETE — 3 admitted |
| evidence fragments/timestamps | COMPLETE for material bounded claims |
| derivation + verification states | COMPLETE |
| schema/workflow gap list | COMPLETE |
| draft export pressure | COMPLETE |

Optional precision gaps remain, but none blocks the evidence contract:

- exact timestamp of the supplied grimoire screenshot;
- finer sub-timestamp split inside the Fortune Teller interaction;
- an explicit primary statement of the Fortune Teller registration witness, if one exists;
- direct primary-page verification of some source metadata.

These remain optional because the corpus can preserve UNKNOWN / INFERRED without inventing facts.

## 3. Admitted DecisionSlices

### DS-ASIS-001 — Drunk shown identity = Empath

Evidence:

- primary grimoire/setup frame shows Sullivan as Empath;
- `09:49` establishes Sullivan is actually the Drunk.

Treatment:

- observed-value derivation: RECONSTRUCTED from primary evidence;
- verification: VERIFIED;
- decision-control classification: Storyteller-controlled by the Evidence Lab normative decision taxonomy;
- historical setup internal order: UNKNOWN;
- personal Storyteller actor attribution: UNKNOWN unless separately evidenced;
- rationale: UNKNOWN;
- rejected alternatives: UNKNOWN.

This slice proves that setup-time choices require decision-prefix semantics that are not limited to Night event sequence numbers.

### DS-ASIS-002 — Red Herring = Sullivan

Evidence:

- `10:32` primary review.

Treatment:

- derivation: OBSERVED;
- verification: VERIFIED;
- setup internal order: UNKNOWN;
- rationale: UNKNOWN;
- rejected alternatives: UNKNOWN.

This slice confirms that setup commitments can be useful evidence even when their exact commit ordering is not recoverable from an edited source.

### DS-ASIS-003 — Drunk-as-Empath Night-1 information = 0

Evidence:

- `12:41` primary review.

Treatment:

- derivation: OBSERVED;
- verification: VERIFIED;
- observed choice: `0`;
- explicit choice-specific rationale: PRESENT;
- explicitly rejected alternative: `2`, because Ben says it would be less believable;
- treatment of alternative `1`: UNKNOWN;
- prior committed Night-1 context includes verified Chef delivery `1`.

This is the strongest current E0 decision record because it preserves a positive expert choice plus explicit rationale and one explicitly rejected alternative without converting unmentioned alternatives into negative labels.

## 4. Verified historical events that are not forced into DecisionSlices

### Chef — 11:53

Primary review establishes:

- Jon is Chef;
- delivered information = `1`;
- derivation = OBSERVED;
- verification = VERIFIED.

No explicit choice-specific rationale or historical registration witness was supplied.

Therefore E0 stores this as a verified historical information-delivery event.

It is intentionally **not** promoted into a discretionary Storyteller DecisionSlice merely because downstream BotC rules may expose alternative registrations/values.

### Fortune Teller — 15:18

Primary review establishes:

- Blair selects Tom + Elliott;
- result delivered = YES;
- target commitment semantically precedes result delivery;
- derivation = OBSERVED;
- verification = VERIFIED.

A knowledgeable reviewer infers that Elliott's Recluse registered as Demon.

Evidence treatment:

- `Tom + Elliott -> YES`: OBSERVED / VERIFIED;
- `Recluse-as-Demon witness`: INFERRED reviewer interpretation;
- source-observed historical registration witness: UNKNOWN.

This is the clearest E0 proof that a strong mechanical inference must not silently become a source-observed historical fact.

## 5. Game context

Human primary review confirms that Ben is running this game for beginner / new players.

Treatment:

- game-level context: OBSERVED / VERIFIED;
- exact source timestamp: not supplied;
- this context must not be copied automatically into every individual DecisionSlice as its rationale.

Context and choice-specific rationale are separate evidence concepts.

## 6. Evidence-contract findings frozen by E0

The following are now requirements, not speculative ideas.

### 6.1 Source locator is not evidence verification

A stable primary URL proves where the source is.

It does not prove that any gameplay assertion was checked against the source.

The workflow must distinguish acquisition/discovery state from evidence verification.

### 6.2 Source time and historical semantic time are different

A video timestamp is where evidence appears in the recording.

It is not necessarily when the game commitment historically occurred.

Edited/explanatory media requires separate:

- source locator time/range;
- historical phase/order semantics.

### 6.3 Partial order is legitimate

Setup commitments may be known to exist before Night 1 without evidence for their exact internal order.

The model must not require fabricated total ordering.

### 6.4 Evidence fragments and semantic events are many-to-many

One source fragment may support several semantic facts/events.

One semantic fact may require multiple source fragments.

The Fortune Teller compound interaction and Drunk actual-vs-shown identity demonstrate both directions.

### 6.5 Historical event is not automatically a DecisionSlice

Evidence Lab may verify that a Storyteller delivered a result without independently proving that the result represented a discretionary choice among alternatives.

Do not use downstream legality to manufacture decision semantics.

### 6.6 Player-controlled and Storyteller-controlled commitments are distinct

Fortune Teller target selection belongs to the committed prefix.

The later result does not.

Compound source moments must preserve this semantic split.

### 6.7 Setup decisions require decision-prefix semantics

Decision boundaries cannot rely only on ordered Night event sequence numbers.

Setup-time choices such as Drunk shown identity and Red Herring need a prefix model that can represent:

- known prior commitments;
- unknown ordering;
- the choice under study;
- later commitments excluded from the prefix.

### 6.8 Reviewer inference is distinct from source observation

A reviewer may make a strong domain inference.

That inference needs:

- its own derivation status;
- provenance to the reviewer/review pass;
- no silent promotion to OBSERVED.

### 6.9 Verification needs an audit record

`VERIFIED` cannot be only a mutable boolean.

At minimum, the durable model needs to know:

- what was verified;
- by whom/reviewer identity or reviewer key;
- when;
- against which evidence fragment(s);
- optional verification note;
- prior status/history where practical.

### 6.10 UNKNOWN must remain cheap and durable

The pilot repeatedly needed UNKNOWN for:

- setup internal order;
- personal actor attribution;
- historical registration witness;
- unmentioned alternatives;
- absent rationale.

UNKNOWN is normal evidence, not an error state.

### 6.11 Observed value provenance and decision-control taxonomy are separate

Primary evidence can establish **what happened** without itself explaining **which game actor owns that kind of choice**.

E0 uses the Evidence Lab's normative decision taxonomy to classify known control ownership, for example:

- Red Herring as Storyteller-controlled;
- Drunk shown identity as a Storyteller decision family.

This classification must remain separate from source provenance.

E1 must not imply that a primary clip “proved” control ownership merely because it proved the observed value, and it must not import downstream legality enumeration to fill that gap.

## 7. What E0 rejects

Do not carry these patterns into E1:

- one timestamp field used for both video locator and game-event time;
- one event per source fragment;
- mandatory total ordering of setup facts;
- registration witness filled from rules legality;
- delivered output automatically treated as a discretionary decision;
- reviewer inference stored as OBSERVED;
- game-level beginner context copied into every decision rationale;
- hand-authored `gold=true`;
- case-specific A Stud / Ben schema fields.

## 8. E1 gate

E1 may begin after this audit.

E1 should implement only enough domain/persistence infrastructure to represent this pilot without information loss and to support a second game.

The E0 branch / PR should remain draft until the user explicitly authorizes merge.
