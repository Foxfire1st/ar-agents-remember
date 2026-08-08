# mcp/src/agents_remember/cli/dashboard.py

| Field                  | Value                                        |
| ---------------------- | -------------------------------------------- |
| repository             | agents-remember                              |
| path                   | `mcp/src/agents_remember/cli/dashboard.py`   |
| doc_type               | `file-level-onboarding`                      |
| lastUpdated            | 2026-08-04T03:03+02:00                       |
| lastVerifiedCommitHash | `1c1629fc97dd4daf352cf9b3529d210be167d2af`   |
| lastVerifiedCommitDate | 2026-08-08T22:29:45+02:00|
| governingOverview      | `../../../../overview.md`                     |

## Governing Overview

[overview.md](../../../../overview.md)

## Purpose

`cli/dashboard.py` is the `agents-remember dashboard` subcommand adapter: it parses the serving
flags and launches the FastAPI app under uvicorn. It mirrors the MCP server's `--config` contract
so the dashboard resolves the identical coordination context — and since 260703 L1 the flag is
**optional**: an omitted `--config` is discovered by `cli/discovery.py`'s upward walk, so the
command runs flag-free from anywhere under the workspace. It wires sim replay via
`--sim` / `--sim-speed` (4b), offers dev hot-reload via `--reload` (task 26), and since 260703 L2
fronts the daemon supervisor: `--daemon` / `--status` / `--stop` dispatch to `serving/daemon.py`
so the dashboard can outlive the terminal that started it.

## Code Commentary

`add_arguments(parser)` registers `--config` (default `None`; its help documents the discovery
fallback), `--host` (default `127.0.0.1`), `--port` (260703 L2: default `None` — resolved after
config load as `args.port or config.dashboard.port`, so the settings key governs and an explicit
flag wins), `--interval` (default `1.0s`; **re-documented by 260712-PTS-L3 as the fast-path
projection cadence floor** — change-driven re-projections are never spaced closer than this, a
continuously-busy world still projects once per interval, and it stays the fixed tick cadence
under `--sim` or when the change watcher is unavailable; also the `/api/events` raw-tail poll
cadence), `--heartbeat` (**260712-PTS-L3**, default `None` ⇒ the serving
`DEFAULT_HEARTBEAT_SECONDS` = 15s: the idle re-projection cadence — with no detected input change
the projection still refreshes at this cadence, the staleness bound for `/api/state` and for
time-derived fields such as `ageSeconds`/`staleSeconds` and stale/overdue flips), `--reload` (a
`store_true` dev hot-reload flag, live
state only), the 4b sim flags `--sim` (a fixture dir with `logs/observer/...`, default `None`)
and `--sim-speed` (default `"1"`; a multiplier or `"paused"`), a mutually exclusive daemon
control group `--daemon` / `--status` / `--stop` (260703 L2), and `--no-access-log` (serve
without per-request access logs; the daemon child uses it to keep its log bounded — both
foreground `uvicorn.run` call sites pass `access_log=not args.no_access_log`).

`run(args)` opens with `declare_process_role("dashboard")` (260731-EFA-L5, L148 — the first
statement in the function, before any settings work), then calls `_resolve_settings(args)`
(260731-EFA-L2), which resolves
`config_path = args.config or discover_config()` — an explicit flag always wins — and loads it,
printing the message and returning `None` for **either** `ConfigDiscoveryError` or `ConfigError`;
`run` turns that `None` into exit `1`. It then resolves the effective `port`, routes any
daemon control flag to `_run_daemon_command(args, config, port)` — `--status` prints the probed
state (exit 0 running / 1 not), `--stop` prints the stop outcome, `--daemon` runs
`serving_daemon.ensure(config, serving_daemon.DaemonEndpoint(host=args.host, port=port),
cadence=ProjectionCadence(interval=args.interval, heartbeat=args.heartbeat))` and
exits 0 only for `adopted`/`started`/`restarted` (heartbeat, like interval, reaches the child only
when ensure spawns/restarts — an adopted daemon keeps its cadences); all three reject
`--sim`/`--reload` combos — then dispatches in priority order:

