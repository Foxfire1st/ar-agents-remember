# mcp/src/agents_remember/serving/app.py

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember                            |
| path                   | `mcp/src/agents_remember/serving/app.py`   |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-07-02T17:04+02:00                    |
| lastVerifiedCommitHash | `ad30dd38c3dcfa13fb85f44b281488499e92519a` |
| lastVerifiedCommitDate | 2026-07-03T08:10:19+02:00|
| governingOverview      | `overview.md`                              |

## Governing Overview

[overview.md](overview.md)

## Purpose

`app.py` builds the dashboard FastAPI app over the observer projection: the one-shot
`GET /api/state`, the multiplexed `GET /api/stream` (`state`) SSE endpoint, the raw
`GET /api/events` SSE channel (4b), the `POST /api/actions/{action}` plane (4b/6b), the
`@app.websocket("/api/terminal/{session}")` Mode B2 terminal bridge (6d-2), the
`POST /api/operator-inbox` external-chat response channel, lifecycle-scoped attention dismissals via
`POST /api/actions/dismiss`, the durable terminal-session catalog
surface (`GET /api/terminal/sessions`, catalog-backed per-WebSocket tmux-client attach, and explicit
`POST /api/terminal/{session}/terminate`), the `POST /api/terminal/{session}` opener that ensures a
detached tmux session — a shell or a detected harness (6e-2a/6e-2b) — the L5/L9
`POST /api/terminal/{session}/attach-leaf` leaf-claim/move route, the `GET /api/harnesses` detection
endpoint (6e-2b), image upload under a live or catalog-restored cwd, the read-only `/api/files/*` files API
(operations-integration L1) and the read-only `/api/changeset/*` change-set API (L3) — both registered
just before the static mount — and the static mount. It is the
slice-04 transport spine plus the external-chat fallback and Mode B2 terminal.

## Code Commentary

`create_app(config, *, interval=1.0, now=None, before_tick=None, refresh_provider_state=None,
terminal_host=None, terminal_catalog=None)`
constructs a `Projector` (threading `now`/`before_tick` straight through — the **sim seams**;
both default to live behaviour) plus a `TerminalHost` (`terminal_host` defaults to a fresh one;
tests inject a fake) and a `TerminalCatalog` at `coordination_root/logs/dashboard/terminal-sessions.json`
(`terminal_catalog` is test-injectable). It wires a FastAPI `lifespan` that `prime()`s the projector
(one initial projection), runs its tick loop as a task, and on shutdown cancels that task and calls
`host.shutdown()`. Endpoints:

When `refresh_provider_state` is left as `None`, live mode (`before_tick is None`)
constructs a `ProviderStateRefresher`, while sim mode disables provider refresh so replayed
fixtures stay deterministic. Tests can still force either branch explicitly.

- `GET /api/state` returns the current projection once as `model_dump(by_alias=True,
  exclude_none=True)` (503 until the first projection exists) — curl-friendly, no streaming.
- `GET /api/stream` (`response_class=EventSourceResponse`) delegates to the module-level
  `stream_events(projector)` so the sequence is unit-testable without an HTTP client.
- `GET /api/events` (`response_class=EventSourceResponse`) delegates to
  `serving.events.stream_raw_events(config, last_event_id=…)`, reading the `Last-Event-ID`
  header via `Annotated[str | None, Header()]` for exact byte-offset resume. It is a *separate*
  stream from `/api/stream` (raw byte-offset resume vs. snapshot resume).
