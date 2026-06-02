# AGENTS.md

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember-md                         |
| path                   | `AGENTS.md`                                |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-06-01T11:18+02:00                     |
| lastVerifiedCommitHash | `53b17f574a53ae400f8abb9fda264fa9fa3e8dff` |
| lastVerifiedCommitDate | 2026-06-02T16:24:22+02:00|

## Purpose

`AGENTS.md` is the repo-root operating contract for agents working on the
`agents-remember-md` source checkout. It now explicitly distinguishes this
source package from the installed coordination runtime and tells agents who
arrive through a workspace-level pointer to follow the installed
`ar-coordination/AGENTS.md` instead when they are working on a sibling
repository.

## Code Commentary

### Logic

The file starts by declaring that `agents-remember-md` is source package code,
not the live runtime after installation. It gives a fallback handoff for the
case where a workspace root includes this file while the actual target is a
sibling repository, then scopes normal resolver input for this checkout to
`code_repository_name = agents-remember-md`.

A `Start Here — Enter the Job Lifecycle` section now sits where Task Format
Routing used to: every session enters `l-01-session-job-lifecycle` (orient →
ground → frame → decide → build → close), the job type is a lens, and the only
task-format decision is `l-01-session-job-lifecycle` skill's build-mode step — read-only exit, chat build
(worktree, no task file), or a durable `w-02-light-task-workflow` skill task. Framing is subsumed into
`l-01-session-job-lifecycle` skill's `frame` phase, where the `tasks/AGENTS.md` collaboration doctrine applies.
The memory section also carries a `Memory Retrieval Strategies` list — Semantics
(GrepAI), Relationship (cgc), and Intent (onboarding plus bounded source
confirmation) — that points to the same `c-04-retrieval-strategy-router` skill router.

The build-mode decision is the only task-format call, and the former standalone
chat workflow is retired — its role is absorbed into the `l-01-session-job-lifecycle` skill's chat build. The memory section
keeps the `c-08-ar-coordination-context-resolver` skill, `context_packet` MCP tool, then `c-02-memory-quality-control` skill memory quality control gate and
points agents at the resolved memory layer's settings, tools, sources, and
optional coding guidelines rather than pretending the source checkout has active
root-level `system/` settings. Provider authority is stated directly as MCP
settings.

The source-layout section records the current package structure: MCP server and
package services, runtime `AGENTS.md` templates, runtime skills, runtime system
defaults, README, and roadmap. The boundaries section keeps root instructions
scoped to source-checkout work and keeps installed coordinator instructions
under `runtime/agents-md-files/`. The final code-quality section tells agents
working in this source checkout to run Ruff, Pyright, and Radon after Python
code changes, then routes exact command details and broader validation guidance to the
resolved memory layer's `system/tools.md` and optional
`system/coding-guidelines.md`.

### Conventions

Workflow names remain stable contracts. C-* skills are core support skills, and
W-* skills are task workflows. Active runtime and memory settings are always
resolved through `c-08-ar-coordination-context-resolver` skill; provider readiness is checked through MCP when that
server and providers are configured; source templates and example defaults are
not treated as the user's live runtime configuration.

### Invariants And Boundaries

This file should not be used as the installed coordinator entrypoint. Installed
coordinator instructions belong in `runtime/agents-md-files/` as package-owned
templates and in the live `ar-coordination/` tree after runtime installation.
User-specific behavior and repo policy belong in the resolved memory layer.
Worktree, closeout, integration, push, cleanup, and protected-branch movement
remain approval-gated. Implementation approval and commit approval are separate
gates; agents must stop after checks or closeout dry-runs until the developer
explicitly approves real commits or lifecycle mutations. The workflow-before-code
warning now says this explicitly: do not randomly commit — use the `c-12-closeout` skill closeout
procedure (`direct_closeout_preview`/`apply`) instead.

### Todos

Refresh verification metadata after this `AGENTS.md` source update is committed.

### Docs References

No external domain documentation is needed to prove this repository-local agent
contract.

| Finding                                                                                           | Citations | Source Path |
| ------------------------------------------------------------------------------------------------- | --------- | ----------- |
| No relevant external documentation found; same-repository workflow files are the direct evidence. | n/a       | n/a         |

## Repo-Internal References

The active repo behavior depends on the source-checkout scope, installed-runtime
handoff, workflow routing, resolver gate, and source-layout boundaries in this
file.

