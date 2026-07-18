# dashboard/src/panels/session-cockpit/ChatContextBar.test.tsx

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `dashboard/src/panels/session-cockpit/ChatContextBar.test.tsx` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-07-18T15:22+02:00 |
| lastVerifiedCommitHash | `31f58834f86c0d98e26b0896e099a2403a8729ee` |
| lastVerifiedCommitDate |  2026-07-18T15:41:39+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[session-cockpit overview](overview.md)

## Purpose

Pins lifecycle-routing honesty and server-first leaf attachment for the canonical Chats duty bar.

## Code Commentary

### FEUI MX-FIX-2 Raw Caller Matrix

The suite proves one accepted raw response creates and focuses the exact server id once. A network
failure and the Round 1 contradictory raw harness/control response both render their typed alerts,
leave the registry empty, and never invoke the focus callback.

Tests distinguish the explicitly local lifecycle patch from leaf authority, prove successful leaf
move sends the exact route/body and broadcasts invalidation, and prove a 409 same-role refusal leaves
the local row unchanged while surfacing an alert.

### Logic

The suite drives the raw create control through the real session store with request-matched
`Response` fixtures, then observes registry rows, alert copy, and the `onSessionOpened` callback. Leaf
attach/move cases use URL-aware fetch fixtures and broadcast doubles.

### Conventions

Stable `data-testid` seams locate the raw control and alert. Store and global transport state are
reset between cases so exact-one focus and zero-ghost assertions remain isolated.

### Invariants And Boundaries

Only an accepted server id may reach the focus callback. Network, protocol, and same-role attach
failure must leave the prior registry/focus state unchanged and visible to the operator.

### Todos

No task-independent technical debt was identified during MX-FIX-2 review.

## Docs References

The curator checked the memory repository's `system/sources.md`; it has no configured Domain
Documentation entries. This card was verified from its direct source/tests and the reviewed L8
task/worker/reviewer evidence.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No configured Domain Documentation source exists for this file. | `system/sources.md` checked | — |

## Cross-Repo References

The suite exercises repository-local routing and browser broadcast doubles; no cross-repository source applies.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No applicable cross-repository source was found. | Import and task-boundary review | — |

## Repo-Internal References

| Finding | Source Path |
| --- | --- |
| Unit under test. | [ChatContextBar.tsx](ChatContextBar.tsx) |

## Update History

- 2026-07-18T15:22+02:00 — FEUI MX-FIX-2: added exact-one accepted raw focus plus network and
  contradictory-authority failure regressions with zero row and zero focus. Verification metadata
  remains pinned until closeout.

- 2026-07-18T07:22+02:00 — Created for FEUI-L8 Chats duty-bar regressions; verification metadata
  remains blank until commit.
