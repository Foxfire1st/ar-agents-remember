# mcp/tests/test_integration_branch_authority_edges.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/test_integration_branch_authority_edges.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-08-16T07:46+02:00 |
| lastVerifiedCommitHash | `8bf6edad7e7e65e27cf735be0822f604531d0c8a` |
| lastVerifiedCommitDate | 2026-08-16T10:54:02+02:00|
| governingOverview | `../overview.md` |

## Governing Overview

[governing overview](../overview.md)

## Purpose

Covers direct helper bypasses, tag and alias collisions, configured identity, carryover fencing,
final CAS races, and exact series closeout/integration. The focused atomic bootstrap
crash/revalidation slice lives in `test_integration_branch_authority_bootstrap_edges.py`; the
atomic source-drift/replay refusal lives in `test_integration_branch_authority_series_drift.py`.

## Code Commentary

Tests bind real journal/queue/config facts and explicitly exercise no-ambient-checkout and contract-before-lane-release recovery edges. Its shared fixture imports now come directly from `integration_branch_authority_test_support.py`, eliminating the former test-module dependency.

## Invariants And Boundaries

- The suite exercises production owners rather than copying their state-transition logic.
- Refusal cases assert no unauthorized Git, contract, queue, task, or memory mutation.
- Crash/retry cases retain exact durable identity and expected-old facts.

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The focused suite owns this L4 authority boundary. | `IntegrationBranchAuthorityEdgeTests` | mcp/tests/test_integration_branch_authority_edges.py:74-1149 |

## Documentation References

No configured domain-documentation or cross-repository source applies to this file.

## Update History

- 2026-08-16T08:12+02:00 — Dagger repair: configured-memory mismatch forcing now preserves an external contract while removing only runtime memory authority. Moved the final preparation race verbatim to the focused operation-authority suite so this file remains below the 1,200-line gate without duplication.
- 2026-08-16T07:46+02:00 — Test-size split: moved the atomic source-drift/replay refusal verbatim into `test_integration_branch_authority_series_drift.py`; no test, assertion, or compatibility path is duplicated.
- 2026-08-16T05:18+02:00 — Dagger fixture repair: foreign-repository candidates use a contract-owned linked worktree, carryover uses a coordination-confined source worktree, and synthetic closeout completion uses the typed lifecycle phase.
- 2026-08-16T04:43+02:00 — Test-size split: moved the three contiguous atomic bootstrap journal/source/topology revalidation tests into `test_integration_branch_authority_bootstrap_edges.py`; no test or helper is duplicated, and this file is now 1,155 lines under the 1,200 hard limit.
- 2026-08-16T04:06+02:00 — Dagger fixture repair: edge forcing now supplies real runtime config, exact atomic child landing facts, canonical task-doc reads, and a structurally external carryover contract whose memory side aliases the code Git common-dir.
- 2026-08-16T03:24+02:00 — 260815-DAG-L4: redirected shared fixture imports to the dedicated support owner; test behavior and assertions are unchanged. Verification remains closeout-owned.
- 2026-08-15T23:38+02:00 — 260815-DAG-L4: created integration authority edge forcing onboarding from the frozen integration-authority candidate. Verification remains closeout-owned.
