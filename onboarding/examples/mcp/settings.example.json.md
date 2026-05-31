# settings.example.json

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember-md                         |
| path                   | `examples/mcp/settings.example.json`       |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-05-31T12:30+02:00                     |
| lastVerifiedCommitHash | `c20a3292e667d227a3be0c1fb276f8a701df814f` |
| lastVerifiedCommitDate | 2026-05-31T14:17:11+02:00|
| governingOverview      | `overview.md`                              |

## Governing Overview

[overview.md](overview.md)

## Purpose

`settings.example.json` is the public MCP settings template. It is the
machine-readable authority shape for the MCP server and replaces the old
coordinator `system/settings.json` provider template.

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

### Invariants And Boundaries

This file must not be placed inside the coordinator root, and it must not carry
duplicated repository or provider runtime paths. If a provider id is present,
the MCP server derives its runner, data, log, requirement, patch, venv, binary,
backend, and watch paths internally. `harnessSkillRoot` is optional and omitted
from the template so normal Codex `.codex/mcp` placement can use the inferred
`.codex/skills` destination.

## Repo-Internal References

| Finding | Citations | Source Path |
| --- | --- | --- |
| MCP config rejects coordinator `system/settings.json` as an authority file and derives provider runtime roots from provider ids. | n/a | [config.py](agents-remember-md/mcp/src/agents_remember/mcp/config.py) |
| Provider lifecycle settings are generated from MCP config instead of read from coordinator settings. | n/a | [settings.py](agents-remember-md/mcp/src/agents_remember/providers/settings.py) |

## Update History

- 2026-05-31T12:30+02:00 — Documented the new top-level `benchmarksEnabled` flag (shipped `false`) the template now carries (1.0.0 review remediation).
- 2026-05-30T21:22+02:00: Documented the `timeoutCaps` block (`toolSeconds`, `providerSetupSeconds`) the template now carries — `providerSetupSeconds` caps only provider image build / dependency install, `0` means unlimited, and it replaces the rejected `providerSeconds` key. Realigned verification metadata to `825a172`.
- 2026-05-28T12:32+02:00: Updated after the example transcript root moved from `providers/logs/mcp` to `logs/mcp`.
- 2026-05-24T09:23+02:00: Updated after Codex project-local MCP settings and skills moved from `.agents` to `.codex`.
- 2026-05-24T00:37+02:00: Clarified that repository roots are inferred from `workspaceRoot` and `coordinationRoot`, while `harnessSkillRoot` is optional and normally inferred from harness-local MCP settings placement.
- 2026-05-23T05:35+02:00: Created after migrating coordinator provider JSON authority into the MCP settings example.
