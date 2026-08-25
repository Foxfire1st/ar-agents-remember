# mcp/tests/test_closeout_queue_store.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/test_closeout_queue_store.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-08-25T15:44+02:00 |
| lastVerifiedCommitHash | `1abeed661cbbf813c7c8a1b651a14dbcf2ad2b4e` |
| lastVerifiedCommitDate | 2026-08-25T17:21:45+02:00|
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

## Current Contract — 260821 CLIVE Final

This is the current source-backed contract for this test card. It supersedes any earlier
queue-lifecycle, blocker-row, replan/drain, or compatibility-reader wording where present.

Forces the two-state disposable projection store, invalidation receipts, atomic replacement, source-fingerprint checks, and strict-read degradation.

### Current Invariants

- Invalidation durably publishes invalid-empty with no candidates.
- Only a complete current-source build can publish valid-built.


## PDLS Reconciliation

Queue-store tests now enforce disposable valid-built/invalid-empty projection semantics instead of stale-row lifecycle transitions.

The test continues to exercise production-owned behavior. No diagnostic result is treated as
certifying evidence and no fallback or threshold exception was introduced.
## Update History

- 2026-08-25T15:44+02:00 — PDLS whole-system reconciliation updated the implementation summary
  above after source and requirement review. Verification remains closeout-owned.


- 2026-08-24T14:48+02:00 — DAGQC cumulative CLIVE final-gap curation: reconciled this test card to current source while preserving prior history and verification provenance.

- 2026-08-21T00:45+02:00 — 260815-DAG master full-gate repair: import paths updated to the moved package locations (`worktrees/queue`, `worktrees/integration`, `application/task_docs`, `models/queue`) and the `unittest.main` tail guard removed where present; reviewed — no content impact on the documented test contracts. Verified at code commit e5cb139f.


- 2026-08-21T00:45+02:00 — 260815-DAG master full-gate repair: import paths updated to the moved package locations (`worktrees/queue`, `worktrees/integration`, `application/task_docs`, `models/queue`) and the `unittest.main` tail guard removed where present; reviewed — no content impact on the documented test contracts. Verified at code commit e5cb139f.


- 2026-08-21T00:45+02:00 — 260815-DAG master full-gate repair: import paths updated to the moved package locations (`worktrees/queue`, `worktrees/integration`, `application/task_docs`, `models/queue`) and the `unittest.main` tail guard removed where present; reviewed — no content impact on the documented test contracts. Verified at code commit e5cb139f.


- 2026-08-21T00:45+02:00 — 260815-DAG master full-gate repair: import paths updated to the moved package locations (`worktrees/queue`, `worktrees/integration`, `application/task_docs`, `models/queue`) and the `unittest.main` tail guard removed where present; reviewed — no content impact on the documented test contracts. Verified at code commit e5cb139f.


- 2026-08-15T14:05+02:00 — L3 final targeted-gate repair: directly forces malformed canonical
  state refusal and recovery of an initial sprint-status WAL before any queue artifact exists.
- 2026-08-15T13:18+02:00 — No content impact: repository Ruff formatting changed only layout;
  confinement, WAL, crash, and replay assertions are identical.
- 2026-08-15T12:53+02:00 — Created for L3's focused durable-store and crash-idempotence suite.
