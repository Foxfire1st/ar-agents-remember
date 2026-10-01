# dashboard/src/data/selection.ts

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

## Evidence

### Docs References

The curator checked the memory repository's `system/sources.md`; no Domain Documentation entries
are configured. This one-to-one card therefore relies on its direct agents-remember source/tests and
the reviewed task evidence for any current behavioral claim.

No configured Domain Documentation source exists for this file.

### Repo-Internal References

- The composer a selection raises. [1]
- The rules + capture tests. [2]
- The task reader marker that supplies task leaf ownership. [3]

### Cross-Repo References

This card maps a repository-local agents-remember source. Import and task-boundary review found no
cross-repository implementation source that governs its behavior.

No applicable cross-repository source was found.
