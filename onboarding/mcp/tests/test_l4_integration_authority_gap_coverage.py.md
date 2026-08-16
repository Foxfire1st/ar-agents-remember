# mcp/tests/test_l4_integration_authority_gap_coverage.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/test_l4_integration_authority_gap_coverage.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-08-16T08:12+02:00 |
| lastVerifiedCommitHash | `8bf6edad7e7e65e27cf735be0822f604531d0c8a` |
| lastVerifiedCommitDate | 2026-08-16T10:54:02+02:00|
| governingOverview | `../overview.md` |

## Governing Overview

[governing overview](../overview.md)

## Purpose

Forces task-derived integration target, ordinary-worktree, series-terminal, and repository-checkout
authority refusals that are deliberately rare in positive lifecycle suites.

## Code Commentary

The cases pin standalone/default landing restrictions, shared code-memory identity refusal, checked
out branch/repository identity, exact atomic spelling and parent protection, parent-series shape,
and contract-independent carryover checkout authority.

## Invariants And Boundaries

- Every negative case calls the real authority owner.
- No compatibility alias or default-branch fallback is introduced for tests.
- Series and leaf authority remain distinct surfaces.

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The suite owns focused branch gaps in task-derived integration authority. | `IntegrationTargetGapCoverageTests`; `OrdinaryAndTerminalAuthorityGapCoverageTests`; `RepositoryCheckoutGapCoverageTests` | mcp/tests/test_l4_integration_authority_gap_coverage.py:42-131; mcp/tests/test_l4_integration_authority_gap_coverage.py:134-317; mcp/tests/test_l4_integration_authority_gap_coverage.py:320-350 |

## Documentation References

No configured domain-documentation or cross-repository source applies to this file.

## Update History

- 2026-08-16T08:12+02:00 — Created focused L4 task-derived authority forcing during targeted Dagger coverage repair.
