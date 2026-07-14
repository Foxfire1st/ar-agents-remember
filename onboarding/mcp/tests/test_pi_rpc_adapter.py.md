# mcp/tests/test_pi_rpc_adapter.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/test_pi_rpc_adapter.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-07-14T12:17+02:00 |
| lastVerifiedCommitHash | `bc2958ae2d90ab3d34bffde5402d2dc21100e41b` |
| lastVerifiedCommitDate | 2026-07-14T16:16:44+02:00|
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

## 260713-PHA-L6 Evidence Boundary

Pi adapter tests prove startup from structured `get_state`/`get_entries` evidence without a
fabricated package version; the exact `0.80.6` data is retained as fixture evidence.

## Update History
- 2026-07-14T16:30:00+02:00 — 260713-PHA-L6 curator: documented version-free Pi startup coverage.
- 2026-07-14T12:17+02:00 — 260713-PHA-L4 curator: created onboarding for Pi fake adapter,
  protocol, activity, extension UI, disconnect, and reconciliation coverage.
