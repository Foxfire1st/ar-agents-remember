# mcp/src/agents_remember/serving/terminal_catalog_migration.py

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

## Evidence

### Docs References


### Repo-Internal References

- Catalog migration is one-way and row-local. [1]
- Role altitude selects the canonical migrated document. [2]

### Cross-Repo References
