# mcp/src/agents_remember/serving/app.py

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember                            |
| path                   | `mcp/src/agents_remember/serving/app.py`   |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated | 2026-08-30T15:15:36+02:00 |
| lastVerifiedCommitHash | `dc03c64a91947cee470622c560c516854eec86b5` |
| lastVerifiedCommitDate | 2026-08-30T17:41:53+02:00|
| governingOverview      | `overview.md`                              |

## Governing Overview

[overview.md](overview.md)

## Purpose

Provides the stable FastAPI composition facade and curated public imports for the serving package.

## Code Commentary

### Logic

`create_app` builds runtime collaborators, registers route families, installs the lifespan, and
returns the app. Terminal assignment exports now use `TerminalAttachTaskRequest` and
`_attach_task_response`; removed leaf-ref helpers are absent. Detailed routing behavior remains in
the private route modules. Serving runtime composition receives `process_serving_build()`, the same
cached process identity projected by MCP `server_info`.

### Conventions

This facade re-exports tested patch/import seams but does not reimplement their behavior.

### Invariants And Boundaries

- Public serving composition exposes task assignment, not leaf assignment.
- Startup migration is delegated to the lifespan.
- Route behavior stays in owned submodules.
- Dashboard and MCP surfaces must not resolve separate build identities inside one process.

### Todos

None.

## Docs References

No Domain Documentation source is configured.

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| App creation composes the serving route and lifespan families. | `create_app` | mcp/src/agents_remember/serving/app.py:230-301 |
| The facade exports structural task-assignment names. | "\"TerminalAttachTaskRequest\"," | mcp/src/agents_remember/serving/app.py:321-321 |

## Cross-Repo References

No cross-repository implementation dependency governs this file.

## 260821-CLIVE Serving Composition

App construction now threads the two task-execution registrars into their owning flows. Terminal
liveness receives `TerminalLivenessActions` containing turn-state observation plus the terminal
registrar; the notifier runtime receives the inbox registrar. Registration is deliberately outside
catalog/inbox deletion decisions and uses task-owned proof, while ordinary injected test seams that
omit registrars remain fail-closed.

## Update History

- 2026-08-30T15:15:36+02:00 — 260821-ARSPAWN-L4: app composition now consumes the shared cached
  process build used by MCP identity advertisement. Verification remains closeout-owned.

- 2026-08-24T14:43+02:00 — 260821-CLIVE cumulative curation: recorded production composition of terminal and inbox execution registration. Timestamp is the curator host's Europe/Berlin system time; verification remains closeout-owned.

- 2026-08-07T22:45:00+02:00 — 260731-EFA-L7 curator: now a facade over `_app_common.py`, `_app_lifespan.py`, `_app_routes.py`, `_app_terminal_routes.py`; full surface re-exported and pinned. Verification metadata stays pinned until closeout stamps the 260731-EFA-L7 commit.

- 2026-08-05T19:26+02:00 — 260731-EFA-L16 curator: recorded the image route's offload —
  `_terminal_image_response` runs the catalog read (`runtime.catalog.get`) and the
  `_write_paste_image` disk write on `asyncio.to_thread`, keeping the catalog RLock wait and
  blocking I/O off the event loop (the loop-side seat of the 2026-08-05 deadlock). Verification
  metadata stays pinned until closeout stamps the L16 commit.
- 2026-08-04T03:21:00+02:00 — S18-SR3-B05 curator: regenerated the serving helper and trusted-attribution whole-claim binding with the locked scoped fixer and inspected the complete generated function extent; no approved semantic claim changes.
- 2026-08-04T03:03:32+02:00 — S18-SR3-B05 worker: selected the complete serving helper as the direct-call and trusted-attribution anchor and returned the whole binding to provisional fixer input.
- 2026-08-04T02:35:12+02:00 — S18-B05 curator delta: resolved provisional source-local citation bindings with fixer-generated current-source ranges; no approved semantic claim changes.
- 2026-08-04T01:28:33+02:00 — S18-SR2-B05 worker: corrected gate recording and operator-inbox ownership, separated explicit REST operator input from spawn/durable briefs, and rebound shared-opener composition to the actual application spawn command; new bindings remain provisional.
- 2026-08-04T00:22:04+02:00 — 260731-EFA-L6 S18-B05 curator: repaired and normalised mechanical citation findings with current source anchors and fixer-generated ranges; no semantic claim changes. Verification metadata pinned until closeout stamps the L6 code commit.
- 2026-08-01T09:44+02:00 — 260731-EFA-L4 curator: recorded the de-injection and the route
  declarations. `servingBuild`/`supervisorHeartbeat` were being written into an already-dumped,
  already-validated projection dict with nothing declaring them; both sites now call the single
  `served_state.served_state_tail` (L328-L329 for the SSE snapshot, L979-L982 for `/api/state`)
  and the result is declared as `ServedWorkspaceProjection`, which `/api/state` and `/api/stream`
  name. Corrected cit:(["def _agent_notifier_heartbeat_payload(runtime: _ServingRuntime) -> AgentNotifierHeartbeatPayload:"], mcp/src/agents_remember/serving/_app_lifespan.py:256-256) and cit:(["async def stream_events("], mcp/src/agents_remember/serving/_app_common.py:116-116),
  which return/accept declared models rather than bare dicts, and the `stream_events` paragraph,
  which now records that a snapshot with neither key is a valid served body and that deltas carry
  no tail. Documented all 17 route declarations with lines — including `/api/state`'s
  model-less `304` entry, `/api/actions/{action}`'s `status_code=202` (the implicit 200 was a
  pair no request can produce), the two two-success-shape terminal routes, and the websocket as
  the one structurally undeclarable route — plus the two bare-`dict` routes
  (`/api/terminal/sessions`, `/api/harnesses`) where FastAPI really does validate and a drifted
  `to_json` is now a live 500, held off by the CI key-set equality test. Added two invariants
  (the declared app-layer boundary, and why the body must stay assembled). Repaired 3 citations:
  the change-set registrar bullet L711-L713/L733 → L749-L751/L771; `test_serving.py` L430-L492 →
  L441-L503 (the `_build_wire` helper added 11 lines above `StreamEventsTests`); and
  `harness_control_api.py` L140-L163/L194-L339/L539-L572 → L156-L179/L210-L409/L618-L651
  (`resolve_terminal_open_selection`, the registrar calls through `_register_submission_routes`,
  and `_running_control_entry`). No wire bytes moved. Verification metadata pinned until closeout
  stamps the L4 commit.

