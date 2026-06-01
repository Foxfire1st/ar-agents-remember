# mcp/src/agents_remember/providers/cgc/lifecycle/query.py

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember-md                         |
| path                   | `mcp/src/agents_remember/providers/cgc/lifecycle/query.py` |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-06-01T23:40+02:00                     |
| lastVerifiedCommitHash | `8833b31a37deda0d9d2e6895659ab0fe085a8ee9` |
| lastVerifiedCommitDate | 2026-06-01T23:39:39+02:00|
| governingOverview      | `overview.md`                              |

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

## Repo-Internal References

| Finding | Source Path |
| --- | --- |
| CGC status checks are provided by the installation module. | [installation.py](agents-remember-md/mcp/src/agents_remember/providers/cgc/lifecycle/installation.py) |
| `cgc_backend_status` (backend-only readiness) is provided by the backend module. | [backend.py](agents-remember-md/mcp/src/agents_remember/providers/cgc/lifecycle/backend.py) |
| Docker command construction is provided by the runner module. | [runner.py](agents-remember-md/mcp/src/agents_remember/providers/cgc/lifecycle/runner.py) |
| Provider lifecycle tests cover visualizer rejection, dry-run visualize command construction, and bounded `cgc run`; the `cgc run` test now stubs `cgc_backend_status`. | [test_provider_lifecycle.py](agents-remember-md/mcp/tests/test_provider_lifecycle.py) |

## Update History

- 2026-06-01T23:40+02:00 — `cgc_run_status_result` now gates on `cgc_backend_status` (FalkorDB backend only) instead of `cgc_status` (full provider including watcher). Fixes OQ7-caused seed failure: worktree watchers start last, so gating `bundle import` on the watcher caused the import to never run and the seed to fall back to a full re-index. The visualize path still uses `cgc_status`. Added `cgc_backend_status` import from `backend.py`. Updated Logic, Invariants, and Repo-Internal References.
- 2026-05-31T12:50+02:00 — `cgc_run_command`, `cgc_run_dry_result`, `cgc_visualize_command`, and `cgc_visualize_dry_result` now type their `layout` param as `CgcRuntimeLayout` (newly imported from `agents_remember.providers.context`) instead of `Any`; added an Invariants note recording the concrete layout type (1.0.0 review remediation).
- 2026-05-29T07:19+02:00: Updated after the visualizer `--repo` argument switched to the driveless container path (`container_code_repo_root`) for Windows-host support.
- 2026-05-26T12:51+02:00: Updated after bounded CGC run and visualizer commands moved into the Docker runner.
- 2026-05-25T21:14+02:00: Split from `process.py` so bounded query and visualizer behavior is separate from watcher process control and refresh.