- **reload** (`--reload` set): delegated to `_run_reload_server(args, config_path, port)`
  (260731-EFA-L2). It rejects `--sim` (`error: --reload is not supported with --sim`,
  return `1`). Otherwise it sets `AR_DASHBOARD_DEV_CONFIG` (the resolved absolute settings path —
  discovered or explicit) and `AR_DASHBOARD_DEV_INTERVAL` env vars — plus (260712-PTS-L3)
  `AR_DASHBOARD_DEV_HEARTBEAT` only when `--heartbeat` was explicit — then calls
  `uvicorn.run("agents_remember.cli.dashboard:_dev_app", factory=True, reload=True,
  reload_dirs=[<package source dir>], host=..., port=...)` and returns `0`.
- **sim or live**: both are built by `_build_app(args, config) -> _DashboardApp | None`
  (260731-EFA-L2) — "the app to serve: live state, or a replayed fixture; `None` when the fixture
  is unusable". With `--sim` it runs
  `build_sim(config, Path(args.sim), speed=parse_sim_speed(args.sim_speed))` (printing and
  returning `None` on `SimError` — bad speed or empty fixture), then
  `create_app(sim.config, cadence=ProjectionCadence(interval=args.interval),
  replay=ProjectionReplay(now=sim.clock.now, before_tick=sim.feeder.feed))` — no `heartbeat` and no
  watcher, so replay stays time-driven on the fixed `--interval`. Without `--sim` it is
  `create_app(config, cadence=ProjectionCadence(interval=args.interval, heartbeat=args.heartbeat))`
  (260712-PTS-L3 — live serving gets change-driven + heartbeat pacing). `run` then serves
  `built.app` with `uvicorn.run(...)`.

**`_DashboardApp(app, sim)`** (a `NamedTuple`) is why the sim survives the server: it carries the
`SimSetup` alongside the app rather than dropping it at build time, **because the sim owns the
throwaway coordination root the server is reading** — releasing it would reclaim the directory
under a running server. `run` keeps `built` referenced for the whole `uvicorn.run` call and, in a
`finally`, calls `built.sim.temp_dir.cleanup()` when there is a sim. Closing it there is what ends
the root's life: dropping the reference instead would leave the directory to
`TemporaryDirectory`'s finaliser, which is a ResourceWarning, not a cleanup.

`_dev_app()` is the zero-arg import-string app **factory** for the reload path: uvicorn's reloader
re-imports the app per worker restart, so it needs a factory, not a pre-built app object. Passing
an object does **not** silently disable reload — uvicorn refuses to start and exits `1` (pinned
citation in the `--reload` invariant below). The factory re-reads the resolved config from
`AR_DASHBOARD_DEV_CONFIG` (`load_config(...)`), the interval from `AR_DASHBOARD_DEV_INTERVAL`
(default `1.0`), and (260712-PTS-L3) the optional heartbeat from `AR_DASHBOARD_DEV_HEARTBEAT`
(absent/empty ⇒ `heartbeat=None`, the serving default) — the env vars the parent `run` set — and
returns `create_app(config, cadence=ProjectionCadence(interval=..., heartbeat=...))`. It is
live-state only; it never builds a sim. `reload_dirs` watches only the
package source dir (`Path(agents_remember.__file__).parent`) so unrelated trees don't churn the
reloader. `os`, `uvicorn`, `create_app`, and the sim helpers are imported at module top (the
established CLI convention); `import agents_remember` is local to the reload branch.

### 260731-EFA-L5: the durable-store process role (the whole change here)

This file's entire L5 change is seven lines — the `declare_process_role` import (L20) and a
five-line comment plus the call as the first statement of `run` (L143-L148; `def run` is L142). No
flag, no dispatch order, no exit code and no serving call moved.

