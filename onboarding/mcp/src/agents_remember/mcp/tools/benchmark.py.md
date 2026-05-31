# mcp/src/agents_remember/mcp/tools/benchmark.py

| Field                  | Value                                            |
| ---------------------- | ------------------------------------------------ |
| repository             | agents-remember-md                               |
| path                   | `mcp/src/agents_remember/mcp/tools/benchmark.py` |
| doc_type               | `file-level-onboarding`                          |
| lastUpdated            | 2026-05-31T12:50+02:00|
| lastVerifiedCommitHash | `c20a3292e667d227a3be0c1fb276f8a701df814f`                                        |
| lastVerifiedCommitDate | 2026-05-31T14:17:11+02:00|
| governingOverview      | `overview.md`                                    |

## Purpose

Codex benchmark prepare/run payload builders.

## Code Commentary

### Logic

Holds `codex_benchmark_prepare_payload` and `codex_benchmark_run_payload`. Each
forwards typed arguments (including the allowlisted `codex_sandbox` and skill
exposure/provider-timeout options) to the matching
`controllers.benchmark_tools` function and returns through `base._tool_payload`.
The `codex_sandbox` default is sourced from the `CODEX_BENCHMARK_SANDBOX`
constant imported from `benchmarks.runner` rather than an inline literal.

### Invariants And Boundaries

- Transport-thin: benchmark orchestration lives in
  `controllers.benchmark_tools` and the `benchmarks` package.

## Update History

- 2026-05-31T12:50+02:00 — `codex_benchmark_run_payload`'s `codex_sandbox` default changed from the inline `"danger-full-access"` literal to the `CODEX_BENCHMARK_SANDBOX` constant imported from `benchmarks.runner`; noted the new constant source in Logic (1.0.0 review remediation).
- 2026-05-29T18:35+02:00: Created from the `mcp/tools.py` domain split (commit `01f503d`).
