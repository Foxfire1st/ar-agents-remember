# dashboard/src/panels/file-viewer/markGutter.test.tsx

## Governing Overview

[file-viewer/ overview](overview.md)

## Purpose

**The marks gutter's collapsed runs, redraw focus and return hold (15 cases).** The real `DiffPane` and CodeMirror render
in jsdom for the collapsed-run cases; the redraw and hold cases drive the exported `HostMarker` and `holdRevealed`
directly, because CodeMirror's element reassignment needs a changing viewport that jsdom does not lay out.

## Code Commentary

### Logic

- **Collapsed runs (4; ruling Q4).** Sixty lines with line 2 edited collapse lines 6–60: a mark in that run expands
  it in both editors side by side, for a before-editor mark too, and inline; a run holding no mark stays collapsed.
- **Redraw (3; review R2-F1).** A focused mark keeps its focus when the new gutter element is drawn first and when the
  old one is dropped first; it never takes focus back from where the reader moved it, nor on a later redraw.
- **The hold (8; review R3-F2).** With `requestAnimationFrame` replaced by a frame queue and the document's listener
  calls recorded: a drifted mark is focused and scrolled back while held, and the three releases are added; an undrawn
  line is scrolled to again; the reader's `pointerdown`, `keydown` and `wheel` each end it (one case each, the release
  list spelled out in the test, not read from the module) with no further frame, focus or scroll and all three
  listeners removed; focus moved elsewhere ends it; a torn-down pane ends it; a return nobody touches runs exactly
  `REVEAL_HOLD_FRAMES + 1` frames.

### Conventions

- `held()` builds the hold's fixture; `frame()` runs one queued frame; `ended()` asserts no frame and all listeners removed.

### Invariants And Boundaries

- Pins the hold's end conditions and cleanup (the reviewer's H1–H8 and the worker's H1k, H1w, H9, H10), and the collapsed-run rule (Q4-3, Q4-4).

### Todos

No additional work is asserted by this card.

## Evidence

### Docs References

No domain documentation source is configured; the requirement packet `MIK-R34@v1` (adopting `ICR-R34@v1`), the adopted `ICR-R24@v3` item 2 and the architect's rulings live outside the code and memory repositories, so they are named here and not cited as rows.

No configured live documentation source was available for this pass.

### Repo-Internal References

- Sixty lines, one edit, and the real `DiffPane` with marks. [1]
- Collapsed runs holding a mark are expanded; others stay collapsed. [2]
- A focused mark redrawn keeps focus, never against the reader. [3]
- The hold's pull-back, releases, teardown and frame cap. [4]
- The module under test. [5]

### Cross-Repo References

No cross-repo boundary is crossed by this file.
