# AGENTS.md

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember                         |
| path                   | `AGENTS.md`                                |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-07-09T10:40+02:00 |
| lastVerifiedCommitHash | `e400ed0ce98752d1b65d00de97c9b84c7ea20814` |
| lastVerifiedCommitDate | 2026-07-10T20:04:45+02:00|

## Purpose

`AGENTS.md` is the repo-root operating contract for agents working on the
`agents-remember` source checkout. It now explicitly distinguishes this
source package from the installed coordination runtime and tells agents who
arrive through a workspace-level pointer to follow the installed
`ar-coordination/AGENTS.md` instead when they are working on a sibling
repository. It also points store, queue, append-only-log, and loop-over-store
changes at the resolved memory layer's stability/reclamation coding doctrine
before implementation.

## Code Commentary

### Logic

The file starts by declaring that `agents-remember` is source package code,
not the live runtime after installation. It gives a fallback handoff for the
case where a workspace root includes this file while the actual target is a
sibling repository, then scopes normal resolver input for this checkout to
`code_repository_name = agents-remember`.

A `Start Here — Route By Role` section now sits where Task Format Routing used
to: sessions route by role through the `l-01-agent-lifecycles` skill — a spawned
agent (the `AR_SPAWN_ROLE` env var, or a role brief as first message) follows
its brief as its session start, and a developer-facing session is the
**architect**, running `skills/l-01-agent-lifecycles/roles/architect.md`
on the request → trust-checkpoint → reframe-research → decide → build → close
phase axis. The job type is a lens during reframe-research, and the build
decision at `decide` has two shapes — a research-only exit (no worktree, no task
file) or a durable `w-02-light-task-workflow` skill task; chat is never a build
route, so small code work takes the minimal artifact and larger work escalates
to a master + light sub-task series. The `tasks/AGENTS.md` collaboration
doctrine applies in the architect lifecycle's reframe-research phase.
The HFX-L6 role split keeps spawned roles on their briefs while making the
owner/developer-facing seat the architect; the backend orchestrator is no
longer the normal developer-facing lifecycle.
The memory section also carries a `Memory Retrieval Strategies` list — Semantics
(GrepAI), Relationship (cgc), and Intent (onboarding plus bounded source
confirmation) — that points to the same `c-04-retrieval-strategy-router` skill router.

The build-mode decision is the only task-format call; the former standalone
chat workflow is retired, and the chat build itself is retired with the
lifecycle convergence — every code change lives under an approved task
document. The memory section
keeps the `c-08-ar-coordination-context-resolver` skill, `context_packet` MCP tool, then `c-02-memory-quality-control` skill memory quality control gate and
points agents at the resolved memory layer's settings, tools, sources, and
optional coding guidelines rather than pretending the source checkout has active
root-level `system/` settings. Provider authority is stated directly as MCP
settings.

