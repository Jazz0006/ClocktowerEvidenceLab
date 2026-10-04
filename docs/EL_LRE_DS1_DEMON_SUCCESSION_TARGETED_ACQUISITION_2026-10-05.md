# EL-LRE-DS1 — Demon Succession Control-Boundary & Targeted Acquisition — 2026-10-05

> Status: **CONTROL BOUNDARY VERIFIED / SUCCESSOR-SELECTION EVIDENCE PARTIAL**
>
> Repository: `Jazz0006/ClocktowerEvidenceLab`
>
> Family: Trouble Brewing Imp self-kill / Star Pass / Scarlet Woman succession / Storyteller-induced Demon transition.

## 1. Why this family must be split before ranking

`Demon succession` is not one decision.

Trouble Brewing contains several different control modes:

1. the Imp choosing to kill itself;
2. the Storyteller selecting which alive Minion receives the Imp when ordinary Star Pass applies;
3. the Scarlet Woman automatically becoming the Imp when her ability applies;
4. the Storyteller indirectly causing Demon death through another discretionary effect such as Mayor redirection;
5. exotic registration interactions such as Recluse being treated as a relevant evil character during the transition.

Only some of these are recommendation decisions owned by the Storyteller.

## 2. DS1-A — Imp self-kill trigger is player-controlled

### Source

Official Blood on the Clocktower Wiki — Imp:
https://wiki.bloodontheclocktower.com/Imp

The Imp ability explicitly lets the Imp choose a player to die each night, including itself. If the Imp kills itself this way, succession occurs.

### Evidence semantics

- control owner: **PLAYER / IMP**
- relation: **RULE DETERMINISTIC AFTER PLAYER ACTION**
- Host recommendation ownership: **NONE for the self-kill trigger itself**

Host may model predicted / inferred Imp intent as context, but must not treat `should the Imp star pass?` as a Storyteller recommendation decision.

## 3. DS1-B — ordinary Star Pass successor selection is Storyteller-controlled

### Source

Official Imp How-to-Run guidance:

- after an Imp kills itself, the Storyteller chooses an alive Minion;
- that Minion's token is replaced with an Imp token and the new Imp is informed.

### Evidence semantics

- control owner: **STORYTELLER**
- decision family: **SUCCESSOR_SELECTION**
- legal domain: alive Minions eligible under current rules/state;
- recommendation relevance: **YES** when more than one legal Minion exists and no stronger forced rule determines the successor.

This is the actual Host recommendation problem inside ordinary Star Pass.

## 4. DS1-C — healthy Scarlet Woman can remove successor discretion

### Source

Official Blood on the Clocktower Wiki — Scarlet Woman:
https://wiki.bloodontheclocktower.com/Scarlet_Woman

Direct rule:

- if five or more non-Traveller players are alive when the Demon dies, Scarlet Woman becomes that Demon;
- if the Imp self-kills at night under that condition, Scarlet Woman **must** become the new Imp before any other Minion.

### Evidence semantics

- control owner: **RULE / CHARACTER ABILITY**
- decision family: **FORCED_SUCCESSION**
- Host recommendation ownership: **NONE over successor identity while the force applies**

Therefore a healthy active Scarlet Woman is not one candidate among several for a ranking model; she collapses the legal successor domain to one.

## 5. DS1-D — Scarlet Woman impairment can reopen ordinary successor choice

### Source

Official Poisoner guidance:
https://wiki.bloodontheclocktower.com/Poisoner

Published strategy explicitly notes that Evil may poison its own Scarlet Woman before an Imp self-kill so that another Minion can become the new Imp while Scarlet Woman remains in play.

### Evidence semantics

- impairment trigger: player-controlled Poisoner action;
- Scarlet Woman forced succession can therefore fail when her ability is not functioning;
- once the Scarlet Woman force is absent, ordinary Imp Star Pass successor rules apply.

Host consequence:

