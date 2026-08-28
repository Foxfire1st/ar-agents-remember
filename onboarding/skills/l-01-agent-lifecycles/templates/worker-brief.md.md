# skills/l-01-agent-lifecycles/templates/worker-brief.md

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `skills/l-01-agent-lifecycles/templates/worker-brief.md` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-08-28T14:18+02:00 |
| lastVerifiedCommitHash | a06d2ffcfae2c277f2ae19330c17d09c616b77e8 |
| lastVerifiedCommitDate | 2026-08-28T13:58:55+02:00 |
| governingOverview | `skills/l-01-agent-lifecycles/overview.md` |

## Governing Overview

[lifecycle overview](../overview.md)

## Purpose

This template is the complete session-start packet for one worker on one canonical leaf. It binds
the worker to named worktrees, one implementation scope, exact approved requirement revisions,
repository-defined checks, and one durable turn report.

## Code Commentary

### Logic

The spawning seat lists every applicable stable ID and version with its immutable packet, corpus
approval, evidence classes, and any already-approved changed delivery. The worker opens those
packets before editing and records a separate acceptance envelope for each revision. The envelope
contains delivery and verification rationales, inspectable citations, the failure each proof would
catch, exact command/results, and approval details for blocked or changed delivery.

The brief also compiles the leaf manifestation, one physical append-only journal path, next
review-handoff attempt ID, predecessor and carried findings, and candidate identity class. Dispatch
and internal implementation/test/evidence reruns do not advance that ID; those runs remain separate
protocol events. Before review handoff, the worker appends one lightweight immutable attempt with
requirement-specific facts and a content-addressed expanded-evidence anchor. A reviewer-rejected
delivery creates a successor at its next handoff. An unrelated later candidate does not reopen
accepted work. Blocked findings use the closed failure taxonomy and requirement problems route
upward for developer-approved revision.
The independently authored reviewer appends a separate adjudication record to that same journal;
the worker turn report links its exact attempt anchors rather than becoming a competing authority.

The brief gives the curator changed paths and observations without granting the worker onboarding,
commit, lifecycle, gate, or task-document mutation authority.

### Conventions

- Compile a fresh brief per leaf and fill every placeholder.
- Use `NONE (native reads only)` when retrieval providers are unavailable.
- Copy the target repository's actual acceptance command; never invent a host fallback.
- Write the turn report as the worker's last act.

### Invariants And Boundaries

- One worker brief targets one leaf and one primary implementation slice.
- “Requirements addressed” is never a substitute for one block per exact ID and version.
- The Checks section and the durable-evidence hold point are both explicit and separate from the
  acceptance envelope.
- The worker never commits, closes out, integrates, or writes accepted onboarding.
- The brief never reuses an attempt ID or authorizes an in-place edit of attempt history.

### Todos

None.

## Docs References

No external Domain Documentation source governs this worker template.

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The brief binds the exact owned requirement revision and evidence classes. | `## Owned primary requirement (exactly one stable-ID + version)` | skills/l-01-agent-lifecycles/templates/worker-brief.md:52-84 |
| The same block compiles leaf manifestation, attempt/predecessor lineage, and candidate identity before handoff. | `## Owned primary requirement (exactly one stable-ID + version)` | skills/l-01-agent-lifecycles/templates/worker-brief.md:52-84 |
| Repository-defined checks and artifact lifecycle remain separate obligations. | `## Checks (green before you report)` | skills/l-01-agent-lifecycles/templates/worker-brief.md:114-128 |
| The final report requires envelopes, checks, curator inputs, and continuity state. | `## Turn report (mandatory, last act)` | skills/l-01-agent-lifecycles/templates/worker-brief.md:146-151 |

## Cross-Repo References

The concrete worktree paths, tool paths, and verification command come from the dispatched target
repository rather than from this generic template.

## 2026-08-27 Attempt Boundary Clarification

Attempt publication is phase-sensitive: validate before append, and treat append plus the exact
review handoff as one formal boundary. A malformed row that never reached review is preserved by a
non-attempt correction/void record without consuming the next attempt ID; after handoff, only an
independent reviewer rejection permits a successor.

## Update History

- 2026-08-28T14:18+02:00 — Reconciled the worker-brief citation with the final primary-requirement
  heading and committed PDLS ranges; the required acceptance envelope is unchanged.

- 2026-08-28T11:32+02:00 — No content impact: re-read the v25 role/topology clarification; this
  card already describes one leaf-owned primary revision, adjacent contextual constraints, and
  the source-specific worker/reviewer/manager/curator boundary.

- 2026-08-27T22:15+02:00 — Distinguished pre-handoff non-attempt correction from post-handoff
  reviewer rejection and successor lineage.

- 2026-08-27T21:53+02:00 — M40@v2: made the next attempt a review-handoff identity, separated
  internal protocol events, and required lightweight content-addressed records.
- 2026-08-27T20:45+02:00 — Clarified one physical per-leaf journal, separate immutable
  worker/reviewer records, and link-only turn-report references.
- 2026-08-27T19:59+02:00 — M42 clarification: narrowed candidate-triggered successor attempts to
  unadjudicated or rejected work and preserved accepted manifestations across unrelated commits.
- 2026-08-27T18:06+02:00 — M40/M43: added leaf journal, immutable attempt/predecessor/candidate
  fields, before-handoff append order, and closed failure/revision routing.
- 2026-08-27T14:52+02:00 — Created onboarding for the approved-packet intake and mandatory
  per-requirement acceptance envelope.
