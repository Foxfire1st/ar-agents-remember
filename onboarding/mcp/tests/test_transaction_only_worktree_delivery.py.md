# mcp/tests/test_transaction_only_worktree_delivery.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/test_transaction_only_worktree_delivery.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-10T07:24:09+02:00 |
| lastVerifiedCommitHash | `6096941f41204c9a7d6ccb2b29f6b2e862ed56b4` |
| lastVerifiedCommitDate | 2026-09-10T09:57:27+02:00|
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

## Invariants And Boundaries

- Normal public closeout/integration does not acquire a quality or certification acceptance tool.
- Closeout preserves the code-to-memory ledger mapping and sequential recovery evidence.
- Integration refuses source movement before changing the protected pair.
- Hook non-invocation is tested only for the configured repository hooks installed by the scenario;
  it does not imply that arbitrary external commands cannot run outside these commit paths.
- This file records focused behavior protection, not full-suite certification or independent review.

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| Public closeout delivers code, memory, and ledger while acceptance helpers are forbidden. | `test_public_closeout_commits_code_memory_and_ledger_without_acceptance_tools` | mcp/tests/test_transaction_only_worktree_delivery.py:216-292 |
| Public integration publishes the prepared pair without acceptance helpers and without configured hooks. | `test_public_integration_merges_prepared_pair_without_acceptance_tools` | mcp/tests/test_transaction_only_worktree_delivery.py:293-337 |
| Source movement refuses before protected pair publication. | `test_public_integration_ref_movement_refuses_before_pair_merge` | mcp/tests/test_transaction_only_worktree_delivery.py:338-388 |

## Update History

- 2026-09-10T07:24:09+02:00 — Added with CCR-R12@v5 source commit `6f3e3fde75a1ca0202c9b07557cf86a7893e8532`. The hook-aware focused run passed 3 tests in 5.95s (measured wall 6.213346s); this is targeted behavior evidence and not a full-suite or certification claim.
