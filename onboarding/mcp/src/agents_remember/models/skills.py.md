# mcp/src/agents_remember/models/skills.py

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember-md                         |
| path                   | `mcp/src/agents_remember/models/skills.py` |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-05-28T19:52+02:00                     |
| lastVerifiedCommitHash | `bf3a3c4e310fb11032da885083d026a74a31ee9c` |
| lastVerifiedCommitDate | 2026-05-28T20:06:49+02:00|
| governingOverview      | `overview.md`                              |

## Purpose

`skills.py` defines the response model for the `skills_install` MCP tool.

## Code Commentary

`SkillsInstallResponse` exposes dry-run/layout/install-root facts plus planned,
installed, removed, and archived path lists while allowing installer-specific
fields to pass through during service evolution.

## Invariants And Boundaries

- Skill installation reports are modeled but intentionally flexible around
  installer detail fields.
- Copy/archive semantics remain owned by the install service and controller.

## Repo-Internal References

| Finding | Source Path |
| --- | --- |
| The skills install controller delegates to package install services. | [skill_tools.py](agents-remember-md/mcp/src/agents_remember/controllers/skill_tools.py) |

## Update History

- 2026-05-28T19:52+02:00: Created for the skill-install response contract.
