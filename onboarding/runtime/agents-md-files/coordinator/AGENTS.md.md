# AGENTS.md

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember-md                         |
| path                   | `runtime/agents-md-files/coordinator/AGENTS.md` |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-05-15T15:08+02:00                     |
| lastVerifiedCommitHash | `962fc96005d7141aaeb905afa63c374f07cae966` |
| lastVerifiedCommitDate | 2026-05-15T15:34:05+02:00|

## Purpose

This file is the package-owned template for the installed coordinator root
`AGENTS.md`. It is intended to land at `ar-coordination/AGENTS.md` after the
future runtime install layout is implemented.

## Code Commentary

### Logic

The template combines the checkout's task-format routing with coordinator
runtime guidance. It requires agents to choose Chat, W-02, or W-01 before
changing code, points agents to the sibling installed `system/`, `tasks/`, and
`skills/` `AGENTS.md` files when those scopes become relevant, resolves active
repository context with C-08 before trusting memory or task surfaces, and uses
coordinator `system/*` files for workspace-wide defaults. It also routes
important developer clarifications through `C-01-findings-capture` and requires
verification against code reality before onboarding propagation through C-05.
The memory-layer read path is explicit: memory repos are not expected to provide
a root-level `AGENTS.md`; repo-specific guidance is read from
`system/settings.md`, `system/tools.md`, `system/sources.md`, and optional
`system/coding-guidelines.md`.

### Conventions

The coordinator root is a workspace-wide default layer. It may direct agents to
global settings, tools, sources, companion installed `AGENTS.md` files, and
durable clarification capture, but repository-specific rules belong in the
resolved memory layer. Memory-layer `system/*` files are listed as read-first
surfaces once C-08 identifies the target repository.

### Invariants And Boundaries

The installed coordinator root template must not become a per-repository policy
file, and it must not imply that memory repos need their own root `AGENTS.md`.
Developer clarifications must not be copied into onboarding verbatim; code
reality mismatches are surfaced before propagation. The template also preserves
workflow approval boundaries by forbidding protected branch movement and
worktree lifecycle operations unless the selected workflow has granted the
required approvals.

### Todos

Refresh verification metadata after this coordinator template update is
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
| The installed `AGENTS.md` routing section tells agents when to read sibling `system/`, `tasks/`, and `skills/` instructions. | L28-L42   | [runtime/agents-md-files/coordinator/AGENTS.md](agents-remember-md/runtime/agents-md-files/coordinator/AGENTS.md) |
| The onboarding and developer-clarification sections require `system/AGENTS.md` before trusting onboarding and route important clarifications through C-01/C-05 only after code-reality checks. | L44-L61 | [runtime/agents-md-files/coordinator/AGENTS.md](agents-remember-md/runtime/agents-md-files/coordinator/AGENTS.md) |
| The resolver and memory-layer routing require C-08 before relying on memory/task surfaces and route repository-specific guidance to memory-layer `system/*` files. | L65-L94 | [runtime/agents-md-files/coordinator/AGENTS.md](agents-remember-md/runtime/agents-md-files/coordinator/AGENTS.md) |
| Branch/worktree approval boundaries and memory-layer authority remain listed in the template. | L96-L112   | [runtime/agents-md-files/coordinator/AGENTS.md](agents-remember-md/runtime/agents-md-files/coordinator/AGENTS.md) |

## Cross-Repo References

No sibling repository evidence is needed for this package template.

| Finding                                    | Citations | Source Path |
| ------------------------------------------ | --------- | ----------- |
| No meaningful cross-repo references found. | n/a       | n/a         |

## Update History

- 2026-05-15T15:08+02:00: Added installed `AGENTS.md` routing guidance and developer clarification capture rules that require C-01, developer approval for onboarding documentation, and code-reality checks before C-05 propagation.
- 2026-05-15T04:23+02:00: Removed the optional memory-repo `AGENTS.md` lookup from the coordinator template and documented `system/*` files as the memory guidance surface.
- 2026-05-15T00:38+02:00: Refreshed after the coordinator template became one of four runtime `AGENTS.md` templates and absorbed the checkout task routing plus coordinator and memory-layer guidance. Verification metadata remains pinned to the last committed source until closeout.
- 2026-05-13T19:11: Created onboarding for the coordinator AGENTS.md install template.
