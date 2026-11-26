# mcp/src/agents_remember/benchmarks/runner_modules/services.py

## Governing Overview

[runner_modules overview](overview.md)

## Purpose

MCP-facing benchmark service payload functions.

## Code Commentary

### 260731-EFA-L2 Preparation And Outcome Objects

`prepare_benchmarks` derives `preparation = request.preparation` once and calls
`prepare_case(preparation, case)`; `run_selected_cases` calls `run_case(request, case)`.

`benchmark_run_payload(request, benchmarks_root, outcome)` takes a `BenchmarkRunOutcome` in place
of the `cases` / `output_roots` / `messages` / `resolved_codex_executable` arguments. The emitted
payload keys are unchanged. `run_selected_cases`'s `cases` parameter is now typed
`list[BenchmarkCase]` instead of `list[Any]`.

### Logic

`services.py` implements `prepare_benchmarks()` and `run_codex_benchmark()`, capturing human-readable progress messages while returning structured payloads without command-style stdout/stderr wrappers.


### Invariants And Boundaries

- Service payloads must remain application-friendly dictionaries.
- CLI-specific printing and parser behavior belongs in `cli.py`.

## Evidence

### Docs References

No external Domain Documentation source is configured for this memory repo.

### Repo-Internal References

- The public benchmark facade re-exports this module's public functions and classes for compatibility. [1]
- The route-local overview summarizes how this module fits into the benchmark runner split. [2]
- Benchmark behavior is covered through the existing worktree/tool test slices. [4]

### Cross-Repo References

No configured sibling repository is required for this module.
