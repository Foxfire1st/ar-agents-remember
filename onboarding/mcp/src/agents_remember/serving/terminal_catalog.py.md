# mcp/src/agents_remember/serving/terminal_catalog.py

| Field                  | Value                                                       |
| ---------------------- | ----------------------------------------------------------- |
| repository             | agents-remember                                             |
| path                   | `mcp/src/agents_remember/serving/terminal_catalog.py`        |
| doc_type               | `file-level-onboarding`                                     |
| lastUpdated | 2026-08-11T14:29+02:00 |
| lastVerifiedCommitHash | `5aff1e8f01dfa949efc8f68e46bc62a99ed31432`                  |
| lastVerifiedCommitDate | 2026-08-14T14:36:50+02:00|
| governingOverview      | `overview.md`                                               |

## Governing Overview

[serving overview](overview.md)

## Purpose

Owns the durable hosted-occupant catalog and structural seat queries. It runs the one-way legacy
catalog migration before strict current parsing.

## Code Commentary

### Logic

`TerminalCatalog` reads/writes current task-document-and-role rows, looks up the singular running
occupant of a structural seat, and retains replacement/provenance/evidence fields. Reads migrate
legacy rows first and then validate the current model; writers do not emit both schemas.

### Conventions

Catalog methods expose runtime ids only as occupant correlations. Topology qualification lives in the
task/structural resolver rather than this persistence class.

### Invariants And Boundaries

- One running occupant may claim a singular task-document-and-role seat.
- Migration is one-way and precedes strict parsing.
- Spawn ancestry remains audit provenance.
- Current writers never restore leaf-key fields.

### Todos

Removal of migration code requires a separately governed durability-epoch decision.

## Docs References

No Domain Documentation source is configured.

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The catalog queries current occupancy by task document and role. | `TerminalCatalog` | mcp/src/agents_remember/serving/terminal_catalog.py:51-104 |
| Legacy rows migrate before strict model parsing. | "rows = migrate_terminal_catalog_v1(self.path.parent.parent.parent, rows)" | mcp/src/agents_remember/serving/terminal_catalog.py:387-390 |
| The current catalog model owns strict row serialization. | `TerminalCatalogEntry` | mcp/src/agents_remember/models/terminal_catalog.py:67-180 |

## Cross-Repo References

No cross-repository implementation dependency governs this file.

## Update History

- 2026-08-11T14:29+02:00 — Re-read the current `TerminalCatalogEntry` model used by this store
  and widened its citation to include the dataclass declaration; verification metadata remains
  unchanged for governed closeout.

- 2026-08-08T14:38+02:00 — 260731-EFA-L9 curator: rewrote after the row vocabulary moved to
  `models/terminal_catalog.py`; preserved the batch/compact/atomic-write store knowledge from the
  pre-split card. Verification metadata pinned until closeout stamps the L9 code commit.
