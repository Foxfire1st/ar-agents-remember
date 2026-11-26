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
optionally sets `transcriptRoot`, and names allowed repositories. Repository entries may carry `certificationProfile` (CCR-R22@v1, L22, commit `685f83c44055`):
the example sets `repositories.agents-remember.certificationProfile` to
`mcp/certification-profile-v1.json`, the repository-relative authority the quality gate admits
before any code commit.

The example also carries a `timeoutCaps` block illustrating `toolSeconds` (`30`, with `0` meaning unlimited). `parse_timeout_caps` admits only `toolSeconds`, ignores retired `providerSetupSeconds` (reporting it in `unused_settings_keys`), and rejects unknown keys.

The example also carries a top-level `benchmarksEnabled` flag, shipped as
`false`, which gates the optional benchmarking surface off by default.

The `dashboard` object (260703 L2) ships `{"autoStart": false, "port": 8765}` —
the defaults, so dashboard daemon supervision stays off until a user opts in;
`agents_remember.mcp.config` fail-loud rejects unknown `dashboard` keys the same
way `timeoutCaps` does.

The template illustrates a `retirement` object (`autoLandOnIntegration`, `autoLandOnFinalize`, `autoCloseCompletedSeats`), which `runtime_config.py` lists in `UNUSED_SETTINGS_SECTIONS` so it loads unread and is reported in `unused_settings_keys`.

The template also shows the optional `toolLog` object (MIK-R108 rule 3):
`{"keepDays": 14, "maxBytes": 268435456, "enclosureMaxBytes": 67108864}` — the coordination-root
keeping and the two log-folder byte budgets, each documented in the settings reference.

### Invariants And Boundaries

This file must not be placed inside the coordinator root, and it must not carry
duplicated repository runtime paths. `harnessSkillRoot` is optional and omitted
from the template so normal Codex `.codex/mcp` placement can use the inferred
`.codex/skills` destination.

## Evidence

### Repo-Internal References

- MCP config rejects coordinator `system/settings.json` as an authority file and derives provider runtime roots from provider ids. [1]