- `POST /api/actions/{action}` parses an `ActionRequest`, calls the pure
  `serving.actions.evaluate_action` (now=`now_iso()`), and returns its `ActionOutcome` as a
  `JSONResponse` (503 when no projection yet). For a gate-decision verb (slice 6b) it then calls
  `gate_decide_for_lifecycle(config, … expected_gate_id=gateId, note=note,
  decided_by="developer", decided_via="dashboard")` and merges the gate result. For a `cancel` that
  carries only `gateId` and no lifecycle target, it calls `gate_decide_payload` against the workspace
  gate log so old malformed attention rows can be physically deleted. No open gate returns
  `409 {"status":"no-open-gate"}`; a mismatched targeted gate returns
  `409 {"status":"stale-gate"}`; lifecycle transitions stay no-mutation. For the task-28 `dismiss`
  verb, a non-gate lifecycle attention item is written through `AttentionDismissalStore.dismiss` as a
  compact current acknowledgement; a `gate-open` dismiss calls `gate_decide_payload(..., decision="cancel")`
  and does not write an acknowledgement row because deleting the gate consumes the source item; an
  `actionable-drift` dismiss writes a targetless repo-level current acknowledgement because its source is
  the drift snapshot rather than a lifecycle.
- `POST /api/operator-inbox` parses `OperatorInboxPostRequest` (`lifecycleId` / `agentId` /
  `gateId` aliases plus `ask` and `response`) and calls `operator_inbox_post_payload` with
  `created_by="developer"` and `created_via="dashboard"`. This is the trusted dashboard write side
  for task-10 external-chat responses when no hosted chat session can receive direct injection.
  Missing lifecycle/agent addressing returns `400 {"status":"bad-address"}` from the builder's
  address validation.
- `POST /api/operator-inbox/{entry_id}/dismiss` physically deletes a pending operator-inbox entry.
  This is the trusted dashboard path used by the dismissible `check chat` task-row warning; it clears
  developer-side noise without marking the entry as agent-consumed.
- `@app.websocket("/api/terminal/{session}")` (slice 6d-2) bridges the Mode B2 terminal host to
  the browser: it `accept()`s, looks up the catalog row, probes tmux, and calls
  `host.attach(..., name=entry.tmux_name)` so this WebSocket gets its own tmux client PTY attached to
  the same durable tmux session. If the row is unknown/non-running or tmux no longer has the session, it
  marks a stale catalog row `exited` and `close(code=4404)`. PTY output is queued via
  `loop.add_reader(master_fd)` (no polling) and sent as **binary** frames (raw VT bytes for
  xterm.js); an EOF sentinel emits the `{"type":"exit"}` text frame then closes. Inbound text
  frames go through `_apply_terminal_session_input` → `host.write_session` (a `{type:"stdin",data}`) /
  `host.resize_session` (a `{type:"resize",cols,rows}`); child-exit and client-disconnect each cancel the
  other pump. `_bridge_terminal` removes the event-loop reader through a one-shot helper because child
  exit can remove it before the bridge `finally`, and closed fd numbers can be reused by other transports.
  **Attach-only** — the session is opened by the `POST` opener below. A normal browser
  disconnect drops only that concrete PTY/tmux client with `host.close_session(session_obj)` while
  leaving the tmux session and catalog row running, so refreshes and second browser tabs attach with
  their own clients instead of competing to read or close one fd; child exit updates the durable catalog
  status to `exited`.
- `GET /api/terminal/sessions` returns catalog rows after refreshing stale `running` rows. A running row
  with an in-process dead child or no in-process session and no tmux match becomes `exited`; explicitly
  terminated rows are filtered by the catalog.
