# mcp/tests/test_integration_authority_lowest_writers.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/test_integration_authority_lowest_writers.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-08-15T23:38+02:00 |
| lastVerifiedCommitHash | `8bf6edad7e7e65e27cf735be0822f604531d0c8a` |
| lastVerifiedCommitDate | 2026-08-16T10:54:02+02:00|
| governingOverview | `../overview.md` |

## Governing Overview

[governing overview](../overview.md)

## Purpose

Proves direct facades, ref movers, checkout refreshers, and bootstrap rollback cannot mutate without journal-bound capabilities.

## Code Commentary

Tests call the actual lowest writers and assert unauthorized calls leave refs and checkouts unchanged.

## Invariants And Boundaries

- The suite exercises production owners rather than copying their state-transition logic.
- Refusal cases assert no unauthorized Git, contract, queue, task, or memory mutation.
- Crash/retry cases retain exact durable identity and expected-old facts.

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The focused suite owns this L4 authority boundary. | `IntegrationAuthorityLowestWriterTests` | mcp/tests/test_integration_authority_lowest_writers.py:15-71 |

## Documentation References

No configured domain-documentation or cross-repository source applies to this file.

## Update History

- 2026-08-15T23:38+02:00 — 260815-DAG-L4: created lowest integration-writer forcing onboarding from the frozen integration-authority candidate. Verification remains closeout-owned.
