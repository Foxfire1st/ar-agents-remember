# mcp/src/agents_remember/controllers/skill_tools.py

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember                         |
| path                   | `mcp/src/agents_remember/controllers/skill_tools.py` |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-06-06T12:28+02:00                     |
| lastVerifiedCommitHash | `11f28a2035f06f8bc33f11b0617b41cda1122c1f` |
| lastVerifiedCommitDate | 2026-06-06T13:01:33+02:00|
| governingOverview      | `overview.md`                              |

## Purpose

`skill_tools.py` now contains only the `skills_install` controller for package
skill installation.

## Code Commentary

The former large skill-facing MCP facade was split into focused controller
modules. This file keeps `skills_install_tool()`, which delegates to
`install.skills.install_skills()` with dry-run, overwrite, and archive options
and returns an operation-labeled payload (the installer is a flat copy, so there
is no layout option).

## Invariants And Boundaries

- Do not rebuild `skill_tools.py` as a mass re-exporter or mega-controller.
- New MCP operation controllers should live in the domain module that owns the
  behavior, then be imported directly by the relevant `mcp/tools/` domain
  module.
- Skill installation remains a package install concern, not a provider,
  worktree, memory, or benchmark controller.
- `skills_install_tool` defaults `dry_run=False` (act-by-default), forwarding to
  `install.skills.install_skills`; `dry_run=true` previews the copy plan.

## Repo-Internal References

| Finding | Source Path |
| --- | --- |
| Split controller route explains the new domain controller layout. | [controllers overview](overview.md) |
| MCP payload builders import this file only for `skills_install`. | [core.py](agents-remember/mcp/src/agents_remember/mcp/tools/core.py) |
| Skill install response model lives in the models package. | [skills.py](agents-remember/mcp/src/agents_remember/models/skills.py) |

## Update History

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
