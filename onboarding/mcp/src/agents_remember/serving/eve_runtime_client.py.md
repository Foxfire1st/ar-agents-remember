# mcp/src/agents_remember/serving/eve_runtime_client.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/serving/eve_runtime_client.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-16T10:15+02:00 |
| lastVerifiedCommitHash | `609756111eb3c239d0563d8631bfd564645bc9d1` |
| lastVerifiedCommitDate | 2026-09-16T10:25:13+02:00|
| governingOverview | `overview.md` |

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
`send_input_responses`, `cancel_turn`, `stream`, `stop`). It exists so a deterministic test transport
can replace **the real HTTP client only**: the adapter, the event mapper, the cursor arithmetic and
the event translation stay production code under test. `EveRuntimeProcess` is the production
implementation of that seam.

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
- `health()` requires eve's own ready payload. A successful process spawn is never readiness proof.
- The client never derives session identity from anything but eve's response or its session-id
  header.

### Todos

None known.

## Docs References

No Domain Documentation source is configured for this repository, so no live domain-documentation
pass was available for this file.

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured `Domain Documentation` source; the HTTP session routes and status codes are eve's published contract, mirrored from the wire module. | — | — |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| Routes, status codes, headers and the queue policy constant are declared once in the wire module and imported here. | `EVE_HEALTH_PATH`; `TURN_POLICY_QUEUE`; `parse_session_acceptance`; `parse_stream_version` | mcp/src/agents_remember/serving/eve_protocol.py:20-60; mcp/src/agents_remember/serving/eve_protocol.py:147-230 |
| Both request bodies are built here from that one literal, which is what pins the queued policy on the wire rather than only in a comment. | `create_session_body`; `follow_up_body`; `cancel_turn_body` | mcp/src/agents_remember/serving/eve_runtime_client.py:62-89 |
| Frame decoding from one transport read is the cursor decoder's job, not this module's. | `EveNdjsonDecoder` | mcp/src/agents_remember/serving/eve_stream_cursor.py:18-69 |
| Node resolution is owned by the launch module so the client never guesses an interpreter, and the caller's choice arrives on the launch it is handed. | `resolve_node_executable`; `EveRuntimeLaunch.node_executable` | mcp/src/agents_remember/serving/eve_runtime_launch.py:101-124; mcp/src/agents_remember/serving/eve_runtime_launch.py:406-453 |
| The native fixture subclasses this client to trace traffic, which is why the route surface must stay observable and every sent body is recorded for assertion. | `TracingEveRuntime` | mcp/tests/live_eve_native_fixture.py:89-103; mcp/tests/live_eve_native_fixture.py:584-670 |
| The deterministic conformance suites implement this seam and leave every other layer production. | `FakeEveRuntime` | mcp/tests/eve_adapter_test_support.py:74-278 |
| The production client itself is driven through a mock transport to assert the exact bodies it sends, including the cancel turn id. | `EveWireRequestTests` | mcp/tests/test_eve_protocol.py:218-526 |

## Cross-Repo References

| Finding | Anchor | Source |
| --- | --- | --- |
| The session routes, the `x-eve-stream-*` headers and the `turnPolicy` vocabulary are the pinned published package's contract. | dependency pins | eve_runtime/package.json:14-20; eve_runtime/README.md:1-22 |

## Update History

- 2026-09-16T10:15+02:00 — 260915-CAPS-L6 curator (A2 delta pass): the request bodies moved into named
  builders and the **follow-up now spells the queued policy too**. `create_session_body` and
  `follow_up_body` both return `{"message": …, "turnPolicy": TURN_POLICY_QUEUE}` from the wire module's
  one literal, `cancel_turn_body` names the exact observed turn, and the production client is now
  driven through a mock transport so the sent body is asserted rather than inferred. Previously the
  follow-up carried no policy, so a seeded steer inheritance passed both suites. Citation tables
  rewritten into the `Finding | Anchor | Source` shape; verification metadata moves to the leaf's
  current base `e9300687`, with the governed closeout stamping the real code commit.

- 2026-09-16T09:00+02:00 — 260915-CAPS-L6 curator: created this card for a file added by the native
  eve session-adapter change set. Records the two ownership rules (subscriber close is not session
  end; `stop` touches only owned resources), the deliberate bounded line-based read with its measured
  cause, and the `may_have_sent` ambiguity carried on write failures. Verification metadata is pinned
  to the leaf's base commit `67b21aeb` because the candidate is deliberately uncommitted — the
  governed closeout stamps the real code commit, and no hash or fingerprint was invented here.
