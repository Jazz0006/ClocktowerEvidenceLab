# Stale PR #3/#4/#5 Consolidation — 2026-09-29

## Purpose

Preserve durable work from three pre-C1 draft branches without merging stale roadmap/handoff state back over the completed C1 mainline.

## PR #3 — E3/E4 qualification refresh

Disposition: **superseded draft; preserve the qualification audit only**.

Preserved:

- `docs/C0_TB_E3_E4_QUALIFICATION_AUDIT_2026-09-27.md`.

Not carried forward:

- stale roadmap/handoff edits from the pre-C1 baseline.

Reason:

The audit remains useful as the historical definition of C5/E3-E4 evidence gaps, while live status is now newer and must remain authoritative.

## PR #4 — podcast expert-rationale acquisition pilot

Disposition: **superseded draft; preserve reusable acquisition infrastructure and research artifacts**.

Preserved:

- podcast RSS/transcript locator parser;
- optional faster-whisper ASR adapter and CLI;
- timestamp-normalization tests;
- podcast rationale acquisition workflow;
- Drunk/Librarian/Recluse scout documents, explicitly retained as historical locator artifacts unless separately human-verified.

Not carried forward:

- stale branch-level status text;
- any implication that machine-ASR text itself is verified evidence.

Reason:

The tooling is generic, tested, and directly useful for future targeted rationale acquisition. Later C1 work demonstrated the intended workflow: machine location followed by bounded human primary review before promotion.

## PR #5 — targeted TB game-gap scouting

Disposition: **close without merging**.

Reason:

- the branch is a large pre-C1 scouting notebook rather than a durable contract;
- its active target gaps are already captured more cleanly by the preserved E3/E4 qualification audit;
- later C1 primary review superseded several candidate dispositions;
- in particular, the G06 introduction/instructional source was later rejected for historical-game evidence, so merging the old scouting document unchanged would reintroduce stale/conflicting guidance.

The closed PR remains available as repository history if an old locator ever needs to be recovered.

## Result

After this consolidation:

- live mainline keeps C1 as the current authority;
- reusable podcast acquisition capability is retained;
- C5/E3-E4 gap definitions are retained;
- obsolete scouting/status branches can be closed without losing the durable material needed for future work.
