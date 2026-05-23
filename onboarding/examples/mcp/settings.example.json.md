# settings.example.json

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember-md                         |
| path                   | `examples/mcp/settings.example.json`       |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-05-24T00:37+02:00                     |
| lastVerifiedCommitHash | `ddf6fcd5981664813c915e94e1c5229b542a28a4` |
| lastVerifiedCommitDate | 2026-05-24T00:25:39+02:00                  |
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
`contractPath`, both bounded by MCP config validation. They do not carry source
or memory root path fields: the MCP config derives source roots from
`workspaceRoot/<repo-id>` and external memory roots from
`coordinationRoot/memory-repos/ar-<repo-id>`. Provider entries are empty objects
by design: `agents_remember.mcp.config` rejects provider-local path fields, and
`agents_remember.providers.settings` derives provider lifecycle settings from
the single configured coordination root.

### Invariants And Boundaries

This file must not be placed inside the coordinator root, and it must not carry
duplicated repository or provider runtime paths. If a provider id is present,
the MCP server derives its runner, data, log, requirement, patch, venv, binary,
backend, and watch paths internally. `harnessSkillRoot` is optional and omitted
from the template so normal `.agents/mcp` placement can use the inferred
`.agents/skills` destination.

## Repo-Internal References

| Finding | Citations | Source Path |
| --- | --- | --- |
| MCP config rejects coordinator `system/settings.json` as an authority file and derives provider runtime roots from provider ids. | n/a | [config.py](agents-remember-md/mcp/src/agents_remember/mcp/config.py) |
| Provider lifecycle settings are generated from MCP config instead of read from coordinator settings. | n/a | [settings.py](agents-remember-md/mcp/src/agents_remember/providers/settings.py) |

## Update History

- 2026-05-24T00:37+02:00: Clarified that repository roots are inferred from `workspaceRoot` and `coordinationRoot`, while `harnessSkillRoot` is optional and normally inferred from `.agents/mcp` placement.
- 2026-05-23T05:35+02:00: Created after migrating coordinator provider JSON authority into the MCP settings example.
