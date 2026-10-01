# mcp/src/agents_remember/providers/cgc/lifecycle/query.py

## Governing Overview

[CGC Lifecycle Overview](overview.md)

## Purpose

`query.py` owns bounded native `cgc run` commands and explicit CGC visualizer
lifecycle commands.

## Code Commentary

### Logic

The module strips native args after `--`, rejects `visualize` through bounded
`run`, checks status before live commands, executes bounded native commands
inside the CGC Docker runner with captured output, builds Dockerized visualizer
server commands, validates ports, and runs visualizer foreground commands only
after durable namespace checks. The visualizer `--repo` argument is the layout's
driveless container path (`container_code_repo_root`), so it is valid inside the
Linux runner on Windows hosts.

`cgc_run_status_result` (the `cgc run` pre-flight) now gates on `cgc_backend_status` (FalkorDB running + data mount + network + ping) instead of `cgc_status` (which also requires the watcher container to be running). A one-shot `cgc run` — such as the seed's `bundle import` or a graph query — needs only the FalkorDB backend; gating on the full provider status blocked the seed because worktree watchers start last (OQ7), causing the import to never run and the seed to fall back to a full re-index. Queries issued with the worktree fully up are unaffected by this change. The visualize path (`cgc_visualize_status_result`) still gates on the full `cgc_status`.

### Invariants And Boundaries

- `cgc run` is only for bounded native commands and must reject visualizer
  server startup.
- `cgc visualize` is the explicit long-running server command and requires a
  durable process namespace.
- Watcher start/stop behavior lives in `process_control.py`.
- Query and visualizer execution must use the Docker runner image, not a host
  `cgc` executable.
- Command/dry-result helpers take a concrete `CgcRuntimeLayout` (imported from
  `agents_remember.providers.context`), not an untyped `Any` layout.
- `cgc_run_status_result` gates on `cgc_backend_status` (backend only); `cgc_visualize_status_result` gates on the full `cgc_status` (backend + watcher).

## Evidence

### Repo-Internal References

- CGC status checks are provided by the installation module. [1]
- `cgc_backend_status` (backend-only readiness) is provided by the backend module. [2]
- Docker command construction is provided by the runner module. [3]
