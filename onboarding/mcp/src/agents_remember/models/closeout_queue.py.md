# mcp/src/agents_remember/models/closeout_queue.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/models/closeout_queue.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-08-15T09:10+02:00 |
| lastVerifiedCommitHash | `cdcdc566fc6bee44b371a9d15c2048ceb1a49b8b` |
| lastVerifiedCommitDate | 2026-08-18T03:31:59+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[models overview](overview.md)

## Purpose

Defines the strict public request, durable candidate/state records, exact evidence facts, scheduling
grade projection, and public queue response for dependency-aware leaf closeout scheduling.

## Code Commentary

### Logic

The request validator enforces one exact action/payload matrix. Candidate records bind candidate
trees, graph revision, source bases, route review, curator evidence, grade evidence, memory mode,
and lifecycle state. State validation allows one active lane owner, enforces atomic-barrier
exclusion, and requires closed queues to be empty. Public projections split candidates into ready,
waiting, blocked, and in-flight lists with actor-legal next operations.

Added the `prepare-quality-repair` event for the failed organizational-completion reset.

### Conventions

All nested models are extra-forbid and every persisted or public collection/text field has an
explicit bound. Priority is the canonical categorical `critical/high/normal/low` vocabulary.

### Invariants And Boundaries

- Manager declaration cannot smuggle a grade; `set-grade` is a separate action.
- Raw lifecycle operation keys are never persisted; only a one-way owner fingerprint is modeled.
- External memory requires exact evidence and commit fields; internal/disabled memory uses a typed
  `not-applicable` state with no memory artifacts.
- Durable state cannot contain impossible candidate-state/owner/commit combinations.

### Todos

None recorded.

## Docs References

No configured Domain Documentation source applies.

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The request schema enforces exact required and forbidden fields per action. | `CloseoutQueueRequest` | mcp/src/agents_remember/models/closeout_queue.py:63-118 |
| Candidate validation binds serviceable lifecycle and memory states. | `CloseoutCandidateRecord` | mcp/src/agents_remember/models/closeout_queue.py:247-324 |
| Queue state permits one lane owner, enforces barrier ownership, and makes closure quiescent. | `CloseoutQueueState` | mcp/src/agents_remember/models/closeout_queue.py:343-377 |
| The response exposes deterministic classification buckets and legal operations. | `CloseoutQueueResponse` | mcp/src/agents_remember/models/closeout_queue.py:380-406 |

## Cross-Repo References

No meaningful cross-repository reference applies.

## 260815-DAG-L4 Authority Boundary

L4 routes this file's existing application, configuration, task, model, registration, or memory responsibility through the shared task-derived integration authority. The change preserves the file's owning altitude while ensuring protected code and external-memory refs cannot be mutated through an ordinary workbench or unjournaled helper.

## Update History

- 2026-08-17T12:30+02:00 — 260815-DAG-L5: added the `prepare-quality-repair` event to the closeout queue event vocabulary. Verification remains closeout-owned.

- 2026-08-15T23:38+02:00 — Reconciled this file's L4 role in task-derived integration authority and protected code/memory boundaries. Verification metadata remains closeout-owned.

- 2026-08-15T09:10+02:00 — Created for L3's strict closeout-queue wire and durable-state vocabulary; verification remains closeout-owned.
