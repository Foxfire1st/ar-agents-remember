# dashboard/src/panels/review/IntentMarkers.tsx

## Governing Overview

[dashboard/src/panels route overview](../overview.md)

## Purpose

**The reviewer's per-hunk intent markers in its diffs (MIK-R34, adopting ICR-R34@v1): each hunk of a changed text file
names the invariants whose recorded ranges meet its changed lines; following one opens that invariant at its tree
position, and `Back to <file>` returns to the hunk with focus on its marker.** Every mark comes from the one per-file
classification (MIK-R32) through `hunkMarkers.ts`, placed on the side line numbers it names, and sits in the diff's own
gutter (`file-viewer/markGutter.tsx`); a mark's list opens below the pane. The module serves every diff surface of a
tree comparison's workspace: the landed source-content view (the explorer's opened file, `Expand full file`, a card's
and the lane's full file), the lane's focused windows (through `LaneFileFocus.tsx`) and the card excerpts. Nothing here
edits, comments on or assesses a change (the adopted Exclusions).

## Code Commentary

### Logic

- **One pane's marks (`usePaneMarking`).** Given `{ path, pane, file, layout, window, whole? }` inside the workspace's
  scope: a file with a file-level mark gets only that note (`FileMarkNote`); otherwise every owner hunk is placed by
  `markAnchor`, and each placed hunk becomes a `PaneMark` whose node is its `MarkButton`. The pane name
  (`opened`, `file`, `lane-full`, `lane-window:<hunk>`, `card:<key>`, `card-excerpt:<key>`) makes a return land in the
  pane the marker was followed from: `returningHunk` picks the scope's `returning` hunk for this path and pane, which
  becomes the gutter's `reveal` and reopens its list (initial state and effect), and `onRevealed` is the scope's
  `settle`. A whole-text pane names the hunks it could not place (`PastTextNote`: past the bounded text) instead of
  dropping them.
- **The mark (`MarkButton`).** A button with `data-mark` (tone), `data-hunk`, `data-before`/`data-after` spans and
  `data-compact`; `aria-expanded`, `aria-controls` while open, and `aria-label`/`title` `<label> · hunk before L…,
  after L…`. **Below 40rem it shows the compact text** through `::after` from `data-compact`, with the full label kept
  as its hidden text, name and title (review R1 F2).
- **The list (`MarkPanel`, `EntryList`).** The label and spans, a Close control, "Intents (n)" for realization
  entries and "Tests (n)" for proof entries (each marked `· test` with its facets), each entry with its revisions and
  entry ids and one button per family occurrence (`occurrenceLabel`, its sides and revision) that follows the target
  through the scope (`follow({ path, pane, hunk }, target)`); the per-side unknown lines; and one sentence per tone,
  for a linked hunk "Listed because a recorded range meets a changed line of this hunk; that asserts no coverage,
  correctness or preservation." (ICR-R34 rule 5).
