# dashboard/src/types/terminalOpen.ts

## Governing Overview

[dashboard/src overview](../overview.md)

## Purpose

Defines the strict terminal-open response union. Successful and seat-conflict responses expose the
structural task-document-and-role binding while the runtime session remains the opened occupant.

## Code Commentary

### Logic

The success body returns the accepted structural binding. `TerminalOpenSeatTakenBody` reports a
document-and-role conflict, and launch-conflict retains the live occupant's launch/binding facts.
Selection and kind refusals remain distinct.

### Conventions

The Python response models are authoritative; the TypeScript mirror is hand-maintained and covered by
contract fixtures.

### Invariants And Boundaries

- No leaf-key conflict body remains.
- Conflict identity is task document plus role.
- Requested model/effort provenance remains distinct from effective runtime evidence.

### Todos

None.

## Evidence

### Docs References

No Domain Documentation source is configured.

### Repo-Internal References

- Success returns the accepted structural binding. [1]
- Seat conflicts use task-document and role identity. [2]
- Launch conflict remains a distinct live-occupant result. [3]

### Cross-Repo References

No cross-repository implementation dependency governs this file.
