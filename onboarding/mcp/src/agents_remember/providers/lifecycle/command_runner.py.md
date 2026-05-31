# mcp/src/agents_remember/providers/lifecycle/command_runner.py

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember-md                         |
| path                   | `mcp/src/agents_remember/providers/lifecycle/command_runner.py` |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-05-31T12:30+02:00|
| lastVerifiedCommitHash | `c20a3292e667d227a3be0c1fb276f8a701df814f` |
| lastVerifiedCommitDate | 2026-05-31T14:17:11+02:00|
| governingOverview      | `overview.md`                              |

## Governing Overview

[Provider Lifecycle Overview](overview.md)

## Purpose

`command_runner.py` owns subprocess execution helpers for provider lifecycle
commands.

## Code Commentary

### Logic

The module runs bounded captured commands and converts timeout exceptions into
structured command dictionaries when allowed.

It defines the `UNLIMITED_TIMEOUT = 0` sentinel: any `timeout <= 0` is passed to
the subprocess as `None`, i.e. uncapped. This is the primitive the never-cap
policy builds on — provider indexing, CGC seed export/load, and GrepAI clone
pass `UNLIMITED_TIMEOUT`/`None` so long index operations are never killed by a
wall-clock cap, while setup/control commands still pass a real timeout.

### Invariants And Boundaries

- Command execution must set UTF-8 subprocess environment defaults.
- Provider policy belongs in provider modules, not in this adapter.
- Keep `UNLIMITED_TIMEOUT`/`timeout<=0 → None` semantics intact: indexing, seed,
  and clone rely on never being time-capped. Capping them is a regression.

## Repo-Internal References

| Finding | Source Path |
| --- | --- |
| Runtime environment defaults come from the lifecycle environment module. | [runtime_environment.py](agents-remember-md/mcp/src/agents_remember/providers/lifecycle/runtime_environment.py) |

## Update History

- 2026-05-31T12:30+02:00 — Removed the now-deleted `run_foreground_command` and `popen_detached_command` helpers from Logic, dropped the detached-stdin/lifetime invariant, and removed the stale CGC `process.py` reference (1.0.0 review remediation).
- 2026-05-30T21:33+02:00: Documented the `UNLIMITED_TIMEOUT = 0` sentinel and the `timeout<=0 → None` (uncapped) subprocess behavior added in the never-cap-indexing run; added the never-cap invariant. Verified against `825a172`.
- 2026-05-29T18:35+02:00: `popen_detached_command` returns `Popen[bytes]` via an explicit `cast` (the `**popen_kwargs` spread defeated overload selection); behavior-preserving (commit `0549b28`).
- 2026-05-25T21:14+02:00: Created from the command execution portion of the former shared lifecycle common module.
