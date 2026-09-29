# C0 Trouble Brewing Expert-Rationale Podcast Scout — Recluse — 2026-09-28

> Historical acquisition/scout artifact preserved from superseded PR #4. Machine-ASR windows are locator aids, not verified evidence unless a later authority document explicitly promotes them after primary review.

## Purpose

This scout reuses the validated podcast acquisition path to search for expert Storyteller rationale relevant to the current Trouble Brewing evidence gaps, especially:

- Gap A — healthy-information strength / middle band;
- Gap C — Spy/Recluse role-function exposure versus concealment;
- committed information trajectories where the same legal registration can support different worlds.

Target episode:

- show: `Cult of the Clocktower`;
- episode: `6: Recluse (Trouble Brewing) - With Official Storyteller Ben Dance!`;
- published: `2019-11-18T18:00:00Z`;
- RSS GUID: `e4b8704a-19d7-5c9f-e483-a659be61cc46`;
- live RSS duration: `4471 s` (~`1:14:31`);
- episode metadata identifies Ben Dance as an Official Storyteller from Melbourne.

This is expert-guidance material, not a reconstructable whole game.

## Acquisition result

The live RSS probe established:

- stable episode identity and public audio enclosure;
- no feed-advertised transcript;
- successful one-off ASR using `faster-whisper` `small.en`, CPU INT8, beam size 1;
- 972 timestamped segments;
- detected language: English;
- language probability: 1.0.

The complete machine transcript and source audio remain acquisition artifacts outside Git.

## Evidence boundary

Every candidate below is currently:

~~~text
MACHINE_LOCATED
+ HUMAN_REVIEW_PENDING
+ NOT_VERIFIED
~~~

The ASR is not diarized. Do **not** attribute an individual statement to Ben Dance or Andrew Nathenson until primary-audio review confirms the speaker, wording, intended meaning and context.

Do not use these candidates as production-policy evidence yet.

## Candidate windows

| ID | Approx. window | Machine-located candidate meaning | Potential relevance | Priority |
| --- | --- | --- | --- | --- |
| R01 | 00:56:36–00:58:41 | The Storyteller section opens with a legality-versus-judgment boundary: some Recluse registrations are technically possible but should normally not be used when they create broken game states or make another player feel arbitrarily deprived of agency. Storyteller decisions should be judged by their effect on the whole table, not only the directly affected player. | Global game-state / player-agency boundary. | P0 |
| R02 | 00:59:51–01:02:44 | Very unusual Recluse interactions and role-lifting are framed as advanced-table material that should depend on player experience and explicit table expectations. Extreme information such as a deliberately engineered Chef 5 is used as an example of something that requires special context. | Experience-sensitive policy; legal does not imply default. | P1 |
| R03 | 01:03:03–01:03:38 | Recluse registration is described as a major Storyteller decision surface capable of changing game flow; the choices deserve deliberate attention rather than automatic registration. | Direct support for explicit registration-policy ownership. | P0 |
| R04 | 01:03:53–01:05:40 | For a Recluse beside two evil players, whether to inflate Chef information should depend on how the table will use top-four claims and whether the Chef result will be trusted. A similarly strong Empath result can immediately expose a neighbouring Minion and deprive that evil player of meaningful play. | **Direct Gap A/C hit:** information strength is evaluated through table behaviour, trust and downstream exposure, not legality alone. | P0 |
| R05 | 01:05:40–01:06:16 | The Recluse is treated as an Outsider that should normally impose some cost on Good rather than accidentally become a large Good clue. One example keeps an Empath result at 1 before and after a neighbouring Minion dies, preserving the Recluse's harmful registration rather than turning the death into a clean confirmation. | **Direct trajectory hit:** registration continuity can deliberately preserve ambiguity after the underlying evil neighbour changes. | P0 |
| R06 | 01:06:18–01:06:42 | Fortune Teller interaction can make the Recluse resemble a Red Herring and can create uncertainty about whether the Fortune Teller is impaired. | Cross-mechanism ambiguity; useful but not a primary current gap. | P1 |
| R07 | 01:06:52–01:08:35 | Investigator information is explicitly tied to setup strength. If another role such as Empath already starts with unusually strong evil exposure, the Recluse can absorb the Investigator's Minion detection to reduce total Good information. The opposite option is also discussed: show the real Minion together with the Recluse, so the Recluse claim gives that real Minion a plausible escape world. | **Direct Gap C hit:** two opposite legal Investigator uses, with whole-setup and evil-escape rationale. | P0 |
| R08 | 01:08:36–01:10:20 | After the Recluse is executed, Undertaker misinformation can be selected dynamically to help Evil when Good is already close to the Demon: showing Spy or Imp can reopen otherwise narrowing worlds. New Recluse players may also need private explanation of how this handicap can affect information. | State-dependent help-to-Evil; beginner support without removing the handicap. | P0 |
| R09 | 01:10:20–01:11:37 | Librarian treatment is explicitly bidirectional. Showing the real Recluse can protect a repeatedly executed Recluse player and change a local meta by lending trust; alternatively the Recluse may register away so the Librarian learns zero Outsiders, creating a different uncertainty structure and a form of soft confirmation if the Recluse later claims. | **Direct Gap C hit:** expose/support versus conceal/zero are distinct policy intents for the same legal mechanism. | P0 |

