# mcp/src/agents_remember/cli/dashboard.py

## Governing Overview

[MCP overview](../../../overview.md)

## Purpose

The command-line entry of the dashboard server and its composition root. `run` resolves the settings,
declares the process role and serves the app in the foreground, under the reloader, from a recorded
fixture, or as a background daemon. `serving_collaborators` binds the application's callables to the
ports of the serving package, which may not import the application itself.

## Code Commentary

### Composition (`serving_collaborators`)

Every `create_app` call of this module goes through `serving_collaborators(config)`. It returns the
execution-evidence registrars of `EXECUTION_REGISTRATION_COLLABORATORS` together with:

- `capsule_launch`: `compile_launch_capsule` bound to the configuration;
- `knowledge_review`: `read_complete_knowledge_review`, which resolves the candidate once for the records
  and the composition;
- `knowledge_review_entries`: `list_knowledge_review_entries`;
- `review_source_content`: `read_review_source_content`;
- `review_intent_summary`: `read_review_intent_summary`;
- `review_trees`: `read_review_trees`, called with `processes=worklist_processes`;
- `review_trees_shutdown`: `worklist_processes.shutdown`;
- `knowledge_reader`: `read_knowledge_reader`.

`worklist_processes` is one `ReviewerWorklistProcesses` object created per call of
`serving_collaborators`, that is, one per composed app. It is the owner of the child processes that
compute the reviewer's leaf-wide worklist. The tree port passes it to every read, and the app's lifespan
calls its `shutdown` when serving ends, so the children of one dashboard are bounded and stopped by that
dashboard. The application imports are made inside the function.

### Serving modes (`run`)

- `run` calls `declare_process_role("dashboard")` first, then loads the settings (`--config`, or
  discovery from the working directory). The port is `--port` or the settings' `dashboard.port`.
- `--daemon`, `--status` and `--stop` go to `_run_daemon_command`, which probes, stops or ensures the
  background daemon recorded under the coordination root. They are refused together with `--sim` or
  `--reload`.
- `--reload` goes to `_run_reload_server`. uvicorn's reloader needs an import-string factory, so the
  resolved configuration path, interval and heartbeat are passed through the environment variables
  `AR_DASHBOARD_DEV_CONFIG`, `AR_DASHBOARD_DEV_INTERVAL` and `AR_DASHBOARD_DEV_HEARTBEAT`, and `_dev_app`
  builds the app in the worker. `_dev_app` declares the process role itself, because the reload worker
  is a spawned process that never runs `run`. `--reload` is refused with `--sim`.
- Otherwise `_build_app` builds a live app, or with `--sim` an app that replays a recorded fixture
  through a replay clock and feeder; the fixture's temporary root is kept until the server stops and is
  then cleaned up.
- Every server is started with `timeout_graceful_shutdown=DASHBOARD_GRACEFUL_SHUTDOWN_SECONDS` (3). The
  bound makes a termination signal close the endless event streams and run the lifespan shutdown instead
  of waiting for them.

### Arguments

`add_arguments` declares `--config`, `--host` (default `127.0.0.1`), `--port`, `--interval` (default 1.0),
`--heartbeat`, `--reload`, `--sim`, `--sim-speed`, the mutually exclusive `--daemon`, `--status` and
`--stop`, and `--no-access-log`.

### Role Runtime and Scope

serving_collaborators retains MIK reviewer/knowledge ports and adds extra_api_routes=partial(register_role_launch_routes, config=config). Ordinary and reload factories bind existing worktree services before composition. The serving app registers the injected launch routes before static mount; the reviewer resolution owner is unchanged. Local app variables only flatten the existing create_app return expressions.

## Evidence

- The bounded graceful shutdown and the registrar collaborators. [32]
- The composition: one worklist process owner per app, the ports, and the owner's shutdown. [33]
- The reload worker's factory declares the process role and composes the same collaborators. [34]
- The command-line arguments. [25]
- The entry: role, settings, daemon commands, reload, foreground, and the fixture's cleanup. [26]
- The reload server passes its configuration through the environment. [27]
- The live app and the replayed fixture are both composed through serving_collaborators. [28]
- The daemon commands. [29]
- The process owner that the composition creates. [30]
- The dashboard's tree port resolves once and computes the leaf-wide view once per comparison. [31]

### Runtime Source References

- Frozen implementation of serving_collaborators supporting the stated file behavior. [22]
- Frozen implementation of _dev_app supporting the stated file behavior. [23]
- Frozen implementation of run supporting the stated file behavior. [24]
