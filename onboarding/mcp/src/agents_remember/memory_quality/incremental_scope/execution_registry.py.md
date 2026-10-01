# mcp/src/agents_remember/memory_quality/incremental_scope/execution_registry.py

## Governing Overview

[memory quality overview](../overview.md)

## Purpose

Owns the exhaustive CCR-R07 execution registry: exactly one `CheckerExecutionPolicy` per R06
incremental checker, so an affected plan's `executionRegistryVersion` names the complete current
execution contract set and no incremental checker can execute with an unregistered contract.

## Code Commentary

### Logic

`_EXECUTION_POLICIES` (`execution_registry.py:11-18`) declares the sole execution policy for
the range-resolution checker (`range_resolution.CHECK_NAME`, validator
`citation-range-resolution/v1`, runtime `python-3.13-memory-quality/v1`, corrective owner
`memory-curator`). `checker_execution_registry` (`execution_registry.py:21-34`) returns the
sorted policies after proving the declared checker set equals exactly the incremental checker set
of `checker_scope_registry`, raising `ValueError` with the missing/stale names otherwise.
`checker_execution_registry_version` (`execution_registry.py:37-38`) is the canonical content
digest of the registry, which the planner binds into every affected plan and the executor
revalidates.

### Conventions

The execution registry mirrors the R06 checker scope registry's incremental subset; a policy may
never exist for a checker the scope registry does not declare incremental, and vice versa.

### Invariants And Boundaries

- The execution registry is exhaustive: incomplete or stale population raises instead of
  returning a partial contract set.
- Runtime/validator identities are part of the content digest, so a runtime change invalidates
  affected subresult reuse.

### Todos

None recorded.

## Evidence

### Docs References

No Domain Documentation source is configured for this memory root. The governing task artifact
below closes the informational gap for execution identity.

CCR-R07@v3 (requirements/CCR-R07-v3-incremental-affected-closure-validation.md,
"Invalidation Boundaries") requires changed runtime identity to invalidate the dependent
closure; the execution-registry digest makes that true.


### Repo-Internal References

- The single execution policy binds the range-resolution checker to its validator/runtime/owner. [1]
- The registry refuses incomplete or stale populations relative to the checker scope registry. [2]
- The planner binds the registry version into every affected plan. [3]
- The execution registry owns the declared checker population, independently of deleted test fixtures. [4]

### Cross-Repo References

No cross-repository implementation boundary is owned here.

- The checker name and scope registry come from the same-repository R06 owners. [5]
