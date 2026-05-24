# mcp/ — MCP Package Overview

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember-md                         |
| sourceRoute            | `mcp/`                                     |
| doc_type               | `route-overview`                           |
| lastUpdated            | 2026-05-24T02:47+02:00                     |
| lastVerifiedCommitHash | `b25d52f2b445554bb64115db2f27fd156954bcf3` |
| lastVerifiedCommitDate | 2026-05-24T02:36:33+02:00                 |
| governingOverview      | `../overview.md`                           |

## Governing Overview

[overview.md](../overview.md)

## Purpose

`mcp/` is the package-managed Agents Remember MCP server. It turns coordinator
startup and provider lifecycle behavior into typed, host-side operations backed
by importable Python services instead of model-edited coordinator scripts or
coordinator `system/settings.json`.

## Hot Path Summary

Start in `src/agents_remember/mcp/config.py` for trusted settings parsing,
`src/agents_remember/mcp/server.py` and `tools.py` for exposed MCP tools,
`controllers/context_packet.py` for startup packets, and
`controllers/runtime_install.py` plus `install/runtime.py` for MCP-owned runtime
installation. Provider status is composed in `providers/status.py`; provider
lifecycle settings are generated from MCP settings in `providers/settings.py`;
runner executable integrity is checked by `providers/integrity.py` before
watcher status is trusted. Memory-layer quality control lives under
`src/agents_remember/memory_quality/`: integrity checks include the onboarding
drift classifier/summary, and style checks currently include update-history
newest-first ordering.

## Route Model

The MCP package separates three surfaces:

- `agents_remember.mcp` owns transport wiring, tool registration, and trusted
  settings parsing.
- `agents_remember.controllers` owns operation-level composition such as
  `context_packet` and `runtime_install`.
- First-class service domains such as `kernel`, `providers`, `memory_quality`,
  `worktrees`, and `install` own deterministic behavior.

The trusted MCP settings file must be absolute and outside the coordinator root.
It supplies `coordinationRoot`, `workspaceRoot`, allowed repository IDs,
allowed provider IDs, timeout caps, and optional repository contract paths. The
server derives repository roots, memory roots, provider runtime roots, provider
data roots, and provider log roots from those settings. Tool calls name allowed
repo IDs and boolean options; they do not pass arbitrary host paths.

Provider runtime layout now uses a single coordinator provider root:

```text
<coordinationRoot>/providers/
  _bin/
  _venvs/
  runners/
    codegraphcontext/
    grepai/
  data/
    codegraphcontext/
    grepai/
  logs/
    codegraphcontext/
    grepai/
```

The MCP `runtime_install` operation copies runtime package assets to the
configured coordinator root and can run provider dependency installation through
package-local lifecycle code. It generates lifecycle settings from MCP settings,
not coordinator `system/settings.json`, and writes provider runner integrity
manifests beside the trusted MCP settings file after non-dry-run installs.

## Invariants And Boundaries

- MCP settings are authority; coordinator files can teach the model what to ask
  for but cannot grant provider or path authority.
- MCP tool calls must not accept `coordinationRoot`, `sourceRoot`, provider
  runtime roots, or arbitrary filesystem paths.
- Provider install/status must use generated lifecycle settings from
  `McpRuntimeConfig`.
- Provider status must check runner integrity before invoking watcher status.
- `providers/runners`, `providers/data`, and `providers/logs` are the active
  provider layout; `providers/<provider>` and `provider-data` are not active
  runtime roots.
- Resolver, provider lifecycle, memory quality, and worktree code under
  `mcp/src/agents_remember` is a package-local implementation surface. Original
  runtime scripts are not the MCP execution authority.

## Repo-Internal References

| Finding | Source Path |
| --- | --- |
| MCP settings reject coordinator `system/settings.json`, forbid settings inside the coordinator, and derive provider runtime roots under `providers/runners/<provider>`. | [config.py](agents-remember-md/mcp/src/agents_remember/mcp/config.py) |
| The tool surface exposes `context_packet` and `runtime_install`; handlers delegate to controllers. | [tools.py](agents-remember-md/mcp/src/agents_remember/mcp/tools.py); [server.py](agents-remember-md/mcp/src/agents_remember/mcp/server.py) |
| `context_packet` composes resolver, git, worktree, provider, and optional drift status without starting providers. | [context_packet.py](agents-remember-md/mcp/src/agents_remember/controllers/context_packet.py) |
| `runtime_install` derives install target and provider settings from `McpRuntimeConfig` and calls package-local install/lifecycle services. | [runtime_install.py](agents-remember-md/mcp/src/agents_remember/controllers/runtime_install.py); [install runtime](agents-remember-md/mcp/src/agents_remember/install/runtime.py) |
| Provider lifecycle settings are generated from MCP settings and include `providers/runners`, `providers/data`, and `providers/logs` paths. | [settings.py](agents-remember-md/mcp/src/agents_remember/providers/settings.py) |
| Provider status checks runner integrity before watcher status and reports structured recovery actions on integrity failure. | [integrity.py](agents-remember-md/mcp/src/agents_remember/providers/integrity.py); [status.py](agents-remember-md/mcp/src/agents_remember/providers/status.py) |
| Memory quality combines drift integrity and onboarding style checks for closeout. | [check.py](agents-remember-md/mcp/src/agents_remember/memory_quality/check.py); [history_order.py](agents-remember-md/mcp/src/agents_remember/memory_quality/style/update_history/history_order.py) |

## Update History

- 2026-05-24T02:47+02:00: Updated after drift moved into `memory_quality.integrity` and `memory_quality_check` became the closeout quality gate.
- 2026-05-23T04:29+02:00: Created for the MCP package route after Phase 3 added MCP-owned runtime installation, provider layout convergence, and runner integrity checks.
