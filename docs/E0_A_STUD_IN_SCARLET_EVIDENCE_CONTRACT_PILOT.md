# E0 Pilot — A Stud In Scarlet Evidence Contract Reconstruction

> Status: **IN PROGRESS**
>
> Purpose: validate the Evidence Lab workflow against one real expert/trusted Storyteller primary source before freezing the persisted schema or implementation stack.
>
> This document is a pilot notebook, not the final schema.

## 1. Primary source record

Pilot-local source key (not a frozen ID scheme):

`SRC-E0-ASIS-YT`

| Field | Current value | Derivation | Verification | Provenance |
|---|---|---|---|---|
| platform | YouTube | OBSERVED | UNVERIFIED | primary source metadata |
| platform source ID | `qZBvRfM3Xow` | OBSERVED | UNVERIFIED | stable primary-source locator |
| title | `A Stud In Scarlet | NRB Play Blood On The Clocktower` | RECONSTRUCTED | UNVERIFIED | consistent public indexes referencing the primary locator; direct primary-page body not captured in this pass |
| channel / publisher | No Rolls Barred | RECONSTRUCTED | UNVERIFIED | consistent public indexes referencing the primary locator |
| publication date | 2021-02-05 | RECONSTRUCTED | UNVERIFIED | consistent public episode indexes; primary-page metadata still needs direct verification |
| URL | `https://www.youtube.com/watch?v=qZBvRfM3Xow` | OBSERVED | UNVERIFIED | primary source locator |
| Storyteller | Ben Burns | RECONSTRUCTED | UNVERIFIED | consistent episode indexes / prior source catalog; in-video or direct primary-description verification still required |
| co-Storyteller / assistant | UNKNOWN | UNKNOWN | UNVERIFIED | secondary sources name Adam; primary in-video verification still required |
| script | UNKNOWN | UNKNOWN | UNVERIFIED | Trouble Brewing is a strong secondary lead but is not yet promoted to a primary-backed assertion |
| inclusion reason | TARGETED_RESEARCH_CASE | NOT_APPLICABLE | UNVERIFIED | selected to stress-test Drunk / Fortune Teller / Recluse / Chef evidence semantics |

### Storyteller qualification evidence

Qualification is separate from game reconstruction.

Official The Pandemonium Institute material documents Ben Burns as a long-running Blood on the Clocktower content creator / representative with years of involvement in the game:

- `https://bloodontheclocktower.com/blogs/news/ben-burns-appreciation-post`
- `https://bloodontheclocktower.com/blogs/news/an-update-on-community-management-and-content-creation-at-tpi`

Current qualification evidence collected from official TPI material:

- TPI describes Ben as integral to Blood on the Clocktower for many years, including early conventions, the Kickstarter, and official Twitch/YouTube work;
- TPI separately describes him as leading YouTube/Twitch content and appearing at conventions as a special guest / representative of the game.

Current pilot treatment:

- qualification candidate: `VERIFIED_EXPERT_OR_TRUSTED`;
- evidence source quality: official TPI;
- verification: `UNVERIFIED` because Evidence Lab requires a human verification pass before promotion;
- do not derive GOLD until a human verification pass confirms both qualification evidence and the individual decision slice.

## 2. Screening record

This is a reconstruction-value screen, not a quality score.

| Screening dimension | Current assessment | Status / note |
|---|---|---|
| primary source exists | YES | official No Rolls Barred YouTube upload |
| public source | YES | public YouTube source |
| game identity recoverable | YES | source title and episode identity are stable |
| Storyteller identity recoverable | YES | Ben is named in primary metadata |
| setup / seating recoverability | YES | human-reviewed primary frame supports full visible seating/roles and Demon bluffs |
| Night 1 recoverability | HIGH | primary timestamps now capture Chef=1, Drunk information=0, and Fortune Teller Tom+Elliott -> YES |
| grimoire / Storyteller view visibility | YES | user-supplied primary frame visibly exposes setup/grimoire state |
| player action visibility | YES | at 15:18 Blair selects Tom + Elliott |
| Storyteller output visibility | YES | at 12:41 Sullivan receives 0; at 15:18 Fortune Teller receives YES |
| choice-specific rationale | PRESENT | at 12:41 Ben explains why 2 would be less believable |
| explicit rejected alternatives | PRESENT | at 12:41 alternative 2 is explicitly rejected as less believable |
| editing gaps | PRESENT / EXPECTED | produced YouTube episode; exact continuity around setup decisions must be checked |
| reconstructable phase selected for E0 | Night 1 + required setup commitments | intentionally bounded first pass |

