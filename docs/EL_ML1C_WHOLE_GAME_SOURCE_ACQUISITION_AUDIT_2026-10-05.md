# EL-ML1C — Whole-Game Source Acquisition Audit

> Date: 2026-10-05  
> Status: **AUDIT COMPLETE / PILOT CONTRACT ACCEPTED / EXECUTION DEFERRED UNTIL EL-ML1B REPAIR GATE**  
> Scope: Trouble Brewing first

## 1. Why this audit exists

EL-ML1A established that the scarce asset for future model-backed Storyteller recommendation is not another isolated principle. It is an independent, leak-free historical decision state embedded in a reconstructable real game.

EL-ML1B therefore remains the current implementation route: repair and canonicalize already-known whole-game evidence before acquiring more games.

EL-ML1C answers the next acquisition question in advance:

> If EL-ML1B repair cannot reach the 20–30 READY pilot target, which external sources can add complete games with the least human effort and the strongest provenance?

This audit does **not** authorize broad scraping, a new persistence schema, a cloud crawler, a new rules engine, or automatic VERIFIED promotion.

## 2. Required acquisition shape

The primary collection unit is one reconstructable real game.

A high-value source should help recover as much as possible of:

```text
source identity
+ Storyteller identity / independence key
+ script / player count / date
+ complete initial seating and actual/shown roles
+ setup commitments
+ Demon bluffs
+ ordered night/day boundaries
+ player-controlled actions
+ Storyteller-controlled outputs
+ deaths / executions / state transitions
+ explicit Storyteller rationale when present
+ final outcome
+ field/event-level provenance
```

A source need not supply all fields itself. Cross-source joins are explicitly allowed when each claim keeps its own provenance.

## 3. Source classes

### 3.1 ClockTracker public games — Tier A for structured historical scaffolding

Observed public capabilities:

- ClockTracker advertises more than 161k recorded games and supports full grimoires, notes and images.
- Public game pages can expose script, date, player count, Storyteller, result, Demon bluffs, final grimoire and free-form notes.
- At least one public Trouble Brewing record contains a near-complete chronological game log in Notes, including setup, Night 1 through Night 7, player actions, Storyteller information, deaths, executions and Demon succession.
- The open-source application fetches public games with final grimoire/token data.
- The application also implements `GrimoireSnapshot` history, but snapshots are created when an owner saves/edits a game and the snapshot endpoint is owner-authenticated. They must **not** be treated as a public semantic gameplay event stream.

Representative public record:

- `https://clocktracker.app/game/ffb40a93-3d7b-42c4-bba8-bc9c363dcd30`

Upstream implementation:

- `https://github.com/lindsaykwardell/clocktracker`

Assessment:

```text
discovery automation       HIGH
final setup/grimoire       HIGH when recorded
ordered trajectory         VARIABLE; can be EXCELLENT when Notes are detailed
Storyteller rationale      LOW–MEDIUM
public bulk API certainty  LOW; do not assume
human verification need    LOW–MEDIUM for detailed records
```

Important conclusion:

ClockTracker should be screened first for complete-game candidates, but quality must be measured per game. A game with only a final grimoire is scaffolding, not a full trajectory.

### 3.2 Storyteller-POV YouTube video — Tier A for trajectory and rationale

A Storyteller-perspective video can expose the missing semantics that a static record often cannot:

- exact night/day ordering;
- grimoire changes;
- information shown;
- Storyteller-controlled decisions;
- spoken alternatives and rationale;
- table/social context;
- Grim Reveal.

A representative Trouble Brewing Storyteller-perspective video publishes explicit chapters for Night 1, every later night/day transition, Final Three and Grim Reveal:

- `https://www.youtube.com/watch?v=VEKA7ntQGmk`

Assessment:

```text
discovery automation       HIGH
initial setup recovery     MEDIUM–HIGH
ordered trajectory         HIGH
Storyteller rationale      MEDIUM–HIGH
machine extraction cost    MEDIUM–HIGH
human verification need    MEDIUM, concentrated on ambiguity
```

Preferred automated pipeline:

```text
video discovery
-> Storyteller-POV / full-game classifier
-> chapters / timestamp segmentation
-> temporary ASR outside Git
-> bounded visual key-frame extraction
-> setup / state / decision candidate reconstruction
-> cross-check audio, visible grimoire and rules-independent temporal consistency
-> confidence routing
-> targeted human verification only for ambiguous/high-value decisions
```

Copyright boundary remains unchanged: do not commit full video, full audio or long transcript reproductions.

### 3.3 Online grimoire / game-log systems — Tier B now, potentially Tier A+

Several open-source tools can produce machine-native state:

#### `mwc34/botc`

Publicly advertises:

