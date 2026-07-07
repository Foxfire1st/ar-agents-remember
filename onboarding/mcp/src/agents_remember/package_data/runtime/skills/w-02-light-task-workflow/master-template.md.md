# `w-02-light-task-workflow` master-template.md

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember                         |
| path                   | `mcp/src/agents_remember/package_data/runtime/skills/w-02-light-task-workflow/master-template.md` |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-07-07T21:00+02:00 |
| lastVerifiedCommitHash | `2c464cf4c29b60165fecae722bf76c307aaac6f1` |
| lastVerifiedCommitDate | 2026-07-07T22:59:19+02:00|

## Purpose

This is the canonical scaffold for a `w-02-light-task-workflow` skill **master + light sub-task series** — the composition that
replaces the retired heavy workflow when a task outgrows a single-page plan. It defines the series
convention, the master `task.md` scaffold, and the per-slice sub-task scaffold.

## Code Commentary

### Logic

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
performs terminal cleanup/task-document reconciliation after integration. Each slice is test-verified before its commit. Decision
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
| The `w-02-light-task-workflow` skill lists `master-template.md` as a companion and adds the master-task composition section + invariant 13. | n/a | [`w-02-light-task-workflow` SKILL.md](agents-remember/mcp/src/agents_remember/package_data/runtime/skills/w-02-light-task-workflow/SKILL.md) |
| The `w-02-light-task-workflow` skill workflow's "Master Task Series" section describes the one-worktree / commit-per-slice / one-integrate lifecycle. | n/a | [`w-02-light-task-workflow` workflow.md](agents-remember/mcp/src/agents_remember/package_data/runtime/skills/w-02-light-task-workflow/workflow.md) |

As of HFX-L6 the escalation line names the architect lifecycle's `decide` step plainly.

## Cross-Repo References

No sibling repository evidence is needed for this template.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No meaningful cross-repo references found. | n/a | n/a |

## Series-Contract Notes

The master template's execution model now says a master provides the integration branch and each active sub-task gets its own leaf enclosure/worktree, replacing the previous single shared worktree guidance.

## Update History

- 2026-07-07T21:00+02:00 — 260707-HFX-L6 architect/orchestrator split: changed the
  master-template escalation pointer from the orchestrator lifecycle's decide step to the
  architect lifecycle's decide step. Sync-propagated bundle copy. Verification metadata pinned
  until closeout stamps the HFX-L6 commit.

- 2026-07-05T16:30+02:00 - L8 seam-ruling remediation (cycle 4): retired build-mode vocabulary removed. Verification metadata pinned until closeout stamps the L8 commit.
- 2026-07-05T01:32+02:00 - L9 lifecycle convergence: the escalation reference now names the l-01-agent-lifecycles orchestrator lifecycle's decide step. Verification metadata pinned until closeout stamps the L9 commit.
- 2026-06-24T06:35+02:00 - Series-contract leaf enclosure slice: packaged master template now teaches "one master integration branch, one leaf enclosure per active sub-task" instead of a single shared series worktree. Verification metadata pinned until closeout stamps the code commit.
- 2026-06-23T22:50+02:00: Dashboard task 14 — updated the master-series convention from integrate+cleanup to integrate+finalize, with `lifecycle_finalize_task` owning terminal cleanup/task-document reconciliation. Verification metadata pinned until closeout stamps the source commit.
- 2026-06-02T04:10+02:00: Created onboarding for the new `w-02-light-task-workflow` skill `master-template.md` (master + light sub-task series scaffold) that formalizes the convention this series prototyped. `l-01-agent-lifecycles` skill series, Sub-task B/S5, mcp 1.1.0.
