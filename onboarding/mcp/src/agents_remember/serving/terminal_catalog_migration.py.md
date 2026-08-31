# mcp/src/agents_remember/serving/terminal_catalog_migration.py

| Field | Value |
|---|---|
| repository | agents-remember |
| path | `mcp/src/agents_remember/serving/terminal_catalog_migration.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-08-31T04:59+02:00 |
| lastVerifiedCommitHash |  `f2b7c648f540efb9d64ceea22e11e651cb5cc914`|
| lastVerifiedCommitDate |  2026-08-31T15:32:32+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[Serving overview](overview.md)

## Purpose

Migrates legacy terminal catalog rows once into the document+role seat schema before strict catalog
validation. It is deployment migration code, not runtime compatibility precedence.

## Code Commentary

### Logic

`migrate_terminal_catalog_v1` upgrades each row idempotently. Legacy qualified leaf bindings map to
real leaf task documents; sprint/master roles resolve their natural-altitude document from topology
and named scope. A legacy reviewer must retain its original `leafKey`; a named master/sprint scope
cannot prove a review manifestation that did not exist in the legacy leaf-only model and therefore
fails instead of inventing a higher reviewer address. Unresolvable rows fail with
`TerminalCatalogMigrationError`.

### Conventions

Legacy field names appear only inside this migration module and migration tests.

### Invariants And Boundaries

- Current writers emit only taskDocumentRef+role.
- Migration runs before strict current catalog parsing.
- No current reader accepts both schemas.
- Natural role altitude controls the migrated task document.
- Legacy reviewer migration is leaf-only and requires the original leaf identity.

### Todos

Remove the migration only through a separately ruled durability-epoch change after deployed data is proven current.

## Docs References


## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| Catalog migration is one-way and row-local. | `migrate_terminal_catalog_v1` | mcp/src/agents_remember/serving/terminal_catalog_migration.py:19-71 |
| Role altitude selects the canonical migrated document. | `task_ref_for_role` | mcp/src/agents_remember/serving/terminal_catalog_migration.py:72-149 |

## Cross-Repo References


## Update History

- 2026-08-31T04:59+02:00 — 260821-ARSPAWN-L5 independent-review repair: made the one-way reviewer
  migration explicitly leaf-only and fail-closed for legacy named master/sprint scopes.
  Verification remains closeout-owned.

- 2026-08-11T06:47+02:00 — 260731-EFA-L19: created for the explicit catalog durability migration.
