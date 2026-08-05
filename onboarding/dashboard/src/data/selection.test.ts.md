# dashboard/src/data/selection.test.ts

| Field                  | Value                                            |
| ---------------------- | ------------------------------------------------ |
| repository             | agents-remember                                  |
| path                   | `dashboard/src/data/selection.test.ts`           |
| doc_type               | `file-level-onboarding`                          |
| lastUpdated | 2026-07-18T07:22+02:00 |
| lastVerifiedCommitHash | `ad30dd38c3dcfa13fb85f44b281488499e92519a`       |
| lastVerifiedCommitDate | 2026-07-03T08:10:19+02:00|
| governingOverview | `overview.md` |

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
| The rules under test. | `isIgnoredAnchor`; `readSelection` | dashboard/src/data/selection.ts:30-32; dashboard/src/data/selection.ts:39-49 |

## Cross-Repo References

This card maps a repository-local agents-remember source. Import and task-boundary review found no
cross-repository implementation source that governs its behavior.

| Finding | Anchor | Source |
| --- | --- | --- |
| No applicable cross-repository source was found. | — | — |

## Update History

- 2026-08-02T16:55+02:00 — 260731-EFA-L6 W1-B08 curator: repaired 1 repo-internal citation row and preserved verification metadata.

- 2026-07-18T07:22+02:00 — FEUI-L8 manual route refactor: retargeted this direct data file card
  from the packed dashboard/src parent to the new nearest data authority overview. Source behavior
  is unchanged by this memory-only governance move; verification hash/date remain pinned.

- 2026-07-02T16:18+02:00 — L8: added coverage that `readSelection` preserves the nearest
  `data-task-leaf-key` as `SelectionContext.leafKey`, enabling task-reader highlights to be routed to
  the adjacent leaf chat. Verification metadata pinned until closeout stamps the L8 commit.
- 2026-06-21T02:44+02:00 — Slice 6g: added the selection-dismiss tests — an empty `mouseup` clears the snapshot, and `clear()` collapses the live selection (`removeAllRanges` called); `fakeSelection` gained `removeAllRanges`. Verification metadata pinned until closeout stamps the 6g code commit.
- 2026-06-19T15:59 — Created for task 6 slice 6f-1: tests for `isIgnoredAnchor` + `readSelection`. Verification metadata pinned until closeout stamps the 6f-1 code commit.
