# dashboard/src/panels/review/changeTraversal.test.tsx

## Governing Overview

[Owning route overview](overview.md)

## Purpose

Pure stop selection and hook controls make j/k follow reading-block identities, with end status tied to the exact displayed stop list.

## Code Commentary

### Logic

- Changed model blocks in display order precede lane hunks; unchanged folded locations are not stops. No selection starts at the first block, a subject starts at its own first block, and an end retains selection.
- A subject or folded location without a stop moves relative to its actual place. A shared entry moves from its single grouped card; a family heading enters its members; unread lane files move between surrounding hunks and the lane heading enters its first hunk.
- The render-recording Probe checks that a status appears only with its exact stop list, disappears immediately for other stops, does not revive when the original list returns and reappears only after a new move.
- The enabled zone binds j/k through successive block identities, ignores a textbox and reports No earlier block at the start.

### Invariants And Boundaries

These are declared component or pure-function checks over the fixtures named here. This read-only analysis did not execute the tests; jsdom or width stubs do not establish browser geometry.

## Evidence

- Declared check and its fixture assertions. [5]
- Declared check and its fixture assertions. [6]
- Declared check and its fixture assertions. [7]
- Declared check and its fixture assertions. [8]
- Declared check and its fixture assertions. [9]
- Declared check and its fixture assertions. [10]
- Declared check and its fixture assertions. [11]
- Declared check and its fixture assertions. [12]
- Declared check and its fixture assertions. [13]
- Declared check and its fixture assertions. [14]
- Declared check and its fixture assertions. [15]

## Historical predecessor account

The earlier account follows as provenance. Current assertions and removed journeys are described above.

> # dashboard/src/panels/review/changeTraversal.test.tsx
>
> ## Governing Overview
>
> [dashboard/src/panels route overview](overview.md)
>
> ## Purpose
>
> The traversal status of `useChangeTraversal` (requirement MIK-R39 rule 11), tested on the hook alone. 1 case. A mounted test sees only what is left when a turn is over; this file records the status of every render, so it sees the very render in which the tree shows other rows.
>
> ## Code Commentary
>
> - `Probe` is a small component that calls `useChangeTraversal(tree, false, rows)` over an empty family list, so every move forward ends at once. It pushes `"<rows>: <status>"` into `rendered` on each render and offers a "next" button that calls `move(1)`.
> - The case renders the probe with the rows `first` and clicks "next": the last render shows "No later change in this tree; the selection stays." beside `first`.
> - It renders again with the rows `second`: every render beside `second` shows an empty status, the first one included.
> - It renders again with `first`: every render shows an empty status, so the message does not come back with the same rows.
> - A new click on "next" is answered with the message again.
>
> ## Evidence
>
> - The file's statement of why the hook is tested alone. (historical reference 1)
> - The probe that records the status of every render. (historical reference 2)
> - A status is rendered only beside the rows it was said for and never again once other rows were shown. (historical reference 3)
> - The hook that keeps the status with its rows. (historical reference 4)
