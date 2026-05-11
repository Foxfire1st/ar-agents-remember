# W-02-light-task-workflow/SKILL.md

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember-md                         |
| path                   | `skills/W-02-light-task-workflow/SKILL.md` |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-05-11T19:42                           |
| lastVerifiedCommitHash | `aa85d3862bf21fed791e3170e6957f9288c319e8` |
| lastVerifiedCommitDate | 2026-05-11T19:32                           |

## Purpose

This skill defines W-02, the light durable task workflow for medium-risk or multi-step changes that need a task artifact but not the full heavy workflow stack.

## Code Commentary

### Logic

W-02 creates or updates one task wrapper folder under the C-08 resolved task root, writes the durable task document as `task.md`, stops for approval before implementation, uses the artifact checklist as the live execution record, and for worktree-backed tasks stops again for explicit commit approval before C-09 closeout creates commits.

### Conventions

The skill keeps planning and implementation in one `task.md` file inside a wrapper folder. The folder is created as soon as the task class, naming, and workflow variables are clear, before any C-09 worktree start. The task document requires explicit objective, requirements, steps, decision log, open questions, and references.

### Invariants And Boundaries

W-02 task artifacts are planning and execution state. They can trigger onboarding updates through C-05, but they should not be treated as onboarding content. If a light task later becomes worktree-backed, C-09 stores `contract.md` beside `task.md` in the same wrapper folder. Refreshed shared-memory onboarding and ledger changes must be committed before that C-09 worktree start. Implementation approval does not authorize closeout commits; the agent must present a commit preview and wait for explicit commit approval.

### Todos

No current todo is recorded for this workflow skill.

### Docs References

No external domain documentation applies to this repository-local workflow skill.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No relevant external documentation found. | n/a | n/a |

## Repo-Internal References

W-02 is the approved workflow used by the preliminary onboarding task and the worktree task stack.

| Finding | Citations | Source Path |
| --- | --- | --- |
| The skill defines the task wrapper plus `task.md` as the durable plan/checklist artifact for medium work. | L25-L36 | [W-02 SKILL.md](agents-remember-md/skills/W-02-light-task-workflow/SKILL.md) |
| Agent responsibilities include creating the wrapper artifact, stopping for implementation approval, implementing checklist items, presenting a worktree-backed commit preview, and waiting for commit approval before closeout commits. | L38-L52 | [W-02 SKILL.md](agents-remember-md/skills/W-02-light-task-workflow/SKILL.md) |
| Invariants require wrapper folders, resolved roots, no implementation before approval, a clean committed shared-memory baseline before C-09 start, separate commit approval before closeout commits, and no stale task state. | L64-L76 | [W-02 SKILL.md](agents-remember-md/skills/W-02-light-task-workflow/SKILL.md) |

## Cross-Repo References

No sibling repository evidence is needed for the current workflow skill.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No meaningful cross-repo references found. | n/a | n/a |

## Update History

- 2026-05-11T19:42: Refreshed verification metadata to `aa85d3862bf21fed791e3170e6957f9288c319e8` after confirming W-02 remains current after the coordination rename.
- 2026-05-10T01:19: Updated after W-02 gained an explicit worktree-backed commit approval handoff before C-09 closeout commits.
- 2026-05-10T00:56: Updated after adding the committed shared-memory baseline requirement before C-09 start.
- 2026-05-10T00:47: Updated after light tasks moved from flat task files to wrapper folders containing `task.md`.
- 2026-05-09T21:15: Created first file-level onboarding baseline for W-02 skill documentation.
