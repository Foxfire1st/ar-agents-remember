# mcp/src/agents_remember/benchmarks/runner_modules Overview

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| sourceRoute            | `mcp/src/agents_remember/benchmarks/runner_modules` |

## Governing Overview

[overview](../../../../overview.md)

## Purpose

The `runner_modules` package contains the focused implementation modules behind the public `benchmarks/runner.py` facade. It separates benchmark manifest handling, workspace preparation, local MCP registration, Codex execution, JSONL analysis, service payloads, and CLI wiring so their owners are independently navigable. The facade re-exports these modules and retains a repository-preparation wrapper for its caller hooks.

## Hot Path Summary

- `models.py`, `constants.py`, and `manifest.py` define case data, manifest path validation, case loading, and prompt/variant selection.
- `filesystem.py`, `commands.py`, and `workspace.py` prepare the source-only and with-memory workspaces: ensure coordination directories, remove old paths and the retired coordinator startup files, render the workspace instructions, prepare pinned Git checkouts and the memory repository, then write benchmark MCP registration.
- `mcp_registration.py` writes benchmark-local MCP settings and Codex configuration. Its runtime configuration helper (`benchmark_mcp_config`) sets coordination, workspace, repository, memory, and `logs/mcp` transcript roots without any provider paths or lifecycle-settings generation.
- `execution.py` resolves Codex from PATH, validates sandbox selection, constructs the command, records run metadata, schedules prompt/variant/repetition tasks, and writes summaries. It reads the workspace's Codex MCP configuration into command overrides so the run can use that workspace's configured server.
- `analysis.py` extracts JSONL event counts, command counts, turn token usage, final answers and errors, combines them with run metadata, and renders summaries. `services.py` returns prepare/run payloads; `cli.py` calls those services and exposes list, prepare, run and analyze commands. `roots.py` selects an explicit benchmark root or the packaged benchmark cases.

## Construction

Five frozen value objects describe the runner's preparation and execution flow: `BenchmarkWorkspace`, `BenchmarkTask`, `BenchmarkRun`, `BenchmarkPreparation`, and `BenchmarkRunOutcome`. Both service request types project their preparation fields into `BenchmarkPreparation`. Prepare passes that object to case preparation; run passes it through execution's preparation step unless preparation is skipped.

Case preparation prepares the source-only and with-memory workspaces, syncs coordination directories, prepares the memory repository, constructs `BenchmarkWorkspace`, and writes benchmark MCP registration without provider filtering or provider setup.


Runner runtime-configuration imports come from `kernel/primitives/runtime_config.py`. Git preparation delegates to `kernel/git_command.py`; `commands.py` owns dry-run reporting and failure reporting rather than subprocess construction.

## Invariants and Boundaries



Benchmark Git preparation uses the shared runner, which strips `GIT_DIR`, `GIT_WORK_TREE`, `GIT_INDEX_FILE`, `GIT_OBJECT_DIRECTORY`, `GIT_ALTERNATE_OBJECT_DIRECTORIES`, `GIT_COMMON_DIR`, `GIT_NAMESPACE`, and `GIT_PREFIX`. It captures stdout/stderr and supplies `DEVNULL` as stdin when no input is provided, keeping these Git subprocesses off the parent's protocol streams. A nonzero preparation command raises with at most the last 2,000 characters of its selected output. Clone and fetch use the bulk remote timeout; repository reuse is checked through the metadata timeout. Repository preparation checks out the pinned commit, resets it, and cleans untracked files in the benchmark checkout.

Local MCP registration requires the source repository directory name to match the repository identifier and the memory repository to be at `coordinationRoot/memory-repos/ar-<repoId>`.


Benchmark cases can clone external repositories, but the implementation owners described here are local to `agents-remember`.

## Authority Bounds

The retained service implementations and CLI callers establish the local call flow described here.

Lifecycle, landing and acceptance authority are outside this source account. Their current status is a named uncertainty: this inspection supplies no test execution, native-host execution, whole-build result, landing result or memory acceptance.

## Evidence

- The facade re-exports runner modules and retains its repository-preparation wrapper.
- Case models, manifest validation, selection, shared preparation and workspace construction.
- Benchmark registration, registration sweep and disabled lifecycle-settings construction.
- Git preparation delegates to the shared environment, argv and subprocess owner.
- Codex execution, analysis, service payloads and direct CLI callers.

## No skill exposure in a benchmark workspace

Preparation mirrors no skill tree into a workspace: `sync_runtime_assets` removes the retired coordinator startup files (`AGENTS.md`, `system/AGENTS.md`, `tasks/AGENTS.md`) and ensures the benchmark coordination directories, no `.codex/skills` exposure helper exists, no preparation object carries a skill-exposure mode and no command accepts one. The workspace's harness reads the skills the tool server serves from its package copy, through the benchmark-local MCP registration the workspace writes.

- The runtime-asset sync that writes no skill tree.

[1] mcp/src/agents_remember/benchmarks/runner.py — lines 28-28; mcp/src/agents_remember/benchmarks/runner.py — lines 10-24; mcp/src/agents_remember/benchmarks/runner.py — lines 28-33
[4] mcp/src/agents_remember/benchmarks/runner_modules/models.py — lines 1-156; mcp/src/agents_remember/benchmarks/runner_modules/manifest.py — lines 1-223; mcp/src/agents_remember/benchmarks/runner_modules/workspace.py — lines 1-293; mcp/src/agents_remember/benchmarks/runner_modules/filesystem.py — lines 1-176
[5] mcp/src/agents_remember/benchmarks/runner_modules/mcp_registration.py — lines 1-300; mcp/src/agents_remember/providers/settings.py — lines 32-47; mcp/src/agents_remember/providers/provider_setup.py — lines 56-121; mcp/src/agents_remember/providers/setup_common.py — lines 66-102
[6] mcp/src/agents_remember/benchmarks/runner_modules/commands.py — lines 1-57; mcp/src/agents_remember/kernel/git_command.py — lines 58-68; mcp/src/agents_remember/kernel/git_command.py — lines 151-231; mcp/src/agents_remember/kernel/git_command.py — lines 302-347; mcp/src/agents_remember/benchmarks/runner_modules/workspace.py — lines 38-75
[7] mcp/src/agents_remember/benchmarks/runner_modules/execution.py — lines 1-420; mcp/src/agents_remember/benchmarks/runner_modules/analysis.py — lines 1-221; mcp/src/agents_remember/benchmarks/runner_modules/services.py — lines 1-117; mcp/src/agents_remember/benchmarks/runner_modules/cli.py — lines 1-185; mcp/src/agents_remember/benchmarks/runner_modules/roots.py — lines 1-17
[8] mcp/src/agents_remember/benchmarks/runner_modules/filesystem.py — symbol sync_runtime_assets

- The facade re-exports runner modules and retains its repository-preparation wrapper. [1]


- Case models, manifest validation, selection, shared preparation and workspace construction. [4]


- Benchmark-local MCP settings, Codex configuration, and runtime-config construction. [5]

- Git preparation delegates to the shared environment, argv and subprocess owner. [6]


- Codex execution, analysis, service payloads and direct CLI callers. [7]


- The runtime-asset sync that writes no skill tree. [8]
