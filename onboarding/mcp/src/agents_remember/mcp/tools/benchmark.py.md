# mcp/src/agents_remember/mcp/tools/benchmark.py

| Field                  | Value                                            |
| ---------------------- | ------------------------------------------------ |
| repository             | agents-remember                               |
| path                   | `mcp/src/agents_remember/mcp/tools/benchmark.py` |
| doc_type               | `file-level-onboarding`                          |
| lastUpdated            | 2026-08-02T01:05+02:00|
| lastVerifiedCommitHash | `5aff1e8f01dfa949efc8f68e46bc62a99ed31432`                                        |
| lastVerifiedCommitDate | 2026-08-14T14:36:50+02:00|
| governingOverview      | `overview.md`                                    |

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

## Update History

- 2026-08-08T17:18+02:00 — No content impact: 260731-EFA-L9 rewrote this source's imports/callers only (model-extraction caller wave); the behavior this card documents is unchanged and the body was re-verified current. Verification metadata pinned until closeout stamps the L9 code commit.

- 2026-08-02T01:05+02:00 — No content impact: `mcp/src/agents_remember/tasks/reopen.py` moved to `mcp/src/agents_remember/worktrees/reopen.py` (reopen rewrites the leaf's enclosure contract, and ranking it as a task operation made `tasks` and `worktrees` mutually dependent per `layers.toml`). Re-pointed the reference here; the behavior this document describes is unchanged. Verification metadata pinned until closeout stamps the L6 code commit.
- 2026-08-02T00:17+02:00 — No content impact: 260731-EFA-L6 renamed `mcp/src/agents_remember/controllers/` to `application/` and moved `worktrees/status.py` to `application/worktree_status.py`. Updated the references and the vocabulary here ("the application layer" for the package, "an application entry point" for one function); the behavior this document describes is unchanged. Verification metadata pinned until closeout stamps the L6 code commit.
- 2026-07-31T15:31+02:00 — 260731-EFA-L2: both builders took `selection`/`preparation` (and run's
  `run`) parameter objects; the `CODEX_BENCHMARK_SANDBOX` import moved to the controller, which now
  owns the default on `CodexBenchmarkRun`. Verification metadata pinned until closeout stamps the L2
  code commit.
- 2026-05-31T12:50+02:00 — `codex_benchmark_run_payload`'s `codex_sandbox` default changed from the inline `"danger-full-access"` literal to the `CODEX_BENCHMARK_SANDBOX` constant imported from `benchmarks.runner`; noted the new constant source in Logic (1.0.0 review remediation).
- 2026-05-29T18:35+02:00: Created from the `mcp/tools.py` domain split (commit `01f503d`).
