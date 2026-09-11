# mcp/src/agents_remember/worktrees/series_closeout.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/worktrees/series_closeout.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-11T12:02+02:00|
| lastVerifiedCommitHash | `3b552f5a215648274dc5e6e4d5f0a01c2ee80be2` |
| lastVerifiedCommitDate | 2026-09-12T01:54:48+02:00|
| governingOverview | `../../../overview.md` |

## Governing Overview

[governing overview](../../../overview.md)

## Purpose

Seals an atomic block only after every canonical leaf forms one exact journaled code-and-memory landing chain, then records the named series refs without ambient workbench commits.

## CCR-R12@v5 Current Series Boundary

Series closeout and integration remain recording/publication operations over already landed leaf
transactions. They re-prove canonical membership, exact code/memory ancestry, named-ref identity,
and authority before recording the pair; they do not create a normal leaf code/memory/ledger
transaction or invoke strict code quality, memory quality, selected certification, curator
coherence, or independent review. Full suites are an explicit developer request.

## Code Commentary

`_exact_atomic_landing_chain` now returns the ordered landed leaf chain, and `atomic_series_ledger_prefix` derives the newest-first ledger rows that chain contributes.

Closeout and series integration share the same canonical task/contract evidence, but only the
protected landing takes the narrow integration-authority lock. Closeout re-proves completion without
that landing-only lock. The seal verifies canonical master membership, exact enclosure
identity, code and memory repository identity, each leaf's base-to-integrated edge, content/ledger
ancestry, and final named-ref tips. Direct commits, missing leaves, foreign copied contracts, mismatched
code/memory order, and concurrent child admission cannot be absorbed into a master candidate.

Since the closeout-door cut (commit `fad9808e`) the landed-leaf proof no longer consults a door: the
`_AtomicLandingFacts` carrier and its `door`/`door_sprint`/`door_candidate` comparisons were removed
from `_require_exact_atomic_landing_chain` and `_atomic_leaf_code_matches` when `contract.closeout_door`
stopped existing.

Since 260815-DAG-L13 the atomic-master completion proof (`_require_atomic_master_complete`) and
the series-edge publication (`_publish_atomic_series_edge`) read the **effective** execution
nature (`scheduling_mode.effective_execution_nature`): a nature-less legacy master executes
atomically under the atomic-sequential default and closes out without migration (L13-R5a), and a
graph-less sprint takes the atomic-sequential series path. Graph absence does not weaken canonical
master/leaf re-proof and no projection row is completion authority.

Since 260831-closeout-door-cut the master/leaf re-proof carries no door dimension at all.

## Invariants And Boundaries

- Atomic membership comes from exact master task rows and canonical parent relations, not sibling-file discovery.
- The series history equals the ordered leaf landing chain from recorded bases to current named refs.
- Every external memory pair proves base-to-content and content-to-ledger ancestry plus exact ledger mapping.
- Series closeout records named refs and never commits ambient repository-root worktrees.
- The effective nature, not graph presence alone, gates the atomic closeout path; graph-less
  atomic-sequential is valid.

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| Closeout re-proves canonical completion without the landing lock; integration repeats it under the narrow protected-landing lock. | `publish_closeout_under_authority`, `publish_series_integration_under_authority` | mcp/src/agents_remember/worktrees/series_closeout.py:33-50; mcp/src/agents_remember/worktrees/series_closeout.py:53-69 |
| The complete leaf set and exact pair chain are proved before sealing. | `_require_every_atomic_leaf_landed`, `_require_exact_atomic_landing_chain` | mcp/src/agents_remember/worktrees/series_closeout.py:72-73; mcp/src/agents_remember/worktrees/series_closeout.py:101-129 |
| Each leaf enclosure, code edge, and memory edge is bound exactly. | `_atomic_leaf_documents`, `_require_atomic_leaf_landed`, `_atomic_leaf_code_matches`, `_atomic_leaf_memory_matches` | mcp/src/agents_remember/worktrees/series_closeout.py:165-203; mcp/src/agents_remember/worktrees/series_closeout.py:206-234; mcp/src/agents_remember/worktrees/series_closeout.py:237-270; mcp/src/agents_remember/worktrees/series_closeout.py:273-300 |
| Atomic-master completion resolves the effective nature under the atomic-sequential default. | `_require_atomic_master_complete` | mcp/src/agents_remember/worktrees/series_closeout.py:309-346 |
| Exact series closeout rejects workbench changes and records the named memory pair. | `refuse_series_workbench_commit`, `exact_series_memory_closeout` | mcp/src/agents_remember/worktrees/series_closeout.py:349-365; mcp/src/agents_remember/worktrees/series_closeout.py:368-400 |

