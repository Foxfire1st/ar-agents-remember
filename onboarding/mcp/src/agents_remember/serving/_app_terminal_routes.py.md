# mcp/src/agents_remember/serving/_app_terminal_routes.py

| Field                  | Value                                            |
| ---------------------- | ------------------------------------------------ |
| repository             | agents-remember                                  |
| path                   | `mcp/src/agents_remember/serving/_app_terminal_routes.py`                                            |
| doc_type               | `file-level-onboarding`                          |
| lastUpdated | 2026-09-15T13:57+02:00 |
| lastVerifiedCommitHash | `6b057238f3b1c6f8ce1420edf48360ef50d3a38f`                                        |
| lastVerifiedCommitDate | 2026-09-15T14:05:57+02:00|
| governingOverview      | `overview.md`                                          |

## Governing Overview

[Serving overview](overview.md)

## Purpose

Owns terminal catalog, open, structural task-assignment, paste/submit, terminate, retire, rename, and
cleanup HTTP route behavior.

## Code Commentary

The WebSocket endpoint attaches only to an already live session. An unavailable attachment closes with 4404; it never creates a replacement process. The bridge carries raw terminal I/O, independently of reliable whole-message adapter submission. On exit it marks a dead process exited, otherwise closes only the attached client, then closes the WebSocket. HTTP callers receive catalog-owned launch/binding facts. cit:([`_serve_terminal_websocket`], mcp/src/agents_remember/serving/_app_terminal_routes.py:86-112).

### Logic

Session-route registration exposes current catalog/open/assignment endpoints. Catalog/open payloads
serialize task-document binding and staged replacement. `_attach_task_response` validates the real
document against topology, applies the generalized assignment primitive, and maps strict success or
refusal models.
The HTTP retirement path now projects both actor and target reviewer parent stamps into `SeatRef`
before calling the same central retirement policy as the MCP path. Thus a sprint architect cannot
retire an orchestrator-owned super reviewer merely because both generations share the sprint
reviewer address.

### Conventions

HTTP routes may use a runtime session id to select the occupant being operated on; the binding itself
is task document plus role.

### Invariants And Boundaries

- No attach-leaf endpoint or leaf-ref compatibility response remains.
- Assignment refuses invalid altitude and occupied singular seats without mutation.
- Open and catalog payloads return server-owned current facts.
- HTTP retirement carries the generation-bound reviewer parent pair into the single authority
  policy; the route does not reimplement ownership.
- `GET /api/terminal/sessions` is a **projection**, never a producer: it serializes whatever the
  catalog already holds and cannot itself make that snapshot newer. It names no sweeper, probes no
  adapter, advances no evidence cursor, rewrites no row, and compacts nothing.

### Todos

None.

## Docs References

No Domain Documentation source is configured.

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| Session route registration owns terminal open/catalog/assignment endpoints. | `_register_terminal_session_routes` | mcp/src/agents_remember/serving/_app_terminal_routes.py:130-205 |
| Catalog/open payloads use current structural binding. | `_terminal_entry_payload` | mcp/src/agents_remember/serving/_app_terminal_routes.py:207-333 |
| Task assignment delegates validation and generalized mutation. | `_attach_task_response` | mcp/src/agents_remember/serving/_app_terminal_routes.py:335-388 |

## Cross-Repo References

No cross-repository implementation dependency governs this file.

## 260831-LOCR-R02 Current Delta — The Catalog GET Is A Projection, Not A Producer

`api_terminal_sessions` returns `{"sessions": [_catalog_payload(entry) for entry in
runtime.catalog.list()]}` under the unchanged `@app.get("/api/terminal/sessions",
response_model=TerminalSessionsResponse, response_model_exclude_unset=True)` declaration. The module
no longer names `liveness_sweeper` at all. Steady-state observation belongs to the serving lifespan
(`_app_lifespan.py::_terminal_observation_loop`, landed as `260831-LOCR-L01` @ `163ba8a9`), which
calls the existing sweeper on its own completion-relative clock; this leaf removes the route as a
second driver of that same sweep.

**Why `list()` and not `list_committed()`.** This was settled by measurement, not by argument.
`TerminalCatalog.batch()` holds `exclusive_terminal_catalog_lock(path)` **and** `self._lock` across
the whole unit of work, so a foreign thread blocks on the `RLock` and then reads the committed atomic
file: with a batch in flight, `list()` blocked 0.424 s and returned rows byte-equal to the committed
on-disk file, while `list_committed()` returned a demonstrably **older** pre-batch snapshot in 0.1 ms.
`list_committed()` is the sweeper's own non-blocking lock-contention read — its only two callers are
`TerminalCatalogLivenessSweeper.refresh` and `_refresh_starting_rows`, each immediately after a
failed non-blocking acquire. Importing a contention workaround into a projection would invert the
intent, so the route uses the ordinary port read: `list()` and `get()` both reach `_read_snapshot()`
under the thread lock, and `active_for_task()` is `list()`-based, while `list_committed()` is the only
read that skips that lock by going straight to `_read_disk()`.

