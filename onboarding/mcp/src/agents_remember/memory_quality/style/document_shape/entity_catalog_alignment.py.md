# mcp/src/agents_remember/memory_quality/style/document_shape/entity_catalog_alignment.py

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

## Evidence

### Docs References

No external Domain Documentation source is configured for this memory repo.

### Repo-Internal References

- The top-level checker enforces section presence and one-to-one entity alignment. [1]
- Inventory and fingerprint parsing is shared with drift classification. [2]
- The registry places this check first in closeout's pre-metadata phase. [3]
