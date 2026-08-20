# mcp/src/agents_remember/worktrees/queue/closeout_queue_lifecycle.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/worktrees/queue/closeout_queue_lifecycle.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-08-21T00:45+02:00 |
| lastVerifiedCommitHash | `e5cb139f66abbd6502d4dcc4be883eb5f49770fe` |
| lastVerifiedCommitDate | 2026-08-21T00:28:23+02:00 |
| governingOverview | `overview.md` |

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

Durable queue-completion evidence (`integration_queue_completion_evidence`) is persisted before a
candidate is consumed, and the completion event is centralized in `_integration_completion_event`.

Since 260815-DAG-L13 the atomic-series terminal publication and master completion gates resolve the
**effective** execution nature (`scheduling_mode.effective_execution_nature`) instead of the
declared cell — a nature-less legacy master executes atomically under the atomic-sequential default
and retires without migration (L13-R5a), and a graph-less sprint has no queue authority to release
(L13-R1), so publication returns directly. The irreversible integration boundary names
`recovery: worktree_sync` when refusal blockers are stale bases (L13-R2), and claiming integration
while another candidate owns the lane adds an `integration-lane-owned-by` blocker (a certified
candidate no longer occupies the lane). `complete_queue_candidate_integration` now returns the
stale-by-evidence sibling facts for the integrate result payload. The never-used
`require_queue_candidate_current` diagnostic helper was removed.

### Conventions

Legacy absence is accepted only when no durable queue binding or state has ever existed. Once bound,
missing/damaged topology or state fails closed.

### Invariants And Boundaries

- The graph is recomputed while the queue lock is held for every claim/certify/final transition.
- Integration moves only the commits certified by the same candidate record.
- Reversible failure/cancellation releases to `declared` or `certified`; post-boundary state is not
  silently rewound.
- Successful integration consumes the exact candidate idempotently and reports stale-by-evidence
  siblings as facts with `worktree_sync` as their recovery.
- Atomic-nature gates read the effective nature: the atomic-sequential default resolves a
  nature-less master to atomic, and a graph-less sprint carries no queue authority to release.
- Atomic-series terminal mutation receives an ephemeral permit only while the sprint queue and
  repository authority are both held. The permit is bound to the exact operation, canonical
  contract path, issuing thread, active `ContextVar`, and issuer-owned live registry; normal exit,
  exceptional exit, copied contexts, and cross-thread replay all fail closed.

### Todos

None recorded.

## Docs References

No configured Domain Documentation source applies.

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| Closeout claim binds the plane-owned lifecycle operation to the selected candidate. | `claim_queue_candidate_for_closeout` | mcp/src/agents_remember/worktrees/queue/closeout_queue_lifecycle.py:406-420 |
| Atomic-series terminal publication mints and revokes the exact non-replayable permit under queue/repository authority. | `publish_atomic_series_terminal_under_authority` | mcp/src/agents_remember/worktrees/queue/closeout_queue_lifecycle.py:205-228 |
| Terminal mutation verifies both context-local and issuer-owned permit liveness. | `require_atomic_series_terminal_permit` | mcp/src/agents_remember/worktrees/queue/closeout_queue_lifecycle.py:231-248 |
| Integration claim binds the same operation to the certified candidate. | `claim_queue_candidate_for_integration` | mcp/src/agents_remember/worktrees/queue/closeout_queue_lifecycle.py:442-458 |
| Irreversible integration revalidates current graph, candidate, readiness, and exact commits under the queue lock. | `require_queue_candidate_for_integration` | mcp/src/agents_remember/worktrees/queue/closeout_queue_lifecycle.py:461-486 |
| Landing consumes the exact lifecycle-owned candidate idempotently and returns stale-by-evidence sibling facts. | `complete_queue_candidate_integration` | mcp/src/agents_remember/worktrees/queue/closeout_queue_lifecycle.py:576-643 |
| Reversible terminal operations release internal ownership safely. | `release_queue_candidate_after_reversible_operation` | mcp/src/agents_remember/worktrees/queue/closeout_queue_lifecycle.py:740-807 |
| Closeout certification refreshes curator evidence and binds the exact committed result. | `_certify_closeout` | mcp/src/agents_remember/worktrees/queue/closeout_queue_lifecycle.py:1040-1077 |

## Cross-Repo References

No meaningful cross-repository reference applies.

## 260815-DAG-L4 Integration-Authority Impact

L4 makes task-derived integration refs mechanically non-ordinary: repository defaults, sprint supers, and active atomic-series refs are censused across code and external memory. Mutation is admitted only through exact lifecycle authority, named-ref compare-and-swap, queue/repository serialization, or a terminal capability; stale topology, aliases, ambient checkouts, and torn recovery fail closed.

## Update History

- 2026-08-21T00:45+02:00 — 260815-DAG master full-gate repair: source moved to `mcp/src/agents_remember/worktrees/queue/closeout_queue_lifecycle.py` (new package route); the citation fixer repointed in-body references; import paths updated inside the module. Verified at code commit e5cb139f.


- 2026-08-19T22:32+02:00 — 260815-DAG-L13: effective-nature gating replaces declared-cell reads at
  the atomic terminal-publication and master-completion seams (nature-less legacy masters retire
  normally; graph-less sprints have no queue authority to release); the integration boundary names
  `recovery: worktree_sync` on stale-base refusals; integration claiming refuses while another
  candidate owns the lane; `complete_queue_candidate_integration` returns stale-by-evidence
  sibling facts; the unused `require_queue_candidate_current` helper was removed. Verification
  remains closeout-owned.

- 2026-08-18T09:10+02:00 — No content impact: renamed the atomic 'barrier' concept to 'blocker' throughout; behavior unchanged. Verification remains closeout-owned.

- 2026-08-17T12:30+02:00 — 260815-DAG-L5: integration completion now persists durable `integration_queue_completion_evidence` before consuming the candidate, and the completion event is emitted through `_integration_completion_event`. Verification remains closeout-owned.

- 2026-08-16T01:30+02:00 — Documented the exact, thread-bound, issuer-revoked atomic-series terminal permit and copied-context replay refusal; verification remains closeout-owned.

- 2026-08-15T23:38+02:00 — Reconciled this worktree owner's role in task-derived protected-ref authority, exact named-ref movement, and crash-safe recovery. Verification metadata remains closeout-owned.

- 2026-08-15T13:08+02:00 — No content impact: Ruff split the aliased lifecycle-owner import from
  the unaliased commit-tree import; both still resolve from one candidate-evidence owner.
- 2026-08-15T12:53+02:00 — No content impact: normalized the split candidate-evidence import;
  lifecycle transition ownership and ordering are unchanged.
- 2026-08-15T09:10+02:00 — Created for L3's task-publication and lifecycle queue seam; verification remains closeout-owned.