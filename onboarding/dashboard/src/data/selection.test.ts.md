# dashboard/src/data/selection.test.ts

| Field                  | Value                                            |
| ---------------------- | ------------------------------------------------ |
| repository             | agents-remember                                  |
| path                   | `dashboard/src/data/selection.test.ts`           |
| doc_type               | `file-level-onboarding`                          |
| lastUpdated            | 2026-06-21T02:44+02:00                           |
| lastVerifiedCommitHash | `84e95ad0379cd864af3cbae21b7ffe3fd2d2b1b1`       |
| lastVerifiedCommitDate | 2026-06-28T18:49:06+02:00|
| governingOverview      | `../overview.md`                                 |

## Governing Overview

[dashboard/src overview](../overview.md)

## Purpose

Unit tests for the pure selection rules (slice 6f-1): `isIgnoredAnchor` (terminal host / composer /
editable fields are ignored) and `readSelection` (trimmed text + rect, or `null` for a
collapsed/empty/ignored/absent selection), plus a `renderHook` test for `useSelectionCapture`
(mouse-up snapshot + `clear`).

## Code Commentary

### Logic

Builds real jsdom nodes (`nodeInside(html)` → the deepest text node) and a `fakeSelection` (a minimal
`Selection` with `toString`/`anchorNode`/`getRangeAt().getBoundingClientRect`). Asserts the ignore
matrix (terminal-host / `data-highlight-composer` / `textarea` → ignored; ordinary content → not) and
that `readSelection` returns the trimmed `{ text, rect }` or `null` across the reject cases. A
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

## Repo-Internal References

| Finding | Citations | Source Path |
| --- | --- | --- |
| The rules under test. | — | [selection.ts](selection.ts) |

## Update History

- 2026-06-21T02:44+02:00 — Slice 6g: added the selection-dismiss tests — an empty `mouseup` clears the snapshot, and `clear()` collapses the live selection (`removeAllRanges` called); `fakeSelection` gained `removeAllRanges`. Verification metadata pinned until closeout stamps the 6g code commit.
- 2026-06-19T15:59 — Created for task 6 slice 6f-1: tests for `isIgnoredAnchor` + `readSelection`. Verification metadata pinned until closeout stamps the 6f-1 code commit.
