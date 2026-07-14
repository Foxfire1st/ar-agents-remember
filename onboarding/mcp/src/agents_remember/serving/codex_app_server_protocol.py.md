# mcp/src/agents_remember/serving/codex_app_server_protocol.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/serving/codex_app_server_protocol.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-07-14T12:30+02:00 |
| lastVerifiedCommitHash | `acb308c50072d8cde0015c4828e39d12480872ed`|
| lastVerifiedCommitDate | 2026-07-14T12:32:48+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[serving/ overview](overview.md)

## Purpose

Owns the bounded newline-delimited JSON-RPC stdio transport for the pinned Codex CLI app-server.

## Code Commentary

`CodexStdioTransport` launches the supplied command and environment unchanged, correlates request
responses, forwards notifications and server requests, and translates malformed, oversized, or
unexpected input into typed failures. It exposes a protocol surface for fake transports and the
production adapter without interpreting thread or turn semantics.

## Conventions

The protocol version is pinned to `0.144.3`; JSON objects are validated at the transport boundary,
and event delivery uses a bounded queue.

## Invariants And Boundaries

- Unterminated, malformed, unknown-id, and over-limit messages fail loudly.
- Queue saturation and subprocess disconnect resolve pending callers; no resend or compatibility
  fallback belongs here.
- Launch argv, cwd, environment, and authentication are supplied by the caller and preserved.

## Todos

None known for this leaf.

## Docs References

No Domain Documentation entries are configured in the resolved source registry; the validated
protocol snapshot is recorded in the repository fixture instead.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No configured live documentation source was available for this pass. | — | — |

## Repo-Internal References

| Finding | Citations | Source Path |
| --- | --- | --- |
| Fixture pins the CLI version, protocol, and stable method inventory. | L1-L31 | [codex_app_server_0_144_3.json](../../../../tests/fixtures/codex_app_server_0_144_3.json) |
| Adapter consumes the transport and reduces protocol events. | L63-L128; L315-L326 | [codex_app_server_adapter.py](codex_app_server_adapter.py) |

## Cross-Repo References

The transport is an external-process boundary to the installed Codex CLI.

| Finding | Citations | Source Path |
| --- | --- | --- |
| PASS review confirms the pinned stable-only protocol boundary. | L22-L30 | [260713-PHA-L3-reviewer-verdict.md](../../../../../../../../../../../../ar-coordination/tasks/agents-remember/260713_protocol-backed-harness-adapters/notes/reports/260713-PHA-L3-reviewer-verdict.md) |

## Update History

- 2026-07-14T12:30+02:00 — 260713-PHA-L3 curator pass: created onboarding for bounded JSON-RPC
  stdio transport, pinned protocol version, and loud failure boundaries. Verification remains
  unset until closeout stamps the code commit.