- `POST /api/terminal/{session}` (slice 6e-2a/6e-2b) is the **opener**: the dashboard ensures a
  detached durable tmux session, then the WebSocket attaches with a per-tab client. `TerminalOpenRequest` carries a `kind` (+ optional `harness`),
  a display `label`, `lifecycleId`, and (L5) `leafKey` (alias `leafKey`); `resolve_terminal_launch(kind, workspace_root, shell, harness)` maps it to `(cwd, argv)`
  **server-side** — `kind="terminal"` ⇒ `[$SHELL]` (`os.environ["SHELL"]` or `/bin/bash`),
  `kind="harness"` ⇒ the registry argv for `harness` (rejecting an absent / unknown / not-installed
  id), both at `config.workspace_root`; only ids are on the wire, never an argv. **L5** then calls
  `_claim_leaf_or_409(catalog, leaf_key, session, role=role_for_kind(kind))` *before* the spawn so a leaf
  already owned by a **different running session of the same role** is refused `409
  {"status":"leaf-taken","leafKey","session"}` (self-reclaim is allowed). The guard is **role-scoped**
  (L5 fix 2): a `kind="terminal"` open claims the terminal slot and a `kind="harness"` open claims the
  chat slot, so opening a terminal never 409s against the leaf's agent chat and vice-versa — a leaf can hold
  one running chat AND one running terminal. `host.ensure(...,
  suspend_unsafe=(kind=="harness"))` returns the tmux binding (200; a bad kind/harness ⇒ 400), and the route
  upserts a `TerminalCatalogEntry` carrying the label, kind, optional harness/lifecycle, cwd, tmux name,
  command argv, timestamps, `running` status, and `leaf_key=request.leaf_key or (existing.leaf_key …)` (an
  explicit key claims now; otherwise an existing binding is preserved across re-open/reconnect). The 200
  body echoes the persisted `leafKey`. There is no starter PTY client to close, so a brand-new
  row stays backed by tmux until the first WebSocket attaches. A bare-pane harness is opened
  suspend-unsafe so the host strips Ctrl-Z for it (slice 6f); a shell is not.
- `POST /api/terminal/{session}/attach-leaf` claims or **moves** a leaf for an **existing** session from
  the Chats page — enclosure-free, no respawn. `TerminalAttachLeafRequest` carries the required `leafKey`;
  the route delegates to `assign_terminal_session_to_leaf(catalog, session_id, leaf_key)`, so browser
  actions and the agent-facing MCP tool share one server-authoritative catalog policy. The result maps to
  `404 {"status":"unknown-session"}` for an unknown/terminated session, `409 {"status":"leaf-taken",...}`
  when a different running session of the same role owns the target leaf, and
  `200 {"session","status":"attached","leafKey"}` after persisting `entry.with_leaf_key(leaf_key)`.
  A conflict does not mutate the catalog.
- `POST /api/terminal/{session}/terminate` is the destructive terminal action. It accepts either a live
  host session or a catalog row, kills the tmux session through `TerminalHost.terminate`, marks the
  catalog row `terminated`, and returns `404 unknown-session` only when neither exists.
- `GET /api/harnesses` (slice 6e-2b) returns `{"harnesses":[{id,name,detected}]}` from
  `serving.harnesses.detect_harnesses()` (`shutil.which` per harness) — the dashboard renders a launch
  button per *detected* harness.
- `POST /api/terminal/{session}/image` (slice 6f) saves a pasted screenshot under the session cwd so the
  highlight composer can inject its on-disk path (the terminal channel is text-only). It validates the
  live host session or catalog row (unknown ⇒ 404), the declared `Content-Length` (over
  `_MAX_IMAGE_BYTES` + slop ⇒ 413 fast), the extension against `_IMAGE_EXTS`, then the body (oversize ⇒
  413; empty or a failed `_looks_like_image` magic-byte sniff ⇒ 400), and writes
  `<cwd>/.dashboard-pastes/<uuid>.<ext>` (uuid
  basename ⇒ no traversal), returning `{path}`. Same localhost posture; unlike the JSON POSTs it is
  multipart (a preflight-free "simple request"), but the write target is keyed by an unguessable session
  UUID. Needs `python-multipart` (for `UploadFile`).
- `register_files_routes(app, config)` (operations-integration L1) registers the read-only
  `GET /api/files/{repos,list,read,onboarding}` routes **before** `mount_static`, so the greedy `/`
  SPA mount cannot swallow them. The handlers live in `serving/files.py`.
- `register_changeset_routes(app, config)` (operations-integration L3) registers the read-only
  `GET /api/changeset/{task,file-diff,master}` change-set routes immediately after the files routes and
  still **before** `mount_static` (L711-L713). The handlers live in `serving/changeset.py`.

