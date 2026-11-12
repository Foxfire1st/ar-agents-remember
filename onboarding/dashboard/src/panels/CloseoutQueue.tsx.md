# dashboard/src/panels/CloseoutQueue.tsx

## Governing Overview

[overview.md](overview.md)

## Purpose

The dashboard's read-only closeout-queue panel: one exact-current disposable scheduling projection
per sprint. It renders service/source condition, bounded source problems with their repair action,
and generation-keyed members with producer-owned classification, priority, order, and reasons. It
never infers readiness from titles, numbering, labels, task prose, or open terminals.

## Code Commentary

### Logic

`CloseoutQueueImpl` selects `state.closeoutQueues` from the store and renders nothing when empty. Each
`Queue` renders revision, service condition, optional source classification, each typed source problem,
and a `MemberRow` per projection member. Member keys use immutable `generationId`; display rows show
classification and priority plus joined reasons.

### Invariants And Boundaries

- Read-only: no scheduling mutation is issued from this panel; every mutation stays task-addressed.
- Projection facts are rendered verbatim; readiness is never re-derived client-side.
- The producer vocabulary permits member classification `ready`, `waiting`, or `blocked`. Those are
  view classifications over waiting door generations, not durable lifecycle dispositions.

## Evidence

### Repo-Internal References

- Candidate row renders state, grade, and reasons. [1]
- Queue section renders service/source condition, source problems, and member list. [2]
- Panel selects and renders the projected queues. [3]


## 260815-DAG-L12 Sprint-Scoped Mount

`CloseoutQueueImpl` takes an optional `sprintRef`: on a sprint page the panel filters
`state.closeoutQueues` to the viewed sprint via `sameTaskDocumentRef`; without a ref it stays
workspace-wide. The heading shows revision and current service/source condition. Empty global or scoped
projections still render `null`. The panel is mounted independently of an optional execution graph, so
graph-less atomic-sequential sprints retain scheduling visibility.


## 260821-CLIVE Projection-Only Authority

The component observes a disposable projection only. Queue rows do not own claims, lifecycle state,
commit evidence, certification, recovery, or terminal authority; invalid projection state is shown as
typed repair evidence rather than being hidden behind a stale candidate/blocker view.
