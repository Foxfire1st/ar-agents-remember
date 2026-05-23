# mcp/src/agents_remember/providers/provider_lifecycle.py

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember-md                         |
| path                   | `mcp/src/agents_remember/providers/provider_lifecycle.py` |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-05-23T13:46+02:00                     |
| lastVerifiedCommitHash | `a6890ae469b70ef045a127fc774d6aa51a54e65a` |
| lastVerifiedCommitDate | 2026-05-23T18:31:48+02:00|
| governingOverview      | `../../../overview.md`                     |

## Purpose

`provider_lifecycle.py` owns the package-local provider lifecycle command
implementation for GrepAI, CodeGraphContext, watcher management, provider
runtime installation, refresh, status, and visualization.

## Code Commentary

### Logic

The module exposes a command-style `main(argv)` entrypoint that MCP tools call
through package-local command capture. It reads generated lifecycle settings via
`--from-settings`, expands provider runtime layouts, manages provider backends,
and builds bounded native provider commands for GrepAI and CodeGraphContext.

### Invariants And Boundaries

- Provider settings authority must come from MCP-generated lifecycle settings
  for normal MCP calls.
- Lifecycle subprocesses must not inherit MCP stdin.
- Long-running watcher operations remain explicit lifecycle operations rather
  than arbitrary shell commands.

## Repo-Internal References

| Finding | Source Path |
| --- | --- |
| MCP provider status writes generated settings before calling watcher status. | [status.py](agents-remember-md/mcp/src/agents_remember/providers/status.py) |
| MCP provider tools call this module through command capture. | [skill_tools.py](agents-remember-md/mcp/src/agents_remember/controllers/skill_tools.py) |
| Provider setup delegates lifecycle actions to this module. | [provider_setup.py](agents-remember-md/mcp/src/agents_remember/providers/provider_setup.py) |

## Update History

- 2026-05-23T13:46+02:00: Added after lifecycle behavior became package-local MCP code and the source `scripts/` route was removed.
