# mcp/src/agents_remember/serving/events.py

## Governing Overview

[overview.md](overview.md)

## Purpose

`events.py` is the raw workspace `event` SSE channel: virtual byte-offset Last-Event-ID resume across age/size compaction, distinct from the snapshot/delta state channel. Fresh reads start in the retained recent window. Emitted batches are count-bounded and offloaded; `_read_lines_from` materializes the selected complete suffix before emission, so raw-byte/line allocation is not batch-bounded.

## Code Commentary

The event tail attributes its actual read/offloaded work to its own ledger owner while keeping the stream write-free. This adds diagnostics, not a new writer, cursor policy, reclamation action or event-delivery guarantee.


### 260928-MIK-L114 Write-Free Stream With Last-Feed Ready

`stream_raw_events` changes no observer file. Workspace reads pair the virtual base/file under an existing shared lock, or read lockless before a lockfile exists and retry once if one appears. A not-held read delays rows without cursor progress. This coordination does not promise crash-atomic or whole-system delivery. Fresh initialization may supply lastEventTs from the last parseable tail row; a nonempty resume cursor omits that fresh-tail fact.

### FEUI-L9R Reviewed Candidate Delta

Raw-event reads now treat byte offsets as untrusted resume hints while the server owns record
boundaries. A nonzero mid-record cursor advances to the next newline; an offset beyond EOF settles
at current EOF; partial trailing records remain unread. Cursor progress is committed before UTF-8
decode and JSON classification, so invalid UTF-8, malformed JSON, blanks, all five non-object JSON
families are skipped without retry. Each accepted top-level object is
parsed once into `RawEvent.payload`, and the SSE stream reuses that object rather than parsing again.

### 260707-HFX2-L13 Virtual Workspace Cursors

The sole workspace source’s reads take the shared river lock,
load `baseOffset`, clamp a client virtual cursor into the current physical file, and translate every
line/end offset back into the virtual coordinate system. A cursor inside reclaimed history therefore
reseats at the retained head, while a cursor in retained/new history resumes exactly. Locking the base
sidecar and file read as one pair prevents a live compaction from exposing mismatched coordinates.

### 260707-HFX2-L12 CS-6 Update

The stream offloads fresh offset/tail-timestamp and recurring event reads without pruning; writer/compactor own River reclamation.

The tail is a **pure** function so resume, multi-source ordering, and partial-line handling are
testable without an HTTP client:

- `read_new_events(root, offsets, *, limit=None)` discovers only `workspace` when present (`_discover_sources`) — seeks each `events.jsonl`
  from a server-owned boundary (`_read_lines_from` realigns a nonzero mid-record cursor and clamps
  beyond EOF) and advances the offset after each complete byte record before decoding it. Invalid
  UTF-8, blank text, malformed JSON, and valid non-object JSON are skipped with that progress
  retained. Accepted top-level objects produce `RawEvent(source, data, payload, cursor)`; no heartbeat filter remains. When `limit` is set, only emitted objects count
  toward the batch. A trailing partial line remains unconsumed.
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
  re-initialization and no pruning: the River writer/compactor owns reclamation) →
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
- **Offloaded reads, bounded emitted batches:** offsets are initialized once and emitted batches yield between calls. This does not bound source-byte reads or line allocation before the first byte: each selected suffix is read in full on the worker.
- **Fresh versus resumed replay:** fresh/invalid-cursor reads start at the retained workspace window; virtual cursors translate through the compaction base and reseat reclaimed history at the retained head.
- **Read-only:** the stream removes no observer file; writer/compactor own retention.
- **Readiness is explicit:** a cursorless fresh connection can legitimately receive zero retained rows;
  the separate `ready` event tells clients that the window-bounded backlog has finished hydrating.

### Logic

The reader discovers only the workspace source, translates its virtual cursor coordinates, realigns
untrusted offsets, advances complete records, admits only parsed top-level objects, and streams the
retained payload with its post-record composite cursor.

### Conventions

Workspace virtual offsets retain the compaction base. Complete records are handled as bytes until record boundaries are established.

### Invariants And Boundaries

Incomplete trailing records remain unread, poison records advance without emission, accepted event text is parsed exactly once.

### Todos

No task-independent technical debt was identified during FEUI-L9R review.

## Evidence

### Docs References

No relevant documentation was found after checking the configured sources; cursor and event-stream
claims are proven by repository source and tests.

No relevant external or domain documentation was found for this repository-local event tail.

### Repo-Internal References

- The observer event envelope tailed here. [1]
- EventStore appends and reads a single workspace Event River at <observer_root>/workspace/events.jsonl, using WORKSPACE_SOURCE = "workspace". Its log_path takes no lifecycle id; lifecycle-specific event logs are not part of this layout. [2]
- The one read/path abstraction (NS #5). [3]


### Cross-Repo References

No meaningful cross-repository implementation source governs this repository-local event tail.

The reviewed behavior is wholly repository-local.

- The app that mounts this as `GET /api/events`.  Anchor: "async def stream_events(" [4]
- initial_event_offsets computes fresh-connect offsets for workspace/events.jsonl from the recent replay window plus the persisted virtual base offset. The retained-offset scan keeps events it cannot prove older than the cutoff. Physical reclamation belongs to the workspace River compactor and append-time size-bound admission under the shared lock, not lifecycle-log pruning in a projection pass. [5]
- `read_new_events` realigns records, admits top-level objects, and bounds emitted batches. [6]
- `stream_raw_events` computes offsets once, drains the backlog in bounded chunks without pruning, and emits `ready` once after it. [7]
