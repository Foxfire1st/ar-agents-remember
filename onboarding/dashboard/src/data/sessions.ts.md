# dashboard/src/data/sessions.ts

## Governing Overview

[data overview](overview.md)

## Purpose

Owns the browser's catalog-backed hosted-session registry and connection registry. Structural seat
binding is carried as a canonical task-document reference plus role; session and lifecycle ids remain
runtime correlation and do not define the seat.

## Code Commentary

### Logic

`OpenSession` mirrors the terminal catalog's structural binding. Store mutations clear duplicate live
occupants only for the same task-document-and-role pair, and `applyTaskAssignment` atomically applies
the server-accepted binding. `findSessionForTask` resolves one live occupant by structural address.
Catalog hydration maps `taskDocumentRef`, role, replacement, provenance, control, and terminal truth
without deriving identity from labels or spawn ancestry. The separate connection registry remains an
imperative PTY transport seam.

### Conventions

`seatRole` is current binding; `spawnRole` is provenance. Lifecycle lookup remains for runtime UI
correlation, while Chats grouping and targeting use task-document identity.

### Invariants And Boundaries

- Seat uniqueness is scoped to one task document and one role.
- A replacement session may occupy the same structural seat without changing its address.
- Browser state never manufactures sprint/master anchor leaves.
- Raw connection transport is not reliable structural-message delivery.

### Todos

None.

## Evidence

### Docs References

No Domain Documentation source is configured; repository source and tests govern this card.

### Repo-Internal References

- The client row carries structural binding separately from runtime identity. [1]
- Assignment updates and uniqueness use task-document plus role. [2]
- Live lookup resolves the current occupant of a structural seat. [3]
- Catalog hydration preserves the server-owned structural row. [4]

### Cross-Repo References

No cross-repository implementation dependency governs this file.
