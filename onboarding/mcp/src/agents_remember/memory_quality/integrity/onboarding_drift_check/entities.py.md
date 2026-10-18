# mcp/src/agents_remember/memory_quality/integrity/onboarding_drift_check/entities.py

## Governing Overview

[overview.md](../../../../../overview.md)

## Purpose

`entities.py` parses entity inventory/fingerprint text for retained readers and structural census comparison. It does not recompute Git fingerprints or grade stamped currentness.

## Code Commentary

### Logic

`parse_entity_fingerprint_rows` reads the fingerprint section and normalizes its evidence paths; `parse_entity_inventory_names` reads named inventory subsections and deduplicates that historical reader. `CensusEntityRow` instead retains exact entity key, curated evidence tuple, inventory bytes and fingerprint-row bytes.

`parse_entity_census_rows` preserves ambiguity for refusal rather than silently selecting it: duplicate inventory/fingerprint keys or headers, rows before their header, width mismatches, missing evidencePaths and unequal inventory/fingerprint key sets raise `ValueError`. It supports subsection and Entity-table inventory forms and returns keys sorted by UTF-8 bytes.

### Invariants And Boundaries

- Parsing never rewrites the catalog or assigns currentness.
- Strict census keys are nonempty decoded UTF-8 strings without NUL; exact row text and evidence spelling are preserved.
- Inventory and fingerprint keys must match exactly once.

## Evidence

### Repo-Internal References



- Entity census parsing preserves exact keys/evidence/row text and refuses duplicate or misaligned structure, never grading currentness. [3]
