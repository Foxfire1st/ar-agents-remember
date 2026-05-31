# mcp/src/agents_remember/providers/cgc/lifecycle/refresh.py

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember-md                         |
| path                   | `mcp/src/agents_remember/providers/cgc/lifecycle/refresh.py` |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-05-31T12:50+02:00|
| lastVerifiedCommitHash | `c20a3292e667d227a3be0c1fb276f8a701df814f` |
| lastVerifiedCommitDate | 2026-05-31T14:17:11+02:00|
| governingOverview      | `overview.md`                              |

## Governing Overview

[CGC Lifecycle Overview](overview.md)

## Purpose

`refresh.py` owns CodeGraphContext index refresh lifecycle for one configured
root or every settings-backed root.

## Code Commentary

### Logic

The module builds Dockerized `cgc index <repo> --force` commands (with `<repo>`
rendered as the driveless container path `container_code_repo_root` so it is
valid inside the Linux runner on Windows hosts), returns
dry-run refresh payloads, starts the managed backend when required, runs CGC
doctor before live refreshes, records refresh state, and aggregates all-root
refresh results. The `cgc index --force` commands run with `UNLIMITED_TIMEOUT`
(from `lifecycle.command_runner`) so a long index pass is never killed by a
wall-clock cap.

### Invariants And Boundaries

- Refresh requires a healthy CGC install and backend when settings-backed roots
  use managed backend mode.
- All-root result aggregation is reused from `process_control.py`.
- Bounded `cgc run` and visualizer behavior live in `query.py`.
- Refresh execution must use the Docker runner image, not a host `cgc`
  executable.
- Index refresh must stay uncapped (`UNLIMITED_TIMEOUT`); do not reintroduce a
  wall-clock timeout on the `cgc index` commands.
- Layout parameters are typed as `CgcRuntimeLayout` (imported from
  `lifecycle.core`, which re-exports it from
  `agents_remember.providers.context`), not bare `Any`.

## Repo-Internal References

| Finding | Source Path |
| --- | --- |
| Backend startup is delegated to the CGC backend lifecycle module. | [backend.py](agents-remember-md/mcp/src/agents_remember/providers/cgc/lifecycle/backend.py) |
| All-root aggregation helpers are shared with process control. | [process_control.py](agents-remember-md/mcp/src/agents_remember/providers/cgc/lifecycle/process_control.py) |
| Docker command construction is provided by the runner module. | [runner.py](agents-remember-md/mcp/src/agents_remember/providers/cgc/lifecycle/runner.py) |

## Update History

- 2026-05-31T12:50+02:00 — Re-typed the `layout` param of `cgc_refresh_command`, `cgc_refresh_dry_result`, `cgc_refresh_backend`, `cgc_write_refresh_state`, and `cgc_refresh_preflight` from bare `Any` to `CgcRuntimeLayout` (newly imported from `lifecycle.core`); behavior-preserving, added a layout-type note to Invariants And Boundaries (1.0.0 review remediation).
- 2026-05-30T21:33+02:00: Documented that `cgc index --force` refresh commands now run with `UNLIMITED_TIMEOUT` (never-cap-indexing run); added the uncapped-index invariant. Verified against `825a172`.
- 2026-05-29T18:35+02:00: `cgc_refresh_preflight` `command` parameter typed `dict[str, Any]` (the compose plan it forwards); behavior-preserving (commit `0549b28`).
- 2026-05-29T07:19+02:00: Updated after the `cgc index` repo argument switched to the driveless container path (`container_code_repo_root`) for Windows-host support.
- 2026-05-26T12:51+02:00: Updated after CGC refresh moved into the Docker runner.
- 2026-05-25T21:14+02:00: Split from `process.py` so refresh orchestration is separate from watcher process control and bounded queries.
