# mcp/src/agents_remember/kernel/primitives/command_capture.py

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember                         |
| path                   | `mcp/src/agents_remember/kernel/primitives/command_capture.py` |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-08-02T01:05+02:00                     |
| lastVerifiedCommitHash | `a09b906bbf2855c3479b4d3199607ff8689b7d93` |
| lastVerifiedCommitDate | 2026-08-13T13:51:44+02:00|
| governingOverview      | `overview.md`                              |

## Governing Overview

[kernel primitives overview](overview.md)

## Purpose

`kernel/primitives/command_capture.py` (moved from `mcp/command_capture.py` by 260731-EFA-L9) adapts package-local command-style modules into structured
response payloads for the remaining script-facade bridge code.

## Code Commentary

### Logic

`run_package_main()` redirects stdout and stderr while calling an importable
`main(argv)` function. It returns `ok`, `operation`, `returncode`, `argv`,
captured streams, and parsed JSON payload when stdout is JSON. Current MCP
skill application entry points call service functions directly; this helper remains only
where lower-level provider setup still bridges through `lifecycle.main`.

### Invariants And Boundaries

- This helper invokes importable package functions, not arbitrary shell command
  strings.
- It exists only for old behavior that still has command-shaped internals during
  the parity bridge; do not use it as the default application entry point pattern.

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| Provider setup still uses this helper while bridging to the provider lifecycle CLI facade. | ["provider_setup."] | mcp/src/agents_remember/providers/setup_common.py:206-206 |
| Skill application entry points now call service-backed functions instead of returning command-capture payloads. | ["install_skills("] | mcp/src/agents_remember/application/runtime/skills.py:25-25 |

## Update History

- 2026-08-02T20:45:43+02:00 — L6 W2-B02 curator: anchored 2 repository-internal references for the provider setup bridge and skill application entry point; final scoped result 0 (checker-clean).

- 2026-08-02T01:05+02:00 — No content impact: `mcp/src/agents_remember/tasks/reopen.py` moved to `mcp/src/agents_remember/worktrees/reopen.py` (reopen rewrites the leaf's enclosure contract, and ranking it as a task operation made `tasks` and `worktrees` mutually dependent per `layers.toml`). Re-pointed the reference here; the behavior this document describes is unchanged. Verification metadata pinned until closeout stamps the L6 code commit.
- 2026-08-02T00:17+02:00 — No content impact: 260731-EFA-L6 renamed `mcp/src/agents_remember/controllers/` to `application/` and moved `worktrees/status.py` to `application/worktree_status.py`. Updated the references and the vocabulary here ("the application layer" for the package, "an application entry point" for one function); the behavior this document describes is unchanged. Verification metadata pinned until closeout stamps the L6 code commit.
- 2026-05-25T19:16+02:00: Updated after lower-level provider setup command capture switched wording to the direct `providers.lifecycle` facade.
- 2026-05-24T00:37+02:00: Updated after worktree, memory, and benchmark MCP controllers stopped using command capture and moved to direct service results.
- 2026-05-23T13:09+02:00: Created for package-local command capture.