- successor legal-domain enumeration must use current ability-functioning state;
- `Scarlet Woman present` is insufficient; Host needs `Scarlet Woman ability functioning at succession time`.

This source is player strategy, not a Storyteller preference among the remaining Minions.

## 6. DS1-E — Storyteller-induced Demon death can indirectly trigger forced succession

### Source

`docs/EL_LRE_MR1_MAYOR_REDIRECT_TARGETED_ACQUISITION_2026-10-04.md` and Scarlet Woman M05.

Machine-semantic lead:

- Imp attacks Mayor;
- Storyteller may redirect Mayor's death onto the Imp;
- if Scarlet Woman's ability is active, Scarlet Woman then becomes the new Imp;
- possible rationale: the current Demon is nearly solved while Scarlet Woman has a stronger established bluff;
- the source flags this as visibly interventionist and potentially perceived as 'tipping the scales'.

### Control decomposition

- Mayor redirect target choice: **STORYTELLER**;
- Demon death: consequence of Storyteller redirect;
- Scarlet Woman becoming Imp: **FORCED BY ABILITY**, not a second successor-ranking decision.

### Evidence status

- MR1/Scarlet Woman passage: **AUDIO-READY / NOT YET PRIMARY-AUDIO VERIFIED**
- production policy: do not promote until audio review confirms exact recommendation strength and intervention-legitimacy caveat.

## 7. DS1-F — exotic Recluse succession interaction is legal-but-cautioned, not a normal candidate

### Source

Official Storyteller Advice:
https://wiki.bloodontheclocktower.com/Storyteller_Advice

The official advice explicitly uses the example of making Recluse register as the Imp during an Imp self-kill to illustrate that a technically legal Storyteller choice may still be unfun or unbalanced.

### Evidence semantics

- relation: **EXPLICIT CAUTION / NEGATIVE POLICY SIGNAL**
- source type: **OFFICIAL WRITTEN STORYTELLER GUIDANCE**
- legal possibility: acknowledged;
- ordinary policy desirability: explicitly questioned.

Host consequence:

- exotic Recluse succession should not enter normal beginner/default successor candidate ranking merely because registration legality permits it;
- if ever exposed as an advanced/manual option, it needs an explicit exceptional-policy scope rather than silent inclusion in the ordinary Minion domain.

## 8. DS1-G — Spy M11 is the strongest current successor-selection comparison lead

### Source

`docs/C2_MACHINE_SEMANTIC_FINDINGS_TB_SPY_2026-10-03.md`, M11.

Window: approximately `01:53:33–01:56:28`.

Machine-understood historical account:

- Star Pass is described as highly situational;
- a common instinct is to pass Demonhood to the Minion in the strongest / most trusted position;
- counterexample: the Storyteller passes Demonhood to a less-trusted Baron instead of a well-trusted Spy;
- rationale: the trusted Spy is more valuable remaining as a support network for the new Demon;
- player experience / fun also influenced the choice;
- the resulting Evil topology produced a close successful game.

### Evidence semantics

- likely relation: **OBSERVED_CHOICE + EXPLICIT RATIONALE + IMPLICIT ALTERNATIVE**
- source status: **MACHINE SEMANTIC / AUDIO-READY, NOT VERIFIED**
- strict historical production reconstruction: incomplete.

### Why this is high value

This is the clearest candidate for a real successor ranking dimension:

`best successor` is not always the most trusted Minion.

Instead Host may need to evaluate:

- candidate successor trust / survivability;
- value of leaving another Minion alive as trusted support;
- division of Evil-team social capital;
- player experience / agency as optional enrichment.

Do not implement this until primary-audio verification confirms the Storyteller actually owned the successor choice and the Spy-vs-Baron comparison/rationale.

## 9. DS1-H — R04 preserves two ordered Star Pass transitions but no rationale

### Source

`docs/C0_TB_RECONSTRUCTION_BATCH_01_2026-09-23.md`, Game R04.

Observed chronology:

