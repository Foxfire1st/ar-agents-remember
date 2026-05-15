# AGENTS.md

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember-md                         |
| path                   | `AGENTS.md`                                |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-05-15T04:12+02:00                     |
| lastVerifiedCommitHash | `e402e1446050a7d61f448f816395b911417a5a50` |
| lastVerifiedCommitDate | 2026-05-15T04:31:07+02:00|

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

The task-routing section keeps the three workflow choices: default chat mode
for small current-session edits, W-02 for durable task-file work, and W-01 only
when the developer explicitly requests the heavy workflow. The memory section
keeps the C-08 then C-02 gate and points agents at the resolved memory layer's
settings, tools, sources, and optional coding guidelines rather than pretending
the source checkout has active root-level `system/` settings.

The source-layout section records the current package structure: installer,
runtime `AGENTS.md` templates, runtime skills, runtime scripts, runtime system
defaults, README, and roadmap. The boundaries section keeps root instructions
scoped to source-checkout work and keeps installed coordinator instructions
under `runtime/agents-md-files/`.

### Conventions

Workflow names remain stable contracts. C-* skills are core support skills, and
W-* skills are task workflows. Active runtime and memory settings are always
resolved through C-08; source templates and example defaults are not treated as
the user's live runtime configuration.

### Invariants And Boundaries

This file should not be used as the installed coordinator entrypoint. Installed
coordinator instructions belong in `runtime/agents-md-files/` as package-owned
templates and in the live `ar-coordination/` tree after runtime installation.
User-specific behavior and repo policy belong in the resolved memory layer.
Worktree, closeout, integration, push, cleanup, and protected-branch movement
remain approval-gated.

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
| Task format routing keeps chat, W-02, and W-01 as the only work formats before changing code or docs.                                          | L16-L27   | [AGENTS.md](agents-remember-md/AGENTS.md) |
| Memory rules require C-08, then C-02, and route agents to the resolved memory layer instead of a root-level source checkout `system/` folder.   | L28-L53   | [AGENTS.md](agents-remember-md/AGENTS.md) |
| Source-layout and boundary notes separate installer/runtime package assets from user-owned memory and installed coordinator configuration.      | L55-L75   | [AGENTS.md](agents-remember-md/AGENTS.md) |

## Cross-Repo References

The workspace root may include this file as a pointer, but this file now
delegates sibling-repository work to the installed runtime instructions.

| Finding                                                                                                   | Citations | Source Path |
| --------------------------------------------------------------------------------------------------------- | --------- | ----------- |
| No sibling repository citation is required; the cross-repo behavior is a handoff instruction in this file. | n/a       | n/a         |

## Update History

- 2026-05-15T04:12+02:00: Reframed the root `AGENTS.md` onboarding around the source checkout contract and the installed-runtime handoff.
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
