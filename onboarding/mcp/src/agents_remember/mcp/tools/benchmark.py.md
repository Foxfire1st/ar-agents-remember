# mcp/src/agents_remember/mcp/tools/benchmark.py

| Field                  | Value                                            |
| ---------------------- | ------------------------------------------------ |
| repository             | agents-remember-md                               |
| path                   | `mcp/src/agents_remember/mcp/tools/benchmark.py` |
| doc_type               | `file-level-onboarding`                          |
| lastUpdated            | 2026-05-29T18:35+02:00|
| lastVerifiedCommitHash | `01f503dcba3a6eacc1587941f6a89fce0bcc72a2`                                        |
| lastVerifiedCommitDate | 2026-05-29T18:32:57+02:00|
| governingOverview      | `overview.md`                                    |

## Purpose

Codex benchmark prepare/run payload builders.

## Code Commentary

### Logic

Holds `codex_benchmark_prepare_payload` and `codex_benchmark_run_payload`. Each
forwards typed arguments (including the allowlisted `codex_sandbox` and skill
exposure/provider-timeout options) to the matching
`controllers.benchmark_tools` function and returns through `base._tool_payload`.

### Invariants And Boundaries

- Transport-thin: benchmark orchestration lives in
  `controllers.benchmark_tools` and the `benchmarks` package.

## Update History

- 2026-05-29T18:35+02:00: Created from the `mcp/tools.py` domain split (commit `01f503d`).
