# mcp/src/agents_remember/benchmarks/runner_modules/mcp_registration.py

## Governing Overview

[runner_modules overview](overview.md)

## Purpose

Benchmark-local MCP/Codex registration and generated provider setup settings.

## Code Commentary

### 260731-EFA-L2 Workspace-Object Signatures

`benchmark_mcp_config(workspace)`, `benchmark_lifecycle_settings(workspace)`,
`write_benchmark_mcp_registration(workspace, *, provider_timeout, dry_run)` and
`prepare_configured_providers(workspace, *, dry_run, provider_timeout)` all take one
`BenchmarkWorkspace` (from `models.py`) in place of the case/roots/provider-ids keyword lists. The
new `benchmark_repo_id(case)` names the per-case repo id these builders derive. Everything written
— `.codex/mcp` settings, `.codex/config.toml`, the generated lifecycle settings and their
`timeoutCaps` — is unchanged, as is the no-seed-options / `cgc_refresh_fallback=True` provider
setup call.

### Logic

`mcp_registration.py` writes `.codex/mcp` settings and `.codex/config.toml`,
builds benchmark `McpRuntimeConfig`/lifecycle settings, names provider
containers per case, derives benchmark transcript roots under `logs/mcp`,
derives provider log roots under `logs/providers/<provider>/<instance>`, and
calls package-local provider setup with generated settings. Generated
`timeoutCaps` use the current `providerSetupSeconds` key (renamed from
`providerSeconds`). `prepare_configured_providers` runs `run_provider_setup`
with **no seed options** — it takes only `provider_ids` and never wires
`cgc_seed`/`grepai_seed` — so a benchmark builds each provider index cold from
its own generated settings and never touches another coordination root. It
opts INTO `cgc_refresh_fallback=True` (260707-HFX-L2 review): hermetic-cold
needs the synchronous, timeout-bounded graph build — with the fleet default
now off, `cgc watch` would self-index asynchronously and the benchmarked
agent would query a half-built graph errorlessly.

`disarm_stale_benchmark_registrations(benchmarks_root, allowed_provider_ids)`
(containment R1, 260707-HFX-L1 review B3) narrows persisted benchmark MCP
settings to the live authority set. The registration written at prepare time
persists in the workspace and acts as the AUTHORITY file for every session
later booted there — the one place the fleet kill-switch cannot reach, because
those servers re-read *this* file, not the developer's. Any prepare/run pass
(the `services.py` entry points call it first) therefore sweeps ALL workspace
registrations — `workspaces/*/<CODEX_HARNESS_DIR>/mcp/<BENCHMARK_MCP_SETTINGS_NAME>`
at one and two directory levels under `workspaces/` — strips providers the
live authority no longer enables, rewrites the file (sorted, indented),
reports each rewrite loudly, and returns the rewritten paths. The sweep is
idempotent (an already-narrowed file is untouched), skips unreadable or
non-object files, and `allowed_provider_ids=None` (no authority context,
direct script use) leaves every file untouched.

### Invariants And Boundaries

- Benchmark provider authority comes from generated MCP/provider settings, not coordinator `system/settings.json`.
- Benchmark provider instances should use the same central `logs/` layout as
  workspace and worktree provider instances.
- Temporary provider settings must be deleted after setup attempts.
- Benchmark provider setup is hermetic-cold: `prepare_configured_providers`
  exposes no seed-source parameter and wires no seed options, so a benchmark can
  never start or clone the live workspace provider backends (task 260619). The
  former `default_cgc_seed_source_coordination_root` helper (which resolved the
  live workspace as the seed source) was removed.
- Benchmark prepare keeps `cgc_refresh_fallback=True`: the hermetic-cold path
  depends on the synchronous bounded refresh building the whole graph before
  the run; an async self-indexing watcher would hand the benchmarked agent a
  half-built graph with no error (260707-HFX-L2 review).
- Persisted workspace registrations must be re-narrowed to the live authority
  on every prepare/run pass (containment R1, review B3): the sweep is
  idempotent, reports loudly per rewritten file, and `None` (no authority
  context) leaves files untouched.

## Evidence

### Docs References

No external Domain Documentation source is configured for this memory repo.

### Repo-Internal References

- The public benchmark facade re-exports this module's public functions and classes for compatibility. [1]
- The route-local overview summarizes how this module fits into the benchmark runner split. [2]
- The shared seed resolvers also refuse a benchmark-scoped target as defense-in-depth. [3]
- The service entry points open every prepare/run pass with the registration sweep. [4]

### Cross-Repo References

No configured sibling repository is required for this module.
