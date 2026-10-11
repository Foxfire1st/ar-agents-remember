# mcp/src/agents_remember/benchmarks/runner_modules Overview

## Current operative account — MIK-R112

The current source facts below replace the former operative inventory. The separately labelled superseded claims describe only the pre-repair card. Original paragraphs, dated closures, evidence and citation identities remain intact in the explicitly historical section; they grant no current call, restored route or fresh execution acceptance.

- benchmark_lifecycle_settings no longer takes a workspace or derives provider blocks from it.
- The shared generator emits enabled=false and an empty provider map.

### Superseded inventory

- Pre-repair card claim: The card still says every benchmark builds indexes and that MCP benchmark application callers exist. This is superseded archival wording, not a current prescription.

### Source and authority bounds

- Source comparison: `mcp/src/agents_remember/benchmarks/runner_modules/mcp_registration.py:239-240,256-300`.
- Source comparison: `mcp/src/agents_remember/providers/settings.py:33-55`.
- Source comparison: `git diff HEAD -- mcp/src/agents_remember/application/benchmark_tools.py (deleted file)`.

Source inspection supplies no new test, native-host, whole-build, landing or memory acceptance. Retained internal services and historical fixtures do not re-advertise deleted MCP tools. Numbered references retain historical custody and may include disclosed inherited stale targets; currentness or proof truth is not inferred from them.

## Historical original card — preserved, not the current operative account

<details>
<summary>Retained original source accounts and producer history</summary>

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| sourceRoute            | `mcp/src/agents_remember/benchmarks/runner_modules` |

## Governing Overview

[overview.md](../../../../overview.md)

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
  GitHub #49) — failures raise with a bounded output tail. Since 260731-EFA-L3 it
  never inherits a **git repository selector** either: both `run_command` and
  `repo_has_commit` pass `env=git_environment()` from
  `kernel/git_command.py`, which strips the eight `GIT_DIR`-family variables
  (`GIT_DIR`, `GIT_WORK_TREE`, `GIT_INDEX_FILE`, `GIT_OBJECT_DIRECTORY`,
  `GIT_ALTERNATE_OBJECT_DIRECTORIES`, `GIT_COMMON_DIR`, `GIT_NAMESPACE`,
  `GIT_PREFIX`). The scrub covers **every** spawned command, not only the ones
  whose argv starts with `git`, because the git argv this runner spawns is
  `clone` / `checkout --detach` / `reset --hard` / `clean -fdx` against a scratch
  workspace — with `GIT_DIR` inherited, the most destructive commands in the
  package would run against whatever repository it names instead. The case manifest
  is NOT provider launch authority (containment R1, 260707-HFX-L1):
  `workspace.filter_benchmark_provider_ids` filters manifest provider ids
  against the caller's `allowed_provider_ids` — the live MCP authority set the
  benchmark application entry points always pass (`None` = no authority context, FAIL-CLOSED
  since review B4; the explicit `AR_BENCHMARK_ALLOW_UNFILTERED_PROVIDERS=1` env
  escape restores an unfiltered direct-script run) — before any workspace
  registration is written or a provider launches, and reports skipped ids
  loudly. `models.py`'s two service requests carry the field; `services.py`
  and `execution.py` thread it down to `prepare_case`.
- `mcp_registration.py` writes benchmark-local MCP/Codex configuration,
  generates provider settings with central `logs/mcp` and `logs/providers`
  paths, and invokes package-local provider setup. Benchmark provider setup is
  **hermetic-cold**: `prepare_configured_providers` wires no seed source, so a
  benchmark builds each index from its own fixture and never starts/clones the
  live workspace provider backends (task 260619). Its
  `disarm_stale_benchmark_registrations` (review B3) is the sweep both
  `services.py` entry points open with: persisted workspace registrations are
  the authority files for sessions booted in those workspaces — the one place
  the fleet kill-switch cannot reach — so every prepare/run pass narrows them
  to the live authority set (idempotent, loud per-file report, `None`
  untouched).
- `execution.py` owns Codex PATH resolution, sandbox policy, command
  construction, per-run metadata, and benchmark run orchestration; its
  `benchmark_mcp_config_overrides` points the benchmarked Codex at the
  benchmark's own MCP server.
- `analysis.py`, `services.py`, and `cli.py` own JSONL metrics, summary
  rendering, MCP service payloads, and the argparse command surface.

## Evidence

### Docs References

No external Domain Documentation source is configured for this memory repo.

### Repo-Internal References

- The public facade re-exports this package for existing callers. [1]
- MCP application entry points call the benchmark service entry points through the facade. [2]
- The shared seed resolvers refuse a benchmark-scoped target as defense-in-depth for the hermetic boundary. [3]

### Cross-Repo References

Benchmark cases may clone external repositories during runs, but this package's
source-level behavior is local to `agents-remember`.

## 260731-EFA-L2 Shared Runner Value Objects

`models.py` now owns five frozen value objects the runner modules are signed on:
`BenchmarkWorkspace` (a materialized case workspace), `BenchmarkTask`, `BenchmarkRun`,
`BenchmarkPreparation` and `BenchmarkRunOutcome`. The load-bearing one is `BenchmarkPreparation`:
**both** `BenchmarkPrepareRequest` and `BenchmarkRunRequest` project onto it through a `preparation`
property, so `prepare_case` takes one object and the prepare and run entry points cannot drift
apart on preparation semantics. `allowed_provider_ids` rides on it, so the containment R1
authority set still reaches `filter_benchmark_provider_ids` with its FAIL-CLOSED `None` handling
intact.

## 260731-EFA-L9 Route Impact — Caller Re-Points

The benchmark runner callers were rewritten by the L9 caller wave: `McpRuntimeConfig` imports now come from `kernel/primitives/runtime_config.py` (the former `mcp/config.py` home) and tool-report/command-capture helpers from `kernel/primitives/`. Runner behavior and benchmark case handling are unchanged.

</details>
