# mcp/src/agents_remember/providers/lifecycle/command_runner.py

## Governing Overview

[Provider Lifecycle Overview](overview.md)

## Purpose

`command_runner.py` owns subprocess execution helpers for provider lifecycle
commands.

## Code Commentary

Absent explicit input routes stdin to DEVNULL; provided text uses subprocess input. Only `allow_timeout=True` turns TimeoutExpired into a timed-out result, preserving partial stdout/stderr and decoding byte output as UTF-8 with replacement. Otherwise the timeout exception remains visible. The nonpositive timeout sentinel is passed as an unlimited wait. cit:([`run_command`; `timeout_command_result`; `timeout_stream_text`], mcp/src/agents_remember/providers/lifecycle/command_runner.py:15-55; mcp/src/agents_remember/providers/lifecycle/command_runner.py:58-74; mcp/src/agents_remember/providers/lifecycle/command_runner.py:77-80).

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

## Evidence

### Repo-Internal References

- Runtime environment defaults come from the lifecycle environment module. [1]