- 2026-07-31T19:30+02:00 — 260731-EFA-L2 curator: repaired 1 incomplete self-citation. The
  change-set bullet cited cit:([`create_app`], mcp/src/agents_remember/serving/app.py:226-285) for a claim about ordering relative to `mount_static`, but
  that span holds only the three registrar calls; `mount_static(app)` is at L733, so the citation
  now names both. Two other flagged items in this card were checked and left alone: `(L2)` and
  `(L5)` next to `collaborators.terminal_catalog` / `lifecycleId` are leaf identifiers
  (260731-EFA-L2, …-L5), not line citations.

- 2026-07-31T17:20+02:00 — 260731-EFA-L2 curator: repaired 2 cross-file line citations. The
  `harness_control_api.py` row's single `L64-L249` span no longer matches the module, which now
  splits registration across three private registrars; replaced it with the three ranges that
  actually hold the named material — `resolve_terminal_open_selection` at L140-L163 (launch
  selection), L194-L339 (the registrar calls plus `_register_capability_routes`' harness-neutral
  advertise and exact-session set-model/set-effort, and `_register_submission_routes`' submit and
  reconcile), and `_running_control_entry` at L539-L572 (liveness-first status mapping, now
  memoized). The `test_serving.py` row moved to L430-L492 — `StreamEventsTests`' interleaved-
  projection handoff test, `test_failed_prime_recovery_emits_one_snapshot_then_normal_deltas`
  (which carries both the identical-republish suppression and the later tokens delta), and
  `test_cancelled_waiting_stream_releases_its_subscription`. Both claims verified unchanged.

- 2026-07-31T16:10+02:00 — 260731-EFA-L2 curator: recorded the structural rewrite — `create_app`'s four
  composition values (`ProjectionCadence`, `ProjectionReplay`, `LiveProjectionInputs`,
  `ServingCollaborators`), the `_ServingRuntime` bundle that replaced closure capture, the
  module-level handlers/loops/registrars, and the two duplicated request-shape guards
  (`missing-gate-id`, the dismissal scope re-check) deleted because `actions.py` already refuses
  those shapes. Verification metadata stays pinned until closeout.
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
- 2026-07-09T11:19+02:00 — 260707-HFX2-L9: `_agent_notifier_context()` now constructs
  `AgentNotifierSignalCooldownStore` and threads `settings.supervisor.signal_cooldown_seconds` into
  `AgentNotifierContext`; the existing redelivery floor setting continues through
  `redeliver_rate_limit_seconds`. Verification metadata pinned until closeout stamps the
  260707-HFX2-L9 commit.
- 2026-07-08T23:59+02:00 — 260707-HFX2-L8 (dead-seat storm, R4/R6): `_agent_notifier_context()`
  now threads `settings.supervisor.redeliver_budget` into `AgentNotifierContext`; `_agent_notifier_heartbeat_payload()`
  includes the supervisor heartbeat's latest pending inbox count, redeliverable inbox count, and sweep
  duration so `/api/state` and SSE consumers can see backlog pressure before the stale banner trips.
  Verification metadata pinned until closeout stamps the 260707-HFX2-L8 commit.
- 2026-07-08T23:15+02:00 — 260707-HFX2-L4 route impact (small): `_agent_notifier_context()` now also
  resolves `settings.escalation.sla_seconds`/`rung_seconds`/`respawn_after_rung` onto
  `AgentNotifierContext`'s new escalation-ladder knobs — no new lifespan task, no new settings read of
  its own; reuses the exact per-sweep `load_agentic_settings` call already wired for the supervisor
  family. Verification metadata pinned until closeout stamps the 260707-HFX2-L4 commit.
- 2026-07-08T18:45+02:00 — 260707-HFX2-L2 (supervisor sweep + predicates, R1/R3/R4/R5): added
  `supervisor_loop()` (a third decoupled-cadence lifespan task, following the `metrics_loop`
  template exactly — settings-driven interval/enable, exception-tolerant, cancelled at shutdown)
  and `_agent_notifier_context()` wiring `AgentNotifierContext` from the app's own catalog/host/paster plus
  fresh `ExpectationRowStore`/`OperatorInboxStore`/`OrchestrationNudgeStore`/`EventStore` instances
  (stores-not-projections, R3). Added the shared `AgentNotifierHeartbeatStore` and
  `_agent_notifier_heartbeat_payload()` (R5): `supervisorHeartbeat` now rides both `GET /api/state`'s
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
- 2026-06-29T15:30+02:00 — operations-integration L3: `create_app` now also calls `register_changeset_routes(app, config)` between `register_files_routes` and `mount_static` (cit:([`create_app`], mcp/src/agents_remember/serving/app.py:226-285)), mounting the read-only `/api/changeset/{task,file-diff,master}` change-set API (handlers in `serving/changeset.py`) — registered before the greedy `/` static mount. Verification metadata pinned to the task base until closeout stamps the L3 code commit.
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
