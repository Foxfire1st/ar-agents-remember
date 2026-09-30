# dashboard/src/panels/review/focusedCards.ts

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `dashboard/src/panels/review/focusedCards.ts` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-30T09:59:20+02:00 |
| lastVerifiedCommitHash | `b54d1b0331f67454bcf245a7a338b04900181c3c`|
| lastVerifiedCommitDate | 2026-09-30T11:03:56+02:00|
| governingOverview | `dashboard/src/panels/overview.md` |

## Governing Overview

[dashboard/src/panels route overview](../overview.md)

## Purpose

**The pure arithmetic of MIK-R31's focused expression cards: grouping by (path, range), MIK-R01 order, counts,
each member's voice, the not-current marks, and how much of a bounded family the cards cover.** It resolves,
searches and guesses nothing: every range comes from the server's MIK-R08 definition 3 resolution
(`ReviewTreeEntry` in `data/reviewTrees.ts`). `ExpressionCards.tsx` renders what it computes.

## Code Commentary

### Logic

- **Grouping (rule 1).** `cardKey` is the kind plus each side's region: `path:start-end` for a resolved side,
  `path:<state>` otherwise. Entries share a card only when both sides are established regions (resolved, or a file
  absent there); an unresolved or unavailable side appends the entry's own ID, because "the same range" is not a
  fact anyone established for it. So two regions of one file keep two cards and two rationales, and several
  members' entries at the same path and range share one card listing each member.
- **Order (MIK-R01 rule 4).** `orderedEntries`: the seed invariant's entries first (the selected member, by
  `invariant_key`), then by invariant ID, realizations before proofs (`KIND_RANK`), path, then entry ID. A card
  takes the position of its first entry (`expressionCards`). The server sorts proofs first within an invariant;
  this order puts them after the realizations.
- **Counts.** `cardCounts` counts cards, `changed`, `unchanged` and `undetermined` apart: an unchanged card is
  excluded from every changed count.
- **Voices (rule 2).** `cardVoice` speaks from the side that records the entry now (after, else before) with that
  side's role, facet and rationale; `missing` is a realization without an authored rationale, which the renderer
  shows as an explicit gap. `revised` carries the before side's different rationale (or facet) for "Revised in this
  leaf".
- **Ranges.** `firstLines` gives each side's first line for a diff gutter that keeps the file's numbering;
  `rangeLabel` prints `L<a>–<b>`, `no file` or the state.
- **Not current (rule 1).** `notCurrent` lists every recorded side whose MIK-R03 state is not `current`, with its
  reason.
- **Scope of a bounded roster (review F2, R2-5).** `cardScope` is `undefined` when every recorded side's page is
  complete, carries all `members_total` rows and every member row is `recorded`. Otherwise it takes the side
  recording the most membership rows and counts that side's distinct loaded members against that side's own
  total, capped at the total, so the loaded count never exceeds it.
- `languageOfPath` maps a path suffix to the highlighting ids `data/review.ts` uses; it styles and decides nothing.

### Conventions

- Pure functions of their arguments; the component owns all state.

### Invariants And Boundaries

- **Candidate invariant (not ingested): focused cards group expressions by (path, range) with the rationale
  directly above the excerpt, and a missing rationale is shown as a gap.** Realized here by `cardKey`,
  `expressionCards` and `cardVoice`, and in `ExpressionCards.tsx` by the voices above the excerpt. Proved by
  `ExpressionCards.test.tsx` (two regions give two cards; a shared range gives one card with two voices; unresolved
  entries never merge; a missing rationale is a gap) and by `ReviewSurface.gitTrees.test.tsx` on real data (4 cards
  in `review_source_admission.py`, 4 distinct rationales, the rationale before the excerpt in the DOM).
