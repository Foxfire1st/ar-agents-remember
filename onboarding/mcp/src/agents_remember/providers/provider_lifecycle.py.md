# mcp/src/agents_remember/providers/provider_lifecycle.py

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember-md                         |
| path                   | `mcp/src/agents_remember/providers/provider_lifecycle.py` |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-05-25T15:12+02:00                     |
| lastVerifiedCommitHash | `a8ee8440dfa920d1153a4bb4bb43cc77534c3c90` |
| lastVerifiedCommitDate | 2026-05-25T15:22:52+02:00|
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

Bounded provider commands still use `run_command()` and its timeout handling,
but continuous provider processes use detached `Popen` startup. CGC watcher
startup launches `cgc watch` through the shared detached helper and records the
managed PID/log file. GrepAI watcher startup launches native
`grepai watch --background` through the same detached helper, performs only a
short non-killing readiness probe, and records `startupPending` when the
launcher is still alive but native status has not reported ready yet.

GrepAI watcher status, stop, and refresh command shapes include the managed
`--log-dir`; status parsing accepts GrepAI's `Workspace <name>: running`
output. This keeps lifecycle state aligned with the watcher instance that was
actually started under the managed provider log directory.

### Invariants And Boundaries

- Provider settings authority must come from MCP-generated lifecycle settings
  for normal MCP calls.
- Lifecycle subprocesses must not inherit MCP stdin.
- Lifecycle timeout wrappers must not own or kill continuous watcher/server
  processes after startup.
- Long-running watcher operations remain explicit lifecycle operations rather
  than arbitrary shell commands.
- GrepAI native watch control commands must use the same managed `--log-dir`
  for start, status, stop, and refresh paths.
- Do not point MCP controllers at `main(argv)`; use `lifecycle_service.py`.

## Repo-Internal References

| Finding | Source Path |
| --- | --- |
| MCP provider status writes generated settings before calling watcher status. | [status.py](agents-remember-md/mcp/src/agents_remember/providers/status.py) |
| MCP provider tools call the typed lifecycle service, which dispatches to implementation functions in this module. | [lifecycle_service.py](agents-remember-md/mcp/src/agents_remember/providers/lifecycle_service.py) |
| Provider setup delegates lifecycle actions to this module. | [provider_setup.py](agents-remember-md/mcp/src/agents_remember/providers/provider_setup.py) |
| Provider lifecycle tests protect detached GrepAI startup, managed log-dir status probing, and already-running watcher adoption. | [test_provider_lifecycle.py](agents-remember-md/mcp/tests/test_provider_lifecycle.py) |

## Update History

- 2026-05-25T15:12+02:00: Updated after watcher startup was moved to detached non-killing `Popen`, CGC watcher startup reused the detached helper, and GrepAI status/stop probes were aligned with the managed log directory.
- 2026-05-23T20:56+02:00: Updated after MCP provider tools moved from `main(argv)` command capture to typed lifecycle service calls.
- 2026-05-23T13:46+02:00: Added after lifecycle behavior became package-local MCP code and the source `scripts/` route was removed.
