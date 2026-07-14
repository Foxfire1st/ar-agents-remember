# mcp/src/agents_remember/serving/codex_app_server_protocol.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/serving/codex_app_server_protocol.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-07-14T12:30+02:00 |
| lastVerifiedCommitHash | `bc2958ae2d90ab3d34bffde5402d2dc21100e41b`|
| lastVerifiedCommitDate | 2026-07-14T16:16:44+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[serving/ overview](overview.md)

## Purpose

Owns the bounded newline-delimited JSON-RPC stdio transport for the Codex app-server. The transport
is version-neutral; `0.144.3` is fixture/smoke evidence, while production compatibility is decided
by the structured messages and fields consumed by the session and adapter.

## Code Commentary

`CodexStdioTransport` launches the supplied command and environment unchanged, correlates request
responses, forwards notifications and server requests, and translates malformed, oversized, or
unexpected input into typed failures. It exposes a protocol surface for fake transports and the
production adapter without interpreting thread or turn semantics.

## Conventions

JSON objects are validated at the transport boundary and event delivery uses a bounded queue. The
transport does not infer compatibility from package text or provide a permissive fallback.

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

### 260713-PHA-L6 Capability Boundary

The protocol identity is `codex-app-server`; the negotiated opaque CLI token is validated from
structured initialization and thread evidence by the session layer. Exact package versions are
fixture/smoke evidence, not production protocol pins.

## Update History
- 2026-07-14T17:00:00+02:00 — 260713-PHA-L6 master-exit correction: historicized the obsolete
  exact-0.144.3 transport convention; structured initialize/thread evidence is authoritative.
- 2026-07-14T16:30:00+02:00 — 260713-PHA-L6 curator: removed the stale pinned-version description and documented
  the unversioned protocol boundary.

- 2026-07-14T12:30+02:00 — 260713-PHA-L3 curator pass: created onboarding for bounded JSON-RPC
  stdio transport, pinned protocol version, and loud failure boundaries. Verification remains
  unset until closeout stamps the code commit.
