# examples/mcp Overview

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember                         |
| doc_type               | `route-local-overview`                     |
| sourceRoute            | `examples/mcp`                             |
| lastUpdated            | 2026-08-10T07:30+02:00                     |
| lastVerifiedCommitHash | `5aff1e8f01dfa949efc8f68e46bc62a99ed31432` |
| lastVerifiedCommitDate | 2026-08-14T14:36:50+02:00|

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
Since 260707-HFX-L7 the template also carries a `providerDegradation` object
(`enabled: true`, `failSafeEnabled: true`, `memoryDegradedRatio: 0.8`,
`memoryCriticalRatio: 0.92`) — a conservative-default illustration of the
degradation-detector thresholds parsed by `mcp/provider_degradation_settings.py`
(the healthy/degraded/critical state machine over the L1/L2 provider metrics
store). Shipping it enabled-by-default in the example (unlike `dashboard`,
which ships opt-in) matches the requirement that the critical-threshold
failsafe defaults ON at a conservative bound.

The template's `retirement` object now carries `autoLandOnIntegration: true`,
`autoLandOnFinalize: true`, and `autoCloseCompletedSeats: true`. The first two are completion-edge
gates; the third selects default report-gated retirement for exact-leaf worker/reviewer/curator
seats. Setting it false restores landed/archive behavior. Manager/orchestrator owners are never
automatic targets. The parser still accepts the older `autoRetire*` edge names as compatibility
aliases, while the example uses only the current keys.

`coding-guidelines.example.md` is an example `system/coding-guidelines.md` body
that teams can adapt for a memory repo. It is documentation-shaped example
content, not a runtime input.

In this leaf the example renamed its layer heading from `### Controller` to
`### Application entry point` (and anti-pattern 7's wording with it), mirroring the
`controllers/` → `application/` package move in the repo; the file remains
documentation-shaped example content, not a runtime input.
The staged L9 example edit remains confined to that documentation-shaped heading/prose rename;
the settings template and runtime-facing example shape are unchanged.

## Update History

- 2026-08-10T13:00+02:00 — 260731-EFA-L9 curator: route impact: re-read the examples/mcp body
  against the staged example change; the route body records the rename and confirms the settings
  template is unchanged. Verification metadata remains pinned until closeout.

- 2026-08-10T07:30+02:00 — 260805-ARG-L1: the authority example now ships
  `autoCloseCompletedSeats:true` with both existing edge gates.

- 2026-08-05T03:47+02:00 — 260731-EFA-L6 route impact: the coding-guidelines example renamed its
  `Controller` layer heading (and anti-pattern 7) to `Application entry point` to mirror the
  `controllers/` → `application/` move; `settings.example.json` is unchanged. Verification
  metadata pinned until closeout stamps the code commit.
- 2026-07-09T14:05+02:00 — 260707-HFX2-L11 route impact: the settings template's `retirement`
  example now shows `autoLandOnIntegration`/`autoLandOnFinalize`, matching landed archive behavior;
  old `autoRetire*` names remain parser aliases only. Verification metadata pinned until closeout
  stamps the HFX2-L11 commit.

- 2026-07-08T04:25+02:00 — 260707-HFX-L12 route impact (docs-parity fold-in, master-exit Finding
  2): the settings template gains the `retirement` block
  (`autoRetireOnIntegration`/`autoRetireOnFinalize`, both `true`), closing the parity gap between
  HFX-L8 (which parsed the setting) and its docs (which never shipped it, unlike L7's
  `providerDegradation`). Verification metadata pinned until closeout stamps the HFX-L12 commit.

- 2026-07-08T01:35+02:00 — 260707-HFX-L7 route impact: the settings template gains the
  `providerDegradation` block (enabled/failSafeEnabled/memoryDegradedRatio/memoryCriticalRatio)
  illustrating the new provider degradation detector's settings surface, shipped enabled-by-default
  matching the conservative-default critical failsafe requirement. Verification metadata pinned
  until closeout stamps the HFX-L7 commit.

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
