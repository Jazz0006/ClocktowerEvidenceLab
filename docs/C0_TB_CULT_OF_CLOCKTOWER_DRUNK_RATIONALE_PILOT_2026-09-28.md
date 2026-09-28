# C0 Trouble Brewing Expert-Rationale Podcast Pilot — Drunk — 2026-09-28

## Purpose

This pilot tests whether a long-form expert podcast with no feed-provided transcript can become a low-human-cost, timestamped rationale-discovery source without weakening Evidence Lab provenance rules.

Target:

- show: `Cult of the Clocktower`;
- episode: `16: Drunk (Trouble Brewing) - With Clocktower Designer Steven Medway!`;
- guest: Steven Medway;
- publication time from live RSS: `2020-04-06T17:00:00Z`;
- RSS GUID: `bf668470-a3fe-41d3-85e8-d028a63cf593`;
- Spotify/Anchor episode slug: `ecemnu`;
- Apple episode ID: `1000470673246`;
- live RSS duration: `8847 s` (`2:27:27`).

This is **expert guidance**, not a reconstructable whole game. It cannot replace whole-game evidence or become a replay fixture by itself.

## Acquisition result

The live RSS probe established:

- stable episode metadata is discoverable automatically;
- the original public MP3 is directly locatable from the RSS enclosure;
- the RSS currently advertises **no transcript** for this episode;
- missing feed transcript can therefore trigger ASR fallback instead of a full manual listen.

The ASR pilot then succeeded end-to-end using `faster-whisper` with `small.en`, CPU, INT8 and beam size 1.

Result:

- 1609 timestamped segments;
- detected language: English;
- language probability: 1.0;
- full machine transcript and source audio remain acquisition artifacts outside Git.

## Evidence boundary

Every candidate below is currently:

~~~text
MACHINE_LOCATED
+ HUMAN_REVIEW_PENDING
+ NOT_VERIFIED
~~~

ASR is a locator, not evidence sufficient to attribute a claim to Steven Medway.

Promotion requires primary-audio review confirming speaker attribution, intended meaning, context, timestamp range and a concise paraphrase.

Do not commit long transcript passages.

## Candidate windows

