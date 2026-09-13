# mcp/tests/test_transaction_only_worktree_delivery.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/test_transaction_only_worktree_delivery.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-10T07:24:09+02:00 |
| lastVerifiedCommitHash | `1ddf7fdac40fa3e9c30b8ded693d440e07d6a8b6` |
| lastVerifiedCommitDate | 2026-09-13T22:07:53+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[Test suite overview](overview.md)

## Purpose

Protects the CCR-R12@v5 transaction-only closeout and integration boundary at the public worktree
tool surface.

## Code Commentary

The focused tests patch strict code quality, memory quality, selected certification, and curator
coherence entry points to fail if normal closeout or integration calls them. They then exercise the
real public closeout and paired integration routes: closeout must produce the code, external-memory,
and ledger commits with the exact ledger mapping; integration must publish the prepared pair; and a
source-ref movement must refuse before protected pair publication.

Each scenario installs a real failing `pre-commit` hook in both repositories and probes it once to
prove the hook itself is active, then asserts that the normal code and memory transaction commits
leave no hook log. This captures the bounded commit contract: closeout stages and uses
`commit_verified_staged` with `--no-verify`, while integration moves existing refs/tree state and
creates no merge commit or merge-hook path.

`_assert_memory_attribution` is the shared attribution reader the closeout scenario calls with the
real commit shas the public closeout returned. It reads the memory-content commit back out of the
object and asserts `%B` equals `MESSAGES.memory` plus `\n\nCode-Commit: <code commit>`, that the
literal `Code-Commit:` appears exactly once, that `git interpret-trailers --parse` returns
`Code-Commit: <code commit>`, and that `git log --format=%(trailers:key=Code-Commit)` returns the
same trailer. The mandatory `memory.md`-only ledger commit is asserted to return `""` from that same
reader: it has no code counterpart to name, so it is deliberately left unattributed.

## Invariants And Boundaries

- Normal public closeout/integration does not acquire a quality or certification acceptance tool.
- Closeout preserves the code-to-memory ledger mapping and sequential recovery evidence.
- The memory-content commit object carries exactly one `Code-Commit:` trailer naming the code commit
  that same closeout landed, and it reads as trailer data to both documented git readers; the
  `memory.md`-only ledger commit carries none. Assertions only: this file gained no new test function
  and no new parametrized case for it.
- Integration refuses source movement before changing the protected pair.
- Hook non-invocation is tested only for the configured repository hooks installed by the scenario;
  it does not imply that arbitrary external commands cannot run outside these commit paths.
- This file records focused behavior protection, not full-suite certification or independent review.

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| Public closeout delivers code, memory, and ledger while acceptance helpers are forbidden. | `test_public_closeout_commits_code_memory_and_ledger_without_acceptance_tools` | mcp/tests/test_transaction_only_worktree_delivery.py:219-315 |
| The memory-content commit carries exactly one `Code-Commit` trailer naming the landed code commit, read back by `%B`, by `git interpret-trailers --parse`, and by `%(trailers:key=Code-Commit)`; the ledger commit returns `""` from the same reader. | `_assert_memory_attribution` | mcp/tests/test_transaction_only_worktree_delivery.py:172-215 |
| Public integration publishes the prepared pair without acceptance helpers and without configured hooks. | `test_public_integration_merges_prepared_pair_without_acceptance_tools` | mcp/tests/test_transaction_only_worktree_delivery.py:317-370 |
| Source movement refuses before protected pair publication. | `test_public_integration_ref_movement_refuses_before_pair_merge` | mcp/tests/test_transaction_only_worktree_delivery.py:373-427 |

## Update History
- 2026-09-13T21:42+02:00 — 260913-LCA-L1 (uncommitted change set on `ar/260913-lca-l1-ar`): assertion-only extension. Added the shared `_assert_memory_attribution` reader and called it from `test_public_closeout_commits_code_memory_and_ledger_without_acceptance_tools`, so the public closeout path is now checked for exactly one `Code-Commit: <code sha>` trailer inside the memory-content commit object (by `%B`, `git interpret-trailers --parse`, and `%(trailers:key=Code-Commit)`) and for no trailer at all on the `memory.md`-only ledger commit. The re-closeout test's direct call into `_commit_memory_content` now passes `code_commit=`. No new test function and no new parametrized case. Rebound every stale row (`test_public_closeout...` 219-315, `_assert_memory_attribution` 172-215, `test_public_integration_merges...` 317-370, `test_public_integration_ref_movement...` 373-427). Verification metadata remains closeout-owned; no acceptance claim and no verification stamp advanced.
- 2026-09-11T22:39:01+00:00: Generated citation repair: `test_public_closeout_commits_code_memory_and_ledger_without_acceptance_tools` repointed to mcp/tests/test_transaction_only_worktree_delivery.py:172-257. No content impact: mechanical anchor-range projection bound to citation source snapshot b911c7c4c4eb354cf78d2a53e1538fc36a5f9a5e36a3702e5953739b48812830; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-11T22:39:01+00:00: Generated citation repair: `test_public_integration_merges_prepared_pair_without_acceptance_tools` repointed to mcp/tests/test_transaction_only_worktree_delivery.py:260-313. No content impact: mechanical anchor-range projection bound to citation source snapshot b911c7c4c4eb354cf78d2a53e1538fc36a5f9a5e36a3702e5953739b48812830; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-11T22:39:01+00:00: Generated citation repair: `test_public_integration_ref_movement_refuses_before_pair_merge` repointed to mcp/tests/test_transaction_only_worktree_delivery.py:316-369. No content impact: mechanical anchor-range projection bound to citation source snapshot b911c7c4c4eb354cf78d2a53e1538fc36a5f9a5e36a3702e5953739b48812830; claim bytes unchanged; generated by ccr-r10@v1.

- 2026-09-10T07:24:09+02:00 — Added with CCR-R12@v5 source commit `6f3e3fde75a1ca0202c9b07557cf86a7893e8532`. The hook-aware focused run passed 3 tests in 5.95s (measured wall 6.213346s); this is targeted behavior evidence and not a full-suite or certification claim.
