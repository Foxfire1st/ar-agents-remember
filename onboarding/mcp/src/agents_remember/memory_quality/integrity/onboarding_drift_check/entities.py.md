# mcp/src/agents_remember/memory_quality/integrity/onboarding_drift_check/entities.py

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember                         |
| path                   | `mcp/src/agents_remember/memory_quality/integrity/onboarding_drift_check/entities.py` |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-05-29T18:35+02:00|
| lastVerifiedCommitHash | `01f503dcba3a6eacc1587941f6a89fce0bcc72a2` |
| lastVerifiedCommitDate | 2026-05-29T18:32:57+02:00|
| governingOverview      | `../../../../../overview.md`               |

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

### Invariants And Boundaries

- Reports drift only; it must not rewrite the entity catalog.
- Fingerprints are deterministic Git blob-set hashes over curated evidence paths.
- Inventory entries without fingerprint rows, and fingerprint rows without
  inventory entries, are actionable maintenance.

## Repo-Internal References

| Finding | Source Path |
| --- | --- |
| Fingerprints and change notes are computed via `git_ops`. | [git_ops.py](agents-remember/mcp/src/agents_remember/memory_quality/integrity/onboarding_drift_check/git_ops.py) |
| `sidecar.py` delegates `repo-entity-catalog` sidecars to `classify_entity_catalog`. | [sidecar.py](agents-remember/mcp/src/agents_remember/memory_quality/integrity/onboarding_drift_check/sidecar.py) |

## Update History

- 2026-05-29T18:35+02:00: Extracted `_entity_fingerprint_from_row`, `_is_table_separator_row`, `_normalized_header_cells`, and an `_early_classification` closure in `classify_entity_fingerprint` to reduce complexity; behavior-preserving (commit `e3dab63`).
- 2026-05-29T12:10+02:00: Created when `drift.py` was split into focused modules; metadata pending closeout refresh to the split commit.
