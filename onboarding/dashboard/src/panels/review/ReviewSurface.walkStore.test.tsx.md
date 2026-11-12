# dashboard/src/panels/review/ReviewSurface.walkStore.test.tsx

## Governing Overview

[Owning route overview](overview.md)

## Purpose

Synthetic complete outlines over captured store replies preserve family occurrence context through row selection, failure and main-page continuation.

## Code Commentary

### Logic

- A row click opens the second-family-only member with one review and keeps the first family's nine members; an explicitly selected unknown member then shows the named transport failure while keeping both families and the selection.
- A partial family has nine complete outline subjects and no tree continuation; its center control sends its exact family ID/cursor in one read, and later family selection preserves that outline.
- Opening the second family's member through its reading slot makes one review, keeps the first family tagged and marks the member under the second family.

### Invariants And Boundaries

These are declared component or pure-function checks over the fixtures named here. This read-only analysis did not execute the tests; jsdom or width stubs do not establish browser geometry.

## Evidence

- Declared check and its fixture assertions. [12]
- Declared check and its fixture assertions.
- Declared check and its fixture assertions. [14]

## Historical predecessor account

The earlier account follows as provenance. Current assertions and removed journeys are described above.

> # dashboard/src/panels/review/ReviewSurface.walkStore.test.tsx
>
> ## Governing Overview
>
> [dashboard/src/panels route overview](overview.md)
>
> ## Purpose
>
> Three mounted store-capture walk cases use a labelled synthetic complete outline over the retained MIK-R33 store-authored review replies. They keep both families across member selection/failure, continue partial family facts in the main page and retain the reading-area member opener; no new backend outline capture is claimed.
>
> Family FAM-F00001 has nine members and FAM-F00002 three. The shared member's review carries both families; INV-PPPPPP belongs to the second family only.
>
> Walk storage across subjects and continuations: j keeps both families, partial families continue in the main page with complete outline rows, and members opened from the reading area keep the first family with k stepping back.
> ## Code Commentary
>
> ### Serving
>
> The file serves its own world through `serve` of `walk.test-utils.tsx`. A review request with a `continuation` parameter gets the continued page of FAM-F00001; a request for the member INV-GGGGGG (its identity read from the family body) answers with a deliberate network failure (`TypeError`), so the last step of the first case is an expected failed read; any other request gets the body whose subject it names among the two family reviews, INV-PPPPPP's review and the shared member's review. `useFirstPage` makes the shared member's review the one captured with a page size of two. The file sets the triage order before each case. Async conditions and test completion use the shared Testing Library and Vitest hang guards.
>
> ### The cases
>
> 1. **Second-family member and failed explicit unknown selection:** J reaches INV-PPPPPP with one review, both families stay and the first has nine distinct outline subjects and a kept tag; K returns to the second family with no review. INV-GGGGGG is unknown and is not a J/K stop: clicking its compact row explicitly produces the deliberate failed-read problem, retaining selection and both families.
> 2. **Partial facts, complete outline:** the first family still has nine distinct outline subjects and no tree continuation. Its centre continuation sends one request with that family's ID and the exact cursor. Nine outline subjects persist and the family is kept after returning to the second family.
> 3. **A member opened from the reading area.** INV-PPPPPP is opened from the reading area's member list with one review request. The tree shows the same families, the first family is kept, and `k` returns to the second family's row.
>
> The store world serves shared and continued family captures with member pages, selecting answers per subject and cursor. Cases assert kept rows after j, outline completeness beside continuation controls, and the reading-area opener preserving the first family. Labels and failed-row helpers name rows for exact assertions.
> ## Evidence
>
> - The file's statement of its data. (historical reference 1)
> - The answers served by subject and by continuation, including the deliberate failure of INV-GGGGGG's read. (historical reference 2)
> - A member opened from the reading area keeps the first family, and `k` steps back. (historical reference 5)
>
> - The receipt of the store-authored bodies. (historical reference 6)
> - Subject and cursor answer selection for the store (historical reference 7)
> - Store view helper with row labels (historical reference 8)
> - Family-row click helper for j journeys (historical reference 9)
> - Reading-area opener preserving the first family (historical reference 11)
>
> - j selects the second family’s changed member and k returns; an explicit selection of the unknown INV-GGGGGG row fails, leaves that row selected, shows the failure and preserves both families. (historical reference 3)
> - A partial family has nine complete synthetic-outline rows and no sidebar continuation; its main-page control sends the cursor in one request and keeps the same outline on subsequent family selection. (historical reference 4)
> - The explicitly selected unknown row names the deliberately failed invariant read and remains selected after failure. (historical reference 10)

- Retired at the fifth freeze d59c3493: dashboard/src/panels/review/ReviewSurface.walkStore.test.tsx:140-167 - the region it cited is not in the file at the candidate and no re-point was possible; it was removed in commit 23cb164fa24dcbc4a98a56fa1324e1fb42c1bf41. Retired means the anchor no longer stands, not that the cited subject was deleted.
