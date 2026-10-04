# EL-LRE-SR1 — Spy / Recluse Registration Targeted Acquisition — 2026-10-04

> Status: **PARTIAL VERIFIED-DIMENSION / CONDITIONAL REGISTRATION PARTITION READY**
>
> Repository: `Jazz0006/ClocktowerEvidenceLab`
>
> Family: Spy / Recluse discretionary registration across Trouble Brewing information roles.

## 1. Core finding

The Spy/Recluse problem should not be represented as one global probability or one fixed `register Good` / `register Evil` default.

The evidence already supports multiple distinct Storyteller intents whose preferred registration can point in opposite directions:

- preserve enough healthy information for Good to reason with;
- reduce over-compression when one clue would expose too much;
- support an established Evil bluff;
- preserve Evil deniability while retaining some true information;
- create a socially difficult truthful result;
- preserve future anti-meta ambiguity;
- adapt registration to the exact world-model consequences of the current game.

The correct Host abstraction is therefore a **scope-partitioned registration policy family**, not a scalar Good/Evil registration rate.

## 2. SR1-A — Recluse / Chef over-compression avoidance

### Source

Official Blood on the Clocktower Wiki — Recluse:
https://wiki.bloodontheclocktower.com/Recluse

Official example:

- Recluse neighbours the Imp and an Evil Traveller;
- if Recluse registered as Evil to Chef, the resulting Chef information could expose too much;
- because a high result would be too revealing, the example instead has Chef learn a truthful `0`.

### Evidence semantics

- relation: **EXPLICIT_PREFERENCE**
- source type: **OFFICIAL_WRITTEN_GUIDANCE / EXAMPLE**
- verification: **DIRECT WRITTEN SOURCE**
- condition: Recluse registration would otherwise create a highly revealing Chef result;
- preferred direction: avoid the high-compression registration and preserve a less-revealing truthful Chef result.

### Host-facing predicate

`RECLUSE_CHEF_OVERCOMPRESSION_AVOIDANCE`

Candidate feature dimensions:

- projected Chef number;
- world compression / adjacent-Evil exposure;
- whether the alternative result remains mechanically truthful;
- existing information density.

### Boundary

This does not imply:

- always make Recluse Good to Chef;
- always prefer Chef 0;
- lower Chef numbers are globally better;
- a numeric threshold for when a Chef result becomes too strong.

## 3. SR1-B — Spy bluff-support registration

### Source

Official Blood on the Clocktower Wiki — Storyteller Advice:
https://wiki.bloodontheclocktower.com/Storyteller_Advice

When a Spy is actively bluffing a Good role and an information ability can legally see that Spy as the bluff role, the official guidance explicitly recommends supporting that bluff. The concrete example is Spy bluffing Fortune Teller and being selected by Ravenkeeper.

### Evidence semantics

- relation: **EXPLICIT_PREFERENCE**
- source type: **OFFICIAL_WRITTEN_GUIDANCE**
- verification: **DIRECT WRITTEN SOURCE**
- already recorded as RK1-A; SR1 references it because it is a registration-policy predicate.

### Host-facing predicate

`SPY_ACTIVE_BLUFF_SUPPORT`

Required context:

- target is Spy;
- active Good bluff is known to Storyteller;
- requested registration can legally match that bluff;
- no stronger scope-specific policy overrides it.

Boundary: no global rule to always register Spy as Good.

## 4. SR1-C — Investigator + Recluse under excessive Good information pressure

### Source

`docs/EL_LRE_INV1_INVESTIGATOR_PAIR_CONSTRUCTION_VERIFIED_HANDOFF_2026-10-04.md`

Primary-audio VERIFIED:

- when Good already has unusually strong information, including the explicit Empath-between-two-Evil example, Investigator may be routed through Recluse rather than exposing the real Minion;
- this uses Recluse registration to reduce compounding Good information.

### Evidence semantics

- relation: **EXPLICIT_PREFERENCE**
- verification: **PRIMARY-AUDIO VERIFIED**
- policy intent: information-budget / Minion-concealment.

### Boundary

This does not establish a universal Recluse-as-Minion default. The opposite real-Minion + Recluse construction is also source-supported for a different intent.

## 5. SR1-D — real Minion + Recluse as truthful deniability

### Source

