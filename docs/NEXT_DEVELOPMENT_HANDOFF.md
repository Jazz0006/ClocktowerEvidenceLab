# NEXT DEVELOPMENT HANDOFF — C2 + EL-LRE Replacement-Policy Evidence

> Current state: **C2 ACTIVE / EL-LRE0 AUDIT COMPLETE / C3 STAGE-1 HISTORICAL-SUPPORTING / EL-TBGS-0/1 ACCEPTED / EL-ML0 ACCEPTED**
>
> Repository: `Jazz0006/ClocktowerEvidenceLab`
>
> Re-check live branch / HEAD / working tree / PR state at the start of the next conversation.

## 1. Read first

1. `AGENTS.md`
2. `README.md`
3. `docs/CURRENT_DEVELOPMENT_ROADMAP.md`
4. `docs/EL_LRE_REPLACEMENT_POLICY_EVIDENCE_ALIGNMENT_2026-10-04.md`
5. `docs/ML_RECOMMENDATION_EVIDENCE_READINESS_CONTRACT_2026-10-03.md`
6. `docs/C2_TB_PODCAST_BATCH_INGESTION_2026-09-29.md`
7. `docs/PODCAST_EXPERT_RATIONALE_ACQUISITION_WORKFLOW.md`
8. `docs/C3_DRUNK_CANDIDATE_COMPARISON_EVIDENCE_2026-09-30.md`
9. this file

The detailed pre-LRE C5/E3 continuation snapshot is archived at:
`docs/archive/PRE_LRE_NEXT_DEVELOPMENT_HANDOFF_2026-10-04.md`.

## 2. Current authority

EvidenceLab now operates two complementary lanes:

```text
C2 automatic podcast semantic collection
        +
Host LRE bounded evidence requests
```

C2 remains the acquisition engine. EL-LRE controls Host-facing triage.

Host's production replacement invariant is:

```text
one legal result
    -> RULE_DETERMINISTIC

multiple legal results + accepted versioned policy
    -> POLICY_READY

multiple legal results + no mature policy
    -> MANUAL_REQUIRED / POLICY_DEFERRED
```

EvidenceLab does not own legality, candidate enumeration, scoring, policy versioning, replay, or cutover.

## 3. Required evidence semantics

Keep these distinct:

```text
OBSERVED_CHOICE
EXPLICIT_PREFERENCE
EXPLICIT_REJECTION
EXPLICIT_COMPARISON_LOSER
LEGAL_UNCHOSEN
SYNTHETIC_NEGATIVE
```

Only the first four may be source-backed EvidenceLab relations.

`LEGAL_UNCHOSEN` is downstream Host enrichment. It must never be silently reclassified as rejection.

`SYNTHETIC_NEGATIVE` is downstream dataset/evaluation material and is never historical evidence.

## 4. Current task

Continue C2 automatic semantic collection without changing its ingestion architecture, while using the EL-LRE priority matrix to select bounded primary-audio reviews.

Do not reopen broad Drunk acquisition.

Do not resume broad E3/C5 hunting as a general objective.

Do not implement recommendation policy in EvidenceLab.

## 5. Immediate bounded review target

### EL-LRE-WW1 — healthy Washerwoman target-selection dimensions

Source:
`11: Washerwoman (Trouble Brewing) - With Official Storyteller Reggie Collins!`

Review these windows:

- `00:43:09–00:43:52` — avoid over-confirming Mayor;
- `00:43:53–00:45:22` — preference for targets that benefit from trusted information routing / credibility support;
- `00:46:39–00:47:55` — Drunk-exclusion / confidence amplification;
- `00:52:51–00:53:42` — anti-meta decoy-category variation.

Promotion target:

```text
explicit preference/rejection
+ condition
+ rationale
+ speaker
+ timestamp
+ bounded scope
+ VERIFIED
```

This is generic policy-dimension evidence. Do not infer a complete Washerwoman ranking and do not enumerate legal candidates inside EvidenceLab.

## 6. Current family priority

### Priority 1

1. Washerwoman
2. Investigator
3. Demon bluffs
4. Red Herring

### Priority 2

- Drunk / Poisoned information;
- Chef;
- Empath;
- Fortune Teller;
- Washerwoman;
- Librarian;
- Investigator;
- Undertaker;
- Ravenkeeper;
- other controllable misinformation.

### Priority 3

- Spy / Recluse registration;
- Mayor redirect;
- Demon succession.

For the family-by-family evidence/gap/review/reconstruction/Host-enrichment matrix, use:
`docs/EL_LRE_REPLACEMENT_POLICY_EVIDENCE_ALIGNMENT_2026-10-04.md`.

## 7. Strongest already-located LRE leads

After EL-LRE-WW1, the strongest bounded targets are:

1. **Investigator pair construction**
   - Empath `00:38:47–00:39:20`;
   - Recluse `01:06:54–01:08:37`.

2. **Poisoned Fortune Teller**
   - Poisoner `01:09:31–01:13:29`;
   - real `YES` vs `NO` choice with explicit rationale and later retrospective update.

3. **Impaired Washerwoman**
   - Washerwoman `00:48:53–00:50:10`;
   - bluff-compatible misinformation vs obviously broken misinformation that exposes poisoning.

4. **Spy / Recluse registration**
   - rich machine-only comparison material already exists in the Spy and Recluse findings.

5. **Mayor redirect**
   - Mayor `00:54:14–00:58:19`;
   - Saint `00:34:01–00:35:04`.

## 8. Already-consumed / historical evidence

- C3 Q04 remains VERIFIED and historically important, but C3 is no longer the general active evidence lane.
- Broad Drunk scouting remains closed.
- G10 functioning-Librarian evidence has already been consumed by Host's functioning Librarian V2 route; it remains corpus evidence rather than a current blocker.
- EL-TBGS-0/1 remains accepted.
- EL-ML0 remains accepted; no new schema migration is authorized by EL-LRE0.
- Existing C5/E3 finding documents remain useful historical records and locator sources, but they no longer define global continuation priority.

## 9. C2 operational boundary

Continue:

```text
prepare-next
-> complete ASR outside Git
-> full-transcript semantic review
-> lightweight findings
-> LRE-aware triage
-> targeted primary-audio verification where useful
-> cleanup-current
-> repeat
```

Machine output remains NOT VERIFIED until primary-audio promotion.

Full audio and full transcripts remain outside Git.

## 10. When to reconstruct more history

Invest in whole-game reconstruction when:

- an observed historical choice is close to policy-authorizing evidence;
- the exact pre-decision state changes the interpretation;
- Host wants exact replay/evaluation;
- legal-domain enrichment requires a precise historical prefix.

Do not reconstruct a whole game merely to turn generic expert guidance into a historical case.

## 11. Do not do

- do not implement Host recommendation policies;
- do not add BotC legality;
- do not enumerate legal candidates;
- do not create GOOD/BAD labels;
- do not convert legal-unchosen alternatives into rejection evidence;
- do not reopen broad Drunk acquisition;
- do not restart broad C5/E3 hunting;
- do not add SQLite/Alembic migration for EL-LRE0;
- do not redesign EL-ML0;
- do not stop C2 automatic semantic collection.
