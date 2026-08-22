# mcp/tests/test_organizational_completion_integration.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/test_organizational_completion_integration.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-08-22T10:39+02:00 |
| lastVerifiedCommitHash | `eb7ea60ab9919f009fef58f81afe5861aa1709da` |
| lastVerifiedCommitDate | 2026-08-22T11:44:33+02:00|
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

## 260821-CLIVE-L1 Contract Hash Migration

Organizational completion fixtures now publish contracts with the canonical serializer used by reset and closeout-finalization hashes. Completion behavior is unchanged; the migration prevents the test from constructing a representation that production identity would reject.

## Update History

- 2026-08-22T10:39+02:00 — 260821-CLIVE-L1: curated relationship changes against accepted candidate tree `4241908c`; verification metadata remains pinned until governed closeout.

- 2026-08-21T00:45+02:00 — 260815-DAG master full-gate repair: queue, model, and
  integration/organizational-completion imports follow the package moves (`worktrees/queue/`,
  `models/queue/`, `worktrees/integration/`); remaining hunks are Ruff formatting-only line joins.
  Verified at code commit e5cb139f.

- 2026-08-19T22:32+02:00 — No content impact: 260815-DAG-L13 split blocker-reason assertions on `:` because stale-base reasons now carry the `worktree_sync` recovery suffix; the documented completion-integration behavior is unchanged. Verification remains closeout-owned.

- 2026-08-17T12:09+02:00 — 260815-DAG-L5: created onboarding for the organizational completion integration suite.
## Docs References

No external Domain Documentation source is configured for this internal route; task `260821-CLIVE-L1` and the cited repository source/tests govern this curation.

## Cross-Repo References

This file owns no ambient cross-repository authority. Any external-memory repository it reaches remains explicitly contract-addressed.
