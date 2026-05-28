# mcp/src/agents_remember/models/benchmarks.py

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember-md                         |
| path                   | `mcp/src/agents_remember/models/benchmarks.py` |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-05-28T19:52+02:00                     |
| lastVerifiedCommitHash | `bf3a3c4e310fb11032da885083d026a74a31ee9c` |
| lastVerifiedCommitDate | 2026-05-28T20:06:49+02:00|
| governingOverview      | `overview.md`                              |

## Purpose

`benchmarks.py` defines response models for Codex benchmark preparation and run
tools.

## Code Commentary

Benchmark responses use flexible tool envelopes because benchmark service
payloads include progress messages, executable resolution data, and benchmark
execution policy details. `CodexExecutionPolicy` models the Codex-specific
policy block used when reporting sandbox and `PATH` resolution behavior.

## Invariants And Boundaries

- Benchmark responses must remain Codex-specific and benchmark-labeled.
- Do not turn benchmark payloads into a generic command execution tunnel.

## Repo-Internal References

| Finding | Source Path |
| --- | --- |
| Benchmark controllers expose prepare/run service payloads through MCP. | [benchmark_tools.py](agents-remember-md/mcp/src/agents_remember/controllers/benchmark_tools.py) |

## Update History

- 2026-05-28T19:52+02:00: Created for benchmark response contracts.
