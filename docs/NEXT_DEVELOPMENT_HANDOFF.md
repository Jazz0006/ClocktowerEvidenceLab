# NEXT DEVELOPMENT HANDOFF — C2 Podcast Batch Ingestion

> Current state: **C2 ACTIVE**
>
> Branch: `docs/podcast-batch-ingestion-route-20260929`
>
> Repository: `Jazz0006/ClocktowerEvidenceLab`

## 1. Read first

Read in this order:

1. `AGENTS.md`
2. `README.md`
3. `docs/ARCHITECTURE.md`
4. `docs/EVIDENCE_AND_PROVENANCE_STANDARD.md`
5. `docs/SOURCE_COLLECTION_STRATEGY.md`
6. `docs/TESTING_STRATEGY.md`
7. `docs/CURRENT_DEVELOPMENT_ROADMAP.md`
8. `docs/PODCAST_EXPERT_RATIONALE_ACQUISITION_WORKFLOW.md`
9. `docs/C2_TB_PODCAST_BATCH_INGESTION_2026-09-29.md`
10. this file

At the start of the next conversation, re-check live `main`, this branch, open PRs/checks and exact file state. Do not assume this handoff's branch status is still live.

## 2. Current baseline

C1 is complete and its targeted Drunk-assignment acquisition is stopped.

PR #7 consolidated durable work from the old podcast branch into main, including:

- RSS episode/audio/transcript locator parsing;
- optional faster-whisper ASR;
- timestamp normalization/tests;
- the podcast acquisition workflow;
- Drunk, Librarian and Recluse machine-located scout artifacts.

Those three episodes are prior-processed source identities for C2 and should not be needlessly retranscribed.

## 3. Current task

Implement **C2A — episode manifest** first.

Goal:

```text
live Cult of the Clocktower RSS
    -> reproducible episode inventory
    -> Trouble Brewing relevance
    -> stable identity
    -> acquisition/transcript/ASR/extraction/review status
    -> deduplicate previously processed episodes
```

Do not begin by manually listening to more episodes.

## 4. C2A minimum contract

The manifest should preserve at least:

- stable episode/source ID;
- show title;
- episode title;
- publication date;
- duration;
- webpage locator when available;
- enclosure/audio locator;
- advertised transcript status/locator;
- current Trouble Brewing scope classification;
- acquisition state;
- ASR state;
- extraction state;
- human-review state;
- optional link to retained prior scout artifact.

Prefer generic podcast/acquisition semantics rather than hard-coded per-role classes.

## 5. Required invariants

1. stable RSS identity deduplicates repeated feed reads;
2. already-processed episodes are recognized without relying only on title text;
3. full audio/transcript payloads are not written into Git-managed manifest artifacts;
4. missing transcript is a normal state that can trigger ASR;
5. ASR complete does not imply evidence VERIFIED;
6. extraction complete does not imply human review complete;
7. out-of-scope scripts can remain inventoried without entering the current processing queue;
8. a relevant episode may legitimately produce zero useful candidate windows.

## 6. Implementation sequence

```text
inspect retained acquisition code
    -> define manifest domain/serialization shape
    -> focused tests
    -> implementation
    -> live RSS enumeration
    -> dedup prior Drunk/Librarian/Recluse identities
    -> quality gate
    -> C2B batch acquisition
```

Use existing podcast tools rather than building a second downloader/transcriber.

## 7. Evidence boundary

Machine transcript/candidate extraction is acquisition assistance only.

Promotion requires primary-audio review confirming speaker, meaning, context and timestamp.

Keep full copyrighted audio/transcripts outside Git.

## 8. Do not do

- do not reopen broad C1 Drunk acquisition;
- do not switch back to quota-driven whole-game collection;
- do not implement BotC legality or policy scoring;
- do not add persistence migrations without a demonstrated batch-workflow need;
- do not make YouTube automation a prerequisite for C2;
- do not treat machine confidence as verification.

## 9. Historical documents

The pre-C2 roadmap/source-strategy/C1 handoff snapshots were moved under `docs/archive/` so they remain available for provenance without competing with the current authority.

Current authority is the C2 document set listed in section 1.
