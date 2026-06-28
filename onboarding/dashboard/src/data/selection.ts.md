# dashboard/src/data/selection.ts

| Field                  | Value                                            |
| ---------------------- | ------------------------------------------------ |
| repository             | agents-remember                                  |
| path                   | `dashboard/src/data/selection.ts`                |
| doc_type               | `file-level-onboarding`                          |
| lastUpdated            | 2026-06-21T02:44+02:00                           |
| lastVerifiedCommitHash | `84e95ad0379cd864af3cbae21b7ffe3fd2d2b1b1`       |
| lastVerifiedCommitDate | 2026-06-28T18:49:06+02:00|
| governingOverview      | `../overview.md`                                 |

## Governing Overview

[dashboard/src overview](../overview.md)

## Purpose

The cockpit text **selection** the highlight composer attaches to (slice 6f). Captured on **mouse-up**
(so the composer never appears mid-drag) and held as a **snapshot**, so clicking into the composer —
which collapses the live DOM selection — never dismisses it. A selection only ever *raises* the
composer; nothing is sent until the operator explicitly Sends (the no-silent-action invariant). Pure
where it can be, so the rules unit-test without a real DOM.

## Code Commentary

### Logic

`useSelectionCapture()` listens for document `mouseup`, **defers one tick** (so the browser finalizes
or collapses the selection), then **mirrors** `readSelection(window.getSelection())` into state — a real
selection raises the composer, an empty one (a click elsewhere) clears it, so one outside click
dismisses reliably. The snapshot survives composer interaction because a release **inside** the composer
(`[data-highlight-composer]`) is skipped (not a new capture). The returned `clear()` (Send / dismiss)
resets the snapshot **and collapses the live DOM selection** (`removeAllRanges`) so the trailing
mouse-up can't re-read the still-present range and re-raise the composer. The pure helpers: `readSelection(sel)` returns `{ text, rect } | null` (`null` for a
collapsed/empty selection or one whose anchor is ignored; `rect` is the range's
`getBoundingClientRect`, the popover anchor), and `isIgnoredAnchor(node)` walks the anchor's nearest
element for `[data-testid="terminal-host"]` (xterm owns its own selection), `[data-highlight-composer]`,
or an editable `input`/`textarea`/`[contenteditable="true"]`.

### Conventions

The pure helpers (`isIgnoredAnchor`, `readSelection`) are split from the hook so the rules test against
fake `Selection`/`Node`s; the hook is the `mouseup` subscription + the snapshot state.

### Invariants And Boundaries

Capture is read-only observation; the **one mutation** is `clear()` collapsing the live selection
(`removeAllRanges`), so a dismiss sticks instead of the trailing mouse-up re-capturing the still-present
range (the multi-click-to-dismiss bug). Capture on mouse-up (not `selectionchange`) keeps the composer
from flickering in mid-drag; the snapshot (not the live selection) keeps it open while the operator
interacts with it. Keyboard-only selection is a follow-up
(no clean "selection complete" event); mouse selection is covered.

## Repo-Internal References

| Finding | Citations | Source Path |
| --- | --- | --- |
| The composer a selection raises. | — | [panels/HighlightComposer.tsx](../panels/HighlightComposer.tsx) |
| The rules + capture tests. | — | [selection.test.ts](selection.test.ts) |

## Update History

- 2026-06-21T02:44+02:00 — Slice 6g (highlight-composer dismiss fix): the `mouseup` handler now **mirrors** the selection (`setSelection(readSelection(...))`, clearing on an empty selection) instead of only-raising, and `clear()` collapses the live DOM selection (`removeAllRanges`). Fixes needing multiple clicks / fast-clicking to dismiss — the old only-raise handler let the trailing mouse-up re-capture the still-present range after the popover had cleared it. Verification metadata pinned until closeout stamps the 6g code commit.
- 2026-06-19T15:59 — Created for task 6 slice 6f-1: the cockpit selection capture (`useSelectionCapture` — **mouse-up** snapshot + `clear`, so the composer doesn't flicker mid-drag and survives clicking into it) + the pure rules (`isIgnoredAnchor` / `readSelection`). Verification metadata pinned until closeout stamps the 6f-1 code commit.
