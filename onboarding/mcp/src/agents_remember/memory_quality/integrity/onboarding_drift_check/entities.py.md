# mcp/src/agents_remember/memory_quality/integrity/onboarding_drift_check/entities.py

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember-md                         |
| path                   | `mcp/src/agents_remember/memory_quality/integrity/onboarding_drift_check/entities.py` |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-05-29T12:10+02:00                     |
| lastVerifiedCommitHash | `12737deaac2fd75563ca1e3037cdac911023cf93` |
| lastVerifiedCommitDate | 2026-05-29T12:28:42+02:00|
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
| Fingerprints and change notes are computed via `git_ops`. | [git_ops.py](agents-remember-md/mcp/src/agents_remember/memory_quality/integrity/onboarding_drift_check/git_ops.py) |
| `sidecar.py` delegates `repo-entity-catalog` sidecars to `classify_entity_catalog`. | [sidecar.py](agents-remember-md/mcp/src/agents_remember/memory_quality/integrity/onboarding_drift_check/sidecar.py) |

## Update History

- 2026-05-29T12:10+02:00: Created when `drift.py` was split into focused modules; metadata pending closeout refresh to the split commit.