- Night 4: Paul self-kills -> Hollie becomes Imp;
- Night 6: Hollie self-kills -> Deonna becomes Imp.

### Evidence semantics

- self-kill triggers: player-controlled;
- successor identities: historically observed;
- Storyteller rationale: not recovered;
- exact eligible-Minions domain at each transition: not fully normalized in the current reconstruction.

Use:

- valuable replay / ordered-state fixture;
- proves succession must be time-indexed rather than flattening final roles;
- not a source-backed successor ranking.

## 10. DS1-I — R06 preserves another Star Pass but no rationale

### Source

`docs/C0_TB_RECONSTRUCTION_BATCH_01_2026-09-23.md`, Game R06.

Observed:

- Imp self-kills on Night 5;
- Spy becomes the new Imp;
- ongoing Fortune Teller information continues across the transition.

Disposition:

- historical ordered-state fixture;
- no recovered Storyteller rationale;
- no ranking inference.

## 11. Control taxonomy for Host

### A. PLAYER_CONTROLLED_TRIGGER

Example:

- Imp chooses itself as the night kill.

Recommendation engine: **not owned by Storyteller**.

### B. STORYTELLER_SUCCESSOR_SELECTION

Example:

- ordinary Star Pass with multiple eligible alive Minions and no active Scarlet Woman force.

Recommendation engine: **YES**.

### C. RULE_FORCED_SUCCESSION

Examples:

- healthy Scarlet Woman with 5+ alive after Demon death / Imp self-kill.

Recommendation engine: **NO ranking; deterministic result**.

### D. STORYTELLER_CONTROLLED_TRIGGER + RULE_FORCED_SUCCESSION

Example:

- Mayor bounce kills Imp while active Scarlet Woman is present.

Recommendation engine:

- Mayor redirect decision may need policy;
- successor identity does not.

### E. EXOTIC_REGISTRATION_SUCCESSION

Example:

- Recluse registration interacting with Star Pass.

Recommendation engine:

- exclude from normal default policy;
- advanced/manual only unless an explicit verified exceptional predicate is later established.

## 12. Required Host state for successor selection

At minimum:

- current Demon identity / role;
- succession trigger type;
- alive Minions and their actual roles;
- ability-functioning state of Scarlet Woman;
- alive-player count / Scarlet Woman threshold;
- legal registration/exotic interactions separated from ordinary legal Minions;
- prior public claims / bluff positions;
- current Evil support topology;
- current historical role transitions.

Optional enrichment:

- player experience / recent role experience;
- local trust / public credibility;
- group tolerance for intervention-heavy Storyteller choices.

## 13. Evidence-backed successor-ranking dimensions currently available

### Verified structural dimensions

- successor choice exists only in ordinary Star Pass after forced rules are resolved;
- Scarlet Woman force has priority when active;
- exotic Recluse succession is officially cautionary;
- historical role/state must remain time-indexed.

### Audio-ready ranking dimensions

From Spy M11:

- successor trust/survivability;
- retained-Minon support value;
- Evil support topology;
- player experience / fun.

### Not supported

- 'always choose the most trusted Minion';
- 'always choose Spy';
- 'always choose the weakest Minion so the trusted one can support';
- numeric trust/support weights;
- generic team-balance override.

## 14. Current DS1 verdict

Demon succession is now separated into legal/control classes.

The broad family is no longer ambiguous:

- Imp self-kill trigger -> player-controlled;
- ordinary successor among eligible Minions -> Storyteller-controlled and recommendation-relevant;
- active Scarlet Woman -> forced successor, no ranking;
- Mayor-bounce-to-Imp -> Storyteller controls the trigger, Scarlet Woman succession remains forced;
- exotic Recluse interaction -> legal possibility with explicit official caution.

The single highest-value remaining evidence task is **primary-audio verification of Spy M11 `01:53:33–01:56:28`**, because it appears to contain a real Storyteller successor choice between Baron and Spy with explicit support-topology rationale.