Selection decision: **keep for E0 reconstruction**.

## 3. Evidence fragments currently supported by the primary source

Automated acquisition recovered only the stable primary locator. Human primary review subsequently supplied a grimoire/setup frame and timed gameplay evidence. Keep the automated-acquisition limitation as provenance history, but treat the human-reviewed fragments in §3.1 as the current authoritative E0 evidence set.

### FRAG-ASIS-LOCATOR-001

- source: `SRC-E0-ASIS-YT`
- locator: `https://www.youtube.com/watch?v=qZBvRfM3Xow`
- timestamp: NOT_APPLICABLE
- fact: stable primary-video locator / platform source ID
- derivation: OBSERVED
- verification: UNVERIFIED

Direct title/channel/date/Storyteller metadata remains reconstructed from consistent public indexes in this pass and is not promoted to a primary-content EvidenceFragment.

## 3.1 First human-verified primary fragments — 2026-09-22

### FRAG-ASIS-SETUP-FRAME-001

- source: `SRC-E0-ASIS-YT`
- locator: user-supplied screenshot captured from the primary video; exact playback timestamp not supplied
- fact: visible grimoire/seating supports:
  - seat 1 Luke — Imp;
  - seat 2 Oli — Ravenkeeper;
  - seat 3 Blair — Fortune Teller;
  - seat 4 Tom — Monk;
  - seat 5 Elliott — Recluse;
  - seat 6 Laurie — Scarlet Woman;
  - seat 7 Isaac — Undertaker;
  - seat 8 Jon — Chef;
  - seat 9 Sullivan — shown Empath;
  - Demon bluffs — Saint / Slayer / Soldier.
- derivation: OBSERVED
- verification: VERIFIED by human primary review
- note: the image is not committed; only concise facts/provenance are retained.

### FRAG-ASIS-09-49-DRUNK

- source: `SRC-E0-ASIS-YT`
- timestamp: `09:49`
- fact: Sullivan is established as the actual Drunk
- derivation: OBSERVED
- verification: VERIFIED by human primary review

Combined with `FRAG-ASIS-SETUP-FRAME-001`, this supports the concrete historical setup fact:

`Sullivan actual role = Drunk; shown/believed role = Empath`

with derivation `RECONSTRUCTED`.

### FRAG-ASIS-10-32-RED-HERRING

- source: `SRC-E0-ASIS-YT`
- timestamp: `10:32`
- fact: Sullivan is made the Fortune Teller Red Herring
- derivation: OBSERVED
- verification: VERIFIED by human primary review
- explicit rationale: none reported
- explicit rejected alternative: none reported

### FRAG-ASIS-11-53-CHEF

- source: `SRC-E0-ASIS-YT`
- timestamp: `11:53`
- fact: Jon's Chef receives `1`
- derivation: OBSERVED
- verification: VERIFIED by human primary review
- explicit registration statement: none supplied
- explicit rationale: none supplied

This supports a verified information-delivery event. It does not by itself establish a discretionary Storyteller decision or historical registration witness.

### FRAG-ASIS-12-41-DRUNK-EMPATH

- source: `SRC-E0-ASIS-YT`
- timestamp: `12:41`
- fact: Sullivan, believing Empath, is given `0`
- derivation: OBSERVED
- verification: VERIFIED by human primary review
- explicit rationale: Ben explains that `2` would be less believable
- explicit rejected alternative: `2`
- unobserved alternatives: no claim is made about whether `1` was considered or rejected

### FRAG-ASIS-15-18-FORTUNE-TELLER

