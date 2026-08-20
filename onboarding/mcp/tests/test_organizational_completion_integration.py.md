# mcp/tests/test_organizational_completion_integration.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/test_organizational_completion_integration.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-08-21T00:45+02:00 |
| lastVerifiedCommitHash | `e5cb139f66abbd6502d4dcc4be883eb5f49770fe` |
| lastVerifiedCommitDate | 2026-08-21T00:28:23+02:00|
| governingOverview | `../overview.md` |

## Governing Overview

[governing overview](../overview.md)

## Purpose

Retains the real parallel-leaf, exact sync, final-gate, sibling-ledger, pre-CAS certification reuse, task-publication, queue-completion, and crash-recovery scenarios for organizational completion.

## Code Commentary

The suite runs the production completion path end to end against real queue and lifecycle state: parallel organizational leaves converge through ancestry rather than memory copying, the final leaf runs one full gate against the exact proposed super candidate, sibling ledger mappings stay one-to-one, a completed integration reuses its certification without rerunning the gate, and crash recovery re-proves the durable removal intent.

## Invariants And Boundaries

- Exercises production owners rather than a copied state machine.
- Refusal cases assert no super ref movement and no stale ledger publication.

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The focused suite owns the end-to-end completion integration surface. | `OrganizationalCompletionIntegrationTests` | mcp/tests/test_organizational_completion_integration.py:95-1179 |

## Documentation References

No configured domain-documentation or cross-repository source applies to this file.

## 260815-DAG Master Full-Gate Repair

The 260815-DAG master full-gate repair moved this suite's imports under the restructured packages:
queue owners (`closeout_queue`, `closeout_queue_lifecycle`) and the request model now come from
`worktrees/queue/` and `models/queue/`, while `integration_quality`, `organizational_completion*`,
and the lifecycle-operation store/dispatch imports come from `worktrees/integration/`. The
remaining hunks are Ruff formatting-only line joins; no assertions changed.

## Update History

- 2026-08-21T00:45+02:00 — 260815-DAG master full-gate repair: queue, model, and
  integration/organizational-completion imports follow the package moves (`worktrees/queue/`,
  `models/queue/`, `worktrees/integration/`); remaining hunks are Ruff formatting-only line joins.
  Verified at code commit e5cb139f.

- 2026-08-19T22:32+02:00 — No content impact: 260815-DAG-L13 split blocker-reason assertions on `:` because stale-base reasons now carry the `worktree_sync` recovery suffix; the documented completion-integration behavior is unchanged. Verification remains closeout-owned.

- 2026-08-17T12:09+02:00 — 260815-DAG-L5: created onboarding for the organizational completion integration suite.
