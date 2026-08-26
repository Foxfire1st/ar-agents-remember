# mcp/tests/test_l6_diff_coverage_abandon.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/test_l6_diff_coverage_abandon.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-08-25T15:44+02:00 |
| lastVerifiedCommitHash | `ae8c47ce897b04380ebcb80f750d77ed4dc9f37d` |
| lastVerifiedCommitDate | 2026-08-26T08:10:26+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[overview](overview.md)

## Purpose

L6 closeout coverage tests for the worktree abandon helpers: reserved-guard entry, guarded
abandon flows, contract-authorized branch refusal and unmerged-commit checks, and external-memory
branch handling.

## Code Commentary

- `TestAbandonReserved` covers guard-entry errors when the namespace is reserved.
- `TestAbandonWithGuard` covers helper failure, blocked mutation, dry-run, and publish paths.
- `_abandon_authority` creates a real Git repository and contract-derived abandon capability so
  helper calls retain the production terminal-ownership boundary.
- `TestAbandonBranch` covers branch refusals, branch-presence refusals, and unmerged commits while
  passing that real capability to the target-bound helper.
- `TestAbandonBranches` covers the current code-and-memory branch set; it does not preserve the
  retired synthesized replay-integration branch.

## Repo-Internal References

This module defines the test classes cited below; each row points at the exact source range holding the anchor.

| Finding | Anchor | Source |
| --- | --- | --- |
| Builds a real contract-derived terminal authority for helper tests. | `_abandon_authority` | mcp/tests/test_l6_diff_coverage_abandon.py:58-85 |
| Defines the class `TestAbandonReserved`. | `TestAbandonReserved` | mcp/tests/test_l6_diff_coverage_abandon.py:88-114 |
| Defines the class `TestAbandonWithGuard`. | `TestAbandonWithGuard` | mcp/tests/test_l6_diff_coverage_abandon.py:117-177 |
| Defines the class `TestAbandonBranch`. | `TestAbandonBranch` | mcp/tests/test_l6_diff_coverage_abandon.py:180-304 |
| Defines the class `TestAbandonBranches`. | `TestAbandonBranches` | mcp/tests/test_l6_diff_coverage_abandon.py:338-345 |

## 260821-CLIVE-L2 Addressable Abandon Fixture

The abandon authority fixture now publishes the lifecycle-operation locator and immutable manifest
before constructing terminal mutation authority. This keeps coverage on the normal root-journal
address path and avoids a test-only contract-path reader.

| Finding | Anchor | Source |
| --- | --- | --- |
| The fixture publishes lifecycle location immediately after contract publication. | `_abandon_authority` | mcp/tests/test_l6_diff_coverage_abandon.py:62-98 |


## PDLS Reconciliation

Abandon diff-coverage forcing now follows the current terminal archive and cleanup proof boundary.

The test continues to exercise production-owned behavior. No diagnostic result is treated as
certifying evidence and no fallback or threshold exception was introduced.
## Update History

- 2026-08-25T15:44+02:00 — PDLS whole-system reconciliation updated the implementation summary
  above after source and requirement review. Verification remains closeout-owned.


- 2026-08-24T00:51+02:00 — 260821-CLIVE-L2: reconciled the L2 test boundary represented by the changed source. Verified at code commit `1d446724`.

- 2026-08-16T00:10+02:00 — 260815-DAG-L4 targeted-gate repair: migrated stale
  `_abandon_branch` and `_abandon_branches` calls to the target object plus real
  contract-derived terminal authority, and removed the retired memory-integration branch
  expectation. Verification metadata remains closeout-owned.

- 2026-08-08T17:18+02:00 — No content impact: 260731-EFA-L9 rewrote this source's imports/callers only (model-extraction caller wave); the behavior this card documents is unchanged and the body was re-verified current. Verification metadata pinned until closeout stamps the L9 code commit.

- 2026-08-05T00:00+02:00 — 260731-EFA-L6 closeout pass: created this file-level onboarding card for the new source file; anchors derived from current worktree source. Verification metadata pinned until closeout stamps the code commit.
