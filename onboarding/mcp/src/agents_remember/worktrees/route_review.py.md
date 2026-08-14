# mcp/src/agents_remember/worktrees/route_review.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/worktrees/route_review.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-08-14T05:26Z |
| lastVerifiedCommitHash | `100b40d6be4a7d03eedbb1164ce54e2e8a314038` |
| lastVerifiedCommitDate |  2026-08-14T08:23:37+02:00|
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
`require_current_route_review` skips unchanged leaves, otherwise resolves the canonical leaf doc,
requires a passing record for the exact current tree, and rechecks its evidence files.

### Conventions

Public failures use a typed status on `RouteReviewError`; private candidate identity is derived from
the contract with an isolated temporary Git index.

### Invariants And Boundaries

- Agents never author `candidateTree` or `reviewedAt`.
- Route review belongs only to leaf altitude and is required for code-changing leaves.
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
| Curator and closeout admission require a passing record for the current candidate tree. | `require_current_route_review` | mcp/src/agents_remember/worktrees/route_review.py:74-111 |

## Cross-Repo References

No cross-repository implementation source governs route review.

## Update History

- 2026-08-14T05:26Z — Created for L23's mandatory candidate-bound independent route-review gate.
  Verification remains closeout-owned until the source commit exists.
