# mcp/src/agents_remember/mcp/tools

| Field                  | Value                                          |
| ---------------------- | ---------------------------------------------- |
| repository             | agents-remember                             |
| sourceRoute            | `mcp/src/agents_remember/mcp/tools`            |
| doc_type               | `route-local-overview`                         |
| lastUpdated            | 2026-06-10T07:40+02:00|
| lastVerifiedCommitHash | `a69b72e101d09423601916c03d4f59ecdee7dda6`                                      |
| lastVerifiedCommitDate | 2026-06-11T11:08:18+02:00|
| governingOverview      | `../../../../../overview.md`                   |

## Purpose

`mcp/tools/` is the pure payload-builder registry for the Agents Remember MCP
server. It was split out of the former single `mcp/tools.py` module (commit
`01f503d`) into one submodule per tool domain, behind a facade `__init__.py`
that preserves the public import surface: every `*_payload` builder, the
`PUBLIC_TOOLS`/`RESERVED_TOOLS`/`TRANSPORT` constants, and the `_tool_payload`
re-export remain importable from `agents_remember.mcp.tools`.

## Hot Path Summary

Server registration imports `*_payload` builders from `agents_remember.mcp.tools`;
each builder forwards typed MCP arguments to its domain controller and validates
the result through `base._tool_payload`. Start at `base.py` for the shared
`_tool_payload`/`PUBLIC_TOOLS` contract, then the domain submodule that owns the
tool.

## Layout

| Module          | Owns                                                                       |
| --------------- | -------------------------------------------------------------------------- |
| `base.py`       | `TRANSPORT`, `PUBLIC_TOOLS`, `RESERVED_TOOLS`, and `_tool_payload`.         |
| `core.py`       | ping, server_info, context_packet, runtime_install, resolve_context, skills_install; `compact_runtime_install_payload`. |
| `memory.py`     | drift_check, memory_quality_check, route_index_refresh, memory_init, baseline status/adopt, carryover plan/apply; `compact_carryover_payload`. |
| `providers.py`  | provider status/diagnostics/watchers, GrepAI search/trace, CGC query tools; `compact_diagnostics_payload`, `compact_watchers_payload`. |
| `worktree.py`   | worktree start/attach/status/sync/closeout/integrate/cleanup/abandon.      |
| `benchmark.py`  | codex_benchmark_prepare, codex_benchmark_run.                              |
| `__init__.py`   | Facade re-exporting the full builder surface and `_tool_payload`.          |

Since 2.5.1 this route also owns the response token-budget layer: the verbose
tools (`runtime_install`, `provider_diagnostics`, `provider_watchers`, and
since 2.5.2 the carryover plan/apply pair) write their full result to
`temp/tool-reports/<tool>/` via `mcp/tool_reports.py` (keep-last-5 / 7-day
write-time prune, secret redaction) and return a compact outcome with an
inline `reportPath` through the per-domain `compact_*_payload` helpers.

## Invariants And Boundaries

- `PUBLIC_TOOLS` (in `base.py`) must match server registration in `server.py`
  and the model registry keys in `models/tool_registry.py`.
- Every public payload returned from any submodule must go through
  `base._tool_payload`, which validates response shape only (request validation
  stays in server signatures and controllers).
- Payload builders stay transport-thin; deterministic behavior belongs in
  controllers and package services. Import the domain controller that owns the
  tool's behavior — do not reintroduce a mega-facade.
- Submodules use `..` for `mcp`-package imports (`from .. import SERVER_NAME`,
  `from ..config import McpRuntimeConfig`) since they sit one level below the
  former `tools.py`.
- The facade `__init__.py` re-exports `_tool_payload` with an explicit
  `import _tool_payload as _tool_payload` so the conformance test's
  `tools._tool_payload` access keeps working.
- Compaction is wire-shape only and lives in this route, not in controllers:
  the full result is written to the tool report BEFORE any compaction mutates
  it, decision/outcome facts stay inline, and
  `test_tool_response_budgets.py` holds every compact builder under
  `INLINE_BUDGET_CHARS` with deliberately fat inputs.

## Repo-Internal References

| Finding | Source Path |
| --- | --- |
| FastMCP server registration calls these payload builders. | [server.py](agents-remember/mcp/src/agents_remember/mcp/server.py) |
| Public response model registry maps each tool name to a Pydantic model. | [tool_registry.py](agents-remember/mcp/src/agents_remember/models/tool_registry.py) |
| Domain controllers own the tool behavior the builders forward to. | [controllers overview](agents-remember/mcp/src/agents_remember/controllers/overview.md) |
| Schema tests assert public tool and response model coverage. | [test_models.py](agents-remember/mcp/tests/test_models.py) |
| Conformance test validates every builder routes through `_tool_payload`. | [test_tool_response_conformance.py](agents-remember/mcp/tests/test_tool_response_conformance.py) |

## Update History

- 2026-06-11T06:47+02:00 — Issue #62 worktree-only closeout: `worktree.py` dropped the two `direct_closeout_*` payload builders (Layout row updated to the current worktree verb set, including sync/abandon); `base.py`'s `PUBLIC_TOOLS` and the facade exports shrank to 36 names.
- 2026-06-10T09:56+02:00 — No route impact: sub-task D adds `worktree_sync_payload` (plus the `PUBLIC_TOOLS`/facade registrations) following the existing one-builder-per-tool pattern; the payload-builder route model this overview describes is unchanged (detail in the file sidecars).
- 2026-06-10T09:30+02:00 — No route impact: `tools/worktree.py` and `tools/core.py` only forward the new `stale_base_choice` / `include_freshness` arguments to their controllers (GitHub #54); the payload-builder surface this overview describes is unchanged.
- 2026-06-10T07:40+02:00 — No route impact: `tools/worktree.py` only forwards the new `retry_provider_setup` flag to the controller (GitHub #53).
- 2026-06-10T05:30+02:00 — Route body caught up with the 2.5.1/2.5.2 response-budget layer (compact builders per domain, tool-report filing, report-before-compaction and budget-test invariants); previous closeouts had only stamped the verification header. Developer-flagged gap.
- 2026-05-30T21:33+02:00: Re-verified the route against `8927f03` after the 0.9.x run; the per-domain Layout, hot path, and invariants still match the current exports. `core.py` gained `no_cache`/`install_provider_deps` forwarding in `runtime_install_payload` (documented on the file card); the registry's public surface is unchanged.
- 2026-05-29T18:35+02:00: Split `mcp/tools.py` (831 lines) into this `mcp/tools/` package by domain (commit `01f503d`); moved the registry purpose, invariants, and references here from the retired `tools.py.md`. Import surface unchanged.
- 2026-05-28T19:52+02:00: (from `tools.py`) Updated after all public payload builders were wired through the Pydantic response model registry and controller imports were split by domain.
- 2026-05-26T23:11+02:00: (from `tools.py`) Refreshed verification metadata after source commit `5ab704a` landed typed GrepAI payload forwarding.
- 2026-05-24T02:47+02:00: (from `tools.py`) Updated after public tool expectations added `memory_quality_check`.
- 2026-05-23T13:09+02:00: (from `tools.py`) Established for the complete Phase 04 public MCP tool surface.
