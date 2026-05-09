# AGENTS.md

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember-md                         |
| path                   | `AGENTS.md`                                |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-05-09T22:57                           |
| lastVerifiedCommitHash | `bb95b9956d55c70555bbbbcd236ca9ab62cd7261` |
| lastVerifiedCommitDate | 2026-05-09T22:15                           |

## Purpose

`AGENTS.md` is the repo's operating contract for agents. It defines how work is classified, when durable task files are required, when approval is required, and how onboarding must be resolved, checked, and refreshed before it is trusted.

## Code Commentary

### Logic

The file starts with collaboration doctrine and then routes work into Chat, W-02, W-01, or P-* workflows by size and risk. The coding workflow requires C-08 context resolution and C-02 drift detection before relying on onboarding. It treats `memory_root` and `coordination_root` as separate resolved facts and defines a six-gate start-of-task onboarding gate before planning against existing onboarding.

### Conventions

Workflow names are treated as stable contracts. C-* skills are core support skills, W-* skills are task workflows, and P-* skills are heavy workflow phases. The file uses directive language because it is meant to constrain agent behavior rather than merely describe it.

### Invariants And Boundaries

Agents must not start source-code implementation before approval on non-trivial work. Onboarding updates are allowed after approval or as standalone onboarding maintenance. C-08 owns context resolution, C-02 owns drift detection, C-05 owns onboarding creation or update, and C-09 owns worktree lifecycle mutation.

### Todos

No standalone TODO is recorded in this onboarding pass. Future worktree-support changes may need to update this file when the implemented workflow roots change.

### Docs References

No external domain documentation is needed to prove this repository-local agent contract.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No relevant external documentation found; same-repository workflow files are the direct evidence. | n/a | n/a |

## Repo-Internal References

The active repo behavior depends on the task routing and onboarding gates in this file.

| Finding | Citations | Source Path |
| --- | --- | --- |
| Task format routing assigns Chat, W-02, W-01, and heavy workflows by scope and risk. | L307-L323 | [AGENTS.md](agents-remember-md/AGENTS.md) |
| Chat coding workflow starts by resolving context with C-08, checking onboarding drift with C-02, and propagating durable onboarding updates through C-05. | L330-L336 | [AGENTS.md](agents-remember-md/AGENTS.md) |
| Memory system rules distinguish memory roots, coordination roots, onboarding roots, task roots, and shared topology behavior. | L349-L379 | [AGENTS.md](agents-remember-md/AGENTS.md) |
| The hard onboarding gate binds task start to C-08 resolution, C-02 drift detection, C-05 refresh when requested, verification rerun, reporting, and drift report cleanup. | L386-L414 | [AGENTS.md](agents-remember-md/AGENTS.md) |
| Implementation rules require C-05 onboarding propagation before an implementation phase is considered done. | L439-L451 | [AGENTS.md](agents-remember-md/AGENTS.md) |

## Cross-Repo References

The file applies as workspace instruction when `C:\ew\AGENTS.md` points sibling projects back to this repository, but this onboarding unit does not need an external repo citation to explain the file itself.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No meaningful cross-repo references found for current file semantics. | n/a | n/a |

## Update History

- 2026-05-09T21:15: Created first file-level onboarding baseline for the agent operating contract.
- 2026-05-09T21:59: Updated for split memory/coordination terminology and C-09 worktree context.
- 2026-05-09T22:57: Refreshed against commit `bb95b99` and tightened references around the six-gate onboarding workflow.
