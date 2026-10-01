# mcp/src/agents_remember/mcp/tools/benchmark.py

## Governing Overview

[overview.md](overview.md)

## Purpose

Codex benchmark prepare/run payload builders.

## Code Commentary

### Logic

Holds `codex_benchmark_prepare_payload` and `codex_benchmark_run_payload`. Each
forwards to the matching `application.benchmark_tools` function and returns
through `base._tool_payload`.

Since 260731-EFA-L2 both take the application entry point's parameter objects rather than a keyword list:

```python
codex_benchmark_prepare_payload(config, *, selection=ALL_CASES, preparation=DEFAULT_PREPARATION)
codex_benchmark_run_payload(config, *, selection=ALL_CASES, preparation=DEFAULT_PREPARATION,
                            run=DEFAULT_RUN)
```

`BenchmarkSelection` is which cases, `BenchmarkPreparation` is how each case workspace is built
(and carries `dry_run` for **both** tools), `CodexBenchmarkRun` is the execution itself — prompt,
variant, repetitions, jobs, `skip_prepare`, `codex_sandbox`. The three defaults, the shared
`ALL_CASES`/`DEFAULT_PREPARATION`/`DEFAULT_RUN` values, and the `codex_sandbox` default
(`CODEX_BENCHMARK_SANDBOX`, not an inline literal) now live on the application entry point's dataclasses; this
module imports them rather than restating them. The published MCP signatures stay flat — packing
happens in `mcp/registration/benchmarks.py`.

### Invariants And Boundaries

- Transport-thin: benchmark orchestration lives in
  `application.benchmark_tools` and the `benchmarks` package.
