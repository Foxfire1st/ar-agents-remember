# examples/mcp Overview

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember                         |
| doc_type               | `route-local-overview`                     |
| sourceRoute            | `examples/mcp`                             |
| lastUpdated            | 2026-07-06T23:06+02:00                     |
| lastVerifiedCommitHash | `9d58058e3ce4815b0356794fc21973ebe9c71345` |
| lastVerifiedCommitDate | 2026-07-06T11:47:10+02:00|

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
dashboard daemon supervision stays opt-in. Since 260703-L13 the template
carries NO `orchestration` block and no `memorySettingsIncludes` key: the
agentic family (including gateDelegation) lives in the global agentic settings
file (`docs/reference/settings-json.md`, Agentic Settings), and the dead
includes plumbing was removed.
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

- 2026-07-06T23:06+02:00 — 260703-L13 route impact: the settings template drops the L4
  `orchestration.gateDelegation` block (moved to the global agentic settings file; the
  authority-file value is only a warned one-cycle legacy fallback) and the removed
  `memorySettingsIncludes` key. Verification metadata pinned until closeout stamps the L13
  commit.

- 2026-07-06T12:10+02:00 — No route impact: reviewed during the 260703-L10 one-vocabulary sweep — the settings/guideline examples carry no lifecycle vocabulary at all, so nothing changed on this route.
- 2026-07-04T12:32+02:00 — 260703-L4 route impact: the settings template gains
  the opt-in `orchestration.gateDelegation` shape, shipped as all-human by
  default. Verification metadata pinned until closeout stamps the L4 commit.
- 2026-07-03T11:50+02:00 — 260703 L2 route impact: the settings template gains the `dashboard`
  object (autoStart/port, shipped at defaults-off). Verification metadata pinned until closeout
  stamps the code commit.
- 2026-06-11T14:12+02:00: No route impact: the repository rename sweep replaced `agents-remember-md` with `agents-remember` in files on this route; route structure and overview content are unchanged.
- 2026-05-31T12:30+02:00 — Noted new top-level `benchmarksEnabled` flag (default `false`) in `settings.example.json` (1.0.0 review remediation, F2).
