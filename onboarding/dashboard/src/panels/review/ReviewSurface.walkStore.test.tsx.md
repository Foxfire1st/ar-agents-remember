# dashboard/src/panels/review/ReviewSurface.walkStore.test.tsx

## Governing Overview

[dashboard/src/panels route overview](../overview.md)

## Purpose

Three mounted store-capture walk cases use a labelled synthetic complete outline over the retained MIK-R33 store-authored review replies. They keep both families across member selection/failure, continue partial family facts in the main page and retain the reading-area member opener; no new backend outline capture is claimed.

Family FAM-F00001 has nine members and FAM-F00002 three. The shared member's review carries both families; INV-PPPPPP belongs to the second family only.

Walk storage across subjects and continuations: j keeps both families, partial families continue in the main page with complete outline rows, and members opened from the reading area keep the first family with k stepping back.
## Code Commentary

### Serving

The file serves its own world through `serve` of `walk.test-utils.tsx`. A review request with a `continuation` parameter gets the continued page of FAM-F00001; a request for the member INV-GGGGGG (its identity read from the family body) answers with a deliberate network failure (`TypeError`), so the last step of the first case is an expected failed read; any other request gets the body whose subject it names among the two family reviews, INV-PPPPPP's review and the shared member's review. `useFirstPage` makes the shared member's review the one captured with a page size of two. The file sets the triage order before each case. Async conditions and test completion use the shared Testing Library and Vitest hang guards.

### The cases

1. **Second-family member and failed explicit unknown selection:** J reaches INV-PPPPPP with one review, both families stay and the first has nine distinct outline subjects and a kept tag; K returns to the second family with no review. INV-GGGGGG is unknown and is not a J/K stop: clicking its compact row explicitly produces the deliberate failed-read problem, retaining selection and both families.
2. **Partial facts, complete outline:** the first family still has nine distinct outline subjects and no tree continuation. Its centre continuation sends one request with that family's ID and the exact cursor. Nine outline subjects persist and the family is kept after returning to the second family.
3. **A member opened from the reading area.** INV-PPPPPP is opened from the reading area's member list with one review request. The tree shows the same families, the first family is kept, and `k` returns to the second family's row.

The store world serves shared and continued family captures with member pages, selecting answers per subject and cursor. Cases assert kept rows after j, outline completeness beside continuation controls, and the reading-area opener preserving the first family. Labels and failed-row helpers name rows for exact assertions.
## Evidence

- The file's statement of its data. [1]
- The answers served by subject and by continuation, including the deliberate failure of INV-GGGGGG's read. [2]
- A member opened from the reading area keeps the first family, and `k` steps back. [5]

- The receipt of the store-authored bodies. [6]
- Subject and cursor answer selection for the store [7]
- Store view helper with row labels [8]
- Family-row click helper for j journeys [9]
- Reading-area opener preserving the first family [11]

- j selects the second family’s changed member and k returns; an explicit selection of the unknown INV-GGGGGG row fails, leaves that row selected, shows the failure and preserves both families. [3]
- A partial family has nine complete synthetic-outline rows and no sidebar continuation; its main-page control sends the cursor in one request and keeps the same outline on subsequent family selection. [4]
- The explicitly selected unknown row names the deliberately failed invariant read and remains selected after failure. [10]
