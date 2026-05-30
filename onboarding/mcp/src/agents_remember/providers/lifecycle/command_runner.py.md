# mcp/src/agents_remember/providers/lifecycle/command_runner.py

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember-md                         |
| path                   | `mcp/src/agents_remember/providers/lifecycle/command_runner.py` |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-05-30T21:33+02:00|
| lastVerifiedCommitHash | `825a172bdf0d4ee3489ae25dbcc19c4e9c7b9493` |
| lastVerifiedCommitDate | 2026-05-30T17:31:45+02:00|
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

It defines the `UNLIMITED_TIMEOUT = 0` sentinel: any `timeout <= 0` is passed to
the subprocess as `None`, i.e. uncapped. This is the primitive the never-cap
policy builds on — provider indexing, CGC seed export/load, and GrepAI clone
pass `UNLIMITED_TIMEOUT`/`None` so long index operations are never killed by a
wall-clock cap, while setup/control commands still pass a real timeout.

### Invariants And Boundaries

- Command execution must set UTF-8 subprocess environment defaults.
- Detached starts must not inherit MCP stdin or command lifetime.
- Provider policy belongs in provider modules, not in this adapter.
- Keep `UNLIMITED_TIMEOUT`/`timeout<=0 → None` semantics intact: indexing, seed,
  and clone rely on never being time-capped. Capping them is a regression.

## Repo-Internal References

| Finding | Source Path |
| --- | --- |
| Runtime environment defaults come from the lifecycle environment module. | [runtime_environment.py](agents-remember-md/mcp/src/agents_remember/providers/lifecycle/runtime_environment.py) |
| CGC process lifecycle uses detached and foreground command helpers. | [process.py](agents-remember-md/mcp/src/agents_remember/providers/cgc/lifecycle/process.py) |

## Update History

- 2026-05-30T21:33+02:00: Documented the `UNLIMITED_TIMEOUT = 0` sentinel and the `timeout<=0 → None` (uncapped) subprocess behavior added in the never-cap-indexing run; added the never-cap invariant. Verified against `825a172`.
- 2026-05-29T18:35+02:00: `popen_detached_command` returns `Popen[bytes]` via an explicit `cast` (the `**popen_kwargs` spread defeated overload selection); behavior-preserving (commit `0549b28`).
- 2026-05-25T21:14+02:00: Created from the command execution portion of the former shared lifecycle common module.