- **Candidate invariant (not ingested): a bounded roster never reads as the whole family; the cards state the
  loaded n of m.** Realized by `cardScope` and `ScopeLine`. Proved by the F2 case over the real walkFinal capture
  (bounded family gives the line; complete family gives none) and the R2-5 disjoint-sides case (`loaded <= total`).
- **Accepted note R3-N1 (09:38:03):** `cardScope` can say "loaded 2 of 2 … load the rest" when the widest side is
  fully loaded and the incompleteness is only on the other side (for example that side's members are
  `content_not_on_page`; ties go to `before`). The line never overstates coverage, so it was accepted as a note.

### Todos

- **R3-N1 (optional, not ruled as work):** take the side that is actually incomplete, or reword the line for rows
  loaded but content not on the page.

## Docs References

No domain documentation source is configured; the requirement packet `MIK-R31@v1` and its rulings
(`31_focused-expression-cards.json`) live outside the code and memory repositories, so they are named here and not
cited as rows.

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured live documentation source was available for this pass. | — | — |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The module's own statement of grouping and order. | "never one path"; "A card takes the position of its first entry." | dashboard/src/panels/review/focusedCards.ts:1-13 |
| A card: kind, path, change, both sides and its entries. | `ExpressionCard`; `CardCounts` | dashboard/src/panels/review/focusedCards.ts:19-27; dashboard/src/panels/review/focusedCards.ts:29-34 |
| The region key; an unresolved or unavailable side keeps its own card. | `region`; `cardKey` | dashboard/src/panels/review/focusedCards.ts:43-46; dashboard/src/panels/review/focusedCards.ts:50-55 |
| MIK-R01 order with the seed first, and one card per key. | `orderedEntries`; `expressionCards` | dashboard/src/panels/review/focusedCards.ts:57-66; dashboard/src/panels/review/focusedCards.ts:68-88 |
| Unchanged excluded from the changed count. | `cardCounts` | dashboard/src/panels/review/focusedCards.ts:91-98 |
| Each member's voice, with `missing` for an absent rationale. | `CardVoice`; `cardVoice` | dashboard/src/panels/review/focusedCards.ts:103-111; dashboard/src/panels/review/focusedCards.ts:113-134 |
| Gutter starts, range labels and not-current marks. | `firstLines`; `rangeLabel`; `notCurrent` | dashboard/src/panels/review/focusedCards.ts:137-139; dashboard/src/panels/review/focusedCards.ts:141-149; dashboard/src/panels/review/focusedCards.ts:152-163 |
| The loaded n of m, counted on the widest side and capped. | `CardScope`; `cardScope` | dashboard/src/panels/review/focusedCards.ts:190-193; dashboard/src/panels/review/focusedCards.ts:195-210 |
| The grouping cases. | "keeps two regions of one file as two cards with their own rationale"; "shares one card between members at the same path and range, each with its own rationale"; "never merges entries whose side did not resolve, and counts unchanged apart from changed"; "orders by the family order, with the selected member first" | dashboard/src/panels/review/ExpressionCards.test.tsx:163-205 |
| The F2 scope case. | "cover only the loaded members and points to the walk (F2)" | dashboard/src/panels/review/ExpressionCards.test.tsx:237-263 |

## Cross-Repo References

| Finding | Anchor | Source |
| --- | --- | --- |
| No cross-repo boundary is crossed by this file. | — | — |

## Update History

<!-- newest entry by date and time is prepended at the top of the list; prepend-only -->
- 2026-09-30T09:59:20+02:00 — 260928-MIK-L31 curator (staged change set on `ar/260928-mik-l31`, code base `48f680d5b95b8cb6eafff4f1ccd19c8f32e8c48c`; review R3 pass-with-notes): created this card for the new module MIK-R31 adds, recording rulings 06:10:21 F2 (the loaded n of m), 06:47:03 R2-5 (counted on one side, capped) and 09:38:03 R3-N1 (accepted note), and two candidate invariants. The verification stamp is left empty: the file is new and uncommitted; closeout owns the real stamp.