| Finding                                                                                                                                        | Citations | Source Path                               |
| ---------------------------------------------------------------------------------------------------------------------------------------------- | --------- | ----------------------------------------- |
| The file identifies `agents-remember-md` as the source package and points sibling-repo work to the installed `ar-coordination/AGENTS.md`.       | L1-L14    | [AGENTS.md](agents-remember-md/AGENTS.md) |
| The repo routes every session into the `l-01-session-job-lifecycle`; the only task-format call is `l-01-session-job-lifecycle` skill's build-mode step (read-only exit / chat build / durable `w-02-light-task-workflow` skill), and the standalone chat workflow is retired. | L16-L34 | [AGENTS.md](agents-remember-md/AGENTS.md) |
| Memory rules require `c-08-ar-coordination-context-resolver` skill, then a configured-provider readiness check, then `c-02-memory-quality-control` skill memory quality control, and route agents to the resolved memory layer, including `system/tools.md` for repo-specific code quality checks, instead of a root-level source checkout `system/` folder. | L28-L62 | [AGENTS.md](agents-remember-md/AGENTS.md) |
| Boundaries state that implementation approval is not commit approval; agents must stop after checks or closeout dry-runs before real commits, closeout apply, integration, push, or cleanup. | L84-L91 | [AGENTS.md](agents-remember-md/AGENTS.md) |
| Source-layout and boundary notes separate MCP/runtime package assets from user-owned memory and installed coordinator configuration.            | L66-L86   | [AGENTS.md](agents-remember-md/AGENTS.md) |
| Code-quality routing tells agents to run Ruff, Pyright, and Radon after Python code changes in this source checkout and sends exact command details plus coding rules to the resolved memory layer's `system/tools.md` and optional `system/coding-guidelines.md`. | L90-L95 | [AGENTS.md](agents-remember-md/AGENTS.md) |

## Cross-Repo References

The workspace root may include this file as a pointer, but this file now
delegates sibling-repository work to the installed runtime instructions.

| Finding                                                                                                   | Citations | Source Path |
| --------------------------------------------------------------------------------------------------------- | --------- | ----------- |
| No sibling repository citation is required; the cross-repo behavior is a handoff instruction in this file. | n/a       | n/a         |

## Update History

- 2026-06-02T03:45+02:00: Rewired the root checkout contract to route every session into `l-01-session-job-lifecycle`: replaced Task Format Routing and the separate `Frame Before You Choose a Format` section with a `Start Here — Enter the Job Lifecycle` section whose only task-format call is L-01's build-mode step (read-only exit / chat build / durable W-02); the standalone W-03 chat workflow is retired and absorbed into L-01's chat build. Part of the L-01 lifecycle reshape (mcp 1.1.0). Verification metadata re-verified at closeout.
- 2026-06-01T11:18+02:00: Documented the new `Frame Before You Choose a Format` section ahead of Task Format Routing (the `tasks/AGENTS.md` collaboration doctrine applies up front and routes evidence to `c-04-retrieval-strategy-router` skill) and the added `Memory Retrieval Strategies` list pointing to `c-04-retrieval-strategy-router` skill. Verification metadata stays pinned; Repo-Internal Reference line ranges will be re-verified at closeout.
- 2026-05-29T20:25+02:00: Updated after the workflow-before-code warning was made explicit ("do not randomly commit; use the `c-12-closeout` skill closeout procedure").
- 2026-05-28T19:52+02:00: Updated after source-checkout code quality guidance added Pyright beside Ruff and Radon.
- 2026-05-24T04:34+02:00: Updated after source-checkout instructions renamed `c-02-memory-quality-control` skill to memory quality control and made commit approval separate from implementation approval.
- 2026-05-23T21:31+02:00: Made source-checkout code quality guidance explicit about Ruff and Radon after Python implementation work.
- 2026-05-23T21:25+02:00: Simplified provider-authority wording and added source-checkout code-quality routing to resolved memory-layer tools and coding guidelines.
- 2026-05-23T14:20+02:00: Updated source-layout onboarding after `installer/` and `runtime/scripts/` were removed from the source package.
- 2026-05-23T13:46+02:00: Updated provider readiness guidance to use `context_packet` MCP tool instead of deleted source lifecycle scripts or coordinator `system/settings.json`.
- 2026-05-21T04:09+02:00: Added the configured-provider readiness check after `c-08-ar-coordination-context-resolver` skill and before `c-02-memory-quality-control` skill for source-checkout work.
- 2026-05-15T04:12+02:00: Reframed the root `AGENTS.md` onboarding around the source checkout contract and the installed-runtime handoff.
- 2026-05-15T00:38+02:00: Refreshed after coordinator and memory-layer settings guidance was folded into the repo-root contract during the `AGENTS.md` template reshuffle. Verification metadata remains pinned to the last committed source until closeout.
- 2026-05-12T18:51+02:00: Refreshed after AGENTS.md emphasized the workflow-before-code warning and separated it from the memory section.
- 2026-05-12T11:30: Updated after AGENTS.md was shortened to the three workflow formats, workflow-before-code rule, and `c-08-ar-coordination-context-resolver` skill resolver contract.
- 2026-05-11T19:52: Corrected escaped workflow wildcard wording introduced during the verification refresh.
- 2026-05-11T19:42: Refreshed verification metadata against commit `aa85d3862bf21fed791e3170e6957f9288c319e8` after coordination rename verification.
- 2026-05-11T18:34: Updated after the memory system rules switched fallback resolver language to `code_repository_name` and `code_repository_root`.
- 2026-05-10T03:01: Updated after chat-mode closeout guidance routed approved micro edits through `c-09-git-worktree-manager` skill `direct-closeout`.
- 2026-05-09T22:57: Refreshed against commit `bb95b99` and tightened references around the six-gate onboarding workflow.
- 2026-05-09T21:59: Updated for split memory/coordination terminology and `c-09-git-worktree-manager` skill worktree context.
- 2026-05-09T21:15: Created first file-level onboarding baseline for the agent operating contract.
