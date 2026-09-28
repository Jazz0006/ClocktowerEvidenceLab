# C0 Trouble Brewing Targeted Game Gap Scout — 2026-09-28

## 1. Scope

This pass does **not** resume broad corpus growth.

It targets complete Trouble Brewing games that may close one of the current E3 acquisition gaps:

- **Gap A — healthy-information floor / middle band**: explicit expert rationale that a legal alternative would leave Good with too little or too much actionable healthy information;
- **Gap B — independent impaired-information believability / continuity**: a non-Ben expert explicitly comparing believable/coherent Drunk or poisoned information against a worse legal result, preferably across multiple nights;
- **Gap C — role-function exposure**: functioning Librarian/Investigator plus Spy/Recluse with at least one healthy legal alternative and explicit rationale about direct exposure versus concealment;
- **Gap D — Demon-bluff triplet**: an experienced Storyteller explicitly comparing legal bluff sets with rationale around route diversity, claim burden, collision, misinformation support or fallback.

A candidate is abandoned for E3 purposes once it lacks qualified Storyteller identity, reconstructable committed state, an observed Storyteller-controlled choice, production-recoverable legal alternatives or explicit choice-specific rationale.

## 2. Initial candidate pool

### G01 — NRB: Live and Imp-Person

Primary video:

- YouTube: `m14N28Lq-jM`;
- Trouble Brewing;
- Storytellers: Ben + Tom;
- 10 players.

A detailed secondary reconstruction is available from the No Rolls Barred Wiki and is sufficient to make this a high-priority **primary-video enrichment candidate**, not sufficient to verify corpus facts by itself.

Secondary reconstruction currently reports:

| Seat / player | Role |
| --- | --- |
| Oli | Baron |
| Carley | Fortune Teller |
| Jon | Librarian |
| Brooke | Drunk shown Undertaker |
| Adam | Chef |
| Isaac | Monk |
| Sullivan | Poisoner |
| Laurie | Recluse |
| Dom | Mayor |
| Blair | Imp |

Setup commitments reported by the secondary source:

- Demon bluffs: Investigator / Empath / Saint;
- Carley the Fortune Teller is her own Red Herring;
- Brooke is the Drunk and believes she is the Undertaker.

Ordered event backbone reported by the secondary source:

~~~text
N1
Jon Librarian -> Adam/Laurie contains Recluse
Adam Chef -> 1
Sullivan Poisoner -> Isaac
Carley FT -> Adam/Laurie -> YES

D1
Adam executed

N2
Brooke Drunk-as-Undertaker -> Adam was Chef (true information)
Sullivan poisons Brooke
Isaac protects Carley
Blair kills Isaac
Carley FT -> Sullivan/self -> YES

D2
Brooke executed

N3
Sullivan poisons Carley
Blair kills Jon
poisoned Carley FT -> self/Dom -> NO

D3
Laurie executed

N4
Sullivan poisons Carley
Blair kills Carley

D4
no nominations

N5
Sullivan chooses Dom
Blair kills Dom
Evil wins
~~~

Why G01 is unusually valuable:

- full/near-full setup is externally reconstructable;
- both Drunk and Poisoner operate in one game;
- the Drunk Undertaker receives truthful information;
- Fortune Teller misinformation has two different mechanisms: self Red Herring and later Poisoning;
- a functioning Librarian directly involves a Recluse;
- a complete Demon-bluff triplet is known;
- independent community descriptions consistently note that the production shows the Storyteller night phase and that Ben/Tom explain or speculate about their Storyteller choices.

Gap fit:

- **Gap B: HIGH potential** — Drunk Undertaker truth plus poisoned Fortune Teller outputs give concrete impaired-information choices;
- **Gap C: MEDIUM potential** — Librarian/Recluse interaction is present, but explicit direct-exposure rationale is not yet recovered;
- **Gap D: MEDIUM potential** — full bluff triplet is present, but choice-over-alternatives rationale is not yet recovered;
- **Gap A: LOW/UNKNOWN** until explicit information-bundle rationale is recovered.

Disposition:

> **P0 PRIMARY-VIDEO ENRICHMENT CANDIDATE.**

Do not promote any secondary-wiki event to VERIFIED. The next useful work is to locate Ben/Tom's choice explanations and verify the relevant setup/night windows from the primary video.

### G02 — TPI: Trouble Brewing (October 2019, Game 1)

