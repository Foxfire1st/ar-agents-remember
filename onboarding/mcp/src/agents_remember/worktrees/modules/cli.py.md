# mcp/src/agents_remember/worktrees/modules/cli.py

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember                         |
| path                   | `mcp/src/agents_remember/worktrees/modules/cli.py` |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-05-31T12:50+02:00                     |
| lastVerifiedCommitHash | `84e95ad0379cd864af3cbae21b7ffe3fd2d2b1b1` |
| lastVerifiedCommitDate | 2026-06-28T18:49:06+02:00|
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
| The public manager facade imports `main()` from this CLI module for `python -m` execution. | [git_worktree_manager.py](agents-remember/mcp/src/agents_remember/worktrees/git_worktree_manager.py) |
| MCP controllers bypass CLI parsing and call result-returning functions directly. | [skill_tools.py](agents-remember/mcp/src/agents_remember/controllers/skill_tools.py) |

## Series-Contract Notes

The common CLI contract-path help now names `series-contract.md`, aligning command-line usage with the root/leaf contract schema.

## Update History

- 2026-06-24T06:35+02:00 - Series-contract leaf enclosure slice: common CLI help now names `series-contract.md` for explicit contract paths, matching the retired `contract.md` schema. Verification metadata pinned until closeout stamps the code commit.
- 2026-06-11T06:47+02:00 — Removed the `direct-closeout` subcommand, `command_direct_closeout`, and the `direct_closeout_result` import (issue #62 worktree-only closeout).
- 2026-05-31T12:50+02:00 — Command functions now wrap `args` in `WorktreeArgs.from_namespace(args)` (new import from `worktrees.modules.args`) before calling each result function; updated Code Commentary to name the `argparse.Namespace`-to-`WorktreeArgs` DTO conversion (1.0.0 review remediation).
- 2026-05-25T20:41+02:00: Created during worktree manager module extraction.
