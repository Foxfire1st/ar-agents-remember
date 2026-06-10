# mcp/ — MCP Package Overview

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember-md                         |
| sourceRoute            | `mcp/`                                     |
| doc_type               | `route-local-overview`                     |
| lastUpdated            | 2026-06-09T14:52+02:00                     |
| lastVerifiedCommitHash | `cca911fcb6417ecf56de00c17d05aa304daa51c5` |
| lastVerifiedCommitDate | 2026-06-10T02:35:22+02:00|
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
`src/agents_remember/mcp/server.py` and the `mcp/tools/` package for exposed
MCP tools (`server.py` installs `mcp/compact_content.py` to minify tool-result
text), `models/tool_registry.py` for public response contracts,
`controllers/context_packet.py` for compact `ContextPacketV2` startup packets,
and `controllers/runtime_install.py` plus `install/runtime.py` for MCP-owned
runtime installation. Provider status is composed in `providers/status.py`;
provider lifecycle settings are generated from MCP settings in
`providers/settings.py`. Provider lifecycle implementation is now split between
the `providers/lifecycle/` facade/shared helpers and provider-owned
`providers/cgc/lifecycle/` plus `providers/grepai/lifecycle/` packages; there
is no legacy `provider_lifecycle.py` facade. Memory-layer quality control lives under
`src/agents_remember/memory_quality/`: integrity checks include the onboarding
drift classifier/summary, and style checks currently include update-history
newest-first ordering. Runtime package data under
`src/agents_remember/package_data/` is synchronized from canonical root runtime
asset folders by `scripts/sync-runtime.py`, and the sync behavior is covered by
`mcp/tests/test_sync_runtime.py` plus the pre-commit check.

## Route Model

The MCP package separates three surfaces:

- `agents_remember.mcp` owns transport wiring, tool registration, and trusted
  settings parsing.
- `agents_remember.controllers` owns operation-level composition such as
  `context_packet`, provider tools, worktree tools, memory tools, benchmarks,
  and `runtime_install`.
- `agents_remember.models` owns public MCP response contracts and the
  tool-to-response-model registry used by the `mcp/tools/` payload builders.
- First-class service domains such as `kernel`, `providers`, `memory_quality`,
  `worktrees`, and `install` own deterministic behavior.

The trusted MCP settings file must be absolute and outside the coordinator root.
It supplies `coordinationRoot`, `workspaceRoot`, allowed repository IDs,
allowed provider IDs, timeout caps, and optional repository contract paths. The
server derives repository roots, memory roots, provider runtime roots, provider
data roots, and provider log roots from those settings. Tool calls name allowed
repo IDs and boolean options; they do not pass arbitrary host paths.

Provider runtime layout now uses a provider runtime root plus a central log
root under the coordinator:

```text
<coordinationRoot>/
  providers/
    runners/
      codegraphcontext/
      grepai/
    data/
      codegraphcontext/
      grepai/
  logs/
    mcp/
    providers/
      codegraphcontext/
      grepai/
      setup/
      status/
```

The `runtime_install` MCP tool operation copies runtime package assets to the
configured coordinator root and can run provider dependency installation through
package-local lifecycle code. It generates lifecycle settings from MCP settings,
not coordinator `system/settings.json`; provider setup records image locks,
setup summaries, and provider-state files through the package lifecycle code.
Settings-backed `grepai-memory` is Docker-only: the complete stack is the
managed runner image/container, PostgreSQL/pgvector, Ollama, and their shared
Docker network, with no host GrepAI binary or host Ollama fallback.

The package data that `runtime_install` copies is not edited as an independent
source of truth. Canonical runtime assets live at the repository root in
`agents-md-files/`, `benchmarks/`, `providers/`, and `system/`; the sync script
replaces the corresponding package-data folders and reports missing, extra, or
changed files in check mode.

## Invariants And Boundaries

- MCP settings are authority; coordinator files can teach the model what to ask
  for but cannot grant provider or path authority.
- MCP tool calls must not accept `coordinationRoot`, `sourceRoot`, provider
  runtime roots, or arbitrary filesystem paths.
- Provider install/status must use generated lifecycle settings from
  `McpRuntimeConfig`.
- Provider status reports watcher/current-state readiness and recovery actions;
  the prior runner-integrity gate was removed in the 1.0.0 remediation.
- `providers/runners`, `providers/data`, `logs/mcp`, and `logs/providers` are
  the active provider/runtime log layout; `providers/_bin`, `providers/_venvs`,
  `providers/<provider>`, and `provider-data` are not active runtime roots.
- CGC managed execution is Docker-runner owned; do not add host `venvRoot`,
  host `cgc` executable, or site-packages patch fallback paths.
- `grepai-memory` must remain Docker-or-bust in the MCP runtime; do not add
  host binary or host Ollama fallbacks.
- Resolver, provider lifecycle, memory quality, and worktree code under
  `mcp/src/agents_remember` is a package-local implementation surface. Original
  runtime scripts are not the MCP execution authority.
- Public MCP tool payloads should validate through
  `models.tool_registry.PUBLIC_TOOL_RESPONSE_MODELS`; compact context belongs
  in `ContextPacketV2`, and detailed provider state belongs in
  `provider_diagnostics`.
- Skipped provider details are still a modeled public contract: compact
  provider summaries report aggregate skipped state, omit provider detail rows,
  and rely on optional-null provider `ok` fields to survive JSON
  serialization/re-validation.

