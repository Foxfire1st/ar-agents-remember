# mcp/tests/test_pi_rpc_adapter.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/test_pi_rpc_adapter.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-07-14T12:17+02:00 |
| lastVerifiedCommitHash | `d5f8edf0ccab21f1cf71723615e394eba40fcebc` |
| lastVerifiedCommitDate | 2026-07-14T12:29:36+02:00|
| governingOverview | `../overview.md` |

## Governing Overview
[mcp/tests overview](../overview.md)

## Purpose
Fake-transport and adapter conformance coverage for the Pi RPC protocol-backed L1 adapter.

## Code Commentary
Protocol tests pin LF-only framing, malformed/overlong refusal, launch preservation, and
capability policy. Async adapter tests cover handshake/state, source-specific busy queueing,
retry/compaction/settled completion, extension UI and bounds, disconnect before/after ack,
reconnect by session identity, cursor reconciliation without resend, and loud malformed transport
failure.

## Invariants And Boundaries
- Fake transports isolate adapter semantics without vendor registration.
- Ambiguous sends reconcile from durable cursor evidence and never resend automatically.
- The suite preserves the L1 normalized contract and no-fallback boundary.

## Repo-Internal References
| Finding | Source Path |
| --- | --- |
| Adapter under test. | [pi_rpc_adapter.py](../src/agents_remember/serving/pi_rpc_adapter.py) |
| Protocol/event seams. | [pi_rpc_protocol.py](../src/agents_remember/serving/pi_rpc_protocol.py), [pi_rpc_events.py](../src/agents_remember/serving/pi_rpc_events.py) |
| Pinned policy fixture. | [0.80.6-capabilities.json](fixtures/pi_rpc/0.80.6-capabilities.json) |

## Cross-Repo References
No meaningful cross-repo references found.

## Update History
- 2026-07-14T12:17+02:00 — 260713-PHA-L4 curator: created onboarding for Pi fake adapter,
  protocol, activity, extension UI, disconnect, and reconciliation coverage.
