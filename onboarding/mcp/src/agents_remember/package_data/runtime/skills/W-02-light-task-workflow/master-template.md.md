# W-02 master-template.md

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember-md                         |
| path                   | `mcp/src/agents_remember/package_data/runtime/skills/W-02-light-task-workflow/master-template.md` |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-06-02T04:10+02:00                     |
| lastVerifiedCommitHash | `5aadda92c9b3c104418770410d49b275deef95c2` |
| lastVerifiedCommitDate | 2026-06-02T03:58:52+02:00|

## Purpose

This is the canonical scaffold for a W-02 **master + light sub-task series** — the composition that
replaces the retired heavy workflow when a task outgrows a single-page plan. It defines the series
convention, the master `task.md` scaffold, and the per-slice sub-task scaffold.

## Code Commentary

### Logic

The file states when to escalate to a series (L-01 `decide` build-mode, once size is apparent), the
series convention (one wrapper folder = master `task.md` + flat numbered `NN_<name>.md` sub-task files
in execution order), and the lifecycle: **one task = one workflow = one worktree**, a commit per slice
via C-09 closeout behind a commit gate, the worktree open across slices, and a single integrate +
release at the end with the master owning the version bump. It then gives a master `task.md` scaffold
(Objective, Sub-tasks execution order, Single Release, Shared Decisions, Open Questions, References)
and a sub-task `NN_<name>.md` scaffold, plus usage rules.

### Conventions

Sub-task files are flat and numbered, never nested phase folders. File numbers are stable creation IDs
while the master's Sub-tasks list is the authoritative execution order. The template was derived from
the hand-rolled master this very lifecycle-reshape series used (`260601_l01-lifecycle-reshape`).

### Invariants And Boundaries

A master series runs in one shared worktree (never one per sub-task). Only the master records the
version bump and release; sub-tasks never bump. Each slice is test-verified before its commit. Decision
logs are append-only in both the master and the sub-task files.

### Todos

No current todo is recorded for this template.

### Docs References

No external domain documentation applies to this repository-local template.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No relevant external documentation found. | n/a | n/a |

## Repo-Internal References

| Finding | Citations | Source Path |
| --- | --- | --- |
| The W-02 skill lists `master-template.md` as a companion and adds the master-task composition section + invariant 13. | n/a | [W-02 SKILL.md](agents-remember-md/mcp/src/agents_remember/package_data/runtime/skills/W-02-light-task-workflow/SKILL.md) |
| The W-02 workflow's "Master Task Series" section describes the one-worktree / commit-per-slice / one-integrate lifecycle. | n/a | [W-02 workflow.md](agents-remember-md/mcp/src/agents_remember/package_data/runtime/skills/W-02-light-task-workflow/workflow.md) |

## Cross-Repo References

No sibling repository evidence is needed for this template.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No meaningful cross-repo references found. | n/a | n/a |

## Update History

- 2026-06-02T04:10+02:00: Created onboarding for the new W-02 `master-template.md` (master + light sub-task series scaffold) that formalizes the convention this series prototyped. L-01 series, Sub-task B/S5, mcp 1.1.0.
