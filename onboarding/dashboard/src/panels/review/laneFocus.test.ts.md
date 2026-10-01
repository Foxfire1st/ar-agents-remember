# dashboard/src/panels/review/laneFocus.test.ts

## Governing Overview

[dashboard/src/panels route overview](../overview.md)

## Purpose

**The lane's presentation rules over the real served bodies (3 cases).** It reads the captured per-file
classification (`laneReview.file.captured.json`, the attributed `review_comparison_retention.py`) and the captured
lane (`laneReview.lane.captured.json`) of the MIK-L32 scratch leaf and checks `laneFocus.ts`'s focus, windows and
totals.

## Code Commentary

### Logic

- **Case 1, focus.** The attributed file has a linked edit and an unexplained appended helper; the
  `Unexplained changes` destination opens it on the one unexplained hunk (`L572–577`), the `Unknown attribution`
  destination on none; a file of the destination's own bucket opens on every hunk.
- **Case 2, windows.** On eight lines, a replace of line 4 gives lines 1-7; an insertion after line 6 gives the gap
  between 6 and 7 (window from 4); an insertion before line 1 starts at 1; a hunk past the text held is `beyond`.
- **Case 3, totals.** `Unexplained changes` reads "5 files · 3 hunks · 2 non-text", its groups are three unexplained
  files then two attributed files, the buckets sum to the changed total, and `Unknown attribution` reads "1 file ·
  1 hunk".

### Conventions

- The bodies are read with `readFileSync` next to the test; nothing is synthesised except the one bucket override
  of case 1.

### Invariants And Boundaries

- Proves rule 8's window rule and rule 10's separate totals on real data. The mutations "focus shows every hunk"
  (2 cases fail) and "window ignores the insertion gap" (1) are caught.

### Todos

No additional work is asserted by this card.

## Evidence

### Docs References

No domain documentation source is configured; the requirement packet `MIK-R32@v1` and its rulings live outside the code
and memory repositories, so they are named here and not cited as rows.

No configured live documentation source was available for this pass.

### Repo-Internal References

- The real bodies read. [1]
- Case 1: the destination's hunks of an attributed file. [2]
- Case 2: windows on the server's line numbers. [3]
- Case 3: file and hunk totals, in the server's order. [4]
- The rules under test. [5]

### Cross-Repo References

No cross-repo boundary is crossed by this file.
