# mcp/src/agents_remember/worktrees/task_leaf_binding.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/worktrees/task_leaf_binding.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-08-24T14:48+02:00 |
| lastVerifiedCommitHash |  `ae8c47ce897b04380ebcb80f750d77ed4dc9f37d`|
| lastVerifiedCommitDate |  2026-08-26T08:10:26+02:00|
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

| Finding | Anchor | Source |
| --- | --- | --- |
| Binding models and resolution establish the canonical leaf identity. | `LeafTaskBinding`; `resolve_leaf_task_binding` | mcp/src/agents_remember/worktrees/task_leaf_binding.py:24-40; mcp/src/agents_remember/worktrees/task_leaf_binding.py:43-71 |
| Parent row and child-source readers enforce exact regular-file authority. | `_load_leaf_parent`; `_read_leaf_source` | mcp/src/agents_remember/worktrees/task_leaf_binding.py:74-84; mcp/src/agents_remember/worktrees/task_leaf_binding.py:112-141 |
| Start admission rechecks the binding before reserving lifecycle authority. | `require_current_start_task_binding` | mcp/src/agents_remember/worktrees/task_leaf_binding.py:158-191 |

## Cross-Repo References

No meaningful cross-repository boundary is owned by this file.

## Update History

- 2026-08-24T14:48+02:00 — DAGQC cumulative CLIVE final-gap curation: created the strict source-mirroring card from current code. Verification hash/date remain blank for architect-owned final stamping.