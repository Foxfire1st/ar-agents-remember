# mcp/tests/test_closeout_queue_store.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/test_closeout_queue_store.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-08-25T15:44+02:00 |
| lastVerifiedCommitHash | `ae8c47ce897b04380ebcb80f750d77ed4dc9f37d` |
| lastVerifiedCommitDate | 2026-08-26T08:10:26+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[MCP tests overview](overview.md)

## Purpose

Owns confinement and atomic persistence for the two-state disposable closeout projection store:
`invalid-empty` after invalidation and `valid-built` only after a current-source rebuild.

## Code Commentary

### Logic

The suite forces absent, malformed, nonregular, stale-source, terminal-empty, and oversized inputs.
It proves that invalidation is durable and idempotent, malformed artifacts are recoverably replaced
without a compatibility reader, stale builders cannot publish, and an exact current-source build is
atomically exposed with bounded members and diagnostics.

### Invariants And Boundaries

- Queue paths remain task-root confined.
- The only persisted service conditions are `invalid-empty` and `valid-built`.
- Invalidation never retains candidates; publication requires exact source identity and cannot
  expose an off-side or stale build.

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| Store paths are confined and persisted conditions are exactly valid-built or invalid-empty. | `test_paths_are_confined_and_persisted_conditions_are_exactly_two` | mcp/tests/test_closeout_queue_store.py:80-92 |
| Invalidation is idempotent and malformed artifacts are overwritten without legacy parsing. | `test_absent_invalidation_publishes_and_reports_persisted_empty`; `test_existing_invalid_empty_is_idempotent`; `test_malformed_artifact_is_recoverably_overwritten_without_legacy_parse` | mcp/tests/test_closeout_queue_store.py:94-99; mcp/tests/test_closeout_queue_store.py:101-105; mcp/tests/test_closeout_queue_store.py:107-120 |
| Stale builders never publish; terminal empty remains valid-built and persisted collections stay bounded. | `test_stale_off_side_builder_never_publishes`; `test_terminal_empty_is_valid_built_not_a_third_condition`; `test_every_persisted_and_wire_collection_is_capped` | mcp/tests/test_closeout_queue_store.py:163-171; mcp/tests/test_closeout_queue_store.py:190-211; mcp/tests/test_closeout_queue_store.py:213-241 |

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