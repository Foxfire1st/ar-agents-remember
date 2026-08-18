# mcp/src/agents_remember/worktrees/series_closeout.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/worktrees/series_closeout.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-08-15T23:38+02:00 |
| lastVerifiedCommitHash | `25841d0ddc2d93c4950abf097168fa24b220c5ad` |
| lastVerifiedCommitDate | 2026-08-18T11:30:22+02:00|
| governingOverview | `../../../overview.md` |

## Governing Overview

[governing overview](../../../overview.md)

## Purpose

Seals an atomic block only after every canonical leaf forms one exact journaled code-and-memory landing chain, then records the named series refs without ambient workbench commits.

## Code Commentary

`_exact_atomic_landing_chain` now returns the ordered landed leaf chain, and `atomic_series_ledger_prefix` derives the newest-first ledger rows that chain contributes.

Closeout and series integration publication share queue-then-repository authority. The seal verifies canonical master membership, exact enclosure identity, queue binding, code and memory repository identity, each leaf's base-to-integrated edge, content/ledger ancestry, and final named-ref tips. Direct commits, missing leaves, foreign copied contracts, mismatched code/memory order, and concurrent child admission cannot be absorbed into a master candidate.

## Invariants And Boundaries

- Atomic membership comes from exact master task rows and canonical parent relations, not sibling-file discovery.
- The series history equals the ordered leaf landing chain from recorded bases to current named refs.
- Every external memory pair proves base-to-content and content-to-ledger ancestry plus exact ledger mapping.
- Series closeout records named refs and never commits ambient repository-root worktrees.

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| Closeout and integration publish under queue-before-repository authority. | `publish_closeout_under_authority`, `publish_series_integration_under_authority` | mcp/src/agents_remember/worktrees/series_closeout.py:43-122 |
| The complete leaf set and exact pair chain are proved before sealing. | `_require_every_atomic_leaf_landed`, `_require_exact_atomic_landing_chain` | mcp/src/agents_remember/worktrees/series_closeout.py:125-202 |
| Each leaf enclosure, code edge, and memory edge is bound exactly. | `_atomic_leaf_documents`, `_require_atomic_leaf_landed`, `_atomic_leaf_code_matches`, `_atomic_leaf_memory_matches` | mcp/src/agents_remember/worktrees/series_closeout.py:205-348 |
| Exact series closeout rejects workbench changes and records the named memory pair. | `refuse_series_workbench_commit`, `exact_series_memory_closeout` | mcp/src/agents_remember/worktrees/series_closeout.py:376-427 |

## Documentation References

No configured domain-documentation or cross-repository source applies to this file.

## Update History

- 2026-08-18T09:10+02:00 — No content impact: renamed the atomic 'barrier' concept to 'blocker' throughout; behavior unchanged. Verification remains closeout-owned.

- 2026-08-17T12:30+02:00 — 260815-DAG-L5: added `atomic_series_ledger_prefix` and made `_exact_atomic_landing_chain` return the ordered leaf chain. Verification remains closeout-owned.

- 2026-08-15T23:38+02:00 — 260815-DAG-L4: created atomic series closeout authority onboarding from the frozen integration-authority candidate. Verification remains closeout-owned.
