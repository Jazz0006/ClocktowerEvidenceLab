# C0 Trouble Brewing Expert-Rationale Podcast Scout — Librarian — 2026-09-28

> Historical acquisition/scout artifact preserved from superseded PR #4. Machine-ASR windows are locator aids, not verified evidence unless a later authority document explicitly promotes them after primary review.

## Purpose

This scout reuses the validated podcast acquisition path to search for expert Storyteller rationale relevant to the current Trouble Brewing evidence gaps, especially:

- Gap A — healthy-information strength / useful-information floor;
- Gap C — Spy/Recluse role-function exposure versus concealment;
- Gap D — Demon-bluff selection rationale.

Target episode:

- show: `Cult of the Clocktower`;
- episode: `8: Librarian (Trouble Brewing) - With Official Storyteller Ben Finney!`;
- published: `2019-12-16T18:00:00Z`;
- RSS GUID: `1d03c939-76bb-3f58-5d86-cd6746d9b0a3`;
- live RSS duration: `3901 s` (`1:05:01`);
- guest qualification in episode metadata: Ben Finney is identified as an Official Storyteller and as having run convention games at PAX Australia in October 2019.

This is expert-guidance material, not a reconstructable whole game.

## Acquisition result

The live RSS probe established:

- stable episode identity and public audio enclosure;
- no feed-advertised transcript;
- successful one-off ASR using `faster-whisper` `small.en`, CPU INT8, beam size 1;
- 754 timestamped segments;
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

The ASR is not diarized. Do **not** attribute an individual statement to Ben Finney or Andrew Nathenson until primary-audio review confirms the speaker, wording, intended meaning and context.

Do not use these candidates as production-policy evidence yet.

## Candidate windows

| ID | Approx. window | Machine-located candidate meaning | Potential relevance | Priority |
| --- | --- | --- | --- | --- |
| L01 | 00:49:14–00:50:37 | The Storyteller section opens by treating first-night information as a setup-level decision surface: which Outsiders exist and what the Librarian is shown are linked choices. A Librarian can legitimately accompany zero Outsiders, or a Baron can be added to create Outsider information. | Whole-setup reasoning; information role is not evaluated locally. | P0 |
| L02 | 00:50:41–00:53:08 | The speakers disagree constructively about showing a Librarian zero to new players: one view treats it as potentially uninteresting/confusing; the other treats the same result as a useful teaching prompt if the Storyteller notices disappointment and helps the player reason from the outsider count. | Strong corrective evidence against a universal beginner rule; player experience and Storyteller support change the value of the same legal output. | P0 |
| L03 | 00:53:13–00:54:22 | Showing the Librarian a Drunk is discussed as a way to introduce the Drunk concept and branching-world reasoning to new players; making a Drunk believe they are the Librarian and then showing a Drunk is also discussed as a recurring Storyteller device. | Beginner handling; information topology around Drunk uncertainty. | P1 |
| L04 | 00:54:30–00:55:41 | A real Recluse ping can be paired with an evil player so the evil player gains a plausible Recluse world. The discussion explicitly explores cross-linking this with Investigator information and using the Spy as the second Librarian candidate. | **Direct Gap C hit:** exposure versus concealment through multi-role registration and confirmation chains. | P0 |
| L05 | 00:55:41–00:57:15 | Two opposite Recluse treatments are contrasted: positively identify the real Recluse to make that inherently suspicious player more trusted, or let the sole Recluse register away so a Librarian sees zero, creating Drunk/Poison/Recluse ambiguity and potentially implying there is no Baron. | **Direct Gap C hit:** the same Recluse ability can be used either to expose/support the Recluse or to conceal them, with different world-shaping consequences. | P0 |
| L06 | 00:57:18–00:59:01 | Saint information is discussed with two structurally different pairings: pair the Saint with evil to create execution danger, or with a good player to more nearly confirm the Saint while placing doubt elsewhere. | Healthy-information strength and consequence severity; useful Gap A comparison shape. | P1 |
| L07 | 00:59:07–00:59:58 | For a Librarian Drunk ping, a low-impact actual Drunk can be paired with a high-impact decoy role so suspicion falls on the more consequential possibility; pairing the real Drunk with Recluse is also discussed. | Misinformation-world design; impact depends on candidate-role consequence, not merely truth/falsehood. | P1 |
| L08 | 01:00:15–01:01:32 | Showing an evil player as the alternative Butler candidate can provide cover for suspicious voting behaviour; making the Butler presence public earlier changes how later actions are interpreted. | Confirmation-chain / social-cover topology. | P1 |
| L09 | 01:01:46–01:02:45 | Librarian is discussed as a Demon bluff that can be selected when the good setup contains a lot of information, explicitly using bluff choice to help Evil operate against the information density of the setup. | **Gap D support:** Demon-bluff choice responds to the whole setup and Good's information budget, though this is not yet a triplet comparison. | P0 |
| L10 | 01:02:50–01:04:10 | First-night information roles are recommended as engaging for new players; later, Librarian is discussed as a false character result that can support an existing evil bluff when a poisoned Undertaker/Ravenkeeper must be shown something misleading. | Beginner setup policy + misinformation support for an existing evil narrative. | P1 |

## First human-review packet

Review these windows first:

~~~text
L01  00:49:14–00:50:37  setup-level Librarian / Outsider choice
L02  00:50:41–00:53:08  opposing views on Librarian zero for new players
L04  00:54:30–00:55:41  Recluse + evil/Spy candidate and Investigator cross-link
L05  00:55:41–00:57:15  expose Recluse versus hide Recluse as zero
L09  01:01:46–01:02:45  Librarian Demon bluff versus high Good information density
~~~

Total first-pass review is about 7.5 minutes.

If L04/L05 verify, they are substantially stronger Gap-C rationale support than a legality-only rule example because they explain different reasons for opposite legal registration choices.

If L09 verifies, it adds a concrete whole-setup information-budget reason for selecting a Demon bluff, but it does **not** by itself close Gap D's desired triplet-comparison evidence.

## Provisional synthesis if P0 windows verify

No production policy change is justified yet.

The candidate discussion would support the following qualitative dimensions:

1. first-night information outputs should be evaluated together with setup and Outsider composition;
2. player experience is not a one-direction rule — the same low-information result may be poor for one new player yet valuable as a guided teaching opportunity for another;
3. Recluse registration has at least two distinct policy intents: **trust/exposure support** and **world concealment/confusion**;
4. Spy/Recluse misregistration can deliberately couple multiple information roles into a confirmation or contradiction chain;
5. Demon-bluff selection can respond to the overall amount of healthy information available to Good.

These are candidate dimensions only until primary-audio verification.

## Acquisition conclusion

The podcast route again passed the low-human-cost test:

~~~text
65:01 source audio
    -> RSS locator
    -> one-off ASR
    -> 754 timestamped segments
    -> targeted policy search
    -> ~7.5 minute P0 human-review packet
~~~

For the current evidence gaps, the next highest-value podcast target is the Recluse episode with Official Storyteller Ben Dance because it should directly test when and why the Storyteller chooses opposite Recluse registrations. Spy and Imp remain useful follow-ups for Gap C/D.
