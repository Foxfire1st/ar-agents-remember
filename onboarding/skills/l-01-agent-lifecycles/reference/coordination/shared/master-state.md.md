# skills/l-01-agent-lifecycles/reference/coordination/shared/master-state.md

## Governing Overview

[overview](../../../overview.md)

## Purpose

The rules Managers, Architects and Orchestrators follow, within their assigned scope, for updating master state through completion. It grants no additional authority.

## Code Commentary

In the same turn as each start, role handover and landing, the acting seat updates the parts of the master document that act changed: status note, counts, order state and the **In work now** section, with task, stage, agents and the time since that state began. Product-mirrored stage fields stay with their existing owner, and no contradictory second status is written. Before completing a master, the seat checks that the master's documentation task changed or confirmed every document the master's tasks made stale, and does not report the master complete while any stays stale. The Orchestrator and Architect roles point to the update section; the Manager role's Reference index links `master-state.md` under Master (`task_doc`/`worktree_abandon`/`record_landing`).

An atomic master's document must read `abandoned` or `Completed` before `worktree_abandon`; otherwise it refuses `abandon-master-not-terminal`, and an admitted call writes `abandoned`. The answer measures `landedWork` by ancestry. A recorded master landing reports `staleEntries` at changed paths as the master's debt, to be repaired by a knowledge-maintenance leaf. An incomplete-integration cleanup names `worktree_record_landing` as the next step, and leaf closeout still refuses a non-current entry at a changed path.

`## End a standalone master` (lines 15-21) states the three-step Manager sequence for a standalone master (a series no sprint commands) whose pull request merged onto the target branch: (1) `worktree_record_landing` with the merged code commit (and merged memory commit when external memory is configured), refusing an abandoned contract or task document; (2) `lifecycle_finalize_task` on the series contract to clean up the branch and worktree folder, release the activation, and mark the master `Completed` without calling `task_doc set_status` first; and (3) `task_doc` with `operation="retire_master"` (dry run first) to archive into `0_archive/`, because finalization never archives a series master.

## Evidence

- Master updates follow every start, handover and landing in the same turn and leave product-mirrored fields with their owner. [1]
- A master is not reported complete while documentation made stale by its tasks remains. [2]

- The Manager role's Reference index links `master-state.md` under Master (`task_doc`/`worktree_abandon`/`record_landing`). \[3] [5]

- `## End a standalone master` prescribes `worktree_record_landing`, `lifecycle_finalize_task` without prior `set_status`, and `task_doc retire_master` (dry run first) because finalization never archives a series master. [4]
