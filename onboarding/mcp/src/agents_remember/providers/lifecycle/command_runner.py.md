# mcp/src/agents_remember/providers/lifecycle/command_runner.py

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember-md                         |
| path                   | `mcp/src/agents_remember/providers/lifecycle/command_runner.py` |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-05-29T18:35+02:00|
| lastVerifiedCommitHash | `01f503dcba3a6eacc1587941f6a89fce0bcc72a2` |
| lastVerifiedCommitDate | 2026-05-29T18:32:57+02:00|
| governingOverview      | `overview.md`                              |

## Governing Overview

[Provider Lifecycle Overview](overview.md)

## Purpose

`command_runner.py` owns subprocess execution helpers for provider lifecycle
commands.

## Code Commentary

### Logic

The module runs bounded captured commands, converts timeout exceptions into
structured command dictionaries when allowed, runs foreground commands, and
starts detached long-running processes with host-appropriate process flags.

### Invariants And Boundaries

- Command execution must set UTF-8 subprocess environment defaults.
- Detached starts must not inherit MCP stdin or command lifetime.
- Provider policy belongs in provider modules, not in this adapter.

## Repo-Internal References

| Finding | Source Path |
| --- | --- |
| Runtime environment defaults come from the lifecycle environment module. | [runtime_environment.py](agents-remember-md/mcp/src/agents_remember/providers/lifecycle/runtime_environment.py) |
| CGC process lifecycle uses detached and foreground command helpers. | [process.py](agents-remember-md/mcp/src/agents_remember/providers/cgc/lifecycle/process.py) |

## Update History

- 2026-05-29T18:35+02:00: `popen_detached_command` returns `Popen[bytes]` via an explicit `cast` (the `**popen_kwargs` spread defeated overload selection); behavior-preserving (commit `0549b28`).
- 2026-05-25T21:14+02:00: Created from the command execution portion of the former shared lifecycle common module.
