# docs/reference/execution-topology-migration.md

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `docs/reference/execution-topology-migration.md` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-08-26T08:45+02:00 |
| lastVerifiedCommitHash | `ae8c47ce897b04380ebcb80f750d77ed4dc9f37d` |
| lastVerifiedCommitDate | 2026-08-26T08:10:26+02:00|
| governingOverview | `docs/reference/overview.md` |

## Governing Overview

[docs/reference/overview.md](overview.md)

## Purpose

Operator-facing guide for the explicit execution topology (`executionNature` on commanded masters,
`executionGraph` on orchestration sprints). It is an *authoring* procedure, not a runtime cutover.
A sprint without an `executionGraph` uses the graph-less atomic-sequential choice: canonical
commanded-master order is an equal-priority tie-break, while exact source-pair activation exposes
one selected atomic master at a time. Selecting another master logically pauses the former without
requiring integration, contract retirement, or process/worktree termination. Authoring a graph is
the explicit opt-in to dependency-aware scheduling; no separate migration operation remains.

## Code Commentary

### Logic

The guide documents: (1) a read-only inventory that proposes the explicit nature
(atomic when an `ar/<slug>` branch already backs the master, organizational otherwise) with
parallel edges pending a ruling; (2) graph authoring through `task_doc.author_execution_graph` —
one validated mutation batch per call whose first `add_node` batch on a graph-less sprint
bootstraps the graph (`bootstrapped: true`), with judgment-bearing mutations requiring a canonical
Judgment Register row and final validation requiring exact `orchestrates` membership plus explicit
natures; (3) the defaults and fail-closed seams — no graph selects the source-pair-activated
atomic-sequential default, while the queue only projects `active`, `reconciling`, paused, or vacant
waiting reasons; manager/worker dispatch and atomic start/attach select, but reviewer/curator
inspection does not; selection publishes `reconciling` before exact source sync and `active` only
after both recorded bases are current; a malformed selector invalidates only affected runtime
projection/admission and is archived/replaced by the next exact selecting operation; task-document
authoring never reads it; a nature-less commanded master under an authored graph remains a hard
refusal naming `set_nature`; and (4) snapshot-based rollback that restores the pre-authoring tree
rather than re-enabling a compatibility path.

### Invariants And Boundaries

- The inventory never infers edges from file order, names, or status.
- A branch recorded atomic is only reclassified by an accepted strategist/orchestrator ruling.
- Rollback restores the snapshot; it does not retain a dual-reader or feature-switch fallback.
- A missing graph is a scheduling default, not an error; a missing nature under an authored graph
  remains a hard refusal.
- Contract presence never elects the selected master, and the closeout queue owns no activation or
  operation-lifecycle transition.
- Selector corruption is scoped to affected runtime admission/projection and cannot subordinate an
  otherwise-valid task-document mutation.

### Todos

Source claims are reconciled to the frozen implementation. Verification metadata remains pinned to
the previously verified commit until governed closeout can stamp the real new code commit.

## Docs References

No Domain Documentation source is configured for this memory root.

| Finding | Anchor | Source |
| --- | --- | --- |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The read-only inventory the guide documents. | `inventory_execution_topology` | mcp/src/agents_remember/application/task_docs/task_execution_topology.py:917-979 |
| The graph-authoring batch (and graph-less bootstrap) the guide documents. | `author_execution_graph` | mcp/src/agents_remember/application/task_docs/task_execution_topology.py:193-261 |
| Fail-closed validation of a sprint's commanded membership and natures. | `validate_execution_topology` | mcp/src/agents_remember/tasks/document_refs.py:300-350 |
| Exact source-pair activation is the single runtime selection authority and archives malformed snapshots before replacement. | `observe_atomic_series`; `publish_atomic_series_selection` | mcp/src/agents_remember/worktrees/activation/atomic_series_activation.py:170-187; mcp/src/agents_remember/worktrees/activation/atomic_series_activation.py:190-249 |
| Queue waiting reasons observe activation without owning its lifecycle. | `activation_waiting_reason` | mcp/src/agents_remember/worktrees/activation/atomic_series_activation.py:298-311 |

## Cross-Repo References

No meaningful cross-repository reference applies to this repository-owned operator guide.

| Finding | Anchor | Source |
| --- | --- | --- |

## Update History

- 2026-08-26T08:45+02:00 — Restored the canonical Docs/Cross-Repo reference section shape after
  reconciling this changed guide.

- 2026-08-26T08:20+02:00 — Reconciled the operator doctrine card to the frozen source; only the
  future real-code-commit verification stamp remains closeout-owned.

- 2026-08-26T05:20+02:00 — Reconciled the graph-less operator guide with source-pair activation:
  switching selection pauses rather than retires, reconciliation precedes exposure, the queue is a
  disposable observer, selector failure is runtime-scoped, and task authoring remains upstream.
  Final citations and verification remain post-Dagger/closeout-owned.

- 2026-08-19T22:32+02:00 — 260815-DAG-L13: the guide was retitled from migration to authoring —
  `migrate_execution_topology` is gone, the atomic-sequential default covers graph-less sprints,
  and `author_execution_graph` bootstraps the first graph; reworked the procedure, seams, and
  release-notes sections accordingly. Verification remains closeout-owned.

- 2026-08-18T12:00:00+00:00 — 260815-DAG-L9: created as the operator migration/rollback reference for the
  explicit execution-topology cutover. Verification remains closeout-owned.