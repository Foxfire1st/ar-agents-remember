# mcp/tests/test_completion_cleanup.py

| Field                  | Value                                          |
| ---------------------- | ---------------------------------------------- |
| repository             | agents-remember                                |
| path                   | `mcp/tests/test_completion_cleanup.py`         |
| doc_type               | `file-level-onboarding`                        |
| lastUpdated            | 2026-08-10T06:28+02:00                         |
| lastVerifiedCommitHash |                                                `d9a1eb82849baea6c0b86735e772a932f4bbdc7c`|
| lastVerifiedCommitDate |                                                2026-08-12T00:45:15+02:00|
| governingOverview      | `overview.md`                                  |

## Governing Overview

[MCP tests overview](overview.md)

## Purpose

Containment suite for task-bound automatic worker/reviewer/curator cleanup after a successful completion edge.

## Code Commentary

### Logic

The matrix resolves the enclosure to `TaskDocumentRef`, admits exact task-addressed turn reports, retires or lands only eligible task seats, and contains unreadable contracts, per-seat retirement failures, concurrent retirement races, and opt-out landing failures.

### Conventions

Test-only evidence uses deterministic fakes/fixtures and exercises the public or owning internal seam directly.

### Invariants And Boundaries

Manager/orchestrator seats stay outside automatic cleanup; missing or wrong-task proof never terminates a seat; cleanup failure cannot rewrite the successful integration/finalization result.

## Docs References

No Domain Documentation source is configured for this repository-local regression contract.

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| Current suite declaration anchoring this card. | `CompletionCleanupContainmentTests` | mcp/tests/test_completion_cleanup.py:51-51 |

## Cross-Repo References

No cross-repository implementation source governs this test module.

## Update History

- 2026-08-11T19:58+02:00 — Reconciled `test_completion_cleanup.py` with its current structural task/seat, tool-vocabulary, or quality-boundary regression contract and removed stale exact-id/leaf implications where present.
- 2026-08-10T13:00+02:00 — 260731-EFA-L9 curator: No content impact: re-read the extracted completion-cleanup containment coverage; the existing test card remains accurate. Verification metadata remains pinned until closeout.
- 2026-08-10T06:28+02:00 — Created by extracting completion-cleanup containment cases from the
  seat-lifecycle suite so both production and test files stay below their architecture thresholds.
  Verification metadata remains blank until closeout stamps the code commit.
