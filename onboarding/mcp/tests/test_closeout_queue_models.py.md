# mcp/tests/test_closeout_queue_models.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/test_closeout_queue_models.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-08-21T00:45+02:00 |
| lastVerifiedCommitHash | `e5cb139f66abbd6502d4dcc4be883eb5f49770fe` |
| lastVerifiedCommitDate | 2026-08-21T00:28:23+02:00 |
| governingOverview | `overview.md` |

## Governing Overview

[MCP tests overview](overview.md)

## Purpose

Owns the closeout-queue request/action matrix, bounded metadata, candidate-state/memory invariants,
queue-state consistency, pending-transaction exactness, and direct imports that bind both split
evidence modules to targeted scope.

## Code Commentary

### Logic

The model tests validate required and forbidden fields for each action, bound and normalize grade,
evidence, admission, and blocker metadata, exhaust reachable candidate lifecycle shapes across
memory modes, reject inconsistent queue lanes and closed state, and bind pending revisions,
fingerprints, sprint status, and receipts. The ownership test keeps both evidence modules attached
to the targeted selection.

### Invariants And Boundaries

- Durable semantic invariants reject impossible states before projection or lifecycle code reads them.
- Direct imports are deliberate gate-scope ownership, not replacement behavior coverage.

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| Split candidate and judgment evidence modules have direct targeted-test ownership. | `test_split_evidence_modules_have_direct_test_ownership` | mcp/tests/test_closeout_queue_models.py:85-90 |
| Candidate state and memory modes are fail closed. | `test_candidate_state_and_memory_matrix_is_fail_closed` | mcp/tests/test_closeout_queue_models.py:193-274 |
| Pending transactions bind exact revisions, status, and receipts. | `test_pending_transactions_bind_revision_status_and_receipt` | mcp/tests/test_closeout_queue_models.py:310-414 |

## Update History

- 2026-08-21T00:45+02:00 — 260815-DAG master full-gate repair: import paths updated to the moved package locations (`worktrees/queue`, `worktrees/integration`, `application/task_docs`, `models/queue`) and the `unittest.main` tail guard removed where present; reviewed — no content impact on the documented test contracts. Verified at code commit e5cb139f.


- 2026-08-21T00:45+02:00 — 260815-DAG master full-gate repair: import paths updated to the moved package locations (`worktrees/queue`, `worktrees/integration`, `application/task_docs`, `models/queue`) and the `unittest.main` tail guard removed where present; reviewed — no content impact on the documented test contracts. Verified at code commit e5cb139f.


- 2026-08-21T00:45+02:00 — 260815-DAG master full-gate repair: import paths updated to the moved package locations (`worktrees/queue`, `worktrees/integration`, `application/task_docs`, `models/queue`) and the `unittest.main` tail guard removed where present; reviewed — no content impact on the documented test contracts. Verified at code commit e5cb139f.


- 2026-08-21T00:45+02:00 — 260815-DAG master full-gate repair: import paths updated to the moved package locations (`worktrees/queue`, `worktrees/integration`, `application/task_docs`, `models/queue`) and the `unittest.main` tail guard removed where present; reviewed — no content impact on the documented test contracts. Verified at code commit e5cb139f.


- 2026-08-18T09:05+02:00 — Renamed the atomic 'barrier' concept to 'blocker' throughout (terminology unification; no behavioral change). Verification remains closeout-owned.

- 2026-08-15T14:05+02:00 — No content impact: corrected two nested invalid-state assertions to
  the earlier closed-queue quiescence invariant that the real model evaluates first.
- 2026-08-15T13:18+02:00 — No content impact: repository Ruff formatting changed only layout;
  strict request, state, memory-mode, and pending-WAL cases are identical.
- 2026-08-15T13:08+02:00 — No content impact: the invalid-status loop now uses a distinct derived
  payload name instead of overwriting its iteration binding; the exact cases remain identical.
- 2026-08-15T12:53+02:00 — L3 targeted-gate repair: expanded the focused model suite across the
  strict request, metadata, durable-state, memory-mode, and pending-WAL branch matrices.
- 2026-08-15T10:24+02:00 — Created by the L3 file-size repair from tests previously located in
  `test_closeout_queue.py`; assertions and imported production owners are unchanged.
