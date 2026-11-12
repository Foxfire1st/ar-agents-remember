# mcp/src/agents_remember/certification/repository_profiles/environment_validation.py

## Governing Overview

[Certification contract overview](../overview.md)

## Purpose

Validates declared original producers and later consumers of reconstructed repository environments.

## Code Commentary

### Logic

`_validate_environments` reports duplicate environment IDs, invalid Gate-1 census producers and mismatched manifest publications. The producer must declare the environment artifact; its publication must belong exactly to Gate 1 with the declared byte bound. The reconstruction proof must be published by exactly the consuming gates and use a 4096-byte bound. Consumers must be nonempty, omit Gate 1, and form an ordered unique gate set.

`_validate_environment_artifacts` owns the census-publication and reconstruction-proof checks. `_validate_environments` invokes it before validating the consumer gate set; extracting the helper preserves separate finding codes and accumulation order.

`_validate_selected_producer` examines each selection: when a later environment consumer is applicable, its original Gate-1 producer must also be applicable and explicitly selected. Findings accumulate in the caller’s list.

### Conventions

Use these functions through the aggregate repository-profile validator and preserve the caller’s complete finding list.

### Invariants And Boundaries

- Profile validity establishes declaration coherence; actual reconstruction and proof-byte checking belong to the execution owner.
- Later consumers cannot be admitted without their original selected producer.
- Producer, proof and consumer failures retain separate finding codes.

### Todos

None recorded.

## Evidence

### Docs References

No configured Domain Documentation source applies to this repository-owned contract.

No configured domain documentation applies.

### Repo-Internal References

- `_validate_environments` implements the described validation step. [1]
- `_validate_selected_producer` implements the described validation step. [2]

### Cross-Repo References

No cross-repository implementation boundary is owned here.

No cross-repository reference is required.
