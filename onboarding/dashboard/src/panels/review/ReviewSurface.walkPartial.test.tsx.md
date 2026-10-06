# dashboard/src/panels/review/ReviewSurface.walkPartial.test.tsx

## Governing Overview

[dashboard/src/panels route overview](../overview.md)

## Purpose

A kept family whose members are not all returned, on a real partial answer (requirement MIK-R39 rules 8 and 11). The real route was asked for the shared member INV-2TQGXFAX with its own `pageSize=2`, so both of its families return two members per side (`walkReal.INV-2TQGXFAX-page2`, and the continued page `walkReal.FAM-R6R095RW-continued`; the receipt's `partial_round` note). `ReviewSurface` is the real component and only `fetch` is stubbed. 2 cases.

## Code Commentary

### Serving

The file uses the real-data world of `walk.test-utils.tsx` (`installWorld`) and, before each test, replaces its answer: a review request with a `continuation` parameter gets the continued page, and the shared member's review is the paged body.

### Case 1: `j` stops at the control of a kept partial family

- With two members returned per side the second family weighs more, so the tree shows FAM-2HBJREC2 before FAM-R6R095RW. The second family's row is clicked.
- The first family is then kept, is marked `data-members-unreturned`, and shows three member occurrences.
- From its last returned change, `j` moves focus to its continuation control, the status contains "are not yet returned", and no review request is made.
- The next `j` reports "No later change in this tree; the selection stays.", still with no request: the kept family is the last in the displayed order. The second family's row stays selected.
- A click on the control makes exactly one review request, with `selectorKind` `family` and the cursor the control held. The first family's review is shown, it shows more than three member occurrences, and the second family is the kept one.
- After the continuation returned members the status is empty: "No later change" was said of the tree before those members were returned.

### Case 2: the order control changes the rows a message was said for

- In triage order the second family is listed first and its own row is the first change. `k` reports "No earlier change in this tree; the selection stays." with no request.
- One click on the order control, awaited until the control shows `authored`, lists the first family before the second. The status is empty, and `k` selects a row of the first family.

## Evidence

- The file's statement of its data. [5]
- The paged body and the continued page replace the world's answers. [6]
- `j` stops at the control of a kept real partial family and reads nothing; the control continues the family by selecting it; the end message is gone once the continuation returned members. [7]
- "No earlier change" is dropped when the order control lists the other family before the selection. [8]
- The receipt of the two partial bodies. [9]
