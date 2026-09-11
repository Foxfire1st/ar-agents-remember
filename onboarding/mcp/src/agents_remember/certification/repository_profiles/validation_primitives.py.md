# mcp/src/agents_remember/certification/repository_profiles/validation_primitives.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/certification/repository_profiles/validation_primitives.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-06T15:09:25+00:00 |
| lastVerifiedCommitHash | c69d5171187fa1957025e393270db9f5a864ab14 |
| lastVerifiedCommitDate | 2026-09-06T16:32:29+02:00 |
| governingOverview | `../overview.md` |

## Governing Overview

[Certification contract overview](../overview.md)

## Purpose

Shares typed finding construction, duplicate reporting and gate-order checks across repository profile validators.

## Code Commentary

### Logic

`_finding` constructs the existing `RegistryValidationFinding`. `_duplicates` counts values and emits one finding containing the sorted duplicate names. `_validate_gate_set` compares a gate tuple with its sorted unique form and appends a canonicality finding on mismatch. These helpers leave collection and aggregation policy with their callers.

### Conventions

Use these functions through the aggregate repository-profile validator and preserve the caller’s complete finding list.

### Invariants And Boundaries

- `_validate_gate_set` checks ordering and uniqueness; it does not itself reject an empty tuple despite the broader wording of its diagnostic. Callers or schema fields own required nonempty populations.
- Helpers append findings without executing commands or certifying a profile.
- Duplicate reporting retains all repeated names in deterministic order.

### Todos

None recorded.

## Docs References

No configured Domain Documentation source applies to this repository-owned contract.

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured domain documentation applies. | N/A | N/A |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| `_finding` implements the described validation step. | `_finding` | mcp/src/agents_remember/certification/repository_profiles/validation_primitives.py:10-11 |
| `_duplicates` implements the described validation step. | `_duplicates` | mcp/src/agents_remember/certification/repository_profiles/validation_primitives.py:14-17 |
| `_validate_gate_set` implements the described validation step. | `_validate_gate_set` | mcp/src/agents_remember/certification/repository_profiles/validation_primitives.py:20-28 |

## Cross-Repo References

No cross-repository implementation boundary is owned here.

| Finding | Anchor | Source |
| --- | --- | --- |
| No cross-repository reference is required. | N/A | N/A |

## Update History

- 2026-09-06T15:09:25+00:00 — Created from actual source at c69d5171187fa1957025e393270db9f5a864ab14; documented the declaration checks and their exact runtime limits.
