# mcp/src/agents_remember/mcp/tools.py

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember-md                         |
| path                   | `mcp/src/agents_remember/mcp/tools.py`     |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-05-23T13:09+02:00                     |
| lastVerifiedCommitHash | `d445e83e7d28e3c34b15d8299d279d65ab9183b9` |
| lastVerifiedCommitDate | 2026-05-23T05:45:38+02:00                 |
| governingOverview      | `../../../overview.md`                     |

## Purpose

`tools.py` contains pure payload builders and public tool metadata for the
Agents Remember MCP server.

## Code Commentary

### Logic

The file keeps `ping`, `server_info`, `context_packet`, and `runtime_install`
payloads, and now exposes the full Phase 04 skill-facing tool surface through
thin functions that delegate to `controllers.skill_tools`.

### Invariants And Boundaries

- `PUBLIC_TOOLS` must match the tools registered in `server.py`.
- Payload builders should stay thin; deterministic behavior belongs in
  controllers and package services.
- `server_info` reports no reserved provider status tool now that
  `provider_status` is public.

## Repo-Internal References

| Finding | Source Path |
| --- | --- |
| Server registration imports payload builders from this file. | [server.py](agents-remember-md/mcp/src/agents_remember/mcp/server.py) |
| Phase 04 behavior lives behind controller facades. | [skill_tools.py](agents-remember-md/mcp/src/agents_remember/controllers/skill_tools.py) |

## Update History

- 2026-05-23T13:09+02:00: Updated for the complete Phase 04 public MCP tool surface.
