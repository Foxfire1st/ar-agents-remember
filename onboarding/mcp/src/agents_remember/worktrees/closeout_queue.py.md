# mcp/src/agents_remember/worktrees/closeout_queue.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/worktrees/closeout_queue.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-08-19T22:32+02:00 |
| lastVerifiedCommitHash | `b523f53b193e9783e7c7e6410c772e7d64d8df17` |
| lastVerifiedCommitDate | 2026-08-19T21:54:50+02:00|
| governingOverview | `../../../overview.md` |

## Governing Overview

[MCP overview](../../../overview.md)

## Purpose

Owns the mechanistic sprint closeout queue: structural authorization, declaration, logistics,
deterministic selection, current-readiness recomputation, and actor-specific public
projection. It makes facts visible and enforces the ruled order; it does not invent scheduling
judgment.

## Code Commentary

### Logic

The service derives a bounded current graph, resolves the ambient `QueueActor`, applies one
revision-checked/idempotent transition under the store lock, then recomputes projection. Managers
declare and maintain admission facts; the orchestrator records canonical grades, selects the first
ready candidate, and owns blockers. Candidate blockers revalidate task completion, graph revision,
source lineage, candidate trees, route review, curator evidence, grade rows, and ledger facts. Exact
route and curator comparisons are delegated to their evidence owners; this service composes the
returned blocker facts. Since 260815-DAG-L11 the queue is leaf-aware: segment-targeted edges block
exactly that segment's leafs, the response carries `leafPlacementFacts` (unplaced/unknown leafs
with their derived segment placement, reported as facts — never silently auto-written), and the
leaf-aware predecessor/waiting-reason/sort-key lookups are delegated to `closeout_queue_graph.py`,
which owns the leaf-to-node index.

Since 260815-DAG-L13 the `status` read never raises on an absent executionGraph or a
missing/malformed canonical register (L13-R4): `_status_readout` projects a graph-less sprint as
the atomic-sequential default through `_degraded_projection` (mode, register facts, the series
lane owner, and legal next operations), and a graph sprint with malformed registers projects with
`state: degraded` plus repair guidance while mutations stay guarded. The atomic-blocker
transitions moved to `closeout_queue_blocker.py`; the projection now carries `mode`, `registers`,
`laneOwner`, and (for acquire-blocker) `acquisitionFacts`. The lane owner is the one candidate in
a lane-occupying state (`LANE_OCCUPYING_STATES` — selected, closeout-in-flight,
integration-in-flight; a certified candidate no longer occupies the lane), a blocker-held waiting
reason names the owner candidate, and stale-base blockers name `worktree_sync` as the recovery.

### Conventions

Judgment is consumed only from canonical sprint Judgment/Priority Registers. Equal categorical
priority uses graph node order and then the leaf key. Ordinary and atomic masters share leaf
candidate mechanics; atomic blockers add exclusivity and exact block-landing proof.

### Invariants And Boundaries

- Actor role and task identity are plane-proven, never request data.
- Only the deterministic first ready candidate may be selected.
- In-flight records are lifecycle-owned and immutable through public actions.
- The `status` read degrades to a facts projection instead of failing on an absent graph or
  malformed registers; only mutations stay guarded.
- Atomic-blocker acquisition requires atomic nature, drained predecessors and landing lane
  (lane-occupying states only), a non-blank rationale, and the atomic series base to still match
  the current code+memory super tips; refusals carry structured owner/in-flight facts.
- A normal atomic-blocker release requires the completed atomic master to prove one exact landed
  series; abort requires a canonical strategist/orchestrator judgment.
- Projection reports only operations legal for the current structural caller.

### Todos

None recorded.

## Docs References

