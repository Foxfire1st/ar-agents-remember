# mcp/src/agents_remember/mcp/tools/core.py

| Field                  | Value                                          |
| ---------------------- | ---------------------------------------------- |
| repository             | agents-remember-md                             |
| path                   | `mcp/src/agents_remember/mcp/tools/core.py`    |
| doc_type               | `file-level-onboarding`                        |
| lastUpdated            | 2026-05-29T18:35+02:00|
| lastVerifiedCommitHash | `23f4d7681f7fcd729049c5f27878c84bbb8f8e58`                                      |
| lastVerifiedCommitDate | 2026-05-29T20:24:00+02:00|
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
`PUBLIC_TOOLS`/`RESERVED_TOOLS`.

### Invariants And Boundaries

- Every builder returns through `base._tool_payload`.
- Imports `SERVER_NAME`/`SERVER_VERSION` via `..` and `McpRuntimeConfig` via
  `..config`.
- `runtime_install_payload`/`skills_install_payload` default `dry_run=False`
  (act-by-default), matching the server registration; `dry_run=true` previews.

## Update History

- 2026-05-29T20:20+02:00: Recorded the act-by-default `dry_run` default on the install payload builders.
- 2026-05-29T18:35+02:00: Created from the `mcp/tools.py` domain split (commit `01f503d`).
