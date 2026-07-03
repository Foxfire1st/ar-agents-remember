# mcp/src/agents_remember/cli/dashboard.py

| Field                  | Value                                        |
| ---------------------- | -------------------------------------------- |
| repository             | agents-remember                              |
| path                   | `mcp/src/agents_remember/cli/dashboard.py`   |
| doc_type               | `file-level-onboarding`                      |
| lastUpdated            | 2026-07-03T11:45+02:00                       |
| lastVerifiedCommitHash | `38c56316207997da98d8408e1a3ada3c7525f4c6`   |
| lastVerifiedCommitDate | 2026-07-03T11:47:48+02:00|
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
flag wins), `--interval` (default `1.0s`), `--reload` (a `store_true` dev hot-reload flag, live
state only), the 4b sim flags `--sim` (a fixture dir with `logs/observer/...`, default `None`)
and `--sim-speed` (default `"1"`; a multiplier or `"paused"`), a mutually exclusive daemon
control group `--daemon` / `--status` / `--stop` (260703 L2), and `--no-access-log` (serve
without per-request access logs; the daemon child uses it to keep its log bounded — both
foreground `uvicorn.run` call sites pass `access_log=not args.no_access_log`).

`run(args)` first resolves `config_path = args.config or discover_config()` (an explicit flag
always wins; `ConfigDiscoveryError` prints and returns `1`), then calls `load_config(config_path)`
(printing the error and returning `1` on `ConfigError`), resolves the effective `port`, routes any
daemon control flag to `_run_daemon_command(args, config, port)` — `--status` prints the probed
state (exit 0 running / 1 not), `--stop` prints the stop outcome, `--daemon` runs
`serving_daemon.ensure(config, host, port, interval=args.interval)` and exits 0 only for
`adopted`/`started`/`restarted`; all three reject `--sim`/`--reload` combos — then dispatches in
priority order:

- **reload** (`--reload` set): rejects `--sim` (`error: --reload is not supported with --sim`,
  return `1`). Otherwise it sets `AR_DASHBOARD_DEV_CONFIG` (the resolved absolute settings path —
  discovered or explicit) and `AR_DASHBOARD_DEV_INTERVAL` env vars, then calls
  `uvicorn.run("agents_remember.cli.dashboard:_dev_app", factory=True, reload=True,
  reload_dirs=[<package source dir>], host=..., port=...)` and returns `0`.
- **sim** (`--sim` set): `build_sim(config, Path(args.sim), speed=parse_sim_speed(args.sim_speed))`
  (printing and returning `1` on `SimError` — bad speed or empty fixture), then
  `create_app(sim.config, interval=..., now=sim.clock.now, before_tick=sim.feeder.feed)`. The
  `sim` setup stays referenced until `run` returns, so its throwaway temp coordination root lives
  for the whole server lifetime.
- **live** (default): builds the app via `serving.app.create_app(config, interval=...)` and serves
  with `uvicorn.run(app, host=..., port=...)`.

`_dev_app()` is the zero-arg import-string app **factory** for the reload path: uvicorn's reloader
re-imports the app per worker restart, so it needs a factory, not a pre-built app object (passing
an object silently disables reload). The factory re-reads the resolved config from
`AR_DASHBOARD_DEV_CONFIG` (`load_config(...)`) and the interval from `AR_DASHBOARD_DEV_INTERVAL`
(default `1.0`) — the env vars the parent `run` set — and returns `create_app(config,
interval=...)`. It is live-state only; it never builds a sim. `reload_dirs` watches only the
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
  built app object, or hot-reload silently no-ops.

## Repo-Internal References

| Finding | Source Path |
| --- | --- |
| The umbrella dispatcher that registers this subcommand. | [__main__.py](agents-remember/mcp/src/agents_remember/cli/__main__.py) |
| The trusted-settings discovery the optional `--config` falls back to. | [discovery.py](agents-remember/mcp/src/agents_remember/cli/discovery.py) |
| The daemon supervisor behind `--daemon`/`--status`/`--stop`. | [serving/daemon.py](agents-remember/mcp/src/agents_remember/serving/daemon.py) |
| Daemon CLI dispatch tests (status/stop/port precedence/failure exits/sim rejection). | [test_dashboard_daemon.py](agents-remember/mcp/tests/test_dashboard_daemon.py) |
| Discovery unit tests (hits, precedence, template skip, miss error). | [test_cli_discovery.py](agents-remember/mcp/tests/test_cli_discovery.py) |
| The app factory it serves (and the `now`/`before_tick` seams it passes). | [serving/app.py](agents-remember/mcp/src/agents_remember/serving/app.py) |
| The sim builder / clock / feeder / speed parser it wires. | [serving/sim.py](agents-remember/mcp/src/agents_remember/serving/sim.py) |
| The `--config` → `McpRuntimeConfig` contract it mirrors. | [mcp/config.py](agents-remember/mcp/src/agents_remember/mcp/config.py) |
| Tests covering the serving CLI (including the `--reload` path). | [tests/test_serving.py](agents-remember/mcp/tests/test_serving.py) |

## Update History

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
