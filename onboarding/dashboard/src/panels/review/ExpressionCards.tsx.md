# dashboard/src/panels/review/ExpressionCards.tsx

## Governing Overview

[dashboard/src/panels route overview](../overview.md)

## Purpose

**The central reading path's code and test expressions for a measured tree comparison (MIK-R31): one focused
card per kind and pair of side regions, its authored rationale or proof facet above the excerpt, a changed range
as its supplied diff and an unchanged range once, labelled unchanged.** `focusedCards.ts` supplies grouping,
order and counts. Full-file inspection stays inside the selected card with its intent markers; the inventory
button delegates to the change-set navigation context. The current caller has no dataset `ReviewExpressions`
fallback: without a measured comparison it shows that explicit boundary instead of resurrecting the removed
whole-file renderer. `ExpressionControls.tsx` now owns the shared layout/full-file controls.

Historically the cards coexisted with the unconverted dataset accordion and reused controls exported from that
renderer. Those were the earlier routing/import boundaries, not current source paths or retained executions.
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
- **Bounded or missing content (review F2).** `ScopeLine` prints loaded/total and the supplied missing reasons.
  Only when loaded is below total does it direct the reader to the roster next-page control and exclude the
  unreturned locations. At equal counts with missing content it explicitly says the cards do not cover that
  named content; a loaded row count is not complete source coverage.
- **A card (`FocusedCard`).** Header: "Code expression" or "Test proof" with the roles (a proof shows `facet`), the
  side path and the change badge (`Changed range`, `Unchanged`, `Not comparable`). Then the voices (rule 1: the
  rationale directly above the excerpt), then the side lines (`Before · L…`, `After · L…`, or one "Before and after
  · … · the same text on both sides" line for an unchanged card whose ranges match), then the excerpt, the
  MIK-R03 not-current marks (`<entry> <state> on the <side> side`), and the actions: **Full file**,
  **All changed files (n)** (opens the comparison change-set viewer). The grouped identifiers disclosure
  belongs to `ReadyCards` once for the selection, not to any card's actions.
- **A voice (`Voice`).** The heading names the invariant, the role (or "proof facet"), MIK-R11's planning mark
  when the workspace passed one (`touched invariant · planned`), and "added" or "retired in this leaf". The body is
  the authored rationale (or proof facet); a missing value is explicitly named as "No authored rationale" or
  "No authored facet" for that entry, never replaced by generated semantics. A revised rationale/facet shows its
  before text under "Revised in this leaf".
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
- **Full file.** `FullFile` requires both supplied code-tree IDs, then delegates to `SourceContent` with the
  listed inventory entry or a synthetic `status: unknown`, `content: unknown` row whose detail says "an unchanged
  file a recorded entry names". That text does not itself establish unchanged content or backend admission. It
  passes `markers={{ pane }}` so the full-file marker return retains this card's identity.

### Conventions

- `ExpressionControls` is imported from its surviving dedicated module, `ExpressionControls.tsx`; the parent
  owns the layout/full-file props. No current control import depends on the removed dataset renderer.
- `data-testid` values name every part (`review-expression-card`, `review-card-voice`, `review-card-rationale`,
  `review-card-rationale-missing`, `review-card-excerpt` with `data-excerpt` `diff`/`unchanged`/`separate`,
  `review-card-currentness`, `review-card-full-file`, `review-card-inventory`, `review-cards-scope`).

### Invariants And Boundaries

- **Design boundary:** focused cards group expression regions, place the supplied rationale/facet above the
  excerpt and show an absent authored value as a gap (with `focusedCards.ts`); this prose is not a new formal
  invariant or acceptance record.
- **Recorded `INV-VPX81HXV`:** bounded linked-source scope is not full-family coverage. `ScopeLine` renders
  `cardScope`'s counts and reasons without relabelling missing content as a continuation requirement.
- The renderer writes no explanation of its own; every sentence about an entry is the entry's authored text or a
  fixed state label.
- Identifier/blob/content provenance stays in a grouped disclosure; not-current reasons remain open in the reading path. `CardCurrentness` keeps the mark text exactly `<entry> <state> on the <side> side`. A supplied reason is a sibling `review-card-currentness-reason` span with the same entry and side, outside every disclosure; it never extends the mark text or changes the owner-supplied state.
- **An excerpt that draws a changed line draws its hunk's intent mark** (MIK-L34; the candidate invariant recorded
  on `IntentMarkers.tsx.md`): nothing here decides a mark; the excerpt passes the sides it draws and places what
  `useExcerptMarking` returns.

### Todos

The current scope text supersedes the former equal-count continuation wording; the dataset accordion import
and fallback are retired. Cited tests are checked-in assertions over captured or synthetic inputs, not a new
execution, whole-file correctness grade or independent MEMORY acceptance.

## Evidence

The evidence table below anchors the exact entry/state/side text and its separate supplied-reason sibling outside disclosures.


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
- The card-owned full-file and inventory paths; the source contains no explorer OpenedFile renderer. [11]
- The center caller passes measured-comparison cards or an explicit comparison-required boundary; no dataset accordion fallback. [12]
- Checked-in card fixtures assert changed versus unchanged excerpts and a named missing-rationale gap; not a fresh execution. [13]
- The F1 mounted fixture stubs an HTTP-shaped Response and counts source-content requests; not a backend or Git read measurement. [14]
- Mounted card fixtures assert the exact returned card, drawn-side mark retention, other-content suppression and no unchanged-file request; not a fresh execution. [15]
- The read-state wrapper delegates ready entries to the card assembly owner. [16]
- ReadyCards owns grouping, counts, selected-card full-file state and returning-card restoration. [17]
- One focused card with roles, voices and excerpts [18]
- Link from a card to the full changed-file inventory [19]
- In-card full file with markers through the shared pane [20]
- Exact entry/state/side text and a separate supplied-reason sibling outside disclosures. [21]
- ScopeLine names actual missing reasons and distinguishes unfinished membership from missing content at equal counts. [22]
- The shared controls are imported from their surviving dedicated module, not ReviewExpressions. [23]

### Cross-Repo References

No cross-repository boundary is asserted by this module.
