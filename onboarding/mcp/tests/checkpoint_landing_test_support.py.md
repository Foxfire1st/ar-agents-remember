# mcp/tests/checkpoint_landing_test_support.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/checkpoint_landing_test_support.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-15T01:15+00:00 |
| lastVerifiedCommitHash | `420669c459aab3650cdaa5b3e5271e71d7d94c0e` |
| lastVerifiedCommitDate | 2026-09-17T10:54:08+02:00|
| verificationStatus | working-candidate |
| governingOverview | `overview.md` |

The body describes the uncommitted LCA L9 working candidate. The commit fields identify the latest real commit touching this source file; they do not claim that the candidate is committed or accepted.

## Governing Overview

[Nearest governing route overview](overview.md)

## Purpose

Provide shared real-Git builders and readers for checkpoint and ordinary series/leaf integration scenarios.

## Code Commentary

### Logic

`close_out_leaf` authors code and one attributed memory-content commit in the leaf's own worktrees, refreshes an untracked cache, and records only the accepted pair. `accumulate_master_line` combines a real code commit with a memory-content commit whose trailer names it; the returned LedgerRow is a convenient value for that actual pair, not a row read from cached history.

`branch_checkout` creates and removes an exact disposable branch worktree. Source advancement and absorption use real content commits and a native merge; no helper creates ledger-only commits, rewrites cached rows to authorize a landing, or manually records a reconciled pair. The remaining readers expose exact revisions, memory repository, payload strings, and master task status.

`checkpoint` calls the public worktree_checkpoint_landing tool with ff-only strategy. Its consumers are the checkpoint end-to-end, cross-master concurrency, and lifecycle playthrough modules.

### Conventions

A flat support module owns shared construction steps; scenario-specific assertions stay in the consumers. A support function's existence does not establish that a scenario ran.

### Invariants And Boundaries

- Real commits and branches back every accepted pair.
- Memory cache preparation is part of ordinary memory content; refreshing the cache is not a Git commit.
- Checkpoint scenarios retain the public tool boundary.
- Disposed scratch worktrees do not become authority for a later scenario.

### Todos

No new file-local follow-up is identified by this source reconciliation.

## Docs References

No domain-documentation source is configured for this slice. The behavior described here is established by current repository source and the authorized LCA L9 change, rather than an invented external reference.

| Finding | Anchor | Source |
| --- | --- | --- |

## Repo-Internal References

These current source spans identify the implementation owners and the specific assertions supporting the file's behavior. A test definition is evidence of its assertions, not an execution or certification receipt.

| Finding | Anchor | Source |
| --- | --- | --- |
| Leaf and accumulated-master pairs are built from real code/memory commits. | `close_out_leaf` | mcp/tests/checkpoint_landing_test_support.py:59-82 |
| Temporary branch ownership and real source-content reconciliation. | `branch_checkout` | mcp/tests/checkpoint_landing_test_support.py:48-56 |
| Public checkpoint and canonical master status helpers. | `checkpoint` | mcp/tests/checkpoint_landing_test_support.py:148-156 |
| The public boundary scenarios consume the shared builders. | `test_a_leaf_closeout_preview_is_untouched_by_the_series_completion_gate` | mcp/tests/test_checkpoint_landing_end_to_end.py:41-479 |

## Cross-Repo References

The operation and fixture boundaries described here are defined by same-repository contracts and Git helpers. No separate cross-repository document is used as evidence for this card.

| Finding | Anchor | Source |
| --- | --- | --- |

## Update History

- 2026-09-15T01:15+00:00 — 260913-LCA-L9 working candidate: Replaced shared three-commit builders with actual attributed memory outputs; removed unused cache-row mutations/readers and retained the three consumers' shared APIs. Current source and citation targets were checked; the metadata records the last real file commit, and candidate changes remain uncommitted.

- 2026-09-14T20:00+02:00 — 260913-LCA-L12 curator: created the one-to-one sidecar for this new
  shared-support module. It holds the checkpoint-landing world builders extracted from
  `test_checkpoint_landing_end_to_end.py`, and the card records that provenance plainly: the move
  exists to clear a duplicated fixture and a size rail, not to add behaviour, so nothing here
  changes what the cases prove. Records the catalog's declared facts — `shared-support`, owner
  `checkpoint-landing-test-port`, introduced by `260913-LCA-L12`, `exact` consumer scope — the
  three consumers and their import sites, and why this module carries no lane row of its own.
  Verification metadata remains closeout-owned; no verification stamp advanced and no acceptance
  claim is made.
