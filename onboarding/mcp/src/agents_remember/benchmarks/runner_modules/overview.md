# mcp/src/agents_remember/benchmarks/runner_modules Overview

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember                         |
| doc_type               | `route-local-overview`                     |
| sourceRoute            | `mcp/src/agents_remember/benchmarks/runner_modules` |
| lastUpdated            | 2026-06-10T05:30+02:00                     |
| lastVerifiedCommitHash | `add1235644c8a5a4b5d6a1b114f29510cdc03d36` |
| lastVerifiedCommitDate | 2026-06-19T15:03:04+02:00|
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
  `commands.py`'s `run_command` captures stdout/stderr and never inherits the
  parent's stdio (on MCP stdio transport those are the protocol pipes; 2.5.1,
  GitHub #49) — failures raise with a bounded output tail.
- `mcp_registration.py` writes benchmark-local MCP/Codex configuration,
  generates provider settings with central `logs/mcp` and `logs/providers`
  paths, and invokes package-local provider setup. Benchmark provider setup is
  **hermetic-cold**: `prepare_configured_providers` wires no seed source, so a
  benchmark builds each index from its own fixture and never starts/clones the
  live workspace provider backends (task 260619).
- `execution.py` owns Codex PATH resolution, sandbox policy, command
  construction, per-run metadata, and benchmark run orchestration; its
  `benchmark_mcp_config_overrides` points the benchmarked Codex at the
  benchmark's own MCP server.
- `analysis.py`, `services.py`, and `cli.py` own JSONL metrics, summary
  rendering, MCP service payloads, and the argparse command surface.

## Docs References

No external Domain Documentation source is configured for this memory repo.

## Repo-Internal References

| Finding | Source Path |
| --- | --- |
| The public facade re-exports this package for existing callers. | [runner.py](agents-remember/mcp/src/agents_remember/benchmarks/runner.py) |
| MCP controllers call the benchmark service entry points through the facade. | [skill_tools.py](agents-remember/mcp/src/agents_remember/controllers/skill_tools.py) |
| The shared seed resolvers refuse a benchmark-scoped target as defense-in-depth for the hermetic boundary. | [grepai/seed.py](agents-remember/mcp/src/agents_remember/providers/grepai/seed.py) |
| Focused benchmark tests exercise facade compatibility, provider setup, MCP registration, Codex execution policy, repository prep, and skill exposure behavior. | [test_worktree_support.py](agents-remember/mcp/tests/test_worktree_support.py) |

## Cross-Repo References

Benchmark cases may clone external repositories during runs, but this package's
source-level behavior is local to `agents-remember`.

## Update History

- 2026-06-19T13:42: Benchmark provider setup is now hermetic-cold — `workspace.py`/`mcp_registration.py` wire no seed source, so benchmark stacks index their own fixture and never start/clone the live workspace backends (task 260619). `execution.py` gained `benchmark_mcp_config_overrides` so the benchmarked Codex uses the benchmark's own MCP server.
- 2026-06-11T14:12+02:00: No route impact: the repository rename sweep replaced `agents-remember-md` with `agents-remember` in files on this route; route structure and overview content are unchanged.
- 2026-06-10T05:30+02:00 — Route body caught up with 2.5.1: `run_command` captures output and never inherits parent stdio (GitHub #49). Previous closeouts had only stamped the verification header (developer-flagged gap).
- 2026-05-30T21:51+02:00: Re-verified the route against `825a172`; the module split summary still matches. The only route change since `3f09b75` was `mcp_registration.py` renaming the generated `providerSeconds` cap to `providerSetupSeconds` (documented on its file card).
- 2026-05-28T12:32+02:00: Updated after benchmark provider settings and scaffolded runtime assets moved logs under the central `logs/` tree.
- 2026-05-26T02:26+02:00: Created when `benchmarks/runner.py` was split into focused implementation modules.
