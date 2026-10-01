# `w-02-light-task-workflow` master-template.md

## Purpose

This is the canonical scaffold for a `w-02-light-task-workflow` skill **master + light sub-task series** — the composition that
replaces the retired heavy workflow when a task outgrows a single-page plan. It defines the series
convention, the master `task.md` scaffold, and the per-slice sub-task scaffold.

## Code Commentary

### Logic

The synchronized master template projects only formal review-handoff attempts, excludes internal
protocol events from counts, and links lightweight leaf records to content-addressed expanded
evidence.

The file states when to escalate to a series (`l-01-agent-lifecycles` architect lifecycle `decide` step, once size is apparent), the
series convention (one wrapper folder = master `task.md` + flat numbered `NN_<name>.md` sub-task files
in execution order), and the lifecycle: **one task = one workflow = one worktree**, a commit per slice
via `c-09-git-worktree-manager` skill closeout behind a commit gate, the worktree open across slices, and a single integrate +
`lifecycle_finalize_task` + release at the end with the master owning the version bump. It then gives a master `task.md` scaffold
(Objective, Sub-tasks execution order, Single Release, Shared Decisions, Open Questions, References)
and a sub-task `NN_<name>.md` scaffold, plus usage rules.

### Conventions

Sub-task files are flat and numbered, never nested phase folders. File numbers are stable creation IDs
while the master's Sub-tasks list is the authoritative execution order. The template was derived from
the hand-rolled master this very lifecycle-reshape series used (`260601_l01-lifecycle-reshape`).

### Invariants And Boundaries

A master series runs in one shared worktree (never one per sub-task). Only the master records the
version bump and release; sub-tasks never bump. `lifecycle_finalize_task` proves the landed edge and
performs terminal cleanup/task-document reconciliation after integration. Each slice reports its relevant targeted checks, including any
failed or not-run result, before its commit transaction. Decision
logs are append-only in both the master and the sub-task files.

### Todos

No current todo is recorded for this template.


## CCR-R12@v5 Light-Task Boundary

A light-task handoff records relevant targeted checks and honest failed or not-run results before the authorized Git transaction. Its commit legs suppress automatic quality and test hooks while ordinary explicit Git hook policy outside closeout/integration remains unchanged. Curation is the exception: the curator always runs the complete memory-quality operation as part of curation, and closeout and integration carry its completed result as a prerequisite, while full code quality, full tests, certification, and review remain explicit operations rather than automatic closeout or integration prerequisites.

### Docs References

No external domain documentation applies to this repository-local template.

No relevant external documentation found.

## Evidence

### Repo-Internal References

- The `w-02-light-task-workflow` skill lists `master-template.md` as a companion and adds the master-task composition section + invariant 13. [1]
- The `w-02-light-task-workflow` skill workflow's "Master Task Series" section describes the one-worktree / commit-per-slice / one-integrate lifecycle. [2]

As of HFX-L6 the escalation line names the architect lifecycle's `decide` step plainly.

### Cross-Repo References

No sibling repository evidence is needed for this template.

No meaningful cross-repo references found.

## Series-Contract Notes

The master template's execution model now says a master provides the integration branch and each active sub-task gets its own leaf enclosure/worktree, replacing the previous single shared worktree guidance.

## M38 Series Requirement Projection

Master and leaf scaffolds now use stable series-qualified IDs, declare ownership, and require each
leaf handoff/review pair to cover its exact leaf-owned plus inherited master set. Every row receives
worker evidence and independent accepted/rejected adjudication; any rejection prevents completion.
The durable-evidence promotion hold point is recorded separately. This installed file is a
synchronized projection only.
Filtered rows link immutable version-addressed packets carrying their durable corpus approval;
neither master nor leaf rewrites or silently upgrades an approved revision.

## M40-M45 Master-Summary Projection

The installed master scaffold exposes attempts, rejection history, current state, dominant class,
and leaf-journal refs through a rebuildable observation that is explicitly never a task,
lifecycle, closeout, integration, or queue authority.

## 2026-08-27 Attempt Boundary Clarification

This packaged projection preserves the canonical phase boundary: validate before append; a
malformed never-handed-off row receives a non-attempt correction/void without consuming an ID;
a malformed handed-off attempt requires independent rejection before successor handoff.
