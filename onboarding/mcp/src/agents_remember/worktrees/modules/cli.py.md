# mcp/src/agents_remember/worktrees/modules/cli.py

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember                         |
| path                   | `mcp/src/agents_remember/worktrees/modules/cli.py` |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated | 2026-08-23T16:08+02:00 |
| lastVerifiedCommitHash | `346507af24396ab7b491e02511c4af006ccd3dc5` |
| lastVerifiedCommitDate | 2026-08-30T07:51:57+02:00|
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

| Finding | Anchor | Source |
| --- | --- | --- |
| The CLI module exposes the public main entry point for `python -m` execution. | "def main" | mcp/src/agents_remember/worktrees/modules/cli.py:192-199 |
| MCP application entry points bypass CLI parsing and call result-returning functions directly. | `worktree_start_tool`; `worktree_attach_tool`; `worktree_status_tool`; `worktree_integrate_tool`; `worktree_cleanup_tool` | mcp/src/agents_remember/application/worktree_tools.py:125-222; mcp/src/agents_remember/application/worktree_tools.py:287-296; mcp/src/agents_remember/application/worktree_tools.py:299-322; mcp/src/agents_remember/application/worktree_tools.py:621-702; mcp/src/agents_remember/application/worktree_tools.py:979-995 |
| The heal implementation this seam invokes (walk once, cheap-skip canonical ids, rewrite + report) lives in the contract module. | `heal_contract_leaf_ids` | mcp/src/agents_remember/worktrees/worktree_contract.py:491-566 |
| The CLI seam regression drives `main(["heal-leaf-ids", ...])` end to end. | `test_heal_cli_command_is_the_on_demand_seam` | mcp/tests/test_leaf_ref_resolution.py:419-433 |

## Series-Contract Notes

The common CLI contract-path help now names `series-contract.md`, aligning command-line usage with the root/leaf contract schema.

## 260815-DAG-L4 Integration-Authority Impact

L4 makes task-derived integration refs mechanically non-ordinary: repository defaults, sprint supers, and active atomic-series refs are censused across code and external memory. Mutation is admitted only through exact lifecycle authority, named-ref compare-and-swap, queue/repository serialization, or a terminal capability; stale topology, aliases, ambient checkouts, and torn recovery fail closed.

## 260821-CLIVE-L1 Legacy CLI Boundary

The synchronous CLI closeout apply path now fails closed with `JOURNALED_CLOSEOUT_REQUIRED`. Dry-run loads the contract and uses the canonical normalizer, returning typed validation behavior without mutation. CLI flags are syntactically optional because enabledness is derived at runtime; enabled messages remain mandatory and explicit. The CLI does not provide a compatibility bypass around the lifecycle journal.

## 260821-CLIVE-L2 Current Contract

The current source seams include `parse_json_stdout`, `command_status`, `command_attach`. This module remains a public execution adapter over closed admission and exact mutation-owner reread; it does not duplicate reader exception families or lifecycle authority.

### Reconciled Source Evidence

| Finding | Anchor | Source |
| --- | --- | --- |
| The current module exposes `parse_json_stdout`, `command_status`, `command_attach` at this ownership boundary. | `parse_json_stdout`; `command_status`; `command_attach` | mcp/src/agents_remember/worktrees/modules/cli.py:30-37; mcp/src/agents_remember/worktrees/modules/cli.py:40-43; mcp/src/agents_remember/worktrees/modules/cli.py:46-49 |

## Update History

- 2026-08-26T10:44:52+02:00 — No content impact: reviewed the closeout corrected-call model package relocation; CLI normalization and command routing are unchanged.
- 2026-08-23T16:08+02:00 — 260821-CLIVE-L2: reconciled this card with the accepted full L2 candidate; verification metadata remains pinned until architect-owned closeout stamps the real code commit.

- 2026-08-22T10:39+02:00 — 260821-CLIVE-L1: curated against accepted candidate tree `4241908c`; verification metadata remains pinned until governed closeout stamps the landed code commit.

- 2026-08-15T23:38+02:00 — Reconciled this worktree owner's role in task-derived protected-ref authority, exact named-ref movement, and crash-safe recovery. Verification metadata remains closeout-owned.
- 2026-08-12T15:19+02:00 — L23 curator: re-read the current source-backed claims and retained their wording while the sanctioned MCP citation-fix wave regenerated exact ranges; verification provenance remains closeout-owned.
- 2026-08-04T12:19:51+02:00 — 260731-EFA-L6 S18-B01 curator: reconciled the bounded worker ledger; source-clear citations were repaired, split, rewritten, or deleted as applicable, then the exact scoped fixer/check passed.

- 2026-08-02T01:05+02:00 — No content impact: `mcp/src/agents_remember/tasks/reopen.py` moved to `mcp/src/agents_remember/worktrees/reopen.py` (reopen rewrites the leaf's enclosure contract, and ranking it as a task operation made `tasks` and `worktrees` mutually dependent per `layers.toml`). Re-pointed the reference here; the behavior this document describes is unchanged. Verification metadata pinned until closeout stamps the L6 code commit.
- 2026-08-02T00:17+02:00 — No content impact: 260731-EFA-L6 renamed `mcp/src/agents_remember/controllers/` to `application/` and moved `worktrees/status.py` to `application/worktree_status.py`. Updated the references and the vocabulary here ("the application layer" for the package, "an application entry point" for one function); the behavior this document describes is unchanged. Verification metadata pinned until closeout stamps the L6 code commit.
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

## Governing Overview

[governing overview](overview.md)
## Cross-Repo References

This file owns no ambient cross-repository authority. Any external-memory repository it reaches remains explicitly contract-addressed.
