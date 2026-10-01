# AGENTS.md

## Governing Overview

[overview.md](../../../../../../overview.md)

## Purpose

This file is the package-owned template for the installed coordinator root
`AGENTS.md`. It is intended to land at `ar-coordination/AGENTS.md` after the
runtime package is installed.

## Code Commentary

### Logic

The packaged coordinator copy carries the same sprint-local launcher contract as the canonical
runtime source. For ordinary role-shaped work, free chat resolves the sprint and first leaf, compiles
`templates/architect-brief.md`, and calls `dispatch_agent` once on the sprint document with role
`architect`. It hands over after the exact brief is durably pinned, never calls the internal
session primitive, and never becomes a global architect. The ensuing architect, orchestrator, and
managers use plane-hosted structural authority within that sprint provenance. An explicit
developer-declared task-seat takeover instead targets the named role at its canonical altitude.

The template combines the checkout's lifecycle routing with coordinator
runtime guidance. It now opens with a concise `Start Here — Route By Role`
section: sessions route by role through the `l-01-agent-lifecycles` skill — a
spawned agent (the `AR_SPAWN_ROLE` env var, or a role brief as first message)
follows its brief as its session start, while a developer-facing session is the
free-chat launcher. Research-only asks stay inline; role-shaped work uses the canonical one-call
architect dispatch instead of turning the launcher into a role seat. Caller kind is derived from
process identity, and a plane authorization failure never falls back to ambient. An
already-running session must stay
aware of managed-repo boundaries so a turn or tool target that crosses from
outside Agents Remember scope into a managed repository enters the architect
lifecycle first. The detailed build-mode explanation lives in
the lifecycle skill rather than being repeated in this coordinator entrypoint.
It requires agents to enter the architect lifecycle and clear its plan gate before
changing code, points agents to the sibling installed `system/`, `tasks/`, and
`skills/` `AGENTS.md` files when those scopes become relevant, resolves active
repository context with `c-08-ar-coordination-context-resolver` skill before trusting memory or task surfaces, checks
configured providers through the Agents Remember `context_packet` MCP tool when
the MCP server is configured, and uses coordinator `system/*` files for
workspace-wide defaults. It also routes
important developer clarifications through
`c-01-findings-capture` and requires
verification against code reality before onboarding propagation through `c-05-create-or-update-onboarding-files` skill.
The context retrieval path is routed at the coordinator entrypoint: source work
that relies on onboarding, providers, or repository source goes through
`c-04-retrieval-strategy-router`, which owns Semantics, Relationship, and Intent
routing across optional providers, route indexes, onboarding, and bounded source
confirmation. This generated runtime mirror now also carries the slice-07
**research-phase read** doctrine: until the build decision (the 260703-L10
sweep retired the pre-convergence "build/job" compound), managed-repo
source is read through the `read_ar_files` MCP tool rather than the native read
(it pairs each file with its onboarding by construction and keeps the read trail
observable), `read_ar_files` calls count as retrieval evidence alongside CGC and
GrepAI, and native read is the edit precondition once building begins. (The
authored doctrine lives in `c-04-retrieval-strategy-router` / `l-01-agent-lifecycles`;
this template is the synced mirror of the coordinator-entry pointer.) The memory-layer read path is also explicit: memory repos are not
expected to provide a root-level `AGENTS.md`; repo-specific guidance is read
from `system/settings.md`, `system/tools.md`, `system/git-workflow.md` (when
present, for the gated-branch landing flow read before any commit/push/PR),
`system/sources.md`, and optional `system/coding-guidelines.md`.
Provider authority is stated directly as the MCP settings file.

### Conventions

The coordinator root is a workspace-wide default layer. It may direct agents to
global settings, tools, sources, companion installed `AGENTS.md` files, and
durable clarification capture, but repository-specific rules belong in the
resolved memory layer. Memory-layer `system/*` files are listed as read-first
surfaces once `c-08-ar-coordination-context-resolver` skill identifies the target repository. Provider readiness is
checked only when the MCP server is configured and MCP settings report enabled
providers. The coordinator names `c-04-retrieval-strategy-router` skill as the retrieval strategy owner instead of duplicating
provider, source, and onboarding ordering rules inline. `system/tools.md`
guidance now explicitly includes code quality checks, and the final
code-quality section routes repository-specific validation to the resolved
memory layer.

### Invariants And Boundaries

The installed coordinator root template must not become a per-repository policy
file, and it must not imply that memory repos need their own root `AGENTS.md`.
Developer clarifications must not be copied into onboarding verbatim; code
reality mismatches are surfaced before propagation. Configured provider readiness
is checked after `c-08-ar-coordination-context-resolver` skill through MCP authority.
`c-04-retrieval-strategy-router` skill owns retrieval strategy and source/onboarding confirmation after the
relevant repository context is known. The template
also preserves workflow approval boundaries by forbidding protected branch
movement and worktree lifecycle operations unless the selected workflow has
granted the required approvals. Repository-specific test, lint, typecheck,
build, smoke-check, branch, and local command guidance belongs in the resolved
memory layer's `system/tools.md`; repo-specific coding rules belong in
`system/coding-guidelines.md` when present. The boundary section also states
that `ar-coordination/` is a scaffold/coordination root rather than a Git
repository root: Git operations should target the resolved code repository root
or memory root when those paths are Git repositories, and task files under
`ar-coordination/tasks/` remain local coordination artifacts unless a workflow
explicitly says otherwise.

### Todos

None.

## Evidence

### Docs References

No external documentation is needed for this repository-local template.

No relevant external documentation found.

### Repo-Internal References

This onboarding is backed by the source template itself.

- The template routes spawned agents by their role brief and keeps the developer-facing chat as a free-chat launcher that spawns a settings-profile architect for role-shaped work. [1]
- The installed `AGENTS.md` routing section tells agents when to read sibling `tasks/AGENTS.md` instructions. [2]
- The onboarding section routes context-backed source reading to `c-04-retrieval-strategy-router`, which owns Semantics, Relationship, and Intent routing across providers, route indexes, onboarding, and bounded source confirmation. [3]
- The developer-clarification section routes important clarifications through `c-01-findings-capture` and `c-05-create-or-update-onboarding-files` skill only after code-reality checks. [4]
- The resolver section requires `c-08-ar-coordination-context-resolver` skill before relying on memory/task surfaces, then checks provider readiness through the `context_packet` MCP tool when the MCP server is configured and providers are enabled. [5]
- Memory-layer routing sends repository-specific guidance, including code quality checks, to memory-layer `system/*` files after `c-08-ar-coordination-context-resolver` skill resolves `memory_root`. [6]
- The template says not to run Git commands against `ar-coordination/` as a whole; Git belongs to resolved code roots or memory roots that are Git repositories, and task files under `ar-coordination/tasks/` are local coordination artifacts unless a workflow says otherwise. [7]
- Branch/worktree approval boundaries and memory-layer authority remain listed in the template. [8]
- The final code-quality section points agents at resolved memory-layer `system/tools.md` and optional `system/coding-guidelines.md` for repository-specific checks and coding rules. [9]

### Cross-Repo References

No sibling repository evidence is needed for this package template.

No meaningful cross-repo references found.
