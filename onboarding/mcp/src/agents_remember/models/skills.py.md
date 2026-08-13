# mcp/src/agents_remember/models/skills.py

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember                         |
| path                   | `mcp/src/agents_remember/models/skills.py` |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-08-02T01:05+02:00                     |
| lastVerifiedCommitHash | `a09b906bbf2855c3479b4d3199607ff8689b7d93` |
| lastVerifiedCommitDate | 2026-08-13T13:51:44+02:00|
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
- Copy/archive semantics remain owned by the install service and application entry point.

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The skills install application entry point delegates to package install services. | `skills_install_tool`; "return install_skills(" | mcp/src/agents_remember/application/runtime/skills.py:11-28 |

## Update History

- 2026-08-02T16:46+02:00 — 260731-EFA-L6 curator W1-B03: repaired 1 citation row with exact anchors and source path; scoped citation recheck recorded separately. Verification metadata remains pinned until closeout.

- 2026-08-02T01:05+02:00 — No content impact: `mcp/src/agents_remember/tasks/reopen.py` moved to `mcp/src/agents_remember/worktrees/reopen.py` (reopen rewrites the leaf's enclosure contract, and ranking it as a task operation made `tasks` and `worktrees` mutually dependent per `layers.toml`). Re-pointed the reference here; the behavior this document describes is unchanged. Verification metadata pinned until closeout stamps the L6 code commit.
- 2026-08-02T00:17+02:00 — No content impact: 260731-EFA-L6 renamed `mcp/src/agents_remember/controllers/` to `application/` and moved `worktrees/status.py` to `application/worktree_status.py`. Updated the references and the vocabulary here ("the application layer" for the package, "an application entry point" for one function); the behavior this document describes is unchanged. Verification metadata pinned until closeout stamps the L6 code commit.
- 2026-05-28T19:52+02:00: Created for the skill-install response contract.
