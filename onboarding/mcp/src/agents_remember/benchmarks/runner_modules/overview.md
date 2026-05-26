# mcp/src/agents_remember/benchmarks/runner_modules Overview

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember-md                         |
| doc_type               | `route-local-overview`                     |
| sourceRoute            | `mcp/src/agents_remember/benchmarks/runner_modules` |
| lastUpdated            | 2026-05-26T02:26+02:00                     |
| lastVerifiedCommitHash | `a7e160cd4381245327da7c5a52e2272b3080ebf7` |
| lastVerifiedCommitDate | 2026-05-26T02:40:22+02:00|
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
- `mcp_registration.py` writes benchmark-local MCP/Codex configuration and
  invokes package-local provider setup with generated provider settings.
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

- 2026-05-26T02:26+02:00: Created when `benchmarks/runner.py` was split into focused implementation modules.
