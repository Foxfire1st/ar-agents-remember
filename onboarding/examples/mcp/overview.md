# examples/mcp Overview

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| sourceRoute            | `examples/mcp`                             |

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
The `agents-remember` repository entry now explicitly selects
`certificationProfile: "mcp/certification-profile-v1.json"` beside `contractPath: null`.
This is an authority-settings reference to the checked-in profile, not an alternate executor.
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

The historical L9 edit renamed its layer heading from `### Controller` to
`### Application entry point` (and anti-pattern 7's wording with it), mirroring the
`controllers/` → `application/` package move in the repo; the file remains
documentation-shaped example content, not a runtime input.
That historical heading-only scope does not describe later changes: CCR subsequently added
the repository certification-profile reference described above.
