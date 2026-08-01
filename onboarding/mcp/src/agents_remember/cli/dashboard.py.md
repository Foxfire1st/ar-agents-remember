# mcp/src/agents_remember/cli/dashboard.py

| Field                  | Value                                        |
| ---------------------- | -------------------------------------------- |
| repository             | agents-remember                              |
| path                   | `mcp/src/agents_remember/cli/dashboard.py`   |
| doc_type               | `file-level-onboarding`                      |
| lastUpdated            | 2026-07-31T22:05+02:00                       |
| lastVerifiedCommitHash | `e52edaf5b655f495580efd93306afdf922b19b51`   |
| lastVerifiedCommitDate | 2026-08-01T11:01:51+02:00|
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

`run(args)` first calls `_resolve_settings(args)` (260731-EFA-L2), which resolves
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

| Finding | Source Path |
| --- | --- |
| The umbrella dispatcher that registers this subcommand. | [__main__.py](agents-remember/mcp/src/agents_remember/cli/__main__.py) |
| The trusted-settings discovery the optional `--config` falls back to. | [discovery.py](agents-remember/mcp/src/agents_remember/cli/discovery.py) |
| The daemon supervisor behind `--daemon`/`--status`/`--stop` (heartbeat plumbed on spawn/restart only). | [serving/daemon.py](agents-remember/mcp/src/agents_remember/serving/daemon.py) |
| The heartbeat default (`DEFAULT_HEARTBEAT_SECONDS`) and the change-driven pacing (`ChangePacer`) that `--interval`/`--heartbeat` configure (260712-PTS-L3). | [serving/change_watcher.py](agents-remember/mcp/src/agents_remember/serving/change_watcher.py) |
| Daemon CLI dispatch tests (status/stop/port precedence/failure exits/sim rejection). | [test_dashboard_daemon.py](agents-remember/mcp/tests/test_dashboard_daemon.py) |
| Discovery unit tests (hits, precedence, template skip, miss error). | [test_cli_discovery.py](agents-remember/mcp/tests/test_cli_discovery.py) |
| The app factory it serves (and the `now`/`before_tick` seams it passes). | [serving/app.py](agents-remember/mcp/src/agents_remember/serving/app.py) |
| The sim builder / clock / feeder / speed parser it wires. | [serving/sim.py](agents-remember/mcp/src/agents_remember/serving/sim.py) |
| The `--config` → `McpRuntimeConfig` contract it mirrors. | [mcp/config.py](agents-remember/mcp/src/agents_remember/mcp/config.py) |
| Tests covering the serving CLI (including the `--reload` path). | [tests/test_serving.py](agents-remember/mcp/tests/test_serving.py) |

## 260718-CHATS-L5I Current Delta

Dashboard shutdown now uses a bounded three-second Uvicorn graceful window. This explicitly terminates intentionally endless SSE responses so lifespan cleanup can cancel projector, landing, and supervisor tasks instead of leaving a process alive after SIGTERM.

This entry supersedes any earlier description in this sidecar that conflicts with the current source behavior above; verification metadata stays pinned to the pre-commit source history until closeout.

## Update History

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
