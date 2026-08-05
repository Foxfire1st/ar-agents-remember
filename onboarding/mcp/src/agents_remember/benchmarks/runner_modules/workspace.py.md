# mcp/src/agents_remember/benchmarks/runner_modules/workspace.py

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember                         |
| path                   | `mcp/src/agents_remember/benchmarks/runner_modules/workspace.py` |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-07-31T00:00+02:00                     |
| lastVerifiedCommitHash | `5920ea2b4bdd5d5ee969ae064ff9a8e1fc6b4060` |
| lastVerifiedCommitDate | 2026-08-05T12:41:24+02:00|
| governingOverview      | `overview.md`                              |

## Governing Overview

[runner_modules overview](overview.md)

## Purpose

Benchmark workspace and repository preparation orchestration.

## Code Commentary

### 260731-EFA-L2 Preparation And Workspace Objects

`prepare_case(preparation, case, *, provider_ids=())` takes a `BenchmarkPreparation` in place of
`benchmarks_root` plus the five preparation keywords (`dry_run`, `skill_exposure_mode`,
`force_clone`, `provider_timeout`, `allowed_provider_ids`). The containment R1 filter still runs
first — `filter_benchmark_provider_ids(case.case_id, provider_ids, preparation.allowed_provider_ids)`
— so the authority set reaches it through the preparation object rather than a loose keyword.

Once the roots are laid down, `prepare_case` builds one **`BenchmarkWorkspace`** (case, with-memory
root, coordination root, source repo root, memory repo, filtered provider ids) and hands that whole
object to `write_benchmark_mcp_registration(workspace, *, provider_timeout, dry_run)` and
`prepare_configured_providers(workspace, *, dry_run, provider_timeout)`. That is the point: the
registration written to disk and the providers launched against it are now guaranteed to describe
the same materialized workspace.

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

| Finding | Anchor | Source |
| --- | --- | --- |
| The public benchmark facade re-exports this module's public functions and classes for compatibility. | `prepare_repo` | mcp/src/agents_remember/benchmarks/runner.py:28-33 |
| The route-local overview summarizes how this module fits into the benchmark runner split. | `# mcp/src/agents_remember/benchmarks/runner_modules Overview` | onboarding/mcp/src/agents_remember/benchmarks/runner_modules/overview.md:1-137 |
| Benchmark behavior is covered through the existing worktree/tool test slices. | `BenchmarkRunnerPortabilityTests` | mcp/tests/test_worktree_support.py:3052-3680 |

## Cross-Repo References

No configured sibling repository is required for this module.

## Update History

- 2026-08-02T16:45:41+02:00 — 260731-EFA-L6 curator W1-B10: repaired 6 citation findings (3 rows); scoped recheck clean.

- 2026-07-31T00:00+02:00 — 260731-EFA-L2 (gate honesty, `PLR0913` armed with no exemptions):
  `prepare_case` was re-signed onto `BenchmarkPreparation`, and it now builds a
  `BenchmarkWorkspace` that both `write_benchmark_mcp_registration` and
  `prepare_configured_providers` consume. The materialized workspace and the written registration
  are unchanged. Verification metadata pinned until closeout stamps the L2 commit.
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
