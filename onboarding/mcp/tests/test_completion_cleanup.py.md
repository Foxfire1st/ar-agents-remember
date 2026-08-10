# mcp/tests/test_completion_cleanup.py

| Field                  | Value                                          |
| ---------------------- | ---------------------------------------------- |
| repository             | agents-remember                                |
| path                   | `mcp/tests/test_completion_cleanup.py`         |
| doc_type               | `file-level-onboarding`                        |
| lastUpdated            | 2026-08-10T06:28+02:00                         |
| lastVerifiedCommitHash |                                                `7bf564a663bb61f12844dee39538dd09a1633cdb`|
| lastVerifiedCommitDate |                                                2026-08-10T12:28:42+02:00|
| governingOverview      | `overview.md`                                  |

## Governing Overview

[MCP tests overview](overview.md)

## Purpose

`test_completion_cleanup.py` isolates failure-containment coverage for report-gated completion
cleanup. It keeps infrastructure/race cases out of the already broad seat-lifecycle suite and
targets the dedicated cleanup owner directly.

## Code Commentary

### Logic

The fixture constructs one worktree contract, runtime config, terminal catalog, and durable inbox
root. Tests prove that an unreadable contract returns empty cleanup evidence; a per-seat retirement
exception is attributed without escaping; a concurrent retirement race is not mislabeled as a
failure; and a landing-path exception under the explicit auto-close opt-out remains subordinate to
the completed edge.

### Conventions

The suite patches only external seams of `completion_cleanup`: contract loading, retirement, and
landing. Real durable inbox and terminal-catalog stores are used for the per-seat cases.

### Invariants And Boundaries

- Failure containment must preserve the completion edge's success.
- A reported seat whose retirement raises is named in `autoCloseFailedSeats`.
- A `None` retirement result represents an already-resolved concurrency race, not a new failure.
- The opt-out path returns the historical `autoLandedSeats` key even when cleanup yields no rows.

### Todos

None.

## Docs References

No Domain Documentation entries are configured, and this is a repository-local regression suite.

| Finding | Anchor | Source |
| --- | --- | --- |
| No external documentation governs these internal test fixtures. | — | — |

## Repo-Internal References

The suite targets the dedicated completion cleanup owner and complements the completion-edge wiring
tests that remain in `test_seat_lifecycle.py`.

| Finding | Anchor | Source |
| --- | --- | --- |
| The cleanup owner contains the outer edge guard and per-seat retirement isolation exercised here. | `auto_complete_seats`; `_retire_reported_leaf_seats` | mcp/src/agents_remember/application/completion_cleanup.py:27-108 |
| The broader seat suite proves successful integration/finalization wiring and role/report selection. | `AutoLandHookIntegrationTests` | mcp/tests/test_seat_lifecycle.py:645-869 |

## Cross-Repo References

No cross-repository boundary is exercised.

| Finding | Anchor | Source |
| --- | --- | --- |
| All fixtures use temporary local paths and in-process repository services. | — | — |

## Update History

- 2026-08-10T13:00+02:00 — 260731-EFA-L9 curator: No content impact: re-read the extracted completion-cleanup containment coverage; the existing test card remains accurate. Verification metadata remains pinned until closeout.
- 2026-08-10T06:28+02:00 — Created by extracting completion-cleanup containment cases from the
  seat-lifecycle suite so both production and test files stay below their architecture thresholds.
  Verification metadata remains blank until closeout stamps the code commit.
