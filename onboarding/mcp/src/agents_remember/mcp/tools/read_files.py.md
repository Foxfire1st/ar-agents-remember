# mcp/src/agents_remember/mcp/tools/read_files.py

## Governing Overview

[overview.md](overview.md)

## Purpose

`read_files.py` is the thin payload builder for the `read_ar_files` tool
(slice 07): it forwards to the application entry point and returns the result through the
shared token choke point.

## Code Commentary

`read_ar_files_payload(config, repo_id, files, refresh=False)` calls
`read_ar_files_tool` (the application entry point, where all resolution lives) and wraps its
dict in `_tool_payload("read_ar_files", ...)`, so the response is validated
against its registered model and the token fields are stamped at the one choke
point. The module holds no logic of its own — the batch-read, path-confinement,
onboarding-lookup, front-door-dedup, and `read.packet` behavior all live in the
application entry point.

## Invariants And Boundaries

- The payload module stays a thin facade: validation and token stamping happen in
  `_tool_payload`; domain behavior belongs to the application entry point.
- Token fields are stamped by `_tool_payload`, never set here.

## Evidence

### Repo-Internal References

- The application entry point that does the actual resolution. [1]
- The shared choke point that validates the response and stamps tokens. [2]
- The strict response model `read_ar_files` validates against. [3]
