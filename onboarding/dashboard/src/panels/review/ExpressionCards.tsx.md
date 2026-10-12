# dashboard/src/panels/review/ExpressionCards.tsx

## Governing Overview

[dashboard/src/panels route overview](../overview.md)

## Purpose

**The central reading path's code and test expressions for a tree comparison (MIK-R31): one focused card per
(path, range), its authored rationale directly above the excerpt, a changed range as its real diff and an
unchanged range once, labelled unchanged.** It replaces the whole-file accordion (`ReviewExpressions.tsx`) for tree
comparisons only; a dataset (unconverted) review never mounts it. Full-file inspection and the complete
changed-file inventory stay one step away from every card (rule 5). The grouping, order and counts are
`focusedCards.ts`'s. **Since MIK-R34** every excerpt that draws changed lines, and every full file, carries the
per-hunk intent markers of the hunks it draws.

The central reading path's code and test expressions for a tree comparison: one focused card per path and range, the authored rationale above the excerpt, a changed range as its diff and an unchanged range once, labelled. Full-file inspection stays inside the card with its intent markers, and the complete changed-file inventory stays one link away in the change-set viewer.
## Code Commentary

### Logic

- **Read states.** `ExpressionCards` shows the layout controls with a status line while the selection's entries
  are loading, `ReviewProblemBlock` when the read is unavailable, and "not a tree comparison" for any other phase;
  otherwise `ReadyCards` renders the cards.
- **`ReadyCards`.** A counts line (`n locations · k changed · m unchanged`, plus `not comparable` when some are
  undetermined, with `data-changed-count` and `data-unchanged-count`), the `ScopeLine` when the roster is bounded,
  an explicit "no realization or proof entry" line when there are none, then one selection-wide
  `EntryIdentifiers` disclosure before the card iteration, followed by one `FocusedCard` per card.
  There is no `OpenedFile` rendering path outside those cards.
- **One full file at a time, in the card that asked (review F1).** The open state is the card's key; a path opened
  by a card reads in that card. One click gives one `SourceContent` read in the
  clicked card; clicking again closes it. **A return to an intent marker (MIK-L34) reopens the exact card it was
  followed from:** each card's full file is the pane `card:<key>`, and
  `ReadyCards` starts from, and follows, `returnedCard` of the marker scope's `returning` pane, not the first card of
  the path.
- **The bounded roster (review F2).** `ScopeLine` says "These cards cover the loaded n of m members", points to the
  roster walk's next-page control, and says the other members' locations are not counted.
