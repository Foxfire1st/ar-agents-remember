# mcp/src/agents_remember/providers/lifecycle/runtime_environment.py

## Governing Overview

[Provider Lifecycle Overview](overview.md)

## Purpose

`runtime_environment.py` defines retained provider lifecycle environment helpers.
The removed CLI no longer uses its root/stdio defaults; command execution still uses `subprocess_env`.

## Code Commentary

### Logic

The module infers the coordination root from the installed package
location, configures stdout/stderr for UTF-8, and builds subprocess
environments that force UTF-8 Python IO.

### Invariants And Boundaries

- Environment helpers are provider-agnostic.
- Command execution belongs in `command_runner.py`; this module only supplies
  environment defaults.

## Evidence

### Repo-Internal References


- Command execution uses the subprocess environment helper. [2]
