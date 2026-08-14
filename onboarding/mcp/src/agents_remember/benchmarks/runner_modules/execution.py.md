# mcp/src/agents_remember/benchmarks/runner_modules/execution.py

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember                         |
| path                   | `mcp/src/agents_remember/benchmarks/runner_modules/execution.py` |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-07-31T00:00+02:00                     |
| lastVerifiedCommitHash | `5aff1e8f01dfa949efc8f68e46bc62a99ed31432`
| lastVerifiedCommitDate | 2026-08-14T14:36:50+02:00|
| governingOverview      | `overview.md`                              |

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

## Docs References

No external Domain Documentation source is configured for this memory repo.

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The public benchmark facade re-exports this module's public functions and classes for compatibility. | "from agents_remember.benchmarks.runner_modules.execution import *" | mcp/src/agents_remember/benchmarks/runner.py:17-17 |
| The benchmark MCP registration writes the `.codex/config.toml` whose `mcp_servers` table these overrides read. | `benchmark_agents_config_text` | mcp/src/agents_remember/benchmarks/runner_modules/mcp_registration.py:131-151 |
| Benchmark behavior is covered through the existing worktree/tool test slices. | `test_codex_command_forwards_benchmark_mcp_config` | mcp/tests/test_worktree_support_benchmark.py:441-495 |

## Cross-Repo References

No configured sibling repository is required for this module.

## Update History

- 2026-08-04T18:20+02:00 — 260731-EFA-L6 S18-B15 curator: resolved 6 citation findings and cut one false
  paragraph. `allowed_provider_ids` rides `BenchmarkPreparation` into `prepare_case`; the stale
  threaded-parameter paragraph was removed (the correct L2 form directly above it stands). Re-anchored
  the facade (runner.py:17), config-text (mcp_registration.py:131-151), and benchmark-test
  (3498-3553) rows. Scoped recheck clean.
- 2026-07-31T00:00+02:00 — 260731-EFA-L2 (gate honesty, `C901`/`PLR0913` armed with no
  exemptions): `run_case`, `maybe_prepare_case`, `run_one` and `run_dry_batches` were re-signed
  onto `BenchmarkRunRequest` / `BenchmarkPreparation` / `BenchmarkRun` / `BenchmarkTask`, and
  `task_batches_for_prompt` now emits `BenchmarkTask` values. `allowed_provider_ids` now reaches
  `prepare_case` via `BenchmarkPreparation`. Run outputs are unchanged. Verification metadata
  pinned until closeout stamps the L2 commit.
- 2026-07-07T16:30+02:00 — 260707-HFX-L1 (provider containment R1): `maybe_prepare_case` and
  `run_case` gained the pass-through `allowed_provider_ids` parameter feeding the workspace
  provider filter. Verification metadata pinned until closeout stamps the HFX-L1 commit.
- 2026-06-19T13:42: Added `benchmark_mcp_config_overrides()` and wired it into `codex_command`: it reads the benchmark workspace `.codex/config.toml` `mcp_servers` table and emits `-c mcp_servers.<name>.<key>=<literal>` overrides so the benchmarked Codex uses the benchmark's own isolated MCP server, not the host workspace's.
- 2026-05-26T02:26+02:00: Created when `benchmarks/runner.py` was split into focused implementation modules.
