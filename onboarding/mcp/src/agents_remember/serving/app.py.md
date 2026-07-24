# mcp/src/agents_remember/serving/app.py

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember                            |
| path                   | `mcp/src/agents_remember/serving/app.py`   |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-07-19T00:06+02:00 |
| lastVerifiedCommitHash | `842b487b854503d95c9c2d9dce1841198ba93c7d` |
| lastVerifiedCommitDate | 2026-07-24T17:08:25+02:00|
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
detached tmux session — a shell or a detected harness (6e-2a/6e-2b), and since **L2** through the shared
`serving.terminal_opener.open_terminal_session` so this route and the agent-facing `spawn_agent_session`
MCP tool spawn through ONE opener — the native capability/control surface
(`GET /api/harnesses/{harness}/capabilities`, live capability and model/effort set, whole-message
submit, and same-id reconcile), the L5/L9
`POST /api/terminal/{session}/attach-leaf` leaf-claim/move route, the **L2**
`POST /api/terminal/{session}/paste` server-side harness-log-verified context-packet delivery, the `GET /api/harnesses` detection
endpoint (6e-2b), the **260707-HFX-L8** `POST /api/terminal/{session}/retire` (server-authoritative
seat retirement with authority policy) and `POST /api/terminal/{session}/rename` (post-spawn
identity rename) endpoints, the **260707-HFX2-L11** landed-archive cleanup endpoint
(`POST /api/terminal/landed-cleanup`), image upload under a live or catalog-restored cwd, the read-only `/api/files/*` files API
(operations-integration L1) and the read-only `/api/changeset/*` change-set API (L3) — both registered
just before the static mount — and the static mount. It is the
slice-04 transport spine plus the external-chat fallback and Mode B2 terminal.

## Code Commentary

### FEUI-L9R Reviewed Candidate Delta

`GET /api/harnesses` now returns only the server-owned pre-session discovery facts `id`, `name`,
and `detected`. It no longer calls `protocol_adapter_status` or emits `control`, because no session
adapter process exists before open. Runtime session/control evidence remains on its existing
post-open authorities; this endpoint is deliberately narrow.

### MX-FIX-1 Atomic Folded-State Stream Boundary

`stream_events()` no longer performs an app-owned `current()` read followed by a later subscription.
It opens exactly one `Projector.subscribe()` iterator, whose queue is already registered when its
current snapshot is captured. The app remains wire-only: it aliases/serializes each projector event,
adds `servingBuild` and `supervisorHeartbeat` to every `snapshot` event (initial or first-recovery),
and preserves the existing event name, sequence id, and `retry=2000` framing. The iterator is wrapped
in `contextlib.aclosing()` so disconnect/cancellation closes the inner subscription immediately.

### 260718-CHATS-L0 Conversation Runtime Composition

The single `register_harness_control_routes(...)` call now also passes
`coordination_root=config.coordination_root` so the harness-control seam can construct the one
immutable `ConversationRuntime` (scope = workspace + coordination roots) and install it on
`app.state` exactly once. This remains the app's only conversation-composition edit: no
`register_conversation_routes` or `include_router` call appears in this file, and later child
leaves add behavior without touching `create_app`.

### Logic

`create_app` constructs the shared projector, terminal/catalog/liveness services, supervisor and
metrics loops, then registers HTTP, SSE, WebSocket, and delegated route modules before the static
mount. Request handlers stay composition-focused: domain behavior remains in the serving modules
and stores they call.

### 260714-ACPUI-L4 Native Capability And Control Composition

`TerminalOpenRequest` accepts optional `model` and `effort`. The route requires either neither or a
complete pair for an AR built-in native harness, resolves it once into the existing `ResolvedLaunch`,
and passes it through the shared opener. A live same-id reopen returns facts from the retained
catalog row; a changed kind, harness, cwd, or explicit pair maps to `409 launch-selection-conflict`
with the actual row and no host/catalog mutation. Successful responses
also source kind, harness, lifecycle, control endpoint/protocol, and resolved pair from that actual
entry rather than echoing attempted request values.

`create_app` registers `harness_control_api` before the static mount and may inject one
`HarnessCapabilityCatalog` for tests. Pre-session advertise is dynamic, token-free, cached by the
installed native executable fingerprint, and explicitly refreshable. Live advertise/set/submit/
reconcile routes address the exact running control endpoint after liveness. Submit is one complete
message with caller-owned request id, never composer paste. Public receipts preserve normalized
acceptance/correlation while omitting private raw adapter evidence; async output remains on the
existing SSE, terminal, transcript, and durable inter-agent bus surfaces.

### 260707-HFX2-L17 HTTP Seat Binding And Served Package Boundary

Terminal open responses expose current `seatRole`. `POST /api/terminal/{session}/attach-leaf`
accepts `{leafKey, role}`, returns `role-required` for an untyped hand-opened harness, and reports
current/previous binding roles; `409` is restricted to a live same-pair owner. Retire endpoints
construct authority refs from binding leaf/role, including replacement-leaf identity. The dashboard
asset refresh remains a source-to-build-to-package operation performed by `scripts/sync-dashboard.py`;
this app only serves the synchronized package tree, so generated hashed assets receive no sidecars.

### 260707-HFX2-L15 Harness-Log Paste Endpoint

Submitted `POST /api/terminal/{session}/paste` input receives a fresh delivery id and routes through
the same `injector.deliver` path as spawn and durable inbox traffic. The endpoint builds
`HarnessSessionLog` from the catalog row, reuses any existing bound log, persists a newly bound
entry id/path with `TerminalCatalog.bind_session_log`, and reports `submitted:true` only when the
id-bearing user record exists. Pane capture is returned only for an unconfirmed failure. Drafts
remain transport-only and intentionally unacked.

Reviewer residual N3: a submitted request for a harness-less `kind=terminal` row has no candidate
harness log, so it exhausts the bounded ladder and remains unconfirmed; submitted REST text also
gains the visible delivery-id envelope required for verification. The owner still owes an explicit
short-circuit/documentation disposition; this sidecar does not present that residual as fixed.

### 260707-HFX2-L13 Live Compaction And Task-Body Endpoint

Dashboard lifespan still compacts the workspace river before accepting clients, then starts a
separate sixty-second live compaction task beside projector, metrics, and supervisor tasks. Shutdown
cancels and awaits that task with the same cancellation discipline as the other loops. Failures are
logged and retried on the next cadence rather than terminating the serving daemon.

`GET /api/task-document?path=...` requires a ready projection, delegates path confinement and schema
validation to `read_task_document_body`, returns the full `TaskDocNode`, and maps missing/invalid
documents to 404 (projection-not-ready to 503). This is the only dashboard route that carries task
reader bodies; `/api/state` and `/api/stream` remain summary-only.

### 260707-HFX2-L12 CS-6 Update

