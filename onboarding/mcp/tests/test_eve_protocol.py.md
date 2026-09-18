# mcp/tests/test_eve_protocol.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/test_eve_protocol.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-16T10:15+02:00 |
| lastVerifiedCommitHash | `d9becade1a373f2272501f7451746ccc259ca9ac` |
| lastVerifiedCommitDate | 2026-09-18T12:33:45+02:00|
| governingOverview | `overview.md` |

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

## Docs References

No Domain Documentation source is configured for this repository, so no live domain-documentation
pass was available for this file.

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured `Domain Documentation` source; the shapes under test come from the eve wire contract and are mirrored by the module under test. | — | — |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The routes, header gates, acceptance parsing and frame schema these cases pin. | `parse_stream_version`; `parse_stream_tail_index`; `parse_session_acceptance`; `parse_event_frame` | mcp/src/agents_remember/serving/eve_protocol.py:147-222 |
| The absolute-index decoder and its frame ceiling. | `EveNdjsonDecoder`; `DEFAULT_MAX_FRAME_BYTES` | mcp/src/agents_remember/serving/eve_stream_cursor.py:15-69 |
| The bounded replay window whose occupancy and eviction these cases pin. | `EveEventDeduplicator`; `EVE_REPLAY_WINDOW`; `retained` | mcp/src/agents_remember/serving/eve_protocol.py:224-268 |
| The production request builders and the transport these wire cases drive. | `create_session_body`; `follow_up_body`; `cancel_turn_body`; `EveRuntimeProcess` | mcp/src/agents_remember/serving/eve_runtime_client.py:62-89; mcp/src/agents_remember/serving/eve_runtime_client.py:118-372 |
| The adapter cases that consume this same wire layer one level up. | `EveAdapterReconnectTests`; `EveAdapterReconcileTests`; `EveAdapterInterruptTests` | mcp/tests/test_eve_adapter.py:661-907 |
| The test suite this file joins and its fixture/collection conventions. | `## Fixture Roles And Claims`; `## Isolation And Collection` | onboarding/mcp/tests/overview.md:646-666; onboarding/mcp/tests/overview.md:668-670 |

## Cross-Repo References

No external repository boundary is implemented by this test.

| Finding | Anchor | Source |
| --- | --- | --- |
| The protocol shapes under test are the pinned published `eve` package's contract, not a sibling repository's. | `eve` | mcp/src/agents_remember/serving/eve_protocol.py:32-40 |

## Update History
2026-09-18T06:55+02:00 — 260915-CAPS-L24 curator: **stale citations repaired in this document.** This leaf's curator re-derived every failing citation row against the file it cites: each Anchor cell now names text that exists inside the cited range, each Source cell is a plain `path:start-end` in bounds of the file as it stands, and a claim whose construct the source no longer carries was re-worded to what the source now says rather than re-pointed at something adjacent. Mechanically regenerable ranges were rewritten by the shipped citation fixer; the rest were repaired by reading the source. No verification stamp advanced on content alone: the candidate is uncommitted and the governed closeout owns the real code and memory commits.

- 2026-09-16T10:15+02:00 — 260915-CAPS-L6 curator (A2 delta pass): this file more than doubled
  (238 → 526 lines) and is the round's main test-strengthening surface. Three new faces are recorded:
  `EveReplayWindowTests` pins the bounded window's eviction, size-1 and id-less cases plus the
  non-positive refusal; `EveWireBodyTests` pins that create **and** follow-up both spell the queued
  policy; `EveWireRequestTests` drives the **production** `EveRuntimeProcess` through
  `httpx.MockTransport` and a `_Recorder`, so the sent request is asserted rather than inferred from a
  fake. The "six contract faces" count was corrected to the actual nine, and the boundary that these
  cases pin framing plus outgoing bodies (never adapter session state) was made explicit. Citation
  tables rewritten into the `Finding | Anchor | Source` shape; verification metadata moves to the
  leaf's current base `e9300687`, with the governed closeout stamping the real code commit.

- 2026-09-16T09:00+02:00 — 260915-CAPS-L6 curator: created this card for a test module added by the
  native eve session-adapter change set. Records the six contract faces, the deliberately narrow
  framing-and-parsing scope, and why the keep-alive case is correctness-bearing. Verification
  metadata is pinned to the leaf's base commit `67b21aeb` because the candidate is deliberately
  uncommitted — the governed closeout stamps the real code commit, and no hash or fingerprint was
  invented here.
