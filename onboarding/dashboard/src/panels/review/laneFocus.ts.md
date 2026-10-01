# dashboard/src/panels/review/laneFocus.ts

## Governing Overview

[dashboard/src/panels route overview](../overview.md)

## Purpose

**The unexplained-changes lane's presentation rules (MIK-R32), kept apart from its components.** Nothing here
classifies: every bucket, hunk and class comes from the server's response. These pure functions choose which of those
hunks a destination focuses on, cut the text window each focused diff shows on the server's side line numbers (rule
8: a mark always sits on the owner's hunk), write the totals lines, and turn the lane into the labels the source
explorer (ruling Q1) and the technical details (review R1 F1) show on a tree comparison.

## Code Commentary

### Logic

- **Destinations.** `DESTINATION_TITLES` (`Unexplained changes`, `Unknown attribution`, the latter named apart from
  the per-member `Attribution unknown` membership state), `GROUP_TITLES` and `GROUP_NOTES` (one line per group saying
  what puts a file there). `destinationOf` picks `unexplained_changes` or `unknown_attribution`;
  `destinationGroups` splits the files at `bucket_files` into the bucket's own files and the attributed files, in the
  server's order; `destinationTotals` writes "5 files · 3 hunks · 2 non-text", file and hunk totals separately.
- **Focus.** `focusedHunks(file, destination)` opens a file of the destination's own bucket on every hunk, and an
  attributed file on its hunks of the destination's class only.
- **Windows.** `spanLabel` gives "L4", "L4–6" or "none (after L5)" for a side where the hunk changes nothing.
  `sideLines` splits a side's text. `hunkWindow(span, lines, context = 3)` returns the window's first line, its text
  and `beyond`: the changed lines (or, on a side with none, the gap after `start`) plus `HUNK_CONTEXT_LINES` (3) on
  each side, clamped to the text; `beyond` is true when the hunk lies past a bounded prefix, so it is never drawn
  from the wrong lines. `FOCUSED_HUNK_LIMIT` (20) caps the windows a focused view draws. Since MIK-L34 the intent
  markers reuse two of these: `sideLines` measures the lines a pane draws, and `spanLabel` names a mark's hunk in its
  accessible name and list heading (`IntentMarkers.tsx`).
- **The explorer's labels (ruling Q1, 2026-09-30T12:19:20).** `EXPLORER_LABELS` maps each bucket to the explorer's
  landed words (`attributed` → `Mapped`, `unexplained` → `Unmapped`, `attribution_unknown` → `Attribution unknown`).
  `explorerAttribution(read, paths)` labels every changed path `Attribution pending` (`EXPLORER_PENDING`) while the
  lane is read, and otherwise by its bucket in `paths`; a path the lane does not list, or an unread lane, is
  `Attribution unknown`, never a guessed bucket.
- **The technical details' facts (review R1 F1, ruling 13:07:38).** `laneAttributionFacts(read)` is `pending`,
  `unknown` (an unread or unavailable lane), or `read` with `partial`, the unexplained paths and the unknown paths.
  `laneCountText(name, facts)` states the landed remaining counts `unattributed_changed_paths` and
  `unknown_attribution_changed_paths` from the lane (the count of each list, marked `(partial)`), or pending or
  unknown; other counts return `undefined` and keep the landed text.

### Conventions

- Pure functions over the served shapes; no fetch, no state.
- The explorer keeps its landed vocabulary; only the source of the label changes on a tree comparison.

### Invariants And Boundaries

- **Part of the candidate invariant "on tree comparisons, the explorer and the technical details take their
  attribution from the lane, so no two surfaces disagree"** (recorded on `review_unexplained_lane.py.md`): realized
  here by `explorerAttribution` and `laneAttributionFacts`; proved by `ReviewSurface.lane.test.tsx` and the gitTrees
  cases; making the explorer ignore the lane fails 3 cases, and forcing the lane facts off fails 3.
- A window's marks sit on the owner's hunks: every window is cut on the server's side line numbers, one per focused
  hunk (rule 8). Since MIK-L34 each window marks every owner hunk whose changed lines it draws, a neighbour shown only
  as context included (`LaneFileFocus.useWindowMarking`).

### Todos

- **Resolved by MIK-L34 (review R1 F5, carried by ruling 2026-09-30T13:07:38):** a window whose context lines show a
  neighbouring hunk now marks that hunk too (the `lines.txt` L4 window draws the L2 replace and the L6 delete, and
  carries three marks: `IntentMarkers.test.tsx`, "marks every hunk a window draws"). The windows here are unchanged;
  the marks are placed in `LaneFileFocus.tsx`. No work remains on this card.

## Evidence

### Docs References

No domain documentation source is configured; the requirement packet `MIK-R32@v1` and its rulings live outside the code
and memory repositories, so they are named here and not cited as rows.

No configured live documentation source was available for this pass.

### Repo-Internal References

- Nothing here classifies; marks sit on the owner's hunks. [1]
- The context and focus bounds; the destination titles. [2]
- One note per group. [3]
- The two groups in the server's order, and the totals line. [4]
- The hunks a destination opens a file on. [5]
- Span labels, side lines and the window on the server's line numbers. [6]
- The explorer's labels from the lane (ruling Q1). [7]
- The technical details' facts and counts from the lane (review F1). [8]
- The workspace's explorer source by kind of review. [9]
- The intent markers' use of the window helpers (MIK-L34). [10]
- The details' counts and lists from the lane. [11]
- The window, focus and totals cases. [12]

### Cross-Repo References

No cross-repo boundary is crossed by this file.
