# mcp/src/agents_remember/models/benchmarks.py

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember                         |
| path                   | `mcp/src/agents_remember/models/benchmarks.py` |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-05-31T12:30+02:00                     |
| lastVerifiedCommitHash | `c20a3292e667d227a3be0c1fb276f8a701df814f` |
| lastVerifiedCommitDate | 2026-05-31T14:17:11+02:00|
| governingOverview      | `overview.md`                              |

## Purpose

`benchmarks.py` defines response models for Codex benchmark preparation and run
tools.

## Code Commentary

Benchmark responses use flexible tool envelopes because benchmark service
payloads include progress messages, executable resolution data, and benchmark
execution policy details. The Codex-specific policy block (sandbox and `PATH`
resolution behavior) is carried on `CodexBenchmarkRunResponse` as the untyped
`codexExecutionPolicy: dict[str, Any] | None` field rather than a dedicated model.

## Invariants And Boundaries

- Benchmark responses must remain Codex-specific and benchmark-labeled.
- Do not turn benchmark payloads into a generic command execution tunnel.

## Repo-Internal References

| Finding | Source Path |
| --- | --- |
| Benchmark controllers expose prepare/run service payloads through MCP. | [benchmark_tools.py](agents-remember/mcp/src/agents_remember/controllers/benchmark_tools.py) |

## Update History

- 2026-05-31T12:30+02:00 — Code Commentary: CodexExecutionPolicy model removed; policy block now an untyped codexExecutionPolicy dict field on CodexBenchmarkRunResponse (1.0.0 review remediation).
- 2026-05-28T19:52+02:00: Created for benchmark response contracts.
