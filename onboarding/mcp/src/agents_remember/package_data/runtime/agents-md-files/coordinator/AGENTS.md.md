# AGENTS.md

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember                         |
| path                   | `mcp/src/agents_remember/package_data/runtime/agents-md-files/coordinator/AGENTS.md` |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-07-10T02:39+02:00                     |
| lastVerifiedCommitHash | `5aff1e8f01dfa949efc8f68e46bc62a99ed31432` |
| lastVerifiedCommitDate | 2026-08-14T14:36:50+02:00|
| governingOverview      | `../../../../../../overview.md`                              |

## Governing Overview

[overview.md](../../../../../../overview.md)

## Purpose

This file is the package-owned template for the installed coordinator root
`AGENTS.md`. It is intended to land at `ar-coordination/AGENTS.md` after the
runtime package is installed.

## Code Commentary

### Logic

The packaged coordinator copy now carries the same sprint-local launcher contract as the canonical
runtime source. A free chat launches one architect bound to a qualified sprint; the ensuing
orchestrator and managers inherit that sprint provenance. It no longer instructs installations to
treat a single architect identity as global across all running sprints.

The template combines the checkout's lifecycle routing with coordinator
runtime guidance. It now opens with a concise `Start Here — Route By Role`
section: sessions route by role through the `l-01-agent-lifecycles` skill — a
spawned agent (the `AR_SPAWN_ROLE` env var, or a role brief as first message)
follows its brief as its session start, while a developer-facing session is the
free-chat launcher. Research-only asks stay inline; role-shaped work spawns a clean architect
session with the settings-owned profile instead of turning the launcher into a role seat. An
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

## Docs References

No external documentation is needed for this repository-local template.

| Finding | Anchor | Source |
| --- | --- | --- |
| No relevant external documentation found. | — | — |

## Repo-Internal References

This onboarding is backed by the source template itself.

| Finding | Anchor | Source |
| --- | --- | --- |
| The template routes spawned agents by their role brief and keeps the developer-facing chat as a free-chat launcher that spawns a settings-profile architect for role-shaped work. | `## Start Here — Route By Role` | mcp/src/agents_remember/package_data/runtime/agents-md-files/coordinator/AGENTS.md:3-12 |
| The installed `AGENTS.md` routing section tells agents when to read sibling `tasks/AGENTS.md` instructions. | `### Installed AGENTS.md Routing` | mcp/src/agents_remember/package_data/runtime/agents-md-files/coordinator/AGENTS.md:34-41 |
| The onboarding section routes context-backed source reading to `c-04-retrieval-strategy-router`, which owns Semantics, Relationship, and Intent routing across providers, route indexes, onboarding, and bounded source confirmation. | `### Onboarding Documentation`, `c-04-retrieval-strategy-router` | mcp/src/agents_remember/package_data/runtime/agents-md-files/coordinator/AGENTS.md:42-54 |
| The developer-clarification section routes important clarifications through `c-01-findings-capture` and `c-05-create-or-update-onboarding-files` skill only after code-reality checks. | `### Developer Clarifications`, `c-01-findings-capture`, `c-05-create-or-update-onboarding-files` | mcp/src/agents_remember/package_data/runtime/agents-md-files/coordinator/AGENTS.md:55-68 |
| The resolver section requires `c-08-ar-coordination-context-resolver` skill before relying on memory/task surfaces, then checks provider readiness through the `context_packet` MCP tool when the MCP server is configured and providers are enabled. | `## Ar-coordination & Memory Layer Resolver` | mcp/src/agents_remember/package_data/runtime/agents-md-files/coordinator/AGENTS.md:69-83 |
| Memory-layer routing sends repository-specific guidance, including code quality checks, to memory-layer `system/*` files after `c-08-ar-coordination-context-resolver` skill resolves `memory_root`. | `### Memory Repo User Settings, Instructions, and Guidelines` | mcp/src/agents_remember/package_data/runtime/agents-md-files/coordinator/AGENTS.md:114-126 |
| The template says not to run Git commands against `ar-coordination/` as a whole; Git belongs to resolved code roots or memory roots that are Git repositories, and task files under `ar-coordination/tasks/` are local coordination artifacts unless a workflow says otherwise. | `### Boundaries` | mcp/src/agents_remember/package_data/runtime/agents-md-files/coordinator/AGENTS.md:152-162 |
| Branch/worktree approval boundaries and memory-layer authority remain listed in the template. | `### Boundaries` | mcp/src/agents_remember/package_data/runtime/agents-md-files/coordinator/AGENTS.md:147-162 |
| The final code-quality section points agents at resolved memory-layer `system/tools.md` and optional `system/coding-guidelines.md` for repository-specific checks and coding rules. | `## Code Quality Instructions` | mcp/src/agents_remember/package_data/runtime/agents-md-files/coordinator/AGENTS.md:163-170 |

