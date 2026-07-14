# mcp/src/agents_remember/serving/pi_rpc_adapter.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/serving/pi_rpc_adapter.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-07-14T12:17+02:00 |
| lastVerifiedCommitHash | `d5f8edf0ccab21f1cf71723615e394eba40fcebc` |
| lastVerifiedCommitDate | 2026-07-14T12:29:36+02:00|
| governingOverview | `overview.md` |

## Governing Overview
[serving/ overview](overview.md)

## Purpose
Composes the Pi 0.80.6 process and event seams into the normalized L1 `HarnessProtocolAdapter`
contract without registering the vendor or introducing a pane/log fallback.

## Code Commentary
Startup adds RPC mode, reads `get_state` and `get_entries`, validates identity/capabilities, and
returns the normalized handshake. Busy terminal submissions select `steer`; durable submissions
select `followUp`; correlated success becomes immediate or queued acceptance. The event stream
reconnects on transport loss, preserves exact session identity, and maps resumed events. Ambiguous
sends are recorded with a pre-send cursor and reconciled only by exact post-cursor user text; no
duplicate resend is attempted. Extension responses route through mapper and transport.

## Invariants And Boundaries
- `get_state` governs readiness/activity and corroborates `agent_settled` completion.
- Reconnect uses the persisted session file and rejects changed session identity.
- Ambiguous submissions remain unresolved without durable evidence.
- Retention is bounded; production registration/cutover belongs to L5.

## Repo-Internal References
| Finding | Source Path |
| --- | --- |
| Normalized adapter contract and L1 bridge. | [harness_control_adapter.py](harness_control_adapter.py), [harness_control_bridge.py](harness_control_bridge.py) |
| Process and event dependencies. | [pi_rpc_process.py](pi_rpc_process.py), [pi_rpc_events.py](pi_rpc_events.py) |
| Adapter coverage. | [test_pi_rpc_adapter.py](../../../../../../tests/test_pi_rpc_adapter.py) |

## Cross-Repo References
No meaningful cross-repo references found.

## Update History
- 2026-07-14T12:17+02:00 — 260713-PHA-L4 curator: created onboarding for L1-backed handshake,
  queue behavior, settlement, extension UI, reconnect, cursor reconciliation, and no-resend policy.