The source-layout section now records root `skills/` as the canonical skill
source tree and `scripts/sync-skills.py` as the repo helper that copies canonical
skills into the MCP package-data tree and every harness starter package. It also
records root `agents-md-files/`, `benchmarks/`, `providers/`, and `system/` as
canonical runtime asset folders and routes their MCP package-data refresh
through `scripts/sync-runtime.py`. The MCP package-data skill and runtime asset
trees are explicitly generated, so agents should edit root canonical folders
first and run the relevant sync helper instead of editing package copies by
hand. The boundaries section keeps root instructions scoped to source-checkout
work, keeps installed coordinator instructions under `runtime/agents-md-files/`,
repeats the "edit root skills, then sync" rule, and adds the matching
runtime-asset sync boundary. The final code-quality section tells agents working
in this source checkout to run Ruff, Pyright, and Radon after Python code
changes, then routes exact command details and broader validation guidance to
the resolved memory layer's `system/tools.md` and optional
`system/coding-guidelines.md`. HFX2-L8 adds a stability/reclamation
cross-reference there: before adding or editing any store, loop-over-a-store,
queue, or append-only log, agents must read the memory layer's
`system/coding-guidelines.md` "Stability, Bounded Resources, and Reclamation"
section. This is a doctrine read requirement, not a new gate or runtime
behavior.

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
| The file identifies `agents-remember` as the source package and points sibling-repo work to the installed `ar-coordination/AGENTS.md`.       | L1-L14    | [AGENTS.md](agents-remember/AGENTS.md) |
| The repo routes sessions by role through the `l-01-agent-lifecycles` skill: spawned agents follow their briefs, a developer session runs the architect lifecycle, and the build decision at `decide` is a research-only exit or a durable `w-02-light-task-workflow` skill task (chat is never a build route); the standalone chat workflow and the chat build are retired. | L16-L40 | [AGENTS.md](agents-remember/AGENTS.md) |
| Memory rules require `c-08-ar-coordination-context-resolver` skill, then a configured-provider readiness check, then `c-02-memory-quality-control` skill memory quality control, and route agents to the resolved memory layer, including `system/tools.md` for repo-specific code quality checks, instead of a root-level source checkout `system/` folder. | L51-L89 | [AGENTS.md](agents-remember/AGENTS.md) |
| Boundaries state that implementation approval is not commit approval; agents must stop after checks or closeout dry-runs before real commits, closeout apply, integration, push, or cleanup. | L122-L137 | [AGENTS.md](agents-remember/AGENTS.md) |
| Source-layout and boundary notes make root `skills/` canonical, identify `scripts/sync-skills.py` as the helper that refreshes generated MCP/harness skill copies, and keep installed coordinator instructions separate from user-owned memory and runtime configuration. | L101-L127; L124-L131 | [AGENTS.md](agents-remember/AGENTS.md) |
| Source-layout and boundary notes make root `agents-md-files/`, `benchmarks/`, `providers/`, and `system/` canonical runtime asset folders, identify `scripts/sync-runtime.py` as the helper that refreshes generated MCP package-data copies, and tell agents not to edit generated runtime asset copies directly. | L106-L118; L128-L129 | [AGENTS.md](agents-remember/AGENTS.md) |
| Code-quality routing tells agents to run Ruff, Pyright, and Radon after Python code changes in this source checkout, sends exact command details plus coding rules to the resolved memory layer's `system/tools.md` and optional `system/coding-guidelines.md`, and requires the Stability/Reclamation doctrine before store, loop-over-store, queue, or append-only-log changes. | L139-L150 | [AGENTS.md](agents-remember/AGENTS.md) |

## Cross-Repo References

The workspace root may include this file as a pointer, but this file now
delegates sibling-repository work to the installed runtime instructions.

| Finding                                                                                                   | Citations | Source Path |
| --------------------------------------------------------------------------------------------------------- | --------- | ----------- |
| No sibling repository citation is required; the cross-repo behavior is a handoff instruction in this file. | n/a       | n/a         |

## Update History

- 2026-07-09T10:40+02:00 — 260707-HFX2-L8 stability/reclamation doctrine: documented the new
  Code Quality Instructions MUST-READ sentence that points store, loop-over-store, queue, and
  append-only-log changes at the resolved memory layer's "Stability, Bounded Resources, and
  Reclamation" doctrine. Verification metadata pinned until closeout stamps the HFX2-L8 commit.

- 2026-07-07T21:00+02:00 — 260707-HFX-L6 architect/orchestrator split: the repo-root
  session-start contract now routes developer-facing sessions to the architect lifecycle
  (`roles/architect.md`) and points the plan gate at the architect, while spawned role
  sessions still follow their briefs. Verification metadata pinned until closeout stamps
  the HFX-L6 commit.

- 2026-07-06T12:05+02:00 — 260703-L10 (one-vocabulary sweep): the `Start Here` section became `Route By Role` — sessions route through the unified `l-01-agent-lifecycles` skill (spawned agents follow briefs; a developer session is the orchestrator on the request → trust-checkpoint → reframe-research → decide → build → close axis), the dead `orient → ground → frame → decide` axis and the retired skill name are gone, the chat build is removed from the build modes (chat is never a build route; research-only exit or `w-02-light-task-workflow` task), and the IMPORTANT block names the orchestrator lifecycle's plan gate. Verification metadata pinned until closeout stamps the L10 commit.
- 2026-06-11T14:07+02:00: No content impact: re-verified against merged main `c2c2dcb` after the upstream doc-link/typo merges (PRs #69-#73) and the repository rename from `agents-remember-md` to `agents-remember`; card content already matched the source.
- 2026-06-08T11:53+02:00: Updated source-layout onboarding for canonical root runtime asset folders (`agents-md-files/`, `benchmarks/`, `providers/`, `system/`) and `scripts/sync-runtime.py`, including the generated package-data boundary. Verification metadata stays pinned until closeout commits the source change.
- 2026-06-03T18:58+02:00: Updated source-layout onboarding for the root-level canonical `skills/` tree and `scripts/sync-skills.py` sync helper. Verification metadata stays pinned until closeout commits the source change.
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
