# mcp/src/agents_remember/memory_quality/incremental_scope/execution_registry.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/memory_quality/incremental_scope/execution_registry.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-06T00:23:26+00:00 |
| lastVerifiedCommitHash | `993953760ef65c4670a40c63a6d6ef0fbcddbe3b`|
| lastVerifiedCommitDate | 2026-09-03T02:13:10+02:00|
| governingOverview | `../overview.md` |

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

## Docs References

No Domain Documentation source is configured for this memory root. The governing task artifact
below closes the informational gap for execution identity.

CCR-R07@v3 (requirements/CCR-R07-v3-incremental-affected-closure-validation.md,
"Invalidation Boundaries") requires changed runtime identity to invalidate the dependent
closure; the execution-registry digest makes that true.


## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The single execution policy binds the range-resolution checker to its validator/runtime/owner. | `_EXECUTION_POLICIES` | mcp/src/agents_remember/memory_quality/incremental_scope/execution_registry.py:11-18 |
| The registry refuses incomplete or stale populations relative to the checker scope registry. | `checker_execution_registry` | mcp/src/agents_remember/memory_quality/incremental_scope/execution_registry.py:21-34 |
| The planner binds the registry version into every affected plan. | `checker_execution_registry_version` | mcp/src/agents_remember/memory_quality/incremental_scope/affected_planning.py:97; mcp/src/agents_remember/memory_quality/incremental_scope/affected_planning.py:115 |
| The execution registry owns the declared checker population, independently of deleted test fixtures. | `checker_execution_registry` | mcp/src/agents_remember/memory_quality/incremental_scope/execution_registry.py:21-34 |

## Cross-Repo References

No cross-repository implementation boundary is owned here.

| Finding | Anchor | Source |
| --- | --- | --- |
| The checker name and scope registry come from the same-repository R06 owners. | `range_resolution`; `checker_scope_registry` | mcp/src/agents_remember/memory_quality/style/citations/range_resolution.py:44-64; mcp/src/agents_remember/memory_quality/incremental_scope/registry.py:108-131 |

## Update History

- 2026-09-06T00:23:26+00:00 — L30 recovery: Corrected incoming references and schema ownership against the reviewed candidate; unchanged source retains its genuine verification stamp.

- 2026-09-03T17:35+02:00 - 260831-CCR-L27 Gate-5 memory pass (src-a): rewrote the task-artifact Docs References row as prose.

- 2026-09-03T12:30+02:00 — 260831-CCR memory curation pass for 993953760ef65c4670a40c63a6d6ef0fbcddbe3b (CCR-R07@v3/L07): created the card for the new R07 execution registry; no prior sidecar existed.
