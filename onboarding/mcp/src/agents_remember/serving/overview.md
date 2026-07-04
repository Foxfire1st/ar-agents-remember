# mcp/src/agents_remember/serving/ — Dashboard Serving Layer Overview

| Field                  | Value                                            |
| ---------------------- | ------------------------------------------------ |
| repository             | agents-remember                                  |
| sourceRoute            | `mcp/src/agents_remember/serving/`               |
| doc_type               | `route-local-overview`                           |
| lastUpdated            | 2026-07-04T12:31+02:00 |
| lastVerifiedCommitHash | `6b940141fc319f1d2d18b2c94fd9e9a213d43141`       |
| lastVerifiedCommitDate | 2026-07-04T12:52:03+02:00|
| governingOverview      | `../../../../overview.md`                         |

## Governing Overview

[mcp/overview.md](../../../../overview.md)

## Purpose

`serving/` is the **local dashboard serving layer** (slice 04 of the 3.0
browser-dashboard series): a FastAPI app over the observer projection read side. It
is **transport only** — it adds no interpretation (the reducer owns that) and reads
coordination state exclusively through `McpRuntimeConfig` + `observer.paths`
(North-Star #5), never raw host paths. It serves `project_and_write`'s
`WorkspaceProjection` live over SSE, tails the raw observer event log, ships the static
cockpit bundle, opens the POST action return-channel (targeted gate decisions are
developer-attributed and binding), and hosts the Mode B2 terminal backend
(`terminal.py` — tmux-wrapped PTY sessions, slice 6d-1) bridged to the browser over the
`@app.websocket("/api/terminal/{session}")` WebSocket (slice 6d-2); a `POST /api/terminal/{session}`
opener + `GET /api/harnesses` let the dashboard spawn + own a shell or a detected harness (slices
6e-2a/6e-2b, the `harnesses.py` registry). Task 10/L3 adds `POST /api/operator-inbox`, the trusted
developer/dashboard write side for durable inbox messages; L3 can immediately push a queued row into a
matching hosted session through the shared terminal paster while keeping the row pollable.
Task 23/24 adds `POST /api/operator-inbox/{entry_id}/dismiss`, the delete path
for stale task-row pickup warnings. Task 22 adds `terminal_catalog.py` and the durable terminal-session
surface: opener rows persist under `logs/dashboard/terminal-sessions.json`, `/api/terminal/sessions`
hydrates the UI after refresh, the opener creates detached tmux sessions, each WebSocket gets its own
tmux client only after a tmux probe, and explicit terminate kills tmux and hides the row from normal
lists. L9 adds `terminal_leaf_assignment.py`, the shared catalog move policy used by both
`POST /api/terminal/{session}/attach-leaf` and the agent-facing MCP tool so hosted chats can move between
durable leaves without respawn. L2 (agent-facing dispatch) adds `terminal_opener.py` — the shared
hosted-session **opener** (leaf claim + env-seeded tmux ensure + catalog upsert) that both the
`POST /api/terminal/{session}` route and the agent-facing `spawn_agent_session` MCP tool compose over so
there is **no parallel spawn path** — and `terminal_paste.py`, the server-side echo-confirmed stdin paste
that backs the new `POST /api/terminal/{session}/paste` endpoint and the tool's context delivery. `terminal.py`
gains an `env` knob-injection seam (`tmux new-session -e KEY=VALUE`) and `terminal_catalog.py` gains
spawned-by provenance columns for the orchestration tree. Run via
`agents-remember dashboard` (the `cli/` umbrella); `--sim` replays a recorded fixture
through the byte-identical path.

## Hot Path Summary

`agents-remember dashboard --config <settings.json>` → `cli/dashboard.py` →
`serving.app.create_app(config)`. The app's lifespan starts one `Projector` that ticks
`project_and_write` on `--interval`, refreshing provider current-state first in live mode, then diffs each
projection against the last
(`serving.delta.diff_projection`), and fans **per-entity deltas** out to every SSE
client. `GET /api/stream` emits `event:snapshot` then per-entity `lifecycle`/`enclosure`/
`provider`/`metrics`/`analytics` (and `*.removed`) events; `GET /api/state` returns the
projection once; `GET /api/events` tails the raw `ar-observer-event/v1` log with exact
byte-offset `Last-Event-ID` resume (`serving.events`), doing one retained-backlog scan per connect,
streaming that bounded backlog in chunks (no whole-history materialization), filtering
`lifecycle.heartbeat` out of the river, and pruning expired logs on a slow cadence; `POST /api/actions/{action}`
validates lifecycle transitions against `ActionAvailability` (no mutation) and records
targeted gate-decision verbs as developer-attributed gate decisions, including `gateId` staleness
checks and rejection notes (`serving.actions` + `gate_decide_for_lifecycle`). `POST /api/operator-inbox` writes developer/dashboard-attributed
external-chat responses through `mcp/tools/operator_inbox.py` so non-hosted agents can poll/consume
them; Task 29 S7 also lets `/api/actions/dismiss` persist targetless actionable-drift acknowledgements
and the raw `/api/events` stream sends a one-shot `ready` marker after retained backlog replay, so the
frontend can avoid painting an empty feed before history has arrived. `POST /api/operator-inbox/{entry_id}/dismiss` deletes stale pending entries after the pickup TTL
warning is shown. `--sim` swaps a replay clock + fixture feeder onto the projector's
`now`/`before_tick` seams (`serving.sim`). Gate-id-only `cancel` requests are the explicit legacy
cleanup path for workspace-shaped stale gates; approve/reject/revision stay lifecycle-targeted. The static bundle (`package_data/dashboard/`)
mounts at `/`. The Mode B2 terminal bridge `@app.websocket("/api/terminal/{session}")` (6d-2)
attaches one concrete `TerminalHost.attach` tmux client per browser WebSocket — binary PTY bytes out,
JSON `stdin`/`resize` in (the `websockets` dep is uvicorn's WS impl). The bridge can rehydrate catalog
rows after a dashboard restart, but only after `TerminalHost.has_session` proves the tmux name still
exists; normal browser disconnect closes only that websocket's PTY client while leaving the tmux/catalog
row running so refreshes and second browser tabs get fresh independent attaches; stale running rows
become `exited`, and `POST /api/terminal/{session}/terminate` is the only destructive terminal action.

## Route Model

- `app.py` — `create_app(config, *, interval, now, before_tick, refresh_provider_state)` builds the FastAPI app: a
  lifespan that primes + runs one shared `Projector`, `GET /api/state` (one-shot),
  `GET /api/stream` (the `state` SSE endpoint, delegating to the testable `stream_events`),
  `GET /api/events` (the raw channel, delegating to `stream_raw_events`; fresh
  connections start from lifecycle-aware retained offsets while valid
  `Last-Event-ID` cursors still resume exactly and emit a backend `ready` event after retained replay),
  `POST /api/actions/{action}` (delegating to `evaluate_action`; gate verbs carry targeted
  `gateId`/`note`, require a reason for reject, and distinguish stale gates from no-open-gate), the
  `@app.websocket("/api/terminal/{session}")` Mode B2 terminal bridge (6d-2 — catalog-backed
  per-websocket `TerminalHost.attach`, binary PTY bytes out / JSON `stdin`+`resize` in, via the
  module-level `_bridge_terminal`/`_apply_terminal_session_input` helpers), `POST /api/operator-inbox` (task 10/L3 — call
  `operator_inbox_post_payload` with developer/dashboard attribution for durable inbox messages,
  accepting lifecycle/agent/recipient role plus role/message/artifact metadata and passing catalog/host/paster
  seams for optional hosted push; bad lifecycle/agent/role addressing returns `400 bad-address`),
  `POST /api/operator-inbox/{entry_id}/dismiss` (task 23/24 — physically delete a pending inbox entry
  for dismissible `check chat` warnings), the
  `POST /api/terminal/{session}` **opener**
  (6e-2a/6e-2b; **since L2** the leaf-claim + `host.ensure` + catalog-upsert composition delegates to the
  shared `terminal_opener.open_terminal_session` — `resolve_terminal_launch` / `_terminal_label` / the
  role-scoped conflict check all left `app.py` for that module — so this route and the `spawn_agent_session`
  MCP tool spawn through ONE opener; the route maps `bad-kind`→400 / `leaf-taken`→409 / `opened`→200.
  Server-resolved harness id, never on the wire; the opener passes `suspend_unsafe=(kind=="harness")` so
  later host writes strip Ctrl-Z for bare-pane harnesses, slice 6f, and persists a `TerminalCatalogEntry`
  carrying label/lifecycle/cwd/tmux/command/status/leafKey + L2 spawned-by provenance without opening a
  starter PTY client; **slice L5** uniqueness is per (leaf, role) so a terminal never collides with the
  leaf's chat, and the `leafKey` is persisted (preserving an existing binding when none is sent) and
  echoed),
  `POST /api/terminal/{session}/paste` (**L2/L3** — server-side echo-confirmed context-packet delivery to a
  hosted session with no attached browser client, over `terminal_paste.TerminalPaster`; L3 requires a
  real pasted draft/chip echo across the boot retry window, not mere pane output; 404 on
  unknown/gone session, else `{delivered, submitted}`),
  `POST /api/terminal/{session}/attach-leaf` (**slice L5/L9** — claim or move a leaf for an existing
  session, enclosure-free / no respawn; delegates to `terminal_leaf_assignment.assign_terminal_session_to_leaf`,
  returning `404 unknown-session`, `409 leaf-taken` without mutation, or `200 attached`), `GET
  /api/terminal/sessions` (task 22 — refresh stale catalog rows and return non-terminated sessions),
  `POST /api/terminal/{session}/terminate` (task 22 — kill tmux and mark the catalog row terminated),
  `GET /api/harnesses` (6e-2b — `detect_harnesses()` per `shutil.which`), `POST /api/terminal/{session}/image`
  (6f — save a validated screenshot under `<cwd>/.dashboard-pastes/<uuid>.<ext>` using either a live host
  session cwd or a catalog-restored cwd so the composer can inject its path; the terminal channel is
  text-only), and the static mount.
  SSE uses built-in `fastapi.sse` (`EventSourceResponse`/`ServerSentEvent`).
- `daemon.py` — the dashboard daemon supervisor (260703 L2): `ensure()` adopts a healthy detached
  daemon, spawns a missing one, and restarts on version/host/port mismatch, behind one
  non-blocking flock (`ensure.lock`) so concurrent MCP boots never double-spawn. State lives under
  `<coordinationRoot>/logs/dashboard/` — an atomic `daemon.json` (pid/host/port/version/paths,
  written immediately after spawn) and a per-spawn-rotated `dashboard.log` (the child serves with
  `--no-access-log` so the log stays bounded). Liveness is kill-probe **plus** `/proc/<pid>/cmdline`
  identity (pid reuse and zombies read as stale); stop is TERM → bounded wait → KILL. The child is
  the plain foreground CLI addressed by module string — the module stays import-light (stdlib +
  config types, never uvicorn/FastAPI), so `mcp/server.py`'s boot hook
  (`maybe_autostart_dashboard`, threaded/total/stderr-only, gated by the `dashboard.autoStart`
  settings key) never pulls the serving stack into MCP startup.
- `projector.py` — `Projector`: owns the latest projection, a monotonic sequence, and the
  subscriber fan-out. `prime()`, `run()` (tick: re-project → diff → broadcast), `current()`,
  `subscribe()`. The `now`/`before_tick` seams + `_tick_sync(moment)` keep one loop generic
  across live and sim. Live projectors can pass a provider refresher into the observer store; sim projectors
  keep fixture state deterministic by omitting it. One re-projection per tick regardless of client count.
- `delta.py` — the **pure** `diff_projection(previous, current) -> list[DeltaEvent]`: the
  per-entity diff over the flat id-keyed collections (upserts in projection order, removals
  sorted for determinism). A transport concern kept out of the reducer. Task 33: it also emits an
  `activeWorktreeGroups` whole-value delta (a bare list wrapped as `{"activeWorktreeGroups": [...]}`)
  when that set changes, alongside the `metrics`/`analytics` whole-block events.
- `events.py` — the raw `event` channel: the **pure** byte-offset tail `read_new_events` (a
  composite per-source offset cursor, `encode_cursor`/`decode_cursor`) + the `stream_raw_events`
  async tailer. Fresh connections use `observer.event_retention.initial_event_offsets` so expired
  (inactivity-pruned) lifecycle logs are skipped, workspace/lifecycle-less rows are bounded by age, and
  active lifecycle histories remain uncapped; malformed/empty cursors fall back to those retained offsets,
  while valid `Last-Event-ID` cursors keep exact byte-offset resume. Separate from `/api/stream`
  (byte-offset resume vs. snapshot resume). Task 29 S7 emits `event: ready` once after the retained
  backlog is sent on each connection, giving the browser a reliable hydration boundary. Task 34 makes the
  connect path cheap and quiet: it does **one** retained-backlog scan per connect (no repeated
  whole-history reads), streams that bounded backlog to the client in **chunks** rather than
  materializing the whole history, filters `lifecycle.heartbeat` events out of the river, and prunes
  expired logs on a slow background cadence instead of on every tail.
- `sim.py` — sim mode: `build_sim` + `ReplayClock` + progressive `ReplayFeeder` +
  `parse_sim_speed`, replaying a fixture's recorded events through the projector's
  `now`/`before_tick` seams over a throwaway temp root (the fixture is never mutated). `build_sim`
  also **materializes the fixture's structural surfaces** (`_materialize_surfaces` — contracts / task
  docs / provider state / ledgers / drift) into the sim root, so a rich fixture exercises the whole
  projection, not only the replayed event logs.
- `actions.py` — the POST action layer: `ActionRequest` + the **pure** `evaluate_action`.
  Lifecycle transitions map against the node's `ActionAvailability` to 202/409/404 with
  attribution (no mutation); gate-decision verbs carry a targeted `GateDecisionIntent` with optional
  `gate_id` and `note`, reject requires a non-empty reason, target omission is allowed for `cancel`
  with `gateId` and for actionable-drift `dismiss`, and the router records the result as a
  developer/dashboard-attributed gate decision via `gate_decide_for_lifecycle` or a workspace-gate
  `gate_decide_payload` cancel. Targetless actionable-drift dismissals are persisted as attention
  acknowledgements instead of gate decisions.
- `static.py` — `dashboard_static_dir()` resolves `package_data/dashboard` via
  `importlib.resources` (the `install.assets` idiom); `mount_static(app)` mounts it at `/`
  (non-fatal when absent).
- `files.py` — the **read-only files API** (operations-integration L1): `register_files_routes(app, config)`
  registers `GET /api/files/{repos,list,read,onboarding}` **before** `mount_static` (the greedy `/` mount
  must stay last). It is the first serving module to resolve a kernel `CoordinationContext`: a
  `{repo, mainline|enclosure}` scope maps to `(codeRoot, onboardingRoot)` to enumerate repos/enclosures,
  list one directory level (code + paired onboarding), read a file (content + drift metadata), and resolve
  the 1:1 code↔onboarding sidecar pairing both ways via the shared `kernel/sidecar_pairing.py`. Allow-listed
  roots only, realpath-confined (Task-6 posture); a memory-less repo degrades to code-only browsing and a
  missing sidecar is a normal `missing` result, never an error. Feeds the dashboard File Viewer (L2) and
  Change-Set Viewer (L3/L4).
- `scope.py` — the **shared browse-scope layer** (operations-integration L3, extracted from `files.py`):
  `FileScope`, `resolve_scope` (`{repo, mainline|enclosure}` → roots), the `run_scoped` error map (404
  unknown-repo/unknown-scope/not-found, 400 bad-path), `language_for`, and the active leaf-enclosure
  enumeration. `files.py` and `changeset.py` both import it (files.py re-exports `FileScope` +
  `_resolve_within` for callers/tests). Behaviour is identical to L1 — one resolver, shared.
- `changeset.py` — the **read-only change-set API** (operations-integration L3): `register_changeset_routes`
  mounts `GET /api/changeset/{task,file-diff,master}` **before** the static mount. Computes a task's
  `base → current` code + memory change-set with insertion/deletion counts + status + `hasSidecar`
  (`task`), BEFORE/AFTER file content for the L4 CodeMirror MergeView (`file-diff`, with an optional `master` param for the series net file-diff), and the master's **NET**
  change-set (`master`) — `git diff <master-base> <series-tip>` for code + memory (one coherent,
  per-file-inspectable range) with a per-leaf counter breakdown alongside. **L4a** adds the doc-reader
  **leaf views**: the `task` + `file-diff` routes take a `leaf` + `mode` selector (precedence
  `leaf > master > scope`), resolving one leaf's `committed` (`base → code_commit`) or `working`
  (`HEAD → worktree`, uncommitted only) change-set straight off the persisted enclosure contract
  (`_load_leaf_contract`, by leaf-id — works with no live worktree, for a completed leaf), with the
  selector validated (`leaf` needs `master` + a valid `mode` → `400`, no-live-worktree `working` → `404`).
  Reuses `scope.py` + the L1 posture; the change-detection primitive is
  `worktrees/modules/git.changed_files_with_counts`. Feeds the dashboard Change-Set Viewer (L4/L4a).
- `terminal.py` — the **Mode B2 terminal host** (slice 6d-1): `TerminalHost`, a registry of
  tmux-wrapped PTY sessions correlated to a lifecycle/worktree. `open`/`write`/
  `read_nonblocking`/`resize`/`close` over a stdlib-`pty` master fd; the spawn (`tmux
  new-session -A … -- <harness>` on `pty.openpty`) is injectable so tests drive a real kernel
  PTY without tmux. The spawn gives the child a **controlling terminal** (`os.login_tty` in a
  `preexec_fn`) + a seeded winsize, so tmux has a `/dev/tty` to size against and honors resize (slice
  6e-4). `write` strips the Ctrl-Z byte `0x1a` for **suspend-unsafe** (bare-pane harness) sessions only,
  so a harness can't be soft-locked into a suspend while a plain shell keeps its job control (slice 6f).
  Task 22 adds injectable tmux probe/create/kill hooks, `has_session`, `ensure`, `terminate`, and
  unregistered per-connection `attach` clients so the durable catalog can create a detached tmux
  session, prove it still exists before attach, kill one explicitly, and serve multiple browser tabs
  without sharing one PTY fd. **L2** threads an optional `env: Mapping[str, str]` through
  `ensure`/`open`/`_build_tmux_command` (`_tmux_create_detached` emits `tmux new-session -e KEY=VALUE`
  via the pure `_env_flags`), seeded only at creation and inert on re-attach — the minimal
  env-passthrough seam the agent-facing spawn tool injects role knobs through (empty-safe: an empty
  mapping keeps the byte-identical legacy argv). The reopened L6 wheel fix adds the injectable `TmuxConfigurer` seam
  (default: per-session `tmux set-option mouse on`, failures suppressed), asserted by `ensure` and
  every `attach`, so browser wheel input reaches tmux as mouse reports — tmux scrolls pane history for
  normal-buffer TUIs and passes wheel through to mouse-aware ones (pane text selection becomes
  Shift+drag). Its copy-mode escape companion: `write_session` arms a per-connection flag on
  mouse-report-only stdin and cancels copy-mode (injectable `TmuxModeCanceller`, `send-keys -X cancel`
  default) on the first typed input after scrolling, so typing anywhere in the scrollback snaps to the
  live bottom and reaches the pane app. Fixed-argv (no shell injection), OS-user creds, localhost. The live
  WebSocket bridge (`@app.websocket("/api/terminal/{session}")`, in `app.py`) + the `websockets`
  dep landed in 6d-2; the xterm.js viewport is 6e.
- `terminal_catalog.py` — the durable dashboard terminal-session catalog (task 22): immutable
  `TerminalCatalogEntry` rows plus a JSON store under `logs/dashboard/terminal-sessions.json`. It
  persists id, label, kind, optional harness/lifecycle, cwd, tmux name, command, timestamps, status,
  (**slice L5**) an optional `leaf_key`, and (**L2**) optional spawned-by provenance
  (`spawned_by_session` / `spawned_by_lifecycle`, written migration-safe only when set; the copiers now
  use `dataclasses.replace` so a new column survives a re-attach); normal `list()` keeps exited rows visible and filters terminated
  rows, while `include_terminated=True`
  is available for audits. Explicit termination wins over later passive exit bookkeeping so an `End`
  action cannot reappear after refresh as an `exited` row. **Slice L5** makes the catalog the
  **leaf→chat registry**: `to_json` writes `leafKey` only when set (migration-safe), `with_leaf_key` is
  the attach write point, and (L5 fix 2) a leaf-uniqueness **role** (`TerminalSessionRole`,
  `role_for_kind` / `entry.role` — a shell is a terminal, a harness is a chat) scopes
  `active_for_leaf(leaf_key, role="chat")` so it returns the single **running** owner *of that role* — the
  per-(leaf, role) single-owner probe the opener + attach-leaf routes call before an upsert, letting one
  leaf hold a running chat AND a running terminal at once.
- `terminal_leaf_assignment.py` — the shared L9 catalog reassignment helper: moves an existing catalog row
  to a new durable `leafKey`, returns `leaf-taken` without mutation when another running same-role session
  owns the target leaf, and is reused by the dashboard route and MCP tool.
- `terminal_opener.py` — the shared **L2 hosted-session opener**: `open_terminal_session(...)` resolves
  the launch (`resolve_terminal_launch` — a harness **id** to its fixed argv, moved here from `app.py`),
  claims `leaf_key` under the role-scoped per-(leaf, role) uniqueness rule **before** any spawn (a taken
  leaf returns `leaf-taken` without ensuring tmux or mutating the catalog), seeds `env` at
  `TerminalHost.ensure` (the L2 knob-injection seam), and upserts a durable `TerminalCatalogEntry`
  carrying write-once spawned-by provenance. Transport-agnostic (`OpenTerminalResult` → HTTP 200/409/400
  in `app.py`, a validated payload in the MCP tool). The ONE opener both the dashboard `POST
  /api/terminal/{session}` route and the agent-facing `spawn_agent_session` tool compose — no parallel
  spawn path.
- `terminal_paste.py` — the **L2/L3 server-side echo-confirmed paste**: `TerminalPaster.paste(tmux_name,
  text, submit=…)` mirrors the frontend `pasteAndConfirm`/`submitAndConfirm` over tmux primitives
  (`set-buffer` + `paste-buffer -p` + `capture-pane` looking for a pasted draft fragment or new paste
  chip, `send-keys Enter` on submit), re-pasting across the harness boot window because a booting harness
  can discard stdin while still producing output. Every
  tmux op + the clock are injectable so the loop is fake-driven and sleepless in tests. Never submits an
  unconfirmed paste; never raises on a gone session. Backs the `spawn_agent_session` context delivery and
  the `POST /api/terminal/{session}/paste` endpoint.
- `harnesses.py` — the **harness launch registry** (slice 6e-2b): the curated `HARNESSES` set (Claude
  Code / Codex / Pi.dev) + `find_harness` / `is_detected` / `detect_harnesses` (injectable, call-time
  `shutil.which`). The data behind `GET /api/harnesses` detection + the `kind="harness"` opener
  resolution — a harness **id** is on the wire, the fixed argv stays here (the 6d posture). Deliberately
  *not* a mirror of `scripts/sync-skills.py`.
- `__init__.py` — package docstring only; `delta`/`projector` stay importable without FastAPI.

## Invariants And Boundaries

- **Transport only.** No interpretation here — the reducer produces full projections; this
  layer serves them, diffs consecutive snapshots, tails the raw log, and reads precomputed
  action availability. The observer stays a pure fold.
- **Client-agnostic (NS #2).** The served shapes are the existing `WorkspaceProjection`
  nodes verbatim; no dashboard-bespoke endpoints in the reducer. Named per-entity SSE events let any
  client (browser, TUI, agent) merge by id. The operator-inbox POST is a dashboard serving write into
  the shared control-plane inbox, not a projection shape.
- **One read abstraction (NS #5).** Every read flows through `config` + `observer.paths` +
  `project_and_write`; sim mode swaps the root + clock at that one seam.
- **Local-first.** Bind `127.0.0.1` only, no auth in v1 (documented in `app.py`). The UI is
  never the gate *enforcement* (the mutating MCP tools bind it server-side); a gate-decision POST
  does record a developer-attributed gate *decision* (slice 6b).
- **Terminal host = render-not-scrape, fixed argv (slice 6d).** `terminal.py` launches the
  harness on a PTY whose raw bytes xterm.js renders verbatim; the spawn is a `Sequence[str]`
  (never a shell string — no injection surface), runs as the dashboard's own OS user, and
  persists via tmux. PTY attach, detached creation, and termination are injectable for tests. Rehydrate
  probes tmux before using `tmux new-session -A`, and detach remains non-destructive; termination is
  explicit.
- **Two resume models, two streams.** The `state` channel re-snapshots on (re)connect; the
  raw `event` channel resumes by exact byte offset (`Last-Event-ID`) when the client presents a
  valid cursor, while fresh connections do one retained-backlog scan, stream that bounded backlog in
  chunks (heartbeats filtered, no whole-history materialization) instead of replaying every
  historical raw row, and then emit a `ready` marker. They stay separate.
- **Sim is a seam, not a fork.** Only `now` + `coordination_root` differ from live, so the
  SSE output is byte-identical and replay is deterministic.

## Repo-Internal References

| Finding | Source Path |
| --- | --- |
| The tick entry the projector drives (read → fold → atomic write; the `now` seam + fixture loader). | [observer/projection_store.py](agents-remember/mcp/src/agents_remember/observer/projection_store.py) |
| The served shapes (`WorkspaceProjection`, `ActionAvailability`). | [observer/projection.py](agents-remember/mcp/src/agents_remember/observer/projection.py) |
| The raw event envelope + log layout tailed by `events.py`/`sim.py`. | [observer/store.py](agents-remember/mcp/src/agents_remember/observer/store.py) |
| The one read/path abstraction (NS #5). | [observer/paths.py](agents-remember/mcp/src/agents_remember/observer/paths.py) |
| The `--config` → `McpRuntimeConfig` contract the CLI mirrors. | [mcp/config.py](agents-remember/mcp/src/agents_remember/mcp/config.py) |
| The umbrella CLI entry that launches the server (and wires `--sim`). | [cli/__main__.py](agents-remember/mcp/src/agents_remember/cli/__main__.py) |
| The transport design (SSE, snapshot-then-deltas, raw channel, sim, placement). | [docs/design/observable-lifecycle.md](agents-remember/docs/design/observable-lifecycle.md) |

## Update History

- 2026-07-04T12:31+02:00 - L3 route impact: `/api/operator-inbox` now accepts
  agent-role/message/artifact metadata, attempts hosted push through
  `inbox_delivery.py`, and `terminal_paste.py` confirms delivery only on a real
  pasted draft/chip echo across the boot window. Verification metadata pinned
  until closeout stamps the L3 commit.
- 2026-07-04T11:10+02:00 — agent-orchestration L2 route impact: the route gains `terminal_opener.py`
  (the shared hosted-session opener extracted from `app.py`'s inline opener handler — leaf claim +
  env-seeded tmux ensure + catalog upsert; `resolve_terminal_launch`/`_terminal_label`/the role-scoped
  conflict check moved here) and `terminal_paste.py` (the server-side echo-confirmed stdin paste mirror
  of the frontend). `app.py`'s `POST /api/terminal/{session}` opener now delegates to the shared opener
  (so it and the `spawn_agent_session` MCP tool share ONE spawn path) and gains `POST
  /api/terminal/{session}/paste` + a `terminal_paster` `create_app` param; `terminal.py` gains the `env`
  knob-injection seam (`tmux new-session -e`); `terminal_catalog.py` gains spawned-by provenance columns
  (via `dataclasses.replace` copiers). Covered by `test_terminal_opener.py`, `test_terminal_paste.py`,
  `test_spawn_agent_session.py`. Verification metadata pinned until closeout stamps the L2 commit.
  (Distinct from the 260703-L2 daemon-supervision entry below.)
- 2026-07-03T12:57+02:00 — 260703 L2 route impact: the route gains `daemon.py` — the dashboard
  daemon supervisor (flock-guarded ensure: adopt/spawn/restart-on-mismatch; atomic `daemon.json`;
  identity-checked liveness; TERM→KILL stop; the threaded `maybe_autostart_dashboard` MCP boot
  hook). Covered by `mcp/tests/test_dashboard_daemon.py`. Verification metadata pinned until
  closeout stamps the code commit.
- 2026-07-03T12:50+02:00 — No route impact: L15 changed only pyright-visible narrowing inside changeset.py; the serving surface and behavior are unchanged.
- 2026-07-02T17:25+02:00 — Reopened L6 copy-mode escape route impact: `terminal.py`'s `write_session`
  now cancels tmux copy-mode (new injectable `TmuxModeCanceller`, `tmux send-keys -X cancel` default)
  on the first typed input after mouse-report traffic, because copy-mode captures the keyboard and
  scrolled-up non-mouse panes swallowed typing until scrolled back to the bottom. At most one cancel
  per scroll-then-type cycle; mouse-aware panes never trigger it. Verification metadata pinned until
  closeout stamps the follow-up commit.
- 2026-07-02T17:04+02:00 — L9 route impact: added `terminal_leaf_assignment.py` and made
  `app.py`'s existing `attach-leaf` route a move/reassign route over the shared helper. The route now
  shares server-authoritative catalog conflict handling with the agent-facing MCP tool and preserves
  `leaf-taken` no-mutation semantics. Verification metadata pinned until closeout stamps the L9 commit.
- 2026-07-02T16:35+02:00 — Reopened L6 wheel fix route impact: `terminal.py` gained the injectable
  `TmuxConfigurer` seam (default `_tmux_enable_mouse`: per-session `tmux set-option mouse on`, failures
  suppressed, DEVNULL hygiene), asserted by `ensure` after create/probe and by every `attach`. Browser
  wheel input now reaches tmux as mouse reports, scrolling pane history for normal-buffer TUIs and
  passing through to mouse-aware TUIs; pane text selection becomes Shift+drag. Verification metadata
  pinned until closeout stamps the follow-up commit.
- 2026-06-30T00:00:00+02:00 — L5 follow-up route impact: leaf uniqueness is now per **(leaf, role)**. `terminal_catalog.py`
  gained `TerminalSessionRole` / `role_for_kind` / `entry.role` and a role kwarg on `active_for_leaf`; in
  `app.py` `_claim_leaf_or_409` is role-aware — the opener passes `role_for_kind(kind)` and `attach-leaf`
  passes `entry.role`, so a terminal can sit beside the leaf's agent chat (no 409) while a second chat or
  terminal still 409s. Updated the `app.py` opener/attach-leaf + `terminal_catalog.py` Route Model bullets.
  Verification metadata pinned until closeout stamps the L5 commit.
- 2026-06-30T00:00:00+02:00 — L5 (Sidebar chat) route impact: `app.py` gained the leaf→chat registry routes — the
  opener now takes a `leafKey`, claims the leaf via `_claim_leaf_or_409` (`409 leaf-taken`, running-only),
  persists + echoes it, and a new `POST /api/terminal/{session}/attach-leaf` claims a leaf for an existing
  session (`404` unknown/terminated). `terminal_catalog.py` gained `TerminalCatalogEntry.leaf_key`
  (migration-safe `to_json`), `with_leaf_key`, and `active_for_leaf` (running-only single-owner lookup).
  Updated the `app.py` + `terminal_catalog.py` Route Model bullets. Verification metadata pinned until
  closeout stamps the L5 commit.
- 2026-06-29T23:00+02:00 — operations-integration L4a route impact: `changeset.py`'s `task` + `file-diff`
  routes gained a `leaf` + `mode` selector (precedence `leaf > master > scope`) for the doc-reader leaf
  views — `committed` (`base → code_commit`) / `working` (`HEAD → worktree`), resolved by leaf-id off the
  persisted enclosure contract (works with no live worktree), with selector validation (400/404). Updated
  the `changeset.py` Route Model bullet. Verification metadata pinned until closeout stamps the L4a commit.
- 2026-06-29T17:00+02:00 — operations-integration L4 follow-up route impact: `changeset.py`'s `master`
  endpoint is now the **NET** series diff (`git diff <master-base> <series-tip>` for code + memory, per-file
  inspectable) rather than the sum-of-leaves, and `/api/changeset/file-diff` gained an optional `master`
  param (the series net file-diff). Updated the `changeset.py` Route Model bullet. Verification metadata
  pinned until closeout stamps the L4 follow-up commit.
- 2026-06-29T15:30+02:00 — operations-integration L3 route impact: added `scope.py` (the shared browse-scope layer extracted from `files.py` — `FileScope`/`resolve_scope`/`run_scoped`/`language_for`/active-enclosure enumeration) and `changeset.py` (the read-only `GET /api/changeset/{task,file-diff,master}` change-set API: per-task `base → current` code+memory counts + status + `hasSidecar`, BEFORE/AFTER file content for the L4 MergeView, and master accumulation) to the Route Model, both registered before the static mount; `files.py` now shares `scope.py`. Verification metadata pinned to the task base until closeout stamps the L3 code commit.
- 2026-06-28T22:41+02:00 — operations-integration L1 route impact: added `files.py` (the read-only `GET /api/files/{repos,list,read,onboarding}` files API) to the Route Model — the first serving module to bridge to the kernel `CoordinationContext`, registered before the static mount. Verification metadata pinned until closeout stamps the L1 code commit.
- 2026-06-28T13:54+02:00 — Task 34 route impact: the raw `/api/events` channel (`events.py`) now does
  **one** retained-backlog scan per connect, streams that bounded backlog in **chunks** instead of
  materializing the whole history, **filters `lifecycle.heartbeat`** out of the river, and prunes expired
  logs on a slow cadence. Updated the `events.py` Route Model bullet, the Hot Path Summary, and the
  two-resume-models invariant. Verification metadata pinned until closeout stamps the task-34 code commit.
- 2026-06-28T07:45+02:00 — Task 33 route impact: `delta.py` now emits an `activeWorktreeGroups` whole-value
  delta (wrapped `{"activeWorktreeGroups": [...]}`) when the set changes. Verification metadata pinned
  until closeout stamps the code commit.
- 2026-06-28T07:43+02:00 — Task 29 S7 route impact: raw `/api/events` now emits a one-shot `ready`
  event after retained backlog replay, and `/api/actions/dismiss` accepts targetless actionable-drift
  acknowledgements while keeping provider/gate dismissals scoped. Verification metadata pinned until
  closeout stamps the task-29 code commit.
- 2026-06-28T06:08+02:00 — Task 29 route impact: the raw `GET /api/events` channel now applies
  lifecycle-aware backend retention on fresh connections through `observer.event_retention`.
  Terminal lifecycle logs are pruned after the grace window, workspace/lifecycle-less rows are
  age-bounded, active lifecycle histories remain uncapped, and valid `Last-Event-ID` cursors retain
  exact byte-offset resume. Verification metadata pinned until closeout stamps the task-29 code
  commit.
- 2026-06-28T03:21+02:00 — Task 31 route impact: live `create_app` installs a `ProviderStateRefresher`
  into `Projector` so each projection tick can refresh provider current-state before diffing and serving
  the snapshot; sim mode disables that refresher and continues to replay fixture provider state. Detail
  lives in the `app.py`, `projector.py`, and serving-test sidecars. Verification metadata pinned until
  closeout stamps the task-31 code commit.
- 2026-06-27T18:43+02:00 — No route impact: terminal.py added stdin=subprocess.DEVNULL on its 3 tmux subprocess.run sites (#49 stdio-pipe guard) — behavior-preserving hygiene; no change to serving architecture or surfaces.
- 2026-06-27T02:28+02:00 — Task 22 follow-up: the terminal opener now uses
  `TerminalHost.ensure` to create a detached tmux session instead of opening and closing a starter PTY
  client. This fixes new chats immediately becoming `exited` while preserving per-tab attach.
- 2026-06-27T01:25+02:00 — Task 22 follow-up: terminal WebSockets now attach independent
  `TerminalHost.attach` clients to the same durable tmux session, and the opener detaches its starter
  client after catalog persistence. This fixes multi-tab sharing without competing reads on one PTY fd.
- 2026-06-27T00:45+02:00 — Task 22 follow-up: WebSocket disconnect now detaches the local PTY client
  without ending the durable tmux/catalog row, fixing blank terminal rehydrate after browser refresh.
- 2026-06-27T00:25+02:00 — Task 22 follow-up: terminal catalog termination is now sticky against later
  WebSocket/PTY exit bookkeeping, so the `End` button cannot leave a row visible after refresh.
- 2026-06-26T23:05+02:00 — Task 22: added `terminal_catalog.py` and documented the durable terminal
  session flow across serving: opener persistence, `/api/terminal/sessions`, WebSocket rehydrate with
  tmux probe, explicit terminate, and catalog-backed image upload after restart. Verification metadata
  pinned until closeout stamps the task-22 code commit.
- 2026-06-25T14:02+02:00 — Task 24 reopened: serving actions now support gate-id-only cancel for stale workspace gates while keeping approve/reject/revision lifecycle-targeted.
- 2026-06-25T13:20+02:00 — Task 23/24: serving route now includes the operator-inbox dismiss endpoint used to delete stale pickup warnings.
- 2026-06-25T07:26+02:00 — Task 19: `/api/actions/{approve,reject}` now accepts targeted `gateId` and
  optional `note`, rejects blank No/reject reasons, maps stale targeted gate ids to `409 stale-gate`,
  and leaves `/api/operator-inbox` as the message-only Chat path. Verification metadata pinned until
  closeout stamps the code commit.
- 2026-06-23T15:05+02:00 — Task 10 dashboard fallback: documented `POST /api/operator-inbox` as the serving-layer write side for external-chat responses, routing to `operator_inbox_post_payload` with developer/dashboard attribution when the frontend has no hosted session to inject into. Verification metadata pinned until closeout stamps the task-10 code commit.
- 2026-06-19T20:30 — Task 6 slice 6f: `app.py` gained `POST /api/terminal/{session}/image` (save a validated screenshot under `<cwd>/.dashboard-pastes/` for path-injection) and now opens harnesses `suspend_unsafe`; `terminal.py`'s `write` strips Ctrl-Z (`0x1a`) for suspend-unsafe (bare-pane harness) sessions only — a shell keeps job control. Updated the `app.py`/`terminal.py` Route Model bullets. Verification metadata pinned until closeout stamps the 6f code commit.
- 2026-06-19T14:05+02:00 — Task 6 slice 6e-4: `terminal.py`'s `_spawn_pty` now gives the child a controlling terminal via `os.login_tty` (`preexec_fn`, setsid + `TIOCSCTTY`) + a seeded default winsize, so tmux honors browser resizes instead of staying at 80×24; the explicit `stdin/stdout/stderr=slave` keeps the child off the MCP stdio pipe (GitHub #49). Updated the `terminal.py` Route Model bullet. Verification metadata pinned until closeout stamps the 6e-4 code commit.
- 2026-06-18T21:27+02:00 — Task 6 slice 6e-2b: added `harnesses.py` (the curated harness launch registry — Claude Code/Codex/Pi.dev + `shutil.which` detection) to the Route Model; `app.py` gained `GET /api/harnesses` (`detect_harnesses()`) and a `kind="harness"` opener branch (`resolve_terminal_launch` resolves the registry argv; absent/unknown/not-installed ⇒ 400). Updated Purpose + the `app.py` Route Model bullet. Verification metadata pinned until closeout stamps the 6e-2b code commit.
- 2026-06-18T17:40+02:00 — Task 6 slice 6e-2a: `app.py` gained the `POST /api/terminal/{session}` **opener** — the dashboard spawns + owns a session (`TerminalOpenRequest` `kind` → the pure `resolve_terminal_launch` → `host.open(cwd=config.workspace_root, command=[$SHELL])`; server-resolved command, unknown kind ⇒ 400), so the WebSocket has a real session to attach to. Updated the `app.py` Route Model bullet. Verification metadata pinned until closeout stamps the 6e-2a code commit.
- 2026-06-18T16:10+02:00 — Task 6 slice 6d-2: `app.py` gained the `@app.websocket("/api/terminal/{session}")` Mode B2 bridge (attach to the `TerminalHost` or `close(4404)`; PTY output via `loop.add_reader` → binary frames; JSON `stdin`/`resize` in via the pure `_apply_terminal_input`; `{type:exit}` on child exit; tmux-persistent on disconnect) + the module-level bridge helpers + the `terminal_host` `create_app` param; `pyproject.toml` added the `websockets` core dep. Updated the `app.py`/`terminal.py` Route Model bullets + Hot Path + Purpose. Verification metadata pinned until closeout stamps the 6d-2 code commit.
- 2026-06-18T15:40+02:00 — Task 6 slice 6d-1: added `terminal.py` (the Mode B2 terminal host — `TerminalHost` over tmux-wrapped stdlib-`pty` sessions, injectable spawn, fixed-argv/localhost posture) to the Route Model + Invariants; the WebSocket bridge + `websockets` dep are 6d-2, the xterm.js viewport 6e. Also corrected the stale "(inert) POST action return-channel" wording in Purpose (6b made gate decisions binding). Verification metadata pinned until closeout stamps the 6d-1 code commit.
- 2026-06-18T12:10+02:00 — Task 6 slice 6b: the POST action plane became enforcing-adjacent — `actions.py`'s `evaluate_action` emits a `GateDecisionIntent` for gate-decision verbs and `app.py` records it as a developer/dashboard-attributed decision (`gate_decide_for_lifecycle`); lifecycle transitions stay the 4b no-mutation skeleton. Verification metadata pinned until closeout stamps the 6b code commit.
- 2026-06-14T23:30+02:00 — Slice 05 (5c): `sim.py`'s `build_sim` materializes the fixture's structural surfaces into the sim root (`_materialize_surfaces`); `events.py` single-encodes the raw channel (`stream_raw_events` emits `json.loads(line)`, matching `/api/stream`; was double-encoded). Verification metadata pinned until closeout stamps the 5c code commit.
- 2026-06-14T11:30+02:00 — Updated for slice 04 commit 4b: added `events.py` (raw `event`
  channel + byte-offset resume), `sim.py` (replay clock + feeder over the projector seams), and
  `actions.py` (the POST action skeleton) to the Route Model; `app.py` now carries
  `GET /api/events` + `POST /api/actions/{action}` and `projector.py` the `now`/`before_tick`
  seams. Verification metadata pinned until closeout stamps the 4b code commit.
- 2026-06-14T11:30+02:00 — Created for slice 04 commit 4a: the dashboard serving spine
  (`app.py`, `projector.py`, `delta.py`, `static.py`) over the observer read side — one
  shared projector, snapshot + per-entity SSE deltas, the static mount, localhost posture.
  The raw `event` channel, sim mode, and the POST action skeleton land in 4b. Verification
  metadata pinned until closeout stamps the 4a code commit.
