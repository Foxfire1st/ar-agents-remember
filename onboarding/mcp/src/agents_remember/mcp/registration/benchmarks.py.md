# mcp/src/agents_remember/mcp/registration/benchmarks.py

## Governing Overview

[registration route overview](overview.md)

## 260731-EFA-L8 Change

The tool-registration functions gained bare-`*` keyword-only signatures (the 19
PLR0917 fixes across `mcp/registration/*.py`); the rule stays enabled and call sites
already pass keywords. Registered tools are unchanged.

## Purpose

`register_benchmark_tools(server, config)` declares `codex_benchmark_prepare` and
`codex_benchmark_run`.

## Code Commentary

### Logic

Both benchmark tools register `dry_run=True`; a real prepare clones third-party repos and writes workspaces, and a real run
executes Codex agents, so both stay preview-first and the docstrings say why.

The bodies pack into the application entry point's three objects: `BenchmarkSelection(target, case_id,
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
  `application/benchmark_tools.py` and the `benchmarks/` package.

## Evidence

### Repo-Internal References

- The payload builders these forward to. [1]
- `BenchmarkSelection`, `BenchmarkPreparation`, `CodexBenchmarkRun`, and the `benchmarksEnabled` refusal. [2]
- `CODEX_BENCHMARK_SANDBOX` and the sandbox allowlist. [3]
