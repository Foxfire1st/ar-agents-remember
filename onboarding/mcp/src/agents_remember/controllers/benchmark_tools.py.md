# mcp/src/agents_remember/controllers/benchmark_tools.py

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember-md                         |
| path                   | `mcp/src/agents_remember/controllers/benchmark_tools.py` |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-05-28T19:52+02:00                     |
| lastVerifiedCommitHash | `bf3a3c4e310fb11032da885083d026a74a31ee9c` |
| lastVerifiedCommitDate | 2026-05-28T20:06:49+02:00|
| governingOverview      | `overview.md`                              |

## Purpose

`benchmark_tools.py` is the controller surface for Codex benchmark preparation
and benchmark run MCP tools.

## Code Commentary

The controller resolves optional benchmark roots inside the coordination root,
temporarily sets benchmark root context when needed, and delegates to the
package benchmark runner. It preserves the benchmark-only Codex execution
policy and sandbox allowlist behavior owned by the benchmark service.

## Invariants And Boundaries

- Benchmark root overrides must be coordination-contained.
- The controller must not accept arbitrary Codex executable paths or free-form
  execution flags.
- Benchmark response payloads stay modeled but flexible around runner details.

## Repo-Internal References

| Finding | Source Path |
| --- | --- |
| Benchmark response models define prepare/run envelopes and Codex execution policy fields. | [benchmarks.py](agents-remember-md/mcp/src/agents_remember/models/benchmarks.py) |
| Benchmark service behavior lives under the benchmarks package. | [runner.py](agents-remember-md/mcp/src/agents_remember/benchmarks/runner.py) |

## Update History

- 2026-05-28T19:52+02:00: Created when benchmark MCP controllers moved into their own domain module.
