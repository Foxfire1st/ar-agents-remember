# mcp/tests/test_closeout_queue_actions.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/test_closeout_queue_actions.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-08-23T16:08+02:00 |
| lastVerifiedCommitHash | `1d446724d099517f6f52d596b47827ae2391a2a4` |
| lastVerifiedCommitDate | 2026-08-24T00:21:10+02:00 |
| governingOverview | `overview.md` |

## Governing Overview

[MCP tests overview](overview.md)

## Purpose

Owns the closeout queue's public action, ambient-seat authority, blocker transition, and
caller-specific legal-operation matrices.

## Code Commentary

### Logic

The suite drives exact request fields and revisions through the queue owner, then exercises
declaration identity, immutable contract binding, atomic blocker acquire/release/abort, lifecycle
operation recovery, and legal projections for manager and orchestrator callers. Since
260815-DAG-L13 the blocker transitions are imported from the extracted
`worktrees/queue/closeout_queue_blocker.py` owner (mock targets follow), and the request-reference
validation cases exercise the shared `queue_task_ref` from `closeout_queue_errors.py`.

### Invariants And Boundaries

- Managers declare/admit and integrate; orchestrators grade/select and own blockers.
- Blocker acquisition proves atomic nature, drained predecessors/lane, rationale, and current
  code+memory super tips.
- A normal atomic blocker release proves the finalized master landing; abort requires canonical
  judgment evidence.
- Legal operations are state- and caller-specific rather than an overbroad union.

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| Public request and mutation authority is exact. | `test_status_scope_and_candidate_mutation_authority_is_exact` | mcp/tests/test_closeout_queue_actions.py:99-143 |
| Blocker release and abort call their exact evidence seams. | `test_release_and_abort_blocker_require_exact_owner_and_empty_block` | mcp/tests/test_closeout_queue_actions.py:478-552 |
| Lifecycle legal operations require the exact durable owner. | `test_owned_lifecycle_operation_requires_exact_kind_contract_and_fingerprint` | mcp/tests/test_closeout_queue_actions.py:686-721 |

## 260815-DAG-L4 Integration-Authority Forcing

This task extends this suite's production-bound fixtures or assertions for task-derived protected-ref ownership, durable closeout/integration authority, external-memory parity, and fail-closed recovery. The suite continues to exercise the real owner named in its existing purpose; the L4 delta adds exact negative or crash/retry evidence rather than a test-only bypass.

## 260815-DAG Master Full-Gate Repair

The 260815-DAG master full-gate repair moved the queue request model import to
`models/queue/closeout_queue.py` and every queue-owner import and mock target under
`worktrees/queue/` (the L13-era extracted blocker owner path is now
`worktrees/queue/closeout_queue_blocker.py`); the `__main__` runner was removed. No assertions
changed.

## 260821-CLIVE-L2 Current Regression Contract

The current forcing seams include `test_status_scope_and_candidate_mutation_authority_is_exact`, `test_public_tool_refuses_blank_time_missing_id_stale_revision_and_completed_mutation`, `test_mutation_rechecks_sprint_completion_inside_the_store_lock`, `test_candidate_action_missing_noop_immutable_and_release_matrix`. These tests cover current queue actions, including transitional pre-L3 states. They do not establish the final waiting-only schema or task-change invalidation contract; L3 owns those proofs.

### Reconciled Source Evidence

| Finding | Citations | Source Path |
| --- | --- | --- |
| The current test source exercises `test_status_scope_and_candidate_mutation_authority_is_exact`, `test_public_tool_refuses_blank_time_missing_id_stale_revision_and_completed_mutation`, `test_mutation_rechecks_sprint_completion_inside_the_store_lock`, `test_candidate_action_missing_noop_immutable_and_release_matrix`. | L99-L143; L145-L198; L200-L233; L235-L299 | `mcp/tests/test_closeout_queue_actions.py` |

## Update History

- 2026-08-23T16:08+02:00 — 260821-CLIVE-L2: reconciled this test card with the accepted full L2 candidate; verification metadata remains pinned until architect-owned closeout stamps the real code commit.

- 2026-08-21T00:45+02:00 — 260815-DAG master full-gate repair: the queue request model and all
  queue-owner imports/mock targets follow the package moves (`models/queue/`,
  `worktrees/queue/`); the `__main__` runner was removed. Verified at code commit e5cb139f.


- 2026-08-19T22:32+02:00 — 260815-DAG-L13: blocker transitions moved to
  `worktrees/closeout_queue_blocker.py` (imports and mock targets follow), and the
  request-reference cases exercise the extracted `queue_task_ref`. Assertions are unchanged.
  Verification remains closeout-owned.

- 2026-08-18T09:05+02:00 — Renamed the atomic 'barrier' concept to 'blocker' throughout (terminology unification; no behavioral change). Verification remains closeout-owned.

- 2026-08-18T01:24+02:00 — 260815-DAG-L6: added `test_acquire_blocker_requires_current_source_bases` covering the new R2 blocker-acquisition super-tip precondition. Verification remains closeout-owned.

- 2026-08-15T23:38+02:00 — Reconciled the suite's L4 fixture and forcing role for protected integration branches, durable operation authority, external-memory parity, and recovery. Verification metadata remains closeout-owned.

- 2026-08-15T14:05+02:00 — L3 final targeted-gate repair: added the successful nondefault
  admission transition and missing terminal-leaf refusal, completing the real action/declaration
  owner map without mocking production dispatch.
- 2026-08-15T13:18+02:00 — No content impact: repository Ruff formatting changed only layout;
  action, authority, blocker, and legal-operation assertions are identical.
- 2026-08-15T13:08+02:00 — No content impact: accepted Ruff's case-sensitive private-name import
  order; the imported action owners and assertions are unchanged.
- 2026-08-15T12:53+02:00 — Created for the focused L3 action/authority suite extracted after the
  first full targeted Dagger artifact exposed insufficient branch forcing.
