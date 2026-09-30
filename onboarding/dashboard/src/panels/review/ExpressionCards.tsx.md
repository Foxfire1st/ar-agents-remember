# dashboard/src/panels/review/ExpressionCards.tsx

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `dashboard/src/panels/review/ExpressionCards.tsx` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-30T09:59:20+02:00 |
| lastVerifiedCommitHash | `b54d1b0331f67454bcf245a7a338b04900181c3c`|
| lastVerifiedCommitDate | 2026-09-30T11:03:56+02:00|
| governingOverview | `dashboard/src/panels/overview.md` |

## Governing Overview

[dashboard/src/panels route overview](../overview.md)

## Purpose

**The central reading path's code and test expressions for a tree comparison (MIK-R31): one focused card per
(path, range), its authored rationale directly above the excerpt, a changed range as its real diff and an
unchanged range once, labelled unchanged.** It replaces the whole-file accordion (`ReviewExpressions.tsx`) for tree
comparisons only; a dataset (unconverted) review never mounts it. Full-file inspection and the complete
changed-file inventory stay one step away from every card (rule 5). The grouping, order and counts are
`focusedCards.ts`'s.

## Code Commentary

### Logic

- **Read states.** `ExpressionCards` shows the layout controls with a status line while the selection's entries
  are loading, `ReviewProblemBlock` when the read is unavailable, and "not a tree comparison" for any other phase;
  otherwise `ReadyCards` renders the cards.
- **`ReadyCards`.** A counts line (`n locations · k changed · m unchanged`, plus `not comparable` when some are
  undetermined, with `data-changed-count` and `data-unchanged-count`), the `ScopeLine` when the roster is bounded,
  an explicit "no realization or proof entry" line when there are none, an `OpenedFile` for a path the explorer
  opened that no card shows, then one `FocusedCard` per card.
- **One full file at a time, in the card that asked (review F1).** The open state is the card's key; a path opened
  from the source explorer opens in the first card of that path. One click gives one `SourceContent` read in the
  clicked card; clicking again closes it.
- **The bounded roster (review F2).** `ScopeLine` says "These cards cover the loaded n of m members", points to the
  roster walk's next-page control, and says the other members' locations are not counted.
