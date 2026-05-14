# AGENTS.md

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember-md                         |
| path                   | `AGENTS.md`                                |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-05-15T00:38+02:00                     |
| lastVerifiedCommitHash | `3a5e72d961b489a7ebb2071e73d0af2247d0ca34` |
| lastVerifiedCommitDate | 2026-05-15T00:52:32+02:00|

## Purpose

`AGENTS.md` is the repo-root operating contract for agents working in the
`agents-remember-md` checkout. It defines the three task/work formats, the
workflow-before-code rule, the C-08 resolver requirement, and the coordinator
and memory-layer settings surfaces agents should consult after context
resolution.

## Code Commentary

### Logic

The file routes work into Chat, W-02 Light Task, or W-01 Heavy Task based on
task size and explicit developer intent, then blocks code changes outside the
selected workflow. It tells agents that onboarding is companion context for
source files and that C-08 must resolve the active memory and coordination
context before onboarding, task files, docs, or tools are trusted. The new
coordination and memory-layer sections fold the runtime template wording back
into the repo-root contract so the checkout itself carries the same settings
and authority model that the installed coordinator root will use.

### Conventions

Workflow names are stable contracts. C-* skills are core support skills, and
W-* skills are task workflows. Coordinator settings are treated as workspace
defaults, while memory-layer settings are repository-specific and more
authoritative for their own code repository.

### Invariants And Boundaries

Agents must choose one of the three workflow formats before changing code. C-08
owns context resolution and returns the memory, coordination, onboarding, task,
docs, tools, and ledger facts that downstream workflows consume. Worktree and
branch movement remain approval-gated, and repository-specific memory-layer
guidance wins over coordinator-wide guidance when the two conflict.

### Todos

Refresh verification metadata after the current `AGENTS.md` source reshuffle is
committed.

### Docs References

No external domain documentation is needed to prove this repository-local agent
contract.

| Finding                                                                                           | Citations | Source Path |
| ------------------------------------------------------------------------------------------------- | --------- | ----------- |
| No relevant external documentation found; same-repository workflow files are the direct evidence. | n/a       | n/a         |

## Repo-Internal References

The active repo behavior depends on the task routing, resolver contract,
settings routing, and approval boundaries in this file.

| Finding                                                                                                                               | Citations | Source Path                               |
| ------------------------------------------------------------------------------------------------------------------------------------- | --------- | ----------------------------------------- |
| Task format routing assigns Chat, W-02 Light Task, and W-01 Heavy Task by task size and explicit developer request.                   | L3-L24    | [AGENTS.md](agents-remember-md/AGENTS.md) |
| Memory system rules define onboarding as companion context and require C-08 resolution through `code_repository_name` or root.        | L28-L45   | [AGENTS.md](agents-remember-md/AGENTS.md) |
| Coordinator settings are workspace defaults, memory-layer settings are repository-specific, and the memory layer wins on conflicts.   | L47-L75   | [AGENTS.md](agents-remember-md/AGENTS.md) |

## Cross-Repo References

The file applies as workspace instruction when a sibling project's root
`AGENTS.md` points back to this repository, but this onboarding unit does not
need a sibling repository citation to explain the file itself.

| Finding                                                               | Citations | Source Path |
| --------------------------------------------------------------------- | --------- | ----------- |
| No meaningful cross-repo references found for current file semantics. | n/a       | n/a         |

## Update History

- 2026-05-15T00:38+02:00: Refreshed after coordinator and memory-layer settings guidance was folded into the repo-root contract during the `AGENTS.md` template reshuffle. Verification metadata remains pinned to the last committed source until closeout.
- 2026-05-12T18:51+02:00: Refreshed after AGENTS.md emphasized the workflow-before-code warning and separated it from the memory section.
- 2026-05-12T11:30: Updated after AGENTS.md was shortened to the three workflow formats, workflow-before-code rule, and C-08 resolver contract.
- 2026-05-11T19:52: Corrected escaped workflow wildcard wording introduced during the verification refresh.
- 2026-05-11T19:42: Refreshed verification metadata against commit `aa85d3862bf21fed791e3170e6957f9288c319e8` after coordination rename verification.
- 2026-05-11T18:34: Updated after the memory system rules switched fallback resolver language to `code_repository_name` and `code_repository_root`.
- 2026-05-10T03:01: Updated after chat-mode closeout guidance routed approved micro edits through C-09 `direct-closeout`.
- 2026-05-09T21:15: Created first file-level onboarding baseline for the agent operating contract.
- 2026-05-09T21:59: Updated for split memory/coordination terminology and C-09 worktree context.
- 2026-05-09T22:57: Refreshed against commit `bb95b99` and tightened references around the six-gate onboarding workflow.
