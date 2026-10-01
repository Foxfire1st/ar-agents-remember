# mcp/src/agents_remember/models/terminal_catalog.py

## Governing Overview

[models overview](overview.md)

## Purpose

Defines the plane-owned hosted-occupant catalog row. Stable seat binding is a canonical task document
plus role; the row id, lifecycle, transport, and adapter fields describe the current occupant.

## Code Commentary

### Logic

`TerminalCatalogEntry` serializes structural binding, optional staged replacement, immutable spawn
provenance, control/liveness evidence, terminal outcome, and audit stamps. `seat_role` is current
binding; `spawn_role` is origin. Replacement names the same task document without creating another
address namespace. Since 260821-ARSPAWN-L1 `spawned_by_kind` (`spawnedByKind` on the wire) is the
caller-kind provenance column: a loose `str | None` written only when set, round-tripped
migration-safely through `from_json`/`to_json` (the serving `/api/terminal/sessions` wire model
`TerminalCatalogEntryWire` mirrors the same field when set); the strict `Literal` vocabulary lives
on the producers (`CallerKind`, `SpawnProvenance.spawned_by_kind`, `SpawnAgentSessionResponse.spawnedByKind`).
Reviewer generations additionally persist `structural_parent_task_document_ref` and
`structural_parent_role`. That pair is plane-owned hierarchy—not spawn ancestry or occupant
identity—and lets the same `(document, reviewer)` seat at sprint altitude distinguish the plan and
super-exit generations. JSON round trips both fields only when present. `with_task_binding` retains
the pair only at the identical document+role address and clears it on a move.
ARSPAWN-L2 adds `dispatch_brief_entry_id` (`dispatchBriefEntryId` on the catalog wire), a private
durable receipt used to distinguish an already-briefed current generation from a crash-stranded
spawn after inbox compaction. `with_task_binding` clears `replacement_for_task_document_ref` when a
staged heir is promoted to the canonical binding. It retains `dispatch_brief_entry_id` only when
the resulting document and role are the identical canonical address; a document or role move
clears the address-bound receipt.

### Conventions

Current readers are strict after startup migration. Optional fields are omitted from JSON when
absent; server response models mirror the emitted key set.

### Invariants And Boundaries

- Seat identity is `(task_document_ref, seat_role)`.
- Runtime id and lifecycle id are private occupant correlation.
- Spawn ancestry is provenance, not hierarchy or authorization.
- A reviewer generation's structural parent is a canonical document+role address; occupant ids do
  not become hierarchy authority.
- One-way migration owns legacy leaf fields; current writers do not.
- A pinned-brief receipt is reconciliation evidence, never a seat address.
- A promoted row cannot remain both a primary and a staged replacement.
- Dispatch receipt evidence survives same-seat promotion only; any cross-document or role move
  clears it before publication.

### Todos

None.

## Evidence

### Docs References

No Domain Documentation source is configured.

### Repo-Internal References

- The catalog row separates binding, replacement, spawn provenance, and pinned-brief receipt evidence. [1]
- The catalog row round-trips caller-kind provenance and the dispatch receipt only when set. [2]
- Binding promotion clears its staging marker and preserves receipt evidence only for the identical document-and-role address. [3]
- Current parsing recognizes task-document references explicitly. [4]
- Role fallback is isolated to migrated/internal catalog interpretation. [5]

### Cross-Repo References

No cross-repository implementation dependency governs this file.
