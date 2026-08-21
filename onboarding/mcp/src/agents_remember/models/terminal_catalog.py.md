# mcp/src/agents_remember/models/terminal_catalog.py

| Field                  | Value                                                       |
| ---------------------- | ----------------------------------------------------------- |
| repository             | agents-remember                                             |
| path                   | `mcp/src/agents_remember/models/terminal_catalog.py`         |
| doc_type               | `file-level-onboarding`                                     |
| lastUpdated | 2026-08-11T14:29+02:00 |
| lastVerifiedCommitHash | `3eafc555c848ac45a07a07720641f1735f8df0eb`                  |
| lastVerifiedCommitDate | 2026-08-21T05:15:52+02:00|
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
address namespace. Since 260821-ARSPAWN-L1 `spawned_by_kind` (`spawnedByKind` on the wire) is the
caller-kind provenance column: a loose `str | None` written only when set, round-tripped
migration-safely through `from_json`/`to_json` (the serving `/api/terminal/sessions` wire model
`TerminalCatalogEntryWire` mirrors the same field when set); the strict `Literal` vocabulary lives
on the producers (`CallerKind`, `SpawnProvenance.spawned_by_kind`, `SpawnAgentSessionResponse.spawnedByKind`).

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
| The catalog row round-trips caller-kind provenance only when set. | `TerminalCatalogEntry.spawned_by_kind`; `from_json`; `to_json` | mcp/src/agents_remember/models/terminal_catalog.py:99-99; mcp/src/agents_remember/models/terminal_catalog.py:182-266; mcp/src/agents_remember/models/terminal_catalog.py:268-352 |
| Current parsing recognizes task-document references explicitly. | `_optional_task_document_ref` | mcp/src/agents_remember/models/terminal_catalog.py:554-557 |
| Role fallback is isolated to migrated/internal catalog interpretation. | `migrated_seat_role` | mcp/src/agents_remember/models/terminal_catalog.py:677-683 |

## Cross-Repo References

No cross-repository implementation dependency governs this file.

## Update History

- 2026-08-21T03:30+02:00 — 260821-ARSPAWN-L1 fix round 2: the serving `/api/terminal/sessions` wire model (`TerminalCatalogEntryWire`) mirrors `spawnedByKind` when set, alongside this row's `to_json` emission. Verification metadata pinned until closeout stamps the 260821-ARSPAWN-L1 commit.

- 2026-08-21T02:50+02:00 — 260821-ARSPAWN-L1: `TerminalCatalogEntry.spawned_by_kind` (`spawnedByKind` on the wire) round-trips caller-kind provenance written-only-when-set, migration-safe; the strict vocabulary lives on the producers. Verification metadata pinned until closeout stamps the 260821-ARSPAWN-L1 commit.

- 2026-08-11T14:29+02:00 — Re-read `TerminalCatalogEntry` and widened its citation to include
  the dataclass declaration and current structural fields; verification metadata remains unchanged
  for governed closeout.

- 2026-08-08T14:38+02:00 — 260731-EFA-L9 curator: created for the row-vocabulary move from
  `serving/terminal_catalog.py`; preserved the entry/liveness/parsing knowledge from the old
  serving card and left store behavior to the serving card. Verification metadata pinned until
  closeout stamps the L9 code commit.
