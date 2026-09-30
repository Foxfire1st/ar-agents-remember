# dashboard/src/panels/file-viewer/markGutter.test.tsx

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `dashboard/src/panels/file-viewer/markGutter.test.tsx` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-30T20:26:08+02:00 |
| lastVerifiedCommitHash | `d3a22213ad3124603b0210afb7e3d049c5589b82`|
| lastVerifiedCommitDate | 2026-09-30T20:52:55+02:00|
| governingOverview | `dashboard/src/panels/file-viewer/overview.md` |

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

## Docs References

No domain documentation source is configured; the requirement packet `MIK-R34@v1` (adopting `ICR-R34@v1`), the adopted `ICR-R24@v3` item 2 and the architect's rulings live outside the code and memory repositories, so they are named here and not cited as rows.

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured live documentation source was available for this pass. | — | — |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| Sixty lines, one edit, and the real `DiffPane` with marks. | `pane`; `collapsedRuns` | dashboard/src/panels/file-viewer/markGutter.test.tsx:18-54 |
| Collapsed runs holding a mark are expanded; others stay collapsed. | "expands the run in both editors of a side-by-side diff"; "leaves a run that holds no mark collapsed, as before" | dashboard/src/panels/file-viewer/markGutter.test.tsx:56-89 |
| A focused mark redrawn keeps focus, never against the reader. | "keeps its focus when the new element is drawn first"; "never takes focus back from where the reader moved it, nor redraws later" | dashboard/src/panels/file-viewer/markGutter.test.tsx:97-156 |
| The hold's pull-back, releases, teardown and frame cap. | `RELEASES`; "ends at its frame cap on a return nobody touches" | dashboard/src/panels/file-viewer/markGutter.test.tsx:161-283 |
| The module under test. | `HostMarker`; `holdRevealed`; `expandMarkedRuns` | dashboard/src/panels/file-viewer/markGutter.tsx:75-101; dashboard/src/panels/file-viewer/markGutter.tsx:195-218; dashboard/src/panels/file-viewer/markGutter.tsx:282-294 |

## Cross-Repo References

| Finding | Anchor | Source |
| --- | --- | --- |
| No cross-repo boundary is crossed by this file. | — | — |

## Update History

<!-- newest entry by date and time is prepended at the top of the list; prepend-only -->
- 2026-09-30T20:26:08+02:00 — 260928-MIK-L34 curator (staged change set on `ar/260928-mik-l34`, code base `904e804b07a598d5d6c66f06b7e67ddab64d9b8e`; reviews R1 to R3 changes-required, each followed by a fix round): created this card for the new gutter test module MIK-R34 adds (15 cases), recording ruling Q4 and review R2-F1, R3-F1 and R3-F2. The verification stamp is left empty: the file is new and uncommitted; closeout owns the real stamp.
