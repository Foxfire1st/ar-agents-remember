# mcp/tests/test_organizational_completion_recovery_edges.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/test_organizational_completion_recovery_edges.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-08-21T00:45+02:00 |
| lastVerifiedCommitHash | `e5cb139f66abbd6502d4dcc4be883eb5f49770fe` |
| lastVerifiedCommitDate | 2026-08-21T00:28:23+02:00 |
| governingOverview | `../overview.md` |

## Governing Overview

[governing overview](../overview.md)

## Purpose

Forces the failure-time repair WAL and crash recovery for a failed final organizational quality gate.

## Code Commentary

The suite starts real queue/lifecycle state, persists the real repair WAL, injects the producer-to-finish crash, recovers through public `start_or_observe_operation`, pins one gate call and unchanged code/memory tips, then consumes the repair through the real cancel/reset route. It also forces malformed lifecycle states, immutability, foreign identity, binding, source, reset, owner, and recovery-evidence refusals.

## Invariants And Boundaries

- The production repair mutator accepts no caller-supplied lifecycle record.
- Refusal cases assert the canonical WAL, queue state, and contract bytes remain exact.

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The focused suite owns the failure repair and crash-recovery surface. | `OrganizationalCompletionRecoveryEdgeTests` | mcp/tests/test_organizational_completion_recovery_edges.py:28-565 |

## Documentation References

No configured domain-documentation or cross-repository source applies to this file.

## Update History

- 2026-08-21T00:45+02:00 — 260815-DAG master full-gate repair: import paths updated to the moved package locations (`worktrees/queue`, `worktrees/integration`, `application/task_docs`, `models/queue`) and the `unittest.main` tail guard removed where present; reviewed — no content impact on the documented test contracts. Verified at code commit e5cb139f.


- 2026-08-17T12:09+02:00 — 260815-DAG-L5: created onboarding for the organizational completion recovery-edge suite.
