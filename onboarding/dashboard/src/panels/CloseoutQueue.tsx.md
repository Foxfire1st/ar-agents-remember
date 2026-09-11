# dashboard/src/panels/CloseoutQueue.tsx

| Field                  | Value                                           |
| ---------------------- | ----------------------------------------------- |
| repository             | agents-remember                                 |
| path                   | `dashboard/src/panels/CloseoutQueue.tsx`        |
| doc_type               | `file-level-onboarding`                         |
| lastUpdated            | 2026-08-24T15:04+02:00 |
| lastVerifiedCommitHash | `ae8c47ce897b04380ebcb80f750d77ed4dc9f37d` |
| lastVerifiedCommitDate | 2026-08-26T08:10:26+02:00|
| governingOverview      | `overview.md`                                   |

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

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| Candidate row renders state, grade, and reasons. | `CandidateRow` | dashboard/src/panels/CloseoutQueue.tsx:29-42 |
| Queue section renders service/source condition, source problems, and member list. | `Queue` | dashboard/src/panels/CloseoutQueue.tsx:44-67 |
| Panel selects and renders the projected queues. | `CloseoutQueue` | dashboard/src/panels/CloseoutQueue.tsx:86-86 |


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

## Update History

- 2026-08-24T15:04+02:00 — Migrated the panel from mutable blocker/candidate vocabulary to the
  exact-current service/source/problem/member projection and corrected graph-less sprint mounting.


- 2026-08-20T10:45+02:00 — 260815-DAG-L12:   `CloseoutQueueImpl` gains the optional `sprintRef` scope and the revision/graph meta line (L12-R5). Verified at code commit b7f2c8e2.

- 2026-08-18T00:00+02:00 — 260815-DAG-L8: created the read-only closeout-queue dashboard panel.
  Verification metadata pinned until closeout stamps the L8 commit.