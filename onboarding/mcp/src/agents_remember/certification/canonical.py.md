# mcp/src/agents_remember/certification/canonical.py

## Governing Overview

[Certification overview](overview.md)

## Purpose

Owns deterministic canonicalization of repository-supplied rail and profile declarations after a
bounded raw-input admission check.

## Code Commentary

### Logic

`canonicalize_registry` first admits the raw registry against the shared work budget. It then
normalizes unordered contract members, collapses only byte-identical declarations, retains
conflicting variants for exhaustive validation, sorts the resulting catalog, and binds it to a
canonical content digest.

### Conventions

Identity and content digest jointly determine deduplication. Sort order is semantic and stable;
input declaration order is never plan authority.

### Invariants And Boundaries

- Admission happens before normalization or digest allocation.
- Exact duplicates may collapse; same-identity conflicts must remain visible to validation.
- Required artifacts, applicability, evidence, outputs, prerequisites, profiles, and rails have
  deterministic order.
- Over-budget input fails closed; it is never truncated or routed to a cheaper fallback.
- Canonicalization supplies bytes for validation and planning but does not decide correctness.

### Todos

None within canonicalization ownership.

## Evidence

### Docs References

No Domain Documentation source is configured for this memory root.

No configured domain documentation could be checked.

### Repo-Internal References

- Raw registry admission refuses excess work before normalization or digest allocation. [1]
- Rail variants deduplicate only by exact normalized digest within one identity. [2]
- Nested contract collections are normalized before stable rail ordering. [3]

### Cross-Repo References

No repository implementation is hardcoded here; all declarations arrive through the registry.

- Canonicalization consumes the generic `RailRegistry` contract. [4]
