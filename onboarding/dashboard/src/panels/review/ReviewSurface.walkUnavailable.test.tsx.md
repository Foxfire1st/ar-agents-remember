# dashboard/src/panels/review/ReviewSurface.walkUnavailable.test.tsx

## Governing Overview

[dashboard/src/panels route overview](../overview.md)

## Purpose

The stacked-layout reveal of an in-tree selection whose read fails or is refused (OR-R033, OR-R042), in the mounted reviewer on its captured real-data world (`walkReal.capture-provenance.json`, `walk.test-utils.tsx`), with one genuine refused answer (`walkUnavailable.refused.captured.json`). `ReviewSurface` is the real component and only `fetch` is stubbed. 10 cases: eight reveal cases over failed/refused × click/key × stacked/wide, and two moved-focus guards.

The case state is built in two steps. Every case first clicks the second family's row (FAM-2HBJREC2), so the second family is the selected subject and the first family FAM-R6R095RW is kept. The click cases then select the target member INV-2E8MG43K in the kept first family; the key cases first click FAM-R6R095RW's own row (lines 65-72), so the first family becomes the selected subject, the second family is kept, and one `j` reaches INV-2E8MG43K as the first change of the selected family.

## Code Commentary

### The world

`installWorld()` mounts the preserved `walkReal` world of `walk.test-utils.tsx`, in which `world.answer` can be replaced per case. `TARGET` is the review of INV-2E8MG43K; `REFUSED` is the captured HTTP 400 body. `viewport(stacked, run)` substitutes `window.matchMedia` so exactly the `(max-width: 60rem)` query answers `stacked`, and records every `scrollIntoView` call in an array (jsdom has no implementation), restoring both afterwards. `targetRow` finds the selected member's row inside the kept family's block by its revision.

### The reveal cases

`cases` is the matrix `[true, false] × ['failed', 'refused'] × ['click', 'key']`. Each case:

- opens the shared member's review and clicks the second family's row, so the first family FAM-R6R095RW is kept;
- replaces the answer of the target subject with a `TypeError` (failed) or with `REFUSED` (refused);
- selects the target row: a click on INV-2E8MG43K in the kept first family, or, for the key cases, a click on FAM-R6R095RW's own row first and one `j` onto INV-2E8MG43K as the first change of the selected family;
- waits for the status block (`review-reading-problem`) and asserts: the block names the requested invariant; exactly the reading-area column came into view when `stacked`, and nothing else ever does when wide; the selection mark is on the requested row; document focus is on that row; both families are still shown; the workspace is the same node; and exactly one review read was made.

### The moved-focus guards

Two cases, one per outcome, hold the target read on a promise, move focus to the tree's filter while the read is pending, then release it. The status block appears, but nothing is scrolled, focus stays on the filter, and the mark and both families stay. This is the one exception OR-R042 keeps: a reader who moved focus while the read was on its way keeps it and gets no reveal.

### Helpers

`targetRow` and `viewport`; everything else comes from `walk.test-utils.tsx` (`open`, `clickedSecondFamily`, `families`, `familyBlock`, `selectedNode`, `step`, `reviewCount`, `subjectOf`, `revisionOf`, `J`, `WAIT`, `world`).

### Boundaries

- The in-tree restriction and the preservation of the focus request are pinned by no failing test: a mutation that reveals for every selection on the stacked layout, or one that uses up the focus request, leaves the suite green (reviewer note N1). Both behave correctly in the real browser, and the reveal's other conditions are pinned by the cases above.
- The reveal is a presentation step. The read, the selection mark, the tree and the request counts belong to the invariants on the walked tree and the focus request.

## Evidence

- The genuine refused answer: the real route asked for an invariant selector absent from the comparison, HTTP 400. [1]
- The receipt of that capture: route, parameters, status, hash and size, and that it is replayed, not authored. [2]
- The eight reveal cases enumerate failed/refused × click/key × stacked/wide. [3]
- A failed or refused in-tree selection reveals the status only on the stacked layout, keeps the mark and both families, and makes one read. [4]
- A reader who moved focus while the read was on its way keeps it: no scroll, mark and families stay. [5]