- source: `SRC-E0-ASIS-YT`
- timestamp: `15:18`
- fact: Blair chooses Tom + Elliott and receives YES
- derivation: OBSERVED
- verification: VERIFIED by human primary review
- player-controlled choice: target pair Tom + Elliott
- Storyteller output: YES
- historical registration witness: UNKNOWN at the evidence layer
- reviewer inference: Elliott's Recluse registering as Demon is the mechanically evident explanation; derivation = INFERRED, not OBSERVED
- explicit rationale: none reported
- explicit rejected alternative: none reported
- precision note: one timestamp currently covers both target commitment and result delivery; exact sub-boundary is not yet timestamped

### FRAG-ASIS-CONTEXT-BEGINNER

- source: `SRC-E0-ASIS-YT`
- timestamp: UNKNOWN / not supplied
- fact: Ben is running the game for beginner / new players
- derivation: OBSERVED through human primary review
- verification: VERIFIED
- scope: game-level context
- important: do not automatically treat this as the rationale for every individual Storyteller decision

### Verification note

This is the first human primary-review pass. It is stronger than the earlier automated locator work because the reviewer directly watched the primary video and supplied timestamps.

The timestamps are evidence locators. They are **not automatically historical event times** for setup facts whose real commitment occurred before the video explained/revealed them.

## 4. Historical locator-only secondary leads

The following information was used only as an acquisition aid before primary playback.

It is **not corpus evidence** and must not be imported as OBSERVED / RECONSTRUCTED facts merely because the secondary sources were accurate. Primary-reviewed replacements now exist for the bounded setup/Night-1 facts.

Secondary lead sources include the public No Rolls Barred fan index and the prior CampBoardGameHost D5F research branch.

Candidate setup / Night-1 picture:

- Luke — Imp;
- Oli — Ravenkeeper;
- Blair — Fortune Teller;
- Tom — Monk;
- Elliott — Recluse;
- Laurie — Scarlet Woman;
- Isaac — Undertaker;
- Jon — Chef;
- Sullivan — Drunk, shown Empath;
- candidate Fortune Teller red herring: Sullivan;
- candidate Night-1 Chef information: `1`;
- candidate Night-1 Drunk-as-Empath information: `0`;
- candidate Night-1 Fortune Teller player choice: Tom + Elliott;
- candidate Night-1 Fortune Teller delivered result: YES.

These items remain secondary locator leads in provenance history. Where §3.1 now contains matching primary-reviewed evidence, the primary evidence supersedes the locator lead for corpus reconstruction.

The old D5F phrase “Fortune Teller YES via Recluse-as-Demon” is specifically **not** imported as historical fact.

## 4.1 Legacy D5F separation audit

The prior CampBoardGameHost branch was inspected directly rather than relying on memory.

Relevant legacy artifacts:

- `docs/SDE_2D5F_EXTERNAL_EVIDENCE_SOURCE_CATALOG_2026-09-21.tsv`;
- `Sde2D5FExpertObservedFirstNightEvidenceTest.kt`;
- `Sde2D5FAStudInScarletCandidateBuilder`.

The legacy fixture itself explicitly states:

- the detailed state came from a public episode index;
- the YouTube recording is the primary source;
- material Night-1 primary verification was still pending;
- the candidate must not be promoted to admitted GOLD before that verification.

This is important because the old catalog also contains fields such as:

`Chef=1 requires Elliott Recluse to register Evil`

and

`FT Tom+Elliott=YES requires Elliott to register as Demon`.

Those are **downstream rules-engine witness projections**, not evidence that the historical Storyteller consciously committed those exact registration witnesses.

Evidence Lab treatment:

- the old setup/Night-1 values remain locator leads;
- the old compatible-witness enumeration is not imported as historical provenance;
- actual registration witness stays UNKNOWN unless the primary recording supports it;
- later CampBoardGameHost analysis may independently recover compatible witness sets after Evidence Lab export.

### Why this matters

This pilot has exposed a concrete contamination path:

```text
secondary reconstruction
    + downstream rules legality
    -> plausible historical explanation
    -> accidentally written as observed expert decision
```

The Evidence Lab contract must prevent that collapse.

## 4.2 Primary timed-evidence acquisition result

A bounded automated acquisition pass was attempted before declaring a manual-review requirement.

