# dashboard/src/data/terminal.ts

## Governing Overview

[data overview](overview.md)

## Purpose

Provides browser terminal transport and the terminal catalog HTTP adapters. Its assignment write now
sends a canonical task-document reference plus role; runtime session id is used only to identify the
hosted occupant being changed.

## Code Commentary

### Logic

PTY WebSocket connection, catalog fetch, termination, and opener re-exports remain transport concerns.
`attachSessionToTask` posts `taskDocumentRef` and `role` to the assignment route and classifies the
strict `ok | seat-taken | error` result. It does not retain the deleted leaf-assignment request.

### Conventions

Callers derive task references from projected documents before entering this adapter. The server is
authoritative for uniqueness and returns the accepted structural binding.

### Invariants And Boundaries

- No leaf-key compatibility body is emitted.
- A session id selects the occupant for this operator/API mutation, never the durable seat.
- Terminal transport closure and durable terminal outcome remain distinct.

### Todos

None.

## Evidence

### Docs References

No Domain Documentation source is configured.

### Repo-Internal References

- The client exposes a structural task-assignment result family. [1]
- Assignment posts a task-document reference and role. [2]
- Terminal transport remains a separate connection concern. [3]

### Cross-Repo References

No cross-repository implementation dependency governs this file.
