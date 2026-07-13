# mcp/src/agents_remember/worktrees/modules/cli.py

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember                         |
| path                   | `mcp/src/agents_remember/worktrees/modules/cli.py` |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-07-12T19:55+02:00                     |
| lastVerifiedCommitHash | `b120efbfda76931cfa8eb9f24c9a808a62c10d1e` |
| lastVerifiedCommitDate | 2026-07-13T12:33:57+02:00|
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

260712-PTS-L1 adds the `heal-leaf-ids` subcommand (`--coordination-root`,
required; `--dry-run`) — the deliberate invocation seam for
`worktree_contract.heal_contract_leaf_ids`. `command_heal_leaf_ids` prints the
heal report as indented JSON and, unlike the lifecycle commands, deliberately
skips the `WorktreeArgs` DTO: healing legacy stem-shaped leaf ids is a one-shot
migration sweep, never a per-read side effect — run it once against a
coordination root (or at daemon startup) instead of relying on `load_contract`
to normalize, which it no longer does.

## Docs References

No external Domain Documentation source is configured for this memory repo.

## Repo-Internal References

| Finding | Source Path |
| --- | --- |
| The public manager facade imports `main()` from this CLI module for `python -m` execution. | [git_worktree_manager.py](agents-remember/mcp/src/agents_remember/worktrees/git_worktree_manager.py) |
| MCP controllers bypass CLI parsing and call result-returning functions directly. | [skill_tools.py](agents-remember/mcp/src/agents_remember/controllers/skill_tools.py) |
| The heal implementation this seam invokes (walk once, cheap-skip canonical ids, rewrite + report) lives in the contract module. | [worktree_contract.py](agents-remember/mcp/src/agents_remember/worktrees/worktree_contract.py) |
| The CLI seam regression drives `main(["heal-leaf-ids", ...])` end to end. | [test_leaf_ref_resolution.py](agents-remember/mcp/tests/test_leaf_ref_resolution.py) |

## Series-Contract Notes

The common CLI contract-path help now names `series-contract.md`, aligning command-line usage with the root/leaf contract schema.

## Update History

- 2026-07-12T19:55+02:00 — 260712-PTS-L1: added the `heal-leaf-ids` subcommand and
  `command_heal_leaf_ids` (`--coordination-root`, `--dry-run`; prints the heal report JSON) — the
  explicit, one-shot invocation seam for `heal_contract_leaf_ids` now that contract loads are walk-free
  and never normalize. The command intentionally bypasses `WorktreeArgs` because the heal is a migration
  sweep, not a lifecycle operation. Verification metadata pinned until closeout stamps the 260712-PTS-L1
  commit.
- 2026-06-24T06:35+02:00 - Series-contract leaf enclosure slice: common CLI help now names `series-contract.md` for explicit contract paths, matching the retired `contract.md` schema. Verification metadata pinned until closeout stamps the code commit.
- 2026-06-11T06:47+02:00 — Removed the `direct-closeout` subcommand, `command_direct_closeout`, and the `direct_closeout_result` import (issue #62 worktree-only closeout).
- 2026-05-31T12:50+02:00 — Command functions now wrap `args` in `WorktreeArgs.from_namespace(args)` (new import from `worktrees.modules.args`) before calling each result function; updated Code Commentary to name the `argparse.Namespace`-to-`WorktreeArgs` DTO conversion (1.0.0 review remediation).
- 2026-05-25T20:41+02:00: Created during worktree manager module extraction.
