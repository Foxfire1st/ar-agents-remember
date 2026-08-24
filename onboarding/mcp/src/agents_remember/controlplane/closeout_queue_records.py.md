# mcp/src/agents_remember/controlplane/closeout_queue_records.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/controlplane/closeout_queue_records.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-08-24T14:43+02:00 |
| lastVerifiedCommitHash | `f95487ec993b58d34911bba0206a7fa6ef9684eb` |
| lastVerifiedCommitDate | 2026-08-24T15:28:18+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[control-plane overview](overview.md)

## Purpose

Defines the strict off-side build record used to publish one complete disposable closeout
projection.

## Code Commentary

### Logic

`CloseoutProjectionBuild` binds the sprint ref, exact source fingerprint and classification,
bounded members, and build timestamp. Validation requires terminal source classifications to carry
no members and keeps the entire candidate self-contained for one later exact-current publication.

### Conventions

The record inherits the repository durable-record schema and bounds every persisted text and
collection field.

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
| The build record is complete off-side projection input. | `CloseoutProjectionBuild` | `mcp/src/agents_remember/controlplane/closeout_queue_records.py` |

## Cross-Repo References

No meaningful cross-repository reference applies.

## 260821-CLIVE Final Projection Contract

`CloseoutProjectionBuild` replaces the former queue-owned WAL transaction vocabulary. One build is
a complete off-side projection candidate binding the sprint ref, canonical source fingerprint and
classification, bounded members, and build timestamp. Terminal source classifications require an
empty member set. These records never own claims, commits, lifecycle transitions, certification,
blockers, or task locks; they are disposable publication input only.

## Update History

- 2026-08-24T14:43+02:00 — 260821-CLIVE cumulative curation: replaced the obsolete queue-WAL authority with the final off-side projection-build contract. Timestamp is the curator host's Europe/Berlin system time; verification remains closeout-owned.

- 2026-08-21T00:45+02:00 — 260815-DAG master full-gate repair: import paths updated to the moved package locations (`worktrees/queue`, `worktrees/integration`, `application/task_docs`, `models/queue`); reviewed — no content impact on the documented contracts. Verified at code commit e5cb139f.


- 2026-08-21T00:45+02:00 — 260815-DAG master full-gate repair: import paths updated to the moved package locations (`worktrees/queue`, `worktrees/integration`, `application/task_docs`, `models/queue`); reviewed — no content impact on the documented contracts. Verified at code commit e5cb139f.


- 2026-08-21T00:45+02:00 — 260815-DAG master full-gate repair: import paths updated to the moved package locations (`worktrees/queue`, `worktrees/integration`, `application/task_docs`, `models/queue`); reviewed — no content impact on the documented contracts. Verified at code commit e5cb139f.


- 2026-08-21T00:45+02:00 — 260815-DAG master full-gate repair: import paths updated to the moved package locations (`worktrees/queue`, `worktrees/integration`, `application/task_docs`, `models/queue`); reviewed — no content impact on the documented contracts. Verified at code commit e5cb139f.


- 2026-08-18T09:05+02:00 — Renamed the atomic 'barrier' concept to 'blocker' throughout (terminology unification; no behavioral change). Verification remains closeout-owned.

- 2026-08-15T09:10+02:00 — Created for L3's bounded closeout-queue WAL contract; verification remains closeout-owned.
