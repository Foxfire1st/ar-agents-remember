# W-02 workflow.md

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember-md                         |
| path                   | `runtime/skills/W-02-light-task-workflow/workflow.md` |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-05-10T01:19                           |
| lastVerifiedCommitHash | `398184b757e336211e335569284f2cde309cd964` |
| lastVerifiedCommitDate | 2026-05-15T04:04:02+02:00|

## Purpose

This workflow file gives the step-by-step W-02 procedure for creating a task wrapper, planning in `task.md`, approving implementation, implementing, validating, requesting separate commit approval for worktree-backed closeout, and closing a light durable task.

## Code Commentary

### Logic

The workflow starts with context resolution and drift checks, creates or reuses a task wrapper folder, writes `task.md` from the template, stops for approval, then executes checklist items while keeping the task artifact current. The wrapper folder is created before C-09 worktrees; refreshed external-memory onboarding and ledger changes are committed before worktree start; worktree-backed light tasks later keep `contract.md` beside `task.md` under the C-08 resolved task root. After implementation, worktree-backed tasks prepare a C-09 closeout dry-run and stop for explicit commit approval before any closeout commits are created.

### Conventions

The workflow treats `task.md` as active state inside the wrapper folder. It uses checkboxes for implementation progress and a decision log for durable choices, and refers to C-08 resolved `tools_path` and `sources_path`.

### Invariants And Boundaries

Implementation cannot begin until the task artifact is approved. Drift detection must happen before planning if onboarding exists, and onboarding changes must be handled through C-05. Worktree-backed closeout commits cannot be created until the developer approves the closeout preview.

### Todos

Add examples once a real C-09-wrapped W-02 task has been run.

### Docs References

No external domain documentation applies to this repository-local workflow.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No relevant external documentation found. | n/a | n/a |

## Repo-Internal References

The workflow defines the concrete process behind the W-02 skill.

| Finding | Citations | Source Path |
| --- | --- | --- |
| Light-task artifacts use `<task-root>/<task-slug>/task.md`, and C-09 later places `contract.md` beside `task.md` when worktrees are created. | L15-L25 | [W-02 workflow.md](agents-remember-md/runtime/skills/W-02-light-task-workflow/workflow.md) |
| Drift-gated planning now records that refreshed external-memory onboarding and ledger changes must be committed before any C-09 worktree starts. | L45-L52 | [W-02 workflow.md](agents-remember-md/runtime/skills/W-02-light-task-workflow/workflow.md) |
| Drift detection is part of task planning before the durable plan is finalized. | L45-L51 | [W-02 workflow.md](agents-remember-md/runtime/skills/W-02-light-task-workflow/workflow.md) |
| Planning checks C-08 resolved docs, sources, and onboarding roots before writing the approval artifact. | L53-L64; L88-L105 | [W-02 workflow.md](agents-remember-md/runtime/skills/W-02-light-task-workflow/workflow.md) |
| Implementation, validation, onboarding propagation, closeout preview, and commit approval handoff are one checklist-driven cycle. | L107-L164 | [W-02 workflow.md](agents-remember-md/runtime/skills/W-02-light-task-workflow/workflow.md) |

## Cross-Repo References

No sibling repository evidence is needed for the current workflow file.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No meaningful cross-repo references found. | n/a | n/a |

## Update History

- 2026-05-10T01:19: Updated after Phase 2 gained the closeout dry-run and explicit commit approval handoff for worktree-backed tasks.
- 2026-05-10T00:56: Updated the C-09 handoff rule so refreshed external-memory onboarding and ledger changes are committed before worktree start.
- 2026-05-10T00:47: Updated W-02 phase language so task wrapper folders are created before any C-09 worktree.
- 2026-05-09T21:15: Created first file-level onboarding baseline for W-02 workflow steps.
- 2026-05-09T21:59: Updated for worktree-backed task folders and C-08 resolved tools/sources paths.
- 2026-05-09T22:57: Refreshed verification metadata and updated W-02 citations.
