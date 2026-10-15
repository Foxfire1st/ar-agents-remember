# mcp/src/agents_remember/serving/events.py

## Governing Overview

[overview.md](overview.md)

## Purpose

`events.py` is the **raw `event` SSE channel** (slice 4b): a byte-offset tail of the
append-only observer logs that streams the `ar-observer-event/v1` *activity* records
**verbatim** — minus liveness `lifecycle.heartbeat` lines — with exact `Last-Event-ID`
resume. It is the counterpart to the `state` channel (`app.py`): the state channel serves the
folded projection and re-snapshots on reconnect, while this channel resumes by byte offset
because lifecycle event logs are append-only — a reconnecting client must resume where it
left off, not replay history. (The shared workspace river is bounded and live-compacted,
not unbounded.) Initial offsets are computed once and emitted event batches are count-bounded and offloaded. Raw bytes/lines are not batch-bounded: _read_lines_from reads the entire selected-source suffix before the first emitted event. It powers the future event-log panel + sim scrubbing.

## Code Commentary

The event tail attributes its actual read/offloaded work to its own ledger owner while keeping the stream write-free. This adds diagnostics, not a new writer, cursor policy, reclamation action or event-delivery guarantee.


### 260928-MIK-L114 Write-Free Stream With Last-Feed Ready

`stream_raw_events` deletes nothing: lifecycle-log reclamation belongs to the projection
pass alone, and a connected browser changes no file under `logs/observer/`. The workspace
read holds the shared river lock without creating any observer file
(`workspace_river_read`); with no lockfile it proceeds lockless and repeats once under
the lock if a lockfile appears, so the base/file pair counts by construction and a lost
or repeated row is impossible. Fresh initialization (absent, invalid or empty decoded cursor) may supply lastEventTs, taking the latest parsed timestamp among each source tail's last parseable row. A nonempty decoded cursor resumes with stored_ts=None and omits the key; this is not a maximum scan of every event timestamp.

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

Historical CS-6 offload account: current stream offloads fresh offset/tail-timestamp reads and recurring event reads, but no longer prunes; reclamation is projection-owned.

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
- `stream_raw_events(config, *, last_event_id, interval)` computes the offset map **once** —
  `initial_event_offsets` when the client has no valid/non-empty `Last-Event-ID`, else the
  explicit resume cursor offsets — then loops over that carried-forward map (no per-tick
  re-scan and no pruning: lifecycle-log reclamation belongs to the projection pass) →
  `read_new_events(..., limit=DEFAULT_EVENT_BATCH)` in a worker thread → yield each as
  `ServerSentEvent(event="event", id=<cursor>, retry=2000)`. While a chunk is non-empty it yields to the
  loop (`await asyncio.sleep(0)`) and drains the next chunk; once the (window-bounded) backlog is empty it
  emits one `ServerSentEvent(event="ready", data={"ready": true}, id=<current cursor>)` and then
  `sleep(interval)`. Offsets are initialized once; emitted batches are bounded, but each source read materializes its remaining complete lines before the emitted-event limit is applied.

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
- **Offloaded reads, bounded emitted batches:** offsets are initialized once and emitted batches yield between calls. This does not bound source-byte reads or line allocation before the first byte: each selected suffix is read in full on the worker.
- **Lifecycle-aware replay boundary** — valid cursor resumes are honored exactly, but fresh or malformed
  cursor connections begin at the retained windowed offsets (dormant logs at EOF, active logs at the recent
  replay window, workspace TTL) instead of replaying every historical observer event from byte zero.
- **Pruning is projection-owned:** this stream never removes a lifecycle log or any
  observer file; the projection pass owns reclamation with its running-master protection.
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


### Cross-Repo References

No meaningful cross-repository implementation source governs this repository-local event tail.

The reviewed behavior is wholly repository-local.

- The app that mounts this as `GET /api/events`.  Anchor: "async def stream_events(" [4]
- The inactivity retention helper computes windowed fresh offsets for connect; lifecycle-log reclamation belongs to the projection pass. [5]
- `read_new_events` realigns records, admits top-level objects, filters heartbeat payloads, and bounds emitted batches. [6]
- `stream_raw_events` computes offsets once, drains the backlog in bounded chunks without pruning, and emits `ready` once after it. [7]
