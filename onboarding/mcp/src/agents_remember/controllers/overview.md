# mcp/src/agents_remember/controllers/ - MCP Controller Overview

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember-md                         |
| sourceRoute            | `mcp/src/agents_remember/controllers/`     |
| doc_type               | `route-local-overview`                     |
| lastUpdated            | 2026-06-10T07:40+02:00|
| lastVerifiedCommitHash | `ab7e21b4ab4b8526adcdad8ea2243657b8aea7a0` |
| lastVerifiedCommitDate | 2026-06-10T08:21:41+02:00|
| governingOverview      | `../../../overview.md`                     |

## Governing Overview

[mcp/overview.md](../../../overview.md)

## Purpose

`controllers/` owns operation-level MCP composition. Controllers translate
trusted MCP runtime config plus typed tool arguments into package service calls
and JSON-compatible payload dictionaries.

## Hot Path Summary

Use `context_packet.py` for compact `ContextPacketV2` assembly,
`coordination_tools.py` for resolver calls, `memory_tools.py` for drift,
memory quality, route-index, init, baseline, and carryover operations,
`provider_tools.py` for provider status/diagnostics/watchers and GrepAI/CGC
operations, `worktree_tools.py` for `c-09-git-worktree-manager` skill worktree/direct-closeout operations,
`benchmark_tools.py` for Codex benchmark prepare/run, `runtime_install.py` for
runtime install, and `skill_tools.py` for skill installation.

## Route Model

- MCP transport lives in `mcp/server.py` and the `mcp/tools/` package.
- Controllers should remain typed operation facades, not generic command
  runners.
- Domain behavior belongs in service modules such as `providers`,
  `worktrees`, `memory_quality`, `memory`, `benchmarks`, and `install`.
- Response shape validation happens after controller return through the model
  registry (`models/tool_registry.py`), applied by the `mcp/tools/` payload
  builders.

## Invariants And Boundaries

- Controllers resolve repo IDs through `McpRuntimeConfig`; they should not
  accept arbitrary source or coordination roots from tool callers.
- Provider, benchmark, and worktree controllers should call package services
  directly rather than CLI `main(argv)` wrappers.
- Keep each controller file scoped by domain; do not rebuild the former
  `skill_tools.py` mega-facade.

## Repo-Internal References

| Finding | Source Path |
| --- | --- |
| MCP payload builders call these controllers and then validate responses through the model registry. | [mcp/tools/](agents-remember-md/mcp/src/agents_remember/mcp/tools/) |
| Public tool response models live in the models package. | [models overview](../models/overview.md) |

Worktree start is async (GitHub #53): `worktree_tools.py` transfers the temp
lifecycle settings file to the background setup thread on a `starting` result,
forwards `retry_provider_setup`, and bounds worktree provider setup by
`timeoutCaps.providerSetupSeconds` instead of the docker-control default.

## Update History

- 2026-06-10T07:40+02:00 — GitHub #53: `worktree_tools.py` start controller hands the temp lifecycle settings file to the background setup thread (skip-unlink on a `starting` result), forwards `retry_provider_setup`, and bounds worktree provider setup by `timeoutCaps.providerSetupSeconds` instead of the docker-control default.
- 2026-06-06T03:43: Re-verified against the current controller surface (9 files incl. `_guards.py` and per-domain tool modules); corrected `mcp/tools.py` references to the `mcp/tools/` package; re-stamped to `7123da56`.
- 2026-05-28T19:52+02:00: Created after the MCP controller surface split out of the former `skill_tools.py` mega-facade.
