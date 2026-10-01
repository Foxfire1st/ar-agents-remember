# settings.example.json

## Governing Overview

[overview.md](overview.md)

## Purpose

`settings.example.json` is the public MCP settings template. It is the
machine-readable authority shape for the MCP server and replaces the old
coordinator `system/settings.json` provider template. Since 260703-L13 it
carries NO `orchestration` block (gateDelegation moved to the global agentic
settings file; an authority-file value is only a warned one-cycle legacy
fallback) and no `memorySettingsIncludes` key (dead plumbing removed).

## Code Commentary

### Logic

The file requires absolute `coordinationRoot` and `workspaceRoot` values,
optionally sets `transcriptRoot`, names allowed repositories, and names allowed
providers. Repository entries may carry `certificationProfile` (CCR-R22@v1, L22, commit `685f83c44055`):
the example sets `repositories.agents-remember.certificationProfile` to
`mcp/certification-profile-v1.json`, the repository-relative authority the quality gate admits
before any code commit. Repository entries may (historically) carry `memorySettingsIncludes` and

The example also carries a `timeoutCaps` block with `toolSeconds` and
`providerSetupSeconds`. `providerSetupSeconds` caps only provider **image build
/ dependency install**; database seed, clone, and indexing are never time-capped.
A cap value of `0` means unlimited. This key was renamed from the old
`providerSeconds`; `agents_remember.mcp.config` fail-loud rejects the old name
with a `ConfigError`, so the template ships the current key.

The example also carries a top-level `benchmarksEnabled` flag, shipped as
`false`, which gates the optional benchmarking surface off by default.

The `dashboard` object (260703 L2) ships `{"autoStart": false, "port": 8765}` —
the defaults, so dashboard daemon supervision stays off until a user opts in;
`agents_remember.mcp.config` fail-loud rejects unknown `dashboard` keys the same
way `timeoutCaps` does.

The template also shows the optional `orchestration.gateDelegation` object
(260703-L4). It is shipped as `policy: "all-human"` with empty `kinds`, so
delegated approvals remain opt-in. Operators can switch to a built-in delegated
policy or add per-kind role entries in real settings files; config validation
rejects unsupported or human-pinned delegation.

The template also ships a `providerDegradation` object (260707-HFX-L7):
`{"enabled": true, "failSafeEnabled": true, "memoryDegradedRatio": 0.8, "memoryCriticalRatio": 0.92}`
— a representative subset of the full 15-key `providerDegradation` shape (the remaining keys take
their conservative defaults when omitted: sample-count thresholds, watcher-lag commit/minute
pairs, probe-latency pair, setup-failure-streak pair, and `recentSampleLimit`). This is the
provider-only degradation detector's settings surface; `agents_remember.mcp.provider_degradation_settings`
fail-loud rejects unknown keys and wrong per-field shapes the same way `timeoutCaps`/`dashboard`
do.

The template also ships a `retirement` object (260707-HFX2-L11):
`{"autoLandOnIntegration": true, "autoLandOnFinalize": true}` — both flags default `true`, unlike
`dashboard`'s off-by-default posture, because successful completion should preserve spent chats in
the landed archive automatically. `agents_remember.mcp.config`'s `parse_retirement_settings`
fail-loud rejects unknown `retirement` keys and non-boolean values for either known field the same
way `timeoutCaps`/`dashboard`/`providerDegradation` do, while still accepting the old
`autoRetireOnIntegration`/`autoRetireOnFinalize` spellings as compatibility aliases. The template
uses the current `autoLand*` keys so new settings files do not teach completion-edge termination.

### Invariants And Boundaries

This file must not be placed inside the coordinator root, and it must not carry
duplicated repository or provider runtime paths. If a provider id is present,
the MCP server derives its runner, data, log, requirement, patch, venv, binary,
backend, and watch paths internally. `harnessSkillRoot` is optional and omitted
from the template so normal Codex `.codex/mcp` placement can use the inferred
`.codex/skills` destination.

## Evidence

### Repo-Internal References

- MCP config rejects coordinator `system/settings.json` as an authority file and derives provider runtime roots from provider ids. [1]
- Provider lifecycle settings are generated from MCP config instead of read from coordinator settings. [2]
- The `providerDegradation` shape shown here validates through the dedicated fail-loud parser (260707-HFX-L7). [3]
