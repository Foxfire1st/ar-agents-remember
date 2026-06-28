# mcp/src/agents_remember/cli/dashboard.py

| Field                  | Value                                        |
| ---------------------- | -------------------------------------------- |
| repository             | agents-remember                              |
| path                   | `mcp/src/agents_remember/cli/dashboard.py`   |
| doc_type               | `file-level-onboarding`                      |
| lastUpdated            | 2026-06-27T18:43+02:00                       |
| lastVerifiedCommitHash | `84e95ad0379cd864af3cbae21b7ffe3fd2d2b1b1`   |
| lastVerifiedCommitDate | 2026-06-28T18:49:06+02:00|
| governingOverview      | `../../../../overview.md`                     |

## Governing Overview

[overview.md](../../../../overview.md)

## Purpose

`cli/dashboard.py` is the `agents-remember dashboard` subcommand adapter: it parses the serving
flags and launches the FastAPI app under uvicorn. It mirrors the MCP server's `--config` contract
so the dashboard resolves the identical coordination context, wires sim replay via
`--sim` / `--sim-speed` (4b), and offers dev hot-reload via `--reload` (task 26).

## Code Commentary

`add_arguments(parser)` registers `--config` (required, absolute MCP settings JSON), `--host`
(default `127.0.0.1`), `--port` (default `8765`), `--interval` (default `1.0s`), `--reload` (a
`store_true` dev hot-reload flag, live state only), and the 4b sim flags `--sim` (a fixture dir
with `logs/observer/...`, default `None`) and `--sim-speed` (default `"1"`; a multiplier or
`"paused"`).

`run(args)` calls `load_config(args.config)` (printing the error and returning `1` on
`ConfigError`), then dispatches in priority order:

- **reload** (`--reload` set): rejects `--sim` (`error: --reload is not supported with --sim`,
  return `1`). Otherwise it sets `AR_DASHBOARD_DEV_CONFIG` (the resolved absolute `--config` path)
  and `AR_DASHBOARD_DEV_INTERVAL` env vars, then calls
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
- **Sim never mutates the fixture** — `build_sim` runs against a throwaway temp root; the
  frontend cannot tell sim from live.
- **`--reload` is live-state only** — it is mutually exclusive with `--sim` (rejected with exit
  `1`), and it must hand uvicorn the `_dev_app` import-string factory (`factory=True`), never a
  built app object, or hot-reload silently no-ops.

## Repo-Internal References

| Finding | Source Path |
| --- | --- |
| The umbrella dispatcher that registers this subcommand. | [__main__.py](agents-remember/mcp/src/agents_remember/cli/__main__.py) |
| The app factory it serves (and the `now`/`before_tick` seams it passes). | [serving/app.py](agents-remember/mcp/src/agents_remember/serving/app.py) |
| The sim builder / clock / feeder / speed parser it wires. | [serving/sim.py](agents-remember/mcp/src/agents_remember/serving/sim.py) |
| The `--config` → `McpRuntimeConfig` contract it mirrors. | [mcp/config.py](agents-remember/mcp/src/agents_remember/mcp/config.py) |
| Tests covering the serving CLI (including the `--reload` path). | [tests/test_serving.py](agents-remember/mcp/tests/test_serving.py) |

## Update History

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
