# mcp/src/agents_remember/serving/pi_rpc_process.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/serving/pi_rpc_process.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-07-16T01:19+02:00 |
| lastVerifiedCommitHash | `06973f6886276d7b3670c2c1e19cbb76928a7892` |
| lastVerifiedCommitDate | 2026-07-16T01:49:31+02:00|
| governingOverview | `overview.md` |

## Governing Overview
[serving/ overview](overview.md)

## Purpose
Owns the async subprocess transport for the Pi RPC child, including request correlation,
incremental stdout framing, cancellation-safe late responses, bounded event/stderr retention,
disconnect classification, and clean termination.

## Code Commentary

### Logic

`PiRpcSubprocess` starts Pi with supplied cwd/environment and pipes, sends encoded commands, keeps
one future per correlated request id, and publishes unsolicited frames through a bounded event
queue. Cancelling a request removes its pending future immediately. If Pi later emits the valid
correlated response, dispatch sees no live consumer and drops it; no abandoned-id tombstone is
retained, and the shared reader continues serving later requests. stdout parsing still uses
`PiRpcJsonlDecoder`; malformed protocol, process failure, and disconnect fail live requests and the
event stream. Stop signals the child, cancels readers, fails pending requests, and closes events.

### Conventions

Request ids are non-empty strings owned by the adapter. Missing live future after syntactically
valid correlation means the caller cancelled; it is not reassigned to another request.

### Invariants And Boundaries
- This is the process/transport seam, not Pi policy or normalized adapter state.
- Queue and stderr buffers are bounded because the child is an external process.
- Disconnect evidence is typed and preserved; transport never retries or resends.
- Cancellation reclaims correlation state, and a late response cannot kill the reader or satisfy a
  later request.
- No pane, log, or terminal fallback exists.

### Todos

None known for the L3 cancellation boundary.

## Docs References

No Domain Documentation source is configured for this repository, so no live
domain-documentation pass was available for this update.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No configured domain documentation could be checked. | — | — |

## Repo-Internal References

The configuration transaction depends on cancellation reclaim so its finite timeout cannot poison
the shared reader.

| Finding | Citations | Source Path |
| --- | --- | --- |
| Configuration wraps mutation plus state/catalog readback in one finite timeout; cancellation propagates into this transport. | L133-L167 | [pi_rpc_configuration.py](agents-remember/mcp/src/agents_remember/serving/pi_rpc_configuration.py) |
| Adapter owns this transport and delegates live setters to the configuration transaction. | L68-L127; L208-L214 | [pi_rpc_adapter.py](agents-remember/mcp/src/agents_remember/serving/pi_rpc_adapter.py) |

## Cross-Repo References

No external repository boundary is implemented beyond the installed Pi child process.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No meaningful cross-repo references found. | — | — |

## Update History
- 2026-07-16T01:19+02:00 — 260714-ACPUI-L3 curator: documented pending-future reclamation on
  cancellation, tombstone-free late-response discard, and preservation of the shared stdout reader
  for subsequent requests.
- 2026-07-14T12:17+02:00 — 260713-PHA-L4 curator: created onboarding for the owned child,
  correlation, bounded buffering, typed disconnects, protocol-failure propagation, and stop path.
