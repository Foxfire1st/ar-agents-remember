# mcp/src/agents_remember/mcp/tools.py

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember-md                         |
| path                   | `mcp/src/agents_remember/mcp/tools.py`     |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-05-23T20:42+02:00                     |
| lastVerifiedCommitHash | `3417d47f1e76d37e9ba6e803c7b28afa4758da9c` |
| lastVerifiedCommitDate | 2026-05-23T23:06:47+02:00|
| governingOverview      | `../../../overview.md`                     |

## Purpose

`tools.py` contains pure payload builders and public tool metadata for the
Agents Remember MCP server.

## Code Commentary

### Logic

The file keeps `ping`, `server_info`, `context_packet`, and `runtime_install`
payloads, and now exposes the full Phase 04 skill-facing tool surface through
thin functions that delegate to `controllers.skill_tools`.

`PUBLIC_TOOLS` now reports typed CGC tools (`cgc_symbol_search`,
`cgc_callers`, `cgc_callees`, `cgc_dependencies`, and `cgc_complexity`) instead
of the removed generic `cgc_query` name. Matching payload builders forward only
typed fields to the controller layer.

### Invariants And Boundaries

- `PUBLIC_TOOLS` must match the tools registered in `server.py`.
- Payload builders should stay thin; deterministic behavior belongs in
  controllers and package services.
- `server_info` reports no reserved provider status tool now that
  `provider_status` is public.
- Do not include removed generic tool names in `PUBLIC_TOOLS`; skill-facing
  provider operations should remain typed.

## Repo-Internal References

| Finding | Source Path |
| --- | --- |
| Server registration imports payload builders from this file. | [server.py](agents-remember-md/mcp/src/agents_remember/mcp/server.py) |
| Phase 04 behavior lives behind controller facades. | [skill_tools.py](agents-remember-md/mcp/src/agents_remember/controllers/skill_tools.py) |

## Update History

- 2026-05-23T13:09+02:00: Updated for the complete Phase 04 public MCP tool surface.
- 2026-05-23T20:42+02:00: Updated public tool metadata and payload builders for typed CGC tools.