Result:

- the stable YouTube source locator is known;
- public search indexes recover the episode identity and detailed secondary event summary;
- no trustworthy primary Night-1 timestamps were recovered;
- the primary YouTube playback page/body was not retrievable through the current automated path;
- no usable primary caption/timed-transcript endpoint was recovered;
- searches for timestamped mirrors/index citations did not yield a primary-backed timestamp;
- the old D5F source catalog confirms that primary Night-1 timestamp verification had never been completed there either.

This automated limitation was later resolved by direct human primary playback.

Do not erase this acquisition history: it demonstrates why locator discovery and evidence verification are separate workflow states. Secondary indexes, mirrors, old D5F fixture order and rules-engine reconstruction still must not substitute for primary verification.

## 5. Primary in-video extraction checklist — bounded pass complete

The bounded primary playback pass captured the material setup/Night-1 fragments required for E0. The checklist below is retained as the workflow template that proved useful.

### Q1 — setup commitments before Night 1

Need primary evidence for:

- actual setup / seating;
- Sullivan actually being the Drunk;
- the Townsfolk identity shown to Sullivan;
- Fortune Teller red herring if visible/announced;
- Demon bluffs if visible and material to the committed prefix.

Important:

- “Drunk shown Empath” is a Storyteller-controlled setup commitment candidate.
- Exact ordering among setup commitments may be unavailable in an edited video.
- If only “committed before Night 1” can be established, preserve that weaker temporal fact rather than inventing a total order.

### Q2 — Chef Night-1 delivery

Captured:

- `11:53`;
- Jon's Chef receives `1`;
- no explicit registration treatment or choice-specific rationale was supplied in the review.

Do not assume that a Storyteller-delivered number is automatically a discretionary Storyteller decision.

Evidence Lab records the delivery. Whether the output had multiple legal alternatives is downstream rules knowledge unless the primary source itself establishes the choice.

### Q3 — Drunk shown-Empath Night-1 information

Captured:

- `12:41`;
- Sullivan-as-Empath receives `0`;
- Ben explicitly explains that `2` would be less believable;
- this supplies both choice-specific rationale and an explicitly rejected alternative.

The pilot must not infer a persistent “fake world” unless the historical source supports the concrete delivered information. Cross-night policy belongs to later analysis unless additional primary decisions are reconstructed.

### Q4 — Fortune Teller player action and Storyteller output

This boundary is especially important.

Captured in one compound source fragment at `15:18`:

1. Blair commits Tom + Elliott;
2. the Storyteller delivers YES;
3. target commitment semantically precedes result delivery;
4. no explicit registration statement was supplied;
5. no choice-specific rationale or rejected alternative was supplied.

A knowledgeable reviewer infers Recluse-as-Demon from mechanics, but that remains INFERRED rather than OBSERVED.

The decision-time prefix for a Fortune Teller output must include the committed target pair but must not include the later delivered result.

### Q5 — registration witness

For the candidate Tom + Elliott -> YES interaction:

- visible YES does not by itself authorize a durable `registration_witness = Recluse-as-Demon` assertion;
- if Ben explicitly states or visibly records the registration decision, capture that timestamped fragment;
- otherwise keep the actual registration witness UNKNOWN.

Do not recover the witness by importing CampBoardGameHost legality logic.

## 5.1 Provisional semantic timeline skeleton — locator only

This section deliberately tests the event/commitment vocabulary without promoting secondary reconstruction into the corpus.

### Setup commitment group — exact internal order UNKNOWN

Primary visual/timed evidence now supports:

- nine-player seating / visible setup as reconstructed above;
- Sullivan actual role = Drunk;
- Sullivan shown / believed role = Empath;
- Fortune Teller red herring = Sullivan;
- Demon bluffs = Saint / Slayer / Soldier.

These facts may now enter the current reconstruction revision.

Their **exact historical setup-commit order remains UNKNOWN**. Source presentation timestamps such as 09:49 and 10:32 must not be mistaken for proof that the original setup choices were committed in that same order.

The useful modeling observation is that an edited source may establish all of them as pre-Night-1 commitments without revealing their exact internal commit order.

