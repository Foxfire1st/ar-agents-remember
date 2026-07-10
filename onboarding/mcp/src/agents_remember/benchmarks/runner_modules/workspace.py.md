# mcp/src/agents_remember/benchmarks/runner_modules/workspace.py

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember                         |
| path                   | `mcp/src/agents_remember/benchmarks/runner_modules/workspace.py` |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-07-07T17:40+02:00                     |
| lastVerifiedCommitHash | `0d5ce6784930aa4e9006ab4bbf2b788a3296abce` |
| lastVerifiedCommitDate | 2026-07-10T22:30:19+02:00|
| governingOverview      | `overview.md`                              |

## Governing Overview

[runner_modules overview](overview.md)

## Purpose

Benchmark workspace and repository preparation orchestration.

## Code Commentary

### Logic

`workspace.py` derives source-only and with-memory workspace paths, prepares Git checkouts, renders benchmark AGENTS files, syncs runtime assets, writes MCP registration, prepares memory repos, and invokes configured provider setup. `prepare_case` calls `prepare_configured_providers` with no seed source: each benchmark stack indexes its own pinned fixture from scratch (hermetic-cold) rather than warm-starting from the live workspace.

`filter_benchmark_provider_ids(case_id, provider_ids, allowed_provider_ids)`
(containment R1, 260707-HFX-L1) enforces that the case manifest is not launch
authority: `prepare_case` filters the manifest's provider ids against the live
MCP authority set as its first step — before the workspace registration is
written (a persisted registration would arm every later session booted in that
workspace) and before `prepare_configured_providers` can launch anything.
Skipped ids are reported loudly with a printed message naming the case and the
authority. `allowed_provider_ids=None` (no authority context, i.e. direct
script use below the MCP layer) is FAIL-CLOSED too — review finding B4: an
implicit default must not be the bypass — every requested provider is skipped
with a loud message naming the escape hatch, unless the explicit developer
act `AR_BENCHMARK_ALLOW_UNFILTERED_PROVIDERS=1` (the module's
`UNFILTERED_PROVIDERS_ENV` constant) is set, which restores the unfiltered
direct-script run.

### Invariants And Boundaries

- Workspace preparation is case setup, not Codex execution.
- Path derivation must stay manifest-validated and relative to the benchmark root.
- Benchmark provider setup is hermetic: `prepare_case` never passes a seed-source coordination root, so a benchmark run cannot start or clone the live workspace provider backends. Seeding from the live workspace previously cascaded a full re-embed across main and every worktree (task 260619).
- The case manifest is not launch authority (containment R1): provider ids outside the caller's `allowed_provider_ids` are dropped — and reported — before any registration or launch; `None` is fail-closed as well (review B4), and only the explicit `AR_BENCHMARK_ALLOW_UNFILTERED_PROVIDERS=1` env escape arms an unfiltered direct-script run.

## Docs References

No external Domain Documentation source is configured for this memory repo.

## Repo-Internal References

| Finding | Source Path |
| --- | --- |
| The public benchmark facade re-exports this module's public functions and classes for compatibility. | [runner.py](agents-remember/mcp/src/agents_remember/benchmarks/runner.py) |
| The route-local overview summarizes how this module fits into the benchmark runner split. | [runner_modules overview](agents-remember/mcp/src/agents_remember/benchmarks/runner_modules/overview.md) |
| Benchmark behavior is covered through the existing worktree/tool test slices. | [test_worktree_support.py](agents-remember/mcp/tests/test_worktree_support.py) |

## Cross-Repo References

No configured sibling repository is required for this module.

## Update History

- 2026-07-07T17:40+02:00 — 260707-HFX-L1 review fix B4: `filter_benchmark_provider_ids`'s
  `None` semantics flipped from unfiltered to FAIL-CLOSED (loud skip naming the escape hatch);
  the new `UNFILTERED_PROVIDERS_ENV` constant (`AR_BENCHMARK_ALLOW_UNFILTERED_PROVIDERS=1`) is
  the explicit developer act that restores an unfiltered direct-script run. Verification
  metadata pinned until closeout stamps the HFX-L1 commit.
- 2026-07-07T16:30+02:00 — 260707-HFX-L1 (provider containment R1): added
  `filter_benchmark_provider_ids` (manifest is not launch authority; skipped ids reported
  loudly; None = unfiltered direct script use) and `prepare_case` now filters before any
  workspace registration or provider launch. Verification metadata pinned until closeout stamps
  the HFX-L1 commit.
- 2026-06-19T13:42: Benchmark provider setup is now hermetic — `prepare_case` passes no seed source, so each benchmark stack indexes its own pinned fixture from scratch and never starts/clones the live workspace provider backends (task 260619: that cross-stack disturbance had cascaded a full re-embed across main + every worktree).
- 2026-05-26T02:26+02:00: Created when `benchmarks/runner.py` was split into focused implementation modules.
