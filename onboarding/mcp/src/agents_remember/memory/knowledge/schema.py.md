# mcp/src/agents_remember/memory/knowledge/schema.py

## Governing Overview

[memory route overview](../overview.md)

## Purpose

**The derived index's one schema: exactly the eight logical tables the projection fills (MIK-R74 rule 1).** `schema_v2.py` through `schema_v9.py`, the generation registry and every other table, index and trigger definition are deleted. Readers of deleted tables were deleted or reduced with the change.

## Code Commentary

`CANONICAL_TABLES` declares the eight tables in manifest order — `repository`, `invariant`, `invariant_revision`, `family`, `family_revision`, `family_member`, `source_anchor`, `realization_claim` — with `CANONICAL_COLUMNS` fixing the column order per table so a reordered column is a manifest mismatch, never a silent re-map. `_compose` builds the single `CURRENT_GENERATION`; `require_pinned_schema_unchanged` fails loudly when the composed fingerprint drifts from the pinned `SCHEMA_FINGERPRINT` — a changed table definition is a finding, never a re-pin. `generation_of_database` refuses any other declared version instead of migrating it; an earlier generation is the legacy format, read only after conversion to text.

## Evidence

- The index owns exactly eight logical tables in manifest order \[9] [9]
- The one schema is composed, pinned, and drift fails instead of re-pinning \[10] [10]
- Any other declared version is refused, never migrated \[11] [11]
