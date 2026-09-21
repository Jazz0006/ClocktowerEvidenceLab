# E0 Primary Review Packet — A Stud In Scarlet

> Status: ready for direct primary-video review
>
> Primary locator: https://www.youtube.com/watch?v=qZBvRfM3Xow
>
> Scope: capture only the minimum primary evidence needed to admit the first E0 decision slices.
>
> Do not transcribe the whole video. Do not infer missing facts. Do not use CampBoardGameHost legality to fill historical witnesses.

## 1. Reviewer objective

One bounded pass over setup + Night 1 should answer four evidence questions:

1. Was Sullivan actually committed as the Drunk and shown/believing Empath?
2. What information was delivered to Jon's Chef on Night 1?
3. What information was delivered to Sullivan-as-Empath on Night 1?
4. Which two players did Blair's Fortune Teller commit as targets, and what result was delivered?

A fifth question is conditional:

5. Does the primary source explicitly establish any interaction-local Recluse registration witness or Storyteller rationale?

If not, preserve UNKNOWN.

## 2. How to record timestamps

Use playback timestamps in `HH:MM:SS` or `MM:SS`.

For every captured fragment record:

- `start`;
- `end` when useful;
- who is visible/speaking;
- concise factual paraphrase;
- whether the fact is directly visible/audible;
- whether editing creates a gap before/after the fragment;
- optional extremely short quote only if needed to disambiguate the fact.

A timestamp is a source locator, not proof by itself. The note must say what the reviewer actually saw/heard.

## 3. Primary-review worksheet

### P1 — game / Storyteller / script identity

Purpose:

Confirm metadata that is currently reconstructed from public indexes rather than directly captured from the primary content.

Capture:

| Field | Value |
|---|---|
| timestamp/range | |
| Ben identified as Storyteller? | YES / NO / UNCLEAR |
| Adam identified as co-Storyteller/assistant? | YES / NO / UNCLEAR |
| script explicitly identified as Trouble Brewing? | YES / NO / UNCLEAR |
| evidence note | |
| derivation | OBSERVED / UNKNOWN |
| reviewer | |
| review date | |

Do not force these facts into a gameplay timestamp if they are only present in video metadata/title/description and the reviewer is checking that primary page directly.

### P2 — setup commitment: Drunk shown identity

This is the most important setup-prefix test.

Capture separate facts where possible:

| Field | Value |
|---|---|
| timestamp/range | |
| Sullivan actual role shown/established as Drunk? | YES / NO / UNCLEAR |
| Sullivan shown/believes Empath? | YES / NO / UNCLEAR |
| does the source show the Storyteller committing that shown identity? | YES / NO / UNCLEAR |
| actor committing the choice | Ben / Adam / joint / UNKNOWN |
| exact ordering relative to other setup commitments visible? | YES / NO |
| evidence note | |
| explicit rationale? | NONE / present — summarize briefly |
| explicit rejected alternative? | NONE / present — summarize briefly |

Admission rule:

- If the source establishes only that Sullivan is the Drunk and later believes Empath, this may support a reconstructed setup fact.
- It does **not** automatically establish which Storyteller personally selected Empath or the exact setup commitment order.
- Do not manufacture a setup event sequence when editing hides the order.

### P3 — Chef Night-1 delivery

Secondary locator lead:

- Jon is Chef;
- candidate delivered value = `1`.

Capture:

| Field | Value |
|---|---|
| timestamp/range | |
| Jon clearly identified as recipient? | YES / NO / UNCLEAR |
| delivered number | |
| delivery directly visible/audible? | YES / NO |
| Storyteller actor | Ben / Adam / joint / UNKNOWN |
| explicit registration statement? | NONE / present |
| exact historical registration witness, if explicit | |
| explicit rationale? | NONE / present |
| evidence note | |

Important:

A directly observed `Chef -> 1` supports an information-delivery event.

It does **not** by itself prove that `1` was a discretionary Storyteller choice. DecisionSlice admission must not depend on rules-engine alternative enumeration.

### P4 — Drunk-as-Empath Night-1 delivery

Secondary locator lead:

- Sullivan believes Empath;
- candidate delivered value = `0`;
- candidate alive-neighbour context = Luke + Jon.

Capture:

| Field | Value |
|---|---|
| timestamp/range | |
| recipient | |
| shown/believed ability | |
| visible neighbour context, if source exposes it | |
| delivered number | |
| delivery directly visible/audible? | YES / NO |
| Storyteller actor | Ben / Adam / joint / UNKNOWN |
| explicit statement that information is intentionally false/misleading? | YES / NO / UNCLEAR |
| explicit rationale? | NONE / present |
| rejected alternative? | NONE / present |
| evidence note | |

This is the strongest likely E0 decision candidate because impairment normally creates Storyteller information control, but Evidence Lab still records only the historical fact/rationale visible in the source.

Do not reconstruct a persistent fake world from one night.

### P5 — Fortune Teller player action

Secondary locator lead:

- Blair chooses Tom + Elliott.

This must be captured separately from the result.

