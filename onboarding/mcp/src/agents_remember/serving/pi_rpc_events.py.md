# mcp/src/agents_remember/serving/pi_rpc_events.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/serving/pi_rpc_events.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-07-14T12:17+02:00 |
| lastVerifiedCommitHash | `d5f8edf0ccab21f1cf71723615e394eba40fcebc` |
| lastVerifiedCommitDate | 2026-07-14T12:29:36+02:00|
| governingOverview | `overview.md` |

## Governing Overview
[serving/ overview](overview.md)

## Purpose
Maps documented Pi RPC frames into the normalized L1 adapter event and snapshot vocabulary while
retaining bounded dialogs and transcript entries.

## Code Commentary
`PiRpcEventMapper` applies `get_state` activity, translates start/end/retry/compaction/queue/
message/extension frames, and only emits terminal completion after `agent_settled` is corroborated
by an idle state. Dialog methods become durable pending interactions; fire-and-forget UI methods
become notices. Event/transcript sequences, raw Pi detail, and bounded interaction retention are
maintained locally.

## Invariants And Boundaries
- Retry and compaction remain settling; `agent_end` is not sufficient for terminal idle.
- Dialog responses are correlated; fire-and-forget UI events do not solicit responses.
- Mapping does not launch processes, reconnect sessions, or register vendors.

## Repo-Internal References
| Finding | Source Path |
| --- | --- |
| Pi frame schemas and UI policy. | [pi_rpc_protocol.py](pi_rpc_protocol.py) |
| Adapter event-stream owner. | [pi_rpc_adapter.py](pi_rpc_adapter.py) |
| Event/settlement coverage. | [test_pi_rpc_adapter.py](../../../../../../tests/test_pi_rpc_adapter.py) |

## Cross-Repo References
No meaningful cross-repo references found.

## Update History
- 2026-07-14T12:17+02:00 — 260713-PHA-L4 curator: created onboarding for normalized activity,
  queue, transcript, extension UI, retry/compaction, and settled completion mapping.
