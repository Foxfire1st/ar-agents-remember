# mcp/src/agents_remember/controllers/benchmark_tools.py

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember-md                         |
| path                   | `mcp/src/agents_remember/controllers/benchmark_tools.py` |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-05-31T12:30+02:00                     |
| lastVerifiedCommitHash | `c20a3292e667d227a3be0c1fb276f8a701df814f` |
| lastVerifiedCommitDate | 2026-05-31T14:17:11+02:00|
| governingOverview      | `overview.md`                              |

## Purpose

`benchmark_tools.py` is the controller surface for Codex benchmark preparation
and benchmark run MCP tools.

## Code Commentary

Both benchmark tools short-circuit with a disabled-tools error unless
`config.benchmarks_enabled` is set (via `"benchmarksEnabled": true` in MCP
settings). When enabled, the controller resolves optional benchmark roots
inside the coordination root via the shared `require_within_coordination`
guard, temporarily sets benchmark root context when needed, and delegates to
the package benchmark runner. It preserves the benchmark-only Codex execution
policy and sandbox allowlist behavior owned by the benchmark service.

## Invariants And Boundaries

- Benchmark tools are disabled unless `benchmarks_enabled` is set; the gate is enforced before any benchmark work runs.
- Benchmark root overrides must be coordination-contained, enforced through the shared `require_within_coordination` guard (raises `AuthorityError` on escape).
- The controller must not accept arbitrary Codex executable paths or free-form
  execution flags.
- Benchmark response payloads stay modeled but flexible around runner details.

## Repo-Internal References

| Finding | Source Path |
| --- | --- |
| Benchmark response models define prepare/run envelopes and Codex execution policy fields. | [benchmarks.py](agents-remember-md/mcp/src/agents_remember/models/benchmarks.py) |
| Benchmark service behavior lives under the benchmarks package. | [runner.py](agents-remember-md/mcp/src/agents_remember/benchmarks/runner.py) |
| Shared coordination-confinement guard used for benchmark root overrides. | [_guards.py](agents-remember-md/mcp/src/agents_remember/controllers/_guards.py) |

## Update History

- 2026-05-31T12:30+02:00 — Documented benchmarks_enabled disabled-tools gate and switch to shared require_within_coordination guard (1.0.0 review remediation).
- 2026-05-28T19:52+02:00: Created when benchmark MCP controllers moved into their own domain module.
