# mcp/src/agents_remember/mcp/tools.py

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember-md                         |
| path                   | `mcp/src/agents_remember/mcp/tools.py`     |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-05-28T19:52+02:00                     |
| lastVerifiedCommitHash | `bf3a3c4e310fb11032da885083d026a74a31ee9c` |
| lastVerifiedCommitDate | 2026-05-28T20:06:49+02:00|
| governingOverview      | `../../../overview.md`                     |

## Purpose

`tools.py` contains pure payload builders and public tool metadata for the
Agents Remember MCP server.

## Code Commentary

### Logic

The module declares `PUBLIC_TOOLS`, imports domain controllers directly, and
validates every public payload through `_tool_payload()`. `_tool_payload()` uses
`models.tool_registry.PUBLIC_TOOL_RESPONSE_MODELS` to select the declared
Pydantic response model for the tool name, validates the controller/core
payload, and serializes it with `model_dump(mode="json", exclude_none=True)`.

Core payloads such as `ping_payload()` and `server_info_payload()` are built in
this file. Operation payload builders remain thin: they pass typed MCP
arguments to the appropriate controller module, then hand the returned
dictionary to `_tool_payload()` for response-contract validation.

The public tool surface currently includes core server tools, context and
runtime tools, memory/onboarding tools, skill install, provider status and
diagnostics, GrepAI and CodeGraphContext provider tools, worktree/direct
closeout tools, memory baseline/carryover tools, and Codex benchmark tools.

### Invariants And Boundaries

- `PUBLIC_TOOLS` must match server registration in `server.py` and model
  registry keys in `models/tool_registry.py`.
- Public tool payload builders should stay transport-thin; deterministic
  behavior belongs in controllers and package services.
- Every public payload returned from this module must go through
  `_tool_payload()`.
- Do not restore the old `controllers.skill_tools` mega-facade. Import the
  domain controller that owns the tool's behavior.
- `_tool_payload()` validates response shape only; request validation remains
  in server signatures and controllers.

## Repo-Internal References

| Finding | Source Path |
| --- | --- |
| FastMCP server registration calls these payload builders. | [server.py](agents-remember-md/mcp/src/agents_remember/mcp/server.py) |
| Public response model registry maps each tool name to a Pydantic model. | [tool_registry.py](agents-remember-md/mcp/src/agents_remember/models/tool_registry.py) |
| Domain controllers now live in focused controller modules. | [controllers overview](agents-remember-md/mcp/src/agents_remember/controllers/overview.md) |
| Schema tests assert public tool and response model coverage. | [test_models.py](agents-remember-md/mcp/tests/test_models.py) |

## Update History

- 2026-05-28T19:52+02:00: Updated after all public payload builders were wired through the Pydantic response model registry and controller imports were split by domain.
- 2026-05-26T23:11+02:00: Refreshed verification metadata after source commit `5ab704a` landed typed GrepAI payload forwarding.
- 2026-05-26T22:54+02:00: Updated after GrepAI payload builders began forwarding typed workspace/project, output, and trace-action fields.
- 2026-05-24T10:06+02:00: Refreshed verification metadata after source commit `f48a346` exposed benchmark sandbox options through tool payload builders.
- 2026-05-24T08:56+02:00: Updated after `codex_benchmark_run_payload()` began forwarding the allowlisted `codex_sandbox` field.
- 2026-05-24T02:47+02:00: Updated after public tool expectations added `memory_quality_check`.
- 2026-05-24T00:35+02:00: Added regression coverage that service-backed MCP tools no longer expose command-capture artifacts.
- 2026-05-23T20:42+02:00: Updated public tool metadata and payload builders for typed CGC tools.
- 2026-05-23T13:09+02:00: Updated for the complete Phase 04 public MCP tool surface.
