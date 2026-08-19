# mcp/src/agents_remember/worktrees/orchestration_portfolio.py

| Field                  | Value                                                        |
| ---------------------- | ------------------------------------------------------------ |
| repository             | agents-remember                                              |
| path                   | `mcp/src/agents_remember/worktrees/orchestration_portfolio.py` |
| doc_type               | `file-level-onboarding`                                      |
| lastUpdated            | 2026-08-19T08:55+02:00                                       |
| lastVerifiedCommitHash | `f2e2f4b9c18d89cc0f5c901f43831e014701aae0`                   |
| lastVerifiedCommitDate | 2026-08-19T11:32:36+02:00|
| governingOverview      | `../../../overview.md`                                       |

## Governing Overview

[MCP overview](../../../overview.md)

## Purpose

Implements the orchestrator's event-driven portfolio loop over the authoritative closeout queue
(L7). It is the intelligence layer over the fact-producing scheduler: the queue already projects
candidates and enforces deterministic selection, so this module adds the durable orchestrator
*decision* record, reshape classification, dependency-safe frontier recomputation, deterministic
choice, and the manager graph/queue slice — without a seat-local watcher or re-deriving order from
transcripts, branch names, or labels.

## Code Commentary

### Logic

`OrchestratorDecision` is a strict frozen record of one orchestrator portfolio decision (selection,
reprioritization, withdrawal, failure handling, or strategist escalation) with recorded rationale.
`classify_reshape(...)` folds the four L7-R4 reshape signals — edge change, master reclassification,
large leaf move, and new common foundation — into `substantial`, otherwise `ordinary`.
`recompute_frontier(graph, state)` returns the dependency-safe frontier of grade-current, unblocked
candidates; `_frontier_ready` mirrors the queue's remaining waiting reasons (incomplete predecessors,
missing grade, and an atomic master without an active blocker) — since 260815-DAG-L11 through the
leaf-aware `candidate_node` lookup, so a candidate is judged on its own lump or segment node, with
an unmappable leaf falling back conservatively to the master's predecessor union; `_candidate_order`
ranks by the candidate node's declaration order (or the master's earliest node). `choose(frontier)`
applies the canonical priority rank, then graph node order, then task key. `manager_slice(graph,
state, master_ref)` builds the per-master graph/queue slice a manager needs (nature, incomplete
predecessors, their own candidates with readiness).

### Conventions

Every function is pure over `QueueGraphContext` + `CloseoutQueueState` (or plain models). Nothing
mutates the queue, writes a file, or spawns a background loop; mechanical/evidence blockers (source,
ledger, route, curator) and in-flight lane ownership stay with the queue's declaration-time validation
and selection.

### Invariants And Boundaries

- The frontier never admits a candidate with an incomplete predecessor, a missing grade, or an
  atomic master without an active blocker.
- Choice is deterministic: priority rank, then node order, then task key.
- Substantial reshapes are escalated, never auto-decided; ordinary changes stay with the orchestrator.
- Managers see only their own master's slice; the global lane and integration order stay task-addressed.

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The durable decision record carries kind, reshape kind, subject, and rationale. | `OrchestratorDecision` | mcp/src/agents_remember/worktrees/orchestration_portfolio.py:48-60 |
| Reshape classification folds four signals into ordinary/substantial. | `classify_reshape` | mcp/src/agents_remember/worktrees/orchestration_portfolio.py:96-109 |
| Frontier recomputation mirrors the queue's waiting reasons. | `recompute_frontier` | mcp/src/agents_remember/worktrees/orchestration_portfolio.py:145-168 |
| Deterministic selection by priority, node order, then key. | `choose` | mcp/src/agents_remember/worktrees/orchestration_portfolio.py:180-192 |
| Manager slice scopes candidates to the owning master. | `manager_slice` | mcp/src/agents_remember/worktrees/orchestration_portfolio.py:195-230 |

## Update History

- 2026-08-19T08:55+02:00 — 260815-DAG-L11: the frontier is leaf-aware — `_frontier_ready` and
  `_candidate_order` resolve the candidate's own lump/segment node via `candidate_node` and fall
  back conservatively to the master's node union/earliest node for an unmappable leaf. Verification
  remains closeout-owned.

- 2026-08-18T00:00+02:00 — 260815-DAG-L7: created the orchestrator portfolio loop (decision record,
  reshape classification, frontier recomputation, deterministic choice, manager slice). Verification
  metadata pinned until closeout stamps the L7 commit.