No configured Domain Documentation source applies; queue doctrine is repository-internal.

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| Structural authorization separates manager logistics from orchestrator grade/selection authority. | `QueueActor` | mcp/src/agents_remember/worktrees/closeout_queue.py:117-123 |
| Mutations re-read the graph under lock before returning a projection. | `closeout_queue_tool` | mcp/src/agents_remember/worktrees/closeout_queue.py:185-251 |
| The status readout degrades graph-less or register-degraded sprints to a facts projection. | `_status_readout`; `_degraded_projection` | mcp/src/agents_remember/worktrees/closeout_queue.py:254-307; mcp/src/agents_remember/worktrees/closeout_queue.py:323-367 |
| Selection takes only the deterministic first ready candidate. | `_apply_candidate_action` | mcp/src/agents_remember/worktrees/closeout_queue.py:400-464 |
| Declaration binds exact code, memory, ledger, review, curator, and source-lineage facts before history moves. | `_declare_candidate` | mcp/src/agents_remember/worktrees/closeout_queue.py:466-474 |
| Candidate projection separates ready, waiting, blocked, and in-flight facts and reports `leafPlacementFacts`. | `_projection` | mcp/src/agents_remember/worktrees/closeout_queue.py:608-646 |

## Cross-Repo References

No external repository owns this queue.

## 260815-DAG-L4 Integration-Authority Impact

L4 makes task-derived integration refs mechanically non-ordinary: repository defaults, sprint supers, and active atomic-series refs are censused across code and external memory. Mutation is admitted only through exact lifecycle authority, named-ref compare-and-swap, queue/repository serialization, or a terminal capability; stale topology, aliases, ambient checkouts, and torn recovery fail closed.

## Update History

- 2026-08-19T22:32+02:00 — 260815-DAG-L13: the `status` read degrades instead of raising — a
  graph-less sprint projects the atomic-sequential default with its series lane owner and legal
  next operations, and malformed registers degrade the projection while mutations stay guarded.
  Atomic-blocker transitions extracted to `closeout_queue_blocker.py`; the projection gains
  `mode`/`registers`/`laneOwner`/`acquisitionFacts`; lane ownership narrows to lane-occupying
  states; the blocker-held reason names the owner candidate; stale-base blockers name
  `worktree_sync`. Verification remains closeout-owned.

- 2026-08-19T08:55+02:00 — 260815-DAG-L11: the queue is leaf-aware — segment-targeted edges block
  exactly that segment's leafs (completion stays master-granular), the projection reports
  `leafPlacementFacts`, and leaf-aware predecessor/waiting-reason/sort-key helpers moved to
  `closeout_queue_graph.py` (file-size rail; public surface unchanged). Verification remains
  closeout-owned.

- 2026-08-18T09:05+02:00 — Renamed the atomic 'barrier' concept to 'blocker' throughout (terminology unification; no behavioral change). Verification remains closeout-owned.

- 2026-08-18T01:24+02:00 — 260815-DAG-L6: blocker acquisition now requires the atomic series base to still match the current code+memory super tips (`require_source_bases_current`), closing R2. Verification remains closeout-owned.

- 2026-08-15T23:38+02:00 — Reconciled this worktree owner's role in task-derived protected-ref authority, exact named-ref movement, and crash-safe recovery. Verification metadata remains closeout-owned.

- 2026-08-15T14:05+02:00 — No content impact: the final targeted-gate repair expresses the
  post-authorization selection arm as the exhaustive remaining action; authorization still owns
  the fail-closed action vocabulary and selection policy is unchanged.
- 2026-08-15T13:08+02:00 — No content impact: Ruff split the aliased graph-context import from
  its unaliased sibling; both names still resolve from the same canonical graph owner.
- 2026-08-15T12:53+02:00 — No content impact: removed an unreachable duplicate candidate-action
  assertion and normalized the split graph import; the single fail-closed dispatch owner and all
  queue policy remain unchanged.
- 2026-08-15T11:25+02:00 — L3 static-gate repair: delegated exact route/curator comparisons to
  their evidence owners and used scoped exception suppression for optional recovery evidence;
  candidate projection and blocker vocabulary are unchanged.
- 2026-08-15T11:07+02:00 — L3 Dagger repair: a closeout-in-flight candidate whose contract was
  committed before certification is projected through post-closeout recovery with refreshed
  memory evidence; route-review failures remain isolated so exact candidate-tree drift is visible.
- 2026-08-15T09:53+02:00 — No content impact: L3's Pyright repair now preserves already-modeled
  task references and constructs the existing scheduling-grade input explicitly; queue policy,
  evidence comparison, and projection behavior are unchanged.
- 2026-08-15T09:10+02:00 — Created for L3's dependency-aware, actor-authorized sprint closeout queue; verification remains closeout-owned.
