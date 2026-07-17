# mcp/src/agents_remember/serving/pi_rpc_events.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/serving/pi_rpc_events.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-07-17T21:39+02:00 |
| lastVerifiedCommitHash | `f8196d98982f834d68152d307ff8025ea69440d5` |
| lastVerifiedCommitDate | 2026-07-17T22:08:10+02:00|
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
- Event raw evidence records the structured Pi protocol and cursor without fabricating a package
  version. Mapping remains responsible only for normalized state/events, not compatibility guesses.
- Retry and compaction remain settling; `agent_end` is not sufficient for terminal idle.
- Dialog responses are correlated; fire-and-forget UI events do not solicit responses.
- Mapping does not launch processes, reconnect sessions, or register vendors.

## Docs References

No Domain Documentation source is configured for this repository; repository code and tests are the authority.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No configured live domain-documentation source was available. | — | — |

## Repo-Internal References
| Finding | Source Path |
| --- | --- |
| Pi frame schemas and UI policy. | [pi_rpc_protocol.py](pi_rpc_protocol.py) |
| Adapter event-stream owner. | [pi_rpc_adapter.py](pi_rpc_adapter.py) |
| Event/settlement coverage. | [test_pi_rpc_adapter.py](../../../tests/test_pi_rpc_adapter.py) |

## Cross-Repo References
No meaningful cross-repo references found.

| Finding | Citations | Source Path |
| --- | --- | --- |
| This file implements a repository-local contract. | — | — |

## 260715-FEUI-L5 Submission Authority Delta

Pi event translation attaches the exact operation ref. Completion requires the settled event plus a
fresh idle observation for the same generation/activity token; `agent_end` or queue depth zero alone
is insufficient and stale events cannot release the successor.

## Update History

- 2026-07-17T21:39+02:00 — FEUI-L5: documented exact-ref event translation and fresh-idle terminal
  evidence.
- 2026-07-14T16:30:00+02:00 — 260713-PHA-L6 curator: removed version fabrication from mapped Pi event evidence and
  documented the structured protocol boundary.
- 2026-07-14T12:17+02:00 — 260713-PHA-L4 curator: created onboarding for normalized activity,
  queue, transcript, extension UI, retry/compaction, and settled completion mapping.
