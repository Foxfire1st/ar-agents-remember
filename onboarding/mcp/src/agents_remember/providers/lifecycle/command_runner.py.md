# mcp/src/agents_remember/providers/lifecycle/command_runner.py

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember                         |
| path                   | `mcp/src/agents_remember/providers/lifecycle/command_runner.py` |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-07-31T00:00+02:00|
| lastVerifiedCommitHash | `f3115ce8603f83b7b5cbd82aa402f66ec1d8a29d` |
| lastVerifiedCommitDate | 2026-07-31T19:28:50+02:00|
| governingOverview      | `overview.md`                              |

## Governing Overview

[Provider Lifecycle Overview](overview.md)

## Purpose

`command_runner.py` owns subprocess execution helpers for provider lifecycle
commands.

## Code Commentary

### 260731-EFA-L2 The `env` Parameter Was Removed

`run_command(command, *, cwd, stdin_text=None, timeout=60, allow_timeout=False)` no longer accepts
an `env` override. Provider commands always run under the sanitized provider environment, and no
caller ever supplied its own, so the body now calls `subprocess_env(None)` directly with a comment
recording why. This is a **contract narrowing**: a caller that wants a different environment can no
longer get one through this seam, and adding that back means deciding deliberately rather than
inheriting a dead parameter.

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

| Finding | Anchor | Source |
| --- | --- | --- |
| Runtime environment defaults come from the lifecycle environment module. | `subprocess_env` | mcp/src/agents_remember/providers/lifecycle/runtime_environment.py:17-23 |

## Update History

- 2026-08-04T18:44+02:00 — 260731-EFA-L6 S18-B17 curator: repaired the single malformed row —
  bound to `subprocess_env` (runtime_environment.py:10-29), the env-default provider this module
  imports and calls unconditionally. Claim wording unchanged.
- 2026-07-31T00:00+02:00 — 260731-EFA-L2 (gate honesty, `PLR0913` armed with no exemptions):
  dropped `run_command`'s unused `env` parameter; the sanitized provider environment
  (`subprocess_env(None)`) is now unconditional. No caller changed. Verification metadata pinned
  until closeout stamps the L2 commit.
- 2026-05-31T12:30+02:00 — Removed the now-deleted `run_foreground_command` and `popen_detached_command` helpers from Logic, dropped the detached-stdin/lifetime invariant, and removed the stale CGC `process.py` reference (1.0.0 review remediation).
- 2026-05-30T21:33+02:00: Documented the `UNLIMITED_TIMEOUT = 0` sentinel and the `timeout<=0 → None` (uncapped) subprocess behavior added in the never-cap-indexing run; added the never-cap invariant. Verified against `825a172`.
- 2026-05-29T18:35+02:00: `popen_detached_command` returns `Popen[bytes]` via an explicit `cast` (the `**popen_kwargs` spread defeated overload selection); behavior-preserving (commit `0549b28`).
- 2026-05-25T21:14+02:00: Created from the command execution portion of the former shared lifecycle common module.
