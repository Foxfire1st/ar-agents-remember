# skills/w-02-light-task-workflow/workflow.md

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `skills/w-02-light-task-workflow/workflow.md` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-08-28T11:32+02:00 |
| lastVerifiedCommitHash | a06d2ffcfae2c277f2ae19330c17d09c616b77e8 |
| lastVerifiedCommitDate | 2026-08-28T13:58:55+02:00 |
| governingOverview | `onboarding/overview.md` |

## Governing Overview

[repository onboarding overview](../../overview.md)

## Purpose

This workflow governs the planning, approval, implementation, evidence, and closeout lifecycle for
one light task or a master plus light-subtask series.

## Code Commentary

### Logic

Phase 0 compiles independently falsifiable obligations into stable, versioned canonical packets,
cold-reads them, and obtains developer approval before any task topology exists. Later phases
project those exact revisions into tasks, implement against a live checklist, maintain one
acceptance envelope per revision, and require independent adjudication before closure.

A changed obligation creates a new version-addressed packet, invalidates only affected acceptance,
updates affected projections, and rebriefs affected leaves. Task documents summarize topology and
never become alternate requirement authorities.

Delivery attempts form a separate append-only axis and advance only when an exact candidate is
handed to independent review, or after rejection when its successor is handed off. Internal
implementation/test/evidence reruns remain separate protocol events. Lightweight worker records
bind exact candidates, requirement-specific facts, predecessors, and content-addressed expanded
evidence; reviewer records independently adjudicate those attempts, and failure classes determine
recovery ownership. Leaf journals remain authority. A rebuildable master summary exposes formal
attempts/rejections/current state/dominant class, excludes protocol events, and cannot gate or lock
any task, lifecycle, closeout, integration, or queue operation.

### Conventions

- Use one planning wrapper with `requirements/README.md` and immutable revision packets.
- Tool-managed light tasks are JSON-primary and rendered through `task_doc`.
- Decision logs are append-only and timestamps use `YYYY-MM-DDTHH:MM`.
- Escalate to a master series when the implementation plan no longer fits one page.

### Invariants And Boundaries

- No sprint, master, task, or leaf is authored before corpus approval.
- Every leaf owns exactly one primary requirement revision.
- One revision may have multiple independently executable manifestation leaves.
- Requirement acceptance and durable-evidence lifecycle remain independent gates.
- Worktree commits still require their separate approval.
- Accepted attempts reopen only through independently proven regression plus owner-recorded bounded
  invalidation, or an approved semantic revision.

### Todos

None.

## Docs References

No external Domain Documentation source governs this workflow.

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| Requirement compilation, cold read, and approval precede topology. | `## Phase 0 — Compile And Approve Requirements Before Task Topology` | skills/w-02-light-task-workflow/workflow.md:16-49 |
| Tasks carry filtered projections rather than rewritten contracts. | `## Phase 1 — Project The Approved Corpus Into Task Documents`; "### 7. Write `task.md`" | skills/w-02-light-task-workflow/workflow.md:50-175 |
| Implementation maintains one acceptance block per exact revision. | `## Phase 2 — Implement Against The Live Checklist` | skills/w-02-light-task-workflow/workflow.md:176-254 |
| Requirement changes version, invalidate, update, and rebrief affected work. | `## Three-touch iteration cycle` | skills/w-02-light-task-workflow/workflow.md:284-315 |
| Phase 2 and closure append exact worker/reviewer records, while master-series summaries remain rebuildable and non-gating. | `## Phase 2 — Implement Against The Live Checklist`; `## Phase 3 — Close`; `## Master Task Series` | skills/w-02-light-task-workflow/workflow.md:176-254; skills/w-02-light-task-workflow/workflow.md:255-329; skills/w-02-light-task-workflow/workflow.md:330-387 |

## Cross-Repo References

The context resolver supplies target-repository paths, tools, and memory policy; this workflow does
not hard-code them.

## 2026-08-27 Attempt Boundary Clarification

Attempt publication is phase-sensitive: validate before append, and treat append plus the exact
review handoff as one formal boundary. A malformed row that never reached review is preserved by a
non-attempt correction/void record without consuming the next attempt ID; after handoff, only an
independent reviewer rejection permits a successor.

## Update History

- 2026-08-28T11:32+02:00 — No content impact: re-read the v25 role/topology clarification; this
  card already describes one leaf-owned primary revision, adjacent contextual constraints, and
  the source-specific worker/reviewer/manager/curator boundary.

- 2026-08-27T22:15+02:00 — Distinguished pre-handoff non-attempt correction from post-handoff
  reviewer rejection and successor lineage.

- 2026-08-27T21:53+02:00 — M40@v2/M44@v2: formal attempts now advance only at review handoff;
  internal protocol events stay separate and journal records link frozen expanded evidence.
- 2026-08-27T19:59+02:00 — M42 clarification: prevented ordinary candidate churn from globally
  reopening accepted requirement manifestations.
- 2026-08-27T18:06+02:00 — M40-M45: added immutable worker/reviewer attempt records, successor
  lineage, failure ownership, bounded invalidation, and leaf-authoritative/non-gating master
  summary behavior.
- 2026-08-27T14:52+02:00 — Created onboarding for the architect-owned requirement compilation gate,
  one-primary topology, version invalidation, and per-revision evidence flow.
