# mcp/src/agents_remember/mcp/registration/benchmarks.py

| Field                  | Value                                                         |
| ---------------------- | ------------------------------------------------------------- |
| repository             | agents-remember                                                |
| path                   | `mcp/src/agents_remember/mcp/registration/benchmarks.py`       |
| doc_type               | `file-level-onboarding`                                        |
| lastUpdated            | 2026-07-31T15:31+02:00                                         |
| lastVerifiedCommitHash | `f3115ce8603f83b7b5cbd82aa402f66ec1d8a29d`                     |
| lastVerifiedCommitDate | 2026-07-31T19:28:50+02:00|
| governingOverview      | `overview.md`                                                  |

## Governing Overview

[registration route overview](overview.md)

## Purpose

`register_benchmark_tools(server, config)` declares `codex_benchmark_prepare` and
`codex_benchmark_run`.

## Code Commentary

### Logic

These are the only two tools on the whole surface that register `dry_run=True`. Everything else is
act-by-default; a real prepare clones third-party repos and writes workspaces, and a real run
executes Codex agents, so both stay preview-first and the docstrings say why.

The bodies pack into the controller's three objects: `BenchmarkSelection(target, case_id,
benchmarks_root)` — which cases; `BenchmarkPreparation(dry_run, force_clone, skill_exposure_mode,
provider_timeout)` — how each case workspace is built; and, for run only, `CodexBenchmarkRun(prompt,
variant, repetitions, jobs, skip_prepare, codex_sandbox)` — the execution itself. Note that
`dry_run` lands on the **preparation** object for both tools.

`codex_sandbox`'s registered default is the imported `CODEX_BENCHMARK_SANDBOX` constant, not an
inline literal, and it resolves to Codex's own `default` sandbox. `danger-full-access` must be
opted into explicitly and is for trusted local runs only; the runner validates the value against its
allowlist and maps `default` to an omitted `--sandbox` argument. A real run is additionally refused
unless the MCP settings set `benchmarksEnabled`.

### Invariants And Boundaries

- Do not turn `codex_sandbox` into a generic Codex-argument surface.
- Do not flip either default to `False`; the preview-first posture is the safety property.
- Case selection, cloning, skill exposure and the Codex invocation live in
  `controllers/benchmark_tools.py` and the `benchmarks/` package.

## Repo-Internal References

| Finding | Source Path |
| --- | --- |
| The payload builders these forward to. | [tools/benchmark.py](agents-remember/mcp/src/agents_remember/mcp/tools/benchmark.py) |
| `BenchmarkSelection`, `BenchmarkPreparation`, `CodexBenchmarkRun`, and the `benchmarksEnabled` refusal. | [controllers/benchmark_tools.py](agents-remember/mcp/src/agents_remember/controllers/benchmark_tools.py) |
| `CODEX_BENCHMARK_SANDBOX` and the sandbox allowlist. | [benchmarks/runner.py](agents-remember/mcp/src/agents_remember/benchmarks/runner.py) |
| The preview default and sandbox value proved through a live server. | [test_mcp_registration_wiring.py](agents-remember/mcp/tests/test_mcp_registration_wiring.py) |

## Update History

- 2026-07-31T15:31+02:00 — 260731-EFA-L2 curator: created with the package. The two benchmark
  declarations moved out of `server.py` and now pack into `BenchmarkSelection`/`BenchmarkPreparation`/
  `CodexBenchmarkRun`. Verification metadata pinned to the pre-change commit until closeout stamps
  the L2 code commit.
