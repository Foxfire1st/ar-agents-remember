# mcp/src/agents_remember/benchmarks/runner_modules/execution.py

## Governing Overview

[runner_modules overview](overview.md)

## Purpose

Codex benchmark execution policy, command construction, per-run metadata, and run orchestration.

## Code Commentary

### 260731-EFA-L2 Run/Task Objects

The execution entry points now take value objects instead of long keyword lists:

- `run_case(request: BenchmarkRunRequest, case)` — one request and one case. It derives
  `preparation = request.preparation` and passes that down, so a run prepares its workspace under
  exactly the same rules `codex_benchmark_prepare` uses.
- `maybe_prepare_case(preparation, case, *, prompt_id, variant_id, skip_prepare)` — the
  preparation object plus the three decisions that are the *run's* own.
- `run_one(run: BenchmarkRun, task: BenchmarkTask)` and
  `run_dry_batches(run: BenchmarkRun, task_batches)` — the case execution frame plus the scheduled
  work. `task_batches_for_prompt` now emits `BenchmarkTask` values rather than bare
  `(prompt, variant, repetition)` tuples, so a batch element is self-describing.

`allowed_provider_ids` still reaches `prepare_case` — it now rides on `BenchmarkPreparation`
rather than being threaded as its own parameter — so the containment R1 (260707-HFX-L1)
live-authority set still flows from the service request to the workspace provider filter.

### Logic

`execution.py` resolves `codex` from PATH, validates the allowlisted sandbox modes, writes per-run metadata, runs prompt variants, builds batches, executes them concurrently, writes summaries, and reports subprocess failures. `benchmark_mcp_config_overrides(cwd)` reads the benchmark workspace's `.codex/config.toml` `mcp_servers` table and emits `-c mcp_servers.<name>.<key>=<literal>` overrides (scalars, `env`, and `env_vars`), which `codex_command` appends so the benchmarked Codex talks to the benchmark's **own** isolated MCP server rather than inheriting the host workspace's MCP configuration.

### Invariants And Boundaries

- Codex execution remains benchmark-only host execution and must not accept arbitrary executable paths or shell snippets.
- `run_case()` is an orchestration wrapper; batching, dry-run replay, and failure collection live in focused helpers.
- The benchmarked Codex must be pointed at the benchmark's own MCP server via the generated `.codex/config.toml` overrides, so a benchmark run never drives the live workspace MCP/providers.

## Evidence

### Docs References

No external Domain Documentation source is configured for this memory repo.

### Repo-Internal References

- The public benchmark facade re-exports this module's public functions and classes for compatibility. [1]
- The benchmark MCP registration writes the `.codex/config.toml` whose `mcp_servers` table these overrides read. [2]

### Cross-Repo References

No configured sibling repository is required for this module.
