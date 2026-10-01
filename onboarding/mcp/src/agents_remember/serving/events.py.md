# mcp/src/agents_remember/serving/events.py

## Governing Overview

[overview.md](overview.md)

## Purpose

`events.py` is the **raw `event` SSE channel** (slice 4b): a byte-offset tail of the
append-only observer logs that streams the `ar-observer-event/v1` *activity* records
**verbatim** — minus liveness `lifecycle.heartbeat` lines — with exact `Last-Event-ID`
resume. It is the counterpart to the `state` channel (`app.py`): the state channel serves the
folded projection and re-snapshots on reconnect, while this channel resumes by byte offset
because the event log is append-only and unbounded — a reconnecting client must resume where it
left off, not replay history. Connect cost is bounded — the offset map is computed once, pruning
runs on a slow cadence, and the backlog drains in bounded chunks — so a large history never blocks
the loop before the first byte. It powers the future event-log panel + sim scrubbing.

## Code Commentary

### FEUI-L9R Reviewed Candidate Delta

Raw-event reads now treat byte offsets as untrusted resume hints while the server owns record
boundaries. A nonzero mid-record cursor advances to the next newline; an offset beyond EOF settles
at current EOF; partial trailing records remain unread. Cursor progress is committed before UTF-8
decode and JSON classification, so invalid UTF-8, malformed JSON, blanks, all five non-object JSON
families, and filtered heartbeats are skipped without retry. Each accepted top-level object is
parsed once into `RawEvent.payload`, and the SSE stream reuses that object rather than parsing again.

### 260707-HFX2-L13 Virtual Workspace Cursors

Lifecycle sources continue to use physical byte offsets. Workspace reads take the shared river lock,
load `baseOffset`, clamp a client virtual cursor into the current physical file, and translate every
line/end offset back into the virtual coordinate system. A cursor inside reclaimed history therefore
reseats at the retained head, while a cursor in retained/new history resumes exactly. Locking the base
sidecar and file read as one pair prevents a live compaction from exposing mismatched coordinates.

### 260707-HFX2-L12 CS-6 Update

`stream_raw_events()` now offloads fresh-connect pruning and initial-offset scans to a worker thread, matching the existing `read_new_events` offload so a large retained river does not block the shared asyncio loop.

The tail is a **pure** function so resume, multi-source ordering, and partial-line handling are
testable without an HTTP client:

- `read_new_events(root, offsets, *, limit=None)` walks every source in a fixed order —
  `lifecycles/*` sorted, then `workspace` last (`_discover_sources`) — seeks each `events.jsonl`
  from a server-owned boundary (`_read_lines_from` realigns a nonzero mid-record cursor and clamps
  beyond EOF) and advances the offset after each complete byte record before decoding it. Invalid
  UTF-8, blank text, malformed JSON, and valid non-object JSON are skipped with that progress
  retained. Accepted top-level objects produce `RawEvent(source, data, payload, cursor)`; heartbeat
  objects are filtered by `_is_heartbeat_event`. When `limit` is set, only emitted objects count
  toward the batch. A trailing partial line remains unconsumed.
- `_is_heartbeat_event(payload)` reads the already-parsed object's `kind`; heartbeat filtering does
  not parse event text again.
- `RawEvent.data` retains the verbatim JSONL object text for diagnostics/tests, while
  `RawEvent.payload` retains the same record parsed exactly once. `stream_raw_events` passes that
  payload directly to `ServerSentEvent`, preserving the single-encoded wire. `RawEvent.cursor` is
  the per-source offset map after the accepted object's record.
- `encode_cursor` / `decode_cursor` carry the offset map opaquely in the SSE `id` as base64url
  JSON (newline-free); `decode_cursor` returns `{}` for an absent or malformed cursor, and the stream
  treats that as a fresh retained-offset connection rather than replaying every historical row.