`controlplane/durable_store.py` names two concurrent writers of the six control-plane JSONL logs,
`"mcp"` and `"dashboard"`; the declaration is what lets code shared by both processes — most
importantly `mcp/tools/gates.py::gate_decide_payload`, which `serving/app.py` calls **directly** —
ask which one it is in. It sits at the top of `run` rather than inside `create_app` for the same
reason the MCP server's sits in `main` rather than `create_server`: `create_app` is a factory the
test suite calls in-process, `durable_store._declared` is a module-level dict with no reset, and a
declaration made in the factory would stamp `"dashboard"` onto the interpreter and every later test
in it.

**Which serving processes this actually reaches, measured rather than assumed:**

| Path | Serves in | Declares `"dashboard"` |
| --- | --- | --- |
| foreground live / `--sim` | this process (`uvicorn.run(built.app, ...)`) | yes |
| `--daemon` | a child `sys.executable -m agents_remember.cli dashboard ...` (`serving/daemon.py` L201-L214), which re-enters `run` | yes |
| `--reload` | a **spawned** uvicorn worker, not this process | **no** |

The `--reload` row is a real gap, and it is worth stating precisely rather than rounding off.
`uvicorn.run(..., reload=True)` keeps only the reload supervisor in the process that called it and
serves from a child built by `multiprocessing.get_context("spawn")` (uvicorn 0.49.0,
`uvicorn/_subprocess.py` L18 + `uvicorn/supervisors/basereload.py` L84-L85). A spawn-context child
does not inherit the parent's module globals — measured directly: a parent that mutates a module
dict before `Process.start()` and a child that reports the same dict give `{'role': 'dashboard'}`
and `{}`. So under `agents-remember dashboard --reload`, the process that serves HTTP, decides
gates and writes these logs has declared no role at all, and `StoreOwnership.is_compaction_owner()`
answers `True` for every log (`role is None`). A dev-reload dashboard therefore *does* run the gate
reclaim pass that a normal dashboard skips.

That is an ownership-advisory gap, not a durability one, and the difference is the point of the
contract: the reclaim still holds the log's `flock` across its read **and** its rewrite like every
other writer, so no record is lost either way. What it falsifies is the contract's stated reason for
letting an undeclared process count as owner — "a CLI or test run is nobody's competitor"
(`durable_store.StoreOwnership.is_compaction_owner`) — because a `--reload` dashboard can be running
against the same coordination root as a live MCP server. Closing it means declaring the role inside
`_dev_app()` as well; nothing else about this file would change.

## Invariants And Boundaries

- **Localhost-only by default** (`--host 127.0.0.1`); the help text warns against exposing it.
- Resolves config through the same `load_config` the MCP server uses — no bespoke path handling.
- **Discovery only fills an omitted flag** — `args.config or discover_config()`; an explicit
  `--config` is never second-guessed, and discovery failures exit `1` with the both-patterns
  error rather than guessing.
- **Foreground behavior is unchanged by the daemon feature** — no control flag means the same
  serve-in-this-terminal flow as before (the `--reload` dev loop included); daemon logic lives in
  `serving/daemon.py`, this file only dispatches.
- **Sim never mutates the fixture** — `build_sim` runs against a throwaway temp root; the
  frontend cannot tell sim from live.
