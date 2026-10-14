# AGENTS.md

## Governing Overview

[overview.md](../../../../../../overview.md)

## Purpose

This file is the package-owned template for the installed coordinator root
`AGENTS.md`. It is intended to land at `ar-coordination/AGENTS.md` after the
runtime package is installed.

## Code Commentary

### Logic

The packaged coordinator copy carries the canonical host launcher contract. Free chat answers questions inline. For managed-repository work it creates or resolves the sprint document, writes the developer’s request into it, calls `role_start` once for an Architect without any document reference or brief, and tells the developer where the agent and request are. The developer names the sprint document to the Architect in the dashboard. A different role is started this way only when the developer explicitly names the role and task. A launched role follows its handover; unbound `role_message` remains refused, and a refusal admits no alternative launch route.

The template combines coordinator guidance with role routing: product-started role agents follow their handover; the rest of its opening is for free chat. Managed-source work enters the Architect workflow before code changes, with existing plan and approval boundaries. It points to the sibling installed `system/`, `tasks/` and `skills/` instructions; resolves repository context before trusting memory/tasks; obtains roots/actions through context_packet without a provider argument, reads provider facts from authority settings/provider operations rather than from that packet, and keeps coordinator system/* workspace defaults; captures durable clarifications and verifies code reality before propagating onboarding.
The context retrieval path is routed at the coordinator entrypoint: source work
that relies on onboarding, providers, or repository source goes through
`c-04-retrieval-strategy-router`, which owns Semantics, Relationship, and Intent
routing across optional providers, route indexes, onboarding, and bounded source
confirmation. The generated mirror carries the research-phase naming doctrine: before the build decision, ask `read_ar_files` which cards govern the paths, then read named source/cards/overviews with harness-native tools. The tool carries no document text and has no session front-door or publication continuation. Naming calls remain retrieval evidence; native reads confirm content both before and after the build decision. The authored read doctrine is in `c-04-retrieval-strategy-router` and `l-01-agent-lifecycles`; this template is a synchronized mirror. The memory-layer read path is also explicit: memory repos are not
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
providers, but provider state is not returned by context_packet. The coordinator names `c-04-retrieval-strategy-router` skill as the retrieval strategy owner instead of duplicating
provider, source, and onboarding ordering rules inline. `system/tools.md`
guidance now explicitly includes code quality checks, and the final
code-quality section routes repository-specific validation to the resolved
memory layer.

### Invariants And Boundaries

The installed coordinator root template must not become a per-repository policy
file, and it must not imply that memory repos need their own root `AGENTS.md`.
Developer clarifications must not be copied into onboarding verbatim; code
reality mismatches are surfaced before propagation. Configured provider readiness
is checked from settings/provider operations after context resolution, not from context_packet provider blocks.
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


- The template separates role handovers from free-chat work, which writes sprint prose and starts an Architect through `role_start` without a document reference or brief. [1]

- The installed `AGENTS.md` routing section tells agents when to read sibling `tasks/AGENTS.md` instructions. [2]
- The onboarding section routes context-backed source reading to `c-04-retrieval-strategy-router`, which owns Semantics, Relationship, and Intent routing across providers, route indexes, onboarding, and bounded source confirmation. [3]
- The developer-clarification section routes important clarifications through `c-01-findings-capture` and `c-05-create-or-update-onboarding-files` skill only after code-reality checks. [4]

- The resolver section uses context_packet for roots/actions with no provider argument; provider state comes from settings/provider operations when configured. [5]

- Memory-layer routing sends repository-specific guidance, including code quality checks, to memory-layer `system/*` files after `c-08-ar-coordination-context-resolver` skill resolves `memory_root`. [6]
- The template says not to run Git commands against `ar-coordination/` as a whole; Git belongs to resolved code roots or memory roots that are Git repositories, and task files under `ar-coordination/tasks/` are local coordination artifacts unless a workflow says otherwise. [7]
- Branch/worktree approval boundaries and memory-layer authority remain listed in the template. [8]
- The final code-quality section points agents at resolved memory-layer `system/tools.md` and optional `system/coding-guidelines.md` for repository-specific checks and coding rules. [9]

### Cross-Repo References

No sibling repository evidence is needed for this package template.

No meaningful cross-repo references found.

## Preserved incoming L109 source witness

- Historical incoming L109 source evidence: Current candidate source supports the operative account; historical sections grant no current tool or execution acceptance. [10]
