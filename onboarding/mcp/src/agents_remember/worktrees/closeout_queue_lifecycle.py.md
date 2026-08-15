# mcp/src/agents_remember/worktrees/closeout_queue_lifecycle.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/worktrees/closeout_queue_lifecycle.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-08-15T13:08+02:00 |
| lastVerifiedCommitHash | `17987fa66a642306eb8d20fa9a4bff2b881550d2` |
| lastVerifiedCommitDate | 2026-08-15T14:36:30+02:00|
| governingOverview | `../../../overview.md` |

## Governing Overview

[MCP overview](../../../overview.md)

## Purpose

Connects the durable queue to task-fact publication and the closeout/integration lifecycle without
making domain modules depend on the public MCP application handler.

## Code Commentary

### Logic

The service resolves durable queue bindings from the leaf contract, routes governed task
publications through the sprint store lock, claims selected candidates for closeout, certifies exact
closeout commits, claims certified candidates for integration, revalidates the same graph/evidence
immediately before source refs move, consumes the record after landing, and releases reversible
failed/cancelled operations. Internal transitions use stable request ids and one-way owner proofs.

### Conventions

Legacy absence is accepted only when no durable queue binding or state has ever existed. Once bound,
missing/damaged topology or state fails closed.

### Invariants And Boundaries

- The graph is recomputed while the queue lock is held for every claim/certify/final transition.
- Integration moves only the commits certified by the same candidate record.
- Reversible failure/cancellation releases to `declared` or `certified`; post-boundary state is not
  silently rewound.
- Successful integration consumes the exact candidate idempotently.

### Todos

None recorded.

## Docs References

No configured Domain Documentation source applies.

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| Closeout claim binds the plane-owned lifecycle operation to the selected candidate. | `claim_queue_candidate_for_closeout` | mcp/src/agents_remember/worktrees/closeout_queue_lifecycle.py:215-229 |
| Integration claim binds the same operation to the certified candidate. | `claim_queue_candidate_for_integration` | mcp/src/agents_remember/worktrees/closeout_queue_lifecycle.py:251-267 |
| Irreversible integration revalidates current graph, candidate, readiness, and exact commits under the queue lock. | `require_queue_candidate_for_integration` | mcp/src/agents_remember/worktrees/closeout_queue_lifecycle.py:296-348 |
| Landing consumes the exact lifecycle-owned candidate idempotently. | `complete_queue_candidate_integration` | mcp/src/agents_remember/worktrees/closeout_queue_lifecycle.py:351-408 |
| Reversible terminal operations release internal ownership safely. | `release_queue_candidate_after_reversible_operation` | mcp/src/agents_remember/worktrees/closeout_queue_lifecycle.py:411-478 |
| Closeout certification refreshes curator evidence and binds the exact committed result. | `_certify_closeout` | mcp/src/agents_remember/worktrees/closeout_queue_lifecycle.py:550-587 |

## Cross-Repo References

No meaningful cross-repository reference applies.

## Update History

- 2026-08-15T13:08+02:00 — No content impact: Ruff split the aliased lifecycle-owner import from
  the unaliased commit-tree import; both still resolve from one candidate-evidence owner.
- 2026-08-15T12:53+02:00 — No content impact: normalized the split candidate-evidence import;
  lifecycle transition ownership and ordering are unchanged.
- 2026-08-15T09:10+02:00 — Created for L3's task-publication and lifecycle queue seam; verification remains closeout-owned.
