# mcp/src/agents_remember/benchmarks/runner_modules/workspace.py

## Governing Overview

[runner_modules overview](overview.md)

## Purpose

Benchmark workspace and repository preparation orchestration.

## Code Commentary

### 260731-EFA-L2 Preparation And Workspace Objects

At this migration, `prepare_case(preparation, case, *, provider_ids=())` took a `BenchmarkPreparation` in place of
`benchmarks_root` plus the five then-present preparation keywords (`dry_run`, `skill_exposure_mode`,
`force_clone`, `provider_timeout`, `allowed_provider_ids`). The current object has the root plus four preparation keywords: `dry_run`, `force_clone`, `provider_timeout` and `allowed_provider_ids`; `skill_exposure_mode` is retired. The containment R1 filter still runs
first — `filter_benchmark_provider_ids(case.case_id, provider_ids, preparation.allowed_provider_ids)`
— so the authority set reaches it through the preparation object rather than a loose keyword.

Once the roots are laid down, `prepare_case` builds one **`BenchmarkWorkspace`** (case, with-memory
root, coordination root, source repo root, memory repo, filtered provider ids) and hands that whole
object to `write_benchmark_mcp_registration(workspace, *, provider_timeout, dry_run)` and
`prepare_configured_providers(workspace, *, dry_run, provider_timeout)`. That is the point: the
registration written to disk and the retained setup call receive the same materialized workspace.
That shared input does not guarantee a provider launch: the current lifecycle-settings generator
emits a disabled, empty provider map.

### Logic

`workspace.py` derives source-only and with-memory workspace paths, prepares Git checkouts, renders benchmark AGENTS files, syncs runtime assets, writes MCP registration, prepares memory repos, and invokes configured provider setup. `prepare_case` calls `prepare_configured_providers` with no seed source. The retained call receives the shared generator's disabled, empty lifecycle settings, so it no longer establishes that each benchmark builds an index from its pinned fixture. The no-seeding boundary still prevents using the live workspace as a seed source.

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

## Evidence

### Docs References

No external Domain Documentation source is configured for this memory repo.

### Repo-Internal References


- The shared BenchmarkWorkspace is passed to registration and retained setup after authority filtering. Setup receives lifecycle_settings_from_config through benchmark_lifecycle_settings; that generator returns disabled empty provider settings, so the call establishes neither a provider launch nor a from-scratch benchmark index-build promise. No live-workspace seed source is wired. [5]


- The public benchmark facade re-exports this module's public functions and classes for compatibility. [1]
The [route overview](overview.md) describes the benchmark runner split; it is a discovery companion rather than a repository source target.

### Cross-Repo References

No configured sibling repository is required for this module.

## Preparation writes no skill exposure

`prepare_case` syncs the runtime assets and no longer calls `sync_workspace_skill_exposure`, and no preparation object carries a skill-exposure mode: the workspace's harness reads the skills the tool server serves from its package copy, through the benchmark-local MCP registration this workspace writes.

- The case preparation that lays down assets and no skill exposure. [3]

- Current source account and its stated boundaries. [4]