## Cross-Repo References

No sibling repository evidence is needed for this package template.

| Finding | Anchor | Source |
| --- | --- | --- |
| No meaningful cross-repo references found. | — | — |

## Update History

- 2026-08-10T04:39+02:00 — 260713-TES-L6: synchronized the packaged coordinator onboarding with
  the sprint-qualified free-chat launcher contract. Verification metadata remains pinned until
  closeout stamps the code commit.

- 2026-08-03T04:32:19+02:00 — W3-B08 curator: curated 16 citations (citation_anchor_missing=8, citation_prose_not_in_cit_form=0, citation_source_malformed=8); final scoped citation check clean.
- 2026-07-10T02:39+02:00 — HFX3 retro curation: corrected the installed coordinator-template
  account to the otherwise-free-chat launcher contract. Research stays inline; role-shaped work
  spawns a clean architect with the settings-owned profile. Updated the source citation range.
  Verification metadata remains pinned until closeout stamps the eventual two-parent code commit.

- 2026-07-07T21:00+02:00 — 260707-HFX-L6 architect/orchestrator split (synced via
  `sync-runtime.py`): the installed coordinator template now routes developer-facing
  sessions and managed-repo boundary crossings to the architect lifecycle (`roles/architect.md`)
  and points the plan gate at the architect, while spawned role briefs remain authoritative.
  Verification metadata pinned until closeout stamps the HFX-L6 commit.

