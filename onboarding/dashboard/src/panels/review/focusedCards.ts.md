# dashboard/src/panels/review/focusedCards.ts

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

## Evidence

### Docs References

No domain documentation source is configured; the requirement packet `MIK-R31@v1` and its rulings
(`31_focused-expression-cards.json`) live outside the code and memory repositories, so they are named here and not
cited as rows.

No configured live documentation source was available for this pass.

### Repo-Internal References

- The module's own statement of grouping and order. [1]
- A card: kind, path, change, both sides and its entries. [2]
- The region key; an unresolved or unavailable side keeps its own card. [3]
- MIK-R01 order with the seed first, and one card per key. [4]
- Unchanged excluded from the changed count. [5]
- Each member's voice, with `missing` for an absent rationale. [6]
- Gutter starts, range labels and not-current marks. [7]
- The loaded n of m, counted on the widest side and capped. [8]
- The grouping cases. [9]
- The F2 scope case. [10]

### Cross-Repo References

No cross-repo boundary is crossed by this file.