## First human-review packet

Review these windows first:

~~~text
R01  00:56:36–00:58:41  legality versus whole-table impact
R03  01:03:03–01:03:38  deliberate registration-policy ownership
R04  01:03:53–01:05:40  Chef/Empath information strength and player exposure
R05  01:05:40–01:06:16  persistent Empath ambiguity after Minion death
R07  01:06:52–01:08:35  Investigator: absorb information vs reveal real Minion + Recluse
R08  01:08:36–01:10:20  Undertaker misinformation chosen from live game state
R09  01:10:20–01:11:37  Librarian: protect/expose Recluse vs register away to zero
~~~

Total first-pass review is roughly 10 minutes.

## Provisional synthesis if P0 windows verify

No production policy change is justified yet.

The candidate discussion would support the following qualitative dimensions:

1. **misregistration is conditional, not automatic**;
2. candidate information should be judged by how the specific table is likely to use and trust it;
3. a legal registration can be rejected because it exposes a Minion too strongly or removes meaningful player agency;
4. registration can preserve a longitudinal ambiguity even after the underlying evil topology changes;
5. Investigator + Recluse has at least two opposite policy intents:
   - reduce excessive Good information by letting the Recluse absorb the detection;
   - reveal the true Minion but give that Minion an alternative Recluse explanation;
6. Librarian + Recluse also has opposite policy intents:
   - expose/support the Recluse to create trust or correct a table meta;
   - conceal/register-away the Recluse to create zero-Outsider uncertainty;
7. Undertaker registration can be state-dependent rather than fixed at setup, specifically to reopen worlds when Good information has become too convergent.

These are candidate dimensions only until primary-audio verification.

## Relationship to the current E3 gaps

If R04/R05/R07/R09 verify, the expert-rationale side of Gap C becomes substantially stronger than before:

- official rules already establish legality and the possibility of choosing normal versus evil registration;
- the Librarian scout supplies expose-versus-conceal examples;
- this Recluse scout supplies explicit reasons for choosing between those legal alternatives.

However, this episode is not a committed whole-game reconstruction. It therefore should **not** by itself close the existing Gap-C whole-game requirement.

The remaining high-value bridge is a real game where the committed setup and registration decision can be reconstructed and the Storyteller's reason for that exact choice is recoverable.

## Acquisition conclusion

The podcast route again passed the low-human-cost test:

~~~text
~74:31 source audio
    -> RSS locator
    -> one-off small.en ASR
    -> 972 timestamped segments
    -> targeted Storyteller-section search
    -> ~10 minute P0 human-review packet
~~~

For Gap C, further generic Recluse guidance now has diminishing value. The next priority should return to **whole-game primary-video enrichment**, especially G01, while retaining the 2026 Clocktower Academy Recluse episode with TPI's Evin Donohoe as an independent expert follow-up only if the human review of this packet exposes an unresolved rationale question.
