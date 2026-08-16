# mcp/src/agents_remember/worktrees/route_review.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/worktrees/route_review.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-08-14T09:08+02:00 |
| lastVerifiedCommitHash | `8bf6edad7e7e65e27cf735be0822f604531d0c8a` |
| lastVerifiedCommitDate |  2026-08-16T10:54:02+02:00|
| governingOverview | `../../../overview.md` |

## Governing Overview

[mcp overview](../../../overview.md)

## Purpose

Own the control-plane binding between independent route-review evidence and the exact current leaf
candidate tree. Curator admission and closeout consume this proof so a review cannot silently apply
to a later code change.

## Code Commentary

### Logic

`build_route_review` accepts only reviewer-authored verdict, evidence, and route rows; the plane
derives candidate tree and review time and verifies every evidence path stays inside the task root.
`require_current_route_review` first excludes series/master altitude because route-review records
are leaf-owned, then skips unchanged leaves. A changed leaf resolves its canonical task document,
requires a passing record for the exact current tree, and rechecks its evidence files.

### Conventions

Public failures use a typed status on `RouteReviewError`; private candidate identity is derived from
the contract with an isolated temporary Git index.

### Invariants And Boundaries

- Agents never author `candidateTree` or `reviewedAt`.
- Route review belongs only to leaf altitude and is required for code-changing leaves; series
  closeout must not attempt candidate-tree or terminal-leaf resolution.
- Blocking, missing, stale, outside-task, and missing-file evidence all fail closed.
- Evidence references are task-relative and may not escape the task root.
- This module validates evidence; it does not perform review or mutate source.

### Todos

None recorded.

## Docs References

No configured Domain Documentation source applies.

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The plane stamps reviewer payloads with the exact candidate and validates task-local evidence. | `build_route_review`; `_require_evidence_files` | mcp/src/agents_remember/worktrees/route_review.py:42-71; mcp/src/agents_remember/worktrees/route_review.py:114-134 |
| Series altitude is excluded before leaf resolution; changed leaves require a passing record for the current candidate tree. | `require_current_route_review` | mcp/src/agents_remember/worktrees/route_review.py:74-113 |

## Cross-Repo References

No cross-repository implementation source governs route review.

## R39 Route-Review Altitude

Current-route-review returns not-required-master-altitude before probing candidate or leaf
task-document state for non-leaf contracts. Candidate-bound independent review remains a leaf
closeout requirement; series/master closeout does not impersonate a terminal leaf.

## 260815-DAG-L4 Integration-Authority Impact

L4 makes task-derived integration refs mechanically non-ordinary: repository defaults, sprint supers, and active atomic-series refs are censused across code and external memory. Mutation is admitted only through exact lifecycle authority, named-ref compare-and-swap, queue/repository serialization, or a terminal capability; stale topology, aliases, ambient checkouts, and torn recovery fail closed.

## Update History

- 2026-08-15T23:38+02:00 — Reconciled this worktree owner's role in task-derived protected-ref authority, exact named-ref movement, and crash-safe recovery. Verification metadata remains closeout-owned.

- 2026-08-14T11:25+02:00 — R39 curator: documented the explicit non-leaf route-review bypass.
  Verification remains closeout-owned.

- 2026-08-14T09:08+02:00 — Reopened L23 repair: excluded series/master closeout before
  candidate-tree and terminal-leaf resolution. Independent route-review authority remains
  leaf-only; verification metadata remains closeout-owned.
- 2026-08-14T05:26Z — Created for L23's mandatory candidate-bound independent route-review gate.
  Verification remains closeout-owned until the source commit exists.
