# EL-LRE-MR1 — Mayor Redirect Targeted Acquisition — 2026-10-04

> Status: **PARTIAL VERIFIED-DIMENSION / TARGET-CLASS REVIEW READY**
>
> Repository: `Jazz0006/ClocktowerEvidenceLab`
>
> Family: Trouble Brewing Mayor night-death redirection.

## 1. Core finding

Mayor redirect should not be modeled as a generic `save Mayor` boolean or a global team-balance score.

The source-backed structure is a staged decision:

1. decide whether Mayor should survive this attack at all;
2. if redirecting, choose a target class whose death creates an appropriate amount and kind of consequence;
3. preserve player agency and avoid using Storyteller discretion to decide the winning team directly;
4. account for repeated Demon intent/history rather than treating every attack identically.

## 2. MR1-A — default is to preserve Mayor until final day

### Source

Official Blood on the Clocktower Wiki — Mayor:
https://wiki.bloodontheclocktower.com/Mayor

Official How-to-Run guidance explicitly recommends keeping Mayor alive until the final day because that creates the most enjoyable intended interaction.

It then gives a bounded exception: if the group becomes overwhelmingly convinced very early that the Mayor is genuine, allowing Mayor to die can restore Evil's ability to contest the game.

### Evidence semantics

- relation: **EXPLICIT_PREFERENCE + NAMED EXCEPTION**
- source type: **OFFICIAL_WRITTEN_GUIDANCE**
- verification: **DIRECT WRITTEN SOURCE**

### Host-facing predicate

`MAYOR_SURVIVAL_DEFAULT`

Positive direction:

- normally redirect rather than let Mayor die before the final day.

Exception feature:

- early hard-confirmation / overwhelming town certainty about Mayor identity.

### Boundary

This does not imply:

- Mayor must always survive;
- Storyteller should rescue Good whenever Good is losing;
- every Demon attack should be punished identically;
- a numeric trust threshold.

## 3. MR1-B — when Evil is clearly dominating, a Minion can be an appropriate redirect target

### Source

Official Blood on the Clocktower Wiki — Storyteller Advice:
https://wiki.bloodontheclocktower.com/Storyteller_Advice

The official advice gives a concrete state-sensitive Mayor example: when Evil is overwhelmingly ahead, if Mayor is attacked at night, the Storyteller may kill a Minion instead of a Townsfolk.

The same section warns against using discretionary rules to simply decide the winning team; the target is an interesting, earned game rather than direct balancing by fiat.

### Evidence semantics

- relation: **EXPLICIT CONDITIONAL PREFERENCE / POSITIVE OPTION**
- source type: **OFFICIAL_WRITTEN_GUIDANCE**
- verification: **DIRECT WRITTEN SOURCE**

### Host-facing predicate

`EVIL_DOMINANT_MINION_REDIRECT_OPTION`

Required context:

- Mayor is legitimately being attacked and redirect is legal;
- Evil is strongly ahead in the current state;
- at least one legal Minion redirect target exists.

Boundary:

- not a blanket kill-Minions-first policy;
- not permission for a generic losing-team rescue heuristic;
- do not redirect to the final Evil player merely to force an outcome.

## 4. MR1-C — no-death redirection is legal but not automatically desirable

### Source

Official Mayor page.

It explicitly states that if the Storyteller redirects the Mayor attack to a dead player, Soldier, or Monk-protected player, no player dies that night.

### Evidence semantics

- relation: **LEGAL_OPTION_TAXONOMY**
- verification: **DIRECT WRITTEN RULE SOURCE**
- preference status: **NONE**.

Host must preserve this as a legal outcome class, but EvidenceLab does not rank it above or below an actual death from the rules text alone.

## 5. MR1-D — official Ravenkeeper example

### Source

Official Mayor page.

Example: Imp attacks Mayor; Storyteller redirects the death to Ravenkeeper.

### Evidence semantics

- relation: **POSITIVE LEGAL EXAMPLE**
- source type: **OFFICIAL_WRITTEN_EXAMPLE**
- rationale: not stated in that example.

This establishes Ravenkeeper as an intended redirect target class but not a universal priority.

## 6. MR1-E — target classes from Mayor episode

### Source

`docs/C2_MACHINE_SEMANTIC_FINDINGS_TB_MAYOR_2026-10-04.md`, M02/M03.

Audio-ready machine understanding:

- default entertainment preference is usually to preserve Mayor and redirect;
- candidate target classes discussed include Minion, already-spent/lower-value Good, Ravenkeeper, Outsider, protected target, and sometimes high-value Good;
- target should vary with the live game state rather than a fixed ordering;
- if Evil has already lost both Minions / is badly behind, letting Mayor die or redirecting onto valuable Good can be reasonable;
- in less lopsided states, redirect to Evil, Ravenkeeper, Outsider or spent first-night role may be appropriate;
- protected target can be a comparatively neutral outcome.

Status: **MACHINE SEMANTIC / AUDIO-READY, NOT VERIFIED**.

Primary window: Mayor `00:54:14–00:58:19`.

## 7. MR1-F — repeated Mayor attacks depend on Demon intent

