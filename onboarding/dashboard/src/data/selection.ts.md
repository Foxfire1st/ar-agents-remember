# dashboard/src/data/selection.ts

| Field                  | Value                                            |
| ---------------------- | ------------------------------------------------ |
| repository             | agents-remember                                  |
| path                   | `dashboard/src/data/selection.ts`                |
| doc_type               | `file-level-onboarding`                          |
| lastUpdated | 2026-07-18T07:22+02:00 |
| lastVerifiedCommitHash | `d9a1eb82849baea6c0b86735e772a932f4bbdc7c`       |
| lastVerifiedCommitDate | 2026-08-12T00:45:15+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[data overview](overview.md)

## Purpose

The cockpit text **selection** the highlight composer attaches to (slice 6f). Captured on **mouse-up**
(so the composer never appears mid-drag) and held as a **snapshot**, so clicking into the composer —
which collapses the live DOM selection — never dismisses it. L8 extends the snapshot with an optional
task-reader `leafKey`, taken from the nearest `data-task-leaf-key` ancestor, so task content can be
distinguished from global cockpit selections before direct-pasting into a leaf chat. Pure where it can
be, so the rules unit-test without a real DOM.

## Code Commentary

### Logic

`useSelectionCapture()` listens for document `mouseup`, **defers one tick** (so the browser finalizes
or collapses the selection), then **mirrors** `readSelection(window.getSelection())` into state — a real
selection raises the composer, an empty one (a click elsewhere) clears it, so one outside click
dismisses reliably. The snapshot survives composer interaction because a release **inside** the composer
(`[data-highlight-composer]`) is skipped (not a new capture). The returned `clear()` (Send / dismiss)
resets the snapshot **and collapses the live DOM selection** (`removeAllRanges`) so the trailing
mouse-up can't re-read the still-present range and re-raise the composer. The pure helpers:
`readSelection(sel)` returns `{ text, rect, leafKey? } | null` (`null` for a collapsed/empty selection or
one whose anchor is ignored; `rect` is the range's `getBoundingClientRect`, the popover anchor). The
optional `leafKey` is read from the anchor element's nearest `[data-task-leaf-key]`. `isIgnoredAnchor`
walks the anchor's nearest element for `[data-testid="terminal-host"]` (xterm owns its own selection),
`[data-highlight-composer]`, or an editable `input`/`textarea`/`[contenteditable="true"]`.

### Conventions

The pure helpers (`isIgnoredAnchor`, `readSelection`) are split from the hook so the rules test against
fake `Selection`/`Node`s; the hook is the `mouseup` subscription + the snapshot state.

### Invariants And Boundaries

Capture is read-only observation plus DOM-derived context metadata; the **one mutation** is `clear()`
collapsing the live selection (`removeAllRanges`), so a dismiss sticks instead of the trailing mouse-up
re-capturing the still-present range (the multi-click-to-dismiss bug). Capture on mouse-up (not
`selectionchange`) keeps the composer from flickering in mid-drag; the snapshot (not the live selection)
keeps it open while the operator interacts with it. Keyboard-only selection is a follow-up
(no clean "selection complete" event); mouse selection is covered.

## Docs References

The curator checked the memory repository's `system/sources.md`; no Domain Documentation entries
are configured. This one-to-one card therefore relies on its direct agents-remember source/tests and
the reviewed task evidence for any current behavioral claim.

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured Domain Documentation source exists for this file. | — | — |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The composer a selection raises. | "export const HighlightComposer" | dashboard/src/panels/HighlightComposer.tsx:1133-1133 |
| The rules + capture tests. | "carries the task leaf key when the selected text belongs to a task reader" | dashboard/src/data/selection.test.ts:52-57 |
| The task reader marker that supplies task leaf ownership. | "export const DetailPanel" | dashboard/src/panels/detail-panel/DetailPanel.tsx:75-75 |

## Cross-Repo References

This card maps a repository-local agents-remember source. Import and task-boundary review found no
cross-repository implementation source that governs its behavior.

| Finding | Anchor | Source |
| --- | --- | --- |
| No applicable cross-repository source was found. | — | — |

## Update History

- 2026-08-05T00:45:16+02:00 — 260731-EFA-L6 S18-B20 curator: replaced the `n/a` table rows with
  exact anchors and fixer-generated ranges; exact non-fixing check returns zero findings.

- 2026-07-18T07:22+02:00 — FEUI-L8 manual route refactor: retargeted this direct data file card
  from the packed dashboard/src parent to the new nearest data authority overview. Source behavior
  is unchanged by this memory-only governance move; verification hash/date remain pinned.

- 2026-07-02T16:18+02:00 — L8: `SelectionContext` now carries an optional `leafKey` from the nearest
  `data-task-leaf-key` ancestor. This lets `HighlightComposer` distinguish viewed task-leaf selections
  from global cockpit selections before using the direct leaf-chat draft-paste path.
- 2026-06-21T02:44+02:00 — Slice 6g (highlight-composer dismiss fix): the `mouseup` handler now **mirrors** the selection (`setSelection(readSelection(...))`, clearing on an empty selection) instead of only-raising, and `clear()` collapses the live DOM selection (`removeAllRanges`). Fixes needing multiple clicks / fast-clicking to dismiss — the old only-raise handler let the trailing mouse-up re-capture the still-present range after the popover had cleared it. Verification metadata pinned until closeout stamps the 6g code commit.
- 2026-06-19T15:59 — Created for task 6 slice 6f-1: the cockpit selection capture (`useSelectionCapture` — **mouse-up** snapshot + `clear`, so the composer doesn't flicker mid-drag and survives clicking into it) + the pure rules (`isIgnoredAnchor` / `readSelection`). Verification metadata pinned until closeout stamps the 6f-1 code commit.
