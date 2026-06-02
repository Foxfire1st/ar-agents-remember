# W-02 workflow.md

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember-md                         |
| path                   | `mcp/src/agents_remember/package_data/runtime/skills/W-02-light-task-workflow/workflow.md` |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-05-31T01:06+02:00                     |
| lastVerifiedCommitHash | `5aadda92c9b3c104418770410d49b275deef95c2` |
| lastVerifiedCommitDate | 2026-06-02T03:58:52+02:00|

## Purpose

This workflow file gives the step-by-step W-02 procedure for creating a task wrapper, planning in `task.md`, approving implementation, implementing, validating, requesting separate commit approval for worktree-backed closeout, and closing a light durable task.

## Code Commentary

### Logic

The workflow starts with context resolution and drift checks, classifies C-02 drift into clean-source update candidates versus dirty-source active work-in-progress, creates or reuses a task wrapper folder, applies the Task Collaboration Doctrine (`tasks/AGENTS.md`) sized to the request and records the settled design in the task file's `## Design` section, writes `task.md` from the template, stops for approval, then executes checklist items while keeping the task artifact current. The wrapper folder is created before C-09 worktrees; refreshed external-memory onboarding and ledger changes are committed before worktree start; worktree-backed light tasks later keep `contract.md` beside `task.md` under the C-08 resolved task root. After implementation, worktree-backed tasks prepare a C-09 closeout dry-run and stop for explicit commit approval before any closeout commits are created. A "Master Task Series" section documents escalating a too-large task to a master + light sub-task series run as one task / one workflow / one worktree: a commit per slice behind a commit gate, the worktree open across slices, and a single integrate + release at the end.

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
| Light-task artifacts use `<task-root>/<task-slug>/task.md`, and C-09 later places `contract.md` beside `task.md` when worktrees are created. | L15-L25 | [W-02 workflow.md](agents-remember-md/mcp/src/agents_remember/package_data/runtime/skills/W-02-light-task-workflow/workflow.md) |
| Drift-gated planning now records that clean-source update candidates are refreshed through C-05, dirty-source drift is left alone unless explicitly owned, and refreshed external-memory onboarding plus ledger changes must be committed before any C-09 worktree starts. | L45-L52 | [W-02 workflow.md](agents-remember-md/mcp/src/agents_remember/package_data/runtime/skills/W-02-light-task-workflow/workflow.md) |
| Drift detection is part of task planning before the durable plan is finalized. | L45-L51 | [W-02 workflow.md](agents-remember-md/mcp/src/agents_remember/package_data/runtime/skills/W-02-light-task-workflow/workflow.md) |
| Planning checks C-08 resolved docs, sources, and onboarding roots before writing the approval artifact. | L57-L64; L98-L115 | [W-02 workflow.md](agents-remember-md/mcp/src/agents_remember/package_data/runtime/skills/W-02-light-task-workflow/workflow.md) |
| Implementation, validation, onboarding propagation, closeout preview, and commit approval handoff are one checklist-driven cycle. | L117-L174 | [W-02 workflow.md](agents-remember-md/mcp/src/agents_remember/package_data/runtime/skills/W-02-light-task-workflow/workflow.md) |
| Before writing `task.md`, the workflow applies the Task Collaboration Doctrine sized to the request and records the settled design in the task file's `## Design` section, from which the implementation steps derive. | L66-L73; L85 | [W-02 workflow.md](agents-remember-md/mcp/src/agents_remember/package_data/runtime/skills/W-02-light-task-workflow/workflow.md) |

## Cross-Repo References

No sibling repository evidence is needed for the current workflow file.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No meaningful cross-repo references found. | n/a | n/a |

## Update History

- 2026-06-02T04:10+02:00: Added a "Master Task Series" section documenting escalation to a master + light sub-task series (one worktree per series, a commit per slice, one integrate + release at the end). L-01 series, Sub-task B/S5, mcp 1.1.0.
- 2026-05-31T01:06+02:00: Added step 6 "Reframe and design before writing the plan" linking the Task Collaboration Doctrine and recording settled design in the task file's `## Design` section before implementation steps; renumbered later steps to 7 and 8, added the design item to the required-sections list, and refreshed the citations my insertion shifted.
- 2026-05-24T18:10+02:00: Moved onboarding to mirror the packaged runtime source route under `mcp/src/agents_remember/package_data/runtime/` after F-10 packaged runtime asset discovery.
- 2026-05-24T10:06+02:00: Refreshed verification metadata after source commit `f48a346` added clean-source versus dirty-source drift classification to W-02 planning.
- 2026-05-24T04:34+02:00: Updated task-start references after C-02 was renamed to memory quality control.
- 2026-05-10T01:19: Updated after Phase 2 gained the closeout dry-run and explicit commit approval handoff for worktree-backed tasks.
- 2026-05-10T00:56: Updated the C-09 handoff rule so refreshed external-memory onboarding and ledger changes are committed before worktree start.
- 2026-05-10T00:47: Updated W-02 phase language so task wrapper folders are created before any C-09 worktree.
- 2026-05-09T22:57: Refreshed verification metadata and updated W-02 citations.
- 2026-05-09T21:59: Updated for worktree-backed task folders and C-08 resolved tools/sources paths.
- 2026-05-09T21:15: Created first file-level onboarding baseline for W-02 workflow steps.
