# mcp/src/agents_remember/providers/cgc/lifecycle/process_control.py

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember-md                         |
| path                   | `mcp/src/agents_remember/providers/cgc/lifecycle/process_control.py` |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-05-31T12:30+02:00|
| lastVerifiedCommitHash | `c20a3292e667d227a3be0c1fb276f8a701df814f` |
| lastVerifiedCommitDate | 2026-05-31T14:17:11+02:00|
| governingOverview      | `overview.md`                              |

## Governing Overview

[CGC Lifecycle Overview](overview.md)

## Purpose

`process_control.py` owns CodeGraphContext watcher container start/stop
lifecycle and all-root start/stop aggregation.

## Code Commentary

### Logic

The module builds dry-run Docker watcher commands, starts the managed FalkorDB
backend when settings-backed roots require it, starts `cgc watch` inside the
CGC runner image, records provider
state, removes watcher containers on stop, marks stopped state, and aggregates
start/stop results across configured roots. Watcher startup renders the Compose
override with backend host ports from the backend start result so repeated
settings-backed starts keep the same FalkorDB/browser port mappings.

### Invariants And Boundaries

- Long-running watcher start/stop operations require a durable process
  namespace even though Docker owns the actual watcher lifetime.
- Backend lifecycle is delegated to `backend.py`.
- Refresh and bounded query behavior live in sibling lifecycle modules.
- Host PIDs are not a managed CGC contract; watcher state is tracked by Docker
  container name.
- Watcher `up` should render dependency backend ports from the current start
  result when available.

## Repo-Internal References

| Finding | Source Path |
| --- | --- |
| Shared process helpers provide durable namespace checks and command execution. | [process_status.py](agents-remember-md/mcp/src/agents_remember/providers/lifecycle/process_status.py); [command_runner.py](agents-remember-md/mcp/src/agents_remember/providers/lifecycle/command_runner.py) |
| CGC backend startup is delegated to the backend module. | [backend.py](agents-remember-md/mcp/src/agents_remember/providers/cgc/lifecycle/backend.py) |
| Docker watcher command construction lives in the runner module. | [runner.py](agents-remember-md/mcp/src/agents_remember/providers/cgc/lifecycle/runner.py) |

## Update History

- 2026-05-31T12:30+02:00 — Removed already-running watcher detection from start preflight: `cgc_running_process_result` (and its `cgc_watcher_inspect` use / `alreadyRunning` short-circuit) deleted; layout params now typed `CgcRuntimeLayout` (1.0.0 review remediation).
- 2026-05-29T18:35+02:00: `cgc_backend_all_error` now accepts `dict | None` with a `None` guard (closes a latent crash when start-all returns a doctor-failure); extracted `_cgc_start_all_live` to reduce `cgc_start_all` complexity; behavior-preserving (commits `0549b28`, `e3dab63`).
- 2026-05-27T00:25+02:00: Updated after watcher startup began reusing
  backend start-result port mappings in its Compose render.
- 2026-05-26T12:51+02:00: Updated after watcher start/stop moved from host PIDs to Docker watcher containers.
- 2026-05-25T21:14+02:00: Split from `process.py` so watcher process control is separate from refresh and bounded query commands.
