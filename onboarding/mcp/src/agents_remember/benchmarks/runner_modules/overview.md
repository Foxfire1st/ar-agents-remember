# mcp/src/agents_remember/benchmarks/runner_modules Overview

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember-md                         |
| doc_type               | `route-local-overview`                     |
| sourceRoute            | `mcp/src/agents_remember/benchmarks/runner_modules` |
| lastUpdated            | 2026-05-30T21:51+02:00                     |
| lastVerifiedCommitHash | `825a172bdf0d4ee3489ae25dbcc19c4e9c7b9493` |
| lastVerifiedCommitDate | 2026-05-30T17:31:45+02:00|
| governingOverview      | `../../../../overview.md`                  |

## Purpose

The `runner_modules` package contains the focused implementation modules behind
the public `benchmarks/runner.py` facade. It exists to keep benchmark manifest
handling, workspace setup, provider registration, Codex execution, JSONL
analysis, service payloads, and CLI wiring independently navigable and testable.

## Hot Path Summary

- `models.py`, `constants.py`, and `manifest.py` define benchmark case data,
  supported provider ids, manifest path validation, case loading, and
  prompt/variant selection.
- `filesystem.py`, `commands.py`, and `workspace.py` own benchmark workspace
  mutation: copying runtime assets, safe removal, Git checkout preparation,
  template rendering, memory repo preparation, and whole-case setup.
- `mcp_registration.py` writes benchmark-local MCP/Codex configuration,
  generates provider settings with central `logs/mcp` and `logs/providers`
  paths, and invokes package-local provider setup with generated provider
  settings.
- `execution.py` owns Codex PATH resolution, sandbox policy, command
  construction, per-run metadata, and benchmark run orchestration.
- `analysis.py`, `services.py`, and `cli.py` own JSONL metrics, summary
  rendering, MCP service payloads, and the argparse command surface.

## Docs References

No external Domain Documentation source is configured for this memory repo.

## Repo-Internal References

| Finding | Source Path |
| --- | --- |
| The public facade re-exports this package for existing callers. | [runner.py](agents-remember-md/mcp/src/agents_remember/benchmarks/runner.py) |
| MCP controllers call the benchmark service entry points through the facade. | [skill_tools.py](agents-remember-md/mcp/src/agents_remember/controllers/skill_tools.py) |
| Focused benchmark tests exercise facade compatibility, provider setup, MCP registration, Codex execution policy, repository prep, and skill exposure behavior. | [test_worktree_support.py](agents-remember-md/mcp/tests/test_worktree_support.py) |

## Cross-Repo References

Benchmark cases may clone external repositories during runs, but this package's
source-level behavior is local to `agents-remember-md`.

## Update History

- 2026-05-30T21:51+02:00: Re-verified the route against `825a172`; the module split summary still matches. The only route change since `3f09b75` was `mcp_registration.py` renaming the generated `providerSeconds` cap to `providerSetupSeconds` (documented on its file card).
- 2026-05-28T12:32+02:00: Updated after benchmark provider settings and scaffolded runtime assets moved logs under the central `logs/` tree.
- 2026-05-26T02:26+02:00: Created when `benchmarks/runner.py` was split into focused implementation modules.
