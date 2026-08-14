# mcp/src/agents_remember/memory_quality/style/document_shape/entity_catalog_alignment.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/memory_quality/style/document_shape/entity_catalog_alignment.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-08-10T12:46+02:00 |
| lastVerifiedCommitHash | `5aff1e8f01dfa949efc8f68e46bc62a99ed31432` |
| lastVerifiedCommitDate | 2026-08-14T14:36:50+02:00|
| governingOverview | `../../overview.md` |

## Governing Overview

[memory quality overview](../../overview.md)

## Purpose

Reject structural disagreement between the repository entity inventory and its fingerprint table
before closeout starts any code-quality subprocess.

## Code Commentary

### Logic

`check_onboarding_root` is a tree-only style check over the root `entities.md`. If no catalog
exists, the check is not applicable. When it exists, both `## Entity Inventory` and
`## Entity Fingerprints` must exist; every inventory name must have exactly one fingerprint row,
and every fingerprint name must have an inventory entry. The checker reuses the drift classifier's
catalog parsers so both phases interpret entity names and table cells identically, but it performs
no Git or hash comparison.

Findings retain catalog line numbers and distinguish missing sections,
`entity_fingerprint_without_inventory`, `entity_inventory_without_fingerprint`, and duplicate
fingerprint rows. This narrow shape check can therefore run before commit metadata exists, unlike
the full onboarding drift check.

### Invariants And Boundaries

- The check owns catalog structure only; source evidence existence and fingerprint freshness stay
  in `integrity/onboarding_drift_check` after metadata refresh.
- Absence of `entities.md` is not a finding because repositories may have no entity catalog.
- A present catalog is one-to-one: one inventory entry and one fingerprint row per entity.
- Findings are enforcing and use the shared `QualityFinding`/`check_result` result shape.

### Todos

None.

## Docs References

No external Domain Documentation source is configured for this memory repo.

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The top-level checker enforces section presence and one-to-one entity alignment. | `check_onboarding_root` | mcp/src/agents_remember/memory_quality/style/document_shape/entity_catalog_alignment.py:70-130 |
| Inventory and fingerprint parsing is shared with drift classification. | `parse_entity_fingerprint_rows`; `parse_entity_inventory_names` | mcp/src/agents_remember/memory_quality/integrity/onboarding_drift_check/entities.py:84-113; mcp/src/agents_remember/memory_quality/integrity/onboarding_drift_check/entities.py:116-132 |
| The registry places this check first in closeout's pre-metadata phase. | `BEFORE_METADATA_REFRESH_CHECKS` | mcp/src/agents_remember/memory_quality/check.py:87-92 |

## Update History

- 2026-08-10T12:46+02:00 — Created for the L9 closeout fail-fast repair; verification metadata
  remains pinned to the prior code tip until closeout stamps the repair commit.