`stream_events(projector)` yields an `event:snapshot` with the full projection on connect, then
per-entity delta events from `projector.subscribe()`. `_encode` dumps projection nodes by alias
(camelCase, `exclude_none`) and passes removal markers (`{key: id}`) through as-is. SSE uses
built-in `fastapi.sse` (`EventSourceResponse`/`ServerSentEvent`, auto keep-alive).

## Invariants And Boundaries

- **Local-first:** bound to `127.0.0.1` by the CLI default, no auth in v1; the module docstring
  records the "do not tunnel it" posture (it now also exposes the POST action surface). The UI
  is never the gate enforcement.
- **Transport + explicit local writes:** serves the `WorkspaceProjection` nodes verbatim (NS #2, no
  interpretation). Lifecycle-transition POSTs stay no-mutation, a lifecycle-targeted gate-decision
  POST records a developer-attributed decision via `gate_decide_for_lifecycle`, gate-id-only `cancel`
  records and deletes a workspace gate via `gate_decide_payload`, `POST /api/operator-inbox`
  records a developer/dashboard response for external-agent polling, and
  `POST /api/operator-inbox/{entry_id}/dismiss` deletes stale pending inbox warnings. Task-28 attention
  `dismiss` records lifecycle-scoped current acknowledgement rows plus targetless actionable-drift rows,
  while gate-open dismiss consumes the gate source by cancellation/deletion. The UI is still never the gate
  *enforcement* — the mutating MCP tools bind it.
- **Two SSE channels, two resume models:** the `state` channel re-snapshots on reconnect; the
  raw `event` channel resumes by exact byte offset (`Last-Event-ID`). They stay separate.
- **Terminal bridge (6d-2):** binary-out / JSON-text-in over one WebSocket; the wire carries only
  `stdin`/`resize` control shapes, never a command (the host spawns a fixed argv). Attach-only,
  localhost-bound like the rest; the bridge helpers (`_bridge_terminal` / `_terminal_to_socket` /
  `_socket_to_terminal` / `_apply_terminal_input` / `_apply_terminal_session_input`) are module-level for
  unit testability. WebSocket attach always probes tmux before calling `host.attach`, so a stale catalog
  row never recreates a fresh session by accident. Browser disconnect detaches only that connection's
  PTY client but does not mark the row exited; the fd reader is removed at most once during cleanup; tmux
  remains the persistence boundary and can serve multiple browser tabs at once.
- **Terminal catalog boundary:** `terminal_catalog.py` owns JSON persistence and filtering semantics;
  this module owns HTTP/WebSocket orchestration and status refresh.
- **Leaf registry (L5):** the catalog is the leaf→chat registry and the server is the uniqueness
  arbiter — at most one *running* session per **(leaf, role)**, enforced by `_claim_leaf_or_409` on both the
  opener (`role=role_for_kind(kind)`) and `attach-leaf` (`role=entry.role`). A **chat** (any harness) and a
  **terminal** (a shell) are separate slots, so a leaf can hold one running chat AND one running terminal,
  and a terminal never conflicts with the leaf's chat. `leaf_key` is opaque here (a qualified leaf id or a
  reserved `master:<…>` key flow identically); the binding is enclosure-independent and survives finalize,
  and a dead/exited session frees its slot because `active_for_leaf` gates on `status == "running"`.
- **Sim is a seam, not a fork:** `now`/`before_tick` default to live; `cli.dashboard` passes a
  replay clock + fixture feeder under `--sim` and the path is otherwise byte-identical.
- `McpRuntimeConfig`/`datetime` are imported under `TYPE_CHECKING` (config is only passed on).

## Repo-Internal References

