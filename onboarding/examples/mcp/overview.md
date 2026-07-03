# examples/mcp Overview

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember                         |
| doc_type               | `route-local-overview`                     |
| sourceRoute            | `examples/mcp`                             |
| lastUpdated            | 2026-07-03T11:50+02:00                     |
| lastVerifiedCommitHash | `38c56316207997da98d8408e1a3ada3c7525f4c6` |
| lastVerifiedCommitDate | 2026-07-03T11:47:48+02:00|

## Purpose

`examples/mcp/` holds the public MCP example/template files: the authority
settings template (`settings.example.json`) and an example memory-layer
coding-guidelines file (`coding-guidelines.example.md`). The settings template
replaces the removed coordinator `system/settings.json` provider example.

## Current Model

`settings.example.json` names one coordination root, one workspace root, allowed
repository ids, allowed provider ids, transcript log root, timeout caps, a
top-level `benchmarksEnabled` flag (defaulting to `false`), and (260703 L2) the
`dashboard` object shipped at its defaults (`autoStart: false`, `port: 8765`) so
dashboard daemon supervision stays opt-in.
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

- 2026-07-03T11:50+02:00 — 260703 L2 route impact: the settings template gains the `dashboard`
  object (autoStart/port, shipped at defaults-off). Verification metadata pinned until closeout
  stamps the code commit.
- 2026-06-11T14:12+02:00: No route impact: the repository rename sweep replaced `agents-remember-md` with `agents-remember` in files on this route; route structure and overview content are unchanged.
- 2026-05-31T12:30+02:00 — Noted new top-level `benchmarksEnabled` flag (default `false`) in `settings.example.json` (1.0.0 review remediation, F2).
