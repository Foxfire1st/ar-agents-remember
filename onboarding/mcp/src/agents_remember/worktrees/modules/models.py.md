# mcp/src/agents_remember/worktrees/modules/models.py

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember-md                         |
| path                   | `mcp/src/agents_remember/worktrees/modules/models.py` |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-05-25T20:41+02:00                     |
| lastVerifiedCommitHash | `c310611a6678051c9e37b912c522b367530c0686` |
| lastVerifiedCommitDate | 2026-05-26T02:17:03+02:00|
| governingOverview      | `overview.md`                              |

## Purpose

Defines shared dataclasses used by the worktree lifecycle modules.

## Code Commentary

`WorktreeCommandResult` is the result envelope consumed by MCP controllers and
CLI adapters. `WorktreeProviderSetupConfig` carries MCP-derived provider setup
roots into worktree start preparation without rebuilding CLI arguments.

## Docs References

No external Domain Documentation source is configured for this memory repo.

## Repo-Internal References

| Finding | Source Path |
| --- | --- |
| MCP skill tools type result envelopes and provider setup config through this facade-exported model. | [skill_tools.py](agents-remember-md/mcp/src/agents_remember/controllers/skill_tools.py) |

## Update History

- 2026-05-25T20:41+02:00: Created during worktree manager module extraction.
