# mcp/src/agents_remember/controllers/skill_tools.py

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember-md                         |
| path                   | `mcp/src/agents_remember/controllers/skill_tools.py` |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-05-23T13:46+02:00                     |
| lastVerifiedCommitHash | `a6890ae469b70ef045a127fc774d6aa51a54e65a` |
| lastVerifiedCommitDate | 2026-05-23T18:31:48+02:00|
| governingOverview      | `../../../overview.md`                     |

## Purpose

`skill_tools.py` is the controller facade for the Phase 04 skill-facing MCP
tool surface. It maps typed MCP inputs to package-owned resolver, drift,
provider, worktree, memory, benchmark, and skill-install services.

## Code Commentary

### Logic

The module keeps model-facing tools away from arbitrary shell execution by
constructing explicit package-local calls and fixed argument vectors. Provider,
worktree, baseline, carryover, and benchmark flows that still have command-like
entrypoints are invoked through `run_package_main()` so stdout, stderr, exit
code, and JSON payloads are returned in a stable shape.

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

## Repo-Internal References

| Finding | Source Path |
| --- | --- |
| Public MCP tool registration delegates to these facade functions. | [server.py](agents-remember-md/mcp/src/agents_remember/mcp/server.py) |
| Payload builders expose these facades to `server.py`. | [tools.py](agents-remember-md/mcp/src/agents_remember/mcp/tools.py) |
| Package-local command-style capture is centralized. | [command_capture.py](agents-remember-md/mcp/src/agents_remember/mcp/command_capture.py) |
| Worktree provider setup consumes the generated settings path. | [git_worktree_manager.py](agents-remember-md/mcp/src/agents_remember/worktrees/git_worktree_manager.py) |

## Update History

- 2026-05-23T13:09+02:00: Created for the Phase 04 skill MCP tool surface.
- 2026-05-23T13:46+02:00: Updated for MCP-derived worktree provider settings after source scripts were removed.
