# mcp/src/agents_remember/providers/provider_lifecycle.py

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember-md                         |
| path                   | `mcp/src/agents_remember/providers/provider_lifecycle.py` |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-05-23T20:56+02:00                     |
| lastVerifiedCommitHash | `a6890ae469b70ef045a127fc774d6aa51a54e65a` |
| lastVerifiedCommitDate | 2026-05-23T18:31:48+02:00|
| governingOverview      | `../../../overview.md`                     |

## Purpose

`provider_lifecycle.py` owns the package-local provider lifecycle command
implementation for GrepAI, CodeGraphContext, watcher management, provider
runtime installation, refresh, status, and visualization.

## Code Commentary

### Logic

The module exposes the dev/operator command-style `main(argv)` entrypoint and
the underlying implementation functions for GrepAI, CodeGraphContext, watcher
management, and rendering. MCP provider tools no longer call `main(argv)`
directly; they call the typed service boundary in `lifecycle_service.py`, which
then dispatches to these implementation functions with server-owned settings.

The CLI path still reads lifecycle settings via `--from-settings`, expands
provider runtime layouts, manages provider backends, and builds bounded native
provider commands for GrepAI and CodeGraphContext.

### Invariants And Boundaries

- Provider settings authority must come from MCP-generated lifecycle settings
  for normal MCP calls.
- Lifecycle subprocesses must not inherit MCP stdin.
- Long-running watcher operations remain explicit lifecycle operations rather
  than arbitrary shell commands.
- Do not point MCP controllers at `main(argv)`; use `lifecycle_service.py`.

## Repo-Internal References

| Finding | Source Path |
| --- | --- |
| MCP provider status writes generated settings before calling watcher status. | [status.py](agents-remember-md/mcp/src/agents_remember/providers/status.py) |
| MCP provider tools call the typed lifecycle service, which dispatches to implementation functions in this module. | [lifecycle_service.py](agents-remember-md/mcp/src/agents_remember/providers/lifecycle_service.py) |
| Provider setup delegates lifecycle actions to this module. | [provider_setup.py](agents-remember-md/mcp/src/agents_remember/providers/provider_setup.py) |

## Update History

- 2026-05-23T13:46+02:00: Added after lifecycle behavior became package-local MCP code and the source `scripts/` route was removed.
- 2026-05-23T20:56+02:00: Updated after MCP provider tools moved from `main(argv)` command capture to typed lifecycle service calls.