- **`--reload` is live-state only** — it is mutually exclusive with `--sim` (rejected with exit
  `1`), and it must hand uvicorn the `_dev_app` import-string factory (`factory=True`), never a
  built app object. Handing uvicorn a built object does **not** make hot-reload silently no-op —
  uvicorn **refuses to start, loudly**. Pinned: **uvicorn 0.49.0**, `uvicorn/main.py` lines
  **604-607** — `if (config.reload or config.workers > 1) and not isinstance(app, str):` logs the
  `uvicorn.error` warning `"You must pass the application as an import string to enable 'reload' or
  'workers'."` and calls `sys.exit(1)`. Measured: `uvicorn.run(<built app object>, reload=True)`
  under the repo `.venv` printed that warning and exited with code **1**, before binding the port.
  So a `factory=True` regression is a hard startup failure, not a silently degraded dev loop.

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The umbrella dispatcher that registers this subcommand. | `build_parser` | mcp/src/agents_remember/cli/__main__.py:16-28 |
| The trusted-settings discovery the optional `--config` falls back to. | `discover_config` | mcp/src/agents_remember/cli/discovery.py:36-50 |
| The daemon supervisor behind `--daemon`/`--status`/`--stop` (heartbeat plumbed on spawn/restart only). | `ensure` | mcp/src/agents_remember/serving/daemon.py:264-290 |
| The serving layer defines the idle heartbeat default and implements change-or-heartbeat scheduling in `ChangePacer`. | `DEFAULT_HEARTBEAT_SECONDS`; `ChangePacer` | mcp/src/agents_remember/serving/change_watcher.py:109-109; mcp/src/agents_remember/serving/change_watcher.py:283-376 |
| This CLI defines `--interval`/`--heartbeat` and threads their cadence through reload parent/worker, live-app, and daemon paths; sim deliberately carries interval only. | `add_arguments`; `_dev_app`; `_run_reload_server`; `_build_app`; `_run_daemon_command` | mcp/src/agents_remember/cli/dashboard.py:52-81; mcp/src/agents_remember/cli/dashboard.py:84-158; mcp/src/agents_remember/cli/dashboard.py:211-232; mcp/src/agents_remember/cli/dashboard.py:246-267; mcp/src/agents_remember/cli/dashboard.py:270-297 |
| Daemon CLI dispatch tests (status/stop/port precedence/failure exits/sim rejection). | `CliDaemonDispatchTests` | mcp/tests/test_dashboard_daemon.py:421-503 |
| Discovery unit tests (hits, precedence, template skip, miss error). | `DiscoverConfigTests` | mcp/tests/test_cli_discovery.py:42-142 |
| The app factory it serves (and the `now`/`before_tick` seams it passes). | `create_app` | mcp/src/agents_remember/serving/app.py:226-285 |
| The sim builder / clock / feeder / speed parser it wires. | `build_sim`; `parse_sim_speed` | mcp/src/agents_remember/serving/sim.py:51-61; mcp/src/agents_remember/serving/sim.py:137-148 |
| The `--config` → `McpRuntimeConfig` contract it mirrors. | `McpRuntimeConfig` | mcp/src/agents_remember/mcp/config.py:113-137 |
| Tests covering the serving CLI (including the `--reload` path). | `CliRunTests` | mcp/tests/test_serving_cli.py:211-310 |
| The durable-store contract whose process role `run` declares — what the role decides, and what the unconditional per-log lock decides instead. | `declare_process_role` | mcp/src/agents_remember/controlplane/durable_store.py:76-84 |
| The MCP server's mirror of the same declaration, in `main` rather than `create_server`. | `main` | mcp/src/agents_remember/mcp/server.py:35-57 |

## 260718-CHATS-L5I Current Delta

Dashboard shutdown now uses a bounded three-second Uvicorn graceful window. This explicitly terminates intentionally endless SSE responses so lifespan cleanup can cancel projector, landing, and agent-notifier tasks instead of leaving a process alive after SIGTERM.

This entry supersedes any earlier description in this sidecar that conflicts with the current source behavior above; verification metadata stays pinned to the pre-commit source history until closeout.

## Update History

