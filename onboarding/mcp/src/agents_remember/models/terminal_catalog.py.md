# mcp/src/agents_remember/models/terminal_catalog.py

| Field                  | Value                                                       |
| ---------------------- | ----------------------------------------------------------- |
| repository             | agents-remember                                             |
| path                   | `mcp/src/agents_remember/models/terminal_catalog.py`         |
| doc_type               | `file-level-onboarding`                                     |
| lastUpdated | 2026-08-11T14:29+02:00 |
| lastVerifiedCommitHash | `5aff1e8f01dfa949efc8f68e46bc62a99ed31432`                  |
| lastVerifiedCommitDate | 2026-08-14T14:36:50+02:00|
| governingOverview      | `overview.md`                                               |

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
address namespace.

### Conventions

Current readers are strict after startup migration. Optional fields are omitted from JSON when
absent; server response models mirror the emitted key set.

### Invariants And Boundaries

- Seat identity is `(task_document_ref, seat_role)`.
- Runtime id and lifecycle id are private occupant correlation.
- Spawn ancestry is provenance, not hierarchy or authorization.
- One-way migration owns legacy leaf fields; current writers do not.

### Todos

None.

## Docs References

No Domain Documentation source is configured.

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The catalog row separates binding, replacement, and spawn provenance. | `TerminalCatalogEntry` | mcp/src/agents_remember/models/terminal_catalog.py:67-180 |
| Current parsing recognizes task-document references explicitly. | `_optional_task_document_ref` | mcp/src/agents_remember/models/terminal_catalog.py:554-557 |
| Role fallback is isolated to migrated/internal catalog interpretation. | `migrated_seat_role` | mcp/src/agents_remember/models/terminal_catalog.py:677-683 |

## Cross-Repo References

No cross-repository implementation dependency governs this file.

## Update History

- 2026-08-11T14:29+02:00 — Re-read `TerminalCatalogEntry` and widened its citation to include
  the dataclass declaration and current structural fields; verification metadata remains unchanged
  for governed closeout.

- 2026-08-08T14:38+02:00 — 260731-EFA-L9 curator: created for the row-vocabulary move from
  `serving/terminal_catalog.py`; preserved the entry/liveness/parsing knowledge from the old
  serving card and left store behavior to the serving card. Verification metadata pinned until
  closeout stamps the L9 code commit.