### Night 1 — primary-reviewed interaction order

Primary playback timestamps now support:

1. `11:53` — Jon's Chef receives `1`;
2. `12:41` — Sullivan-as-Empath receives `0`; Ben explicitly rejects `2` as less believable;
3. `15:18` — Blair selects Tom + Elliott and receives YES.

The timestamp order above is primary-supported source order.

For the Fortune Teller interaction, the target commitment semantically precedes the result delivery, but both currently share one source timestamp.

For primary extraction, the Fortune Teller compound lead must be split into at least:

```text
PLAYER_ACTION_COMMITTED
    Blair -> [Tom, Elliott]

<decision boundary candidate>

STORYTELLER_CHOICE_COMMITTED or historical-output commitment
    result = YES

INFORMATION_DELIVERED
    recipient = Blair
    result = YES
```

Whether the middle event should be represented as a distinct Storyteller-choice event is itself part of the E0 audit. Evidence Lab must not invent a discretionary choice merely because downstream rules analysis can enumerate alternatives.

## 6. Provisional decision-slice candidates

These are **candidates**, not admitted DecisionSlices.

### CANDIDATE-1 — Drunk shown identity

Potential observed choice:

`shown_identity = Empath`

Required before admission:

- timestamped primary evidence that Sullivan is the Drunk and is shown/believes Empath;
- setup-prefix reconstruction sufficient to establish the decision context;
- decision actor attribution;
- human verification pass.

### CANDIDATE-2 — Drunk Night-1 information

Potential observed choice:

`delivered_information = 0`

Required before admission:

- timestamped primary evidence;
- relevant committed prefix;
- distinction between historical delivery and downstream evaluation;
- human verification pass.

### CANDIDATE-3 — Fortune Teller Night-1 output

Potential observed output:

`targets = [Tom, Elliott]`
`delivered_result = YES`

Required before admission:

- timestamped primary player-action fragment;
- timestamped primary result fragment;
- boundary after target commitment and before result delivery;
- registration witness remains UNKNOWN unless explicitly evidenced;
- human verification pass.

### CANDIDATE-4 — Chef Night-1 information

Potential observed output:

`delivered_information = 1`

Required before admission:

- timestamped primary fragment;
- sufficient prefix;
- do not assert “expert chose 1 from alternatives” unless evidence establishes that a genuine Storyteller choice existed;
- human verification pass.

E0 still targets at least three admitted decision slices, but quantity must not override provenance.

## 6.1 Admitted E0 decision slices after primary review 1

These are admitted as traceable historical decision slices, but **not GOLD-qualified yet**.

### DS-ASIS-001 — Drunk shown identity = Empath

- decision family: setup / Drunk shown identity
- observed choice: Empath
- evidence:
  - `FRAG-ASIS-SETUP-FRAME-001`;
  - `FRAG-ASIS-09-49-DRUNK`
- derivation: RECONSTRUCTED
- verification: VERIFIED
- decision actor: Storyteller-controlled setup commitment; personal actor attribution remains UNKNOWN unless primary source establishes it
- committed-prefix precision: PARTIAL / setup internal ordering UNKNOWN
- rationale: UNKNOWN
- rejected alternatives: UNKNOWN
- GOLD: NOT YET ELIGIBLE because exact setup prefix/order and actor attribution remain incomplete

### DS-ASIS-002 — Fortune Teller Red Herring = Sullivan

- decision family: setup / Red Herring
- observed choice: Sullivan
- evidence: `FRAG-ASIS-10-32-RED-HERRING`
- derivation: OBSERVED
- verification: VERIFIED
- committed-prefix precision: PARTIAL / setup internal ordering UNKNOWN
- rationale: UNKNOWN
- rejected alternatives: UNKNOWN
- GOLD: NOT YET ELIGIBLE because committed setup-prefix completeness has not been established

### DS-ASIS-003 — Drunk-as-Empath Night-1 information = 0

