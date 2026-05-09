# W-02 workflow.md

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember-md                         |
| path                   | `skills/W-02-light-task-workflow/workflow.md` |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-05-09T22:57                           |
| lastVerifiedCommitHash | `bb95b9956d55c70555bbbbcd236ca9ab62cd7261` |
| lastVerifiedCommitDate | 2026-05-09T22:15                           |

## Purpose

This workflow file gives the step-by-step W-02 procedure for planning, approving, implementing, validating, and closing a light durable task.

## Code Commentary

### Logic

The workflow starts with context resolution and drift checks, creates a task file from the template, stops for approval, then executes checklist items while keeping the task artifact current. Worktree-backed light tasks keep the task artifact beside `contract.md` under the C-08 resolved task root.

### Conventions

The workflow treats the task file as active state. It uses checkboxes for implementation progress and a decision log for durable choices, and now refers to C-08 resolved `tools_path` and `sources_path`.

### Invariants And Boundaries

Implementation cannot begin until the task artifact is approved. Drift detection must happen before planning if onboarding exists, and onboarding changes must be handled through C-05.

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
| Light-task artifacts live under the C-08 resolved task root, and worktree-backed tasks place the artifact beside `contract.md`. | L19-L20 | [W-02 workflow.md](agents-remember-md/skills/W-02-light-task-workflow/workflow.md) |
| Drift detection is part of task planning before the durable plan is finalized. | L39-L45 | [W-02 workflow.md](agents-remember-md/skills/W-02-light-task-workflow/workflow.md) |
| Planning checks C-08 resolved docs, sources, and onboarding roots before writing the approval artifact. | L51-L53; L56-L93 | [W-02 workflow.md](agents-remember-md/skills/W-02-light-task-workflow/workflow.md) |
| Implementation, validation, onboarding propagation, and closeout are one checklist-driven cycle. | L101-L145 | [W-02 workflow.md](agents-remember-md/skills/W-02-light-task-workflow/workflow.md) |

## Cross-Repo References

No sibling repository evidence is needed for the current workflow file.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No meaningful cross-repo references found. | n/a | n/a |

## Update History

- 2026-05-09T21:15: Created first file-level onboarding baseline for W-02 workflow steps.
- 2026-05-09T21:59: Updated for worktree-backed task folders and C-08 resolved tools/sources paths.
- 2026-05-09T22:57: Refreshed verification metadata and updated W-02 citations.
