# mcp/src/agents_remember/certification/repository_profiles/validation_primitives.py

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

## Evidence

### Docs References

No configured Domain Documentation source applies to this repository-owned contract.

No configured domain documentation applies.

### Repo-Internal References

- `_finding` implements the described validation step. [1]
- `_duplicates` implements the described validation step. [2]
- `_validate_gate_set` implements the described validation step. [3]

### Cross-Repo References

No cross-repository implementation boundary is owned here.

No cross-repository reference is required.
