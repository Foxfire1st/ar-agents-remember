# mcp/tests/test_eve_protocol.py

## Governing Overview

[mcp/tests overview](overview.md)

## Purpose

Wire-contract conformance for the eve session protocol reader, and — since the A2 revision — for the
**exact bytes the production client puts on the wire**. The file's own docstring states why it exists:
the cursor is the one piece of this adapter that **cannot be repaired after the fact** — an off-by-one
or a frame-boundary mistake silently drops or duplicates a durable event, and the sessions that
suffered it are the ones already running. So these cases pin the decoder's index arithmetic and the
envelope parsing against eve's documented shapes, and the request bodies against the transport the
adapter actually uses.

## Code Commentary

### Logic

Nine `unittest.TestCase` classes, one per contract face:

- `EveRouteTests` — routes are ID-addressed and exact; a negative cursor and an empty identity segment
  are refused. Nothing here can create or follow a replacement session.
- `EveStreamHeaderTests` — the declared stream version is **required, not inferred from the JSON**:
  each of `21`–`25` is accepted, `26` and a missing header raise. The optional tail-index header reads
  or is absent, and a non-numeric one raises. Header lookup is case-insensitive and a blank value
  counts as absent.
- `EveAcceptanceTests` — the durable session id may come from the body or the session-id header, and
  an acceptance carrying **no** identity fails instead of unbinding the session.
- `EveFrameTests` — the envelope is read field by field (including `deliveryIds` and the `raw_frame()`
  round-trip), a pre-version-20 event with no `meta.id` still parses, and five malformed shapes are
  refused.
- `EveCursorTests` — frames split across reads keep their absolute index; blank keep-alive lines do
  **not** consume one; a trailing frame without a newline is still decoded by `finish()`; an oversized
  frame is refused; a frame exactly at the ceiling is still read.
- `EveEnvelopeIdentityTests` — `turn_id` reads the documented coordinate and nothing else, and is
  optional.
- `EveReplayWindowTests` — the bounded replay window: a repeated id is a replay and a first sight is
  not, the window evicts oldest-first and stays bounded, a size-1 window still recognises its single
  entry, an event with no id is **never** a replay, and a non-positive window is refused at
  construction.
- `EveWireBodyTests` — the body builders themselves: create and follow-up **both** spell the queued
  policy, and the cancel body addresses the exact observed turn.
- `EveWireRequestTests` — the production `EveRuntimeProcess` driven through `httpx.MockTransport`
  against a `_Recorder`, so the request the adapter really sends is asserted rather than inferred from
  a fake. This is the face that pins the wire, and it does not require a server.

### Conventions

- The module inserts `mcp/src` on `sys.path` itself, the sibling-test convention in this suite.
- `_frame(...)` builds one NDJSON frame with a deterministic envelope id, so a case reads as the
  protocol shape it pins rather than as JSON construction.
- Cases are added to a `unittest.TestCase`, so they join the existing unit population rather than
  introducing a second test framework to this suite.
- `_StartedRuntime` subclasses the production process so the wire cases exercise real `start`,
  `create_session`, `send_message` and `cancel_turn` code against a recorded transport.

### Invariants And Boundaries

- These cases pin **framing, parsing and the outgoing request bodies**. They do not start an eve
  process, do not exercise the adapter's session state, and prove nothing about delivery, acceptance
  or terminal state — that is `test_eve_adapter.py`'s scope.
- The keep-alive case is load-bearing for correctness, not for tidiness: advancing the index on a
  blank line would drift the persisted cursor away from the durable record.
- **A policy asserted only on the create is not asserted.** The follow-up carries its own body, so the
  queued policy is pinned on both shapes; a second, unasserted follow-up body is how a steer
  inheritance hides.
- Asserting both directions is the local style: each case also pins the refusal it would otherwise
  hide.

### Todos

None known.

## Evidence

### Docs References

No Domain Documentation source is configured for this repository, so no live domain-documentation
pass was available for this file.

No configured `Domain Documentation` source; the shapes under test come from the eve wire contract and are mirrored by the module under test.

### Repo-Internal References

- The routes, header gates, acceptance parsing and frame schema these cases pin. [1]
- The absolute-index decoder and its frame ceiling. [2]
- The bounded replay window whose occupancy and eviction these cases pin. [3]
- The production request builders and the transport these wire cases drive. [4]
- The adapter cases that consume this same wire layer one level up. [5]
- The test suite this file joins and its fixture/collection conventions. [6]

### Cross-Repo References

No external repository boundary is implemented by this test.

- The protocol shapes under test are the pinned published `eve` package's contract, not a sibling repository's. [7]
