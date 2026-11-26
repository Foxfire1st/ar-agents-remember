# skills/l-01-agent-lifecycles/reference/coordination/shared/master-state.md

## Governing Overview

[overview](../../../overview.md)

## Purpose

The rules Managers, Architects and Orchestrators follow, within their assigned scope, for updating master state through completion. It grants no additional authority.

## Code Commentary

In the same turn as each start, role handover and landing, the acting seat updates the parts of the master document that act changed: status note, counts, order state and the **In work now** section, with task, stage, agents and the time since that state began. Product-mirrored stage fields stay with their existing owner, and no contradictory second status is written. Before completing a master, the seat checks that the master's documentation task changed or confirmed every document the master's tasks made stale, and does not report the master complete while any stays stale. The Orchestrator and Architect roles point to the update section; the Manager role points to the update, completion and abandonment sections before updating master state through completion.

An atomic master's document must read `abandoned` or `Completed` before `worktree_abandon`; otherwise it refuses `abandon-master-not-terminal`, and an admitted call writes `abandoned`. The answer measures `landedWork` by ancestry. A recorded master landing reports `staleEntries` at changed paths as the master's debt, to be repaired by a knowledge-maintenance leaf. An incomplete-integration cleanup names `worktree_record_landing` as the next step, and leaf closeout still refuses a non-current entry at a changed path.

## Evidence

- Master updates follow every start, handover and landing in the same turn and leave product-mirrored fields with their owner. [1]
- A master is not reported complete while documentation made stale by its tasks remains. [2]

- The Manager role reference index points here for master state (`task_doc`, `worktree_abandon`, `record_landing`). [3]
