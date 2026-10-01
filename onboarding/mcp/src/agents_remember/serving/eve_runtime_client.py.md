# mcp/src/agents_remember/serving/eve_runtime_client.py

## Governing Overview

[serving/ overview](overview.md)

## Purpose

The whole process boundary for one AR bridge epoch: it starts the pinned AR-owned eve application,
waits for eve's own health route, speaks the documented session routes, and reads the durable NDJSON
stream from an absolute event index. One epoch owns exactly one eve application process and one
durable eve session.

## Code Commentary

### Logic

`EveRuntimeTransport` is the narrow native seam (`start`, `health`, `create_session`, `send_message`,
`send_input_responses`, `cancel_turn`, `compact_session`, `clear_session`, `stream`, `stop`). It exists
so a deterministic test transport can replace **the real HTTP client only**: the adapter, the event
mapper, the cursor arithmetic and the event translation stay production code under test.
`EveRuntimeProcess` is the production implementation of that seam.

`compact_session` (242) and `clear_session` (257) post eve's two ID-addressed session controls. Both
send **no body at all** — `session_control_body()` (91) returns `None` and documents why: the routes are
ID-addressed and accept no continuation token or options, and the documented `curl` form sends no body,
so sending one is not merely redundant but refusable by a strict schema. They exist because the
trusted-instruction survival claim needs them: compaction may summarize user-role history while
system-role instructions stay outside it, and clear removes the model-message history **without**
rerunning instruction definitions or resolvers — so only a system-role instruction can still govern the
call after a clear.

`start` launches `node_modules/eve/bin/eve.js dev --no-ui` with the resolved node executable, the
composed environment, and the resolved root as `cwd`; it refuses when the entrypoint is missing, and
it drains stderr into a bounded buffer so a failed launch can report why. `_await_health` polls the
health route until `{"ok": true, "status": "ready"}`, and short-circuits when the child has already
exited, quoting the stderr excerpt.

**Every request body is built by one named builder, and the queued policy is spelled by the wire
module's single literal in each of them.** `create_session_body` and `follow_up_body` both return
`{"message": …, "turnPolicy": TURN_POLICY_QUEUE}`, so a follow-up turn cannot silently inherit eve's
cancellation-backed `steer` default while the create still queues; `cancel_turn_body` names the exact
turn and answers `None` when there is no observed turn to name. `create_session` posts the create body
and expects `202`; `send_message` posts the follow-up body to the ID-addressed route. Both read
`(session_id, delivery_id)` through `eve_protocol.parse_session_acceptance`. `cancel_turn` posts the
turn-addressed cancel and accepts either `202` or the no-active-turn `200`. `send_input_responses`
posts the strict entry list.

`stream` reads line by line (`aiter_lines`) under a `httpx.Timeout` whose **read** budget is
`DEFAULT_STREAM_READ_SECONDS` (10 s). It ends the iterator when the connection closes or the bounded
read elapses; a silent bounded read is swallowed as the expected shape of a parked session, while a
transport error becomes a `HarnessAdapterDisconnectedError` with `may_have_sent=False`.

### Conventions

- `_post_json` carries write ambiguity on the error: a transport failure while posting raises
  `HarnessAdapterDisconnectedError(may_have_sent=True)` so the caller reconciles rather than repeats.
- The `409`/`session_not_active` answer is translated into the explicit refusal "the durable session
  is unknown or terminal; no replacement session is created".
- `_terminate` escalates once (`terminate`, bounded wait, then `kill`), so a process that never exits
  is not left behind.
- The body builders are module-level functions, not inlined dict literals, so the exact wire shape is
  directly assertable without standing up a server.

### Invariants And Boundaries

- **Closing a subscriber cancels the HTTP read only.** The durable session keeps running, because
  eve's turns survive a disconnected reader.
- **`stop` terminates only the process this adapter started**, and never deletes a durable eve
  session.
- **The read is line-based and bounded on purpose.** An unbounded chunked read (`aiter_bytes`) was
  measured returning zero bytes for 25 s against this server's chunked-but-silent response, while the
  same session's events were durable and readable by `curl` and by a line-based reader. Replacing
  this with an unbounded chunked read reproduces that stall; the events are already durable, so a
  reconnect from the persisted absolute index loses nothing and duplicates nothing.
- **Queued, explicitly.** No request this client sends leaves `turnPolicy` to eve's default.
- **The session controls send no body.** `compact_session` and `clear_session` are ID-addressed routes
  with no options and no continuation token; a body here would be a field the route does not declare.
- **A cleared or compacted session does not rerun instruction resolvers.** This is why the mandatory
  capsule is applied in the system role at the route gate rather than through a per-turn resolver that
  a clear could drop.
- `health()` requires eve's own ready payload. A successful process spawn is never readiness proof.
- The client never derives session identity from anything but eve's response or its session-id
  header.

### Todos

None known.

## Evidence

### Docs References

No Domain Documentation source is configured for this repository, so no live domain-documentation
pass was available for this file.

No configured `Domain Documentation` source; the HTTP session routes and status codes are eve's published contract, mirrored from the wire module.

### Repo-Internal References

- Routes, status codes, headers and the queue policy constant are declared once in the wire module and imported here. [1]
- Both request bodies are built here from that one literal, which is what pins the queued policy on the wire rather than only in a comment. [2]
- Frame decoding from one transport read is the cursor decoder's job, not this module's. [3]
- Node resolution is owned by the launch module so the client never guesses an interpreter, and the caller's choice arrives on the launch it is handed. [4]
- The native fixture subclasses this client to trace traffic, which is why the route surface must stay observable and every sent body is recorded for assertion. [5]
- The deterministic conformance suites implement this seam and leave every other layer production. [6]
- The two session controls this client gained, and why they matter to the trusted-instruction claim: clear does not rerun resolvers, compaction may summarize user-role history. [7]
- The trusted instructions are applied in the system role so they survive turn boundaries, compaction and clear. [8]
- The cases that exercise the controls through this client's own seam. [9]

### Cross-Repo References

- The session routes, the `x-eve-stream-*` headers and the `turnPolicy` vocabulary are the pinned published package's contract. [10]