## Repo-Internal References

| Finding | Source Path |
| --- | --- |
| MCP settings reject coordinator `system/settings.json`, forbid settings inside the coordinator, and derive provider runtime roots under `providers/runners/<provider>`. | [config.py](agents-remember-md/mcp/src/agents_remember/mcp/config.py) |
| The tool surface exposes `context_packet`, provider diagnostics, runtime, memory, worktree, benchmark, and install tools; handlers delegate to controllers and response validation flows through the model registry. | [mcp/tools/](agents-remember-md/mcp/src/agents_remember/mcp/tools/); [server.py](agents-remember-md/mcp/src/agents_remember/mcp/server.py); [tool_registry.py](agents-remember-md/mcp/src/agents_remember/models/tool_registry.py) |
| `server.py` installs a FastMCP shim that minifies the JSON text mirror of tool results without touching structured content. | [compact_content.py](agents-remember-md/mcp/src/agents_remember/mcp/compact_content.py) |
| `context_packet` composes resolver, git, worktree, compact provider summary, and optional drift status into `ContextPacketV2`; detailed provider state is exposed by `provider_diagnostics`. | [context_packet.py](agents-remember-md/mcp/src/agents_remember/controllers/context_packet.py); [context_packet model](agents-remember-md/mcp/src/agents_remember/models/context_packet.py); [provider models](agents-remember-md/mcp/src/agents_remember/models/providers.py) |
| `runtime_install` derives install target and provider settings from `McpRuntimeConfig` and calls package-local install/lifecycle services. | [runtime_install.py](agents-remember-md/mcp/src/agents_remember/controllers/runtime_install.py); [install runtime](agents-remember-md/mcp/src/agents_remember/install/runtime.py) |
| Runtime package data is synchronized from canonical root asset folders, and tests verify missing, extra, changed, and target-scope behavior. | [sync-runtime.py](agents-remember-md/scripts/sync-runtime.py); [test_sync_runtime.py](agents-remember-md/mcp/tests/test_sync_runtime.py); [pre-commit hook](agents-remember-md/.githooks/pre-commit) |
| Provider lifecycle settings are generated from MCP settings and include `providers/runners`, `providers/data`, `logs/mcp`, and `logs/providers` paths. | [settings.py](agents-remember-md/mcp/src/agents_remember/providers/settings.py) |
| Provider status reports watcher status and structured recovery actions; the prior runner-integrity check was removed in the 1.0.0 remediation. | [status.py](agents-remember-md/mcp/src/agents_remember/providers/status.py) |
| Provider lifecycle is now a facade plus focused provider/shared packages instead of a monolithic file. | [providers/lifecycle/](agents-remember-md/mcp/src/agents_remember/providers/lifecycle/); [CGC lifecycle overview](src/agents_remember/providers/cgc/lifecycle/overview.md); [GrepAI lifecycle overview](src/agents_remember/providers/grepai/lifecycle/overview.md) |
| Memory quality combines drift integrity and onboarding style checks for closeout. | [check.py](agents-remember-md/mcp/src/agents_remember/memory_quality/check.py); [history_order.py](agents-remember-md/mcp/src/agents_remember/memory_quality/style/update_history/history_order.py) |

## Update History

- 2026-06-09T14:52+02:00: Refreshed the MCP route overview against MCP 2.4.1 `main`; added the canonical root runtime asset sync boundary for package data.
- 2026-06-08T09:57+02:00: Re-verified the MCP package route after PR-39 restored context-packet provider-summary validation and made skipped-provider summaries a modeled optional-null contract.
- 2026-06-06T12:15: Re-verified against the current MCP package surface; corrected stale `mcp/tools.py` and provider lifecycle module references after the `mcp/tools/` package split and provider-first lifecycle packages.
- 2026-05-31T12:40+02:00: Removed the deleted `providers/integrity.py` runner-integrity prose and reference row after the provider-runner integrity feature was removed in the 1.0.0 remediation; `providers/status.py` no longer checks runner integrity.
- 2026-05-29T08:53+02:00: Updated after `server.py` began installing the `mcp/compact_content.py` shim that minifies tool-result text mirrors, and after dev-time tool-response conformance tests landed.
- 2026-05-28T19:52+02:00: Updated after public MCP response payloads were wired through Pydantic models, context packets moved to compact V2, provider diagnostics became the detail boundary, and controllers split by domain.
- 2026-05-28T13:40+02:00: Tightened MCP provider invariants to forbid CGC host `venvRoot`, host executable, and site-packages patch fallback paths.
- 2026-05-28T12:32+02:00: Updated after provider operator logs moved into the central `logs/` tree and provider status began writing current-state snapshots under `logs/providers/status/`.
- 2026-05-25T19:16+02:00: Updated after the legacy `provider_lifecycle.py` facade was deleted and `providers.lifecycle` became the sole lifecycle facade.
- 2026-05-25T19:01+02:00: Updated after provider lifecycle split into focused modules and GrepAI runtime became Docker-only without `_bin`, `_venvs`, host GrepAI, or host Ollama fallback.
- 2026-05-24T02:47+02:00: Updated after drift moved into `memory_quality.integrity` and `memory_quality_check` became the closeout quality gate.
- 2026-05-23T04:29+02:00: Created for the MCP package route after Phase 3 added MCP-owned runtime installation, provider layout convergence, and runner integrity checks.
