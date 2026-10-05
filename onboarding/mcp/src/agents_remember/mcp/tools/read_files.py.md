# mcp/src/agents_remember/mcp/tools/read_files.py

## Governing Overview

[overview.md](overview.md)

## Purpose

`read_files.py` is the thin payload builder for the `read_ar_files` tool
(slice 07): it forwards to the application entry point and returns the result through the
shared token choke point.

Builds read_ar_files response payload through existing resolution and token owners.

## Code Commentary

`read_ar_files_payload(config, repo_id, files, refresh=False, *, task_context=None)` first derives
the immutable call-local configuration through `task_scoped_mcp_config_for_reader`. It then calls
`read_ar_files_tool`, where source/onboarding resolution remains, and wraps the dictionary in
`_tool_payload("read_ar_files", ...)` for registered-model validation and token stamping. Task/enclosure
admission belongs to its application owner; batch read, confinement, onboarding lookup, overview dedup
and `read.packet` emission remain the existing reader owner's behavior.

### Role Runtime and Scope

Optional task_context is admitted to a call-local config with task_scoped_mcp_config_for_reader, then forwarded to read_ar_files_tool. Without context the original config is retained. Keep the existing thin-facade/token-stamping description, extending its signature and admission forwarding.

## Invariants And Boundaries

- The payload module stays a thin facade: validation and token stamping happen in
  `_tool_payload`; domain behavior belongs to the application entry point.
- Token fields are stamped by `_tool_payload`, never set here.

## Evidence

### Repo-Internal References

- The application entry point that does the actual resolution. [1]
- The shared choke point that validates the response and stamps tokens. [2]
- The strict response model `read_ar_files` validates against. [3]

### Runtime Source References

- Frozen implementation of read_ar_files_payload supporting the stated file behavior. [4]
- Alternating/concurrent registered base and leaf calls preserve their source/memory roots; wrong repository, canonical contract and malformed pairs refuse. [5]
