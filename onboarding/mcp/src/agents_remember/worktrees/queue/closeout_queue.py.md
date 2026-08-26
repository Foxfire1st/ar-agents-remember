# mcp/src/agents_remember/worktrees/queue/closeout_queue.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/worktrees/queue/closeout_queue.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-08-26T08:20+02:00 |
| lastVerifiedCommitHash | `ae8c47ce897b04380ebcb80f750d77ed4dc9f37d` |
| lastVerifiedCommitDate | 2026-08-26T08:10:26+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[governing route overview](overview.md)

## Purpose

Owns the sprint-scoped status/rebuild facade and the exact first-ready waiting-generation admission
check for the disposable closeout projection.

## Code Commentary

### Logic

`closeout_queue_tool` structurally authorizes the sprint caller and serves effective status or an
idempotent rebuild. `require_first_ready_generation` is called only while its caller holds the
short task/door publication mutex; it rechecks the exact current projection and admits only the
named first-ready waiting generation. All candidate construction, source census, member readiness,
and publication effects delegate to the projection modules.

### Conventions

Judgment and priority are read from canonical sources during projection construction. Equal
effective priority uses graph declaration order and then leaf identity. A graph-less
atomic-sequential sprint remains valid; its waiting reasons observe the strict source-pair
activation snapshot rather than electing a series from contract presence.

### Invariants And Boundaries

- Only status and rebuild are public queue actions.
- Only the deterministic first-ready waiting generation passes the claim-admission fence.
- Task edits and door controls remain canonical even when rebuild fails.
- In-flight records, commits, certification, integration, and lifecycle controls are journal-owned.
- There is no persistent blocker, release, abort, declared-candidate, or queue-owned grade action.
- Activation is read-only input to projection; this facade cannot select, pause, activate, or vacate
  a master.

### Todos

Activation-related claims are reconciled to the frozen projection behavior. Verification metadata
remains closeout-owned.

## Docs References

No configured Domain Documentation source applies; queue doctrine is repository-internal.

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The facade serves status and idempotent rebuild. | `closeout_queue_tool` | mcp/src/agents_remember/worktrees/queue/closeout_queue.py:33-83 |
| Claim admission requires the exact first-ready waiting generation. | `require_first_ready_generation` | mcp/src/agents_remember/worktrees/queue/closeout_queue.py:86-112 |

## Cross-Repo References

No external repository owns this queue.

## 260815-DAG-L4 Integration-Authority Impact

L4 makes task-derived integration refs mechanically non-ordinary: repository defaults, sprint supers, and active atomic-series refs are censused across code and external memory. Mutation is admitted only through exact lifecycle authority, named-ref compare-and-swap, queue/repository serialization, or a terminal capability; stale topology, aliases, ambient checkouts, and torn recovery fail closed.

## 260821-CLIVE Status/Rebuild Facade

The command processor is reduced to sprint-scoped `status` and idempotent `rebuild`, plus
`require_first_ready_generation` for the short claim admission fence. That fence runs while the
caller holds the task/door CAS and requires the exact first ready waiting generation. Declare,
grade, claim, certify, block, release, abort, and integration-completion mutations are removed. Task
authoring is never gated by this facade.

## IAS Activation Projection Boundary

The facade remains status/rebuild plus first-ready admission. For graph-less atomic work,
projection helpers derive active/reconciling/paused/vacant waiting reasons from the exact selector
snapshot. Contract presence is not a lane owner, selector corruption makes only the affected
projection invalid-empty, and no queue action mutates activation or operation lifecycle.


## PDLS Reconciliation

Projection access now recognizes the exact sprint planning actor and commanded manager set; queue authorization no longer subordinates task authoring or infers managers from unrelated topology.

This change preserves the file's existing authority boundary. No threshold exception, silent
fallback, or compatibility reader was added.
## Update History

- 2026-08-26T08:20+02:00 — Final frozen reconciliation: the queue observes activation only as
  disposable projection input and retains no transition or lifecycle authority.

- 2026-08-26T05:20+02:00 — Removed the obsolete lane-owner reading from current onboarding and
  recorded activation as read-only projection input. Verification remains post-Dagger-owned.

- 2026-08-25T15:44+02:00 — PDLS whole-system reconciliation updated the implementation summary
  above after source and requirement review. Verification remains closeout-owned.


- 2026-08-24T14:43+02:00 — 260821-CLIVE cumulative curation: replaced mutable queue commands with status/rebuild and exact first-ready admission. Timestamp is the curator host's Europe/Berlin system time; verification remains closeout-owned.

- 2026-08-23T16:08+02:00 — 260821-CLIVE-L2: reconciled this card with the accepted full L2 candidate; verification metadata remains pinned until architect-owned closeout stamps the real code commit.

- 2026-08-21T00:45+02:00 — 260815-DAG master full-gate repair: source moved to `mcp/src/agents_remember/worktrees/queue/closeout_queue.py` (new package route); the citation fixer repointed in-body references; import paths updated inside the module. Verified at code commit e5cb139f.


- 2026-08-20T09:35+02:00 — 260815-DAG-L16: the declare path's contract-bound refusals now name
  the missing binding and the recovery (L16-R9: leaf worktree contract or the direct landing
  operation), and a `ContractError` on load wraps as `closeout-candidate-contract-invalid`. The
  queue's identity invariant is updated to the declared-caller reality (L16-R2/F5). Verified at
  code commit a9d50e08.


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