- 2026-08-08T22:10+02:00 — 260713-TES-L1 completion round (curator): refreshed this sidecar body for the supervisor -> agent-notifier rename (module paths, identifiers, settings keys, wire keys, prose) and the compat seams; verification metadata pinned until closeout stamps the 260713-TES-L1 commit.
- 2026-08-04T03:26:26+02:00 — 260731-EFA-L6 S18-SR3-B06 curator: generated and source-inspected the cadence-owner range (1 repair, 0 normalisations, 0 declines); the locked immediate recheck was clean with frozen zero source/tokenize/parse/build telemetry.
- 2026-08-04T03:03:23+02:00 — 260731-EFA-L6 S18-SR3-B06 worker: replaced the
  underbound declaration/call fragments with the five complete CLI owners that define and consume
  cadence across reload parent/worker, live, sim, and daemon paths. The changed binding is a
  provisional `:1-1` input for the fresh Luna curator; no citation mechanics ran.
- 2026-08-04T02:20:03+02:00 — 260731-EFA-L6 S18-B06 curator delta: repaired the scoped citations against the frozen source snapshot; generated ranges were inspected and the managed index remained warm/frozen with zero source reads, tokenization, parsing, and build.

- 2026-08-04T01:24:49+02:00 — 260731-EFA-L6 S18-SR2-B06 worker: source-first separated
  `ChangePacer`/heartbeat-default ownership from this CLI's flag definitions and cadence wiring.
  Preserved both generated serving ranges and added one honest `:1-1` CLI binding covering reload,
  live, daemon, and the deliberate sim exception; no citation mechanics ran.
- 2026-08-04T00:28:23+02:00 — 260731-EFA-L6 S18-B06 curator: repaired the scoped dashboard CLI citation claims; final exact frozen-snapshot check is clean.
- 2026-08-02T16:55+02:00 — 260731-EFA-L6 W1-B08 curator: repaired 12 citation claims and preserved verification metadata.

- 2026-08-01T13:20+02:00 — 260731-EFA-L5 curator: this file's change is **small, and is recorded as
  small** — seven lines, one import and `declare_process_role("dashboard")` as the first
  statement of `run` cit:([`run`], mcp/src/agents_remember/cli/dashboard.py:161-196). Nothing else in the file moved. Recorded the placement rule (entry
  point, never `create_app`, because the factory is called in-process by tests and `_declared` has
  no reset) and, more usefully, **which serving processes the declaration actually reaches**:
  foreground live/sim yes; the `--daemon` child yes, because `serving/daemon.py` L201-L214 spawns
  `sys.executable -m agents_remember.cli dashboard ...` and that re-enters `run`; `--reload` **no**.
  The reload gap was verified, not inferred from the flag: uvicorn 0.49.0 serves the reload worker
  from a `multiprocessing.get_context("spawn")` child (`uvicorn/_subprocess.py` L18,
  `uvicorn/supervisors/basereload.py` L84-L85), and a spawn child does not inherit parent module
  globals — measured with a two-line harness (parent `{'role': 'dashboard'}`, child `{}`). Stated
  the consequence at its true weight: the dev-reload dashboard counts as compaction owner of every
  log and so runs the gate reclaim pass a normal dashboard skips, which is an ownership-advisory
  gap and **not** a durability one, because the reclaim holds the log's lock across read and rewrite
  regardless. Verification metadata pinned until closeout stamps the L5 code commit.
- 2026-07-31T22:05+02:00 — 260731-EFA-L4 curator: the previous claim that handing uvicorn a built
  app object instead of the `_dev_app` import-string factory makes hot-reload "silently no-op" was
  **false**. It appeared twice in this sidecar (the `_dev_app` commentary and the `--reload`
  invariant) and once as a source comment. uvicorn does not silently no-op — it refuses to start.
  Verified against **uvicorn 0.49.0**: `uvicorn/main.py:604-607` guards
  `if (config.reload or config.workers > 1) and not isinstance(app, str):`, logs the `uvicorn.error`
  warning "You must pass the application as an import string to enable 'reload' or 'workers'." and
  calls `sys.exit(1)`. Measured by running `uvicorn.run(<built app object>, host=..., port=...,
  reload=True)` under the repo `.venv`: the warning printed and the process exited with code **1**
  before binding the port. Both prose sites now carry that version-pinned citation, and the same
  false belief was corrected in the source comment at
  `mcp/src/agents_remember/cli/dashboard.py:27-33` (comment text only — no code, no argument and no
  `factory=True` change; the code was already correct, only its stated reason was wrong).
  Verification metadata unchanged.
