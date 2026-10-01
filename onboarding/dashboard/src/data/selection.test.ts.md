# dashboard/src/data/selection.test.ts

## Governing Overview

[data overview](overview.md)

## Purpose

Unit tests for the pure selection rules (slice 6f-1): `isIgnoredAnchor` (terminal host / composer /
editable fields are ignored) and `readSelection` (trimmed text + rect, or `null` for a
collapsed/empty/ignored/absent selection), including L8's optional `leafKey` captured from the nearest
task-reader `data-task-leaf-key` ancestor, plus a `renderHook` test for `useSelectionCapture`
(mouse-up snapshot + `clear`).

## Code Commentary

### Logic

Builds real jsdom nodes (`nodeInside(html)` → the deepest text node) and a `fakeSelection` (a minimal
`Selection` with `toString`/`anchorNode`/`getRangeAt().getBoundingClientRect`). Asserts the ignore
matrix (terminal-host / `data-highlight-composer` / `textarea` → ignored; ordinary content → not) and
that `readSelection` returns the trimmed `{ text, rect }` or `null` across the reject cases. A
specific L8 assertion wraps selected text in `<article data-task-leaf-key="repo/master/L8">` and expects
`readSelection` to carry `leafKey: "repo/master/L8"` beside the trimmed text and rect. A
`renderHook` case (fake timers + a stubbed `window.getSelection`) asserts `useSelectionCapture`
snapshots on a `mouseup` (deferred a tick) and `clear()`s on demand. Slice 6g adds two dismiss cases:
a `mouseup` with no live selection clears the snapshot (the handler now mirrors the live selection
rather than only-raising), and `clear()` collapses the live DOM selection (`removeAllRanges` is
called) so a trailing `mouseup` can't re-capture it — the fix for the "click-outside takes several
tries to dismiss" bug; `fakeSelection` gained a `removeAllRanges` stub.

### Conventions

Pure-function tests — no React, no hook; fake `Selection` + jsdom nodes only.

### Invariants And Boundaries

Covers `selection.ts`'s pure exports + the `useSelectionCapture` hook; the composer's two-stage flow
is in `HighlightComposer.test.tsx` (which mocks `useSelectionCapture`).

## Evidence

### Docs References

The curator checked the memory repository's `system/sources.md`; no Domain Documentation entries
are configured. This one-to-one card therefore relies on its direct agents-remember source/tests and
the reviewed task evidence for any current behavioral claim.

No configured Domain Documentation source exists for this file.

### Repo-Internal References

- The rules under test. [1]

### Cross-Repo References

This card maps a repository-local agents-remember source. Import and task-boundary review found no
cross-repository implementation source that governs its behavior.

No applicable cross-repository source was found.
