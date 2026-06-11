# mcp/src/agents_remember/worktrees/modules/cli.py

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember-md                         |
| path                   | `mcp/src/agents_remember/worktrees/modules/cli.py` |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-05-31T12:50+02:00                     |
| lastVerifiedCommitHash | `a69b72e101d09423601916c03d4f59ecdee7dda6` |
| lastVerifiedCommitDate | 2026-06-11T11:08:18+02:00|
| governingOverview      | `overview.md`                              |

## Purpose

Owns command-line parsing and JSON print adapters for the worktree lifecycle.

## Code Commentary

The module builds the `start`, `attach`, `status`, `closeout`, `integrate`,
and `cleanup` subcommands (the `direct-closeout` subcommand was removed with
the direct-closeout surface, issue #62). Each command function
converts the raw `argparse.Namespace` into the typed `WorktreeArgs` DTO via
`WorktreeArgs.from_namespace(args)` before calling the result-returning service
functions, then prints payload JSON — keeping CLI transport concerns out of the
lifecycle operation modules.

## Docs References

No external Domain Documentation source is configured for this memory repo.

## Repo-Internal References

| Finding | Source Path |
| --- | --- |
| The public manager facade imports `main()` from this CLI module for `python -m` execution. | [git_worktree_manager.py](agents-remember-md/mcp/src/agents_remember/worktrees/git_worktree_manager.py) |
| MCP controllers bypass CLI parsing and call result-returning functions directly. | [skill_tools.py](agents-remember-md/mcp/src/agents_remember/controllers/skill_tools.py) |

## Update History

- 2026-06-11T06:47+02:00 — Removed the `direct-closeout` subcommand, `command_direct_closeout`, and the `direct_closeout_result` import (issue #62 worktree-only closeout).
- 2026-05-31T12:50+02:00 — Command functions now wrap `args` in `WorktreeArgs.from_namespace(args)` (new import from `worktrees.modules.args`) before calling each result function; updated Code Commentary to name the `argparse.Namespace`-to-`WorktreeArgs` DTO conversion (1.0.0 review remediation).
- 2026-05-25T20:41+02:00: Created during worktree manager module extraction.
