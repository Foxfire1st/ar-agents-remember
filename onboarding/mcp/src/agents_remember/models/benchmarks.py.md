# mcp/src/agents_remember/models/benchmarks.py

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember                         |
| path                   | `mcp/src/agents_remember/models/benchmarks.py` |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-08-02T01:05+02:00                     |
| lastVerifiedCommitHash | `5aff1e8f01dfa949efc8f68e46bc62a99ed31432` |
| lastVerifiedCommitDate | 2026-08-14T14:36:50+02:00|
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

| Finding | Anchor | Source |
| --- | --- | --- |
| Benchmark application entry points expose prepare/run service payloads through MCP. | `codex_benchmark_prepare_tool`, `codex_benchmark_run_tool` | mcp/src/agents_remember/application/benchmark_tools.py:64-84; mcp/src/agents_remember/application/benchmark_tools.py:87-134 |

## Update History

- 2026-08-02T16:44:57+02:00 — L6 W1-B02 curator: repaired 1 repository-internal citation for the two benchmark application entry points.
- 2026-08-02T01:05+02:00 — No content impact: `mcp/src/agents_remember/tasks/reopen.py` moved to `mcp/src/agents_remember/worktrees/reopen.py` (reopen rewrites the leaf's enclosure contract, and ranking it as a task operation made `tasks` and `worktrees` mutually dependent per `layers.toml`). Re-pointed the reference here; the behavior this document describes is unchanged. Verification metadata pinned until closeout stamps the L6 code commit.
- 2026-08-02T00:17+02:00 — No content impact: 260731-EFA-L6 renamed `mcp/src/agents_remember/controllers/` to `application/` and moved `worktrees/status.py` to `application/worktree_status.py`. Updated the references and the vocabulary here ("the application layer" for the package, "an application entry point" for one function); the behavior this document describes is unchanged. Verification metadata pinned until closeout stamps the L6 code commit.
- 2026-05-31T12:30+02:00 — Code Commentary: CodexExecutionPolicy model removed; policy block now an untyped codexExecutionPolicy dict field on CodexBenchmarkRunResponse (1.0.0 review remediation).
- 2026-05-28T19:52+02:00: Created for benchmark response contracts.
