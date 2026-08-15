# mcp/src/agents_remember/models/closeout_queue.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/models/closeout_queue.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-08-15T09:10+02:00 |
| lastVerifiedCommitHash | `17987fa66a642306eb8d20fa9a4bff2b881550d2` |
| lastVerifiedCommitDate | 2026-08-15T14:36:30+02:00|
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

## Update History

- 2026-08-15T09:10+02:00 — Created for L3's strict closeout-queue wire and durable-state vocabulary; verification remains closeout-owned.
