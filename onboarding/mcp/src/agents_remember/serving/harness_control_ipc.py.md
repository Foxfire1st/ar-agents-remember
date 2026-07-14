# mcp/src/agents_remember/serving/harness_control_ipc.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/serving/harness_control_ipc.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-07-14T17:52:13+02:00 |
| lastVerifiedCommitHash | `e35584a2efec5f2b4eb5ac7c4ee9a129757c92b0` |
| lastVerifiedCommitDate | 2026-07-14T17:54:34+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[serving/ overview](overview.md)

## Purpose

Provides user-private Unix-domain-socket IPC for one exact-session bridge, with bounded JSON-line
requests and explicit handshake, snapshot, submit, respond, reconcile, transcript, and stop calls.

## Code Commentary

Endpoint names hash the complete control identity. Runtime directories are `0700`, sockets `0600`,
and non-socket replacements are refused. Every request validates protocol and identity before
dispatch; malformed, unknown, oversized, and wrong-session actions fail loudly. After accepted
dispatch, the response lifecycle contains only peer-loss `BrokenPipeError` and
`ConnectionResetError` from `writer.write`/`drain` and cleanup `close`/`wait_closed`; a client
timeout cannot become an unhandled loop exception. IPC exposes bridge receipts and reconciliation
without making the socket a second control authority.

## Invariants And Boundaries

- Same-user filesystem permissions are the local endpoint security boundary.
- Exact catalog/session identity is required on every request.
- Dispatch, identity, protocol, request validation, serialization, cancellation, and unrelated
  failures remain authoritative and loud. Only the two concrete peer-disconnect classes are
  contained after accepted dispatch; this is not a broad connection-error or fallback boundary.
- A delayed reply disconnect leaves an ambiguous accepted submission reconcilable through the bridge;
  it does not retry or silently degrade the request.
- Endpoint transport is replaceable behind the protocol contract.

## Repo-Internal References

| Finding | Source Path |
| --- | --- |
| Bridge served by IPC. | [harness_control_bridge.py](harness_control_bridge.py) |
| Additive endpoint metadata. | [terminal_catalog.py](terminal_catalog.py) |
| IPC regression coverage. | [test_harness_control.py](../../../tests/test_harness_control.py) |

## Update History
- 2026-07-14T17:52:13+02:00 — 260713-PHA-L6 curator: documented narrow post-dispatch peer-disconnect
  containment during reply and close lifecycle, with delayed-reply reconciliation preserved.

- 2026-07-14T12:00+02:00 — 260713-PHA-L1 curator pass: created onboarding for private exact-identity
  IPC, permissions, bounded messages, and explicit control operations.