- `stream_raw_events(config, *, last_event_id, interval)` prunes dormant lifecycle logs on connect,
  computes the offset map **once** — `initial_event_offsets` when the client has no valid/non-empty
  `Last-Event-ID`, else the explicit resume cursor offsets — then loops over that carried-forward map (no
  per-tick re-scan): prune only on a slow cadence (`PRUNE_INTERVAL_SECONDS`, 60s) →
  `read_new_events(..., limit=DEFAULT_EVENT_BATCH)` in a worker thread → yield each as
  `ServerSentEvent(event="event", id=<cursor>, retry=2000)`. While a chunk is non-empty it yields to the
  loop (`await asyncio.sleep(0)`) and drains the next chunk; once the (window-bounded) backlog is empty it
  emits one `ServerSentEvent(event="ready", data={"ready": true}, id=<current cursor>)` and then
  `sleep(interval)`. Net: no 3x scan and no whole-history materialization before the first byte.

## Invariants And Boundaries

- **Separate endpoint from `/api/stream`** — byte-offset resume (raw) and snapshot resume
  (state) do not mix on one stream; the cockpit opens both EventSources (well under ~6/origin).
- **Pure tail** — `read_new_events` / `encode_cursor` / `decode_cursor` have no HTTP dependency.
- **Reads only through `observer.paths.observer_root`** (NS #5) — no host paths; sim points the
  same root at a fixture so the raw channel replays identically.
- **Single-encoded object wire** — each complete record is parsed once, admitted only when its top
  level is an object, and emitted from the retained payload. Invalid/non-object records advance but
  never cross the SSE boundary.
- **Heartbeats never reach the river** — `read_new_events` filters `lifecycle.heartbeat` (liveness already
  lives in the projection status file); the offset still advances past a heartbeat so a resume never
  re-reads it.
- **Connect cost is bounded** — the offset map is computed once (not re-scanned every tick), pruning runs
  on `PRUNE_INTERVAL_SECONDS` cadence not every loop, and the backlog drains in `DEFAULT_EVENT_BATCH`
  chunks that yield between chunks, so a long history never blocks the event loop or materializes all at
  once before the first byte.
- **Lifecycle-aware replay boundary** — valid cursor resumes are honored exactly, but fresh or malformed
  cursor connections begin at the retained windowed offsets (dormant logs at EOF, active logs at the recent
  replay window, workspace TTL) instead of replaying every historical observer event from byte zero.
- **Pruning is serving-owned and projection-owned:** the raw tail prunes dormant lifecycle logs on connect
  and on a slow cadence while tailing; projection does the same before folding lifecycle logs.
- **Readiness is explicit:** a cursorless fresh connection can legitimately receive zero retained rows;
  the separate `ready` event tells clients that the window-bounded backlog has finished hydrating.

### Logic

The reader discovers lifecycle/workspace sources, translates their cursor coordinates, realigns
untrusted offsets, advances complete records, admits only parsed top-level objects, and streams the
retained payload with its post-record composite cursor.

### Conventions

Lifecycle offsets remain physical; workspace offsets retain the compaction base. Complete records
are handled as bytes until record boundaries are established.

### Invariants And Boundaries

Incomplete trailing records remain unread, poison records advance without emission, heartbeat rows
are liveness rather than activity, and accepted event text is parsed exactly once.

### Todos

No task-independent technical debt was identified during FEUI-L9R review.

## Evidence

### Docs References

No relevant documentation was found after checking the configured sources; cursor and event-stream
claims are proven by repository source and tests.

No relevant external or domain documentation was found for this repository-local event tail.

### Repo-Internal References

- The observer event envelope tailed here. [1]
- The log layout (`lifecycles/<id>/events.jsonl`, `workspace/events.jsonl`). [2]
- The one read/path abstraction (NS #5). [3]
- The app that mounts this as `GET /api/events`. [4]
- The inactivity retention helper that computes windowed fresh offsets and prunes dormant lifecycle logs. [5]
- `read_new_events` realigns records, admits top-level objects, filters heartbeat payloads, and bounds emitted batches. [6]
- `stream_raw_events` computes offsets once, prunes on a slow cadence, drains the backlog in bounded chunks, and emits `ready` once after it. [7]


### Cross-Repo References

No meaningful cross-repository implementation source governs this repository-local event tail.

The reviewed behavior is wholly repository-local.
