# mcp/src/agents_remember/benchmarks/runner_modules/services.py

## Governing Overview

[runner_modules overview](overview.md)

## Purpose

MCP-facing benchmark service payload functions.

## Code Commentary

### 260731-EFA-L2 Preparation And Outcome Objects

`prepare_benchmarks` derives `preparation = request.preparation` once and calls
`prepare_case(preparation, case, provider_ids=selected_provider_ids(case))`; `run_selected_cases`
calls `run_case(request, case)`. Both therefore thread `request.allowed_provider_ids` to the
workspace provider filter through the preparation object (containment R1, 260707-HFX-L1) rather
than as a loose keyword, and both still OPEN with `disarm_stale_benchmark_registrations`.

`benchmark_run_payload(request, benchmarks_root, outcome)` takes a `BenchmarkRunOutcome` in place
of the `cases` / `output_roots` / `messages` / `resolved_codex_executable` arguments. The emitted
payload keys are unchanged. `run_selected_cases`'s `cases` parameter is now typed
`list[BenchmarkCase]` instead of `list[Any]`.

### Logic

`services.py` implements `prepare_benchmarks()` and `run_codex_benchmark()`, capturing human-readable progress messages while returning structured payloads without command-style stdout/stderr wrappers.

`prepare_benchmarks()` and `run_selected_cases()` thread
`request.allowed_provider_ids` into `prepare_case`/`run_case` (containment R1,
260707-HFX-L1), so the MCP-supplied live-authority set reaches the workspace
provider filter unchanged. Both entry points also OPEN with
`disarm_stale_benchmark_registrations(benchmarks_root,
request.allowed_provider_ids)` (review B3): `prepare_benchmarks`'s
`run_prepare` and `run_selected_cases` sweep every persisted workspace
registration before any case work, because those files are the authority
settings for sessions later booted in the workspaces — the one place the
fleet kill-switch cannot reach.

### Invariants And Boundaries

- Service payloads must remain application-friendly dictionaries.
- CLI-specific printing and parser behavior belongs in `cli.py`.
- `allowed_provider_ids` is pass-through plumbing here: the service layer must
  never default it away or synthesize its own set (containment R1).
- Every prepare/run pass sweeps stale workspace registrations
  (`disarm_stale_benchmark_registrations`) before case work (review B3).

## Evidence

### Docs References

No external Domain Documentation source is configured for this memory repo.

### Repo-Internal References

- The public benchmark facade re-exports this module's public functions and classes for compatibility. [1]
- The route-local overview summarizes how this module fits into the benchmark runner split. [2]
- The stale-registration sweep both entry points open with lives in the registration module. [3]
- Benchmark behavior is covered through the existing worktree/tool test slices. [4]

### Cross-Repo References

No configured sibling repository is required for this module.
