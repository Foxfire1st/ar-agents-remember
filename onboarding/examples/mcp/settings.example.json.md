# settings.example.json

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember-md                         |
| path                   | `examples/mcp/settings.example.json`       |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-05-23T05:35+02:00                     |
| lastVerifiedCommitHash | `7ab4b520b9178a31c4a5f5f8a5393b9b6ba82e0e` |
| lastVerifiedCommitDate | 2026-05-23T00:34:51+02:00                  |
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
`contractPath`, both bounded by MCP config validation. Provider entries are
empty objects by design: `agents_remember.mcp.config` rejects provider-local
path fields, and `agents_remember.providers.settings` derives provider
lifecycle settings from the single configured coordination root.

### Invariants And Boundaries

This file must not be placed inside the coordinator root, and it must not carry
duplicated provider runtime paths. If a provider id is present, the MCP server
derives its runner, data, log, requirement, patch, venv, binary, backend, and
watch paths internally.

## Repo-Internal References

| Finding | Citations | Source Path |
| --- | --- | --- |
| MCP config rejects coordinator `system/settings.json` as an authority file and derives provider runtime roots from provider ids. | n/a | [config.py](agents-remember-md/mcp/src/agents_remember/mcp/config.py) |
| Provider lifecycle settings are generated from MCP config instead of read from coordinator settings. | n/a | [settings.py](agents-remember-md/mcp/src/agents_remember/providers/settings.py) |

## Update History

- 2026-05-23T05:35+02:00: Created after migrating coordinator provider JSON authority into the MCP settings example.

