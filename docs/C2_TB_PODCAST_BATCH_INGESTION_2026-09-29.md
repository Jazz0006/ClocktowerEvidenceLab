# C2 — Trouble Brewing Podcast Batch Ingestion — 2026-09-29

> Status: **ACTIVE — C2A COMPLETE / C2B COMPLETE / C2C COMPLETE / REAL TWO-EPISODE VALIDATION COMPLETE / C2D IMPLEMENTATION GREEN / HUMAN REVIEW QUEUE READY**
>
> Scope: `Cult of the Clocktower` expert audio relevant to the current Trouble Brewing-only product scope.
>
> Purpose: turn the successful one-episode podcast pilot into a repeatable, low-human-cost batch acquisition path.

## 1. Why C2 exists

The Drunk podcast pilot proved that a long expert episode with no feed-provided transcript can be processed through:

```text
public RSS
    -> stable episode/audio locator
    -> local ASR when needed
    -> timestamped machine transcript outside Git
    -> machine candidate extraction
    -> short human primary-audio review
    -> concise provenance-backed evidence
```

The pilot reduced a 2:27:27 episode to a small review packet and the reusable RSS/ASR tooling is now on main.

C2 scales that workflow across the remaining relevant Trouble Brewing episodes instead of continuing one episode at a time.

## 2. Product role

Podcast material is a complementary **expert-guidance / rationale corpus**.

It does not replace the project's whole-real-game corpus and it does not become replay evidence merely because a qualified expert speaks in it.

Use podcasts to discover and verify:

- Storyteller rationale;
- qualitative policy dimensions;
- concrete examples;
- explicitly contrasted alternatives;
- player-experience considerations;
- setup-level reasoning;
- misinformation / registration / bluff principles.

Whole-game evidence remains necessary for historical replay and committed-prefix reconstruction.

## 3. C2 batch scope

### C2A — episode manifest — COMPLETE / GREEN

A machine-readable manifest from the live public RSS feed is implemented.

The manifest must preserve stable identity and current acquisition state for every Trouble Brewing-relevant episode.

At minimum record:

- show;
- episode title;
- RSS GUID;
- publication date;
- duration;
- webpage locator when available;
- audio enclosure locator;
- advertised transcript locator/status;
- Trouble Brewing relevance;
- acquisition status;
- ASR status;
- extraction status;
- human-review status.

Do not hard-code the series inventory when the RSS can be enumerated.

Already processed/scouted material must be recognized by stable source identity and not needlessly retranscribed. Current known processed episodes include the Drunk, Librarian and Recluse scouts retained from the earlier pilot.

### C2B — batch acquisition — IMPLEMENTATION COMPLETE / GREEN

The repository now provides a tested resumable batch planner/runner and CLI. For remaining relevant episodes:

1. use feed-advertised transcript when available as a locator aid;
2. otherwise acquire the public audio outside Git;
3. run timestamped ASR;
4. keep full audio/transcript outside Git;
5. persist only lightweight machine acquisition metadata in repository artifacts.

Do not commit copyrighted full audio or full transcript text.

Implementation completion means the workflow can perform these operations; it does **not** mean the remaining live episodes have already been transcribed, reviewed or promoted. Real multi-episode execution remains part of C2 validation.

### C2C — structured candidate extraction — IMPLEMENTATION COMPLETE / GREEN

The repository now provides a deterministic timestamp-preserving extractor and CLI over external ASR segments. It searches for high-value Storyteller material while keeping complete transcript text outside Git-managed candidate artifacts. Rationale matching supports adjacent ASR segments and overlapping matches are merged into bounded review windows.

A bounded real two-episode C2B -> C2C validation has completed successfully for Investigator and Imp. The run exercised live RSS discovery, public audio acquisition, ASR and lightweight candidate extraction while keeping full audio/transcripts outside Git.

Initial target categories:

```text
STORYTELLER_DECISION
STORYTELLER_RATIONALE
SETUP_LEVEL_REASONING
MISINFORMATION_POLICY
REGISTRATION_CHOICE
DEMON_BLUFF_REASONING
PLAYER_EXPERIENCE
PLAYER_AGENCY
INFORMATION_STRENGTH
CONFIRMATION_CHAIN
LONGITUDINAL_TRAJECTORY
EXPLICIT_ALTERNATIVE
REAL_GAME_EXAMPLE
```

The extractor must preserve timestamps and distinguish:

- machine transcript text;
- machine interpretation;
- source-observed/verified evidence.

No machine-generated paraphrase is automatically VERIFIED evidence.

### C2D — relevance ranking and bounded human review — IMPLEMENTATION GREEN / HUMAN REVIEW PENDING

The deterministic review-packet domain, writer and CLI are implemented:

