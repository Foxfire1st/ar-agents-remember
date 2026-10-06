# dashboard/src/panels/review/changeTraversal.test.tsx

## Governing Overview

[dashboard/src/panels route overview](../overview.md)

## Purpose

The traversal status of `useChangeTraversal` (requirement MIK-R39 rule 11), tested on the hook alone. 1 case. A mounted test sees only what is left when a turn is over; this file records the status of every render, so it sees the very render in which the tree shows other rows.

## Code Commentary

- `Probe` is a small component that calls `useChangeTraversal(tree, false, rows)` over an empty family list, so every move forward ends at once. It pushes `"<rows>: <status>"` into `rendered` on each render and offers a "next" button that calls `move(1)`.
- The case renders the probe with the rows `first` and clicks "next": the last render shows "No later change in this tree; the selection stays." beside `first`.
- It renders again with the rows `second`: every render beside `second` shows an empty status, the first one included.
- It renders again with `first`: every render shows an empty status, so the message does not come back with the same rows.
- A new click on "next" is answered with the message again.

## Evidence

- The file's statement of why the hook is tested alone. [1]
- The probe that records the status of every render. [2]
- A status is rendered only beside the rows it was said for and never again once other rows were shown. [3]
- The hook that keeps the status with its rows. [4]
