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
captured streams, and parsed JSON payload when stdout is JSON. The skill-application entry routes described by the older card were removed in this leaf. The retained helper’s provider-setup account applies where setup bridges through `lifecycle.main`; it does not establish a current public skill-application endpoint.

### Invariants And Boundaries

- This helper invokes importable package functions, not arbitrary shell command
  strings.
- It exists only for old behavior that still has command-shaped internals during
  the parity bridge; do not use it as the default application entry point pattern.

## Evidence

### Repo-Internal References

- Provider setup invokes run_package_main with lifecycle.main and constructed arguments. [1]
