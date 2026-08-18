# mcp/src/agents_remember/worktrees/orchestration_portfolio.py

| Field                  | Value                                                        |
| ---------------------- | ------------------------------------------------------------ |
| repository             | agents-remember                                              |
| path                   | `mcp/src/agents_remember/worktrees/orchestration_portfolio.py` |
| doc_type               | `file-level-onboarding`                                      |
| lastUpdated            | 2026-08-18T00:00+02:00                                       |
| lastVerifiedCommitHash | `e460d4c000983d96a3ef6d105a1aeecbb73d5dc5`                   |
| lastVerifiedCommitDate | 2026-08-18T13:41:53+02:00|
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
missing grade, and an atomic master without an active blocker). `choose(frontier)` applies the canonical
priority rank, then graph node order, then task key. `manager_slice(graph, state, master_ref)` builds
the per-master graph/queue slice a manager needs (nature, incomplete predecessors, their own
candidates with readiness).

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
| The durable decision record carries kind, reshape kind, subject, and rationale. | `OrchestratorDecision` | mcp/src/agents_remember/worktrees/orchestration_portfolio.py:44-56 |
| Reshape classification folds four signals into ordinary/substantial. | `classify_reshape` | mcp/src/agents_remember/worktrees/orchestration_portfolio.py:92-105 |
| Frontier recomputation mirrors the queue's waiting reasons. | `recompute_frontier` | mcp/src/agents_remember/worktrees/orchestration_portfolio.py:135-157 |
| Deterministic selection by priority, node order, then key. | `choose` | mcp/src/agents_remember/worktrees/orchestration_portfolio.py:160-172 |
| Manager slice scopes candidates to the owning master. | `manager_slice` | mcp/src/agents_remember/worktrees/orchestration_portfolio.py:175-208 |

## Update History

- 2026-08-18T00:00+02:00 — 260815-DAG-L7: created the orchestrator portfolio loop (decision record,
  reshape classification, frontier recomputation, deterministic choice, manager slice). Verification
  metadata pinned until closeout stamps the L7 commit.