### Source

Mayor M04, `00:54:55–00:56:23`.

Machine understanding:

- repeated careless targeting after Demon has already learned the Mayor interaction can justify continued bounces;
- deliberate repeated targeting as a strategic investment may eventually justify letting Mayor die;
- therefore attack history / inferred intent matters.

Status: **MACHINE SEMANTIC / AUDIO-READY, NOT VERIFIED**.

This is important because it prevents a rigid `first attack bounce, second attack kill` rule.

## 8. MR1-G — Saint as a moderate-severity redirect target

### Source

`docs/C2_MACHINE_SEMANTIC_FINDINGS_TB_SAINT_E3_PASS_2026-10-03.md`, M03.

Window: `00:34:01–00:35:04`.

Machine comparison:

- killing Minion or Ravenkeeper is described as harsher for Evil;
- redirecting to Saint still helps Good because night-dead Saint becomes more credible;
- Saint is presented as a less swingy middle-severity target;
- appropriateness depends partly on whether Demon attack looked intentional or random.

Status: **MACHINE SEMANTIC / AUDIO-READY, NOT VERIFIED**.

## 9. MR1-H — Undertaker can be a high-value Good redirect when Good is far ahead

### Source

`docs/C2_MACHINE_SEMANTIC_FINDINGS_TB_UNDERTAKER_2026-10-04.md`, M05.

Window: `00:39:45–00:40:25`.

Machine understanding:

- Mayor + Undertaker can create a very strong Good information network;
- when Good is substantially ahead, redirecting Mayor attack onto Undertaker is proposed as reasonable;
- rationale is current team state plus Undertaker remaining utility, not a fixed Undertaker target preference.

Status: **MACHINE SEMANTIC / AUDIO-READY, NOT VERIFIED**.

## 10. MR1-I — redirecting onto Imp to force Scarlet Woman succession is a high-intervention special case

### Source

`docs/C2_MACHINE_SEMANTIC_FINDINGS_TB_SCARLET_WOMAN_2026-10-04.md`, M05.

Window: `00:53:11–00:54:31`.

Machine understanding:

- if Imp attacks Mayor, Storyteller can redirect the death onto Imp;
- Scarlet Woman may then become Demon;
- a possible rationale is that current Demon is nearly solved while Scarlet Woman has a better bluff;
- the speakers explicitly flag this as visibly interventionist / scale-tipping and group-tolerance sensitive.

Status: **MACHINE SEMANTIC / AUDIO-READY, NOT VERIFIED**.

This must remain a special intervention class, not ordinary Mayor redirect policy.

## 11. Mayor redirect target-class model

Evidence supports the following qualitative classes:

### A. Preserve Mayor / actual death elsewhere

Default intended interaction before final day.

### B. Evil-side redirect

Example: Minion when Evil is strongly ahead.

Potentially large pro-Good swing; use only under bounded state conditions.

### C. High-information Good redirect

Examples: Ravenkeeper, Undertaker.

Can preserve Mayor while removing a strong information asset.

### D. Spent / lower-value Good or Outsider

Lower intervention severity; may preserve game uncertainty without heavily swinging either side.

### E. Protected / dead / Soldier target

Legal no-death outcome class.

Legality is source-backed; preference requires additional evidence.

### F. Let Mayor die

Officially supported exception when Mayor is over-confirmed early; machine guidance adds possible Evil-behind / repeated strategic-investment contexts pending audio review.

### G. Force Demon succession

Imp redirect with Scarlet Woman present.

High-intervention special case; requires separate legitimacy predicate.

## 12. Required Host context

At minimum:

- Mayor attack is rule-legitimate;
- legal redirect targets;
- target alive/dead/protected state;
- target alignment / role / remaining utility;
- alive player count / final-day proximity;
- prior Mayor attacks by Demon;
- whether Demon likely knows Mayor;
- current public Mayor trust / confirmation;
- Minions alive / Evil remaining resources;
- succession consequences if target is Demon.

Optional / enrichment:

- current team pressure;
- player experience;
- group tolerance for visible Storyteller intervention.

Do not collapse these into one opaque balance score.

## 13. Current MR1 verdict

Mayor redirect is no longer merely READY-DIMENSION.

Already direct-written VERIFIED:

- keep Mayor alive until final day by default, with early overwhelming-confirmation exception;
- Evil-dominant state may justify Minion redirect instead of Townsfolk;
- protected/dead/Soldier target is a legal no-death class;
- Ravenkeeper is an official positive redirect example.

Audio-ready policy refinements:

1. Mayor `00:54:14–00:58:19` — target classes + state sensitivity;
2. Mayor `00:54:55–00:56:23` — repeated attack intent;
3. Saint `00:34:01–00:35:04` — moderate-severity target comparison;
4. Undertaker `00:39:45–00:40:25` — high-value Good redirect when Good ahead;
5. Scarlet Woman `00:53:11–00:54:31` — succession-forcing high-intervention special case.

The verified subset is sufficient for Host to model distinct redirect outcome classes and a narrow Mayor-survival default. It is not sufficient for a total target ranking or numeric balance algorithm.