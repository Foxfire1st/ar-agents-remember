# mcp/src/agents_remember/serving/_app_terminal_routes.py

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

**Since 260915-CAPS-L15 this route is a wired production launch point for the capsule.** This is the
only production launch point that starts a **free agent**, so it is where a role-only session with no
task document receives instructions. `_open_terminal_response` resolves the launch's instruction
delivery **before any host side effect** through `serving/launch_capsule.py::resolve_launch_capsule`,
taking the compiler across the injected application-rank port (`runtime.capsule_launch`, filled by
`cli/dashboard.py::serving_collaborators` — `serving` ranks below `application` in `layers.toml` and
may not import it). The decision and the record stay here, so this route answers
`capsule`/`legacy`/`refused` exactly as the spawn primitive does.

- A refusal returns **HTTP 400 `capsule-unavailable`** with the role and the gate's own explanation,
  before the opener is called; nothing is started.
- The session's workspace comes from `session_workspace(capsule, server_workspace=config.workspace_root)`
  and the settings selection follows it through `selection_for_workspace`, so the child's cwd,
  `ResolvedLaunch.workspace` and the carrier's own `AR_WORKSPACE_ROOT` are one value.
- The per-run record is published as **`instructionMode`** on the open response, beside the existing
  catalog entry payload: `capsule` with the digest and byte size, or `legacy` with the named decision.

**One measured reachability limit, disclosed rather than smoothed.** This route does **not** set
`TerminalLaunchRequest.session_backend`, so `terminal_launch_detail` checks the harness's argv as a
PATH program — and the **shipped eve row** deliberately is not one (its runtime is the AR-owned Node
application the session adapter starts). A `POST /api/terminal/{id}` naming the shipped eve row
therefore answers `bad-kind` and starts no session. That is **pre-existing** (the base tree answers the
identical refusal), not introduced by this leaf's wiring: the spawn primitive sets
`session_backend=True` for exactly this reason, and the route's launch case therefore teaches an
`orchestration.harnesses` row that names a program on PATH. Owner: **L17**, which either starts the
adapter-owned harness on this route or declares the exclusion by name.

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
- **The instruction delivery is resolved before any host side effect.** A role-configured session is
  never started without its capsule; a refusal is HTTP 400 `capsule-unavailable` with the role and the
  reason, and nothing is started.
- **The session runs where its capsule admits.** The route passes the reconciled workspace to both the
  request and the settings selection; a capsule that admits none (a free agent's Codex capsule, a legacy
  launch) keeps the server's workspace exactly as before.
- **The route decides no policy of its own.** It calls the one gate and reports what that gate answered;
  the compile crosses an injected port because this rank may not import `application`.
- **`session_backend` is deliberately not set here**, and the consequence is stated above rather than
  implied: an adapter-owned harness row is refused on this route as a PATH-program shape.

### Todos

None.

## Evidence

### Docs References

No Domain Documentation source is configured.

### Repo-Internal References

- Session route registration owns terminal open/catalog/assignment endpoints. [1]
- Catalog/open payloads use current structural binding. [2]
- Task assignment delegates validation and generalized mutation. [3]
- The wired launch point: the capsule is resolved before any host side effect, a refusal is HTTP 400 `capsule-unavailable`, the workspace comes from the one rule, and the per-run record rides the response as `instructionMode`. [4]
- The application-rank compiler is injected here rather than imported, because `serving` ranks below `application`. [5]
- The route's launchability question and the pre-existing reason an adapter-owned harness is refused here. [6]
- The cases: a free agent reads its capsule out of its own first prompt through this route, and an un-compilable role refuses before any host effect. [7]

### Cross-Repo References

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
