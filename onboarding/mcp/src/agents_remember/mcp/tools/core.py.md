# mcp/src/agents_remember/mcp/tools/core.py

| Field                  | Value                                          |
| ---------------------- | ---------------------------------------------- |
| repository             | agents-remember-md                             |
| path                   | `mcp/src/agents_remember/mcp/tools/core.py`    |
| doc_type               | `file-level-onboarding`                        |
| lastUpdated            | 2026-05-30T21:33+02:00|
| lastVerifiedCommitHash | `72789a48dc47acf417725ae051eaa123cadeaa0b`                                      |
| lastVerifiedCommitDate | 2026-06-02T04:33:30+02:00|
| governingOverview      | `overview.md`                                  |

## Purpose

Server, context, install, and skills payload builders.

## Code Commentary

### Logic

Holds `ping_payload`, `server_info_payload`, `context_packet_payload`,
`runtime_install_payload`, `resolve_context_payload`, and
`skills_install_payload`. `ping`/`server_info` are built locally from
`SERVER_NAME`/`SERVER_VERSION`/`TRANSPORT` and config; the rest forward typed
arguments to their controllers (`build_context_packet`, `run_runtime_install`,
`resolve_context_tool`, `skills_install_tool`). `server_info_payload` reports
`PUBLIC_TOOLS`/`RESERVED_TOOLS`. `runtime_install_payload` forwards a full
`RuntimeInstallRequest` — `dry_run`, `include_benchmarks`, `install_provider_deps`
(default `True`), and `no_cache` (default `False`) — and `skills_install_payload`
forwards `overwrite`/`archive_existing` alongside `dry_run` (the installer is a
flat copy, so there is no layout argument).

### Invariants And Boundaries

- Every builder returns through `base._tool_payload`.
- Imports `SERVER_NAME`/`SERVER_VERSION` via `..` and `McpRuntimeConfig` via
  `..config`.
- `runtime_install_payload`/`skills_install_payload` default `dry_run=False`
  (act-by-default), matching the server registration; `dry_run=true` previews.
- Keep the builder signatures in lockstep with the `RuntimeInstallRequest` /
  `skills_install_tool` contracts and the server registration (e.g. `no_cache`);
  the builder stays transport-thin and does not interpret these flags.

## Update History

- 2026-06-02T04:40+02:00: `skills_install_payload` dropped the `layout` argument after the installer became a single flat copy (U-01-core-skills dissolved). `l-01-session-job-lifecycle` skill series, Sub-task B/S7, mcp 1.1.0.
- 2026-05-30T21:33+02:00: Documented `runtime_install_payload` forwarding the full `RuntimeInstallRequest` including `install_provider_deps` and the new `no_cache` flag, and `skills_install_payload`'s `layout`/`overwrite`/`archive_existing` forwarding. Verified against `8927f03`.
- 2026-05-29T20:20+02:00: Recorded the act-by-default `dry_run` default on the install payload builders.
- 2026-05-29T18:35+02:00: Created from the `mcp/tools.py` domain split (commit `01f503d`).
