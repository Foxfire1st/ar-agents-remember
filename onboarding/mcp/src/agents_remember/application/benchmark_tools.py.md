# mcp/src/agents_remember/application/benchmark_tools.py

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember                         |
| path                   | `mcp/src/agents_remember/application/benchmark_tools.py` |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-08-02T01:05+02:00                     |
| lastVerifiedCommitHash | `5920ea2b4bdd5d5ee969ae064ff9a8e1fc6b4060` |
| lastVerifiedCommitDate | 2026-08-05T12:41:24+02:00|
| governingOverview      | `overview.md`                              |

## Purpose

`benchmark_tools.py` is the application entry point surface for Codex benchmark preparation
and benchmark run MCP tools.

## Code Commentary

### Parameter Objects (260731-EFA-L2)

This module now owns the three concepts a benchmark call is made of, each with a shared default:

- `BenchmarkSelection(target, case_id, benchmarks_root)` — which cases an operation acts on
  (`ALL_CASES`: every case in the default benchmarks root).
- `BenchmarkPreparation(dry_run, force_clone, skill_exposure_mode, provider_timeout)` — how each
  selected case's workspace is built before it can run (`DEFAULT_PREPARATION`: plan-only, cached
  clones, copied skills). `dry_run` lives here for **both** tools.
- `CodexBenchmarkRun(prompt, variant, repetitions, jobs, skip_prepare, codex_sandbox)` — one Codex
  execution over the prepared cases (`DEFAULT_RUN`). Its `codex_sandbox` default is
  `benchmark_runner.CODEX_BENCHMARK_SANDBOX`, so the sandbox default lives beside the field it
  belongs to rather than being restated at each call site.

`codex_benchmark_prepare_tool(config, *, selection, preparation)` and
`codex_benchmark_run_tool(config, *, selection, preparation, run)` unpack these onto the runner's
own `BenchmarkPrepareRequest` / `BenchmarkRunRequest`.

Both benchmark tools short-circuit with a disabled-tools error unless
`config.benchmarks_enabled` is set (via `"benchmarksEnabled": true` in MCP
settings). When enabled, the application entry point resolves optional benchmark roots
inside the coordination root via the shared `require_within_coordination`
guard, temporarily sets benchmark root context when needed, and delegates to
the package benchmark runner. It preserves the benchmark-only Codex execution
policy and sandbox allowlist behavior owned by the benchmark service.

Both request payloads carry `allowed_provider_ids=_live_provider_ids(config)`
(containment R1, 260707-HFX-L1): the sorted provider ids of the live on-disk
authority, re-read per call through `reload_provider_authority`. A fail-closed
read error yields an empty set, so no case manifest can arm providers the
developer has disabled on disk — the filter itself is applied downstream by
`runner_modules/workspace.filter_benchmark_provider_ids` before any workspace
registration or provider launch.

## Invariants And Boundaries

- Benchmark tools are disabled unless `benchmarks_enabled` is set; the gate is enforced before any benchmark work runs.
- Benchmark root overrides must be coordination-contained, enforced through the shared `require_within_coordination` guard (raises `AuthorityError` on escape).
- The application entry point must not accept arbitrary Codex executable paths or free-form
  execution flags.
- Benchmark response payloads stay modeled but flexible around runner details.
- MCP-driven benchmark provider synthesis is bounded by the live on-disk
  authority (containment R1): the application entry point always passes
  `allowed_provider_ids` (empty on a failed read, fail-closed); direct script
  use outside the MCP is fail-closed too since review B4 unless the explicit
  `AR_BENCHMARK_ALLOW_UNFILTERED_PROVIDERS=1` env escape is set.

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| Benchmark response models define prepare/run envelopes and Codex execution policy fields. | `CodexBenchmarkPrepareResponse` | mcp/src/agents_remember/models/benchmarks.py:16-28 |
| Benchmark service behavior lives under the benchmarks package. | "Compatibility facade for Agents Remember benchmark prepare/run/analyze tools." | mcp/src/agents_remember/benchmarks/runner.py:1-25 |
| Shared coordination-confinement guard used for benchmark root overrides. | `require_within_coordination` | mcp/src/agents_remember/kernel/authority.py:27-35 |
| The live-authority reload behind `_live_provider_ids` (containment R1). | `_live_provider_ids` | mcp/src/agents_remember/application/benchmark_tools.py:137-144 |
| The workspace-side filter that consumes `allowed_provider_ids`. | `filter_benchmark_provider_ids` | mcp/src/agents_remember/benchmarks/runner_modules/workspace.py:205-238 |
| Containment tests pin the manifest filter and the fail-closed-None + env-escape contract. | `BenchmarkProviderFilterTests` | mcp/tests/test_provider_containment.py:209-273 |

## Update History

- 2026-08-04T18:40+02:00 — 260731-EFA-L6 S18-B18 curator: normalized the 5 citation rows and
  retargeted the removed `_guards.py` link to the guard's current home
  (`kernel/authority.py:27-35`). Zero findings remain.

- 2026-08-02T01:05+02:00 — No content impact: `mcp/src/agents_remember/tasks/reopen.py` moved to `mcp/src/agents_remember/worktrees/reopen.py` (reopen rewrites the leaf's enclosure contract, and ranking it as a task operation made `tasks` and `worktrees` mutually dependent per `layers.toml`). Re-pointed the reference here; the behavior this document describes is unchanged. Verification metadata pinned until closeout stamps the L6 code commit.
- 2026-08-02T00:17+02:00 — 260731-EFA-L6 curator: source moved. `mcp/src/agents_remember/controllers/` was renamed to `application/`, so this sidecar moved with its source; path metadata and every in-body path follow, and the prose adopts "the application layer" / "an application entry point" for what it used to call a controller. Behavior is unchanged. Verification metadata pinned until closeout stamps the L6 code commit.
- 2026-07-31T15:31+02:00 — 260731-EFA-L2: added `BenchmarkSelection`, `BenchmarkPreparation` and
  `CodexBenchmarkRun` (with `ALL_CASES` / `DEFAULT_PREPARATION` / `DEFAULT_RUN`) and moved both
  controllers' keyword lists onto them; the `codex_sandbox` default now sits on
  `CodexBenchmarkRun`. The `benchmarksEnabled` gate, coordination containment and live-provider
  filtering are unchanged. Verification metadata pinned until closeout stamps the L2 code commit.
- 2026-07-07T17:40+02:00 — 260707-HFX-L1 review fix B4 (downstream): the workspace filter's
  `None` semantics flipped to fail-closed with the `AR_BENCHMARK_ALLOW_UNFILTERED_PROVIDERS=1`
  env escape; this controller's behavior is unchanged (it always passes the live set) — the
  direct-script invariant wording updated to match. Verification metadata pinned until closeout
  stamps the HFX-L1 commit.
- 2026-07-07T16:30+02:00 — 260707-HFX-L1 (provider containment R1): added `_live_provider_ids`
  (the live on-disk authority's sorted provider ids; fail-closed empty set on a read error) and
  both benchmark requests now carry `allowed_provider_ids`, so a case manifest can never arm
  providers disabled on disk. Verification metadata pinned until closeout stamps the HFX-L1
  commit.
- 2026-05-31T12:30+02:00 — Documented benchmarks_enabled disabled-tools gate and switch to shared require_within_coordination guard (1.0.0 review remediation).
- 2026-05-28T19:52+02:00: Created when benchmark MCP controllers moved into their own domain module.