- decision family: impaired information
- observed choice: `0`
- evidence: `FRAG-ASIS-12-41-DRUNK-EMPATH`
- derivation: OBSERVED
- verification: VERIFIED
- explicit rationale: PRESENT — Ben says `2` would be less believable
- explicit rejected alternative: `2`
- unobserved alternative treatment: UNKNOWN for `1`
- committed prefix currently includes:
  - verified setup commitments above;
  - verified Chef delivery = `1` at 11:53
- GOLD: still pending the dedicated second verification / qualification gate rather than missing Chef-prefix data

This slice is already high-value positive expert evidence even before GOLD qualification because it preserves:

```text
expert chose 0
+ explicit choice-specific reason
+ explicit rejected alternative 2
!= claim that 1 or 2 are globally bad
```

### Fortune Teller remains an output event / decision candidate

The 15:18 primary fragment is now verified for:

- player choice: Tom + Elliott;
- delivered result: YES.

The reviewer notes that, given the reconstructed setup and normal game mechanics, the evident explanation is that Elliott's Recluse registered as Demon for this interaction.

Evidence Lab treatment remains deliberately split:

- the semantic player-action event is admitted;
- the YES delivery event is admitted;
- `Recluse-as-Demon` is stored only as an INFERRED reviewer interpretation;
- the source-observed historical registration witness remains UNKNOWN because Ben did not explicitly state it in the supplied primary review;
- promotion to a Storyteller DecisionSlice must not silently convert that inference into an OBSERVED witness.

## 7. Schema / workflow gaps exposed so far

These are findings from the real pilot, not frozen solutions.

### Gap A — research locator leads are not evidence assertions

Secondary indexes and prior D5F reconstruction are extremely useful for finding the right primary-video region.

They should not be forced into the evidence derivation enum.

Potential need:

- a lightweight non-corpus “research lead / locator note” concept; or
- an explicitly disposable acquisition notebook outside durable corpus export.

Do not add a persisted `ResearchLead` entity until the rest of E0 shows whether this recurs.

### Gap B — not every primary-video fact has a timestamp

Video title, source ID, description and publication metadata are primary evidence but are not timeline fragments.

The future EvidenceFragment locator needs to handle source metadata as well as timed media regions without inventing `00:00`.

### Gap C — edited video can establish partial temporal order

A setup fact may be provably committed before Night 1 while its exact position among other setup decisions remains unknown.

The durable model must not require a fabricated total order for facts whose exact ordering is not evidenced.

The existing architecture already helps by separating setup commitments from the ordered semantic event stream; E0 should test whether that is sufficient.

### Gap D — delivered output is not automatically a decision

The corpus can observe “Storyteller delivered X”.

It cannot automatically conclude “Storyteller freely chose X from alternatives” without either:

- explicit primary evidence; or
- downstream rules analysis.

This suggests the final model may need a clean distinction between a historical Storyteller-controlled delivery/event and a research-qualified decision slice.

Do not freeze that distinction until the primary Night-1 pass is complete.

### Gap E — decision actor may be uncertain in co-Storyteller productions

The source clearly identifies Ben as Storyteller in metadata, while secondary material also describes Adam as participating in Storyteller duties.

A decision slice may need:

- responsible Storyteller;
- co-Storyteller / assistant context;
- UNKNOWN actor when the source does not show which person committed a choice.

Do not attribute every setup choice to Ben merely because he is the named expert.

### Gap G — acquisition provenance is distinct from evidence provenance

The pilot now has three materially different things:

1. a primary-source locator;
2. secondary locator/reconstruction leads;
3. primary timed gameplay fragments (currently missing).

A future workflow must make it difficult to mistake “we found the primary URL” for “this gameplay fact was verified against the primary source”.

This may be a workflow-state concern rather than a new domain entity. Do not freeze a schema solution yet.

### Gap H — downstream compatible witnesses must not masquerade as historical witnesses

The legacy D5F case demonstrates the exact failure mode: a rules engine can prove that a visible result has only certain compatible registration explanations, while the historical source still does not tell us which witness the Storyteller actually used or conceptualized.

Evidence Lab therefore needs to preserve separately:

- observed delivered result;
- explicitly evidenced historical witness, if any;
- UNKNOWN historical witness otherwise.

Compatible/legal witness enumeration remains downstream.

### Gap I — setup decisions need a committed-prefix boundary too

