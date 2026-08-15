# mcp/src/agents_remember/controlplane/closeout_queue_records.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/controlplane/closeout_queue_records.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-08-15T09:10+02:00 |
| lastVerifiedCommitHash | `17987fa66a642306eb8d20fa9a4bff2b881550d2` |
| lastVerifiedCommitDate | 2026-08-15T14:36:30+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[control-plane overview](overview.md)

## Purpose

Defines the strict one-record write-ahead transaction used to recover queue mutations and sprint
completion/reopen publication without turning the WAL into the survival record.

## Code Commentary

### Logic

`CloseoutQueuePendingTransaction` binds one request fingerprint and actor to an exact previous
revision and next `CloseoutQueueState`. Validation requires exactly one revision advance, an exact
retry receipt for queue mutations, and a quiescent closed/open target for sprint-status changes.

### Conventions

The record inherits the repository durable-record schema and bounds every persisted text field.

### Invariants And Boundaries

- A pending transaction advances exactly one revision.
- Queue mutation state carries its exact request receipt.
- Sprint-status WAL rows contain no candidate, barrier, or receipt state.

### Todos

None recorded.

## Docs References

No configured Domain Documentation source applies.

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| Transaction validation separates queue mutations from quiescent sprint-status transitions. | `CloseoutQueuePendingTransaction` | mcp/src/agents_remember/controlplane/closeout_queue_records.py:19-74 |

## Cross-Repo References

No meaningful cross-repository reference applies.

## Update History

- 2026-08-15T09:10+02:00 — Created for L3's bounded closeout-queue WAL contract; verification remains closeout-owned.
