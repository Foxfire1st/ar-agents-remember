# dashboard/src/panels/CloseoutQueue.tsx

| Field                  | Value                                           |
| ---------------------- | ----------------------------------------------- |
| repository             | agents-remember                                 |
| path                   | `dashboard/src/panels/CloseoutQueue.tsx`        |
| doc_type               | `file-level-onboarding`                         |
| lastUpdated            | 2026-08-18T00:00+02:00                          |
| lastVerifiedCommitHash | `2597ff98306ba7c7963005092ac597c4972e63ce`      |
| lastVerifiedCommitDate | 2026-08-18T15:45:32+02:00|
| governingOverview      | `overview.md`                                   |

## Governing Overview

[overview.md](overview.md)

## Purpose

The dashboard's read-only closeout-queue panel (L8-R4/R5/R6): one ordered list per sprint — the active
atomic blocker first, then every candidate with its queue state, grade, and the exact reasons it is not
selectable. It renders the projected `closeoutQueues` verbatim and never infers readiness from titles,
numbering, labels, or open terminals.

## Code Commentary

### Logic

`CloseoutQueueImpl` selects `state.closeoutQueues` from the store and renders nothing when empty. Each
`Queue` renders the sprint ref, the optional blocker (with rationale), and a `CandidateRow` per candidate
(name, state · grade, and joined reasons). React keys derive from `repository/path` because the wire
`TaskDocumentRef` carries no `key` field.

### Invariants And Boundaries

- Read-only: no scheduling mutation is issued from this panel; every mutation stays task-addressed.
- Candidate facts are rendered verbatim; readiness is never re-derived client-side.

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| Candidate row renders state, grade, and reasons. | `CandidateRow` | dashboard/src/panels/CloseoutQueue.tsx:29-42 |
| Queue section renders the blocker and candidate list. | `Queue` | dashboard/src/panels/CloseoutQueue.tsx:44-61 |
| Panel selects and renders the projected queues. | `CloseoutQueue` | dashboard/src/panels/CloseoutQueue.tsx:63-75 |

## Update History

- 2026-08-18T00:00+02:00 — 260815-DAG-L8: created the read-only closeout-queue dashboard panel.
  Verification metadata pinned until closeout stamps the L8 commit.
