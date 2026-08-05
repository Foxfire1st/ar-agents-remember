# mcp/src/agents_remember/serving/pi_rpc_process.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/serving/pi_rpc_process.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-07-17T21:39+02:00 |
| lastVerifiedCommitHash | `5920ea2b4bdd5d5ee969ae064ff9a8e1fc6b4060` |
| lastVerifiedCommitDate | 2026-08-05T12:41:24+02:00|
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

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured domain documentation could be checked. | — | — |

## Repo-Internal References

The configuration transaction depends on cancellation reclaim so its finite timeout cannot poison
the shared reader.

| Finding | Anchor | Source |
| --- | --- | --- |
| Configuration wraps mutation plus state/catalog readback in one finite timeout; cancellation propagates into this transport. | `PiRpcConfiguration`, `_transaction` | mcp/src/agents_remember/serving/pi_rpc_configuration.py:50-193 |
| Adapter owns this transport and delegates live setters to the configuration transaction. | `PiRpcAdapter`, `set_model`, `set_effort` | mcp/src/agents_remember/serving/pi_rpc_adapter.py:94-768 |

## Cross-Repo References

No external repository boundary is implemented beyond the installed Pi child process.

| Finding | Anchor | Source |
| --- | --- | --- |
| No meaningful cross-repo references found. | — | — |

## 260715-FEUI-L5 Submission Authority Delta

Pi writes now share one process lock and accept a generation/activity/event-token guard immediately
before the first byte. Stop/restart invalidates tokens and cleans pending requests. The write result
preserves whether no byte or a possible first byte crossed the boundary for certified retry versus
unknown classification.

## Update History

- 2026-08-03T04:32:19+02:00 — W3-B08 curator: curated 4 citations (citation_anchor_missing=2, citation_prose_not_in_cit_form=0, citation_source_malformed=2); final scoped citation check clean.
- 2026-07-17T21:39+02:00 — FEUI-L5: documented token-guarded shared writes, cleanup, and first-byte
  classification.
- 2026-07-16T01:19+02:00 — 260714-ACPUI-L3 curator: documented pending-future reclamation on
  cancellation, tombstone-free late-response discard, and preservation of the shared stdout reader
  for subsequent requests.
- 2026-07-14T12:17+02:00 — 260713-PHA-L4 curator: created onboarding for the owned child,
  correlation, bounded buffering, typed disconnects, protocol-failure propagation, and stop path.
