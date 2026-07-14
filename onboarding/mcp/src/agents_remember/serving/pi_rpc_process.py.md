# mcp/src/agents_remember/serving/pi_rpc_process.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/serving/pi_rpc_process.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-07-14T12:17+02:00 |
| lastVerifiedCommitHash | `d5f8edf0ccab21f1cf71723615e394eba40fcebc` |
| lastVerifiedCommitDate | 2026-07-14T12:29:36+02:00|
| governingOverview | `overview.md` |

## Governing Overview
[serving/ overview](overview.md)

## Purpose
Owns the async subprocess transport for the Pi RPC child, including request correlation,
incremental stdout framing, bounded event/stderr retention, disconnect classification, and clean
termination.

## Code Commentary
`PiRpcSubprocess` starts Pi with supplied cwd/environment and pipes, sends encoded commands, keeps
one future per correlated request id, and publishes unsolicited frames through a bounded event
queue. stdout parsing uses `PiRpcJsonlDecoder`; protocol errors fail pending requests and the event
stream. Write failures distinguish before-write from possible-send disconnects. Stop signals the
child, cancels readers, fails pending requests, and closes the event stream.

## Invariants And Boundaries
- This is the process/transport seam, not Pi policy or normalized adapter state.
- Queue and stderr buffers are bounded because the child is an external process.
- Disconnect evidence is typed and preserved; transport never retries or resends.
- No pane, log, or terminal fallback exists.

## Repo-Internal References
| Finding | Source Path |
| --- | --- |
| Strict encoder/decoder and launch contract. | [pi_rpc_protocol.py](pi_rpc_protocol.py) |
| Adapter consuming this transport. | [pi_rpc_adapter.py](pi_rpc_adapter.py) |
| Child-process coverage. | [test_pi_rpc_process.py](../../../../../../tests/test_pi_rpc_process.py) |

## Cross-Repo References
No meaningful cross-repo references found.

## Update History
- 2026-07-14T12:17+02:00 — 260713-PHA-L4 curator: created onboarding for the owned child,
  correlation, bounded buffering, typed disconnects, protocol-failure propagation, and stop path.