| Finding | Source Path |
| --- | --- |
| The shared tick/fan-out loop the app drives (with the `now`/`before_tick` seams). | [projector.py](agents-remember/mcp/src/agents_remember/serving/projector.py) |
| The raw `event` channel `/api/events` delegates to. | [events.py](agents-remember/mcp/src/agents_remember/serving/events.py) |
| The pure action evaluation `/api/actions/{action}` delegates to. | [actions.py](agents-remember/mcp/src/agents_remember/serving/actions.py) |
| The gate write-path the router calls for a gate-decision verb (slice 6b). | [mcp/tools/gates.py](agents-remember/mcp/src/agents_remember/mcp/tools/gates.py) |
| The operator inbox payload builder used by `/api/operator-inbox`. | [mcp/tools/operator_inbox.py](agents-remember/mcp/src/agents_remember/mcp/tools/operator_inbox.py) |
| The Mode B2 terminal host the `/api/terminal` WebSocket bridges to (slice 6d), including tmux probe/kill hooks used for durability. | L86-L121; L230-L239; L287-L289; L340-L347 | [terminal.py](terminal.py) |
| The durable terminal-session catalog persisted by the opener, sessions endpoint, and terminate route. | L15-L30; L110-L185 | [terminal_catalog.py](terminal_catalog.py) |
| The shared leaf reassignment helper used by this route and the agent-facing MCP tool. | L45-L83 | [terminal_leaf_assignment.py](terminal_leaf_assignment.py) |
| The harness launch registry the opener + `/api/harnesses` consume (slice 6e-2b). | [harnesses.py](agents-remember/mcp/src/agents_remember/serving/harnesses.py) |
| The static-bundle resolver/mount. | [static.py](agents-remember/mcp/src/agents_remember/serving/static.py) |
| The read-only files API registered just before the static mount (operations-integration L1). | [files.py](agents-remember/mcp/src/agents_remember/serving/files.py) |
| The read-only change-set API registered right after the files routes (operations-integration L3). | [changeset.py](agents-remember/mcp/src/agents_remember/serving/changeset.py) |
| The served projection shape + `ActionAvailability`. | [observer/projection.py](agents-remember/mcp/src/agents_remember/observer/projection.py) |
| The CLI adapter that builds and serves this app (and wires sim). | [cli/dashboard.py](agents-remember/mcp/src/agents_remember/cli/dashboard.py) |

## Update History

- 2026-07-02T17:04+02:00 — L9: `attach-leaf` is now a true move/reassign route. It delegates to
  `serving.terminal_leaf_assignment.assign_terminal_session_to_leaf`, so dashboard clicks and the
  agent-facing MCP tool share the same catalog uniqueness policy; `leaf-taken` returns 409 without
  mutating the row. Verification metadata pinned until closeout stamps the L9 commit.
- 2026-06-30T00:00:00+02:00 — L5 follow-up: `_claim_leaf_or_409` is now **role-aware** — it takes a `role` kwarg and
  probes `catalog.active_for_leaf(leaf_key, role=role)`, so uniqueness is per **(leaf, role)**. The opener
  passes `role_for_kind(kind)` and `attach-leaf` passes the existing `entry.role`, so a terminal can sit
  beside the leaf's agent chat (no 409) while a second chat / second terminal still 409s. Updated the
  opener + attach-leaf bullets and the Leaf-registry invariant. Verification metadata pinned until closeout
  stamps the L5 commit.
- 2026-06-30T00:00:00+02:00 — L5 (Sidebar chat: leaf-keyed attachment): `TerminalOpenRequest` gained `leaf_key` (alias
  `leafKey`); a new `TerminalAttachLeafRequest` + `POST /api/terminal/{session}/attach-leaf` claim a leaf
  for an existing session (404 unknown/terminated). The shared `_claim_leaf_or_409` helper is the
  server-authoritative uniqueness guard (`409 {"status":"leaf-taken","leafKey","session"}` when a
  *different* running chat owns the leaf, self-reclaim allowed), called by both the opener and attach-leaf
  before the catalog upsert; the opener now claims + persists `leaf_key` (preserving an existing binding
  when none is sent) and echoes `leafKey`. Verification metadata pinned until closeout stamps the L5
  commit.