- **A card (`FocusedCard`).** Header: "Code expression" or "Test proof" with the roles (a proof shows `facet`), the
  side path and the change badge (`Changed range`, `Unchanged`, `Not comparable`). Then the voices (rule 1: the
  rationale directly above the excerpt), then the side lines (`Before · L…`, `After · L…`, or one "Before and after
  · … · the same text on both sides" line for an unchanged card whose ranges match), then the excerpt, the
  MIK-R03 not-current marks (`<entry> <state> on the <side> side`), and the actions: **Full file**,
  **All changed files (n)** (scrolls to and focuses the source explorer) and **Entry details**.
- **A voice (`Voice`).** The heading names the invariant, the role (or "proof facet"), MIK-R11's planning mark
  when the workspace passed one (`touched invariant · planned`), and "added" or "retired in this leaf". The body is
  the authored rationale (or facet); a missing one is "No authored rationale is recorded for <ID>." (rule 2), never
  generated text. A revised rationale shows its before text under "Revised in this leaf".
- **Excerpts.** `UnchangedExcerpt`: one `FilePane` of the after excerpt, numbered from the range's first line.
  `ChangedExcerpt`: a `DiffPane` of the two excerpts with `collapse={false}` and each side's own first line; a side
  with no file is the empty operand of an added or deleted file. `SeparateSides`: a card whose sides are not both
  regions shows each readable side's text alone and draws no diff. `Truncated` states a prefix excerpt.
- **Side states (Failure and Recovery).** `sideStateText`: `no file on this side`, `unresolved: <reason>`,
  `unavailable: <reason>`; `sideLine` adds "entry not recorded on this side".
- **Full file.** `FullFile` reads through the landed `SourceContent` at the review's own code trees, with the
  inventory entry when the path is listed, else a synthetic unchanged entry ("an unchanged file a recorded entry
  names"), which the server admits for a realization's or, since ruling Q1, a proof's path.

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
- Diagnostic clutter stays in "Entry details" (IDs, blobs, content identities, MIK-R03 reasons).

### Todos

No additional work is asserted by this card.

## Docs References

No domain documentation source is configured; the requirement packet `MIK-R31@v1`, the accepted design
(ICR-R24@v3 "Accepted layout") and the rulings live outside the code and memory repositories, so they are named here
and not cited as rows.

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured live documentation source was available for this pass. | — | — |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The props the centre passes: the read, the seed, the planning marks, layout and open path, and the scope. | `CardsProps` | dashboard/src/panels/review/ExpressionCards.tsx:121-134 |
| Loading, unavailable and not-a-tree-comparison states. | `ExpressionCards` | dashboard/src/panels/review/ExpressionCards.tsx:136-176 |
| The counts, the scope line and one full file keyed by the card (F1). | `ReadyCards`; `ScopeLine` | dashboard/src/panels/review/ExpressionCards.tsx:180-230; dashboard/src/panels/review/ExpressionCards.tsx:233-241 |
| Side lines, one line for an unchanged same region, and the side-state texts. | `sideLine`; `SideLines`; `sameRegion`; `sideStateText` | dashboard/src/panels/review/ExpressionCards.tsx:249-257; dashboard/src/panels/review/ExpressionCards.tsx:259-274; dashboard/src/panels/review/ExpressionCards.tsx:277-286; dashboard/src/panels/review/ExpressionCards.tsx:288-292 |
| One card: header, voices, side lines, excerpt, marks, actions. | `FocusedCard` | dashboard/src/panels/review/ExpressionCards.tsx:294-366 |
| A voice: the authored rationale or facet, or the named gap. | `voiceHeading`; `Voice` | dashboard/src/panels/review/ExpressionCards.tsx:376-382; dashboard/src/panels/review/ExpressionCards.tsx:384-409 |
| Unchanged once, changed as a diff, sides that are not both regions shown apart. | `Excerpt`; `UnchangedExcerpt`; `ChangedExcerpt`; `SeparateSides` | dashboard/src/panels/review/ExpressionCards.tsx:411-417; dashboard/src/panels/review/ExpressionCards.tsx:420-430; dashboard/src/panels/review/ExpressionCards.tsx:434-463; dashboard/src/panels/review/ExpressionCards.tsx:467-483 |
| Entry details kept out of the reading path. | `CardDetails`; `sideFacts` | dashboard/src/panels/review/ExpressionCards.tsx:493-505; dashboard/src/panels/review/ExpressionCards.tsx:507-524 |
| The inventory jump, the full file through the landed content read, and a file opened from the explorer. | `InventoryLink`; `FullFile`; `OpenedFile` | dashboard/src/panels/review/ExpressionCards.tsx:526-545; dashboard/src/panels/review/ExpressionCards.tsx:548-583; dashboard/src/panels/review/ExpressionCards.tsx:587-606 |
| The one caller, which mounts cards only for a tree comparison. | `CenterExpressions` | dashboard/src/panels/review/FamilyReviewCenter.tsx:973-1029 |
| The card-state cases. | "draws a changed range as its real diff and an unchanged range once, labelled unchanged"; "names a missing rationale as a gap and never writes text of its own" | dashboard/src/panels/review/ExpressionCards.test.tsx:66-81; dashboard/src/panels/review/ExpressionCards.test.tsx:137-147 |
| The F1 case. | "opens one full file, in the card that asked, with one read (F1)" | dashboard/src/panels/review/ExpressionCards.test.tsx:209-235 |

## Cross-Repo References

| Finding | Anchor | Source |
| --- | --- | --- |
| No cross-repo boundary is crossed by this file. | — | — |

## Update History

<!-- newest entry by date and time is prepended at the top of the list; prepend-only -->
- 2026-09-30T09:59:20+02:00 — 260928-MIK-L31 curator (staged change set on `ar/260928-mik-l31`, code base `48f680d5b95b8cb6eafff4f1ccd19c8f32e8c48c`; review R3 pass-with-notes): created this card for the new component MIK-R31 adds, recording rulings 05:36:19 Q1 (a proof's path opens in full), 06:10:21 F1 (one full file keyed by card) and F2 (the loaded n of m), and two candidate invariants. The verification stamp is left empty: the file is new and uncommitted; closeout owns the real stamp.
