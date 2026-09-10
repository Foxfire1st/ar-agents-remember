# skills/l-01-agent-lifecycles/templates/manager-brief.md

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `skills/l-01-agent-lifecycles/templates/manager-brief.md` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-09T14:45+02:00|
| lastVerifiedCommitHash | `6f3e3fde75a1ca0202c9b07557cf86a7893e8532`|
| lastVerifiedCommitDate | 2026-09-10T07:24:09+02:00|
| governingOverview | `skills/l-01-agent-lifecycles/overview.md` |

## Governing Overview

[lifecycle overview](../overview.md)

## Purpose

This is the orchestrator-compiled, self-contained session start for a manager that owns one
master. It transfers task topology, source-edge truth, targeted/scoped evidence, closeout scheduling, and
the exact approved requirement revisions the manager must dispatch and close.

## Code Commentary

### Logic

Before each worker dispatch, the manager receives one stable ID, exact version, matching approved
canonical packet, corpus ruling, and expected evidence classes for every applicable requirement.
The manager requires one worker acceptance block and one independent reviewer adjudication per
revision. It separately preserves the durable-evidence promotion hold point, optional requested
review, curator handoff, and repository-defined transaction boundaries.

The brief also requires the manager to compile the next review-handoff attempt identity without
advancing it during dispatch or internal implementation/test/evidence reruns, validate the
lightweight candidate-bound worker record and content-addressed expanded-evidence anchor, and
dispatch that exact candidate to independent review. The reviewer proves any direct regression;
the owning manager records bounded invalidation. The rebuildable master summary links authoritative
leaf journals, excludes separate protocol events from attempt counts, and never gates task,
lifecycle, closeout, integration, or queue work.

A reviewer-rejected manifestation creates a successor at the next handoff; an unrelated later
candidate does not reopen accepted work.

The brief also keeps task authoring independent of disposable closeout projections: valid task
mutations proceed, projection effects are reported, and affected door generations are re-proved
rather than treating queue state as a task lock.

### Conventions

- The orchestrator fills every placeholder before dispatch.
- Canonical task documents and plane-owned contracts carry branch and source identity.
- Stable requirement IDs and versions are copied exactly; master prose never replaces packets.
- Worker, reviewer, and curator seats remain distinct; the reviewer is also distinct from the seat
  that authored the plan, preventing plan-author self-adjudication.

### Invariants And Boundaries

- An unstable, unapproved, missing, duplicated, or version-mismatched requirement makes dispatch
  invalid.
- Any rejected requirement blocks the overall reviewer recommendation.
- Requirement acceptance cannot substitute for stable-contract-or-expiry evidence, or vice versa.
- A manager reports readiness but does not rank the portfolio or decide developer-owned gates.
- Requirement problems route to architect/developer revision authority; worker/reviewer records
  cannot change semantic versions.

### Todos

None.


## CCR-R12@v5 Handoff Boundary

This template records the exact targeted or scoped checks and their failed or not-run status as handoff evidence. Closeout and integration consume the prepared code, memory-content, and ledger transaction; full quality, full tests, full memory quality, certification, and review are explicit requests rather than automatic template gates.

## Docs References

No external Domain Documentation source governs this dispatch template.

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The source edge and every requirement revision are compiled before worker dispatch. | "## The source edge (plane-owned, load-bearing)"; "## Dispatch defaults" | skills/l-01-agent-lifecycles/templates/manager-brief.md:32-42; skills/l-01-agent-lifecycles/templates/manager-brief.md:61-175 |
| Master exit carries the full revision set and independent adjudications. | "## The exit" | skills/l-01-agent-lifecycles/templates/manager-brief.md:176-194 |
| Attempt dispatch, bounded invalidation, and the non-gating master summary are explicit manager obligations. | "## Dispatch defaults" | skills/l-01-agent-lifecycles/templates/manager-brief.md:61-175 |

## Cross-Repo References

No sibling-repository contract is defined here; repository-specific executors are resolved from
the target repository's system guidance.

## 2026-08-27 Attempt Boundary Clarification

Attempt publication is phase-sensitive: validate before append, and treat append plus the exact
review handoff as one formal boundary. A malformed row that never reached review is preserved by a
non-attempt correction/void record without consuming the next attempt ID; after handoff, only an
independent reviewer rejection permits a successor.

## Update History
- 2026-09-10T07:30+02:00 — CCR-R12@v5 transaction-only curation: updated the current onboarding boundary; verification metadata remains preserved for the coordinated final stamp.

- 2026-09-09T14:45+02:00 — CCR-L42 curator reconciliation: re-read affected claims against the frozen current source and corrected only their source anchors/ranges; verification stamps remain closeout-owned.

- 2026-08-28T11:51+02:00 — Required the reviewer seat to be distinct from both the builder and
  plan author.

- 2026-08-28T11:32+02:00 — No content impact: re-read the v25 role/topology clarification; this
  card already describes one leaf-owned primary revision, adjacent contextual constraints, and
  the source-specific worker/reviewer/manager/curator boundary.

- 2026-08-27T22:15+02:00 — Distinguished pre-handoff non-attempt correction from post-handoff
  reviewer rejection and successor lineage.

- 2026-08-27T21:53+02:00 — M40@v2/M44@v2: corrected attempt advancement to review handoff,
  required lightweight content-addressed records, and excluded protocol events from summaries.
- 2026-08-27T19:59+02:00 — M42 clarification: made candidate replacement an in-flight or
  rejected-repair event rather than an implicit post-acceptance invalidation.
- 2026-08-27T18:06+02:00 — M40-M45: documented immutable attempt dispatch, exact reviewer binding,
  owner-recorded invalidation, closed failure routing, and the rebuildable non-gating summary.
- 2026-08-27T14:52+02:00 — Created onboarding for the exact-version dispatch and per-requirement
  acceptance/adjudication contract introduced by M38 and M39.
