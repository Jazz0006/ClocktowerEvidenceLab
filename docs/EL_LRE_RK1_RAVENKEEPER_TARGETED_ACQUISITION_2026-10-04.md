# EL-LRE-RK1 — Ravenkeeper Misinformation / Registration Targeted Acquisition — 2026-10-04

> Status: **PARTIAL VERIFIED-DIMENSION / TARGETED PRIMARY-AUDIO REVIEW READY**
>
> Repository: `Jazz0006/ClocktowerEvidenceLab`
>
> Family: Ravenkeeper information / Spy registration / impaired Ravenkeeper misinformation

## 1. Acquisition result

The previous gap was an explicit source-backed A-vs-B misinformation / registration comparison.

This targeted pass found three complementary evidence shapes:

1. **official written Storyteller guidance** directly recommending bluff-supporting Spy registration when a Ravenkeeper chooses that Spy;
2. **expert public transcript guidance** giving opposite healthy-Ravenkeeper outputs for the same Spy interaction at different game stages;
3. **real-game impaired Ravenkeeper examples** showing false role information as part of a broader false world.

The fixed Cult of the Clocktower feed remains exhausted. This pass deliberately admits a targeted external expert source rather than reopening broad feed traversal.

## 2. RK1-A — Spy bluff-support registration

### Source

Official Blood on the Clocktower Wiki — Storyteller Advice:
https://wiki.bloodontheclocktower.com/Storyteller_Advice

The relevant official guidance says that when a Spy is bluffing Fortune Teller and is chosen by the Ravenkeeper, the Storyteller should use the Spy's legal Good registration to support the Fortune Teller bluff.

### Evidence semantics

- relation: **EXPLICIT_PREFERENCE**
- source type: **OFFICIAL_WRITTEN_GUIDANCE**
- verification status: **VERIFIED FROM DIRECT WRITTEN SOURCE**
- preferred action: support the Spy's active Good bluff when that registration is legal and known;
- direct Spy exposure is the unchosen comparison in this stated bluff-support condition;
- other unmentioned Good registrations remain **LEGAL_UNCHOSEN**, not source-backed rejection.

### Bounded policy dimension

**bluff_support_registration**

Required context:

- chosen target is the Spy;
- Spy's active public / communicated Good bluff is known to the Storyteller;
- that bluff is a legal registration;
- Ravenkeeper information is functioning sufficiently for registration-based truthful information.

Boundary: this does not authorize always hiding Spy, inventing an unestablished bluff, or a complete Good-role registration ranking.

## 3. RK1-B — healthy Ravenkeeper Spy output changes with game stage

### Source

Clocktower Academy — `Ravenkeeper (TB) w/ Beardy`

Published: 2026-03-27

Host: Dylan DeAngelis

Guest: Beardy / Beardy Does Clocktower

Public transcript:
https://www.listennotes.com/podcasts/clocktower-academy/ravenkeeper-tb-w-beardy-wQl6i4IEDqG/

This source was already admitted in the earlier C0 rationale scout as `EXPERT_GUIDANCE_WITH_GAME_EXAMPLES`.

### Transcript-confirmed comparison

The public transcript gives the same Ravenkeeper -> Spy interaction under two different game stages:

- early / Night 2: showing the Spy's current bluff may be appropriate to support Evil;
- near Final 3: directly showing Spy may be appropriate.

The speaker explicitly frames the choice as situation-dependent rather than a fixed registration rule and scopes it to a sober / healthy Ravenkeeper.

### Evidence semantics

- relation: **EXPLICIT_CONDITIONAL_PREFERENCE**
- source type: **EXPERT_GUIDANCE_WITH_GAME_EXAMPLES**
- transcript status: **PUBLIC TRANSCRIPT CONFIRMED**
- primary-audio status: **NOT YET HUMAN-VERIFIED**
- production promotion: **PENDING PRIMARY-AUDIO REVIEW**

Same legal interaction:

- candidate A: Spy registers as current Good bluff;
- candidate B: Spy registers as Spy;
- early-game direction: A may be preferable;
- near-Final-3 direction: B may be preferable.

Supported dimensions:

- game phase / alive-player compression;
- Evil-cover preservation;
- confirmation-chain strength;
- information swing severity;
- active Spy bluff;
- Ravenkeeper reliability.

This is the exact A/B evidence shape that was previously missing from the Ravenkeeper family. It argues against both fixed policies: always show Spy and always show bluff.

