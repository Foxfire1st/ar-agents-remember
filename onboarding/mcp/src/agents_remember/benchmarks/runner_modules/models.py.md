# mcp/src/agents_remember/benchmarks/runner_modules/models.py

## Governing Overview

[runner_modules overview](overview.md)

## Purpose

Typed benchmark case and service request dataclasses.

## Code Commentary

### 260731-EFA-L2 Shared Benchmark Value Objects

This dated migration introduced five frozen dataclasses. The signature and six-field projection account below describe that migration; the current `BenchmarkPreparation` has three facts (`benchmarks_root`, `dry_run`, `force_clone`) and no `skill_exposure_mode`, `provider_timeout`, or `allowed_provider_ids`:

- **`BenchmarkWorkspace(case, workspace_root, coordination_root, source_repo_root, memory_repo)`** — one case's materialized with-memory workspace: the case plus the roots laid down for it. Prepared once by `workspace.prepare_case` and handed whole to `write_benchmark_mcp_registration`.
- **`BenchmarkTask(prompt, variant, repetition)`** — one prompt/variant/repetition scheduled inside
  a run. It replaces the bare `(prompt, variant, repetition)` tuples the batch builder used to emit.
- **`BenchmarkRun(benchmarks_root, case, output_root, dry_run, codex_sandbox=CODEX_BENCHMARK_SANDBOX)`**
  — one case execution: what it reads, where results land, how Codex runs.
- **`BenchmarkPreparation(benchmarks_root, dry_run=True, skill_exposure_mode="copy",
  force_clone=False, provider_timeout=1800, allowed_provider_ids=None)`** — how a workspace is
  (re)materialized before use. **Shared by prepare and run**: `BenchmarkPrepareRequest` and
  `BenchmarkRunRequest` each expose a `preparation` property projecting onto it (resolving
  `benchmarks_root` as they go), so `prepare_case` takes one object instead of the same six fields
  unpacked at every layer — and the two entry points cannot drift apart on preparation semantics.
- **`BenchmarkRunOutcome(cases, output_roots, messages, codex_executable)`** — what one
  `codex_benchmark_run` produced, before it is rendered as a payload.


### Logic

`models.py` defines `BenchmarkCase`, `BenchmarkPrepareRequest`, and `BenchmarkRunRequest`, including property accessors that normalize manifest dictionaries for downstream modules.


### Invariants And Boundaries

- Keep request defaults here aligned with the CLI and MCP tool defaults.
- Do not add workflow behavior to the dataclasses.

## Evidence

### Docs References

No external Domain Documentation source is configured for this memory repo.

### Repo-Internal References

- The public benchmark facade re-exports this module's public functions and classes for compatibility. [1]
The [route overview](overview.md) describes the benchmark runner split; it is a discovery companion rather than a repository source target.

### Cross-Repo References

No configured sibling repository is required for this module.

## Preparation carries no skill-exposure mode

`BenchmarkPreparation`, `BenchmarkPrepareRequest` and `BenchmarkRunRequest` no longer carry `skill_exposure_mode`, and the preparation projections no longer forward it: there is no copy-or-none choice left to name. The remaining preparation facts are root, dry run and force clone (`provider_timeout` and `allowed_provider_ids` were removed).

- The shared preparation object, without a skill-exposure mode. [3]

- Current source account and its stated boundaries. [4]
