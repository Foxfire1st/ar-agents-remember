# mcp/src/agents_remember/worktrees/task_leaf_binding.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/worktrees/task_leaf_binding.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-01T03:58+02:00 |
| lastVerifiedCommitHash |  `47c8d102c2430d5337dbe207d4601efb4844fec0`|
| lastVerifiedCommitDate |  2026-09-01T08:53:56+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[Worktrees overview](overview.md)

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
| Binding models and resolution establish the canonical leaf identity through the shared pure task-domain owner. | `LeafTaskBinding`; `resolve_leaf_task_binding` | mcp/src/agents_remember/worktrees/task_leaf_binding.py:30-45; mcp/src/agents_remember/worktrees/task_leaf_binding.py:48-87 |
| Parent and child source readers enforce exact regular-file authority after canonical row/source derivation. | `_load_leaf_parent`; `_read_leaf_source` | mcp/src/agents_remember/worktrees/task_leaf_binding.py:90-100; mcp/src/agents_remember/worktrees/task_leaf_binding.py:103-127 |
| Start admission rechecks the same canonical composite binding before reserving lifecycle authority. | `require_current_start_task_binding` | mcp/src/agents_remember/worktrees/task_leaf_binding.py:144-177 |

## Cross-Repo References

No meaningful cross-repository boundary is owned by this file.

## Update History

- 2026-09-01T03:58+02:00 — 260831-CCR-L01 Attempt 8: re-read the reopened child-source claim,
  documented delegation to the shared canonical leaf-binding owner, regenerated moved ranges, and
  rebound the card to its nearest worktrees overview. Verification remains closeout-owned.

- 2026-08-24T14:48+02:00 — DAGQC cumulative CLIVE final-gap curation: created the strict source-mirroring card from current code. Verification hash/date remain blank for architect-owned final stamping.
