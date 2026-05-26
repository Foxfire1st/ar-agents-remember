# mcp/src/agents_remember/providers/lifecycle/command_runner.py

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember-md                         |
| path                   | `mcp/src/agents_remember/providers/lifecycle/command_runner.py` |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-05-25T21:14+02:00                     |
| lastVerifiedCommitHash | `c310611a6678051c9e37b912c522b367530c0686` |
| lastVerifiedCommitDate | 2026-05-26T02:17:03+02:00|
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

- 2026-05-25T21:14+02:00: Created from the command execution portion of the former shared lifecycle common module.
