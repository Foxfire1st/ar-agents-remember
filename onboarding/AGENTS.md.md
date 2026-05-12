# AGENTS.md

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember-md                         |
| path                   | `AGENTS.md`                                |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-05-12T11:30                           |
| lastVerifiedCommitHash | `3274222c6f818f2241073eecd351cc6f6cb43e07` |
| lastVerifiedCommitDate | 2026-05-12T11:38:46+02:00|

## Purpose

`AGENTS.md` is the repo's operating contract for agents. It defines the three task/work formats, the workflow-before-code rule, and the memory/context resolver entry point agents must use before relying on onboarding or task artifacts.

## Code Commentary

### Logic

The file routes work into Chat, W-02 Light Task, or W-01 Heavy Task based on task size and explicit developer intent. It adds a hard workflow discipline line before the memory system section, then tells agents that onboarding is companion context for source files and that C-08 must resolve `code_repository_name` or `code_repository_root` into the active memory and coordination context before onboarding, tasks, docs, or tools are trusted.

### Conventions

Workflow names are treated as stable contracts. C-* skills are core support skills, and W-* skills are task workflows. The file uses directive language because it is meant to constrain agent behavior rather than merely describe it.

### Invariants And Boundaries

Agents must choose one of the three workflow formats before changing code. C-08 owns context resolution and returns the memory, coordination, onboarding, task, docs, tools, and ledger facts that downstream workflows consume.

### Todos

No standalone TODO is recorded in this onboarding pass.

### Docs References

No external domain documentation is needed to prove this repository-local agent contract.

| Finding                                                                                           | Citations | Source Path |
| ------------------------------------------------------------------------------------------------- | --------- | ----------- |
| No relevant external documentation found; same-repository workflow files are the direct evidence. | n/a       | n/a         |

## Repo-Internal References

The active repo behavior depends on the task routing and resolver contract in this file.

| Finding                                                                                                                      | Citations | Source Path                               |
| ---------------------------------------------------------------------------------------------------------------------------- | --------- | ----------------------------------------- |
| Task format routing assigns Chat, W-02 Light Task, and W-01 Heavy Task by task size and explicit developer request.          | L1-L22    | [AGENTS.md](agents-remember-md/AGENTS.md) |
| The file explicitly forbids code changes outside one of the named workflows.                                                  | L24-L24   | [AGENTS.md](agents-remember-md/AGENTS.md) |
| Memory system rules define onboarding as companion context and require C-08 resolution through `code_repository_name` or root. | L26-L40   | [AGENTS.md](agents-remember-md/AGENTS.md) |

## Cross-Repo References

The file applies as workspace instruction when `C:\ew\AGENTS.md` points sibling projects back to this repository, but this onboarding unit does not need an external repo citation to explain the file itself.

| Finding                                                               | Citations | Source Path |
| --------------------------------------------------------------------- | --------- | ----------- |
| No meaningful cross-repo references found for current file semantics. | n/a       | n/a         |

## Update History

- 2026-05-12T11:30: Updated after AGENTS.md was shortened to the three workflow formats, workflow-before-code rule, and C-08 resolver contract.
- 2026-05-11T19:52: Corrected escaped workflow wildcard wording introduced during the verification refresh.
- 2026-05-11T19:42: Refreshed verification metadata against commit `aa85d3862bf21fed791e3170e6957f9288c319e8` after coordination rename verification.
- 2026-05-11T18:34: Updated after the memory system rules switched fallback resolver language to `code_repository_name` and `code_repository_root`.
- 2026-05-10T03:01: Updated after chat-mode closeout guidance routed approved micro edits through C-09 `direct-closeout`.
- 2026-05-09T21:15: Created first file-level onboarding baseline for the agent operating contract.
- 2026-05-09T21:59: Updated for split memory/coordination terminology and C-09 worktree context.
- 2026-05-09T22:57: Refreshed against commit `bb95b99` and tightened references around the six-gate onboarding workflow.