- 2026-06-29T15:30+02:00 — operations-integration L3: `create_app` now also calls `register_changeset_routes(app, config)` between `register_files_routes` and `mount_static` (L711-L713), mounting the read-only `/api/changeset/{task,file-diff,master}` change-set API (handlers in `serving/changeset.py`) — registered before the greedy `/` static mount. Verification metadata pinned to the task base until closeout stamps the L3 code commit.
- 2026-06-28T22:41+02:00 — operations-integration L1: `create_app` now calls `register_files_routes(app, config)` immediately before `mount_static`, mounting the read-only `/api/files/{repos,list,read,onboarding}` files API (handlers in `serving/files.py`). Registered before the greedy `/` static mount so it cannot swallow them. Verification metadata pinned until closeout stamps the L1 code commit.
- 2026-06-28T07:32+02:00 — Task 29 S7 follow-up: `/api/actions/dismiss` now persists targetless
  actionable-drift acknowledgements while keeping gate-open dismissal source-consuming and lifecycle
  dismissals lifecycle-scoped. Verification metadata pinned until closeout stamps the task-29 code commit.
- 2026-06-28T03:52+02:00 — Task 28 S5.2 after source sync: `/api/actions/dismiss`
  now writes compact lifecycle-scoped attention acknowledgements for non-gate items and consumes
  gate-open items by cancelling/deleting the gate without appending a stale marker. Verification
  metadata pinned until closeout stamps the task-28 code commit.
- 2026-06-27T23:08+02:00 — Task 31 provider-state honesty: live dashboard apps now attach a provider refresher by default, while sim/replay apps keep provider refresh disabled unless explicitly requested. Verification metadata pinned until closeout stamps the code commit.
- 2026-06-27T02:28+02:00 — Task 22 follow-up: the opener now calls `TerminalHost.ensure`
  instead of `open` followed by `close`, creating a detached tmux session with no starter PTY client.
  This fixes new chats immediately rendering `session ended` while preserving catalog-first
  per-WebSocket attach. Verification metadata pinned until closeout stamps the task-22 follow-up code
  commit.
- 2026-06-27T01:25+02:00 — Task 22 follow-up: WebSocket attach is now catalog-first and creates one
  unregistered `TerminalHost.attach` client per browser connection; the bridge reads/writes/resizes the
  concrete session object and disconnect closes only that attachment. The opener detaches its starter
  client after persisting the catalog row. Bridge reader cleanup is now one-shot so child exit and
  disconnect cannot double-remove a reused fd. This fixes multi-tab shared-chat behavior and removes
  shared-PTY read/close contention. Verification metadata pinned until closeout stamps the task-22
  follow-up code commit.
- 2026-06-27T00:45+02:00 — Task 22 follow-up: WebSocket disconnect now closes only the local
  `TerminalHost` attachment while preserving the running tmux/catalog row, so refresh reconnects via a
  fresh tmux attach and restores the terminal screen.
- 2026-06-26T23:05+02:00 — Task 22: added durable dashboard terminal-session catalog orchestration.
  `create_app` now owns a `TerminalCatalog`; the opener persists labels, lifecycle ids, cwd, tmux name,
  command, timestamps, and running status; WebSocket attach rehydrates catalog rows only after a tmux
  probe; `GET /api/terminal/sessions` refreshes stale rows; `POST /api/terminal/{session}/terminate`
  kills the tmux session and marks rows terminated; image upload can use a catalog cwd after a dashboard
  restart. Verification metadata pinned until closeout stamps the task-22 code commit.
