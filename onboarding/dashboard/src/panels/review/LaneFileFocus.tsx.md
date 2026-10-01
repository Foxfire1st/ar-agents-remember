# dashboard/src/panels/review/LaneFileFocus.tsx

## Governing Overview

[dashboard/src/panels route overview](../overview.md)

## Purpose

**One changed file opened from the unexplained-changes lane (MIK-R32 rules 8 and 10): the actual diff, focused on
the hunks the destination is about, with the full file one control away.** The hunks, their classes and their
reasons are the server's per-file classification (`useReviewFileClassification`); the text is the landed
source-content read of the listed generation, the exact side blobs the source explorer also reads and caches. The
gate's own items for the file (MIK-R10, with the history rows that answer them) are shown beside, through L31's
`UnexplainedGroups`. **Since MIK-R34** every window and the full file carry the per-hunk intent markers, from this
same one per-file read.

## Code Commentary

### Logic

- **The read.** `LaneFileFocus` asks the file's classification; it says "classifying …" while pending and shows the
  owner's problem on a failed read. It takes the destination's hunks (`focusedHunks`) and the inventory entry for
  the path (or `fallbackEntry` from the classification), and needs both code generations of the inventory, else it
  says no content can be opened.
- **Facts.** `FileFacts` shows the bucket and the per-class counts, the reason behind "Why this attribution", a
  non-text change's content, mode flag and the gate's linkage ("the gate holds it unexplained", or "of unknown
  linkage"), and each side whose knowledge is unavailable with its detail.
- **Focused diffs.** `FocusedDiffs` makes one `useSourceContentRead` (now exported by `SourceContent.tsx`), shows the
  owner's problem with a retry, and draws at most `FOCUSED_HUNK_LIMIT` (20) hunks, keyed by `hunkMarkers.hunkKey`.
  Above the windows it draws the file's one file-level mark (`IntentMarkers.FileMark`) when the file carries one: a
  confirmed-unregistered file, or one neither side of which has readable knowledge. **The note for the hunks it does
  not draw is accurate since MIK-L34 (the L32 review F5 carry):** it says that many hunks of this class are not drawn
  here, and that Full file draws every changed region of the text its read returns, each owner hunk with its own mark
  (or, for a file-level-marked file, under the one mark the file carries). It no longer says "the full file shows
  every one", which read as though every classified hunk carried a mark there.
  `FocusedHunk` heads each window with its class badge and "before L… → after L…" spans and lists its unknown
  reasons per side. `HunkExcerpt` cuts each side's window with `hunkWindow` on the server's line numbers
  (`sideWindow`) and draws a `DiffPane` (both sides as text) or a `FilePane` (one side), with `firstLine` so the
  gutter numbers are the file's; a hunk past the bounded text is named, never drawn from the wrong lines.
- **The marks of a window (MIK-L34, the L32 review F5 carry ruled 2026-09-30T13:07:38).** `useWindowMarking` gives
  each window its own pane (`lane-window:<hunkKey>`) and the file lines each side draws (`drawnLines`), and marks
  **every owner hunk whose changed lines the window draws**: the focused hunk and any neighbour its three context
  lines show, each on its own side lines, so a neighbour drawn as context is never an unmarked change. It marks only
  inside the workspace's marker scope, only for a file with per-hunk marks, and only when the classification's side
  blobs are the drawn objects (`IntentMarkers.describesDrawn`). A one-sided window places as a split pane and its
  `FilePane` receives only the drawn side's marks (`sideMarks`); the open marker's list renders below the window.
- **Full file.** `FullFile` toggles the landed `SourceContent` for the entry and generation, handing it the lane's own
  classification with the pane name `lane-full` (`markers`), so the one per-file read also marks the full file. A
  return to a marker followed from the full file opens it again (its initial state reads the scope's `returning`).
- **The gate's items.** `GateItems` takes a `GateRead`: `reading` ("Reading the gate's items for this file…",
  never "none" while the slower leaf-wide read has not answered), `none` with why, or `read` with the worklist, whose
  `worklistGroups(...).unexplained` groups for this path render through `UnexplainedGroups`; with none it says the
  gate raised no unexplained item for the file. The workspace builds the `GateRead` (`gateRead`) only from a
  leaf-wide read of the same comparison.

### Conventions

- One window per focused server hunk, and one mark per owner hunk a window draws: a displayed change region never
  merges two owner hunks under one mark (rule 8), and a neighbour shown as context keeps its own mark (MIK-L34).
- The gate may differ from the lane's classification; neither is changed by the other.

### Invariants And Boundaries

- Nothing here assesses, approves, waives or explains a change (the adopted Exclusions): the gate's items are shown
  with their answering rows, and no disposition control is offered.
- The content read is the landed one (same request type, same cache), so the lane opens exactly the bytes the source
  explorer would.

### Todos

- **Resolved by MIK-L34 (review R1 F5, carried by ruling 2026-09-30T13:07:38):** every owner hunk a window draws,
  including a neighbour shown only as context, now carries its own intent mark, and the more-hunks note says what
  the full file draws instead of "the full file shows every one". No work remains on this card.

## Evidence

### Docs References

No domain documentation source is configured; the requirement packet `MIK-R32@v1` and its rulings live outside the code
and memory repositories, so they are named here and not cited as rows.

No configured live documentation source was available for this pass.

### Repo-Internal References

- The focused diff, the exact blobs, every drawn owner hunk's own intent mark (MIK-L34) and the gate's items beside, in the module's own words. [1]
- The gate read's three states and the task a file is opened in. [2]
- One opened file: its classification, facts, focused diffs, full file and gate items. [3]
- The bucket, counts, reason, non-text fact and unread sides. [4]
- One content read; the file-level mark once above at most twenty hunk windows; what the full file draws of the hunks not drawn here (MIK-L34, F5). [5]
- One hunk's badge, spans, reasons and window on the server's line numbers. [6]
- The full file one control away, marked from the lane's own classification and reopened by a return to a marker followed from it (MIK-L34). [7]
- A window's marks: every owner hunk whose changed lines it draws, on its own pane, only for the drawn blobs (MIK-L34). [8]
- The window cases: three marks in the one window whose context draws two neighbours, a neighbour's list from that window, the more-hunks wording, and the full file's return. [9]
- The gate's items: reading, none, or the file's groups. [10]
- The gate read, only from the same comparison's leaf-wide read. [11]
- The content read, exported for this file. [12]
- The file's groups, rendered as the leaf panel renders them. [13]
- A focused hunk, the full file control and the gate's item; "reading", never "none". [14]

### Cross-Repo References

No cross-repo boundary is crossed by this file.
