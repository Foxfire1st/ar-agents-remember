# settings.example.json

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember                         |
| path                   | `examples/mcp/settings.example.json`       |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-07-09T14:05+02:00                     |
| lastVerifiedCommitHash | `7bf564a663bb61f12844dee39538dd09a1633cdb` |
| lastVerifiedCommitDate | 2026-08-10T12:28:42+02:00|
| governingOverview      | `overview.md`                              |

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
providers. Repository entries may carry `memorySettingsIncludes` and
`contractPath`, both bounded by MCP config validation. The transcript root
example points at the central MCP log directory under `logs/mcp/`. Repository
entries do not carry source
or memory root path fields: the MCP config derives source roots from
`workspaceRoot/<repo-id>` and external memory roots from
`coordinationRoot/memory-repos/ar-<repo-id>`. Provider entries are empty objects
by design: `agents_remember.mcp.config` rejects provider-local path fields, and
`agents_remember.providers.settings` derives provider lifecycle settings from
the single configured coordination root.

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

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| MCP config rejects coordinator `system/settings.json` as an authority file and derives provider runtime roots from provider ids. | "class McpRuntimeConfig" | mcp/src/agents_remember/kernel/primitives/runtime_config.py:123-123 |
| Provider lifecycle settings are generated from MCP config instead of read from coordinator settings. | "def lifecycle_settings_from_config" | mcp/src/agents_remember/providers/settings.py:32-32 |
| The `providerDegradation` shape shown here validates through the dedicated fail-loud parser (260707-HFX-L7). | "class ProviderDegradationSettings:" | mcp/src/agents_remember/kernel/primitives/provider_degradation_settings.py:37-37 |

## Update History

- 2026-08-05T00:45:16+02:00 — 260731-EFA-L6 S18-B24 curator: replaced the `n/a` rows with exact
  anchors and fixer-generated ranges; exact non-fixing check returns zero findings.

- 2026-07-09T14:05+02:00 — 260707-HFX2-L11 curator correction: the template's `retirement` example
  now documents `autoLandOnIntegration`/`autoLandOnFinalize`, preserving successful chats in the
  landed archive; legacy `autoRetire*` keys are compatibility aliases only. Verification metadata
  pinned until closeout stamps the HFX2-L11 commit.
- 2026-07-08T04:25+02:00 — 260707-HFX-L12 route impact (docs-parity fold-in, master-exit Finding
  2): the template now ships a `retirement` block (`autoRetireOnIntegration`/
  `autoRetireOnFinalize`, both `true`) — the settings object HFX-L8 parsed but left undocumented
  here, closing the parity gap against L7's `providerDegradation` precedent. Verification metadata
  pinned until closeout stamps the HFX-L12 commit.
- 2026-07-08T01:00+02:00 — 260707-HFX-L7 route impact (small): the template now ships a
  representative `providerDegradation` block (`enabled`, `failSafeEnabled`,
  `memoryDegradedRatio`, `memoryCriticalRatio`); the remaining allowed keys take their
  conservative defaults when omitted. Verification metadata pinned until closeout stamps the
  HFX-L7 commit.
- 2026-07-06T22:52+02:00 — 260703-L13 (settings unification): dropped the `orchestration`
  example block (the agentic family's home is the coordinator's global settings file now)
  and the removed `memorySettingsIncludes` key. Verification metadata pinned until closeout
  stamps the L13 commit.

- 2026-07-04T12:32+02:00 — 260703-L4: the template now carries the
  opt-in `orchestration.gateDelegation` shape, shipped at `all-human` defaults
  with no delegated kinds. Verification metadata pinned until closeout stamps
  the L4 commit.
- 2026-07-03T11:45+02:00 — 260703 L2: the template now carries the `dashboard` object
  (`autoStart: false`, `port: 8765` — supervision off by default). Verification metadata pinned
  until closeout stamps the code commit.
- 2026-06-11T14:12+02:00: No content impact: the repository rename sweep replaced `agents-remember-md` with `agents-remember` in the source file; the card already uses the new name and its semantics are unchanged.
- 2026-05-31T12:30+02:00 — Documented the new top-level `benchmarksEnabled` flag (shipped `false`) the template now carries (1.0.0 review remediation).
- 2026-05-30T21:22+02:00: Documented the `timeoutCaps` block (`toolSeconds`, `providerSetupSeconds`) the template now carries — `providerSetupSeconds` caps only provider image build / dependency install, `0` means unlimited, and it replaces the rejected `providerSeconds` key. Realigned verification metadata to `825a172`.
- 2026-05-28T12:32+02:00: Updated after the example transcript root moved from `providers/logs/mcp` to `logs/mcp`.
- 2026-05-24T09:23+02:00: Updated after Codex project-local MCP settings and skills moved from `.agents` to `.codex`.
- 2026-05-24T00:37+02:00: Clarified that repository roots are inferred from `workspaceRoot` and `coordinationRoot`, while `harnessSkillRoot` is optional and normally inferred from harness-local MCP settings placement.
- 2026-05-23T05:35+02:00: Created after migrating coordinator provider JSON authority into the MCP settings example.