**The accepted trade-off is stated rather than hidden.** A GET may wait for an in-flight batch to
commit. That wait is bounded (per-row probe timeouts times the selected rows), it lands on a
threadpool worker because the handler is a plain `def` — never the event loop — and it is strictly
*smaller* than the behaviour it replaced, where the same request thread ran a full sweep (probes,
cursor writes, compaction) inline. The handler's own comment claims `list()` can return "the in-flight
batch buffer when this instance owns one"; that branch is unreachable for this handler, because the
buffer is reachable only reentrantly by the batch-owning thread, which a request thread never is.
The behaviour is correct; only the sentence is imprecise.

**Failure behaviour.** A stale or failed observer does not change the route's answer: the GET serves
the stored snapshot and the observer-health surface identifies the producer fault. There is no
compatibility `refresh()`, no `list_committed()` "repair" fallback, and no `except` that would swallow
a broken catalog — a raising read surfaces instead.

**Recorded limit.** The regression module `mcp/tests/test_serving_terminal_catalog_read.py` pins the
Forbidden-Overreach clause by object identity across every module-global reader binding shape. It does
**not** cover every binding shape: a reader reached through a module-singleton function default (for
example `DEFAULT_LIVENESS_PROBE.snapshot_reader(entry)`) still passes the module. That residue is a
disclosed limit of the instrument, measured by the independent reviewer and deliberately banked for a
hardening leaf — closing it properly means patching a seam both shapes share (the transport/exchange
function), which is a scope decision rather than a leaf repair. The card states the limit so no reader
mistakes the instrument for a total guarantee.

## L23 Dashboard Refusal Transport

Terminal open and task-attach routes map source-lineage refusals to HTTP 409 and
preserve status, detail, and the strict projection. The dashboard receives
operator-actionable evidence while the catalog remains unchanged.

## Update History

- 2026-09-15T13:57+02:00 — 260831-LOCR-L02 curator (uncommitted change set on `ar/260831-locr-l02`,
  base `67b21aeb`): body update, not a history-only note. `api_terminal_sessions` stopped calling
  `runtime.liveness_sweeper.refresh()` and now serializes `runtime.catalog.list()`; the module names
  no sweeper. The card gained the projection invariant in `### Invariants And Boundaries` and the
  `## 260831-LOCR-R02 Current Delta` section, which records why `list()` rather than
  `list_committed()` was ruled correct by measurement (a request thread blocks on the batch `RLock`
  and then reads committed bytes, while `list_committed()` is the sweeper's own contention read and
  returned a demonstrably older snapshot), the accepted bounded-blocking trade-off, the no-fallback
  failure behaviour, and the measured residual reach limit of the new regression instrument. Route
  path, declared model, conditional-key behaviour and status semantics are unchanged. Verification
  metadata stays closeout-owned: the candidate is uncommitted, so `lastVerifiedCommitHash` remains
  pinned to the last commit that actually verified this card.

- 2026-09-06T22:06:54+00:00 — Preserved source-verified runtime semantics from retired test onboarding; no removed coverage is claimed and verification pins are unchanged.
- 2026-08-31T04:59+02:00 — 260821-ARSPAWN-L5 independent-review repair: recorded HTTP retirement
  propagation of reviewer parent provenance into the shared plane-specific authority policy.
  Verification remains closeout-owned.

- 2026-08-12T20:10+02:00 — L23 curator: documented HTTP transport of lineage admission failures; verification remains closeout-owned.

- 2026-08-11T19:58+02:00 — Aligned the current serving card for `_app_terminal_routes.py` with seat ownership, delivery, lifecycle, and terminal boundaries represented by this source.
- 2026-08-08T17:18+02:00 — No content impact: 260731-EFA-L9 rewrote this source's imports/callers only (model-extraction caller wave); the behavior this card documents is unchanged and the body was re-verified current. Verification metadata pinned until closeout stamps the L9 code commit.

- 2026-08-07T22:45:00+02:00 — 260731-EFA-L7 curator: created this file-level onboarding card for the split module; content derived from the current worktree source. Verification metadata pinned until closeout stamps the 260731-EFA-L7 commit.
