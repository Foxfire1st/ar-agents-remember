# mcp/src/agents_remember/serving/pi_rpc_process.py

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

## Evidence

### Docs References

No Domain Documentation source is configured for this repository, so no live
domain-documentation pass was available for this update.

No configured domain documentation could be checked.

### Repo-Internal References

The configuration transaction depends on cancellation reclaim so its finite timeout cannot poison
the shared reader.

- Configuration wraps mutation plus state/catalog readback in one finite timeout; cancellation propagates into this transport. [1]
- Adapter owns this transport and delegates live setters to the configuration transaction. [2]

### Cross-Repo References

No external repository boundary is implemented beyond the installed Pi child process.

No meaningful cross-repo references found.

## 260715-FEUI-L5 Submission Authority Delta

Pi writes now share one process lock and accept a generation/activity/event-token guard immediately
before the first byte. Stop/restart invalidates tokens and cleans pending requests. The write result
preserves whether no byte or a possible first byte crossed the boundary for certified retry versus
unknown classification.