Do not mark RK1-B VERIFIED until primary audio confirms speaker identity, exact early-vs-late condition, recommendation strength, healthy/sober scope, and nearby qualifiers.

## 4. RK1-C — impaired Ravenkeeper false information can fit a coherent false world

### Source A — TPI published real-game example

The Pandemonium Institute — `Blood on the Clocktower is a Strategy Game`:
https://bloodontheclocktower.com/blogs/news/blood-on-the-clocktower-is-a-strategy-game

The article presents a simplified version of a real game the author Storytold:

- Ravenkeeper is poisoned when killed;
- Ravenkeeper chooses the Imp;
- Ravenkeeper is shown Mayor;
- other false information coheres around a Scarlet Woman rather than Poisoner world;
- the article explicitly notes that Storyteller choices determined what false information players learned.

Disposition:

- relation: **OBSERVED_CHOICE**
- source type: **PUBLISHED_EXPERT_REAL_GAME_EXAMPLE**
- status: **DIRECT WRITTEN SOURCE / SUPPORTING**
- strict same-state candidate comparison: **NO** — rejected legal role-token alternatives are not enumerated.

### Source B — existing EvidenceLab whole-game reconstruction

`docs/C0_TB_RECONSTRUCTION_BATCH_01_2026-09-23.md` retains another impaired chain:

Poisoner targets Ravenkeeper -> Imp kills Ravenkeeper -> Ravenkeeper chooses Imp -> Ravenkeeper is shown Slayer.

This is an observed impaired-output example, not a source-backed ranking.

### Source C — Clocktower Academy anecdotes

The Ravenkeeper episode also gives real-game anecdotes where an impaired Ravenkeeper is shown a false Evil role on a Good target and that Good player is executed. These establish severity / exploitability, but not an exact A-vs-B Storyteller rationale.

Supported dimensions:

- impaired Ravenkeeper information is high-impact;
- output should be evaluated against current false-world / public-claim context;
- role-token choice can redirect execution;
- misinformation coherence matters.

These examples do not establish a preferred false role token, an always-show-Evil rule, or numeric misinformation strength.

## 5. RK1 package disposition

### Immediately usable verified dimension

**RK1-A — bluff-support Spy registration**

Host may consume this as a narrow source-backed predicate after mapping its own legal domain and canonical bluff state.

### Primary-audio promotion target

**RK1-B — game-stage-sensitive Spy reveal vs bluff-support**

The public transcript does not expose stable audio timestamps. Do not fabricate timestamps. Resolve exact audio timing during primary-audio review.

### Supporting-only historical dimension

**RK1-C — impaired false-world coherence**

Useful for replay / evaluation, but insufficient to rank false role tokens without same-state alternatives and rationale.

## 6. Host-facing mapping proposal

### Predicate A — ACTIVE_SPY_BLUFF_SUPPORT

chosen target is Spy + functioning Ravenkeeper + active Good Spy bluff known + bluff registration legal -> bluff-support registration is evidence-backed.

Authority: RK1-A.

### Predicate B — LATE_GAME_SPY_EXPOSURE

chosen target is Spy + functioning Ravenkeeper + near Final 3 -> direct Spy exposure may outrank bluff preservation.

Authority: RK1-B **only after primary-audio verification**.

### Predicate C — IMPAIRED_NARRATIVE_COHERENCE

Ravenkeeper impaired -> evaluate false output against current public world / established bluff narrative.

Authority: supporting dimension only; no complete selector authorized.

## 7. Required context for future Host policy

At minimum:

- Ravenkeeper reliability;
- chosen target actual role;
- whether target is Spy / Recluse;
- active target bluff / public claim known to Storyteller;
- game stage / alive count / Final-3 proximity;
- relevant confirmation-chain structure;
- prior public information that the result would strengthen or break.

Optional enrichment:

- current team pressure;
- player experience;
- local meta.

Do not make optional enrichment mandatory unless later evidence requires it.

## 8. Current verdict

Ravenkeeper is no longer correctly described as merely **SUPPORTING / SPARSE**.

- RK1-A official written bluff-support registration -> **VERIFIED-DIMENSION**;
- RK1-B early-vs-late Spy A/B comparison -> **READY FOR PRIMARY-AUDIO VERIFICATION**;
- RK1-C impaired-output historical examples -> **SUPPORTING**.

This is still not a complete Ravenkeeper ranking policy.

The next best EvidenceLab action is bounded primary-audio review of RK1-B. If it verifies as transcribed, Ravenkeeper becomes a strong Host-ready conditional registration family rather than a sparse evidence gap.