Primary video:

- YouTube: `2TlW06GVF8I`;
- official Blood on the Clocktower channel;
- full 7-player Trouble Brewing game;
- Storyteller: Jon Gjengset.

The official video description verifies the script, player count and Storyteller identity.

Why it remains useful:

- independent qualified Storyteller;
- short full game, so primary review cost is low;
- 7-player table is directly relevant to the app's mainline size range.

Current limitation:

- indexed public sources recovered in this pass do not expose the setup/ordered game state or decision-specific Storyteller rationale.

Disposition:

> **P1 SCREENING CANDIDATE.**

Do not ask for human review until setup/mechanism screening shows a Gap A/B/C/D shape.

### G03 — TPI: Trouble Brewing (October 2019, Game 2)

Primary video:

- YouTube: `pVzZms1FTr4`;
- official Blood on the Clocktower channel;
- full 8-player Trouble Brewing game;
- Storyteller: Steven Medway, designer of Blood on the Clocktower.

The official video description verifies the script, player count and Storyteller identity.

Why it remains useful:

- exceptionally strong Storyteller qualification;
- short full game;
- 8 players sits directly inside the app's mainline range.

Current limitation:

- indexed public sources recovered in this pass do not expose the setup/ordered game state or decision-specific rationale.

Disposition:

> **P1 HIGH-QUALIFICATION SCREENING CANDIDATE.**

If later screening exposes one of Gap A/B/C/D, promote ahead of ordinary community games.

### G04 — TPI & Friends: Trouble Brewing — Yeah Boi!

Primary video:

- YouTube: `EsTXhFKtER8`;
- official Blood on the Clocktower channel;
- in-person Trouble Brewing;
- contemporary community references describe it as a strong short example involving experienced/expert players.

Current pass has not yet established enough setup/rationale detail to rank it above G01–G03.

Disposition:

> **P2 QUEUE.**

## 3. Transcript-access experiment

A bounded one-off probe tested:

- `yt-dlp --list-subs`;
- `youtube-transcript-api`;

against G01/G02/G03 from GitHub Actions.

Result:

~~~text
ACCESS_BLOCKED
not
NO_TRANSCRIPT
~~~

Observed failure modes:

- YouTube rejected the GitHub/Azure runner with bot/sign-in verification;
- `youtube-transcript-api` returned `RequestBlocked` for all three candidates.

Therefore:

- do **not** record these videos as having no captions;
- do **not** add account cookies or personal YouTube credentials to CI;
- do **not** make GitHub-hosted YouTube extraction part of the durable acquisition architecture.

The experiment answered an infrastructure question and should not be repeated on every candidate.

## 4. Current ranking

| Candidate | Whole-game state | Qualified ST | Gap shape already visible | Explicit rationale recovered | Priority |
| --- | --- | --- | --- | --- | --- |
| G01 Live and Imp-Person | strong secondary reconstruction; primary pending | yes, Ben/Tom | B strong; C/D possible | not yet | **P0** |
| G03 TPI Oct 2019 Game 2 | primary full game | yes, Steven Medway | unknown | not yet | **P1** |
| G02 TPI Oct 2019 Game 1 | primary full game | yes, Jon Gjengset | unknown | not yet | **P1** |
| G04 Yeah Boi! | primary full game | likely strong | unknown | not yet | **P2** |

## 5. Next acquisition action

Continue with **G01 first** because a complete game-state backbone is already available and only primary-video rationale/verification is missing.

Search specifically for primary/secondary locators around:

1. why Brooke, the Drunk-as-Undertaker, is shown true Chef information on Night 2;
2. why Carley is selected as her own Red Herring;
3. why the poisoned Fortune Teller receives NO on Night 3;
4. whether Ben/Tom explain the Investigator / Empath / Saint bluff triplet;
5. whether Jon's Librarian result involving Adam/Laurie is discussed as a Recluse-exposure choice.

If no rationale is recoverable without a full manual watch, reduce G01 to a short human review packet rather than asking for a 2+ hour review.

In parallel, continue indexed-source screening of G02/G03/G04 for setup roles and known misinformation mechanics.

## 6. Stop rule

Do not reconstruct a candidate merely because it is a famous or entertaining game.

The acquisition succeeds only if the game adds a missing evidence shape or provides enough decision-specific rationale to advance an E3 question.