The serving lifespan now runs the startup-only workspace-river compactor before starting projector/supervisor/metrics loops, the metrics loop compacts provider metrics after degradation evaluation, and the supervisor context wires `escalation_budget` from agentic settings.

L16 review follow-up (L16R-1): the terminal-open route loads the effective harness registry ONLY when the request resolves a harness (kind=harness or an explicit harness id) — a malformed agentic settings file fails the launches that use it, never a plain scratch terminal.

`create_app(config, *, interval=1.0, heartbeat=None, now=None, before_tick=None,
refresh_provider_state=None, refresh_landing_state=None, watch_changes=None,
terminal_host=None, terminal_catalog=None, terminal_paster=None)`
constructs a `Projector` (threading `now`/`before_tick` straight through — the **sim seams**;
both default to live behaviour). **260712-PTS-L3:** `interval` is the fast-path projection cadence
floor and `heartbeat` bounds quiet-world `/api/state` staleness (default
`DEFAULT_HEARTBEAT_SECONDS`, 15s); `watch_changes` defaults to `before_tick is None` — exactly like
the provider/landing refreshers — so LIVE serving gets a `ProjectionInputWatcher(config)` injected
as the projector's `change_watcher` (change-driven + heartbeat waking) while `--sim` replay stays
time-driven (the sim feeder only writes *inside* a tick, so a change-gated loop would never wake).
It also builds a `TerminalHost` (`terminal_host` defaults to a fresh one;
tests inject a fake), a `TerminalCatalog` at `coordination_root/logs/dashboard/terminal-sessions.json`
(`terminal_catalog` is test-injectable), and (L2) a `TerminalPaster` (`terminal_paster` defaults to a
fresh one; tests inject a fake for the paste endpoint). Since **260707-HFX-L5** it also builds the
catalog-liveness wiring: `liveness_clock = now or utc_now` (ONE timestamp base per app instance —
sim/replay wires its replay clock through liveness too, the L5R2 fix), one
`TerminalCatalogLivenessConfig` (the code-default hysteresis knobs), and one
`TerminalCatalogLivenessSweeper(catalog, host, now=now, config=…,
on_turn_state_change=lambda observation: log_turn_state_change_event(config, observation.entry))`
shared by the sessions endpoint — the **260707-HFX-L8** callback is what turns a sweep-detected live
turn-state transition into an `ar-observer-event/v1` record without adding a second code path;
attach + paste run direct per-row `observe_terminal_liveness` calls with `checked_at=liveness_clock()`.
It wires a FastAPI `lifespan` that `prime()`s the projector
(one initial projection), runs its tick loop as a task beside the provider metrics sampling task,
and on shutdown cancels both tasks (awaiting each under `CancelledError` suppression) and calls
`host.shutdown()`. Endpoints:

When `refresh_provider_state` is left as `None`, live mode (`before_tick is None`)
constructs a `ProviderStateRefresher`, while sim mode disables provider refresh so replayed
fixtures stay deterministic. Tests can still force either branch explicitly.

The provider metrics loop (containment R4, 260707-HFX-L1) makes the serving daemon the
central containment sampler: `create_app` builds a
`ProviderMetricsStore(config.coordination_root)` and the lifespan runs `metrics_loop()` as a
task beside the projector — each pass calls `sample_provider_containers` and
`ProviderMetricsStore.record` via `asyncio.to_thread`, then sleeps
`DEFAULT_SAMPLE_INTERVAL_SECONDS` (30s, deliberately decoupled from the projection tick —
formerly a fixed 1s, change-driven + heartbeat since 260712-PTS-L3).
The loop is exception-tolerant: any failure is logged through the module `logger`
(`logger.exception`) and the loop retries next interval, so one failed docker probe never
kills sampling. The store feeds `provider_status`, the degradation protocol (260707-HFX-L7),
and the statistics board later; sampling is read-only and dockerless-safe.

**260707-HFX-L7 (provider degradation protocol):** immediately after
`metrics_store.record(snapshot)` in the same sampling-loop iteration, the loop calls
`await asyncio.to_thread(evaluate_provider_degradation, config)` — one call per tick, no extra
task, sharing the same exception-tolerant `try/except` as the metrics record call above, so a
degradation-evaluation failure never kills sampling either. This is the ONLY caller of the
detector's entry point; the detector itself owns state persistence, inbox alerting, and the
critical-threshold failsafe stop (`providers/degradation.py`) — `app.py` only wires the call into
the loop it already owns.

**260707-HFX2-L2 (R1, supervisor sweep host):** `create_app` builds a third decoupled-cadence
lifespan task, `supervisor_loop()`, following the exact `metrics_loop()` template — its own
`settings.supervisor.interval_seconds` sleep (default 10s, re-read from `load_agentic_settings`
every iteration so a settings edit takes effect without a restart), an `enabled` early-continue when
the family is switched off, and the same `try/except Exception: logger.exception(...)` resilience
posture so a sweep failure never crashes the daemon and simply retries next interval. Each iteration
builds a fresh `SupervisorContext` (`_supervisor_context()`) wiring the catalog/host/paster the app
already owns plus fresh `OperatorInboxStore`/`ExpectationRowStore`/`OrchestrationNudgeStore`/
`SupervisorSignalCooldownStore`/`EventStore` instances and the shared `SupervisorHeartbeatStore`, then runs
`run_supervisor_sweep(ctx, now=(now or utc_now)())` via `asyncio.to_thread` (the sweep's store I/O is
synchronous, so it never blocks the event loop). `stale_seat_seconds` is derived as
`max(settings.supervisor.interval_seconds * 4, 60.0)` — four sweep intervals of grace before a
turn-state-stale row fires the seat-liveness predicate (R2e), floored at 60s so a very fast sweep
interval cannot make the liveness predicate trigger-happy. **260707-HFX2-L4:** the same
`_supervisor_context()` call now also resolves `settings.escalation.sla_seconds`/`rung_seconds`/
`respawn_after_rung` straight onto `SupervisorContext`'s plain-primitive escalation knobs — no new
settings read of its own, the same per-sweep `load_agentic_settings` call this function already
made for the supervisor family. **260707-HFX2-L8 (R4/R6):** that same context wiring also threads
`settings.supervisor.redeliver_budget`, the conservative per-sweep inbox-redelivery budget that keeps
large redeliverable backlogs spread across sweeps while preserving the supervisor heartbeat cadence.
**260707-HFX2-L9:** `_supervisor_context()` now also wires
`settings.supervisor.signal_cooldown_seconds` and the new persisted
`SupervisorSignalCooldownStore`, while continuing to pass the configured redelivery floor through
`redeliver_rate_limit_seconds`.
The lifespan cancels
`supervisor_task` (added to the existing metrics/projector cancel set, same
`contextlib.suppress(asyncio.CancelledError)` await pattern) on shutdown.

