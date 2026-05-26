# mcp/src/agents_remember/providers/cgc/lifecycle/ - CGC Lifecycle Modules Overview

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember-md                         |
| sourceRoute            | `mcp/src/agents_remember/providers/cgc/lifecycle/` |
| doc_type               | `route-overview`                           |
| lastUpdated            | 2026-05-26T13:58+02:00                     |
| lastVerifiedCommitHash | `a8ee8440dfa920d1153a4bb4bb43cc77534c3c90` |
| lastVerifiedCommitDate | 2026-05-25T15:22:52+02:00                  |
| governingOverview      | `../overview.md`                           |

## Governing Overview

[CodeGraphContext Provider Overview](../overview.md)

## Purpose

`cgc/lifecycle/` contains the CodeGraphContext provider lifecycle
implementation, organized behind a CGC package facade with prefix-free
filenames.

## Hot Path Summary

`__init__.py` re-exports the CGC public lifecycle surface. `core.py` derives
settings and runtime layout, `backend.py` manages the FalkorDB Docker backend,
`runner.py` builds the Docker runner image and command lines,
`installation.py` owns install/status/patch/doctor behavior,
`process_control.py` owns watcher process start/stop,
`refresh.py` owns index refresh, and `query.py` owns bounded native run plus
visualizer commands.

## Route Model

- `core.py` is configuration and layout only.
- `backend.py` owns the managed FalkorDB container, backend state, and shared
  CGC Docker network attachment.
- `runner.py` owns the CGC Docker runner image, patch script, networked mounts,
  host-user container execution, env, and Docker command construction.
- `installation.py` owns Docker runner install, status, no-op patch reporting,
  and doctor checks.
- `process_control.py` owns long-running Docker watcher container start/stop.
- `refresh.py` owns Dockerized CGC index refresh.
- `query.py` owns Dockerized bounded commands and visualizer lifecycle.

## Invariants And Boundaries

- Keep `__init__.py` as the package export facade.
- Do not put GrepAI behavior in this package.
- Long-running CGC process actions must keep durable namespace checks.
- Backend Docker lifecycle stays separate from process start/stop logic.
- Managed CGC commands must run through Docker, not through a host Python venv
  or host `cgc` executable.
- CGC runner and watcher containers must reach FalkorDB over the shared Docker
  network, not through host loopback.

## Repo-Internal References

| Finding | Source Path |
| --- | --- |
| The parent lifecycle facade imports the CGC package facade. | [__init__.py](agents-remember-md/mcp/src/agents_remember/providers/lifecycle/__init__.py) |
| Watcher aggregation imports CGC all-root start/status/stop behavior from this package. | [watchers.py](agents-remember-md/mcp/src/agents_remember/providers/lifecycle/watchers.py) |

## Update History

- 2026-05-26T13:58+02:00: Updated after CGC backend and runner lifecycle gained shared Docker network wiring and host-user runner execution.
- 2026-05-26T12:51+02:00: Updated after CGC moved to a Docker runner image/container instead of a host provider venv.
- 2026-05-25T21:14+02:00: Moved under the provider-owned `providers/cgc/lifecycle/` route.
- 2026-05-25T21:14+02:00: Split the former process module into process control, refresh, and query modules to clear Radon MI pressure.
- 2026-05-25T19:09+02:00: Created when flat `cgc_*` lifecycle modules moved under `lifecycle_modules/cgc/` with prefix-free filenames.
