# core/invariants.md

## Governing Overview

[MCP package overview](../../../../../../../overview.md)

## Purpose

The shared **invariants** block: the facts every role can count on, authored once so a role file
names the invariant it depends on instead of restating the set.

## Code Commentary

### Logic

`## Continuity lives in durable state, never in transcripts` states why short-lived workers and reviewers
are safe and why **every seat writes its artifact of record** — a finding held only in a chat is a bug.
`## The decision surface` routes decision-needing questions to the task doc's `openQuestions` with the
analysis in `notes/`, and keeps backend seats behind the architect relay.

`## Sequencing is decided by the dependency graph, not by habit` sets parallel-by-default up to the
`orchestration.concurrency` cap, requires a named gate / one-writer dependency / explicit ruling for any
sequential exception, and states that build concurrency never grants landing order. `## Observability`
keeps coordination seats as `task_doc` leaves with attached chats. `## The spine: task doc → branch →
worktree` fixes what creates a branch or worktree, that design and portfolio work never touch git, and
that chat is never a build route.

`## Default behavior, and where it is overridden` states the fill-small-blanks default, the one-rung
escalation for a plan delta beyond blank-filling, and that the **spirit test is orchestrator-only**.
`## Knob resolution and capability doctrine` fixes the resolution order (role-file defaults < global
settings < repo-local settings), which rows are settings keys, the deliberate absence of per-harness role
files, and `role_start` as the harness-independent role-agent fan-out. Current launch rows are harness, model, effort, serviceTier, mode and featureValues; the retained launchArgs/sessionCommands/promptKeywords keys load but are no longer read. `## Instruction-surface boundaries`
assigns task-collaboration doctrine to `tasks/AGENTS.md`, the task format to
`w-02-light-task-workflow`, repository specifics to the memory layer, and the corpus's own division of
labour to `roles/` / `operations/` / `reference/`.

### Conventions

Keep each invariant to the statement and its consequence; long rationale belongs in
`reference/rationale.md`.

### Invariants And Boundaries

- Continuity lives in the task tree plus written artifacts, never in a transcript.
- Sequential execution is the exception and must name its reason.
- Only the launch-setting rows are settings keys; `dispatch` and `tools` are structural descriptions.
- There are deliberately no per-harness role files.
- The retained corpus describes core/role/operation inheritance, but native role launch selects its role and operation without injecting this shared core; source doctrine is not evidence of delivered capsule contents.

### Todos

None recorded.

## Evidence

### Docs References

No external or domain documentation governs this repository-local instruction file; it is canonical
repository prose consumed by the skill router.

No relevant documentation found after checking live sources.

### Repo-Internal References

- Task intent creates its branch and build worktree; design and chat are not build routes. \[1] [1]

- Launch settings own current knob rows; removed launchArgs/sessionCommands/promptKeywords load but are unused. \[2] [2]

- Task collaboration, format, memory-specific commands and role/operation duties have separate instruction owners. \[3] [3]

- Core inheritance is retained corpus doctrine and does not prove current native capsule contents. \[4] [4]

### Cross-Repo References

No sibling-repository contract defines this instruction file.

No meaningful cross-repo references found.
