# mcp/src/agents_remember/mcp/tools

| Field                  | Value                                          |
| ---------------------- | ---------------------------------------------- |
| repository             | agents-remember-md                             |
| sourceRoute            | `mcp/src/agents_remember/mcp/tools`            |
| doc_type               | `route-local-overview`                         |
| lastUpdated            | 2026-05-30T21:33+02:00|
| lastVerifiedCommitHash | `4117c3d98eadb4265af6e55f3dd8f2552e8589a0`                                      |
| lastVerifiedCommitDate | 2026-06-01T20:31:44+02:00|
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
| `core.py`       | ping, server_info, context_packet, runtime_install, resolve_context, skills_install. |
| `memory.py`     | drift_check, memory_quality_check, route_index_refresh, memory_init, baseline status/adopt, carryover plan/apply. |
| `providers.py`  | provider status/diagnostics/watchers, GrepAI search/trace, CGC query tools.|
| `worktree.py`   | worktree start/attach/status/closeout/integrate/cleanup, direct closeout.  |
| `benchmark.py`  | codex_benchmark_prepare, codex_benchmark_run.                              |
| `__init__.py`   | Facade re-exporting the full builder surface and `_tool_payload`.          |

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

## Repo-Internal References

| Finding | Source Path |
| --- | --- |
| FastMCP server registration calls these payload builders. | [server.py](agents-remember-md/mcp/src/agents_remember/mcp/server.py) |
| Public response model registry maps each tool name to a Pydantic model. | [tool_registry.py](agents-remember-md/mcp/src/agents_remember/models/tool_registry.py) |
| Domain controllers own the tool behavior the builders forward to. | [controllers overview](agents-remember-md/mcp/src/agents_remember/controllers/overview.md) |
| Schema tests assert public tool and response model coverage. | [test_models.py](agents-remember-md/mcp/tests/test_models.py) |
| Conformance test validates every builder routes through `_tool_payload`. | [test_tool_response_conformance.py](agents-remember-md/mcp/tests/test_tool_response_conformance.py) |

## Update History

- 2026-05-30T21:33+02:00: Re-verified the route against `8927f03` after the 0.9.x run; the per-domain Layout, hot path, and invariants still match the current exports. `core.py` gained `no_cache`/`install_provider_deps` forwarding in `runtime_install_payload` (documented on the file card); the registry's public surface is unchanged.
- 2026-05-29T18:35+02:00: Split `mcp/tools.py` (831 lines) into this `mcp/tools/` package by domain (commit `01f503d`); moved the registry purpose, invariants, and references here from the retired `tools.py.md`. Import surface unchanged.
- 2026-05-28T19:52+02:00: (from `tools.py`) Updated after all public payload builders were wired through the Pydantic response model registry and controller imports were split by domain.
- 2026-05-26T23:11+02:00: (from `tools.py`) Refreshed verification metadata after source commit `5ab704a` landed typed GrepAI payload forwarding.
- 2026-05-24T02:47+02:00: (from `tools.py`) Updated after public tool expectations added `memory_quality_check`.
- 2026-05-23T13:09+02:00: (from `tools.py`) Established for the complete Phase 04 public MCP tool surface.
