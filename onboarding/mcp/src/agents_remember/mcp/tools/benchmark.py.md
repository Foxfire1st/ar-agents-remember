# mcp/src/agents_remember/mcp/tools/benchmark.py

## Current operative account — MIK-R112

The current source facts below replace the former operative inventory. The separately labelled superseded claims describe only the pre-repair card. Original paragraphs, dated closures, evidence and citation identities remain intact in the explicitly historical section; they grant no current call, restored route or fresh execution acceptance.

- HEAD diff deletes the entire named source file.

### Superseded inventory

- Pre-repair card claim: Card describes current Codex benchmark payload builders and flat MCP signatures. This is superseded archival wording, not a current prescription.

### Source and authority bounds

- Source comparison: `mcp/src/agents_remember/mcp/tools/benchmark.py (absent; git diff HEAD -- this path: deleted file mode 100644)`.

Source inspection supplies no new test, native-host, whole-build, landing or memory acceptance. Retained internal services and historical fixtures do not re-advertise deleted MCP tools. Numbered references retain historical custody and may include disclosed inherited stale targets; currentness or proof truth is not inferred from them.

## Historical original card — preserved, not the current operative account

<details>
<summary>Retained original source accounts and producer history</summary>

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

</details>
