# C3 — Drunk Candidate Comparison / Rejection Evidence — 2026-09-30

> Status: **STAGE-1 ACCEPTED / HISTORICAL SUPPORTING LANE — OPERATIONAL PRIORITY SUPERSEDED BY EL-LRE**
>
> Cross-project source: `Jazz0006/CampBoardGameHost` Drunk-assignment production cutover gate audit; current continuation authority is `docs/EL_LRE_REPLACEMENT_POLICY_EVIDENCE_ALIGNMENT_2026-10-04.md`.
>
> Scope: narrow evidence acquisition for **comparative Drunk-assignment reasoning after the setup/history prefix is fixed**. This lane does not replace or interrupt C2 Podcast Batch Ingestion.

## 1. Why C3 exists

CampBoardGameHost completed the Drunk-assignment execution infrastructure needed for production evaluation, including the legal candidate domain, hypothetical projection, DecisionTrace/replay, and Experienced-mode manual selection. C3 was opened because the remaining Beginner automatic-assignment blocker was evidential rather than infrastructural.

That Stage-1 gap is now closed by human-verified Q04, and Host has since cut over `DRUNK_ASSIGNMENT_Q04_V1`. C3 remains historical/supporting evidence for comparative Drunk guidance, but new bounded Host evidence requests are routed through EL-LRE and C2 rather than reopening C3 as a separate active program.

This does **not** reopen broad Drunk scouting. The continuing target is not “games containing a Drunk”; it is evidence that says why candidate A was preferred to, compared with, or rejected relative to candidate B under a reconstructable assignment-time context.

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
- trusted expert / Storyteller source provenance;
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

The historical choice, explicit alternatives, and explicit rationale are evidence. Policy interpretation remains downstream. Snapshot interoperability is likewise a transport/projection concern, not a policy or quality label.

## 6. C2C / C2D reuse audit

The existing semantic category `EXPLICIT_ALTERNATIVE` is sufficient for C3 comparative/rejection discovery and is already P0 in C2D review triage.

The identified gap is lexical coverage, not schema ownership. C2C therefore adds conservative locator rules for:

- explicit rejection language;
- explicit preference language;
- conditional Drunk-assignment language that does not necessarily say “Storyteller”.

These rules still produce machine candidates only. C2D continues to treat `EXPLICIT_ALTERNATIVE` as P0 acquisition-review priority; no Storyteller choice score is introduced.

## 7. Stage-1 acceptance condition

For `Cult of the Clocktower`, the project owner accepts the host and episode guests as trusted expert/Storyteller clue sources; do not require a separate creator/official title for C3 source qualification. C3 Stage 1 succeeds when at least one item is **human-verified from primary audio** with all of:

```text
fixed setup/history prefix
+ candidate A vs candidate B
+ explicit preference or rejection
+ source-backed rationale
+ reconstructable assignment-time context
```

Sample count is not the gate.

C3 Stage 1 is now **SATISFIED** by human-verified Q04 from `12: Monk (Trouble Brewing)`, `00:43:28–00:44:30`. The accepted handoff is bounded to the source-described conditional preference and is recorded in `docs/C3_Q04_VERIFIED_MONK_CONDITIONAL_PREFERENCE_HANDOFF_2026-10-02.md`. CampBoardGameHost may now evaluate a first bounded, versioned Drunk production-policy predicate and rerun its production cutover gate. The standard snapshot remains the transport boundary; do not broaden Q04 into a global ranking or manufacture missing historical state.

## 8. Retrospective audit of existing C1 evidence

Before acquiring new material, C3 re-audited the already human-reviewed C1 Drunk-assignment evidence.

Result: **no existing VERIFIED C1 item satisfies the C3 Stage-1 comparison gate**.

- `A Stud In Scarlet`: fixed prefix and selected Drunk are VERIFIED, but assignment rationale is UNKNOWN and no alternative Drunk candidate was discussed.
- `A Fond Farewell`: fixed prefix + selected Chef + explicit assignment rationale are VERIFIED, but the review explicitly records `explicit alternative Drunk candidates: NONE OBSERVED`. Surrounding Recluse / Scarlet Woman / Traveler discussion must not be reclassified as rejected Drunk candidates.
- G10 Game 2: fixed prefix + selected Empath + explicit adjacency-to-Demon rationale are VERIFIED, but the review explicitly records `explicitly considered/rejected alternative Drunk candidates: NONE OBSERVED`.
- Steven Medway 01:28:18–01:29:18: VERIFIED creator guidance distinguishes player-first, role-first and setup-first assignment modes, but it does not compare candidate A with candidate B under one assignment context.

Therefore C3 must acquire/verify genuinely comparative material rather than reinterpret C1 selections as rankings.

The strongest retained machine-located lead is the Steven Medway Drunk episode around `02:04:10–02:07:39`, where beginner/expert handling appears to contrast Monk/Soldier-like Drunk assignments with Ravenkeeper-like assignments. This remains **NOT VERIFIED for C3** until primary-audio review confirms the exact comparison, speaker, condition and rationale.

The original targeted review queue is preserved as historical acquisition context at `docs/archive/C3_DRUNK_CANDIDATE_REVIEW_QUEUE_2026-09-30.md`; its embedded next-action instructions are superseded by Q04 acceptance and the current EL-LRE route.

## 9. Relationship to EL-LRE

The earlier C5 / `BEGINNER_CONSERVATIVE_V2` continuation wording is historical and no longer controls EvidenceLab priority.

EL-LRE generalizes C3's reusable lesson:

```text
bounded context
+ source-backed candidate A
+ explicit candidate B / rejection / comparison loser
+ rationale
+ conditions
+ provenance / verification
```

C3-Q04 remains a valid VERIFIED evidence item. Future Drunk evidence should enter through ordinary C2 collection or a new bounded EL-LRE Host request. Do not reopen broad Drunk scouting, and do not reinterpret downstream legal-but-unchosen candidates as source-backed rejection evidence.
