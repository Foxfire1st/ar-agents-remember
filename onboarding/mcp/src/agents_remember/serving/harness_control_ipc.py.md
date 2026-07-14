# mcp/src/agents_remember/serving/harness_control_ipc.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/serving/harness_control_ipc.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-07-14T12:00+02:00 |
| lastVerifiedCommitHash | `409891a4bea54f3b6c3a125611afe54c41cca661` |
| lastVerifiedCommitDate | 2026-07-14T10:43:35+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[serving/ overview](overview.md)

## Purpose

Provides user-private Unix-domain-socket IPC for one exact-session bridge, with bounded JSON-line
requests and explicit handshake, snapshot, submit, respond, reconcile, transcript, and stop calls.

## Code Commentary

Endpoint names hash the complete control identity. Runtime directories are `0700`, sockets `0600`,
and non-socket replacements are refused. Every request validates protocol and identity before
dispatch; malformed, unknown, oversized, and wrong-session actions fail loudly. IPC exposes bridge
receipts and reconciliation without making the socket a second control authority.

## Invariants And Boundaries

- Same-user filesystem permissions are the local endpoint security boundary.
- Exact catalog/session identity is required on every request.
- Endpoint transport is replaceable behind the protocol contract.

## Repo-Internal References

| Finding | Source Path |
| --- | --- |
| Bridge served by IPC. | [harness_control_bridge.py](harness_control_bridge.py) |
| Additive endpoint metadata. | [terminal_catalog.py](terminal_catalog.py) |
| IPC regression coverage. | [test_harness_control.py](../../../tests/test_harness_control.py) |

## Update History

- 2026-07-14T12:00+02:00 — 260713-PHA-L1 curator pass: created onboarding for private exact-identity
  IPC, permissions, bounded messages, and explicit control operations.
