# mcp/src/agents_remember/memory/knowledge/schema.py

## Governing Overview

[memory route overview](../overview.md)

## Purpose

**The derived index's one schema: exactly the eight logical tables the projection fills (MIK-R74 rule 1).** Revision tables store the selected tree's derived state. The schema admits generation 10.

## Code Commentary

`CANONICAL_TABLES` declares the eight tables in manifest order — `repository`, `invariant`, `invariant_revision`, `family`, `family_revision`, `family_member`, `source_anchor`, `realization_claim` — with `CANONICAL_COLUMNS` fixing the column order per table so a reordered column is a manifest mismatch, never a silent re-map. `_compose` builds the single `CURRENT_GENERATION`; `require_pinned_schema_unchanged` fails loudly when the composed fingerprint drifts from the pinned `SCHEMA_FINGERPRINT` — a changed table definition is a finding, never a re-pin. `generation_of_database` refuses any other declared version instead of migrating it; an earlier generation is the legacy format, read only after conversion to text.

## Evidence




- The one admitted schema checks its pinned definition and declared generation. [12]

- The index declares eight logical tables and their manifest column order. [9]
- The composed schema is checked against the pinned fingerprint. [10]
- A database with another declared generation is refused. [11]