- **A card (`FocusedCard`).** Header: "Code expression" or "Test proof" with the roles (a proof shows `facet`), the
  side path and the change badge (`Changed range`, `Unchanged`, `Not comparable`). Then the voices (rule 1: the
  rationale directly above the excerpt), then the side lines (`Before · L…`, `After · L…`, or one "Before and after
  · … · the same text on both sides" line for an unchanged card whose ranges match), then the excerpt, the
  MIK-R03 not-current marks (`<entry> <state> on the <side> side`), and the actions: **Full file**,
  **All changed files (n)** (opens the comparison change-set viewer). The grouped identifiers disclosure
  belongs to `ReadyCards` once for the selection, not to any card's actions.
- **A voice (`Voice`).** The heading names the invariant, the role (or "proof facet"), MIK-R11's planning mark
  when the workspace passed one (`touched invariant · planned`), and "added" or "retired in this leaf". The body is
  the authored rationale (or facet); a missing one is "No authored rationale is recorded for <ID>." (rule 2), never
  generated text. A revised rationale shows its before text under "Revised in this leaf".
- **Excerpts.** `UnchangedExcerpt`: one `FilePane` of the after excerpt, numbered from the range's first line.
  `ChangedExcerpt`: a `DiffPane` of the two excerpts with `collapse={false}` and each side's own first line; a side
  with no file is the empty operand of an added or deleted file. `SeparateSides`: a card whose sides are not both
  regions shows each readable side's text alone and draws no diff. `Truncated` states a prefix excerpt.
- **Excerpt marks (MIK-L34; ruling 2026-09-30T16:19:34 Q4, review R1 F1).** Each excerpt asks
  `IntentMarkers.useExcerptMarking(card, layout, draws)` for the sides it draws (`UnchangedExcerpt` the after side
  only, since a range with the same text on both sides can still hold changed lines when code moved as a whole;
  `ChangedExcerpt` and `SeparateSides` both), and every owner hunk whose changed lines the excerpt draws is marked
  on those sides at the excerpt's own file line numbers, from the file's one cached classification. Only the drawn
  sides' blobs are compared with the classification's, so an unreadable memory side (served with no blob) never takes
  the drawn side's marks away; a drawn side of other content gets the `other-content` note, never silence. A card
  whose two blobs are equal is never active (an unchanged file's card asks nothing). `SeparateSides` hands each side's
  `FilePane` only that side's marks. The note and the open marker's list render below the excerpt, in the pane
  `card-excerpt:<key>`.
- **Side states (Failure and Recovery).** `sideStateText`: `no file on this side`, `unresolved: <reason>`,
  `unavailable: <reason>`; `sideLine` adds "entry not recorded on this side".
- **Full file.** `FullFile` reads through the landed `SourceContent` at the review's own code trees, with the
  inventory entry when the path is listed, else a synthetic unchanged entry ("an unchanged file a recorded entry
  names"), which the server admits for a realization's or, since ruling Q1, a proof's path. It passes its pane name
  (`markers={{ pane }}`) so the full file's marks, and a return to them, belong to this card.

### Conventions

- `ExpressionControls` is reused from `ReviewExpressions.tsx` (now exported), so the diff layout and full-file
  toggles are the same controls and keep their state across layout switches.
- `data-testid` values name every part (`review-expression-card`, `review-card-voice`, `review-card-rationale`,
  `review-card-rationale-missing`, `review-card-excerpt` with `data-excerpt` `diff`/`unchanged`/`separate`,
  `review-card-currentness`, `review-card-full-file`, `review-card-inventory`, `review-cards-scope`).

### Invariants And Boundaries

- **Candidate invariant (not ingested): focused cards group expressions by (path, range) with the rationale
  directly above the excerpt, and a missing rationale is shown as a gap** (with `focusedCards.ts`).
- **Candidate invariant (not ingested): a bounded roster never reads as the whole family; the cards state the
  loaded n of m** (`ScopeLine`, with `cardScope`).
- The renderer writes no explanation of its own; every sentence about an entry is the entry's authored text or a
  fixed state label.
- Identifier/blob/content provenance stays in a grouped disclosure; not-current reasons remain open in the reading path. `CardCurrentness` keeps the mark text exactly `<entry> <state> on the <side> side`. A supplied reason is a sibling `review-card-currentness-reason` span with the same entry and side, outside every disclosure; it never extends the mark text or changes the owner-supplied state.
- **An excerpt that draws a changed line draws its hunk's intent mark** (MIK-L34; the candidate invariant recorded
  on `IntentMarkers.tsx.md`): nothing here decides a mark; the excerpt passes the sides it draws and places what
  `useExcerptMarking` returns.

### Todos

No additional work is asserted by this card.

## Evidence

- Exact entry/state/side text and a separate supplied-reason sibling outside disclosures. [21]


### Docs References

No domain documentation source is configured; the requirement packet `MIK-R31@v1`, the accepted design
(ICR-R24@v3 "Accepted layout") and the rulings live outside the code and memory repositories, so they are named here
and not cited as rows.

No configured live documentation source was available for this pass.

### Repo-Internal References

- The props the centre passes: the read, the seed, the planning marks, layout and open path, and the scope. [1]

- Loading, unavailable and not-a-tree-comparison states. [2]

- The counts, the scope line and one full file keyed by the card (F1). [3]

- A return to a marker followed from a card's full file reopens that card (MIK-L34). [4]
- Side lines, one line for an unchanged same region, and the side-state texts. [5]
- One card: header, voices, side lines, excerpt, marks, actions. [6]

- A voice: the authored rationale or facet, or the named gap. [7]

- Unchanged once, changed as a diff, sides that are not both regions shown apart; each marks the owner hunks whose changed lines it draws, on the sides it draws (MIK-L34). [8]

- The excerpt marking: only the drawn sides compared, a mismatch said, an unchanged file's card never active. [9]
- One grouped identifiers disclosure carries the selected entries and their supplied side blobs and digests. [10]

- Cards open their own full file with marker identity and link all changed files to the comparison viewer; no explorer OpenedFile is rendered. [11]

- The one caller, which mounts cards only for a tree comparison. [12]

- The card-state cases. [13]
- The F1 case. [14]
- The marker cases on real cards: the exact card reopened, and the excerpt marks with an unreadable memory side, other content and an unchanged file. [15]

### Cross-Repo References

No cross-repo boundary is crossed by this file.
- Card collection assembly with grouping, order and counts [16]
- Grouped ready cards with returning-card state [17]
- One focused card with roles, voices and excerpts [18]

- Link from a card to the full changed-file inventory [19]
- In-card full file with markers through the shared pane [20]