- day/night phases;
- nomination tracking;
- interactive night actions;
- toggleable log tracking;
- grimoire reveal.

Repository:

- `https://github.com/mwc34/botc`

Code inspection shows the visible game log is retained in browser `sessionStorage`. This is useful evidence that event-like data exists during play, but it is not yet evidence of a durable public historical export.

#### `vkluna/grimlive`

Publicly advertises:

- integrated game tracking;
- starting roles;
- final roles;
- win/loss stats;
- Discord attribution;
- a read API described as "coming soon".

Repository:

- `https://github.com/vkluna/grimlive`

This is promising for future structured acquisition but should not be depended on until a stable read/export interface is actually available.

#### Other live grimoire implementations

Current community projects commonly track role assignment, reminders, alignment, death state, day/night state and live sessions. That does not automatically mean they preserve an immutable historical event log.

Assessment:

```text
discovery automation       MEDIUM
machine-readable state     HIGH
durable event history      UNKNOWN / project-dependent
public historical corpus   LOW today
future partnership value   VERY HIGH
```

Policy:

Do not build scraper-specific integrations against undocumented internal endpoints yet. First prefer an explicit read/export contract or maintainer-approved interface.

### 3.4 Twitch / streamed Storyteller POV — Tier B

Semantically similar to YouTube Storyteller POV and can use the same reconstruction model.

Main disadvantages:

- VOD retention/availability is less stable;
- chaptering and long-term identifiers may be weaker;
- discovery/deduplication is less predictable.

Use when a high-value game is available, but do not make Twitch the first corpus-growth dependency.

### 3.5 Actual-play podcasts — Tier C for complete-game reconstruction

Advantages:

- ASR can be highly automated;
- complete games may be available;
- spoken decisions can be rich.

Disadvantages:

- no visible grimoire;
- seating/state recovery is often incomplete;
- speaker/action attribution can be harder;
- silent Storyteller choices may be unrecoverable.

Use mainly when the episode itself supplies unusually complete state narration or when paired with a structured game record.

### 3.6 Expert role / Storyteller podcasts — supporting rationale lane

The exhausted Trouble Brewing podcast queue remains valuable as expert semantic evidence.

It is no longer the default marginal acquisition path for the global-recommendation objective.

Use it to explain, qualify or compare decisions found in whole games, or to fill a bounded benchmark gap.

### 3.7 EvidenceLab / Host-native telemetry — future highest-fidelity source

For games run through a consenting future Host workflow, the ideal evidence can be captured directly:

```text
canonical pre-decision Game State
-> legal-domain owner remains Host
-> Storyteller chosen action
-> resulting state
-> next decision
-> optional bounded rationale
```

This would eliminate most visual reconstruction.

It remains deferred because the current EvidenceLab external-source scope and consent/privacy model do not yet authorize broad direct telemetry ingestion.

## 4. Highest-value acquisition pattern: cross-source joining

The strongest practical near-term case is often not one perfect source but:

```text
ClockTracker record
    + Storyteller-POV video
    + optional expert/post-game commentary
```

ClockTracker can provide structured historical scaffolding and a final grimoire.

Video can provide exact chronology, visible state transitions and rationale.

The join must never collapse provenance. Every reconstructed field/event retains the source fragment that supports it.

Cross-source agreement is a confidence signal, not permission to invent missing chronology.

## 5. Automation levels

EL-ML1C freezes the following workflow levels as operational concepts, not new persisted evidence enums:

### A0 — automated discovery

Machine identifies candidate games and records source URL/platform/basic metadata.

No evidence claim is created.

### A1 — automated source screening

Machine evaluates:

- complete game vs clip;
- Trouble Brewing vs other script;
- Storyteller POV / grimoire visibility;
- likely Storyteller identity;
- presence of notes/chapters/Grim Reveal;
- likely source duplication.

Output remains an acquisition candidate.

### A2 — machine reconstruction draft

Machine attempts:

- setup map;
- ordered phase boundaries;
- semantic events;
- Storyteller decisions;
- rationale candidates;
- provenance anchors.

All reconstructed fields remain machine-derived and UNVERIFIED.

### A3 — automated consistency gate

Rules-independent checks may include:

- stable seat identity;
- monotonic phase/event ordering;
- no event after its own claimed decision boundary;
- source timestamps in range;
- setup count consistency with the source;
- cross-source contradictions surfaced rather than resolved by guessing.

BotC legality and legal-candidate enumeration remain downstream Host responsibilities.

### A4 — targeted human verification

Human review is required only for:

- ambiguous or contradictory facts;
- important Storyteller-controlled decisions;
- candidate GOLD/benchmark decisions;
- uncertain attribution;
- sampled QA.

Goal:

> Human review should become exception/acceptance work, not full-game transcription work.

