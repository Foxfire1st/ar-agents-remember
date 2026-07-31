# mcp/src/agents_remember/controllers/benchmark_tools.py

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember                         |
| path                   | `mcp/src/agents_remember/controllers/benchmark_tools.py` |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-07-31T15:31+02:00                     |
| lastVerifiedCommitHash | `f3115ce8603f83b7b5cbd82aa402f66ec1d8a29d` |
| lastVerifiedCommitDate | 2026-07-31T19:28:50+02:00|
| governingOverview      | `overview.md`                              |

## Purpose

`benchmark_tools.py` is the controller surface for Codex benchmark preparation
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
settings). When enabled, the controller resolves optional benchmark roots
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
- The controller must not accept arbitrary Codex executable paths or free-form
  execution flags.
- Benchmark response payloads stay modeled but flexible around runner details.
- MCP-driven benchmark provider synthesis is bounded by the live on-disk
  authority (containment R1): the controller always passes
  `allowed_provider_ids` (empty on a failed read, fail-closed); direct script
  use outside the MCP is fail-closed too since review B4 unless the explicit
  `AR_BENCHMARK_ALLOW_UNFILTERED_PROVIDERS=1` env escape is set.

## Repo-Internal References

| Finding | Source Path |
| --- | --- |
| Benchmark response models define prepare/run envelopes and Codex execution policy fields. | [benchmarks.py](agents-remember/mcp/src/agents_remember/models/benchmarks.py) |
| Benchmark service behavior lives under the benchmarks package. | [runner.py](agents-remember/mcp/src/agents_remember/benchmarks/runner.py) |
| Shared coordination-confinement guard used for benchmark root overrides. | [_guards.py](agents-remember/mcp/src/agents_remember/controllers/_guards.py) |
| The live-authority reload behind `_live_provider_ids` (containment R1). | [config.py](agents-remember/mcp/src/agents_remember/mcp/config.py) |
| The workspace-side filter that consumes `allowed_provider_ids`. | [workspace.py](agents-remember/mcp/src/agents_remember/benchmarks/runner_modules/workspace.py) |
| Containment tests pin the manifest filter and the fail-closed-None + env-escape contract. | [test_provider_containment.py](agents-remember/mcp/tests/test_provider_containment.py) |

## Update History

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
