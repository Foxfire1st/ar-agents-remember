# skills/l-01-agent-lifecycles/roles/designer.md

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | skills/l-01-agent-lifecycles/roles/designer.md |
| doc_type | file-level-onboarding |
| lastUpdated | 2026-08-30T12:34+02:00 |
| lastVerifiedCommitHash | `f9f92ca793811b6cb738d7e302dfecdf8636e96e` |
| lastVerifiedCommitDate | 2026-08-30T14:26:46+02:00|
| governingOverview | skills/l-01-agent-lifecycles/roles/overview.md |

## Governing Overview

Governing overview: skills/l-01-agent-lifecycles/roles/overview.md

## Purpose

The optional sprint-bound design seat and the drawing-board method an architect may collapse inline
when a separate design conversation would add no value.

## Code Commentary

### Logic

The designer binds to `(sprint document, designer)`, has no leaf worktree, and returns a master-scoped
task design plus its declared cross-master blind spot to the architect. It reframes intent, retrieves
evidence, measures the within-master blast radius, authors the requirement-derived task topology,
and never implements. A dispatched designer uses `message_parent`; an architect may perform the
same method inline without changing roles.

When separately hosted, designer is target-only. Its architect ordinarily creates or switches the
seat with one `dispatch_agent` call on the sprint document and is the plane-hosted caller. An
identity-free developer launcher may target the designer only for an explicit task-seat takeover;
the designer itself has no dispatch caller authority or ambient recovery route. Its role-table
dispatch/tools rows are structural documentation, not settings keys.

### Invariants And Boundaries

- The designer is a seat when dispatched, not an architect role mutation; inline use is explicit
  architect hat-collapse.
- It is sprint-bound, worktree-free, and master-scoped; portfolio collision review remains downstream.
- Canonical lifecycle doctrine owns this source; generated copies are synchronization outputs.

## Docs References

No relevant documentation was configured in the resolved source registry; task artifacts and the final candidate are the direct evidence.

## Repo-Internal References

`skills/l-01-agent-lifecycles/roles/designer.md` is the canonical role contract; the governing role
overview supplies the shared lifecycle frame.

## Cross-Repo References

No meaningful cross-repo references.

## Update History

- 2026-08-30T12:34+02:00 — 260821-ARSPAWN-L3 classified separately hosted designer as target-only,
  replaced the stale Operations creator with architect-owned dispatch, and distinguished explicit
  ambient takeover from ordinary plane creation. Verification remains closeout-owned.

- 2026-08-28T14:15+02:00 — Replaced the generic dispatch placeholder with the current optional
  sprint-bound designer contract, inline architect collapse, worktree-free boundary, structural
  parent handoff, and master-scoped limitation; stamped the landed candidate.

- 2026-07-12T14:20:00+02:00 — 260712-TRH-L4 curator refresh: final candidate onboarding; exact-session dispatch and serialized-writer/lock-free-reader concurrency recorded.
