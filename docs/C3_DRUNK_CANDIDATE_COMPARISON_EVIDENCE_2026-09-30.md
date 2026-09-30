# C3 — Drunk Candidate Comparison / Rejection Evidence — 2026-09-30

> Status: **ACTIVE TARGETED EVIDENCE LANE — REUSES C2**
>
> Cross-project source: `Jazz0006/CampBoardGameHost` Drunk-assignment production cutover gate audit.
>
> Scope: narrow evidence acquisition for **comparative Drunk-assignment reasoning after the setup/history prefix is fixed**. This lane does not replace or interrupt C2 Podcast Batch Ingestion.

## 1. Why C3 exists

CampBoardGameHost has completed the Drunk-assignment execution infrastructure needed for production evaluation, including the legal candidate domain, hypothetical projection, DecisionTrace/replay, and Experienced-mode manual selection.

The remaining Beginner automatic-assignment blocker is evidential rather than infrastructural: the Host does not yet have source-backed semantics for ranking or rejecting one legal Drunk candidate relative to another in the same fixed setup.

Evidence Lab must therefore search for explicit comparative evidence without inventing downstream policy.

This does **not** reopen broad Drunk scouting. The target is not “games containing a Drunk”; it is evidence that says why candidate A was preferred to, compared with, or rejected relative to candidate B under a reconstructable assignment-time context.

## 2. Acquisition route

C3 reuses the existing C2 acquisition path:

```text
RSS / public audio
    -> ASR outside Git
    -> C2C candidate extraction
    -> C2D bounded review packet
    -> human primary-audio verification
    -> verified evidence
```

No second ingestion stack, persistence subsystem, recommendation engine, or BotC legality layer should be created for C3.

C2 batch acquisition continues normally. C3 only adds a targeted review lane over material already flowing through C2.

## 3. Priority evidence shapes

Search in this order:

1. a qualified Storyteller explicitly compares two or more Townsfolk candidates after the full setup/history prefix is fixed;
2. an explicit rejection, for example “I would not make X drunk here because …”, together with a recoverable final selection;
3. a conditional preference, for example “if condition C holds, I prefer candidate A …”, where condition C can be reconstructed from assignment-time context;
4. an explicit case where player experience changes which candidate is selected or rejected;
5. an explicit tradeoff between strong first-night misinformation and a credible multi-night misinformation narrative.

An observed final selection without explicit comparison/rejection does not satisfy C3.

## 4. Minimum evidence record

Each promoted C3 comparison must preserve, as evidence permits:

- assignment-time setup/history prefix;
- observed selected candidate;
- explicitly compared or rejected alternatives;
- concise source-backed rationale;
- the assignment-time context actually invoked by that rationale;
- Storyteller / creator provenance;
- primary-source timestamp or timestamp range;
- derivation and verification state.

Candidates that the source does not explicitly compare remain `UNKNOWN`.

Evidence Lab records only alternatives that the source actually mentions. It does not enumerate the legal candidate set.

## 5. Interpretation boundaries

Strictly prohibited:

- inferring that choosing A means A ranked above every unmentioned candidate;
- inferring a general Drunk rule from one game outcome;
- promoting ASR, keyword extraction, or machine summaries directly to VERIFIED;
- encoding CampBoardGameHost legality or recommendation scoring in Evidence Lab;
- treating a C3 comparison as a GOOD/BAD label;
- stopping C2 automatic batch ingestion to perform C3;
- reopening broad C1-style “find games with a Drunk” scouting.

The historical choice, explicit alternatives, and explicit rationale are evidence. Policy interpretation remains downstream.

## 6. C2C / C2D reuse audit

The existing semantic category `EXPLICIT_ALTERNATIVE` is sufficient for C3 comparative/rejection discovery and is already P0 in C2D review triage.

The identified gap is lexical coverage, not schema ownership. C2C therefore adds conservative locator rules for:

- explicit rejection language;
- explicit preference language;
- conditional Drunk-assignment language that does not necessarily say “Storyteller”.

These rules still produce machine candidates only. C2D continues to treat `EXPLICIT_ALTERNATIVE` as P0 acquisition-review priority; no Storyteller choice score is introduced.

## 7. Stage-1 acceptance condition

C3 Stage 1 succeeds when at least one item is **human-verified from primary audio** with all of:

```text
fixed setup/history prefix
+ candidate A vs candidate B
+ explicit preference or rejection
+ source-backed rationale
+ reconstructable assignment-time context
```

Sample count is not the gate.

As soon as the first qualifying evidence item is VERIFIED, prepare an EvidenceLab -> CampBoardGameHost handoff containing only the evidence/provenance needed for the Host to evaluate a first bounded, versioned Drunk production-policy predicate and rerun its production cutover gate.

## 8. Relationship to C5

C5 / `BEGINNER_CONSERVATIVE_V2` is a separate evidence and policy gate.

Do not mix C3 Drunk-assignment comparison evidence with the broader C5 policy program. C3 exists only to close the current Drunk-assignment production evidence gap.
