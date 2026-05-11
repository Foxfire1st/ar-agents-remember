# AGENTS.md

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember-md                         |
| path                   | `AGENTS.md`                                |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-05-11T19:52                           |
| lastVerifiedCommitHash | `aa85d3862bf21fed791e3170e6957f9288c319e8` |
| lastVerifiedCommitDate | 2026-05-11T19:32                           |

## Purpose

`AGENTS.md` is the repo's operating contract for agents. It defines how work is classified, when durable task files are required, when approval is required, and how onboarding must be resolved, checked, and refreshed before it is trusted.

## Code Commentary

### Logic

The file starts with collaboration doctrine and then routes work into Chat, W-02, W-01, or P-\* workflows by size and risk. The coding workflow requires C-08 context resolution with `code_repository_name` or `code_repository_root` and C-02 drift detection before relying on onboarding, requires paired source/onboarding reads before planning, requires approval before code edits, and now routes small approved chat-mode current-checkout edits through C-09 `direct-closeout` for shared-memory commit sequencing. It treats `memory_root` and `coordination_root` as separate resolved facts, names shared topology by shared memory, and defines a six-gate start-of-task onboarding gate before planning against existing onboarding.

### Conventions

Workflow names are treated as stable contracts. C-* skills are core support skills, W-* skills are task workflows, and P-* skills are heavy workflow phases. The file uses directive language because it is meant to constrain agent behavior rather than merely describe it.

### Invariants And Boundaries

Agents must not start source-code implementation before approval on non-trivial work. Onboarding updates are allowed after approval or as standalone onboarding maintenance. C-08 owns context resolution, C-02 owns drift detection, C-05 owns onboarding creation or update, and C-09 owns Git lifecycle mutation for worktree-backed tasks and direct current-checkout closeout.

### Todos

No standalone TODO is recorded in this onboarding pass. Future worktree-support changes may need to update this file when the implemented workflow roots change.

### Docs References

No external domain documentation is needed to prove this repository-local agent contract.

| Finding                                                                                           | Citations | Source Path |
| ------------------------------------------------------------------------------------------------- | --------- | ----------- |
| No relevant external documentation found; same-repository workflow files are the direct evidence. | n/a       | n/a         |

## Repo-Internal References

The active repo behavior depends on the task routing and onboarding gates in this file.

| Finding                                                                                                                                                                                                                                                                | Citations | Source Path                               |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------- | ----------------------------------------- |
| Task format routing assigns Chat, W-02, W-01, and heavy workflows by scope and risk.                                                                                                                                                                                   | L330-L348 | [AGENTS.md](agents-remember-md/AGENTS.md) |
| Chat coding workflow starts by resolving context with C-08, checking onboarding drift with C-02, propagating durable onboarding updates through C-05, and routing approved small current-checkout edits through C-09 `direct-closeout` for code/memory/ledger commits. | L353-L365 | [AGENTS.md](agents-remember-md/AGENTS.md) |
| Memory system rules distinguish code repository inputs, memory roots, coordination roots, onboarding roots, task roots, and shared topology behavior.                                                                                                                  | L374-L407 | [AGENTS.md](agents-remember-md/AGENTS.md) |
| The hard onboarding gate binds task start to C-08 resolution, C-02 drift detection, C-05 refresh when requested, verification rerun, reporting, and drift report cleanup.                                                                                              | L411-L459 | [AGENTS.md](agents-remember-md/AGENTS.md) |
| Implementation rules require C-05 onboarding propagation before an implementation phase is considered done.                                                                                                                                                            | L464-L476 | [AGENTS.md](agents-remember-md/AGENTS.md) |

## Cross-Repo References

The file applies as workspace instruction when `C:\ew\AGENTS.md` points sibling projects back to this repository, but this onboarding unit does not need an external repo citation to explain the file itself.

| Finding                                                               | Citations | Source Path |
| --------------------------------------------------------------------- | --------- | ----------- |
| No meaningful cross-repo references found for current file semantics. | n/a       | n/a         |

## Update History

- 2026-05-11T19:52: Corrected escaped workflow wildcard wording introduced during the verification refresh.
- 2026-05-11T19:42: Refreshed verification metadata against commit `aa85d3862bf21fed791e3170e6957f9288c319e8` after coordination rename verification.
- 2026-05-11T18:34: Updated after the memory system rules switched fallback resolver language to `code_repository_name` and `code_repository_root`.
- 2026-05-10T03:01: Updated after chat-mode closeout guidance routed approved micro edits through C-09 `direct-closeout`.
- 2026-05-09T21:15: Created first file-level onboarding baseline for the agent operating contract.
- 2026-05-09T21:59: Updated for split memory/coordination terminology and C-09 worktree context.
- 2026-05-09T22:57: Refreshed against commit `bb95b99` and tightened references around the six-gate onboarding workflow.
