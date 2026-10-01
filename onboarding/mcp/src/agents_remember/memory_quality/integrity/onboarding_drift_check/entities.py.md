# mcp/src/agents_remember/memory_quality/integrity/onboarding_drift_check/entities.py

## Governing Overview

[overview.md](../../../../../overview.md)

## Purpose

`entities.py` classifies repo entity-catalog (`entities.md`) drift. It parses the
fingerprint and inventory tables, recomputes deterministic evidence fingerprints,
and reconciles inventory entries against fingerprint rows.

## Code Commentary

### Logic

`parse_entity_fingerprint_rows` and `parse_entity_inventory_names` read the
catalog tables; `classify_entity_fingerprint` recomputes the `git-blob-set-v1`
fingerprint and compares it to the recorded value (also surfacing local-change
notes and missing evidence paths); `missing_entity_fingerprint_row` and
`orphaned_entity_fingerprint_row` build reconciliation rows; `classify_entity_catalog`
ties inventory and fingerprint rows together.

**`EntityCatalog` (frozen, 260731-EFA-L2)** is the document all three row builders are signed on:
`onboarding_file`, `onboarding_root`, `repository`, `settings` and `last_updated`. All five are
read out of one catalog document before any row is emitted and every builder needs all five, so
the catalog travels as the document it is. `classify_entity_catalog` constructs it once, right
after `parse_table_metadata`, and passes it down — which is why the `repository` /
`storage_mode` / `last_verified_date` stamped on every emitted row necessarily come from the same
document. Current signatures: `classify_entity_fingerprint(catalog, repo_root, row)`,
`missing_entity_fingerprint_row(catalog, entity, note)`,
`orphaned_entity_fingerprint_row(catalog, row)`.

### Invariants And Boundaries

- Reports drift only; it must not rewrite the entity catalog.
- Fingerprints are deterministic Git blob-set hashes over curated evidence paths.
- Inventory entries without fingerprint rows, and fingerprint rows without
  inventory entries, are actionable maintenance.

## Evidence

### Repo-Internal References

- Fingerprints and change notes are computed via `git_ops`. [1]
- `sidecar.py` delegates `repo-entity-catalog` sidecars to the sidecar classifier. [2]
- `entities.py` implements `classify_entity_catalog`. [3]
