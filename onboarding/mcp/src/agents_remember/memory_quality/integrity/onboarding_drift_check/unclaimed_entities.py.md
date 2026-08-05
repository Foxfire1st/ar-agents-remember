# mcp/src/agents_remember/memory_quality/integrity/onboarding_drift_check/unclaimed_entities.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/memory_quality/integrity/onboarding_drift_check/unclaimed_entities.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-08-05T00:00+02:00 |
| lastVerifiedCommitHash | `5920ea2b4bdd5d5ee969ae064ff9a8e1fc6b4060` |
| lastVerifiedCommitDate | 2026-08-05T12:41:24+02:00|
| governingOverview | `../../overview.md` |

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

## Repo-Internal References

This module defines the top-level symbols cited below; each row points at the exact source range holding the anchor.

| Finding | Anchor | Source |
| --- | --- | --- |
| Defines the class `UnclaimedEntitySource` (lines 49-65) — One meaningful unclaimed source and the declarations that ranked it.. | `UnclaimedEntitySource` | mcp/src/agents_remember/memory_quality/integrity/onboarding_drift_check/unclaimed_entities.py:49-65 |
| Defines the class `UnclaimedEntityReport` (lines 69-75) — Complete coverage counts plus the ranked meaningful subset.. | `UnclaimedEntityReport` | mcp/src/agents_remember/memory_quality/integrity/onboarding_drift_check/unclaimed_entities.py:69-75 |
| Defines the function `_assigned_names` (lines 78-80). | `_assigned_names` | mcp/src/agents_remember/memory_quality/integrity/onboarding_drift_check/unclaimed_entities.py:78-80 |
| Defines the function `_assigned_value` (lines 83-84). | `_assigned_value` | mcp/src/agents_remember/memory_quality/integrity/onboarding_drift_check/unclaimed_entities.py:83-84 |
| Defines the function `_call_name` (lines 87-94). | `_call_name` | mcp/src/agents_remember/memory_quality/integrity/onboarding_drift_check/unclaimed_entities.py:87-94 |
| Defines the function `declaration_signals` (lines 97-126) — Return the explicit contract/schema/authority facts declared by one Python module.. | `declaration_signals` | mcp/src/agents_remember/memory_quality/integrity/onboarding_drift_check/unclaimed_entities.py:97-126 |
| Defines the function `_rank_key` (lines 129-144). | `_rank_key` | mcp/src/agents_remember/memory_quality/integrity/onboarding_drift_check/unclaimed_entities.py:129-144 |
| Defines the function `rank_unclaimed_entity_sources` (lines 147-175) — Compute the real inventory/evidence set difference and rank its meaningful members.. | `rank_unclaimed_entity_sources` | mcp/src/agents_remember/memory_quality/integrity/onboarding_drift_check/unclaimed_entities.py:147-175 |

## Update History

- 2026-08-05T00:00+02:00 — 260731-EFA-L6 closeout pass: created this file-level onboarding card for the new source file; anchors and ranges derived from the current worktree source. Verification metadata pinned until closeout stamps the code commit.
