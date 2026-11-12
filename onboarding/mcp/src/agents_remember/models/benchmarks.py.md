# mcp/src/agents_remember/models/benchmarks.py

## Governing Overview

[overview.md](overview.md)

## Purpose

`benchmarks.py` retains response models for Codex benchmark preparation and run payloads.
Their MCP entrypoints were removed; model presence does not advertise a callable tool.

## Code Commentary

Benchmark responses use flexible tool envelopes because benchmark service
payloads include progress messages, executable resolution data, and benchmark
execution policy details. The Codex-specific policy block (sandbox and `PATH`
resolution behavior) is carried on `CodexBenchmarkRunResponse` as the untyped
`codexExecutionPolicy: dict[str, Any] | None` field rather than a dedicated model.

## Invariants And Boundaries

- Benchmark responses must remain Codex-specific and benchmark-labeled.
- Do not turn benchmark payloads into a generic command execution tunnel.

## Evidence

### Repo-Internal References
