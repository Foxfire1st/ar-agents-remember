# mcp/src/agents_remember/controllers/skill_tools.py

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember-md                         |
| path                   | `mcp/src/agents_remember/controllers/skill_tools.py` |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-05-23T20:56+02:00                     |
| lastVerifiedCommitHash | `4ad9686b20334d36308a05d615bccde204b11d7e` |
| lastVerifiedCommitDate | 2026-05-23T21:18:05+02:00|
| governingOverview      | `../../../overview.md`                     |

## Purpose

`skill_tools.py` is the controller facade for the Phase 04 skill-facing MCP
tool surface. It maps typed MCP inputs to package-owned resolver, drift,
provider, worktree, memory, benchmark, and skill-install services.

## Code Commentary

### Logic

The module keeps model-facing tools away from arbitrary shell execution by
constructing explicit package-local calls and fixed argument vectors. Provider
flows call the typed `providers.lifecycle_service` API with MCP-generated
settings instead of invoking `provider_lifecycle.main(argv)`. Worktree,
baseline, carryover, and benchmark flows that still have command-like
entrypoints are invoked through `run_package_main()` pending their own
service-layer refactors.

CodeGraphContext access is split into typed controller functions:
`cgc_symbol_search_tool()`, `cgc_callers_tool()`, `cgc_callees_tool()`,
`cgc_dependencies_tool()`, and `cgc_complexity_tool()`. These build fixed CGC
native argument vectors internally and no longer accept caller-supplied generic
`query_type` plus arbitrary argument lists.

`worktree_start_tool()` writes MCP-derived provider lifecycle settings when
provider setup is enabled and passes that path into the package-local worktree
manager. That keeps worktree provider preparation independent of coordinator
`system/settings.json` and deleted source scripts.

### Invariants And Boundaries

- Repo ids must resolve through `McpRuntimeConfig.repositories`.
- Contract, source-memory, and benchmark paths accepted by these tools must stay
  inside the configured coordination root unless the tool is explicitly a setup
  copy target such as `skills_install`.
- Do not add a generic command runner here; every public operation needs a
  typed function and package-owned target.
- Do not reintroduce generic CGC native-query plumbing on the MCP path; add a
  typed controller for each CGC operation the skills need.
- Provider tools should call `providers.lifecycle_service`, not the provider
  lifecycle CLI `main(argv)`.

## Repo-Internal References

| Finding | Source Path |
| --- | --- |
| Public MCP tool registration delegates to these facade functions. | [server.py](agents-remember-md/mcp/src/agents_remember/mcp/server.py) |
| Payload builders expose these facades to `server.py`. | [tools.py](agents-remember-md/mcp/src/agents_remember/mcp/tools.py) |
| Provider lifecycle service calls are centralized in the typed service layer. | [lifecycle_service.py](agents-remember-md/mcp/src/agents_remember/providers/lifecycle_service.py) |
| Package-local command-style capture still supports non-provider legacy facades. | [command_capture.py](agents-remember-md/mcp/src/agents_remember/mcp/command_capture.py) |
| Worktree provider setup consumes the generated settings path. | [git_worktree_manager.py](agents-remember-md/mcp/src/agents_remember/worktrees/git_worktree_manager.py) |

## Update History

- 2026-05-23T13:09+02:00: Created for the Phase 04 skill MCP tool surface.
- 2026-05-23T13:46+02:00: Updated for MCP-derived worktree provider settings after source scripts were removed.
- 2026-05-23T20:42+02:00: Updated for typed CodeGraphContext controllers replacing the generic `cgc_query` facade.
- 2026-05-23T20:56+02:00: Updated after MCP provider tools moved from provider lifecycle CLI capture to typed lifecycle service calls.
