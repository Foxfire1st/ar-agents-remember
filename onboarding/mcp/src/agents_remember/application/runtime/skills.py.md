# mcp/src/agents_remember/application/runtime/skills.py

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember                         |
| path                   | `mcp/src/agents_remember/application/runtime/skills.py` |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-08-13T08:40+02:00                     |
| lastVerifiedCommitHash | `a09b906bbf2855c3479b4d3199607ff8689b7d93` |
| lastVerifiedCommitDate | 2026-08-13T13:51:44+02:00|
| governingOverview      | `overview.md`                              |

## Governing Overview

[runtime overview](overview.md)

## Purpose

`runtime/skills.py` contains only the `skills_install` application entry point for package
skill installation.

## Code Commentary

The former large skill-facing MCP facade was split into focused application entry point
modules. This file keeps `skills_install_tool()`, which delegates to
`install.skills.install_skills()` with dry-run, overwrite, and archive options
and returns an operation-labeled payload (the installer is a flat copy, so there
is no layout option).

## Invariants And Boundaries

- Do not rebuild `runtime/skills.py` as a mass re-exporter or mega-entry-point.
- New MCP operation application entry points should live in the domain module that owns the
  behavior, then be imported directly by the relevant `mcp/tools/` domain
  module.
- Skill installation remains a package install concern, not a provider,
  worktree, memory, or benchmark application entry point.
- `skills_install_tool` defaults `dry_run=False` (act-by-default), forwarding to
  `install.skills.install_skills`; `dry_run=true` previews the copy plan.

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| Split application route explains the new application layer layout. | `# mcp/src/agents_remember/application/ - MCP Application Layer Overview` | onboarding/mcp/src/agents_remember/application/overview.md:1-312 |
| MCP payload builders import this file only for `skills_install`. | `skills_install` | mcp/src/agents_remember/mcp/tools/core.py:152-152 |
| Skill install response model lives in the models package. | `SkillsInstallResponse` | mcp/src/agents_remember/models/skills.py:12-20 |

## Update History

- 2026-08-13T08:40+02:00 — L23 integration-gate repair: moved the preserved skill-install card with its source into the cohesive `application/runtime/` package and rebound it to the new governing overview; behavior is unchanged. Verification metadata remains closeout-owned.

- 2026-08-08T17:18+02:00 — No content impact: 260731-EFA-L9 rewrote this source's imports/callers only (model-extraction caller wave); the behavior this card documents is unchanged and the body was re-verified current. Verification metadata pinned until closeout stamps the L9 code commit.

- 2026-08-04T18:18+02:00 — 260731-EFA-L6 S18-B17 curator: repaired the two malformed rows — the
  application overview is now cited as the memory card `onboarding/.../application/overview.md`
  with its `#` heading anchor, and the response-model row is rebound to `SkillsInstallResponse`
  with the spurious `agents-remember/` path prefix dropped. Claim wording unchanged.
- 2026-08-02T01:05+02:00 — No content impact: `mcp/src/agents_remember/tasks/reopen.py` moved to `mcp/src/agents_remember/worktrees/reopen.py` (reopen rewrites the leaf's enclosure contract, and ranking it as a task operation made `tasks` and `worktrees` mutually dependent per `layers.toml`). Re-pointed the reference here; the behavior this document describes is unchanged. Verification metadata pinned until closeout stamps the L6 code commit.
- 2026-08-02T00:17+02:00 — 260731-EFA-L6 curator: source moved. `mcp/src/agents_remember/controllers/` was renamed to `application/`, so this sidecar moved with its source; path metadata and every in-body path follow, and the prose adopts "the application layer" / "an application entry point" for what it used to call a controller. Behavior is unchanged. Verification metadata pinned until closeout stamps the L6 code commit.
- 2026-06-06T12:28+02:00: Corrected current MCP payload-builder references after the former `mcp/tools.py` module became the `mcp/tools/` package; source behavior unchanged.
- 2026-06-02T04:40+02:00: Dropped the `layout` option from `skills_install_tool` after the installer became a single flat copy (U-01-core-skills dissolved). `l-01-session-job-lifecycle` skill series, Sub-task B/S7, mcp 1.1.0.
- 2026-05-28T19:52+02:00: Updated after provider, worktree, memory, coordination, and benchmark controllers moved out of the former `skill_tools.py` mega-facade.
- 2026-05-28T12:32+02:00: Updated after `provider_watchers` status began writing and returning current provider state snapshots.
- 2026-05-26T23:11+02:00: Refreshed verification metadata after source commit `5ab704a` landed the GrepAI MCP search and trace shape.
- 2026-05-26T22:54+02:00: Updated after GrepAI MCP search gained workspace/project selection, JSON default output, configured-repo validation, and explicit trace action handling.
- 2026-05-25T19:16+02:00: Updated after provider lifecycle wording switched to the direct `providers.lifecycle` facade.
- 2026-05-24T19:25+02:00: Updated after provider operation controllers gained a shared runner-integrity preflight that blocks lifecycle execution on manifest drift.
- 2026-05-24T10:06+02:00: Refreshed verification metadata after source commit `f48a346` forwarded benchmark sandbox options through MCP controller payloads.
- 2026-05-24T08:56+02:00: Updated after `codex_benchmark_run_tool()` began forwarding the allowlisted `codex_sandbox` mode into success and missing-Codex policy payloads.
- 2026-05-24T06:57+02:00: Updated after Codex benchmark missing-executable responses started exposing benchmark-only `PATH` resolution policy.
- 2026-05-24T05:03+02:00: Updated after `worktree_start_tool()` switched provider setup handoff to an internal `WorktreeProviderSetupConfig`.
- 2026-05-24T02:47+02:00: Updated after adding the `memory_quality_check` controller for closeout drift and onboarding style checks.
- 2026-05-24T00:35+02:00: Updated after worktree, baseline, carryover, and benchmark controllers stopped using command-style `main(argv)` capture.
- 2026-05-23T20:56+02:00: Updated after MCP provider tools moved from provider lifecycle CLI capture to typed lifecycle service calls.
- 2026-05-23T20:42+02:00: Updated for typed CodeGraphContext controllers replacing the generic `cgc_query` facade.
- 2026-05-23T13:46+02:00: Updated for MCP-derived worktree provider settings after source scripts were removed.
- 2026-05-23T13:09+02:00: Created for the Phase 04 skill MCP tool surface.
