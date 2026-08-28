# skills/w-02-light-task-workflow/master-template.md

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `skills/w-02-light-task-workflow/master-template.md` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-08-28T11:32+02:00 |
| lastVerifiedCommitHash | a06d2ffcfae2c277f2ae19330c17d09c616b77e8 |
| lastVerifiedCommitDate | 2026-08-28T13:58:55+02:00 |
| governingOverview | `onboarding/overview.md` |

## Governing Overview

[repository onboarding overview](../../overview.md)

## Purpose

This template defines a master plus flat light-subtask series when one task no longer fits a
single-page plan. It connects one integration branch and multiple leaf enclosures to the approved
requirement corpus.

## Code Commentary

### Logic

The master carries a filtered table of stable IDs, exact versions, canonical packet links, and
manifestation leaves. Each leaf names exactly one primary revision and may reference adjacent
dependency or preservation constraints. Subtasks close incrementally into the master branch;
the master owns the single release boundary.

The scaffold includes a Requirement Attempt Summary with attempts, rejection history/count,
current state, dominant open failure class, and authoritative leaf-journal links. It is regenerated
from immutable worker/reviewer records and is explicitly non-gating; leaf journals win every
conflict or stale-summary case.

Only formal review-handoff attempts appear in that summary. Internal implementation/test/evidence
runs remain separate protocol events. Leaf records stay lightweight and requirement-specific by
linking content-addressed frozen expanded evidence instead of copying the complete master corpus.

An unrelated later candidate does not reopen an accepted attempt; only the two bounded
invalidation authorities apply.

### Conventions

- Flat numbered files are stable creation identities; the master's list determines execution
  order.
- One master integration branch holds all leaf integrations.
- Each active subtask receives its own enclosure/worktree.
- Decision logs stay append-only.

### Invariants And Boundaries

- Corpus approval precedes both master and leaf creation.
- A master summarizes but never rewrites requirement contracts.
- No leaf may claim closure of multiple independently falsifiable requirements.
- Every revision appears in worker evidence and independent adjudication.
- Requirement version changes invalidate and rebrief only affected work.
- The summary is observation, never requirement, task, lifecycle, closeout, integration, or queue
  authority.

### Todos

None.

## Docs References

No external Domain Documentation source governs this topology template.

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The master projects requirements to manifestation subtasks. | `## Filtered Requirement Projection` | skills/w-02-light-task-workflow/master-template.md:53-65 |
| Each subtask names one primary revision and adjacent constraints separately. | `## Primary Requirement Revision`; `## Adjacent Requirement Constraints` | skills/w-02-light-task-workflow/master-template.md:136-139 |
| Usage rules preserve approval, versioning, and evidence boundaries. | `## Usage rules` | skills/w-02-light-task-workflow/master-template.md:125-159 |
| The master summary exposes attempt state while preserving leaf-journal authority and a non-gating boundary. | `## Requirement Attempt Summary (rebuildable projection — never a gate)` | skills/w-02-light-task-workflow/master-template.md:66-82 |

## Cross-Repo References

The target repository supplies its integration, check, and release policy; this template supplies
only lifecycle topology.

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

- 2026-08-27T21:53+02:00 — M44@v2: summaries now exclude internal protocol events and project
  lightweight leaf records that link content-addressed expanded evidence.
- 2026-08-27T19:59+02:00 — M42 clarification: excluded unrelated candidate movement from the
  accepted-attempt invalidation contract.
- 2026-08-27T18:06+02:00 — M40-M45: added the rebuildable requirement-attempt summary, exact
  failure/current-state fields, leaf authority links, and explicit non-gating recovery semantics.
- 2026-08-27T14:52+02:00 — Created onboarding for filtered master projections, one-primary leaf
  ownership, manifestation mapping, and exact-version review.
