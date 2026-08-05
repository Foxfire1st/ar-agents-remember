# mcp/src/agents_remember/memory_quality/integrity/onboarding_drift_check/entities.py

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember                         |
| path                   | `mcp/src/agents_remember/memory_quality/integrity/onboarding_drift_check/entities.py` |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-07-31T00:00+02:00|
| lastVerifiedCommitHash | `5920ea2b4bdd5d5ee969ae064ff9a8e1fc6b4060` |
| lastVerifiedCommitDate | 2026-08-05T12:41:24+02:00|
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

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| Fingerprints and change notes are computed via `git_ops`. | `compute_git_blob_set_fingerprint`; `entity_local_change_notes` | mcp/src/agents_remember/memory_quality/integrity/onboarding_drift_check/git_ops.py:65-73; mcp/src/agents_remember/memory_quality/integrity/onboarding_drift_check/git_ops.py:76-82 |
| `sidecar.py` delegates `repo-entity-catalog` sidecars to the sidecar classifier. | `classify_sidecar_onboarding_units` | mcp/src/agents_remember/memory_quality/integrity/onboarding_drift_check/sidecar.py:289-342 |
| `entities.py` implements `classify_entity_catalog`. | `classify_entity_catalog` | mcp/src/agents_remember/memory_quality/integrity/onboarding_drift_check/entities.py:313-386 |

## Update History

- 2026-08-04T11:43:39+02:00 — 260731-EFA-L6 S18-B03 curator: anchored fingerprint/change-note and sidecar
  delegation references to exact implementation symbols; narrowed the entity row to its cited
  classifier implementation.

- 2026-07-31T00:00+02:00 — 260731-EFA-L2 (gate honesty, `PLR0913` armed with no exemptions):
  added the frozen `EntityCatalog` and re-signed all three row builders onto it —
  `classify_entity_fingerprint(catalog, repo_root, row)`,
  `missing_entity_fingerprint_row(catalog, entity, note)` and
  `orphaned_entity_fingerprint_row(catalog, row)` replace the previous five- to seven-argument
  signatures. `classify_entity_catalog` builds the catalog once. No emitted `DriftRow` changed.
  Verification metadata pinned until closeout stamps the L2 commit.
- 2026-05-29T18:35+02:00: Extracted `_entity_fingerprint_from_row`, `_is_table_separator_row`, `_normalized_header_cells`, and an `_early_classification` closure in `classify_entity_fingerprint` to reduce complexity; behavior-preserving (commit `e3dab63`).
- 2026-05-29T12:10+02:00: Created when `drift.py` was split into focused modules; metadata pending closeout refresh to the split commit.
