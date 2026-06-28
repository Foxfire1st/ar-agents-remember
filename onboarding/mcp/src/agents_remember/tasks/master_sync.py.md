# mcp/src/agents_remember/tasks/master_sync.py

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember                            |
| path                   | `mcp/src/agents_remember/tasks/master_sync.py` |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-06-26T20:18+02:00                     |
| lastVerifiedCommitHash | `84e95ad0379cd864af3cbae21b7ffe3fd2d2b1b1`                                         |
| lastVerifiedCommitDate |                                            2026-06-28T18:49:06+02:00|
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

`plan_master_sync(task_root, leaf)` only acts on `kind == "subTask"` documents. It
resolves the parent master JSON from the leaf's `master` reference when that points
inside the same task root, otherwise from a sibling `task.json` when present. Missing
masters and cross-series refs return `status="none"` so navigation metadata does not
become an implicit cross-folder write. A resolvable but unreadable or non-master
parent raises `MasterSyncError`.

When a parent master is available, the planner finds the existing row by
`SubTaskRef.number == leaf.id`, maps deterministic leaf fields into a row
(`number`, `name`, `file`, derived `status`), and preserves any existing manual
`scope`. It returns `created`, `updated`, or `unchanged` with the planned master
document; callers decide whether to preview or write it.

### Conventions

The module is pure planning plus reads. It does not write the master file and does
not render markdown; the controller/store boundary owns that.

### Invariants And Boundaries

- Auto-sync is same-root only. A `master` reference outside `task_root` is navigation
  metadata and must not trigger a write to another task series.
- Manual master-row `scope` is preserved; the sync only owns deterministic row
  fields that can be derived from the leaf.
- Leaf step/substep status collapses into the strict master status vocabulary:
  all done becomes `Completed`, any active/done/blocked progress becomes
  `inProgress`, otherwise the leaf's declared status is retained.

### Todos

No known local todos.

## Docs References

No relevant external documentation found after checking the task-document route
scope; this file implements an internal coordination contract.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No relevant external documentation found; behavior is defined by repo task-document contracts and tests. | n/a | n/a |

## Repo-Internal References

| Finding | Citations | Source Path |
| --- | --- | --- |
| The task-doc controller invokes `plan_master_sync`, includes sync data in dry-run previews, and writes the changed leaf plus changed master together. | L125-L135; L444-L472 | [task_doc_tools.py](agents-remember/mcp/src/agents_remember/controllers/task_doc_tools.py) |
| Store batch writes prepare every JSON and markdown payload before writing, then return paths in input order. | L35-L57 | [store.py](agents-remember/mcp/src/agents_remember/tasks/store.py) |
| Controller tests prove row creation, manual scope preservation, status derivation, and dry-run sync preview without writing the master. | L603-L666 | [test_task_document.py](agents-remember/mcp/tests/test_task_document.py) |

## Cross-Repo References

No meaningful cross-repo references found; this planner only writes within the
resolved agents-remember coordination task root.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No cross-repo dependency; external-memory alignment is handled by the worktree lifecycle outside this file. | n/a | n/a |

## Update History

- 2026-06-26T20:18+02:00 — Created for Task 21: documents same-root leaf-to-master row sync planning, status derivation, manual scope preservation, and the preview/write boundary. Verification metadata left blank until closeout stamps the first code commit for this new file.