- 2026-06-25T14:02+02:00 — Task 24 reopened: `/api/actions/cancel` can delete a workspace-shaped gate by `gateId` when the request has no lifecycle target, keeping approve/reject/revision lifecycle-targeted.
- 2026-06-25T13:20+02:00 — Task 23/24: added `POST /api/operator-inbox/{entry_id}/dismiss` so stale pickup warnings can delete pending throwaway inbox entries.
- 2026-06-25T07:17+02:00 — Task 19: `/api/actions/{approve,reject}` now forwards targeted `gateId` and optional `note` into `gate_decide_for_lifecycle`, distinguishes stale gate 409s from no-open-gate 409s, and preserves the operator-inbox fallback endpoint as the message-only Chat return path. Verification metadata pinned until closeout stamps the task-19 code commit.
- 2026-06-23T15:05+02:00 — Task 10 dashboard fallback: added `OperatorInboxPostRequest` and `POST /api/operator-inbox`, which writes trusted developer/dashboard responses through `operator_inbox_post_payload` for external chats when no hosted session is available. Verification metadata pinned until closeout stamps the task-10 code commit.
- 2026-06-19T20:30 — Task 6 slice 6f: added `POST /api/terminal/{session}/image` (save a validated — extension + magic bytes + size — pasted screenshot under `<cwd>/.dashboard-pastes/<uuid>.<ext>`, return its path; unknown session ⇒ 404, missing cwd ⇒ 409, oversize ⇒ 413, bad/empty body ⇒ 400) with the `_IMAGE_EXTS`/`_MAX_IMAGE_BYTES`/`_looks_like_image` helpers, and the opener now passes `suspend_unsafe=(kind=="harness")` to `host.open` so the host strips Ctrl-Z for bare-pane harnesses only (a shell keeps job control). `python-multipart` added to deps for `UploadFile`. Verification metadata pinned until closeout stamps the 6f code commit.
- 2026-06-18T21:27+02:00 — Task 6 slice 6e-2b: added `GET /api/harnesses` (`detect_harnesses()` → `{id,name,detected}` per `shutil.which`) and extended the opener — `TerminalOpenRequest` gained `harness`, `resolve_terminal_launch` gained a `kind="harness"` branch resolving the `serving.harnesses` registry argv (absent/unknown/not-installed ⇒ 400). Updated Purpose, the opener/GET Code Commentary bullets, and the references. Verification metadata pinned until closeout stamps the 6e-2b code commit.
- 2026-06-18T17:40+02:00 — Task 6 slice 6e-2a: added the `POST /api/terminal/{session}` **opener** — the dashboard spawns + owns a session (`TerminalOpenRequest` `kind` → `resolve_terminal_launch` → `host.open(cwd=workspace_root, command=[$SHELL])`; server-resolved command, unknown kind ⇒ 400), so the WebSocket has a real session to attach to ("＋ Terminal" works). Harness kinds are 6e-2b. Verification metadata pinned until closeout stamps the 6e-2a code commit.
- 2026-06-18T16:10+02:00 — Task 6 slice 6d-2: added the `@app.websocket("/api/terminal/{session}")` Mode B2 bridge (attach to `host.get(session)` or `close(4404)`; PTY output via `loop.add_reader` → binary frames; `{type:stdin|resize}` text frames in via the pure `_apply_terminal_input`; child-exit → `{type:exit}`; tmux-persistent on disconnect) + the module-level bridge helpers, and the `terminal_host` `create_app` param (+ `host.shutdown()` on lifespan teardown). Verification metadata pinned until closeout stamps the 6d-2 code commit.
- 2026-06-18T12:10+02:00 — Task 6 slice 6b: `POST /api/actions/{action}` now executes a gate-decision verb as a developer/dashboard-attributed gate decision (`gate_decide_for_lifecycle`; no open gate ⇒ 409), beyond the 4b no-mutation skeleton that still governs lifecycle transitions. Verification metadata pinned until closeout stamps the 6b code commit.
- 2026-06-14T11:30+02:00 — Updated for slice 04 commit 4b: added `GET /api/events` (raw channel
  with `Last-Event-ID` resume) and `POST /api/actions/{action}` (the no-mutation action
  skeleton), and the `now`/`before_tick` sim seams on `create_app`. Verification metadata pinned
  until closeout stamps the 4b code commit.
- 2026-06-14T11:30+02:00 — Created for slice 04 commit 4a: `create_app` + the `state` SSE
  channel (snapshot + per-entity deltas) + one-shot `/api/state` + static mount. The raw
  `event` channel and POST action skeleton land in 4b. Verification metadata pinned until
  closeout stamps the 4a code commit.