- nearby/overlapping candidates can be merged into one bounded listen window;
- P0/P1/P2 are acquisition-review priorities only, never Storyteller decision-quality labels;
- window-count and total-review-time budgets are explicit;
- review packets retain machine summaries/tags/confidence without transcript bodies;
- `clocktower-podcast-review` converts a C2C candidate artifact into a bounded C2D packet;
- human review remains NOT_STARTED until a person actually reviews the primary source.

The full Install / Ruff check / Ruff format / pytest gate is GREEN at quality #284.

The successful bounded Investigator/Imp run #4 artifacts were reused directly; no audio was retranscribed:

- run ID: `36574401873`;
- Investigator artifact ID: `11038036661`, source `podcast:90e5895f9886d0d14325f829f548182a`;
- Imp artifact ID: `11037392096`, source `podcast:1a7eb4d86b3f2a42b6693356f20c0253`;
- Investigator packet: 12 selected windows / 16 selected candidate hits / 127.32 seconds;
- Imp packet: 12 selected windows / 17 selected candidate hits / 258.28 seconds;
- combined review queue: 24 windows / 385.60 seconds (6m25.6s).

Both generated packets remain `human_review_state=NOT_STARTED`. The durable per-window queue is `docs/C2D_PRIMARY_AUDIO_REVIEW_QUEUE_2026-09-30.md`. The next operation is bounded primary-audio review of these windows; C2E promotion must wait for that human confirmation.

Human review should focus on this small packet rather than either full episode.

High-value current topics include:

- which Townsfolk is selected as Drunk;
- explicit comparison/rejection among possible Drunk candidates under one fixed setup;
- conditional Drunk preferences whose conditions can be reconstructed at assignment time;
- persistent Drunk misinformation across nights;
- healthy-information strength;
- Spy/Recluse registration intent;
- Demon bluff selection;
- whole-setup information topology;
- beginner / experienced-player differences;
- respecting player-controlled choices;
- examples where experts explicitly compare opposite legal choices.

### C2C/C2D targeted enhancement for C3

CampBoardGameHost has identified a narrow downstream evidence gap: explicit comparison or rejection among Drunk candidates under the same fixed setup/history prefix.

C3 reuses this C2 pipeline and does not interrupt batch ingestion. The existing `EXPLICIT_ALTERNATIVE` category already has P0 C2D review priority, so no new ranking subsystem is needed. C2C only expands conservative locator coverage for explicit rejection, explicit preference and conditional Drunk-assignment expressions.

Machine matches remain unverified acquisition assistance. See `docs/C3_DRUNK_CANDIDATE_COMPARISON_EVIDENCE_2026-09-30.md`.

### C2E — promotion into durable evidence

Only after primary-audio review:

- confirm speaker attribution;
- confirm timestamp/range;
- confirm intended meaning and context;
- save concise paraphrase;
- preserve derivation and verification state;
- link to stable source identity.

Full transcript remains an acquisition artifact outside Git.

## 4. Automation boundary

C2 aims to automate **discovery, download/locator handling, ASR, candidate extraction and prioritization**.

Human review remains the promotion gate for evidence used as verified expert guidance.

Desired state:

```text
hours of source audio
    -> minutes of targeted review
```

Do not optimize for zero human review if doing so weakens provenance.

## 5. Relationship to YouTube/video work

C2 is the current task because podcast acquisition is already proven and stable.

A future video route may use direct multimodal video understanding or other acquisition tooling, but it is not required to complete C2.

The two routes should eventually converge on a common candidate/evidence schema:

```text
Podcast RSS/audio -> ASR ---------┐
                                  ├-> candidate extractor -> review -> Evidence Lab
Video source -> multimodal ingest ┘
```

Do not block the podcast batch on YouTube automation.

## 6. Implementation order

```text
C2A manifest
    -> C2B batch acquisition
    -> C2C structured extraction
    -> C2D relevance/review packets
    -> C2E verified evidence promotion
```

Use tests-first for stable machine-readable contracts and pure transformations.

Do not add persistence migrations unless the batch workflow proves the current lightweight acquisition artifacts are insufficient.

## 7. C2 success criteria

C2 is complete for the current checkpoint when:

1. the relevant Trouble Brewing podcast inventory is reproducibly enumerated;
2. already-processed episodes are deduplicated by stable identity;
3. remaining relevant episodes can be batch acquired/transcribed without committing full media/transcripts;
4. structured candidate extraction returns timestamped rationale/example windows;
5. review packets reduce human listening effort substantially;
6. at least one multi-episode batch has been human-reviewed and promoted into concise provenance-backed expert guidance;
7. current Host-facing evidence gaps are mapped to the new corpus without converting expert guidance into policy verdicts.

The success metric is not raw transcript volume. It is **high-value verified guidance per minute of human review**.
