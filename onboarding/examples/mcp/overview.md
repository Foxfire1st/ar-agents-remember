# examples/mcp Overview

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember-md                         |
| doc_type               | `route-local-overview`                     |
| sourceRoute            | `examples/mcp`                             |
| lastUpdated            | 2026-05-30T21:22+02:00                     |
| lastVerifiedCommitHash | `825a172bdf0d4ee3489ae25dbcc19c4e9c7b9493` |
| lastVerifiedCommitDate | 2026-05-30T17:31:45+02:00                  |

## Purpose

`examples/mcp/` holds the public MCP example/template files: the authority
settings template (`settings.example.json`) and an example memory-layer
coding-guidelines file (`coding-guidelines.example.md`). The settings template
replaces the removed coordinator `system/settings.json` provider example.

## Current Model

`settings.example.json` names one coordination root, one workspace root, allowed
repository ids, allowed provider ids, transcript log root, and timeout caps.
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