## 6. Source-acquisition scorecard

Every candidate source/game pilot should measure:

| Metric | Meaning |
| --- | --- |
| setup completeness | Can initial seat/actual/shown-role state be recovered? |
| chronology completeness | Are phase boundaries and event order recoverable? |
| ST-decision recovery | Can Storyteller-controlled choices be located? |
| rationale recovery | Are reasons/alternatives stated? |
| provenance precision | Can facts be anchored to timestamp, note line/block or structured field? |
| Storyteller independence | Can the Storyteller/grouping key be retained without guessing? |
| automation yield | Fraction recovered without human intervention |
| ambiguity load | Number of fields/decisions needing review |
| source stability | Are URLs/identifiers likely to remain usable? |
| rights/privacy fit | Can metadata/paraphrase/provenance be retained under project policy? |

## 7. Pilot contract

The first acquisition pilot, if triggered, should stay bounded and Trouble-Brewing-first.

### Batch CT-1 — ClockTracker

Screen at least 25 public Trouble Brewing game records.

Prefer:

- recorded Storyteller identity;
- full grimoire;
- detailed Notes;
- independent Storytellers not already dominant in the corpus.

Measure:

- percentage with complete initial layout;
- percentage with usable chronological Notes;
- number of recoverable Storyteller decisions per game;
- later-game/history-sensitive decision yield.

Do not attempt authenticated/private snapshot harvesting.

### Batch YT-1 — Storyteller POV video

Screen 10 complete Trouble Brewing Storyteller-POV videos across at least 4 Storyteller independence groups where possible.

Prefer:

- visible grimoire;
- explicit night/day chapters;
- Grim Reveal;
- clear Storyteller narration;
- no heavy edit that removes night decisions.

For 3 representative games, run A0–A3 reconstruction before asking for broad human review.

### Batch DG-1 — digital grimoire/log capability

Audit at least 3 current public/open-source grimoire systems for:

- durable historical event storage;
- explicit export/read API;
- stable identifiers;
- permission/privacy model;
- setup/final-state vs true event-stream distinction.

Do not implement an integration until one source exposes a stable, permitted export/read contract.

## 8. Candidate admission gate

A newly acquired game should not enter the canonical whole-game reconstruction backlog merely because it is interesting.

Preferred admission requires:

1. stable public source identity;
2. Storyteller identity or explicit uncertainty that can be retained;
3. recoverable initial setup/seating at useful completeness;
4. enough ordered history to materialize at least several real decision prefixes;
5. at least one Storyteller-controlled decision with precise provenance;
6. no need to invent chronology or registration witnesses;
7. useful independence or later-game coverage relative to the existing corpus.

A final grimoire with no recoverable chronology may be retained as a source candidate but is not by itself a benchmark trajectory.

## 9. Execution order relative to EL-ML1B

EL-ML1C does **not** pre-empt current repair work.

Accepted route:

```text
EL-ML1B existing-corpus repair/materialization
    -> count READY historical decisions
    -> if 20–30 target is reached with required diversity:
         no broad new acquisition yet
    -> if target remains below 20 or independence/later-game mix is weak:
         run EL-ML1C CT-1 + YT-1 + DG-1 pilot
         -> compare automation yield
         -> choose acquisition lane
         -> acquire only the number of new whole games needed
```

This preserves the higher marginal value of already-known evidence while preventing future source collection from falling back to ad-hoc video hunting.

## 10. Current audit conclusion

```text
PRIMARY NEAR-TERM SOURCE:
    ClockTracker public complete-game records
    especially detailed chronological Notes

PRIMARY TRAJECTORY COMPLEMENT:
    Storyteller-POV YouTube video

HIGHEST-VALUE JOIN:
    ClockTracker + matching Storyteller-POV video

PROMISING FUTURE STRUCTURED SOURCE:
    explicit digital-grimoire event export / read API

SUPPORTING SOURCE:
    Twitch / actual-play audio

RATIONALE-ONLY DEFAULT:
    expert role / Storyteller podcast

AUTO VERIFIED FROM MACHINE OUTPUT:
    NO

AUTO DISCOVERY / SCREENING / DRAFT RECONSTRUCTION:
    YES — desired default

BROAD NEW INGESTION NOW:
    NO — finish EL-ML1B repair gate first
```

## 11. Evidence for this audit

External capability observations were checked on 2026-10-05 against:

- ClockTracker public site and public Trouble Brewing game pages;
- ClockTracker open-source server/reconstruction code;
- `mwc34/botc` open-source log implementation;
- `vkluna/grimlive` public README;
- a chaptered Trouble Brewing Storyteller-perspective YouTube game.

These observations describe source capabilities. They are not themselves canonical Blood on the Clocktower game evidence.