- 2026-07-06T13:35+02:00 — 260703-L10 round 2 (L10R-2, synced via `sync-runtime.py`): the Onboarding Documentation section's "Until the build/job decision" became "Until the build decision" — the same dead-vocabulary class as the retired names, missed by round 1 in a template the sweep otherwise rewrote. Verification metadata pinned until closeout stamps the L10 commit.
- 2026-07-06T12:05+02:00 — 260703-L10 (one-vocabulary sweep, synced from root `agents-md-files/` via `sync-runtime.py`): the template's `Start Here` section became `Route By Role`, matching the landed `ar-coordination/AGENTS.md` — sessions route through the unified `l-01-agent-lifecycles` skill (spawned agents follow briefs; a developer session is the orchestrator entering `roles/orchestrator.md`), the retired `l-01-session-job-lifecycle` name and the nonexistent `frame` plan-gate phase are gone, and the tasks/AGENTS.md routing bullet points at the orchestrator lifecycle's reframe-research phase. Verification metadata pinned until closeout stamps the L10 commit.
- 2026-06-23T00:53+02:00 — Slice 07 (S5 sync): this generated coordinator-template mirror was re-synced to carry the `read_ar_files` **research-phase read** doctrine — until the build/job decision, read managed-repo source through `read_ar_files` (paired onboarding by construction; counts as retrieval evidence) rather than native read, which is the edit precondition once building begins. Generated-mirror note only; the authored doctrine lives in the `c-04`/`l-01` skills. Verification metadata pinned until closeout stamps the slice-07 code commit.
- 2026-06-08T11:53+02:00: Updated coordinator-template onboarding for the narrower lifecycle entry surface: session start remains the primary lifecycle entry, and managed-repo boundary crossings inside an already-running session re-enter the lifecycle. Verification metadata stays pinned until closeout commits the source change.
- 2026-06-02T03:45+02:00: Rewired the coordinator template to route every session into `l-01-session-job-lifecycle`: replaced the three-way Task Format Routing and the separate `Frame Before You Choose a Format` section with a `Start Here — Enter the Job Lifecycle` section whose only task-format call is `l-01-session-job-lifecycle` skill's build-mode step (read-only exit / chat build / durable `w-02-light-task-workflow` skill); repointed the Installed AGENTS.md Routing bullet at `l-01-session-job-lifecycle` skill's `frame` phase; and de-duped `c-04-retrieval-strategy-router` skill by collapsing the Onboarding Documentation explanation into a pointer to Memory Retrieval Strategies. Part of the `l-01-session-job-lifecycle` skill lifecycle reshape (mcp 1.1.0). Verification metadata recomputed at this closeout.
- 2026-06-02T03:30+02:00: Registered `system/git-workflow.md` as a read-first memory-layer file (when present): added it to the read list after the `c-08-ar-coordination-context-resolver` skill resolves context, and to the memory-repo system-file list, and pointed "Branch And Workflow Notes" at it for the gated-branch landing flow. Verification metadata + the `Runtime AGENTS Template Package` entity fingerprint recomputed at this closeout (mcp 1.0.2).
- 2026-06-01T11:18+02:00: Documented the new top `Frame Before You Choose a Format` routing section (the `tasks/AGENTS.md` collaboration doctrine now applies up front, before a task format is chosen, and routes evidence to `c-04-retrieval-strategy-router` skill) and the slimming of the buried "do not rush" bullet to a plain `tasks/AGENTS.md` pointer. Verification metadata stays pinned; Repo-Internal Reference line ranges and the `Runtime AGENTS Template Package` entity fingerprint will be re-verified/recomputed at the single closeout after the routing-layer optimization pass and mcp version bump.
- 2026-05-29T20:25+02:00: Updated after the coordinator AGENTS template gained the explicit "do not randomly commit; use the `c-12-closeout` skill closeout procedure" workflow-before-code rule.
- 2026-05-27T12:50+02:00: Added the coordinator Git-boundary rule that `ar-coordination/` is a scaffold root, not a repository root; Git commands should target resolved code or memory Git repositories and `tasks/` artifacts stay local unless a workflow says otherwise.
- 2026-05-24T18:10+02:00: Moved onboarding to mirror the packaged runtime source route under `mcp/src/agents_remember/package_data/runtime/` after F-10 packaged runtime asset discovery.
- 2026-05-24T04:34+02:00: Updated after coordinator template made commit approval separate from implementation approval.
- 2026-05-23T21:25+02:00: Simplified provider-authority wording and added installed coordinator code-quality routing to resolved memory-layer tools and coding guidelines.
- 2026-05-23T04:43+02:00: Updated provider readiness onboarding for `context_packet` MCP tool authority instead of coordinator settings.
- 2026-05-21T15:42+02:00: Updated the installed provider readiness command after provider lifecycle commands began inferring the coordinator root from their installed path.
- 2026-05-21T04:09+02:00: Added the configured-provider readiness check after `c-08-ar-coordination-context-resolver` skill in the coordinator root template.
- 2026-05-21T03:05+02:00: Updated coordinator routing so `c-04-retrieval-strategy-router` skill owns retrieval strategy across GrepAI Semantics, CGC Relationship, and Intent proof.
- 2026-05-18T21:44+02:00: Refreshed after pulling the committed `c-04-retrieval-strategy-router` skill onboarding read-mode rename from `origin/main`.
- 2026-05-18T21:38+02:00: Refreshed against the current committed coordinator template, removing unlanded `c-04-retrieval-strategy-router` skill read-mode wording and updating verification metadata.
- 2026-05-18T17:03+02:00: Updated the coordinator onboarding to route onboarding-backed source reading to `c-04-retrieval-strategy-router` instead of duplicating the sidecar lookup and fallback-search protocol inline.
- 2026-05-18T14:09+02:00: Added coordinator-entrypoint guidance for deterministic sidecar lookup and made broad onboarding `rg`/`find` fallback-only discovery after direct sidecar plus governing overview reads. Verification metadata remains pinned to the last committed source until closeout.
- 2026-05-15T15:08+02:00: Added installed `AGENTS.md` routing guidance and developer clarification capture rules that require `c-01-findings-capture` skill, developer approval for onboarding documentation, and code-reality checks before `c-05-create-or-update-onboarding-files` skill propagation.
- 2026-05-15T04:23+02:00: Removed the optional memory-repo `AGENTS.md` lookup from the coordinator template and documented `system/*` files as the memory guidance surface.
- 2026-05-15T00:38+02:00: Refreshed after the coordinator template became one of four runtime `AGENTS.md` templates and absorbed the checkout task routing plus coordinator and memory-layer guidance. Verification metadata remains pinned to the last committed source until closeout.
- 2026-05-13T19:11: Created onboarding for the coordinator AGENTS.md install template.
