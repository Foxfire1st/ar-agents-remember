# mcp/src/agents_remember/mcp/tools/base.py

| Field                  | Value                                          |
| ---------------------- | ---------------------------------------------- |
| repository             | agents-remember-md                             |
| path                   | `mcp/src/agents_remember/mcp/tools/base.py`    |
| doc_type               | `file-level-onboarding`                        |
| lastUpdated            | 2026-05-29T18:35+02:00|
| lastVerifiedCommitHash | `01f503dcba3a6eacc1587941f6a89fce0bcc72a2`                                      |
| lastVerifiedCommitDate | 2026-05-29T18:32:57+02:00|
| governingOverview      | `overview.md`                                  |

## Purpose

Shared payload-builder primitives for the MCP tools package: the public tool
name list and the single response-validation helper that every builder uses.

## Code Commentary

### Logic

Declares `TRANSPORT = "stdio"`, the `PUBLIC_TOOLS` tuple (36 tool names),
`RESERVED_TOOLS`, and `_tool_payload(tool_name, payload)`. `_tool_payload`
selects the declared Pydantic model from
`models.tool_registry.PUBLIC_TOOL_RESPONSE_MODELS`, validates the
controller/core payload, and serializes it with
`model_dump(mode="json", exclude_none=True)`.

### Invariants And Boundaries

- `PUBLIC_TOOLS` must match server registration in `server.py` and the model
  registry keys in `models/tool_registry.py`.
- `_tool_payload` validates response shape only; request validation stays in
  server signatures and controllers.
- Every public payload in the sibling domain modules must pass through
  `_tool_payload`.

## Repo-Internal References

| Finding | Source Path |
| --- | --- |
| Response model registry resolved per tool name. | [tool_registry.py](agents-remember-md/mcp/src/agents_remember/models/tool_registry.py) |
| Server registers exactly the `PUBLIC_TOOLS` names. | [server.py](agents-remember-md/mcp/src/agents_remember/mcp/server.py) |

## Update History

- 2026-05-29T18:35+02:00: Created when `mcp/tools.py` was split into the `mcp/tools/` package (commit `01f503d`); holds the `_tool_payload`/`PUBLIC_TOOLS` contract previously documented in `tools.py.md`.
