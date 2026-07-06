# mcp/src/agents_remember/providers/cgc/lifecycle/ - CGC Lifecycle Modules Overview

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember                         |
| sourceRoute            | `mcp/src/agents_remember/providers/cgc/lifecycle/` |
| doc_type               | `route-local-overview`                     |
| lastUpdated            | 2026-07-06T23:55+02:00                     |
| lastVerifiedCommitHash | `9d58058e3ce4815b0356794fc21973ebe9c71345` |
| lastVerifiedCommitDate | 2026-07-06T11:47:10+02:00|
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
`installation.py` owns install/status/patch/doctor behavior including watcher
container state, last-refresh, and indexing-state reporting,
`process_control.py` owns watcher process start/stop,
`refresh.py` owns index refresh, and `query.py` owns bounded native run plus
visualizer commands.

## Route Model

- `core.py` is configuration and layout only. Since L13 its settings-backed layout requires an EXPLICIT `--from-settings` path — `cgc_settings_from_file` dropped the coordination-root fallback argument (the old implicit fallback was fail-open: empty config on a missing file).
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
- Status surfaces should include backend and watcher container state so MCP
  current-state packets can report what is running now.

## Repo-Internal References

| Finding | Source Path |
| --- | --- |
| The parent lifecycle facade imports the CGC package facade. | [__init__.py](agents-remember/mcp/src/agents_remember/providers/lifecycle/__init__.py) |
| Watcher aggregation imports CGC all-root start/status/stop behavior from this package. | [watchers.py](agents-remember/mcp/src/agents_remember/providers/lifecycle/watchers.py) |

## Update History

- 2026-07-06T23:55+02:00 — L13 owner follow-up (body): core.py's settings-backed layout now states the explicit --from-settings requirement in the route model (the earlier ride-along was history-only). Verification metadata pinned until closeout stamps the L13 commit.

- 2026-07-06T23:08+02:00 — 260703-L13 ride-along: `core.py`'s settings-backed layout reads
  call `cgc_settings_from_file` with the explicit `--from-settings` path only (the implicit
  coordinator-settings fallback was deleted route-wide; the manual
  `--repo-id`/`--code-repo-root` override path is unaffected). Route model unchanged.
  Verification metadata pinned until closeout stamps the L13 commit.

- 2026-06-06T12:15: Re-verified against the current CGC lifecycle package; backend, runner, installation, process, refresh, and query boundaries still match.
- 2026-05-28T12:32+02:00: Updated after CGC status began surfacing backend/watcher container state for provider current-state reporting.
- 2026-05-26T13:58+02:00: Updated after CGC backend and runner lifecycle gained shared Docker network wiring and host-user runner execution.
- 2026-05-26T12:51+02:00: Updated after CGC moved to a Docker runner image/container instead of a host provider venv.
- 2026-05-25T21:14+02:00: Moved under the provider-owned `providers/cgc/lifecycle/` route.
- 2026-05-25T21:14+02:00: Split the former process module into process control, refresh, and query modules to clear Radon MI pressure.
- 2026-05-25T19:09+02:00: Created when flat `cgc_*` lifecycle modules moved under `lifecycle_modules/cgc/` with prefix-free filenames.
