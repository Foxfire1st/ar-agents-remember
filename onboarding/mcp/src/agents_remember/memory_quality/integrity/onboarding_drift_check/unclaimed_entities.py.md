# mcp/src/agents_remember/memory_quality/integrity/onboarding_drift_check/unclaimed_entities.py

## Governing Overview

[overview](../../overview.md)

## Purpose

Rank source files that no entity-catalog fingerprint claims.

## Code Commentary

### Logic

Module-level surface:

- `UnclaimedEntitySource` (class, lines 49-65) — One meaningful unclaimed source and the declarations that ranked it.
- `UnclaimedEntityReport` (class, lines 69-75) — Complete coverage counts plus the ranked meaningful subset.
- `_assigned_names` (function, lines 78-80)
- `_assigned_value` (function, lines 83-84)
- `_call_name` (function, lines 87-94)
- `declaration_signals` (function, lines 97-126) — Return the explicit contract/schema/authority facts declared by one Python module.
- `_rank_key` (function, lines 129-144)
- `rank_unclaimed_entity_sources` (function, lines 147-175) — Compute the real inventory/evidence set difference and rank its meaningful members.

### Conventions

Module-level definitions follow the package conventions; names prefixed with `_` are private to this module.

### Invariants And Boundaries

- The card mirrors the source file one-to-one at `mcp/src/...` path.

### Todos

None.

## Evidence

### Repo-Internal References

This module defines the top-level symbols cited below; each row points at the exact source range holding the anchor.

- Defines the class `UnclaimedEntitySource` (lines 49-65) — One meaningful unclaimed source and the declarations that ranked it.. [1]
- Defines the class `UnclaimedEntityReport` (lines 69-75) — Complete coverage counts plus the ranked meaningful subset.. [2]
- Defines the function `_assigned_names` (lines 78-80). [3]
- Defines the function `_assigned_value` (lines 83-84). [4]
- Defines the function `_call_name` (lines 87-94). [5]
- Defines the function `declaration_signals` (lines 97-126) — Return the explicit contract/schema/authority facts declared by one Python module.. [6]
- Defines the function `_rank_key` (lines 129-144). [7]
- Defines the function `rank_unclaimed_entity_sources` (lines 147-175) — Compute the real inventory/evidence set difference and rank its meaningful members.. [8]