The current architecture correctly says that authoritative history consists of:

- setup commitments; plus
- ordered semantic events.

However, the current conceptual `DecisionSlice` boundary is described mainly as an event-sequence boundary.

The A Stud pilot includes at least one high-value candidate decision that occurs during setup: the Drunk's shown identity (and potentially Red Herring / Demon bluffs).

A future decision-prefix contract must therefore be able to express:

- which setup commitments were already fixed;
- which setup commitment is the observed choice under study;
- which later setup commitments were not yet committed, when the source can establish that order;
- UNKNOWN internal ordering when an edited source cannot establish it.

Do not solve this by pretending setup commitments are ordinary Night-1 events solely to satisfy one sequence-number field.

### Gap J — compound source moments may contain player action, Storyteller commitment and delivery

A single short video region may show the Fortune Teller selecting two targets and then receiving a result.

The historical semantics are still distinct:

- player-controlled target commitment;
- possible Storyteller-controlled result commitment;
- information delivery.

Field/event-level provenance should allow several semantic assertions/events to cite the same or overlapping source fragment without collapsing them into one event.

### Gap K — evidence locator time and historical event time are different clocks

The human review exposed this directly.

For example:

- `09:49` is when the source establishes to the reviewer that Sullivan is the Drunk;
- the actual setup commitment necessarily existed earlier.

Therefore a future model must not overload one timestamp field to mean both:

1. **source locator time** — where evidence appears in the recording;
2. **historical semantic time/order** — when the game commitment/action actually occurred.

For edited/explanatory video, these can differ substantially.

The event model may use semantic ordering while provenance independently carries source timestamps.

Do not infer historical setup order from the order in which an edited video explains setup facts.

### Gap L — reviewer inference needs provenance separate from source observation

The first human review produced a useful example:

- primary source visibly supports Tom + Elliott -> YES;
- a knowledgeable reviewer can infer that Recluse-as-Demon is the mechanically evident explanation;
- the source itself did not explicitly state that historical registration witness.

Therefore the final workflow must preserve:

1. source-observed fact;
2. reviewer inference;
3. inference provenance / reviewer;
4. verification of the source fact;
5. explicit non-promotion of the inference to OBSERVED.

This is not the same as UNKNOWN: we may have a strong inference while still lacking direct historical witness evidence.

### Gap F — verification needs its own audit trail

Because AI extraction may propose evidence but human confirmation is required for VERIFIED/GOLD, E1 likely needs an auditable verification record rather than a bare boolean/status.

E0 should determine the minimum fields after the first human pass.

## 8. Draft export pressure — not a schema

The pilot currently requires these semantic groups:

```text
source
screening
source-locator fragment
historical assertion
setup commitment
semantic event
decision-slice candidate
verified decision slice
storyteller qualification evidence
verification record
```

This is only an inventory of observed needs.

Do not turn it into tables/classes/files until the E0 primary reconstruction and gap audit are complete.

## 9. Current completion state

- source record: STARTED
- screening: STARTED
- source-locator evidence: STARTED
- direct primary gameplay review: STARTED / HUMAN-REVIEWED
- primary timed evidence fragments: 4 timed fragments + 1 primary setup frame captured
- setup reconstruction: PRIMARY-SUPPORTED; exact internal commit order remains UNKNOWN
- ordered Night-1 timeline: PRIMARY-VERIFIED for the bounded Chef / Drunk-Empath / Fortune Teller interactions
- admitted decision slices: 3 (none GOLD-qualified yet)
- Chef delivery: VERIFIED = 1
- Fortune Teller historical registration witness: UNKNOWN at source-observation layer; Recluse-as-Demon retained only as INFERRED reviewer interpretation
- game context: beginner/new-player table VERIFIED by human primary review
- explicit rationale: PRESENT for Drunk-as-Empath 0
- explicit rejected alternative: PRESENT — 2 for the Drunk-as-Empath decision
- schema/workflow gap audit: STARTED
- draft export pressure: STARTED

The bounded E0 primary reconstruction is complete enough for the evidence-contract completion audit. Optional precision improvements may still be added later, but they are not required to justify E1.
