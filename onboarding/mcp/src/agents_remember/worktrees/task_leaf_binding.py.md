# mcp/src/agents_remember/worktrees/task_leaf_binding.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/worktrees/task_leaf_binding.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-08-24T14:48+02:00 |
| lastVerifiedCommitHash |  `f95487ec993b58d34911bba0206a7fa6ef9684eb`|
| lastVerifiedCommitDate |  2026-08-24T15:28:18+02:00|
| governingOverview | `../../../overview.md` |

## Governing Overview

[governing route overview](../../../overview.md)

## Purpose

Resolve the canonical master-row to leaf-task binding used by lifecycle admission.

## Code Commentary

### Logic

The resolver loads the exact parent task, identifies one child row, validates regular JSON/Markdown child sources, derives the canonical task reference and enclosure path, and supplies a source-CAS check for start.

### Invariants And Boundaries

- Parent row and child sources must name one exact leaf identity.
- Missing, symlinked, non-regular, or contradictory sources fail closed.
- Start revalidates the current task binding under the shared task-publication lock.
- No path naming inference replaces the canonical row/source binding.

### Todos

None recorded.

## Docs References

No configured domain-documentation source applies to this repository-internal route.

## Repo-Internal References

| Finding | Source Range | Source Path |
| --- | --- | --- |
| Binding models and resolution establish the canonical leaf identity. | L14-L73 | [source](mcp/src/agents_remember/worktrees/task_leaf_binding.py) |
| Parent row and child-source readers enforce exact regular-file authority. | L74-L157 | [source](mcp/src/agents_remember/worktrees/task_leaf_binding.py) |
| Start admission rechecks the binding before reserving lifecycle authority. | L158-L202 | [source](mcp/src/agents_remember/worktrees/task_leaf_binding.py) |

## Cross-Repo References

No meaningful cross-repository boundary is owned by this file.

## Update History

- 2026-08-24T14:48+02:00 — DAGQC cumulative CLIVE final-gap curation: created the strict source-mirroring card from current code. Verification hash/date remain blank for architect-owned final stamping.
