# operations/bootstrap.md

## Governing Overview

[MCP package overview](../../../../../../../overview.md)

## Purpose

The instruction for the session-bootstrap operation: the new user's first hour around the memory repository —
what Agents Remember is, the developer-only decisions, the user settings, memory-root initialization, what the
memory root already carries, the first attributed baseline, result verification, and the handover that names the
Architect as the next step. First onboarding and the knowledge foundation are that Architect's regular work, not
stages of this operation.

## Current Contract

**When it is selected.** A repository has no working memory root yet, or has one that does not resolve: no memory
root, a memory root with no baseline, the removed repo-local layout, a coordination root that will not resolve, or
providers configured but not indexing. With an attributed baseline and resolving context, ordinary work belongs to
the lifecycle roles, and this operation is never re-entered to maintain or tidy a working installation. A resolving
repository without a recorded knowledge foundation uses step 8 instead of re-entry.

**How the carrier is started.** As a free agent, not a task seat, with no task document and no brief. The absence
of a task document is the shape of the operation, not a repairable error, and `bootstrap` is its only carrier: a
seat already in a sprint, master or leaf resolves its own context through `c-08-ar-coordination-context-resolver`
and, if setup is genuinely missing, says so and stops.

**Required inputs.** Workspace facts rather than task facts: the code repository the developer means and its
absolute root; the resolved `coordinationRoot` and `workspaceRoot` from `server_info` on the `agents-remember-task`
server; whether a memory root already resolves and in what state; and the developer's own decisions — which branch
is the foundation (the spear), whether they are scaffolding a new memory repo or pointing at an existing one, and
whether providers index now or are deferred.

**The workflow, each step on its owning surface.** Say what Agents Remember is and what setup will change; establish
the resolved context or name the missing fact; take the spear-branch decision and record it as the memory repo's
initial branch name; write the user's settings once through `user_settings_init`, previewing with `dry_run=true` and
reading the state back; initialize or repair the memory root through `memory_init`, also previewed; read what the
baseline will carry and author none of it; adopt the first attributed baseline through `memory_baseline_adopt` with
`memory_baseline_status` read before and after and the drift decision put to the developer; report the knowledge
foundation's state and hand its making to the Architect; and configure indexing or say plainly that it is deferred.

**One harness per role, chosen once.** Ask which harness each role should use, offering only the harnesses the host
runs, and let one harness serve every role if that is the answer — at least one is required. Model, effort and the
rest stay unset on purpose, so a role whose settings name only a harness starts on that harness's own defaults. An
existing settings file that holds its own choices is read and reported, never overwritten, merged or completed: a
harness-only file is a valid start, so an existing file is not a gap. A refused write is reported with its path and
reason, and this seat changes no mode.

**Handoff.** The operation ends when the surfaces establish the resolved roots, the foundation branch, the user
settings path and what initialization did, the baseline's existence and commit, whether onboarding exists (read,
never authored here), the knowledge foundation's recorded identity or the named state that says it is not, providers
indexing or deferred, and every skipped step's reason. The one next step it names is the Architect, which organises
memory and knowledge bootstrapping as a regular task, master or sprint through `c-14`'s Curator route.

## Conventions

Each step names its owning surface and its `c-*` procedure — `c-00-initialize-memory-repo` for the memory root,
`c-10-adopt-memory-baseline` for the baseline, `c-14-knowledge-bootstrap` for the foundation — and points at it
rather than restating its procedure. The tools named are called on the `agents-remember-task` tool server. The two
detail references, the foundation handover and the failure states, are read when their step is reached, not before.

## Invariants And Boundaries

- The carrier has no task document, no worktree, no gate and no task altitude, and that is its shape rather than a
  gap: it creates none, dispatches nothing, and does not acquire authority by having set the workspace up.
- It never commits code, lands, pushes, runs closeout or integration. The memory content commit that adoption
  performs is the setup surface's own designed effect.
- It writes to the memory layer only through the setup surfaces and their `c-*` procedures: no onboarding of its
  own, no refresh of existing onboarding, no citation fixer, and no memory edit made to pass a check.
- It does not author the knowledge foundation; it reads and reports that foundation's state and hands the authoring
  on, never running the knowledge writer, inventing invariants or populating a database.
- It asks before anything irreversible, and it reports rather than repairs a removed `ar-memory/` layout.

## Code Commentary

### Logic

Conformance is evidenced by the reader's ability to re-derive every report claim from its named surface without
asking the agent: the surface, the exact arguments and the result that was read back. This agent has no independent
acceptor — no task document, no gate, no reviewer in its loop — so its report is completion truth about itself and
never an acceptance, and is stated as such. Every effectful step is previewed with `dry_run=true` and followed by a
call that states the resulting state; a step applied but never read back is not complete. A failure is reported as
a failure, with the real output in the report's own "Steps Skipped Or Failed" section.

### Invariants And Boundaries

A developer who will not answer a decision is a stop, not a guess: without a foundation branch setup cannot pass
step 3; an unanswered memory-repo question is resolved from `context_packet` and reported; an unanswered indexing
question defers providers, which is always available and never a failure; an unnamed repository stops the
operation, because there is no default repository. A failed step is reported with the server's own refusal, is not
retried under a different flag, and is never described as the intended outcome. A capability that does not exist is
named as absent, stating which half of a route is unexercised — the instruction channel's own case is wired end to
end and covered by `mcp/tests/test_capsule_launch_wiring.py`, whose free-agent case reads the compiled capsule out
of the session's first prompt, while a launch that cannot compile a capsule refuses by name. A contradiction
between this instruction and the system being set up is reported as a finding about the instruction.

## Evidence

- The operation's coverage, selection conditions, free-agent carrier and the removal of any task document.
- The three developer decisions, the required workspace inputs, and the step that owns each setup surface.
- The one harness-per-role settings write, its preview and read-back, and the existing file left untouched.
- The authority gates that keep this seat out of tasks, commits, onboarding and knowledge authoring.
- The evidence standard (re-derivable claims, preview and read-back, failures reported as failures) and the
  handoff that names the Architect as the one next step.