- **The file-level mark.** `FileMark` (for a view that draws it once above several panes, the lane's windows) and
  `FileMarkNote`: one mark for the whole file of a confirmed-unregistered path, or one note that neither side's
  knowledge could be read; nothing for a file with per-hunk marks or outside a workspace.
- **The source-content view (`useSourceMarking`).** Reads the classification through `useMarkClassification` (only
  for a changed file; the caller's `classification` when it holds one, as the lane's full file does), places marks
  only when `describesDrawn` holds (the classification's two side blobs are the drawn objects' ids), over each whole
  side (`sideWindow`, `sourceInput`: the layout on screen when both sides are drawn, else split placement), and
  prefixes `MarkReadNote`.
- **Never silence (`MarkReadNote`).** A changed file shows why it has no marks: `unlisted` ("the change inventory is
  partial and does not list this path, so its classification is not read"; review R1 F5), `loading`, `unavailable`
  with the owner's code and detail, or `other-content` ("the classification describes other content of this path
  than the text drawn here"). A card excerpt stays quiet only while its read is under way.
- **Card excerpts (`useExcerptMarking`; ruling Q4, review R1 F1).** Active only for a card whose two blobs differ (an
  unchanged file's card asks nothing; review R2). `excerptWindow` gives the lines each drawn side's resolved range
  covers; `drawnSidesMatch` compares **only the sides the excerpt draws** with the classification's blobs, so an
  unreadable memory side, which serves no blob, never removes the drawn side's marks, and a drawn side of other
  content says so. The pane is `card-excerpt:<key>`.
- **Helpers and the return.** `sideMarks` gives a one-sided pane its side's marks. `MarkerReturn` renders
  `← Back to <file name>` (with `data-return-path`, `-pane`, `-hunk`, the full path as title) while a followed marker
  has not been returned to; its click is the scope's `back`.

### Conventions

- Test ids: `review-hunk-mark`, `review-hunk-mark-panel`, `review-hunk-mark-group`, `review-hunk-mark-entry`,
  `review-hunk-mark-facet`, `review-hunk-mark-occurrence`, `review-hunk-mark-unknown`, `review-file-mark`,
  `review-marks-past-text`, `review-marks-state` (with `data-marks-state`), `review-marker-return`.
- Panda `css` constants in the file; the tones reuse the lane's colours (cyan linked, amber unexplained, dashed muted
  unknown).
- The mark button carries `data-path`, which also keeps the surface's generic button chrome off a gutter mark.

### Invariants And Boundaries

- **Candidate invariant (not ingested): every hunk drawn in any diff surface carries its mark: lane windows, full
  files and card excerpts, including hunks inside collapsed runs.** Realized by `usePaneMarking` (every owner hunk a
  pane draws is placed), `useSourceMarking` (full files), `useExcerptMarking` (card excerpts, only the drawn sides
  compared), `LaneFileFocus.useWindowMarking` (a window marks each neighbour its context shows: the L32 F5 carry,
  ruling 2026-09-30T13:07:38) and `markGutter.expandMarkedRuns` (no mark in a collapsed run, ruling Q4); a mark is
  withheld only when the drawn text is not the classified text, and then the pane says so. Proved by
  `IntentMarkers.test.tsx` (full diff, lane windows with three marks in the F5 window, card excerpts with an unreadable
  memory side, the other-content and unchanged cases), `markGutter.test.tsx` (collapsed runs), the surface case's card
  excerpts, and the mutation sets (M7, Q4-1 to Q4-4, F1, N3 and R2-3 all caught).
- Nothing here computes an intersection: marks and lists are `hunkMarkers.ts`'s reading of the owner's response.
- Outside a tree comparison's workspace there is no scope, and every surface renders exactly as landed.

### Todos

No additional work is asserted by this card.

## Evidence

### Docs References

No domain documentation source is configured; the requirement packet `MIK-R34@v1` (adopting `ICR-R34@v1`), the adopted `ICR-R24@v3` item 2 and the architect's rulings live outside the code and memory repositories, so they are named here and not cited as rows.

No configured live documentation source was available for this pass.

### Repo-Internal References

- The module's own statement: marks from the one classification, in the diff's own gutter; no editing, commenting or assessment. [1]
- A pane's input, named so a return lands in the pane a marker was followed from. [2]
- Placing every owner hunk a pane draws, the reveal and list reopened on a return, and hunks past a bounded text named. [3]
- The mark: tone, spans, compact text below 40rem, and its accessible name (review R1 F2). [4]
- The list: intents and tests apart, occurrences that follow their target, unknown lines, and the intersection-only sentence. [5]
- The file-level mark and the past-text note. [6]
- The source-content view: marks only on the drawn blobs the classification names. [7]
- Card excerpts: only the drawn sides compared (review R1 F1); an unchanged file's card never active. [8]
- Why a changed file shows no marks: unlisted, loading, unavailable or other content; never silence (review R1 F5). [9]
- One side's marks, and `Back to <file>`. [10]
- The renderers that place it: the source view, the lane windows and full file, and the card excerpts. [11]
- The renderer cases. [12]

### Cross-Repo References

No cross-repo boundary is crossed by this file.
