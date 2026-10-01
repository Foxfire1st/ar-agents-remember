# mcp/src/agents_remember/serving/eve_protocol.py

## Governing Overview

[serving/ overview](overview.md)

## Purpose

The eve wire contract in one place: the `/eve/v1` routes, the NDJSON event envelope, the response
shapes acceptance is read from, the queued-turn policy literal, and the **absolute stream cursor**
rule. Every other eve module depends on this file so the protocol assumption is stated once rather
than re-derived at each call site.

It exists because eve's stream position cannot be reconstructed after the fact. An off-by-one in this
cursor silently drops or duplicates a durable event, and the sessions that suffered it are the ones
already running — so the rule is stated in the module that owns the arithmetic's inputs.

## Code Commentary

### Logic

`EVE_ROUTE_PREFIX` is `/eve/v1`; the adapter speaks no other HTTP surface. `eve_session_route`,
`eve_session_control_route` and `eve_session_stream_route` build ID-addressed routes only — there is
no create-route builder here, because a create is one POST to `EVE_SESSION_PATH` and every follow-up
must name an existing durable id. `eve_session_stream_route` omits the query parameter at index 0,
appends `startIndex` above it, and refuses a negative index.

Header and body parsing is explicit rather than permissive:

- `parse_stream_version` **requires** `x-eve-stream-version` and accepts only
  `EVE_SUPPORTED_STREAM_VERSIONS` (`21`–`25`). An unknown version raises instead of treating unknown
  JSON as a current event. Version 25 is the delta-only contract; lower versions are accepted because
  eve normalises their cumulative appends on replay, not because this reader interprets them
  differently — the delta fields it consumes are present in every accepted version.
- `parse_stream_tail_index` reads the optional `x-eve-stream-tail-index` bound and answers `None`
  when the server reports none.
- `parse_session_acceptance` reads `(session_id, delivery_id)` from the body, falling back to the
  `x-eve-session-id` header, and raises when neither proves an identity — an acceptance with no
  durable id is a protocol failure, never a silently unbound session.
- `parse_event_frame` reads `type`, `data` and `meta` **field by field from the declared schema**,
  never by scanning text.

`EveStreamEvent` carries the absolute `index` it was read at plus the optional envelope identity;
`raw_frame()` reconstructs the documented envelope, which is what an evidence buffer retains
verbatim.

`EVE_REPLAY_WINDOW` (2048) and `EveEventDeduplicator` are declared here, and the class is the **single
owner** of that window: the adapter holds one instance and asks it about every identified event, so
the component this module documents is the one under test. The bound is a fixed window rather than a
growing set because eve promises overlap at the tail of the record, never an arbitrarily deep rewind;
`retained` exposes the current occupancy for the bounded-growth assertion, and the non-positive window
is refused at construction.

`TURN_POLICY_QUEUE` is the one literal `"queue"` in the tree: the transport client's create and
follow-up body builders both spell it from here, so no second spelling can drift toward eve's
`steer` default.

`EveRuntimeLaunch` is declared here, beside the wire contract it serves, so the launch spec and the
transport client can both depend on it without importing each other.

### Conventions

- Header lookup (`_header`) is case-insensitive and treats a blank value as absent.
- `_encode_segment` percent-encodes `/` in an identity segment and refuses an empty one.
- Every refusal is a `HarnessControlError` naming what was actually seen.
- The event-type sets (`TURN_BOUNDARY_EVENT_TYPES`, `SESSION_TERMINAL_EVENT_TYPES`,
  `TURN_FAILURE_EVENT_TYPES`, `ACTION_REQUEST_EVENT_TYPES`, and the interaction/authorization names)
  are the protocol's own vocabulary, referenced by name rather than re-spelled elsewhere.

### Invariants And Boundaries

- **The absolute event index — not `meta.id` — is the only lossless cursor.** Two events emitted in
  the same millisecond by different durable steps may sort either way, so an id-ordered cursor can
  skip events. The id is used only to recognise an event a reconnect already delivered.
- `meta.id` is optional **by contract, not by laxity**: records written before stream version 20
  carry no identity, and `is_replay` returns `False` for them because the caller's absolute index is
  then the only ordering that exists.
- An acceptance carrying no durable session id fails; it never yields an unbound or replacement
  session.
- An unsupported or missing stream version fails; unknown JSON is never assumed current.
- **One deduplicator, one bound.** A second replay window anywhere else in the adapter is a
  regression against this module's ownership.
- This module declares no adapter behavior: it parses and routes, and never decides delivery,
  acceptance or terminal state.

### Todos

None known.

## Evidence

### Docs References

No Domain Documentation source is configured for this repository, so no live domain-documentation
pass was available for this file. eve's own published protocol documentation is the external
authority this module mirrors.

No configured `Domain Documentation` source exists in `system/sources.md`; eve's published protocol docs are the external authority and are cited by the runtime README instead.

### Repo-Internal References

The wire contract is consumed by the transport client and the cursor decoder, and it is mirrored by
the AR-owned runtime application's authored channel.

- The transport client is the only caller of these routes and parsers, and both of its body builders spell the queued policy from this module's one literal. [1]
- The incremental decoder feeds raw bytes through `parse_event_frame` one completed line at a time. [2]
- The adapter owns the persisted cursor and drops a replayed envelope id before translating. [3]
- The runtime application's authored channel carries the same queue default for every later turn. [4]
- Wire-conformance cases pin the index arithmetic, the version gate, the permissive-parse refusals, and the exact request bodies the production client sends over a mock transport. [5]
- The replay window's own cases cover first-sight versus repeat, oldest-first eviction at the bound, a size-1 window, id-less events, and the non-positive refusal. [6]

### Cross-Repo References

The protocol is defined by the published `eve` package — a pinned third-party dependency, not a
sibling Agents Remember repository.

- The `/eve/v1` routes, the `x-eve-stream-*` headers and the event envelope are eve's published wire contract, re-verified against the installed package at the pinned release. [7]
