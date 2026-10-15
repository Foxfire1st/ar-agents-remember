# mcp/src/agents_remember/tasks/master_sync.py

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
When a leaf has a `master` reference, `_master_json_path` calls the shared
`master_json_path_from_ref`: task, task.md and task.json resolve to the same
same-folder document. Missing, escaping or nested named masters raise
`MasterSyncError` with the leaf, reference and remedy; they do not become
`status="none"`. Without a master reference, `folder_master_json_path` supplies
the existing folder task.json or None. An unreadable or non-master parent
also raises `MasterSyncError`.

**`folder_master_json_path` is the one rule for a leaf that names no master
(MIK-R38).** It returns `None` for a leaf that names its master or is not a
`subTask` (a `light` or master document *is* the folder's `task.json`, so it
would otherwise resolve to itself), and otherwise the folder's `task.json` when
it exists, unresolved, exactly the path the sync used before, so `masterDocPath`
in task-document responses is unchanged. The finalizer
(`worktrees/modules/finalize.py`, which completes the row when the leaf lands)
and reopen (`worktrees/reopen.py`, which resets it) call the same helper. Before
MIK-R38 the finalizer called such a leaf standalone, so the row this sync kept
current stayed `inProgress` after the leaf finished (260928-MIK: 15 rows,
repaired by resync writes). The sync's own behaviour is unchanged: it already
gated on `subTask` before reaching this point.

When a parent master is available, the planner finds the existing row by
`SubTaskRef.number == leaf.id`, maps `number`, `name`, `file`, and derived
`status`, and preserves an existing manual `scope`. It returns
`created`, `updated`, or `unchanged` with the planned master document.

### Conventions

The module is pure planning plus reads. It does not write the master file and does
not render markdown; the application/store boundary owns that.

### Invariants And Boundaries

- Auto-sync accepts only a same-root master candidate whose parent is exactly
  the task root. Missing, escaping or nested named masters refuse; task/task.md/task.json resolve uniformly across all three writers.
- Manual master-row `scope` is preserved; the sync only owns deterministic row
  fields that can be derived from the leaf.
- With statuses present, leaf document status already `Completed`, and no
  `completion_blockers`, the derived row is `Completed`. Any done, in-progress, or blocked status otherwise derives
  `inProgress`; an inconsistent completed leaf also derives
  `inProgress`, and the remaining case keeps the leaf status.
- **One resolution rule for every writer of a leaf's master row (MIK-R38).** All three writers share folder_master_json_path for unnamed leaves and master_json_path_from_ref for named masters.
- **An abandoned leaf projects `abandoned` unchanged:** `derived_master_status`
  returns `abandoned` before the rollup, so a deliberately dropped leaf does not
  collapse back to `inProgress` and a later master sync cannot silently reopen a
  row that was abandoned on purpose.

### Todos

No known local todos.

## Evidence

### Docs References

No relevant external documentation found after checking the task-document route
scope; this file implements an internal coordination contract.

No relevant external documentation found; behavior is defined by repo task-document contracts and tests.

### Repo-Internal References

- Same-root parent planning uses the shared named-master refusal rule; unnamed leaves retain folder fallback. [1]
- The one rule for a leaf naming no master: `None` for a named master or a non-`subTask`, else the folder's `task.json` when it exists. [2]

- The finalizer and reopen resolve an unnamed leaf through the same helper. [3]
- Deterministic leaf-to-row mapping with manual scope preservation. [4]
- Strict master-row status derivation and unresolved-master demotion. [5]
- Existing-row path validation. [6]
- Parent document loading uses the exact accepted JSON snapshot. [7]

### Cross-Repo References

No meaningful cross-repo references found; this planner only writes within the
resolved agents-remember coordination task root.

No cross-repo dependency; external-memory alignment is handled by the worktree lifecycle outside this file.

## 260821-CLIVE-L2 Current Contract

The current source seams include `MasterSyncError`, `MasterSyncPlan`, `plan_master_sync`. L2 adds the accepted master source snapshot to the synchronization plan so publication can compare exact before-state. Queue invalidation/rebuild after affected task changes remains L3 scope.

### Reconciled Source Evidence

- The current module exposes `MasterSyncError`, `MasterSyncPlan`, `plan_master_sync` at this ownership boundary. [8]
