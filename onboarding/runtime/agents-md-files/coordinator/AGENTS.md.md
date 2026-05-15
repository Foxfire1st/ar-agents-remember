# AGENTS.md

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember-md                         |
| path                   | `runtime/agents-md-files/coordinator/AGENTS.md` |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-05-15T00:38+02:00                     |
| lastVerifiedCommitHash | `398184b757e336211e335569284f2cde309cd964` |
| lastVerifiedCommitDate | 2026-05-15T04:04:02+02:00|

## Purpose

This file is the package-owned template for the installed coordinator root
`AGENTS.md`. It is intended to land at `ar-coordination/AGENTS.md` after the
future runtime install layout is implemented.

## Code Commentary

### Logic

The template combines the checkout's task-format routing with coordinator
runtime guidance. It requires agents to choose Chat, W-02, or W-01 before
changing code, resolve active repository context with C-08 before trusting
memory or task surfaces, use coordinator `system/*` files for workspace-wide
defaults, and prefer the resolved memory layer when repository-specific guidance
is more restrictive.

### Conventions

The coordinator root is a workspace-wide default layer. It may direct agents to
global settings, tools, and sources, but repository-specific rules belong in the
resolved memory layer. Memory-layer settings and coding guidelines are listed
as read-first surfaces once C-08 identifies the target repository.

### Invariants And Boundaries

The installed coordinator root template must not become a per-repository policy
file. It also preserves workflow approval boundaries by forbidding protected
branch movement and worktree lifecycle operations unless the selected workflow
has granted the required approvals.

### Todos

Refresh verification metadata after the current `AGENTS.md` source reshuffle is
committed.

### Docs References

No external documentation is needed for this repository-local template.

| Finding                                   | Citations | Source Path |
| ----------------------------------------- | --------- | ----------- |
| No relevant external documentation found. | n/a       | n/a         |

## Repo-Internal References

This onboarding is backed by the source template itself.

| Finding                                                                                                                       | Citations | Source Path |
| ----------------------------------------------------------------------------------------------------------------------------- | --------- | ----------- |
| The template installs the same Chat/W-02/W-01 routing and workflow-before-code rule expected at a coordinator root.           | L3-L24    | [runtime/agents-md-files/coordinator/AGENTS.md](agents-remember-md/runtime/agents-md-files/coordinator/AGENTS.md) |
| The memory and resolver sections require C-08 before relying on onboarding, task files, docs, tools, or memory-layer state.    | L28-L45   | [runtime/agents-md-files/coordinator/AGENTS.md](agents-remember-md/runtime/agents-md-files/coordinator/AGENTS.md) |
| Coordinator defaults, memory-layer authority, branch/worktree approval boundaries, and repo-specific settings surfaces are listed in the template. | L47-L85   | [runtime/agents-md-files/coordinator/AGENTS.md](agents-remember-md/runtime/agents-md-files/coordinator/AGENTS.md) |

## Cross-Repo References

No sibling repository evidence is needed for this package template.

| Finding                                    | Citations | Source Path |
| ------------------------------------------ | --------- | ----------- |
| No meaningful cross-repo references found. | n/a       | n/a         |

## Update History

- 2026-05-15T00:38+02:00: Refreshed after the coordinator template became one of four runtime `AGENTS.md` templates and absorbed the checkout task routing plus coordinator and memory-layer guidance. Verification metadata remains pinned to the last committed source until closeout.
- 2026-05-13T19:11: Created onboarding for the coordinator AGENTS.md install template.
