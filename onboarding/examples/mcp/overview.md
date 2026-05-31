# examples/mcp Overview

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember-md                         |
| doc_type               | `route-local-overview`                     |
| sourceRoute            | `examples/mcp`                             |
| lastUpdated            | 2026-05-31T12:30+02:00                     |
| lastVerifiedCommitHash | `c20a3292e667d227a3be0c1fb276f8a701df814f` |
| lastVerifiedCommitDate | 2026-05-31T14:17:11+02:00|

## Purpose

`examples/mcp/` holds the public MCP example/template files: the authority
settings template (`settings.example.json`) and an example memory-layer
coding-guidelines file (`coding-guidelines.example.md`). The settings template
replaces the removed coordinator `system/settings.json` provider example.

## Current Model

`settings.example.json` names one coordination root, one workspace root, allowed
repository ids, allowed provider ids, transcript log root, timeout caps, and a
top-level `benchmarksEnabled` flag (defaulting to `false`).
Repository source roots are derived from `workspaceRoot/<repo-id>`, and external
memory roots are derived from `coordinationRoot/memory-repos/ar-<repo-id>`.
Provider entries stay empty because the MCP server derives provider runtime
roots, data roots, central logs, Docker backends, and watch settings internally.
The `timeoutCaps` block uses `toolSeconds` and `providerSetupSeconds` (the
renamed `providerSeconds`); `providerSetupSeconds` caps only provider image
build / dependency install, never indexing.

`coding-guidelines.example.md` is an example `system/coding-guidelines.md` body
that teams can adapt for a memory repo. It is documentation-shaped example
content, not a runtime input.

## Update History

- 2026-05-31T12:30+02:00 — Noted new top-level `benchmarksEnabled` flag (default `false`) in `settings.example.json` (1.0.0 review remediation, F2).
