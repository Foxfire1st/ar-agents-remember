# dashboard/src/panels/review/ReviewSurface.walkStore.test.tsx

## Governing Overview

[dashboard/src/panels route overview](../overview.md)

## Purpose

The walked family tree in the mounted reviewer on the store-authored comparison (`walkStore.capture-provenance.json`, requirement MIK-R39): a member of the second family only, and a kept family whose members are not all returned. `ReviewSurface` is the real component and only `fetch` is stubbed. 3 cases.

Family FAM-F00001 has nine members and FAM-F00002 three. The shared member's review carries both families; INV-PPPPPP belongs to the second family only.

## Code Commentary

### Serving

The file serves its own world through `serve` of `walk.test-utils.tsx`. A review request with a `continuation` parameter gets the continued page of FAM-F00001; a request for the member INV-GGGGGG (its identity read from the family body) answers with a deliberate network failure (`TypeError`), so the last step of the first case is an expected failed read; any other request gets the body whose subject it names among the two family reviews, INV-PPPPPP's review and the shared member's review. `useFirstPage` makes the shared member's review the one captured with a page size of two. The file sets a test timeout of 60 seconds and the triage order before each case.

### The cases

1. **A member of the second family only, and a failed read.** After the second family's row is clicked, `j` selects INV-PPPPPP with one review request. The tree still shows both families in the same order, the kept tag stands in the first family's block, and that block shows nine member occurrences. `k` returns to the second family's row with no request. A further `k` selects INV-GGGGGG under the kept family, whose read deliberately fails: the requested row stays selected, `review-reading-problem` shows the failure for it, one review request is made, and both families stay.
2. **A kept family with unreturned members.** With the first page of two members per side, in authored order, the first family is marked `data-members-unreturned`. After the second family's row is clicked the first family is kept and shows fewer than nine member occurrences. From its last returned change, `j` moves focus to its continuation control, the status contains "Further members of FAM-F00001 are not yet returned", and no review request is made. The next `j` selects the second family's own row with no request. A click on the control makes exactly one review request, whose subject is the first family and whose `continuation` is the cursor the control held; the first family's review is then shown, the second family is the kept one, and the first family shows more members and still has unreturned ones. After the second family's row is clicked again, the first family is kept and shows the same continued members.
3. **A member opened from the reading area.** INV-PPPPPP is opened from the reading area's member list with one review request. The tree shows the same families, the first family is kept, and `k` returns to the second family's row.

## Evidence

- The file's statement of its data. [1]
- The answers served by subject and by continuation, including the deliberate failure of INV-GGGGGG's read. [2]
- `j` onto a member of the second family only keeps the first family, `k` returns, and a further `k` selects a member of the kept family whose read deliberately fails: the row stays selected, the failure is shown and both families stay. [3]
- `j` stops at a kept family's continuation control and reads nothing; the control continues the family by selecting it; the continued members survive a later selection. [4]
- A member opened from the reading area keeps the first family, and `k` steps back. [5]

- The receipt of the store-authored bodies. [6]