- 2026-07-31T00:00+02:00 — 260731-EFA-L2 (gate honesty, `C901`/`PLR0912`/`PLR0915` armed with no
  exemptions): `run` was split into `_resolve_settings` (discover + load, one refusal path for
  `ConfigDiscoveryError` and `ConfigError`), `_run_reload_server` and `_build_app` (returning the
  new `_DashboardApp(app, sim)` NamedTuple, or `None` for an unusable fixture). The serving calls
  were re-signed onto the serving layer's new parameter objects — `create_app(config,
  cadence=ProjectionCadence(...), replay=ProjectionReplay(...))` and
  `serving_daemon.ensure(config, DaemonEndpoint(host, port), cadence=ProjectionCadence(...))`.
  `run` now also closes the sim's temp root explicitly in a `finally` instead of leaving it to the
  `TemporaryDirectory` finaliser. No flag, dispatch order or exit code changed. Verification
  metadata pinned until closeout stamps the L2 commit.
- 2026-07-24T13:18:47Z — 260718-CHATS-L5I curator: corrected the source-side behavior record for the current backend/shared delta and preserved the pre-commit verification stamp.

- 2026-07-12T20:24+02:00 — 260712-PTS-L3: added `--heartbeat` (default `None` ⇒ serving default
  15s — the idle re-projection cadence and the `/api/state`/time-derived-field staleness bound)
  and re-documented `--interval` as the fast-path projection cadence floor (unchanged fixed
  cadence under `--sim`/watcher-unavailable). Live `run` and `_dev_app` (via the new
  `AR_DASHBOARD_DEV_HEARTBEAT` env) pass heartbeat to `create_app`; the sim branch deliberately
  does not; `--daemon` forwards it to `serving_daemon.ensure` (reaches the child on spawn/restart
  only). Verification metadata pinned until closeout stamps the PTS-L3 commit.
- 2026-07-03T11:45+02:00 — 260703 L2: daemon mode — the mutually exclusive `--daemon`/`--status`/
  `--stop` group dispatches to `serving/daemon.py` after config resolution, `--port` defaults from
  the `dashboard.port` settings key (explicit flag wins), `--interval` is forwarded to the daemon
  child, and `--no-access-log` reaches both foreground `uvicorn.run` sites. Foreground behavior
  unchanged. Verification metadata pinned until closeout stamps the code commit.
- 2026-07-03T09:55+02:00 — 260703 L1: `--config` became optional — `run` resolves
  `args.config or discover_config()` (explicit flag wins; `ConfigDiscoveryError` → exit 1) and the
  reload env handoff uses the resolved path. Discovery semantics live in `cli/discovery.py`.
  Verification metadata pinned until closeout stamps the code commit.
- 2026-06-27T18:43+02:00 — Task 26: added dev hot-reload `--reload` (`store_true`, live-state
  only, rejects `--sim`). Documented the `_dev_app()` zero-arg import-string factory and the
  `AR_DASHBOARD_DEV_CONFIG` / `AR_DASHBOARD_DEV_INTERVAL` env handoff, plus the `run` reload branch
  (`uvicorn.run(..., factory=True, reload=True, reload_dirs=[package src])`).
- 2026-06-14T11:30+02:00 — Updated for slice 04 commit 4b: added the `--sim` / `--sim-speed`
  flags and the sim `run` branch (`build_sim` → `create_app` with the replay clock + feeder; the
  sim setup is held for the server lifetime; `SimError` → exit 1). Verification metadata pinned
  until closeout stamps the 4b code commit.
- 2026-06-14T11:30+02:00 — Created for slice 04 commit 4a: the `dashboard` subcommand adapter
  (config → create_app → uvicorn). Verification metadata pinned until closeout stamps the 4a code
  commit.