`docs/EL_LRE_INV1_INVESTIGATOR_PAIR_CONSTRUCTION_VERIFIED_HANDOFF_2026-10-04.md`

Primary-audio VERIFIED bounded design option:

- Investigator can be shown the real Minion plus Recluse;
- after Recluse becomes known, town may attribute the Minion ping to Recluse registration and discount the real Minion;
- truthful information can therefore preserve Evil deniability.

### Evidence semantics

- relation: **BOUNDED POSITIVE DESIGN OPTION / RATIONALE**
- verification: **PRIMARY-AUDIO VERIFIED**
- no source-backed ordering between SR1-C and SR1-D.

The two constructions must remain separate conditional intents.

## 6. SR1-E — Undertaker / Recluse registration is world-model dependent

### Source

`docs/C2_MACHINE_SEMANTIC_FINDINGS_TB_RECLUSE_2026-10-04.md`, M10

Primary-audio VERIFIED:

- after Recluse is executed, showing Spy, Imp, or another legal role can alter different live worlds;
- Spy can reopen doubt around trustworthy players;
- Imp can imply Scarlet Woman and change Baron / Poisoner deductions;
- the source explicitly treats this as state-dependent rather than a fixed token ordering.

### Evidence semantics

- relation: **EXPLICIT STATE-DEPENDENT GUIDANCE**
- verification: **PRIMARY-AUDIO VERIFIED**
- no fixed Spy-vs-Imp ranking.

### Host-facing requirement

The policy requires current world-model / prior-information context, not only executed role and legal token domain.

## 7. SR1-F — truthful Spy display can itself be socially misleading

### Source

`docs/C2_MACHINE_SEMANTIC_FINDINGS_TB_SPY_2026-10-03.md`, M09

Primary-audio VERIFIED historical choice:

- Spy was bluffing Investigator and publicly accusing another player;
- after Spy was executed, Storyteller showed the actual Spy token to the real Undertaker;
- rationale: mechanically correct information created a difficult social puzzle because the Undertaker was already under suspicion.

### Evidence semantics

- relation: **OBSERVED_CHOICE + EXPLICIT_RATIONALE**
- verification: **PRIMARY-AUDIO VERIFIED**
- alternate token was not explicitly discussed, so this is not a pairwise comparison.

Policy dimension: `truth_as_misinformation / social_believability`.

## 8. SR1-G — truthful registration precedent has anti-meta value

### Source

`docs/C2_MACHINE_SEMANTIC_FINDINGS_TB_SPY_2026-10-03.md`, M10

Primary-audio VERIFIED descriptive dimension:

- occasionally showing Spy truthfully to a healthy Undertaker can establish precedent;
- later identical-looking information from a Drunk / poisoned Undertaker becomes harder to solve by Storyteller meta.

### Evidence semantics

- verification: **PRIMARY-AUDIO VERIFIED**
- relation: **DESCRIPTIVE POLICY DIMENSION**, not an explicit default preference.

Do not convert anti-meta value into a fixed frequency.

## 9. Official legality and multi-registration semantics

Official Spy / Recluse pages independently establish that registration can differ between abilities and even within the same night.

Examples include:

- Spy registering Evil to Chef and Good to Empath later the same night;
- Recluse changing registration across different information interactions;
- Undertaker / Investigator / Slayer examples with role-specific registration.

This verifies that Host must model registration per interaction, not as one persistent binary state.

These examples establish legality / representation semantics, not preference rankings.

## 10. Highest-value audio-ready predicates

The following machine-semantic findings are the strongest remaining promotion targets.

### SR1-H — Recluse / Empath: avoid `2` when it instantly exposes the adjacent Evil player

Source window: Recluse `01:04:57–01:06:17`.

Machine understanding:

- Empath sits between Recluse and actual Evil;
- `2` can overexpose Evil and undermine the Outsider burden / Evil-player agency;
- proposed alternative is `1`;
- after Evil neighbour dies, continuing `1` may preserve uncertainty.

Status: **MACHINE SEMANTIC / AUDIO-READY, NOT VERIFIED**.

This is the top remaining primary-audio target because it contains explicit `2` vs `1` output comparison and longitudinal rationale.

### SR1-I — Spy / Empath: Good registration is a tendency, topology can reverse it

