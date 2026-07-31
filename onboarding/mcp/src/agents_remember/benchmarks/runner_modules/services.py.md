# mcp/src/agents_remember/benchmarks/runner_modules/services.py

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember                         |
| path                   | `mcp/src/agents_remember/benchmarks/runner_modules/services.py` |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-07-31T00:00+02:00                     |
| lastVerifiedCommitHash | `f3115ce8603f83b7b5cbd82aa402f66ec1d8a29d` |
| lastVerifiedCommitDate | 2026-07-31T19:28:50+02:00|
| governingOverview      | `overview.md`                              |

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

- Service payloads must remain controller-friendly dictionaries.
- CLI-specific printing and parser behavior belongs in `cli.py`.
- `allowed_provider_ids` is pass-through plumbing here: the service layer must
  never default it away or synthesize its own set (containment R1).
- Every prepare/run pass sweeps stale workspace registrations
  (`disarm_stale_benchmark_registrations`) before case work (review B3).

## Docs References

No external Domain Documentation source is configured for this memory repo.

## Repo-Internal References

| Finding | Source Path |
| --- | --- |
| The public benchmark facade re-exports this module's public functions and classes for compatibility. | [runner.py](agents-remember/mcp/src/agents_remember/benchmarks/runner.py) |
| The route-local overview summarizes how this module fits into the benchmark runner split. | [runner_modules overview](agents-remember/mcp/src/agents_remember/benchmarks/runner_modules/overview.md) |
| The stale-registration sweep both entry points open with lives in the registration module. | [mcp_registration.py](agents-remember/mcp/src/agents_remember/benchmarks/runner_modules/mcp_registration.py) |
| Benchmark behavior is covered through the existing worktree/tool test slices. | [test_worktree_support.py](agents-remember/mcp/tests/test_worktree_support.py) |

## Cross-Repo References

No configured sibling repository is required for this module.

## Update History

- 2026-07-31T00:00+02:00 — 260731-EFA-L2 (gate honesty, `PLR0913` armed with no exemptions):
  `prepare_benchmarks` / `run_selected_cases` now pass `BenchmarkPreparation` and the whole
  request down, and `benchmark_run_payload` takes a `BenchmarkRunOutcome`. Emitted payloads are
  unchanged. Verification metadata pinned until closeout stamps the L2 commit.
- 2026-07-07T17:40+02:00 — 260707-HFX-L1 review fix B3: `prepare_benchmarks.run_prepare` and
  `run_selected_cases` now both open with
  `disarm_stale_benchmark_registrations(benchmarks_root, request.allowed_provider_ids)`, sweeping
  persisted workspace registrations before case work. Verification metadata pinned until closeout
  stamps the HFX-L1 commit.
- 2026-07-07T16:30+02:00 — 260707-HFX-L1 (provider containment R1): `prepare_benchmarks` and
  `run_selected_cases` now thread `request.allowed_provider_ids` through to
  `prepare_case`/`run_case`. Verification metadata pinned until closeout stamps the HFX-L1
  commit.
- 2026-05-26T02:26+02:00: Created when `benchmarks/runner.py` was split into focused implementation modules.
