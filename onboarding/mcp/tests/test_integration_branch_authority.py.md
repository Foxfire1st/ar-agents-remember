# mcp/tests/test_integration_branch_authority.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/test_integration_branch_authority.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-08-16T04:06+02:00 |
| lastVerifiedCommitHash | `8bf6edad7e7e65e27cf735be0822f604531d0c8a` |
| lastVerifiedCommitDate | 2026-08-16T10:54:02+02:00|
| governingOverview | `../overview.md` |

## Governing Overview

[governing overview](../overview.md)

## Purpose

Exercises the repository-global surface census, exact operation authority, alias/default refusal, CAS and rollback, conflict handoff, crash recovery, and bootstrap WAL.

## Code Commentary

The broad production-bound matrix covers code and external memory, linked worktrees, missing/corrupt authority, duplicate workers, and hard-crash recovery without substituting ambient checkout facts. Shared configured-repository and closed-leaf builders live in `integration_branch_authority_test_support.py` so this file remains focused on assertions.

## Invariants And Boundaries

- The suite exercises production owners rather than copying their state-transition logic.
- Refusal cases assert no unauthorized Git, contract, queue, task, or memory mutation.
- Crash/retry cases retain exact durable identity and expected-old facts.

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The focused suite owns this L4 authority boundary. | `IntegrationBranchAuthorityTests` | mcp/tests/test_integration_branch_authority.py:77-1029 |

## Documentation References

No configured domain-documentation or cross-repository source applies to this file.

## Update History

- 2026-08-16T05:18+02:00 — Dagger fixture repair: repository-global standalone census expectations include the concurrently commanded atomic sibling, and journaled candidate worktrees remain inside their contract-owned worktree group.
- 2026-08-16T04:06+02:00 — Dagger fixture repair: exact authority tests now use recorded leaf worktrees, named atomic-memory checkouts, standalone default sources, active-task surface lifetime, and fresh paired bootstrap recovery facts.
- 2026-08-16T03:29+02:00 — No content impact: retargeted the injected Git-error mock to the extracted repository-facts owner so the same fail-closed public assertion remains executable after the size split. Verification remains closeout-owned.
- 2026-08-16T03:24+02:00 — 260815-DAG-L4: moved shared fixture builders to the dedicated support module without changing the production routes or assertions. Verification remains closeout-owned.
- 2026-08-15T23:38+02:00 — 260815-DAG-L4: created integration branch authority forcing onboarding from the frozen integration-authority candidate. Verification remains closeout-owned.