**260707-HFX2-L2 (R5, self-liveness surfacing):** a module-level `SupervisorHeartbeatStore` is
constructed once in `create_app` (shared by the loop and the read side below).
`_supervisor_heartbeat_payload()` reads the current tick via `heartbeat_age_seconds` at RESPONSE
time (using `liveness_clock()`, the same `now or utc_now` base every other liveness call in this
file shares) and returns `{lastTickAt, ageSeconds, staleCutoffSeconds, stale}` plus, since
**260707-HFX2-L8 (R6)**, `{pendingInboxCount, redeliverableInboxCount, lastSweepDurationSeconds}` —
the forward signal that shows inbox storm pressure before a stale banner trips. `stale` is `True`
when there is no tick yet OR the age has passed `settings.supervisor.stale_cutoff_seconds`. This
payload is attached as `supervisorHeartbeat` on both `GET /api/state`'s JSON body and the SSE
snapshot (`stream_events` gained a `supervisor_heartbeat` keyword, attached the same way
`servingBuild` already is). It is deliberately computed at response/connect time rather than folded
into the change-gated projection: like `servingBuild`, it never affects `/api/state`'s ETag
revision (delta.py's "volatile ages excluded" posture) — a live tick age must never make an
otherwise-unchanged projection look changed.

- `GET /api/state` returns the current projection once as `model_dump(by_alias=True,
  exclude_none=True)` plus the boot-time `servingBuild` stamp (503 until the first projection
  exists) — curl-friendly, no streaming. **Change-gated (260703-L15):** the response carries a
  weak `ETag: W/"<projector.revision(seq)>"` + `Cache-Control: no-cache`, and an `If-None-Match`
  that weak-matches (via the module-level `_if_none_match_matches` — `*`, comma lists, `W/`
  prefixes) returns `304` with the same headers and an empty body, skipping the whole dump. The
  revision only advances on stable-content change (delta.py's volatile-age-free diff), so a
  poller of an unchanged projection pays a header exchange instead of a ~780 KB parse.
- `GET /api/stream` (`response_class=EventSourceResponse`) delegates to the module-level
  `stream_events(projector, build=build, supervisor_heartbeat=...)`. That helper consumes one atomic
  projector subscription; it does not read current state separately. Initial and failed-prime
  recovery snapshots receive the same boot/heartbeat decoration before reaching the browser.
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
  `recipientRole` / `gateId` aliases plus `ask`, `response`, sender/message metadata, optional
  `artifactPath`, and `deliverToHosted`) and calls `operator_inbox_post_payload` with
  `created_by="developer"` and `created_via="dashboard"`. This is the trusted dashboard write side
  for task-10/L3 durable inbox messages; when a hosted session matches, it passes the catalog/host/paster
  seams so the same row can be pushed over echo-confirmed stdin immediately. Missing lifecycle/agent/role
  addressing returns `400 {"status":"bad-address"}` from the builder's address validation.
- `POST /api/operator-inbox/{entry_id}/dismiss` physically deletes a pending operator-inbox entry.
  This is the trusted dashboard path used by the dismissible `check chat` task-row warning; it clears
  developer-side noise without marking the entry as agent-consumed.
- `@app.websocket("/api/terminal/{session}")` (slice 6d-2) bridges the Mode B2 terminal host to
  the browser: it `accept()`s, looks up the catalog row, runs a direct liveness observation
  (`_attach_terminal_session` takes `checked_at` + `liveness_config` and calls
  `observe_terminal_liveness` — HFX-L5: a transient tmux command failure records hysteresis
  evidence instead of immediately exit-marking the row; a dead probe still refuses), and calls
  `host.attach(..., name=entry.tmux_name)` so this WebSocket gets its own tmux client PTY attached to
  the same durable tmux session. Since **260707-HFX2-L11**, a row with `status:"landed"` is also
  attachable for read-only archive inspection; the background liveness sweeper deliberately skips
  these rows, but attach still performs an on-demand tmux check before connecting. If the row is
  unknown, not `running`/`landed`, or the observation says
  not-alive/not-running, it `close(code=4404)` (exit marks now come only from the evidence-backed
  liveness path, revivable by the sweeper's self-heal). PTY output is queued via
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
- `GET /api/terminal/sessions` returns catalog rows via `liveness_sweeper.refresh()` (HFX-L5): a
  full probe sweep runs at most every 10s (default) and never overlaps — a rate-limited or
  concurrent call serves the persisted catalog without probing, so the dashboard's 1s polling
  cadence no longer implies 1s tmux probing. Landed rows are returned without background probing or
  turn-state classification, preserving the inspectable archive as a cold list. A running row exit-marks only after the hysteresis
  evidence threshold (3 command failures across ≥5s, or one definitive pane-gone probe); a falsely
  exited row self-heals to `running` on the next alive probe; explicitly terminated rows are
  filtered by the catalog.
- `POST /api/terminal/{session}` (slice 6e-2a/6e-2b, extended by ACPUI L4) is the **opener**: the dashboard ensures a
  detached durable tmux session, then the WebSocket attaches with a per-tab client. `TerminalOpenRequest`
  carries a `kind` (+ optional `harness`), optional complete `model`/`effort`, a display `label`,
  `lifecycleId`, and (L5) `leafKey`. A partial pair or a pair on a plain/non-native session returns
  `400 launch-selection-invalid` before spawn. **Since
  L2 the whole leaf-claim + tmux-ensure + catalog-upsert composition moved into
  `serving.terminal_opener.open_terminal_session`** (`resolve_terminal_launch`, `_terminal_label`, and the
  role-scoped conflict check all left `app.py` for that module) — the route first normalizes any supplied
  `leafKey` through `leaf_ref_validation.resolve_catalog_leaf_key`, returning `400` with
  `leaf-ref-not-found` / `leaf-ref-ambiguous` detail before any tmux/catalog mutation when it cannot
  resolve. It then calls the opener with the request fields + the resolved `shell` and maps the
  `OpenTerminalResult`: `bad-kind` ⇒ `400`,
  `leaf-taken` ⇒ `409 {"status":"leaf-taken","leafKey","session":<owner>}` (server-arbitrated,
  role-scoped, self-reclaim allowed — a `kind="terminal"` open never 409s against the leaf's agent chat),
  `launch-conflict` ⇒ `409 launch-selection-conflict` with the actual durable kind/harness/pair/
  endpoint, and `opened` ⇒ `200` returning the persisted `leafKey`/`cwd`/`tmuxName` and actual
  native selection/control provenance. This is the same opener the
  agent-facing `spawn_agent_session` MCP tool composes, so there is **no parallel spawn path**. Command
  resolution stays server-side (`kind="terminal"` ⇒ `[$SHELL]`, `kind="harness"` ⇒ the registry argv,
  rejecting absent/unknown/uninstalled ids; only ids on the wire), the leaf binding is preserved across a
  re-open when none is sent, there is no starter PTY client to close, and a bare-pane harness is opened
  suspend-unsafe (slice 6f).
- The native capability/control routes are registered by `harness_control_api`: pre-session
  `GET /api/harnesses/{harness}/capabilities` (optional `refresh=true`), live
  `GET /api/terminal/{session}/capabilities`, `POST .../set-model`, `POST .../set-effort`,
  `POST .../submit`, and `POST .../reconcile`. Live routes observe running-state/liveness before
  endpoint support, so unknown/stopped/dead rows are `404`, live plain/legacy rows are `409`, and a
  live native endpoint proceeds. Set responses retain honest adapter acceptance at `200`; endpoint
  or discovery failure is `503`. Submit and reconcile use raw-free public serializers.
- `POST /api/terminal/{session}/paste` (**L2**) delivers a context packet to a hosted session
  server-side — the mirror of the frontend WebSocket `pasteAndConfirm`/`submitAndConfirm` for a durable
  tmux session that has no attached browser client. `TerminalPasteRequest` carries `text` + `submit`
  (default false). It `404 {"status":"unknown-session"}`s when the row is unknown/non-running, and
  otherwise runs a direct `observe_terminal_liveness` check (HFX-L5: `checked_at=liveness_clock()`;
  a transient tmux command failure records hysteresis evidence — no immediate exit mark — but a
  not-alive observation still 404s); on an alive running row it runs `paster.paste(entry.tmux_name,
  text, submit=submit)` — the same capture-verified paster mechanic as the spawn tool, no separate
  path — and returns `{session, status:"delivered"|"unconfirmed", delivered, submitted}`; since
  260707-HFX-L3 an unconfirmed outcome additionally ships `capture` (the paster's final pane
  snapshot) as loud-failure evidence, omitted when delivered.
- `POST /api/terminal/{session}/attach-leaf` claims or **moves** a leaf for an **existing** session from
  the Chats page — enclosure-free, no respawn. `TerminalAttachLeafRequest` carries the required `leafKey`;
  the route normalizes it to the canonical qualified task-doc id before delegating to
  `assign_terminal_session_to_leaf(catalog, session_id, leaf_key)`, so browser actions and the
  agent-facing MCP tool share one server-authoritative catalog policy. Invalid or ambiguous leaf refs
  return `400` before mutating the row. The result maps to
  `404 {"status":"unknown-session"}` for an unknown/non-running session, `409 {"status":"leaf-taken",...}`
  when a different running session of the same role owns the target leaf, and
  `200 {"session","status":"attached","leafKey"}` after persisting `entry.with_leaf_key(leaf_key)`.
  A conflict does not mutate the catalog.
- `POST /api/terminal/{session}/terminate` is the destructive terminal action. It accepts either a live
  host session or a catalog row, kills the tmux session through `TerminalHost.terminate`, marks the
  catalog row `terminated`, and returns `404 unknown-session` only when neither exists.
- `POST /api/terminal/{session}/retire` (**260707-HFX-L8**, issue #12) is the server-authoritative
  seat retirement surface: a `TerminalRetireRequest` (`actorSession` alias, `reason` default
  "manual retire"). 404 `unknown-session`/`unknown-actor` when either row is missing; if the target
  is already `terminated` it short-circuits to `200 already-retired` with its existing provenance
  BEFORE any authority check (idempotent, read-only fast path); otherwise `check_retire_authority`
  runs against `SeatRef`s built from each entry's `spawn_role`/`leaf_key` (via `master_of`) — a
  `RetirePolicyError` returns `403 retire-refused` with `detail` naming the exact clause; on success
  `retire_entry` kills the tmux session + persists the terminal mark, `log_retire_event` fires, and
  the route returns `200 retired` + the four retirement provenance fields. Same underlying
  `retire_entry`/`check_retire_authority` mechanics as the `session_retire` MCP tool
  (`mcp/tools/terminal.py`) so the dashboard-button path and the agent-tool path retire identically.
- `POST /api/terminal/landed-cleanup` (**260707-HFX2-L11**) closes the dashboard's collapsed landed
  archive group. `TerminalLandedCleanupRequest` carries `sessions`; the route re-reads each catalog
  row and only calls `retire_entry(..., reason="landed group cleanup", edge="landed-group-cleanup")`
  when the current row is still `status:"landed"`. Rows that vanished or changed status are returned
  in `skipped`; successfully closed rows are logged through `log_retire_event`. This is explicit
  cleanup, not completion-edge automation.
- `POST /api/terminal/{session}/rename` (**260707-HFX-L8**, issue #4) is the post-spawn identity
  surface: a `TerminalRenameRequest` (`label`). `404 unknown-session` when the row is missing or
  already `terminated`; else `catalog.set_label` + `log_rename_event`, returns `200 renamed` +
  `label`/`spawnedLabel`. Identity text only — never touches `spawn_role` (L6 immutability).
- `GET /api/harnesses` (slice 6e-2b; effective registry 260703-L16) returns
  `{"harnesses":[{id,name,detected}]}` from `serving.harnesses.detect_harnesses(registry=...)`
  (`shutil.which` per harness) over the EFFECTIVE registry — the builtin table merged with
  `orchestration.harnesses` in the GLOBAL agentic settings, loaded per request — so settings-defined
  harnesses get launch buttons too; the dashboard renders a button per *detected* harness. The
  `POST /api/terminal/{session}` opener passes the same effective global registry into
  `open_terminal_session`, keeping dashboard launches and MCP dispatches on one argv truth
  (repo-local harness overrides remain leaf-scoped dispatch material via the MCP tool). A malformed
  settings file raises the loader's fail-loud error (never a silent fallback).
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
- `register_notes_routes(app, config)` (agent-orchestration L9) registers the read-only
  `GET /api/notes/{list,read}` coordination-notes routes after the change-set routes and still
  **before** `mount_static`. The handlers live in `serving/notes.py`.

`stream_events(projector, *, build=None, supervisor_heartbeat=None)` owns one atomic projector
subscription. It serializes the initial current snapshot when available; if `prime()` left no
projection, the same connected iterator waits and serializes the projector's first successful full
recovery snapshot. Every snapshot is decorated identically with the optional boot-time
`servingBuild` and connect-time `supervisorHeartbeat`; ordinary later events remain per-entity
deltas. `_encode` dumps projection nodes by alias (camelCase, `exclude_none`) and passes removal
markers (`{key: id}`) through as-is. `contextlib.aclosing()` explicitly closes the inner generator
when the consumer disconnects or is cancelled. SSE uses built-in `fastapi.sse`
(`EventSourceResponse`/`ServerSentEvent`, auto keep-alive).

### 260712-TRH-L7 refresher lifecycle wiring

Live app creation enables the landing refresher; simulation supplies a feeder and disables remote observation. Lifespan shutdown tolerates a failed refresher task and still reaches `TerminalHost.shutdown`.

### Invariants And Boundaries

### Native control contract boundary

The serving app now registers the L4 harness-neutral production routes, while protocol bridge,
private IPC, pre-session cache, and normalized terminal surface remain explicit modules. Control
state and receipts belong to the bridge/adapter contract; tmux pane and terminal-log text are
diagnostics only. Vendor-specific behavior remains behind AR's native adapter port rather than in
this app.

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
- **The state channel has one subscription owner:** `Projector.subscribe()` owns registration plus
  current-snapshot capture; `app.py` only decorates and serializes its events. A state mutation
  therefore cannot fall between an app snapshot read and subscriber registration. A failed-prime
  recovery snapshot is wire-equivalent to an initial snapshot, and explicit iterator closure
  releases the projector queue on disconnect/cancellation.
- **The `/api/state` ETag is a content fingerprint, not a byte fingerprint (260703-L15):** two
  200 bodies under one revision can differ in `generatedAt` and volatile ages (recomputed at
  request time) — that is exactly the change-gating semantics, hence the WEAK ETag form. The
  `servingBuild` stamp is app-layer only (never on `WorkspaceProjection`/`latest-state.json`).
- **Terminal bridge (6d-2):** binary-out / JSON-text-in over one WebSocket; the wire carries only
  `stdin`/`resize` control shapes, never a command (the host spawns a fixed argv). Attach-only,
  localhost-bound like the rest; the bridge helpers (`_bridge_terminal` / `_terminal_to_socket` /
  `_socket_to_terminal` / `_apply_terminal_input` / `_apply_terminal_session_input`) are module-level for
  unit testability. WebSocket attach always probes tmux before calling `host.attach`, so a stale catalog
  row never recreates a fresh session by accident. Browser disconnect detaches only that connection's
  PTY client but does not mark the row exited; the fd reader is removed at most once during cleanup; tmux
  remains the persistence boundary and can serve multiple browser tabs at once.
- **Terminal catalog boundary:** `terminal_catalog.py` owns JSON persistence and filtering semantics;
  this module owns HTTP/WebSocket orchestration. Status refresh is delegated to
  `terminal_liveness.py` (HFX-L5): one sweeper instance behind the sessions endpoint, direct
  observations on attach/paste, one injected clock — the deleted `_refresh_catalog_entries`
  immediate-exit-mark path no longer exists, so a tmux command-failure storm cannot mass-exit the
  fleet and a false exit self-heals within one sweep interval. The WebSocket-close `mark_exited`
  (dead PTY — process evidence, not a probe) remains and is itself sweep-revivable while tmux still
  holds the session.
- **Leaf registry (L5):** the catalog is the leaf→chat registry and the server is the uniqueness
  arbiter — at most one *running* session per **(leaf, role)**. Since **L2** the opener's claim lives in
  `terminal_opener.open_terminal_session` (via the shared `leaf_conflict_owner`, `role=role_for_kind(kind)`)
  rather than the removed local `_claim_leaf_or_409`; `attach-leaf` still delegates to
  `assign_terminal_session_to_leaf` (`role=entry.role`). Landed rows are non-active and cannot claim
  a new leaf; cleanup is separate from leaf ownership. A **chat** (any harness) and a **terminal** (a
  shell) are separate slots, so a leaf can hold one running chat AND one running terminal, and a terminal
  never conflicts with the leaf's chat. `leaf_key` is opaque here (a qualified leaf id or a reserved
  `master:<…>` key flow identically); the binding is enclosure-independent and survives finalize, and a
  dead/exited session frees its slot because `active_for_leaf` gates on `status == "running"`.
- **Sim is a seam, not a fork:** `now`/`before_tick` default to live; `cli.dashboard` passes a
  replay clock + fixture feeder under `--sim` and the path is otherwise byte-identical.
- **Metrics sampling is observation, not control (containment R4):** the loop is read-only and
  dockerless-safe, runs on its own 30s cadence (never the projection tick), and must survive
  sampling failures — a failed pass logs and retries next interval; shutdown cancels it cleanly.
- **The projection watcher is a live-only seam with a loud fallback (260712-PTS-L3):**
  `watch_changes` follows the refresher pattern (`before_tick is None`), the watcher task's
  lifecycle is owned by `Projector.run` (not the lifespan), and any watcher absence/failure
  degrades LOUDLY to the legacy fixed-`interval` ticking. The `heartbeat` (default 15s) is the
  `/api/state` staleness bound and the resolution of time-derived fields for a quiet world.
- **The supervisor sweep is stores-not-projections, code-not-model (260707-HFX2-L2 R1/R3):**
  `supervisor_loop` and `_supervisor_context` wire the app's OWN store instances directly into
  `SupervisorContext` — `app.py` never reaches into `serving/projector.py` or
  `observer/reducer.py` for the sweep's predicates. Own decoupled cadence (settings-controlled,
  default 10s), never the projection tick; exception-tolerant like the metrics loop; zero model
  calls anywhere in the loop.
- **The supervisor heartbeat is a volatile age, same posture as `servingBuild` (R5):** computed at
  response/connect time via `liveness_clock()`, never folded into the `/api/state` ETag revision —
  an idle dashboard tab whose OTHER content never changes will not see `ageSeconds` advance until a
  real reconnect or an unrelated content change forces a fresh `200` (the same accepted limitation
  `servingBuild` already has).
- `McpRuntimeConfig`/`datetime` are imported under `TYPE_CHECKING` (config is only passed on).

### Conventions

`create_app` composes route modules and shared stores; vendor protocol logic stays out of this file.
Request/response routes carry immediate command evidence, while existing streams carry asynchronous
output. Settings are read as authority where already established and are never mutated here.

### Todos

Frontend and settings-authoring consumers belong to the separate FEUI and CFGUI masters.

## Docs References

No Domain Documentation source is configured for this repository, so no live domain-documentation
pass was available for this update.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No configured domain documentation could be checked. | — | — |

## Repo-Internal References

| Finding | Citations | Source Path |
| --- | --- | --- |
| The shared projector owns atomic registration/snapshot capture, publish-before-notify ordering, first-recovery snapshots, and the ETag revision. | L135-L178; L207-L269 | [projector.py](agents-remember/mcp/src/agents_remember/serving/projector.py) |
| Deterministic serving regressions force the former handoff mutation, failed-prime recovery, identical-state suppression, later delta, and cancellation cleanup. | L395-L457 | [test_serving.py](agents-remember/mcp/tests/test_serving.py) |
| The live change watcher `create_app` injects when `watch_changes` resolves true (260712-PTS-L3). | `ProjectionInputWatcher` | [change_watcher.py](agents-remember/mcp/src/agents_remember/serving/change_watcher.py) |
| The boot-time serving build stamp injected on `/api/state` + the SSE snapshot. | [build_info.py](agents-remember/mcp/src/agents_remember/serving/build_info.py) |
| The raw `event` channel `/api/events` delegates to. | [events.py](agents-remember/mcp/src/agents_remember/serving/events.py) |
| The pure action evaluation `/api/actions/{action}` delegates to. | [actions.py](agents-remember/mcp/src/agents_remember/serving/actions.py) |
| The gate write-path the router calls for a gate-decision verb (slice 6b). | [mcp/tools/gates.py](agents-remember/mcp/src/agents_remember/mcp/tools/gates.py) |
| The operator inbox payload builder used by `/api/operator-inbox`. | [mcp/tools/operator_inbox.py](agents-remember/mcp/src/agents_remember/mcp/tools/operator_inbox.py) |
| The Mode B2 terminal host the `/api/terminal` WebSocket bridges to (slice 6d), including tmux probe/kill hooks used for durability. | L86-L121; L230-L239; L287-L289; L340-L347 | [terminal.py](terminal.py) |
| The durable terminal-session catalog persisted by the opener, sessions endpoint, landed cleanup, and terminate route. | L15-L30; L110-L185 | [terminal_catalog.py](terminal_catalog.py) |
| The catalog liveness sweeper + shared observation path behind the sessions endpoint, attach, and paste (HFX-L5). | `TerminalCatalogLivenessSweeper`; `observe_terminal_liveness` | [terminal_liveness.py](terminal_liveness.py) |
| The shared leaf reassignment helper used by this route and the agent-facing MCP tool. | L45-L83 | [terminal_leaf_assignment.py](terminal_leaf_assignment.py) |
| The shared hosted-session opener (L2) both this route and the `spawn_agent_session` tool compose. | L84-L174 | [terminal_opener.py](terminal_opener.py) |
| The L4 route module owns harness-neutral advertise, launch selection, exact-session set, submit, reconcile, and liveness-first status mapping. | L64-L249 | [harness_control_api.py](agents-remember/mcp/src/agents_remember/serving/harness_control_api.py) |
| The pre-session catalog owns bounded dynamic discovery and failed-refresh quarantine. | L80-L195 | [harness_capability_catalog.py](agents-remember/mcp/src/agents_remember/serving/harness_capability_catalog.py) |
| The shared opener owns live launch-truth checks and the fenced read/probe/ensure/upsert transaction. | L170-L648 | [terminal_opener.py](agents-remember/mcp/src/agents_remember/serving/terminal_opener.py) |
| The serving leaf-ref adapter normalizes terminal open/attach leaf keys before catalog writes. | resolve_catalog_leaf_key | [leaf_ref_validation.py](leaf_ref_validation.py.md) |
| The server-side capture-verified paste helper the L2 `/paste` endpoint drives (260707-HFX-L3: unconfirmed ships the pane capture). | L133-L229 | [terminal_paste.py](terminal_paste.py) |
| The harness launch registry the opener + `/api/harnesses` consume (slice 6e-2b). | [harnesses.py](agents-remember/mcp/src/agents_remember/serving/harnesses.py) |
| The static-bundle resolver/mount. | [static.py](agents-remember/mcp/src/agents_remember/serving/static.py) |
| The read-only files API registered just before the static mount (operations-integration L1). | [files.py](agents-remember/mcp/src/agents_remember/serving/files.py) |
| The read-only change-set API registered right after the files routes (operations-integration L3). | [changeset.py](agents-remember/mcp/src/agents_remember/serving/changeset.py) |
| The served projection shape + `ActionAvailability`. | [observer/projection.py](agents-remember/mcp/src/agents_remember/observer/projection.py) |
| The CLI adapter that builds and serves this app (and wires sim). | [cli/dashboard.py](agents-remember/mcp/src/agents_remember/cli/dashboard.py) |
| The central containment metrics store + sampler the lifespan loop drives (containment R4). | [providers/metrics.py](agents-remember/mcp/src/agents_remember/providers/metrics.py) |
| The provider degradation detector this loop calls once per tick after recording a metrics sample (260707-HFX-L7). | evaluate_provider_degradation | [providers/degradation.py](agents-remember/mcp/src/agents_remember/providers/degradation.py) |
| The landed archive helper records completion-edge seats without terminating them. | `land_seats_for_leaf` | [landing.py](landing.py) |
| The retire/rename mechanics + authority policy the explicit retire and landed-cleanup endpoints call into. | `retire_entry`; `check_retire_authority`/`SeatRef`/`master_of` | [retire.py](retire.py); [retire_policy.py](retire_policy.py) |
| The observer-event loggers the landed, retire, rename, and turn-state paths fire. | `log_landed_event`; `log_retire_event`; `log_rename_event`; `log_turn_state_change_event` | [seat_events.py](seat_events.py) |
| The deterministic supervisor sweep + predicate library `supervisor_loop`/`_supervisor_context` drive every interval (260707-HFX2-L2 R1-R4). | `SupervisorContext`; `run_supervisor_sweep` | [supervisor.py](supervisor.py.md) |
| The pane-state classifier one of the sweep's predicates (`evaluate_pane_findings`, inside `supervisor.py`) calls. | `classify_pane_signal` | [pane_signals.py](pane_signals.py.md) |
| The self-liveness heartbeat store both the loop (tick) and the read side (`_supervisor_heartbeat_payload`) share, including L8 inbox backlog and sweep-duration fields. | `SupervisorHeartbeatStore`; `heartbeat_age_seconds` | [supervisor_heartbeat.py](supervisor_heartbeat.py.md) |
| The agentic-settings loader `supervisor_loop`/`_supervisor_context`/`_supervisor_heartbeat_payload` all re-read per-use for the `orchestration.supervisor` family. | `load_agentic_settings` | [../kernel/agentic_settings.py](../kernel/agentic_settings.py.md) |
| The stores the sweep's predicates read directly (R3: never the projection). | `ExpectationRowStore`; `OperatorInboxStore`; `OrchestrationNudgeStore`; `SupervisorSignalCooldownStore`; `EventStore` | [../controlplane/expectation_rows.py](../controlplane/expectation_rows.py); [../controlplane/operator_inbox_store.py](../controlplane/operator_inbox_store.py); [../controlplane/orchestration_nudges.py](../controlplane/orchestration_nudges.py); [../controlplane/supervisor_signals.py](../controlplane/supervisor_signals.py.md); [../observer/store.py](../observer/store.py) |

## Cross-Repo References

No external repository boundary, Toad host, or ACP transport is implemented by the serving app.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No meaningful cross-repo references found. | — | — |

### 260713-PHA-L5 Hosted Projection And Interaction Routes

Serving routes expose additive adapter catalog state, route hosted delivery through the durable
inbox-backed bridge, and surface adapter interactions without making pane or log timing authoritative.

## 260718-CHATS-L5I Current Delta

The app reuses one serialized projection body per published projection for `/api/state` and snapshot SSE payloads, then injects heartbeat and build details per response. JSON responses are gzip-compressed at level 6 while `text/event-stream` remains uncompressed and streaming; the lifespan also owns the explicitly enabled heap-diagnostic and allocator-trim tasks.

This entry supersedes any earlier description in this sidecar that conflicts with the current source behavior above; verification metadata stays pinned to the pre-commit source history until closeout.

## Update History

- 2026-07-24T13:18:47Z — 260718-CHATS-L5I curator: corrected the source-side behavior record for the current backend/shared delta and preserved the pre-commit verification stamp.

- 2026-07-19T00:06+02:00 — 260718-CHATS-L0 curator: documented the one-line composition edit —
  `register_harness_control_routes` now receives `coordination_root=config.coordination_root` so
  the harness-control seam constructs the immutable conversation runtime scope; the registration
  remains the app's only conversation seam. Verification metadata remains pinned until closeout
  stamps the candidate commit.
- 2026-07-18T14:16+02:00 — 260715-FEUI-MX-FIX-1: documented the removal of the app-owned
  snapshot/subscription seam, identical initial/recovery snapshot decoration, preserved SSE wire
  contract, and explicit iterator closure on disconnect/cancellation. Verification metadata remains
  pinned until closeout stamps the candidate commit.
- 2026-07-18T12:43+02:00 — FEUI-L9R: documented removal of fictitious pre-session adapter state
  from the harness discovery endpoint; verification metadata remains pinned pending closeout.
- 2026-07-16T06:15+02:00 — 260714-ACPUI-L4 curator: documented the daemon's dynamic advertise,
  complete-pair launch, exact-session set, reliable submit/reconcile, raw-free public evidence,
  live-reopen conflict response, and preserved streams, role spawn, and durable bus boundaries.
- 2026-07-14T13:59+02:00 — 260713-PHA-L5: refreshed dashboard/API projection and bridge-backed route composition.
- 2026-07-14T12:00+02:00 — 260713-PHA-L1 curator refresh: documented additive harness control
  metadata and the deliberate no-production-wiring boundary for the new bridge seams.
- 2026-07-12T20:24+02:00 — 260712-PTS-L3: `create_app` gained `heartbeat=` (quiet-world staleness
  bound, default 15s) and `watch_changes=` (defaults to `before_tick is None`, the refresher
  pattern) — live serving injects a `ProjectionInputWatcher` as the projector's `change_watcher`
  for change-driven + heartbeat pacing; `--sim` replay stays time-driven. Endpoints, lifespan
  structure, and ETag semantics unchanged. Verification metadata pinned until closeout stamps the
  PTS-L3 commit.
- 2026-07-12T17:30+02:00 — 260712-TRH-L7: live app lifecycles enable the landing refresher while simulation remains observation-disabled; shutdown retains host cleanup if the refresher has already failed.

- 2026-07-10T15:07+02:00 — 260707-HFX2-L17: carried role through HTTP open/attach responses,
  added explicit hand-opened role claims and pair-scoped conflicts, and keyed retire authority on
  binding identity. Reconfirmed that packaged hashed assets are served output, not onboarding
  subjects. Verification metadata remains pinned until closeout stamps L17.

- 2026-07-10T13:03+02:00 — 260707-HFX2-L15: routed the REST terminal paste endpoint through the
  shared log-verified injector, added per-request delivery ids and safe catalog log binding, and
  removed pane movement/rendering as submitted authority. Verification metadata remains pinned
  until closeout stamps the eventual L15 code commit.

- 2026-07-10T01:14+02:00 — 260707-HFX2-L13 F3/F6: added the live workspace-river compaction loop
  and the projection-gated, path-confined on-demand task-document endpoint. Verification metadata
  remains pinned until closeout stamps the eventual L13 code commit.

- 2026-07-09T19:31+02:00 — 260707-HFX2-L12: documented the CS-6 scaling/reclamation change for this file. Verification metadata pinned until closeout stamps the HFX2-L12 commit.
- 2026-07-09T14:05+02:00 — 260707-HFX2-L11 curator correction: documented the landed archive
  surfaces in `app.py`: WebSocket attach now admits `running` and `landed` rows for inspection,
  `GET /api/terminal/sessions` returns sweep-cold landed rows, `attach-leaf` refuses non-running
  rows, and `POST /api/terminal/landed-cleanup` explicitly retires only rows still marked landed
  after a catalog re-read. Verification metadata pinned until closeout stamps the HFX2-L11 commit.
- 2026-07-09T11:19+02:00 — 260707-HFX2-L9: `_supervisor_context()` now constructs
  `SupervisorSignalCooldownStore` and threads `settings.supervisor.signal_cooldown_seconds` into
  `SupervisorContext`; the existing redelivery floor setting continues through
  `redeliver_rate_limit_seconds`. Verification metadata pinned until closeout stamps the
  260707-HFX2-L9 commit.
- 2026-07-08T23:59+02:00 — 260707-HFX2-L8 (dead-seat storm, R4/R6): `_supervisor_context()`
  now threads `settings.supervisor.redeliver_budget` into `SupervisorContext`; `_supervisor_heartbeat_payload()`
  includes the supervisor heartbeat's latest pending inbox count, redeliverable inbox count, and sweep
  duration so `/api/state` and SSE consumers can see backlog pressure before the stale banner trips.
  Verification metadata pinned until closeout stamps the 260707-HFX2-L8 commit.
- 2026-07-08T23:15+02:00 — 260707-HFX2-L4 route impact (small): `_supervisor_context()` now also
  resolves `settings.escalation.sla_seconds`/`rung_seconds`/`respawn_after_rung` onto
  `SupervisorContext`'s new escalation-ladder knobs — no new lifespan task, no new settings read of
  its own; reuses the exact per-sweep `load_agentic_settings` call already wired for the supervisor
  family. Verification metadata pinned until closeout stamps the 260707-HFX2-L4 commit.
- 2026-07-08T18:45+02:00 — 260707-HFX2-L2 (supervisor sweep + predicates, R1/R3/R4/R5): added
  `supervisor_loop()` (a third decoupled-cadence lifespan task, following the `metrics_loop`
  template exactly — settings-driven interval/enable, exception-tolerant, cancelled at shutdown)
  and `_supervisor_context()` wiring `SupervisorContext` from the app's own catalog/host/paster plus
  fresh `ExpectationRowStore`/`OperatorInboxStore`/`OrchestrationNudgeStore`/`EventStore` instances
  (stores-not-projections, R3). Added the shared `SupervisorHeartbeatStore` and
  `_supervisor_heartbeat_payload()` (R5): `supervisorHeartbeat` now rides both `GET /api/state`'s
  JSON body and the SSE snapshot (`stream_events` gained a `supervisor_heartbeat` keyword),
  computed at response/connect time and deliberately excluded from the `/api/state` ETag revision
  (same volatile-age posture as `servingBuild`). New imports: `serving.supervisor`,
  `serving.supervisor_heartbeat`, `ExpectationRowStore`, `OrchestrationNudgeStore`, `EventStore`.
  Verification metadata pinned until closeout stamps the 260707-HFX2-L2 commit.
- 2026-07-08T02:55+02:00 — 260707-HFX-L8 (seat lifecycle: retirement + live identity + turn-state):
  new `TerminalRetireRequest`/`TerminalRenameRequest` models and two new routes,
  `POST /api/terminal/{session}/retire` (authority-checked via `check_retire_authority`, idempotent
  already-retired fast path, 403 retire-refused with a named policy clause on refusal) and
  `POST /api/terminal/{session}/rename` (identity text only). `create_app`'s
  `TerminalCatalogLivenessSweeper` construction gained `on_turn_state_change=lambda observation:
  log_turn_state_change_event(config, observation.entry)`, wiring sweep-detected turn-state
  transitions into observer events. Verification metadata pinned until closeout stamps the HFX-L8
  commit.
- 2026-07-08T01:00+02:00 — 260707-HFX-L7 route impact (small): the metrics sampling loop's `try`
  block now also calls `await asyncio.to_thread(evaluate_provider_degradation, config)` right
  after `metrics_store.record(snapshot)`, sharing the loop's existing exception-tolerant handling.
  This is a two-line addition (import + one call); no route shape, endpoint, or lifespan
  structure changed. Verification metadata pinned until closeout stamps the HFX-L7 commit.
- 2026-07-07T23:45+02:00 — 260707-HFX-L5 (catalog liveness hysteresis): deleted
  `_refresh_catalog_entries` (the immediate exit-mark refresh); `create_app` now wires
  `liveness_clock = now or utc_now`, one `TerminalCatalogLivenessConfig`, and one
  `TerminalCatalogLivenessSweeper` — `GET /api/terminal/sessions` returns
  `liveness_sweeper.refresh()` (≤1 probe sweep per 10s, non-overlapping; rate-limited callers get
  the persisted catalog), and WebSocket attach (`_attach_terminal_session` gained `checked_at` +
  `liveness_config`) and the `/paste` endpoint run direct `observe_terminal_liveness` observations
  with the injected clock (L5R2: no hard `utc_now()` beside a sim replay clock). Transient tmux
  command failures now record hysteresis evidence instead of exit-marking; false exits self-heal.
  Verification metadata pinned until closeout stamps the HFX-L5 commit.
- 2026-07-07T23:20+02:00 — 260707-HFX-L3 round 2: the paste endpoint attaches the pane `capture`
  on submit-failure too (`not delivered or (submit and not submitted)`), tested in both directions;
  the per-field `status` stays truthful (`"delivered"` even when submit failed).
- 2026-07-07T22:15+02:00 — 260707-HFX-L3 (capture-verified delivery): the `/paste` endpoint's
  unconfirmed response now ships `capture` — the paster's final pane snapshot — as loud-failure
  evidence (omitted on delivered); same paster mechanic as the spawn tool, no separate path. The
  route shape is otherwise unchanged. Verification metadata pinned until closeout stamps the
  HFX-L3 commit.
- 2026-07-07T20:50+02:00 — 260707-HFX-L4: dashboard terminal open and attach-leaf routes now
  normalize accepted `leafKey` refs to canonical qualified task-doc ids before opener/catalog writes and
  return `400` leaf-ref refusals before mutation when refs are missing or ambiguous. Verification metadata
  pinned until closeout stamps the 260707-HFX-L4 commit.
- 2026-07-07T16:30+02:00 — 260707-HFX-L1 (provider containment R4): the lifespan now starts a
  provider metrics sampling task beside the projector — `sample_provider_containers` →
  `ProviderMetricsStore.record` every `DEFAULT_SAMPLE_INTERVAL_SECONDS` (30s, decoupled from the
  1s tick), exception-tolerant loop (module `logger` added), cancelled and awaited at shutdown.
  Verification metadata pinned until closeout stamps the HFX-L1 commit.
- 2026-07-07T12:40+02:00 — L16 adversarial-review follow-up (L16R-1): registry load scoped to harness-resolving opens; scratch terminals immune to settings errors; regression test added. Verification metadata pinned until closeout stamps the L16 commit.
- 2026-07-07T09:45+02:00 — 260703-L16 (spawn knob application): `GET /api/harnesses` and the
  `POST /api/terminal/{session}` opener now resolve against the EFFECTIVE harness registry
  (builtin merged with `orchestration.harnesses` from the global agentic settings, read per
  request via `load_agentic_settings`) so settings-defined harnesses spawn from the dashboard and
  argv customizations apply on both spawn paths. Two call sites; no route shapes changed.
  Verification metadata pinned until closeout stamps the L16 commit.
- 2026-07-07T05:10+02:00 — 260703-L15 (S1 + S3): `/api/state` gained the change gate — weak
  `ETag` from `projector.revision(seq)`, `If-None-Match` → `304` via `_if_none_match_matches`,
  `Cache-Control: no-cache` — and both `/api/state` and the SSE snapshot now carry the boot-time
  `servingBuild` stamp (`resolve_serving_build()` once in `create_app`; `stream_events` gained
  the `build` keyword). Verification metadata pinned until closeout stamps the L15 commit.
- 2026-07-06T01:30+02:00 — agent-orchestration L9: `create_app` now also calls
  `register_notes_routes(app, config)` between `register_changeset_routes` and `mount_static`,
  mounting the read-only `/api/notes/{list,read}` coordination-notes API (handlers in
  `serving/notes.py`) — registered before the greedy `/` static mount. Verification metadata
  pinned until closeout stamps the L9 commit.
- 2026-07-04T12:31+02:00 - L3: `/api/operator-inbox` now accepts agent-role,
  message-kind, artifact, and delivery-request metadata and attempts hosted push
  through the shared terminal paster while keeping the durable inbox row.
  Verification metadata pinned until closeout stamps the L3 commit.
- 2026-07-04T11:10+02:00 — L2 (agent-facing dispatch): the `POST /api/terminal/{session}` opener now
  delegates the whole leaf-claim + tmux-ensure + catalog-upsert composition to the new shared
  `serving.terminal_opener.open_terminal_session` (`resolve_terminal_launch` / `_terminal_label` /
  `_claim_leaf_or_409` **left this module** for the opener — `_claim_leaf_or_409`'s logic is now the
  opener's `leaf_conflict_owner` call), so this route and the agent-facing `spawn_agent_session` MCP tool
  spawn through ONE opener (no parallel spawn path); the route just maps `bad-kind`/`leaf-taken`/`opened`
  to 400/409/200. Added `POST /api/terminal/{session}/paste` (the server-side echo-confirmed context
  paste over `serving.terminal_paste.TerminalPaster` — 404 on unknown/gone session, else
  delivered/submitted) + `TerminalPasteRequest`, and a `terminal_paster` `create_app` param. Verification
  metadata pinned until closeout stamps the L2 commit.
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