## Documentation References

No configured domain-documentation or cross-repository source applies to this file.

## 260821-CLIVE Atomic Completion Re-Proof

Series closeout no longer creates or mutates an initial queue state. It re-proves the atomic master
is complete and every atomic leaf is landed from canonical task/contract evidence, then repeats
that proof under the landing-only integration authority lock immediately before protected
publication. Door candidate/sprint identities no longer participate in the landed-leaf proof — that
comparison was deleted with the contract field by the closeout-door cut (commit `fad9808e`).
Scheduling projection absence is irrelevant to atomic completion truth.

## Update History
- 2026-09-11T22:39:01+00:00: Generated citation repair: `_require_atomic_master_complete` repointed to mcp/src/agents_remember/worktrees/series_closeout.py:309-346. No content impact: mechanical anchor-range projection bound to citation source snapshot b911c7c4c4eb354cf78d2a53e1538fc36a5f9a5e36a3702e5953739b48812830; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-11T12:02+02:00 — Closeout-door cut reconciliation at code commit `fad9808e`: removed the door dimension from the landed-leaf proof claim — `_AtomicLandingFacts` and its `door`/`door_sprint`/`door_candidate` comparisons were deleted with `contract.closeout_door`. Verification metadata remains pinned because only the cut-affected claims were reconciled; source documentation only, no acceptance claim.
- 2026-09-10T07:33:57+02:00 — CCR-R12@v5 scoped runtime curation against code commit `6f3e3fde75a1ca0202c9b07557cf86a7893e8532`: reconciled the normal transaction boundary and preserved earlier history. This records source documentation only; it makes no acceptance or certification claim.

- 2026-09-09T14:45+02:00 — CCR-L42 curator reconciliation: re-read affected claims against the frozen current source and corrected only their source anchors/ranges; verification stamps remain closeout-owned.

- 2026-08-29T17:23+02:00 — No content impact: reviewed the Python 3.13 local type-parameter migration for closeout and integration publication callbacks and confirmed that series authority remains as documented. Verification remains closeout-owned.

- 2026-08-24T15:04+02:00 — Cumulative CLIVE curation: replaced initial queue-state publication with exact atomic completion and claimed-door re-proof at landing. Timestamp is the curator host's Europe/Berlin system time; verification remains closeout-owned.

- 2026-08-24T00:51+02:00 — No content impact: 260821-CLIVE-L2 the source only imports the extracted `initial_queue_state` owner and calls the same initializer with the same arguments. Verified at code commit `1d446724`.

- 2026-08-21T00:45+02:00 — 260815-DAG master full-gate repair: import paths updated to the moved package locations (`worktrees/queue`, `worktrees/integration`, `application/task_docs`, `models/queue`) and the `unittest.main` tail guard removed where present; reviewed — no content impact on the documented contracts. Verified at code commit e5cb139f.


- 2026-08-19T22:32+02:00 — 260815-DAG-L13: atomic closeout gates on the effective execution
  nature (nature-less legacy masters close out atomically under the default, L13-R5a), and a
  graph-less sprint's series edge publishes queue-free because the live series contract already
  owns the sequential lane (L13-R1). Verification remains closeout-owned.

- 2026-08-18T09:10+02:00 — No content impact: renamed the atomic 'barrier' concept to 'blocker' throughout; behavior unchanged. Verification remains closeout-owned.

- 2026-08-17T12:30+02:00 — 260815-DAG-L5: added `atomic_series_ledger_prefix` and made `_exact_atomic_landing_chain` return the ordered leaf chain. Verification remains closeout-owned.

- 2026-08-15T23:38+02:00 — 260815-DAG-L4: created atomic series closeout authority onboarding from the frozen integration-authority candidate. Verification remains closeout-owned.
