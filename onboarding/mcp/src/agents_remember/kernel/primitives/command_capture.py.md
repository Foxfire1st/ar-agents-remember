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
skill application entry points call service functions directly. The retained
`setup_common.run_lifecycle` caller passes `main=lifecycle.main` to this helper,
but the current lifecycle facade exports no CLI/main and has no package-execution
entrypoint. That attempted call is a retained caller inconsistency, not an
available lifecycle CLI bridge or evidence of successful provider execution.

### Invariants And Boundaries

- This helper invokes importable package functions, not arbitrary shell command
  strings.
- It exists only for old behavior that still has command-shaped internals during
  the parity bridge; do not use it as the default application entry point pattern.

## Evidence

### Repo-Internal References

- The retained provider caller requests `lifecycle.main`, but the current facade has no CLI/main export; this helper still captures an explicitly supplied callable and does not establish a working provider CLI bridge. [1]

- Skill application no longer goes through this helper — skills are the package copy the server serves — and the surviving caller is `setup_common.run_lifecycle`, which passes `main=lifecycle.main`. [2]
