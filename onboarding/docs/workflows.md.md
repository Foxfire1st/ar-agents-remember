# docs/workflows.md

## Governing Overview

[Repository overview](../overview.md)

## Purpose

The workflow page: how a session routes by role, the discipline every build keeps, the three build
modes, and what is worktree-backed. It names modes and owners; the landing flow itself belongs to
the resolved memory's instruction file, which this page points at.

## Code Commentary

The page opens with routing: sessions go through `l-01-agent-lifecycles`, a role agent the product
started follows its handover, and any other session is developer-facing free chat — which answers a
question inline, or for a managed repository creates or resolves the sprint document, writes the
developer's request into it, starts an Architect with `role_start` naming no document, and tells the
developer where the work sits. It states the architect's phase axis (request, trust-checkpoint,
reframe-research, decide, build, close) and says the job type is a lens during reframe-research
rather than a gate, so the only task-format decision is the build-mode step. [1]

Shared Discipline lists the five rules every build keeps: resolve the active context, run drift
detection before planning against onboarding, wait for the developer's approval before
implementation, update onboarding live per completed plan section, and run the checks the resolved
memory's `system/tools.md` lists. [2]

At `decide` the architect picks one of three modes. A research-only exit answers and changes no
code — no worktree, no task file, no closeout. A durable task takes the minimal
`w-02-light-task-workflow` artifact under `ar-coordination/tasks/<repo>/<task-slug>/task.md`, whose
checklist is the live execution state. Work that outgrows one page escalates to a master plus flat,
numbered sub-task series: one wrapper folder, one master task file, one shared worktree, a commit
per slice and a single release at the end. [3]

Worktree-backed tasks follow the ladder task doc (approved) → branch (intent) → worktree (only what
is built), with a `contract.md` beside the task file, and a series runs in one shared worktree for
the whole series. Closeout and commit approval are separate from implementation approval, and the
landing flow — direct or pull-request gated — is deferred to the repository's
`system/task-publication.md` when present, together with the `landing.workflow` setting that decides
which of the two the repository runs. [4]

The page closes with a table mapping five situations to a build mode. [5]

## Evidence

### Repo-Internal References

- The source describes the routing paragraph as summarized above. [1]
- The source lists the five shared-discipline rules. [2]
- The source names the three build modes and what each produces. [3]
- The source states the worktree ladder and defers landing to `system/task-publication.md` with the `landing.workflow` setting. [4]
- The source's closing table maps situations to build modes. [5]
