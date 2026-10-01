# mcp/src/agents_remember/kernel/primitives/command_capture.py

## Governing Overview

[kernel primitives overview](overview.md)

## Purpose

`kernel/primitives/command_capture.py` (moved from `mcp/command_capture.py` by 260731-EFA-L9) adapts package-local command-style modules into structured
response payloads for the remaining script-facade bridge code.

## Code Commentary

### Logic

`run_package_main()` redirects stdout and stderr while calling an importable
`main(argv)` function. It returns `ok`, `operation`, `returncode`, `argv`,
captured streams, and parsed JSON payload when stdout is JSON. Current MCP
skill application entry points call service functions directly; this helper remains only
where lower-level provider setup still bridges through `lifecycle.main`.

### Invariants And Boundaries

- This helper invokes importable package functions, not arbitrary shell command
  strings.
- It exists only for old behavior that still has command-shaped internals during
  the parity bridge; do not use it as the default application entry point pattern.

## Evidence

### Repo-Internal References

- Provider setup still uses this helper while bridging to the provider lifecycle CLI facade. [1]
- Skill application entry points now call service-backed functions instead of returning command-capture payloads. [2]