| ID | Approx. window | Machine-located candidate meaning | Potential relevance | Priority |
| --- | --- | --- | --- | --- |
| P01 | 01:28:18–01:29:18 | Three Drunk-selection approaches are discussed: player-driven, role-driven, and whole-setup-driven. Whole-setup context is presented as especially interesting, with fun/interest distinguished from balance-for-balance's-sake. | Global setup/context over role-local heuristics. | P0 |
| P02 | 01:29:19–01:30:14 | Drunk value is discussed together with another linked information role/player; Librarian/Investigator interaction can create immediate conflicting narratives. | Information topology / bundle effects. | P1 |
| P03 | 01:31:00–01:31:35 | Drunk Washerwoman is discussed as more suitable for new players than veterans because discovering one's drunkenness can itself be a comprehensible puzzle. | Player-experience-sensitive policy. | P1 |
| P04 | 01:32:20–01:34:45 | Drunk Librarian can create uncertainty while leaving other information roles sober; misinformation is treated as more than a simple penalty/hurdle. | Evaluate misinformation by structural effect, not false-count alone. | P1 |
| P05 | 01:41:15–01:43:25 | Drunk Investigator can create conversation/conflict; target selection may depend on player traits and interaction style. | Social/player context as rationale evidence. | P1 |
| P06 | 01:50:01–01:52:37 | Drunk Chef guarantees a first-night intervention; seating/setup is used as a concrete reason to choose Chef, and materially different information is preferred over barely changed information in the discussed examples. | Whole-setup selection; may challenge overly conservative role-local magnitude assumptions. | P0 |
| P07 | 01:54:39–01:55:10 | An Empath seated beside two evil players need not automatically be Drunk; an unusually strong result can itself make the player distrust the result. | Existing ambiguity reduces marginal need for another misinformation source. | P0 |
| P08 | 01:55:10–01:56:05 | Drunk Empath is explicitly longitudinal: prior outputs should be remembered; later output can preserve or deliberately break the false narrative, and contradiction can itself be a clue. | Persistent Drunk trajectory / committed-prefix evaluation. | P0 |
| P09 | 01:56:10–01:57:41 | Drunk Fortune Teller is discussed as harder to keep narratively consistent because the player chooses new pairs; detailed consistency is relaxed compared with Empath, and repeated outputs can instead hint that the player is Drunk. | Important corrective evidence: coherence appears role/interaction dependent, not one universal Drunk rule. | P0 |
| P10 | 01:58:34–02:01:11 | Drunk Undertaker can reinforce or later contradict narratives; true and false information may be mixed so players know some misinformation exists without knowing where. | Trajectory + confirmation-chain topology; impairment need not mean always false. | P1 |
| P11 | 02:04:10–02:05:11 | Drunk Monk/Soldier can make a new-player puzzle easier by exposing that a Drunk exists without creating large false-information chaos. | Beginner-table policy; separate Drunk-existence uncertainty from misinformation volume. | P0 |
| P12 | 02:05:38–02:07:39 | Drunk Ravenkeeper is discouraged for new-player games in the discussed context because successfully dying at night is hard-earned; veteran treatment is much harsher and Ravenkeeper misinformation is high-impact. | Experience-sensitive policy + information-impact severity. | P0 |
| P13 | 02:14:25–02:16:54 | Drunk Mayor can reshape a mature group's metagame, but is discouraged for a new group; other roles can narrow who is or is not Drunk. | Group-meta context; not a Host requirement unless group history is modelled. | P1 |
| P14 | 02:17:37–02:22:47 | Poisoner target choice is treated as player agency that should be respected; poisoning actively requests incorrect information, whereas Drunk misinformation is more directly Storyteller-controlled. The discussion warns against overriding player agency merely to rebalance. | Strong qualitative support for Drunk vs Poisoner ownership semantics and player-controlled committed actions. | P0 |
| P15 | 02:22:58–02:24:17 | Closing principle: attend to Evil bluffs and the narratives the table is actually building; consider how players will react to a Drunk output; Storyteller's goal is an interesting game rather than winning/losing. | Whole-bundle/contextual recommendation principle. | P0 |

## Immediate consequences if P0 windows verify

No production policy change is justified yet.

If primary-audio review confirms the P0 meanings and attribution, this episode would add expert-guidance support for:

1. **whole-setup selection** rather than role-local Drunk choice;
2. **existing ambiguity budget** before adding another misinformation mechanism;
3. **trajectory dependence** for repeated Drunk information;
4. **role-specific coherence**, especially Empath versus Fortune Teller;
5. **beginner sensitivity** in selecting which role becomes Drunk;
6. **Drunk versus Poisoner ownership**, adding player-agency semantics to the already-observed duration distinction;
7. **player agency over forced balance** when player-controlled actions have already committed a consequence.

These are qualitative dimensions, not numeric weights or mandatory rules.

## First human-review packet

Review only these windows first:

~~~text
P01  01:28:18–01:29:18  setup-driven Drunk selection
P06  01:50:01–01:52:37  Drunk Chef / seating-driven misinformation
P07  01:54:39–01:55:10  Empath 2 already creates doubt
P08  01:55:10–01:56:05  Empath longitudinal false narrative
P09  01:56:10–01:57:41  Fortune Teller coherence differs from Empath
P11  02:04:10–02:05:11  new-player Monk/Soldier
P12  02:05:38–02:07:39  new-player versus veteran Ravenkeeper
P14  02:17:37–02:22:47  Poisoner versus Drunk / player agency
P15  02:22:58–02:24:17  closing whole-narrative principle
~~~

This is about 15 minutes of first-pass review instead of a 2:27:27 full manual listen.

## Pilot conclusion

The retained workflow is:

~~~text
public podcast RSS
    -> episode/audio/transcript locator probe
    -> use feed transcript when advertised
    -> otherwise optional local ASR
    -> timestamped machine transcript outside Git
    -> candidate discovery
    -> short human primary-audio review
    -> concise provenance-backed expert rationale
~~~

This does **not** change the project's whole-game-first strategy.

Podcast material is a complementary expert-rationale corpus used to explain, support or challenge policy dimensions found in whole-game evidence.
