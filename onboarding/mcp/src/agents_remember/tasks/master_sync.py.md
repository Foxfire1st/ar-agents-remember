# mcp/src/agents_remember/tasks/master_sync.py

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember                            |
| path                   | `mcp/src/agents_remember/tasks/master_sync.py` |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated | 2026-08-23T16:08+02:00 |
| lastVerifiedCommitHash | `ae8c47ce897b04380ebcb80f750d77ed4dc9f37d` |
| lastVerifiedCommitDate | 2026-08-26T08:10:26+02:00|
| governingOverview      | `overview.md`                              |

## Governing Overview

[tasks/overview.md](overview.md)

## Purpose

Plans the automatic same-series synchronization from a leaf JSON task document to
its parent master `subTasks[]` row. It is the task-document layer's bridge between
leaf progress edits and the master checklist, without making the renderer or store
know task-series policy.

## Code Commentary

### Logic

`plan_master_sync(task_root, leaf)` only acts on `kind == "subTask"` documents.
When a leaf has a `master` reference, `_json_path_from_master_ref` accepts
only a candidate inside the task root whose parent is that root. Without a
master reference, the planner checks the root's default `task.json`. Missing
or cross-series candidates return `status="none"`; a found but unreadable or
non-master parent raises `MasterSyncError`.

When a parent master is available, the planner finds the existing row by
`SubTaskRef.number == leaf.id`, maps `number`, `name`, `file`, and derived
`status`, and preserves an existing manual `scope`. It returns
`created`, `updated`, or `unchanged` with the planned master document.

### Conventions

The module is pure planning plus reads. It does not write the master file and does
not render markdown; the application/store boundary owns that.

### Invariants And Boundaries

- Auto-sync accepts only a same-root master candidate whose parent is exactly
  the task root. A cross-series or nested candidate is ignored.
- Manual master-row `scope` is preserved; the sync only owns deterministic row
  fields that can be derived from the leaf.
- With statuses present and no `completion_blockers`, the derived row is
  `Completed`. Any done, in-progress, or blocked status otherwise derives
  `inProgress`; an inconsistent completed leaf also derives
  `inProgress`, and the remaining case keeps the leaf status.

### Todos

No known local todos.

## Docs References

No relevant external documentation found after checking the task-document route
scope; this file implements an internal coordination contract.

| Finding | Anchor | Source |
| --- | --- | --- |
| No relevant external documentation found; behavior is defined by repo task-document contracts and tests. | n/a | n/a |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| Same-root parent resolution and master-plan construction. | `plan_master_sync`; `_master_json_path`; `_json_path_from_master_ref` | mcp/src/agents_remember/tasks/master_sync.py:35-89; mcp/src/agents_remember/tasks/master_sync.py:144-148; mcp/src/agents_remember/tasks/master_sync.py:151-161 |
| Deterministic leaf-to-row mapping with manual scope preservation. | `subtask_ref_from_leaf` | mcp/src/agents_remember/tasks/master_sync.py:92-102 |
| Strict master-row status derivation and unresolved-master demotion. | `derived_master_status`; `demote_completed_master_if_unresolved` | mcp/src/agents_remember/tasks/master_sync.py:105-116; mcp/src/agents_remember/tasks/master_sync.py:119-125 |
| Existing-row path validation. | `_validate_existing_row_path` | mcp/src/agents_remember/tasks/master_sync.py:128-141 |
| Parent document loading uses the exact accepted JSON snapshot. | "master = TaskDocument.model_validate_json(source_snapshot.json_bytes)" | mcp/src/agents_remember/tasks/master_sync.py:46-46 |

## Cross-Repo References

No meaningful cross-repo references found; this planner only writes within the
resolved agents-remember coordination task root.

| Finding | Anchor | Source |
| --- | --- | --- |
| No cross-repo dependency; external-memory alignment is handled by the worktree lifecycle outside this file. | n/a | n/a |

## 260821-CLIVE-L2 Current Contract

The current source seams include `MasterSyncError`, `MasterSyncPlan`, `plan_master_sync`. L2 adds the accepted master source snapshot to the synchronization plan so publication can compare exact before-state. Queue invalidation/rebuild after affected task changes remains L3 scope.

### Reconciled Source Evidence

| Finding | Anchor | Source |
| --- | --- | --- |
| The current module exposes `MasterSyncError`, `MasterSyncPlan`, `plan_master_sync` at this ownership boundary. | `MasterSyncError`; `MasterSyncPlan`; `plan_master_sync` | mcp/src/agents_remember/tasks/master_sync.py:18-19; mcp/src/agents_remember/tasks/master_sync.py:22-32; mcp/src/agents_remember/tasks/master_sync.py:35-89 |

## Update History

- 2026-08-23T16:08+02:00 — 260821-CLIVE-L2: reconciled this card with the accepted full L2 candidate; verification metadata remains pinned until architect-owned closeout stamps the real code commit.
- 2026-08-04T08:03:35+02:00 — 260731-EFA-L6 S18-B07 curator: repaired the bounded citation findings from the recovered Avicenna and Kuhn ledgers, splitting or narrowing claims to the frozen source and normalizing scoped citation ranges.

- 2026-08-02T01:05+02:00 — No content impact: `mcp/src/agents_remember/tasks/reopen.py` moved to `mcp/src/agents_remember/worktrees/reopen.py` (reopen rewrites the leaf's enclosure contract, and ranking it as a task operation made `tasks` and `worktrees` mutually dependent per `layers.toml`). Re-pointed the reference here; the behavior this document describes is unchanged. Verification metadata pinned until closeout stamps the L6 code commit.
- 2026-08-02T00:17+02:00 — No content impact: 260731-EFA-L6 renamed `mcp/src/agents_remember/controllers/` to `application/` and moved `worktrees/status.py` to `application/worktree_status.py`. Updated the references and the vocabulary here ("the application layer" for the package, "an application entry point" for one function); the behavior this document describes is unchanged. Verification metadata pinned until closeout stamps the L6 code commit.
- 2026-07-31T17:20+02:00 — 260731-EFA-L2 curator: repaired 1 cross-file line citation. The master-sync controller tests now sit at L635-L758 of `test_task_document.py` (1375 lines): `test_leaf_create_syncs_parent_master_row` L635, `test_leaf_updates_preserve_manual_master_scope` L650, `test_leaf_step_progress_derives_master_row_status` L669, unreadable-parent and wrong-kind refusals L684/L711, and `test_leaf_dry_run_includes_master_sync_preview_without_writing` L745-L758. Extended the claim to name the two refusal tests the range now covers.

- 2026-07-31T16:35+02:00 — No content impact: the only change to
  `mcp/src/agents_remember/tasks/master_sync.py` since the L2 base commit is the whole-tree `ruff
  format` pass in `00e8379`, which re-wrapped 3 line(s) with no token change whatsoever. Checked
  by parsing both revisions and comparing the abstract syntax trees (identical) and the comment
  tokens (identical), so no symbol, signature, default, decorator, control-flow branch, docstring,
  or assertion this card describes has moved, and every claim this card makes about its own source
  still holds. Noted while checking: the references table also cites line ranges inside
  `task_doc_tools.py`, `test_task_document.py`; those ranges shifted because this task edited
  those files, so treat the cited numbers as approximate and the linked cards as authoritative.

- 2026-06-26T20:18+02:00 — Created for Task 21: documents same-root leaf-to-master row sync planning, status derivation, manual scope preservation, and the preview/write boundary. Verification metadata left blank until closeout stamps the first code commit for this new file.