Source window: Spy `01:49:40–01:50:24`.

Machine understanding:

- guest says Spy registers Good to Empath more often than not;
- when Spy + Imp both neighbour a sober Empath, alternative legal registrations can be interesting;
- exact neighbourhood consequences should control the choice.

Status: **MACHINE SEMANTIC / AUDIO-READY, NOT VERIFIED**.

Do not promote 'more often than not' to numeric probability.

### SR1-J — Recluse / Librarian: trust support versus concealment

Source window: Recluse `01:10:21–01:11:39`.

Machine understanding:

- showing Recluse can help a genuine Recluse survive an execute-Recluse local meta;
- opposite option: show `0` Outsiders to conceal Recluse existence and preserve ambiguity;
- the two directions serve different intents.

Status: **MACHINE SEMANTIC / AUDIO-READY, NOT VERIFIED**.

### SR1-K — Spy registration should preserve a usable information ecology

Source window: Spy `01:43:27–01:46:20`.

Machine understanding:

- do not contaminate every Good information source when Good already has little reliable information;
- stronger Good information setup gives more room for Spy misinformation;
- goal is enough meaningful information for deduction, not maximum deception.

Status: **MACHINE SEMANTIC / AUDIO-READY, NOT VERIFIED**.

## 11. Registration intent partition

Evidence currently supports this conceptual partition:

1. `INFORMATION_ECOLOGY_PRESERVATION`
   - avoid making every information channel unreliable;
   - SR1-K needs audio verification.

2. `OVERCOMPRESSION_AVOIDANCE`
   - reduce a registration result that would reveal too much;
   - SR1-A VERIFIED official Chef example;
   - SR1-H Empath variant is audio-ready.

3. `ACTIVE_BLUFF_SUPPORT`
   - match Spy registration to an established Good bluff;
   - SR1-B VERIFIED official guidance.

4. `EVIL_DENIABILITY_WITH_TRUE_SIGNAL`
   - retain real information while providing an alternate registration explanation;
   - SR1-D VERIFIED bounded option.

5. `WORLD_MODEL_DISRUPTION`
   - choose legal Recluse role registration according to current deduction consequences;
   - SR1-E VERIFIED.

6. `TRUTH_AS_MISINFORMATION`
   - truthful Spy display can be hard to believe under the public narrative;
   - SR1-F VERIFIED historical evidence.

7. `ANTI_META_FUTURE_FLEXIBILITY`
   - occasional truthful precedent can preserve ambiguity in later impaired results;
   - SR1-G VERIFIED descriptive dimension only.

8. `TRUST_SUPPORT_VS_CONCEALMENT`
   - registration may deliberately strengthen a Recluse claim or conceal it;
   - SR1-J requires audio verification.

## 12. Host-facing boundary

Host must not implement:

- `Spy register Good = 90%`;
- `Recluse register Evil = default`;
- one global registration score independent of target ability;
- a generic 'help losing team' switch.

Host should instead request a typed registration decision with:

- registering character (Spy / Recluse);
- detecting / affected ability;
- target ability's exact legal registration domain;
- current game phase / alive count;
- information topology and prior public information;
- known Evil bluff when source-backed;
- relevant player-experience enrichment only where evidence supports it;
- candidate-specific downstream world consequences.

## 13. Current SR1 verdict

Spy/Recluse registration is no longer merely a machine-only Priority-3 lead.

Already VERIFIED:

- official Recluse/Chef over-compression avoidance;
- official Spy active-bluff support;
- Investigator/Recluse strong-Good-info concealment;
- Investigator real-Minion + Recluse truthful deniability option;
- Undertaker/Recluse state-dependent role registration;
- historical truthful Spy/Undertaker social-puzzle choice;
- truthful-registration anti-meta dimension.

Still audio-ready:

- Recluse/Empath `2` vs `1`;
- Spy/Empath Good-vs-Evil tendency under exact adjacency;
- Recluse/Librarian trust support vs concealment;
- Spy whole-setup information-ecology guidance.

The next best EvidenceLab action is bounded primary-audio verification of SR1-H, then SR1-I, SR1-J and SR1-K. Even before those reviews, the verified subset is sufficient to reject any universal registration default and to support narrow Host predicates for Chef, active Spy bluff support, Investigator and Undertaker contexts.