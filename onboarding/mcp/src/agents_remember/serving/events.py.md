# mcp/src/agents_remember/serving/events.py

| Field                  | Value                                       |
| ---------------------- | ------------------------------------------- |
| repository             | agents-remember                             |
| path                   | `mcp/src/agents_remember/serving/events.py` |
| doc_type               | `file-level-onboarding`                     |
| lastUpdated            | 2026-07-18T12:43+02:00 |
| lastVerifiedCommitHash | `ae8c47ce897b04380ebcb80f750d77ed4dc9f37d`  |
| lastVerifiedCommitDate | 2026-08-26T08:10:26+02:00|
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

## Docs References

No relevant documentation was found after checking the configured sources; cursor and event-stream
claims are proven by repository source and tests.

| Finding | Anchor | Source |
| --- | --- | --- |
| No relevant external or domain documentation was found for this repository-local event tail. | — | — |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The observer event envelope tailed here. | `Event` | mcp/src/agents_remember/observer/events.py:39-64 |
| The log layout (`lifecycles/<id>/events.jsonl`, `workspace/events.jsonl`). | `EventStore` | mcp/src/agents_remember/observer/store.py:103-171 |
| The one read/path abstraction (NS #5). | `observer_root` | mcp/src/agents_remember/serving/projections/paths.py:32-34 |
| The app that mounts this as `GET /api/events`. | "async def stream_events(" | mcp/src/agents_remember/serving/_app_common.py:116-116 |
| The inactivity retention helper that computes windowed fresh offsets and prunes dormant lifecycle logs. | `prune_expired_lifecycle_event_logs` | mcp/src/agents_remember/observer/event_retention.py:73-107 |
| `read_new_events` realigns records, admits top-level objects, filters heartbeat payloads, and bounds emitted batches. | `read_new_events` | mcp/src/agents_remember/serving/events.py:189-227 |
| `stream_raw_events` computes offsets once, prunes on a slow cadence, drains the backlog in bounded chunks, and emits `ready` once after it. | `stream_raw_events` | mcp/src/agents_remember/serving/events.py:230-277 |


## Cross-Repo References

No meaningful cross-repository implementation source governs this repository-local event tail.

| Finding | Anchor | Source |
| --- | --- | --- |
| The reviewed behavior is wholly repository-local. | — | — |

## Update History

- 2026-08-08T17:18+02:00 — 260731-EFA-L9 curator: body verified against the current worktree after the model-extraction/caller-rewrite wave; stale moved-path references repaired and the L9 change recorded. Verification metadata pinned until closeout stamps the L9 code commit.

- 2026-08-02T17:12:10+02:00 — W1-B04 curator: repaired 7 citation claims; scoped recheck clean (0 findings).

- 2026-07-31T17:20+02:00 — 260731-EFA-L2 curator: repaired the one remaining cross-file citation,
  into `mcp/tests/test_serving.py`. The stamped `L994-L1124` now lands in `BuildInfoTests` /
  `ActionGateTests`, nothing to do with raw events. The five behaviours the row names are
  `RawEventTests` L1913-L2039 (`test_read_new_events_skips_heartbeats`,
  `test_read_new_events_limit_bounds_batch`, the two
  `test_dormant_*_lifecycle_pruned_without_terminal_event` cases, and
  `test_initial_offsets_bound_active_replay_to_recent_window`) plus
  `StreamRawEventsTests.test_stream_does_not_emit_heartbeats` at L2099-L2128. Both ranges read
  back; the claim is unchanged and still true.

- 2026-07-31T16:40+02:00 — 260731-EFA-L2: the whole-tree `ruff format` pass (`00e8379`) reflowed
  `mcp/src/agents_remember/serving/events.py` and moved the lines this card cites, so the
  Citations column no longer pointed at the code its rows name. Corrected the ranges (L125-L225 →
  L125-L227; L188-L231 → L190-L233). The behaviour described is unchanged — the file's AST is
  identical to the base revision — this is a citation repair only. Verification metadata pinned
  until closeout stamps the L2 commit.

- 2026-07-31T16:10+02:00 — 260731-EFA-L2 curator ATTESTATION: this file was touched by the whole-tree `ruff format` commit (`00e8379`) and by nothing else — `git diff 00e8379 -- <this file>` is empty, so no identifier, signature, branch or behaviour in it changed in this leaf and no claim in this sidecar can have been invalidated by it. Attested, deliberately not rewritten.
- 2026-07-18T12:43+02:00 — FEUI-L9R: documented server-owned record realignment, exact skip/cursor
  semantics, top-level-object admission, and one-parse payload reuse; verification metadata remains
  pinned pending candidate closeout.

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