| Field | Value |
|---|---|
| timestamp/range | |
| player actor | Blair / other / UNCLEAR |
| first selected target | |
| second selected target | |
| target pair clearly committed before result? | YES / NO / UNCLEAR |
| editing gap between action and result? | YES / NO |
| evidence note | |

If clear, this becomes a player-controlled `PLAYER_ACTION_COMMITTED` event in the decision-time prefix.

### P6 — Fortune Teller Storyteller output / delivery

Secondary locator lead:

- candidate result = YES.

Capture:

| Field | Value |
|---|---|
| timestamp/range | |
| delivered result | YES / NO / UNCLEAR |
| Storyteller actor | Ben / Adam / joint / UNKNOWN |
| result directly visible/audible? | YES / NO |
| source explicitly states Recluse registration? | YES / NO |
| if YES, exact source wording/action summarized | |
| explicit rationale? | NONE / present |
| explicit rejected alternative? | NONE / present |
| evidence note | |

Hard rule:

`Tom + Elliott -> YES` does **not** imply historical witness `Elliott registered as Demon`.

If the primary source does not explicitly establish the interaction-local registration, record:

`historical_registration_witness = UNKNOWN`

Downstream CampBoardGameHost may later derive compatible witnesses independently.

## 4. Decision-boundary worksheet

For every candidate Storyteller decision, write only the facts committed **before** the choice.

### D1 — Drunk shown identity

Potential boundary shape:

```text
known pre-commit setup facts
    ↓
[decision boundary]
    ↓
shown identity = Empath
    ↓
later setup commitments / Night 1
```

If exact setup commitment order is hidden by editing:

- record only the partial order that the source supports;
- keep unknown-before/unknown-after relationships UNKNOWN;
- do not assign artificial sequence numbers.

### D2 — Drunk Night-1 information

Potential boundary shape:

```text
setup commitments established before Night 1
+ prior Night-1 events that are evidenced as already committed
    ↓
[decision boundary]
    ↓
Drunk-as-Empath information commitment = 0
    ↓
delivery
```

Do not include later Fortune Teller targets/results or later game outcome.

### D3 — Fortune Teller output

Required boundary shape:

```text
setup commitments
+ prior Night-1 committed events
+ Blair target pair committed
    ↓
[decision boundary]
    ↓
Storyteller output commitment / historical result = YES
    ↓
delivery
```

The player target pair belongs in the prefix.

The YES result does not.

## 5. Evidence promotion rules

After direct review, classify each material claim independently.

### OBSERVED

Use when the primary video directly shows or audibly states the fact.

Examples:

- Blair visibly selects Tom and Elliott;
- a Storyteller directly signals YES;
- Sullivan is explicitly shown the Empath identity.

### RECONSTRUCTED

Use only when multiple primary fragments combine into a concrete historical fact.

Example:

- one fragment establishes Sullivan's actual Drunk token; another later fragment unambiguously establishes he believes Empath.

### INFERRED

Use for interpretations not actually established by primary evidence.

These should normally not be used to admit an E0 historical decision slice when the inference changes its context.

### UNKNOWN

Use whenever the primary source does not settle the field.

Expected likely UNKNOWN fields include:

- exact historical registration witness;
- exact Storyteller actor for a joint setup discussion;
- exact ordering of edited setup commitments;
- rejected alternatives;
- choice-specific rationale.

## 6. Verification pass

The extraction pass and verification pass are separate.

After filling P1–P6, a reviewer should replay each captured range and check:

1. timestamp is correct;
2. paraphrase says no more than the clip supports;
3. actor attribution is supported;
4. target identities are unambiguous;
5. player action and Storyteller output are not collapsed;
6. no downstream legality was imported;
7. no later game information appears in an earlier prefix;
8. registration witness remains UNKNOWN unless explicit;
9. rationale/rejected alternatives are recorded only when choice-specific.

Only then may a field/event move from `UNVERIFIED` to `VERIFIED`.

## 7. Minimum E0 admission target

The first direct-primary pass should attempt to admit these in order:

1. **Drunk shown identity** — if a genuine Storyteller setup commitment is primary-supported;
2. **Drunk Night-1 information** — expected high-value Storyteller-controlled information decision;
3. **Fortune Teller result after committed player targets** — if the source supports a Storyteller-controlled historical output boundary;
4. **Chef information** — retain as a verified delivery even if Evidence Lab cannot independently establish that it was a discretionary decision.

E0 succeeds on evidence quality, not by forcing all four into DecisionSlice.

If Chef is only an observed delivery, that is a useful schema result rather than a failure.

## 8. What to return to the pilot notebook

For each P1–P6 fragment, copy back only:

- source ID;
- timestamp/range;
- concise fact;
- derivation;
- verification;
- actor if supported;
- minimal rationale/rejected-alternative note if actually present.

Do not copy a long transcript.

The pilot notebook should then be updated with:

- verified setup commitments;
- ordered/partially ordered Night-1 semantic events;
- admitted DecisionSlices;
- unresolved UNKNOWNs;
- any additional schema/workflow gaps exposed by direct playback.
