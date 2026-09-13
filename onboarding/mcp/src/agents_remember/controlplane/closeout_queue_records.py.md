# mcp/src/agents_remember/controlplane/closeout_queue_records.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/controlplane/closeout_queue_records.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-08-24T14:43+02:00 |
| lastVerifiedCommitHash | `9f0309447d6820d90e59279abc84f87f1ccbb3b3` |
| lastVerifiedCommitDate | 2026-09-13T22:28:36+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[control-plane overview](overview.md)

## Purpose

Defines the strict off-side build record used to publish one complete disposable closeout
projection.

## Code Commentary

### Logic

`CloseoutProjectionBuild` binds the sprint ref, exact source fingerprint and classification,
members, and build timestamp. The member list carries no item ceiling since 260913-LCA-L6.
Validation requires terminal source classifications to carry
no members and keeps the entire candidate self-contained for one later exact-current publication.

### Conventions

The record inherits the repository durable-record schema and bounds its text fields (`builtAt` is a
bounded string). Its `members` collection carries no item ceiling since 260913-LCA-L6, so how many
leaves a sprint declares never reaches this build guard.

### Invariants And Boundaries

- A build is scratch input, not the survival record for scheduling or lifecycle evidence.
- It contains no claim, commit, blocker, receipt, certification, or task-lock state.
- Prior projection rows are never inputs to a new build.

### Todos

None recorded.

## Docs References

No configured Domain Documentation source applies.

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The build record is complete off-side projection input. | `CloseoutProjectionBuild` | mcp/src/agents_remember/controlplane/closeout_queue_records.py:17-31 |

## Cross-Repo References

No meaningful cross-repository reference applies.

## 260821-CLIVE Final Projection Contract

`CloseoutProjectionBuild` replaces the former queue-owned WAL transaction vocabulary. One build is
a complete off-side projection candidate binding the sprint ref, canonical source fingerprint and
classification, members, and build timestamp. Terminal source classifications require an
empty member set. These records never own claims, commits, lifecycle transitions, certification,
blockers, or task locks; they are disposable publication input only. The member list was bounded to
256 at the time this section was written; 260913-LCA-L6 removed that ceiling, so only the
terminal-classification emptiness rule limits membership today.

## Update History

- 2026-09-13T22:22+02:00 — L6 (260913-LCA): the off-side build record no longer caps its member population. `CloseoutProjectionBuild.members` is `Field(default_factory=list)` and the literal `max_length=256` is gone; both "bounded members" claims are corrected and the terminal-classification emptiness rule is unchanged. Source is a read-only uncommitted change set; verification metadata remains closeout-owned and no stamp advanced.

- 2026-08-26T10:44:52+02:00 — No content impact: reviewed the closeout-projection model package relocation; disposable projection-build record behavior is unchanged.

- 2026-08-24T14:43+02:00 — 260821-CLIVE cumulative curation: replaced the obsolete queue-WAL authority with the final off-side projection-build contract. Timestamp is the curator host's Europe/Berlin system time; verification remains closeout-owned.

- 2026-08-21T00:45+02:00 — 260815-DAG master full-gate repair: import paths updated to the moved package locations (`worktrees/queue`, `worktrees/integration`, `application/task_docs`, `models/queue`); reviewed — no content impact on the documented contracts. Verified at code commit e5cb139f.


- 2026-08-21T00:45+02:00 — 260815-DAG master full-gate repair: import paths updated to the moved package locations (`worktrees/queue`, `worktrees/integration`, `application/task_docs`, `models/queue`); reviewed — no content impact on the documented contracts. Verified at code commit e5cb139f.


- 2026-08-21T00:45+02:00 — 260815-DAG master full-gate repair: import paths updated to the moved package locations (`worktrees/queue`, `worktrees/integration`, `application/task_docs`, `models/queue`); reviewed — no content impact on the documented contracts. Verified at code commit e5cb139f.


- 2026-08-21T00:45+02:00 — 260815-DAG master full-gate repair: import paths updated to the moved package locations (`worktrees/queue`, `worktrees/integration`, `application/task_docs`, `models/queue`); reviewed — no content impact on the documented contracts. Verified at code commit e5cb139f.


- 2026-08-18T09:05+02:00 — Renamed the atomic 'barrier' concept to 'blocker' throughout (terminology unification; no behavioral change). Verification remains closeout-owned.

- 2026-08-15T09:10+02:00 — Created for L3's bounded closeout-queue WAL contract; verification remains closeout-owned.
