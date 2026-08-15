# mcp/tests/test_closeout_queue_store.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/test_closeout_queue_store.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-08-15T14:05+02:00 |
| lastVerifiedCommitHash | `17987fa66a642306eb8d20fa9a4bff2b881550d2` |
| lastVerifiedCommitDate | 2026-08-15T14:36:30+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[MCP tests overview](overview.md)

## Purpose

Owns closeout-queue store confinement, state/WAL validation, sprint-status crash recovery, request
idempotence, and closed-sprint task-fact refusal.

## Code Commentary

### Logic

The suite injects read/write failures and pre/post-publication crash cuts around the canonical
state and one-record pending file. It proves exact revision/fingerprint matching, survival-record
requirements, no-op receipt persistence, and deterministic Completed/reopened recovery.

### Invariants And Boundaries

- Queue paths remain task-root confined.
- A pending record cannot reconstruct a missing noninitial survival state.
- Successful no-ops consume their request id, preventing a later retry from becoming a mutation.

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| Pending state must follow exact revision and bytes. | `test_pending_must_follow_current_revision_and_exact_state` | mcp/tests/test_closeout_queue_store.py:149-174 |
| Sprint status recovers on both sides of state publication. | `test_pending_status_recovers_before_and_after_state_publication` | mcp/tests/test_closeout_queue_store.py:183-194 |
| No-op receipts retain exact replay semantics. | `test_retry_receipt_is_persisted_for_noop_and_reuse_is_exact` | mcp/tests/test_closeout_queue_store.py:217-244 |

## Update History

- 2026-08-15T14:05+02:00 — L3 final targeted-gate repair: directly forces malformed canonical
  state refusal and recovery of an initial sprint-status WAL before any queue artifact exists.
- 2026-08-15T13:18+02:00 — No content impact: repository Ruff formatting changed only layout;
  confinement, WAL, crash, and replay assertions are identical.
- 2026-08-15T12:53+02:00 — Created for L3's focused durable-store and crash-idempotence suite.
