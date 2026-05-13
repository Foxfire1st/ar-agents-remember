# AGENTS.md

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember-md                         |
| path                   | `system/agents-md-files/coordinator/AGENTS.md` |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-05-13T19:11                           |
| lastVerifiedCommitHash | `522d5a2bdc98f7058eeac5a95ee0e67aadfbf719` |
| lastVerifiedCommitDate | 2026-05-13T19:14:23+02:00|

## Purpose

This file is the installable coordinator-level `AGENTS.md` template for an
`ar-coordination` runtime. It tells agents how to route from the coordinator
into repository-specific memory and which coordinator files carry global
instructions, tools, sources, and layout hints.

## Code Commentary

### Logic

The file identifies the coordinator as workspace-wide Agents Remember state,
then requires agents to resolve the active repository context with C-08 before
using tasks, worktrees, notes, docs, or memory repos. Its routing section points
agents to coordinator-level settings, tools, and sources while preserving the
boundary that repository-specific rules belong in the selected memory layer.

### Conventions

Coordinator guidance is treated as a default layer. Once C-08 resolves a
repository memory root, agents should read that memory layer's `AGENTS.md` and
system files for more specific repository behavior.

### Invariants And Boundaries

The coordinator file must not become a place for repository-specific policy. It
also preserves workflow approval boundaries by forbidding protected-branch
movement and worktree lifecycle changes unless the selected workflow has granted
the required approvals.

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
| The template defines the coordinator as workspace-wide Agents Remember state and requires C-08 context resolution before using coordinator task, worktree, note, doc, or memory surfaces. | L3-L9 | [system/agents-md-files/coordinator/AGENTS.md](agents-remember-md/system/agents-md-files/coordinator/AGENTS.md) |
| The routing rules map coordinator settings, JSON hints, tools, and sources, while directing repository-specific rules into the resolved memory layer. | L11-L22 | [system/agents-md-files/coordinator/AGENTS.md](agents-remember-md/system/agents-md-files/coordinator/AGENTS.md) |
| The boundary rules protect branch movement, worktree lifecycle operations, and repository-specific authority precedence. | L24-L30 | [system/agents-md-files/coordinator/AGENTS.md](agents-remember-md/system/agents-md-files/coordinator/AGENTS.md) |

## Cross-Repo References

No sibling repository evidence is needed for this package template.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No meaningful cross-repo references found. | n/a | n/a |

## Update History

- 2026-05-13T19:11: Created onboarding for the coordinator AGENTS.md install template.
