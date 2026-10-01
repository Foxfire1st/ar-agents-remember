# dashboard/src/types/terminalCatalog.ts

## Governing Overview

[dashboard/src overview](../overview.md)

## Purpose

Mirrors the terminal-catalog wire row consumed by the dashboard. The current binding fields are
`taskDocumentRef` plus `seatRole`; replacement declares the same structural document independently
of runtime session identity.

## Code Commentary

### Logic

`TerminalCatalogRow` carries runtime transport/status, structural binding, replacement declaration,
spawn provenance, control evidence, and terminal outcome. `dispatchBriefEntryId` is an optional
private control-plane receipt proving which durable pinned brief completed the current generation's
spawn transaction. `TaskDocumentRef` is declared locally as the canonical `{repository, path}`
shape used by this catalog wire; it is not imported from the generated projection module. The full
catalog interface now has 66 fields and is checked bidirectionally against the server response
model.

### Conventions

`seatRole` is current binding and `spawnRole` is provenance. Optionality mirrors catalog rows
during creation/migration; current server writers use the structural fields.

### Invariants And Boundaries

- `leafKey` and `replacementForLeaf` are not current wire fields.
- Task document plus role is the stable seat; `id` is the occupant.
- Replacement provenance does not create a second seat identity.
- `dispatchBriefEntryId` is reconciliation/diagnostic evidence, never a destination or public seat
  identity.

### Todos

None.

## Evidence

### Docs References

No Domain Documentation source is configured.

### Repo-Internal References

- The wire row separates runtime identity, structural binding, replacement, and dispatch receipt evidence. [1]
- The canonical task-document pair is declared locally for this catalog wire. [2]

### Cross-Repo References

No cross-repository implementation dependency governs this file.
