# mcp/tests/test_memory_incremental_scope_candidate.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/test_memory_incremental_scope_candidate.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-03T12:30:00+02:00 |
| lastVerifiedCommitHash | `1ad9d51f743c5b17de51cc46d8b29e004736022d` |
| lastVerifiedCommitDate | 2026-09-02T06:25:51+02:00 |
| governingOverview | `overview.md` |

## Governing Overview

[mcp tests overview](overview.md)

## Purpose

Focused evidence for the CCR-R06@v2 candidate observation seam: proves that changed roots derive
only from exact Git tree diffs (including rename endpoints) and that a missing canonical task
baseline refuses before any live identity is derived. It backs the packet's "exact Git tree-diff
owner" and root-authority requirements cit:([`test_exact_tree_diff_classifies_add_modify_delete_and_both_rename_ends`, `test_mtime_only_change_is_not_a_changed_root`], mcp/tests/test_memory_incremental_scope_candidate.py:43-89).

## Code Commentary

### Logic

Harnesses build a scratch Git repository (`_repository`) whose base commit contains changed,
deleted, renamed, and untouched files, then stage a candidate tree via `worktree_candidate_tree`.
`test_exact_tree_diff_classifies_add_modify_delete_and_both_rename_ends` asserts the observed
delta classifies added/modified/deleted/renamed changes with both rename endpoints and equal
rename blobs cit:([`test_exact_tree_diff_classifies_add_modify_delete_and_both_rename_ends`], mcp/tests/test_memory_incremental_scope_candidate.py:43-70).
`test_mtime_only_change_is_not_a_changed_root` touches only mtimes via `os.utime` and asserts the
delta is empty — mtimes are not root authority
cit:([`test_mtime_only_change_is_not_a_changed_root`], mcp/tests/test_memory_incremental_scope_candidate.py:72-89).
`test_missing_canonical_task_baseline_refuses_before_current_identity_is_derived` constructs a
minimal external-memory `WorktreeContract` with no closeout door and asserts
`task-base-unavailable` cit:([`test_missing_canonical_task_baseline_refuses_before_current_identity_is_derived`], mcp/tests/test_memory_incremental_scope_candidate.py:91-127).

### Conventions

- Git plumbing is invoked through the repository's `run_git` helper; no host-pytest or Dagger
  bypass exists in the test.
- Candidates are staged through the shared `worktree_candidate_tree` helper, mirroring production.

## Invariants And Boundaries

- An exact tree diff is the only root authority: renames keep both ends, deletes keep the old blob,
  and mtime-only changes produce no roots.
- Every refusal is a typed `ScopeUnprovenError` whose `failure.code` identifies the class.
- The suite never fabricates topology or intent identities; the missing-door case refuses early.

## Docs References

No configured Domain Documentation applies; the assertions follow the CCR-R06@v2 packet.

| Finding | Anchor | Source |
| --- | --- | --- |
| Root authority semantics are repository-owned. | — | — |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| Production functions under test. | `observe_contract_task_pair`, `observe_git_tree_delta` | mcp/src/agents_remember/memory_quality/incremental_scope/candidate.py:102-149, 213-236 |
| Candidate-tree staging matches the production memory-candidate path. | `worktree_candidate_tree` | mcp/src/agents_remember/worktrees/modules/git.py |
| Git plumbing call wrapper. | `run_git` | mcp/src/agents_remember/kernel/git_command.py |
| Companion edge suite for the same candidate observation surface. | — | mcp/tests/test_memory_incremental_scope_candidate_edges.py |

## Update History

- 2026-09-03T12:30+02:00 — 260831-CCR memory curation pass for 1ad9d51f743c5b17de51cc46d8b29e004736022d (CCR-R06@v2/L26): created the card for the new candidate-observation evidence suite of the R06v2 successor leaf; no prior sidecar existed.