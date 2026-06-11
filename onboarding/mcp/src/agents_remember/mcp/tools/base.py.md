# mcp/src/agents_remember/mcp/tools/base.py

| Field                  | Value                                          |
| ---------------------- | ---------------------------------------------- |
| repository             | agents-remember-md                             |
| path                   | `mcp/src/agents_remember/mcp/tools/base.py`    |
| doc_type               | `file-level-onboarding`                        |
| lastUpdated            | 2026-06-10T09:56+02:00|
| lastVerifiedCommitHash | `a69b72e101d09423601916c03d4f59ecdee7dda6`                                      |
| lastVerifiedCommitDate | 2026-06-11T11:08:18+02:00|
| governingOverview      | `overview.md`                                  |

## Purpose

Shared payload-builder primitives for the MCP tools package: the public tool
name list and the single response-validation helper that every builder uses.

## Code Commentary

### Logic

Declares `TRANSPORT = "stdio"`, the `PUBLIC_TOOLS` tuple (36 tool names —
`direct_closeout_preview`/`apply` left in issue #62's worktree-only closeout),
`RESERVED_TOOLS`, and `_tool_payload(tool_name, payload)`. `_tool_payload`
selects the declared Pydantic model from
`models.tool_registry.PUBLIC_TOOL_RESPONSE_MODELS`, validates the
controller/core payload, serializes it with
`model_dump(mode="json", exclude_none=True)`, and then stamps token-accounting
metadata onto the dumped dict via `finalize_payload_tokens` (from
`models/tokens.py`). Because this is the single choke point every public payload
passes through, that one call is what gives every MCP response a real
`tokens`/`tokenizer`/`tokenCountExact` rather than the model defaults.

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
| Token-accounting finalizer applied to every dumped payload. | [tokens.py](agents-remember-md/mcp/src/agents_remember/models/tokens.py) |

## Update History

- 2026-06-11T06:47+02:00 — Removed `direct_closeout_preview`/`direct_closeout_apply` from `PUBLIC_TOOLS` (issue #62 worktree-only closeout); tuple is now 36 names (the earlier "37" count was itself stale — the tuple held 38 before this removal).
- 2026-06-10T09:56+02:00 — Registered `worktree_sync` in `PUBLIC_TOOLS` (GitHub #54 sub-task D); tuple is now 37 names.
- 2026-06-01T20:45+02:00 — Registered `worktree_abandon` in `PUBLIC_TOOLS` so its response is validated like every other public tool.
- 2026-05-30T22:29+02:00: Documented that `_tool_payload` now finalizes token-accounting metadata via `finalize_payload_tokens` (S6 wiring), making it the single point that populates `tokens`/`tokenizer`/`tokenCountExact` on every MCP response. Verification metadata stays pinned until closeout commits the source change.
- 2026-05-29T18:35+02:00: Created when `mcp/tools.py` was split into the `mcp/tools/` package (commit `01f503d`); holds the `_tool_payload`/`PUBLIC_TOOLS` contract previously documented in `tools.py.md`.
