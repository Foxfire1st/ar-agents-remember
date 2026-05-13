# AGENTS.md

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember-md                         |
| path                   | `system/agents-md-files/memory-repo/AGENTS.md` |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-05-13T19:11                           |
| lastVerifiedCommitHash | `522d5a2bdc98f7058eeac5a95ee0e67aadfbf719` |
| lastVerifiedCommitDate | 2026-05-13T19:14:23+02:00|

## Purpose

This file is the installable `AGENTS.md` template for each durable
Agents Remember memory repository. It establishes the memory layer as
repository-specific authority and tells agents which memory-system files to read
before relying on that memory.

## Code Commentary

### Logic

The file scopes a memory layer to one code repository and requires agents to
resolve context with C-08 and run the C-02 onboarding drift gate before trusting
memory contents. Its read-first list points agents to settings, storage policy,
tools, sources, and optional coding guidelines.

### Conventions

Repository-specific branching and workflow notes belong in the memory layer's
`system/tools.md`, where agents can discover them before using worktree
integration commands.

### Invariants And Boundaries

This template makes the memory layer more specific than coordinator-wide
guidance for its repository. It should not describe global coordinator behavior
as if it applied equally to every repository attached to the coordinator.

### Todos

None.

### Docs References

No external documentation is needed for this repository-local template.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No relevant external documentation found. | n/a | n/a |

## Repo-Internal References

This onboarding is backed by the source template itself.

| Finding | Citations | Source Path |
| --- | --- | --- |
| The template scopes a memory layer to one code repository and distinguishes it from global coordinator instructions. | L3-L5 | [system/agents-md-files/memory-repo/AGENTS.md](agents-remember-md/system/agents-md-files/memory-repo/AGENTS.md) |
| The trust gate requires C-08 context resolution and C-02 onboarding drift detection before relying on memory content. | L7-L9 | [system/agents-md-files/memory-repo/AGENTS.md](agents-remember-md/system/agents-md-files/memory-repo/AGENTS.md) |
| The read-first list identifies the memory-layer settings, storage policy, tools, sources, and optional coding guidelines that agents should inspect. | L11-L18 | [system/agents-md-files/memory-repo/AGENTS.md](agents-remember-md/system/agents-md-files/memory-repo/AGENTS.md) |
| Branch and workflow notes belong in `system/tools.md`, and memory-layer rules win over coordinator-wide defaults when more specific. | L20-L28 | [system/agents-md-files/memory-repo/AGENTS.md](agents-remember-md/system/agents-md-files/memory-repo/AGENTS.md) |

## Cross-Repo References

No sibling repository evidence is needed for this package template.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No meaningful cross-repo references found. | n/a | n/a |

## Update History

- 2026-05-13T19:11: Created onboarding for the memory-repo AGENTS.md install template.
