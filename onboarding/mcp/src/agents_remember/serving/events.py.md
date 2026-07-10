# mcp/src/agents_remember/serving/events.py

| Field                  | Value                                       |
| ---------------------- | ------------------------------------------- |
| repository             | agents-remember                             |
| path                   | `mcp/src/agents_remember/serving/events.py` |
| doc_type               | `file-level-onboarding`                     |
| lastUpdated            | 2026-07-10T01:14+02:00 |
| lastVerifiedCommitHash | `0d5ce6784930aa4e9006ab4bbf2b788a3296abce`  |
| lastVerifiedCommitDate | 2026-07-10T22:30:19+02:00|
| governingOverview      | `overview.md`                               |

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
  past its recorded byte offset (`_read_lines_from`: binary seek + complete-line split) and emits one
  `RawEvent(source, data, cursor)` per complete line. `lifecycle.heartbeat` lines are **filtered** via
  `_is_heartbeat_line` — the offset still advances past them, but they are never emitted (liveness, not
  activity). When `limit` is set the read returns early after that many emitted events (offsets just past
  the last consumed line), so a caller can drain a large backlog in bounded chunks. A trailing partial
  line (no terminating newline) is left unconsumed so a half-written append is never emitted.
- `_is_heartbeat_line(text)` is the filter: the compact on-disk wire form (`model_dump_json`, no spaces)
  matches the `_HEARTBEAT_MARKER` substring on the fast path; a tolerant `json.loads` fallback catches
  alternate spacing so a heartbeat can never slip into the river; lines without the `_HEARTBEAT_KIND`
  text are never parsed.
- `RawEvent.data` is the verbatim JSONL line (the camelCase wire form on disk); it is parsed to an
  object at the SSE boundary — `stream_raw_events` yields `ServerSentEvent(data=json.loads(line))` —
  so the wire is **single-encoded** like the state channel, not the double-encoded `data: "{…}"` that
  passing the pre-serialized string produced (every client would otherwise have to `JSON.parse`
  twice). `RawEvent.cursor` is the per-source offset map **after** that event, i.e. the
  `Last-Event-ID` to resume the whole stream from that point.
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
- **Single-encoded wire** — each line is parsed and emitted as a JSON object (like `/api/stream`),
  not the pre-serialized string (`ServerSentEvent` would double-encode that); the layer adds no
  interpretation beyond the parse.
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

## Repo-Internal References

| Finding | Citations | Source Path |
| --- | --- | --- |
| The observer event envelope tailed here. | — | [observer/events.py](agents-remember/mcp/src/agents_remember/observer/events.py) |
| The log layout (`lifecycles/<id>/events.jsonl`, `workspace/events.jsonl`). | — | [observer/store.py](agents-remember/mcp/src/agents_remember/observer/store.py) |
| The one read/path abstraction (NS #5). | — | [observer/paths.py](agents-remember/mcp/src/agents_remember/observer/paths.py) |
| The app that mounts this as `GET /api/events`. | — | [app.py](agents-remember/mcp/src/agents_remember/serving/app.py) |
| The inactivity retention helper that computes windowed fresh offsets and prunes dormant lifecycle logs. | L36-L94 | [event_retention.py](agents-remember/mcp/src/agents_remember/observer/event_retention.py) |
| `read_new_events` filters heartbeat lines (`_is_heartbeat_line`) and bounds a batch via `limit`. | L143-L185 | [events.py](agents-remember/mcp/src/agents_remember/serving/events.py) |
| `stream_raw_events` computes offsets once, prunes on a slow cadence, drains the backlog in bounded chunks, and emits `ready` once after it. | L188-L231 | [events.py](agents-remember/mcp/src/agents_remember/serving/events.py) |
| Raw-event tests cover heartbeat skipping, limit batches, dormant pruning without a terminal event, bounded active replay, and no-heartbeat streaming. | L994-L1124 | [test_serving.py](agents-remember/mcp/tests/test_serving.py) |

## Update History

- 2026-07-10T01:14+02:00 — 260707-HFX2-L13 F3: moved workspace `/api/events` resume to locked
  virtual offsets over the compacted physical river while leaving lifecycle cursors physical.
  Verification metadata remains pinned until closeout stamps the eventual L13 code commit.

- 2026-07-09T19:31+02:00 — 260707-HFX2-L12: documented the CS-6 scaling/reclamation change for this file. Verification metadata pinned until closeout stamps the HFX2-L12 commit.
- 2026-06-28T13:54+02:00 — Task 34: `read_new_events` now filters `lifecycle.heartbeat` lines via
  `_is_heartbeat_line` (compact-wire substring fast-path + tolerant JSON fallback) and takes a `limit`
  for bounded chunks (offset still advances past skipped/consumed lines). `stream_raw_events` computes the
  offset map once, prunes on a slow `PRUNE_INTERVAL_SECONDS` cadence, drains the backlog in
  `DEFAULT_EVENT_BATCH` chunks yielding between them, and sends `ready` only after the window-bounded
  backlog drains — so connect cost is bounded (no 3x scan, no whole-history materialization). Verification
  metadata pinned until closeout stamps the task-34 code commit.
- 2026-06-28T07:32+02:00 — Task 29 S7 follow-up: the raw Event River stream now emits a one-shot
  `ready` event after initial backlog delivery so clients can distinguish "still hydrating" from "no
  retained events." Verification metadata pinned until closeout stamps the task-29 code commit.
- 2026-06-28T05:38+02:00 — Task 29: the raw SSE tail now prunes expired terminal lifecycle logs and
  starts cursor-less or malformed-cursor connections from lifecycle-aware retained offsets rather than
  replaying all history; valid `Last-Event-ID` resumes still use the supplied byte offsets exactly.
  Verification metadata pinned until closeout stamps the task-29 code commit.
- 2026-06-14T23:30+02:00 — Slice 05 (5c): `stream_raw_events` now emits `ServerSentEvent(data=json.loads(line))` so the raw channel is single-encoded like `/api/stream` (was double-encoded `data: "{…}"`, forcing every client to parse twice); docstring + invariant updated. Verification metadata pinned until closeout stamps the 5c code commit.
- 2026-06-14T11:30+02:00 — Created for slice 04 commit 4b: the raw `event` SSE channel — a pure
  byte-offset tail (`read_new_events`) with composite per-source cursor resume
  (`encode_cursor` / `decode_cursor`) and the `stream_raw_events` async tailer. Verification
  metadata pinned until closeout stamps the 4b code commit.
