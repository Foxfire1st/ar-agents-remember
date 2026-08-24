# mcp/src/agents_remember/testing/pytest_certifying_bootstrap.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/testing/pytest_certifying_bootstrap.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-08-24T21:23+02:00 |
| lastVerifiedCommitHash | `b99501852bcfa5f499a25e7183063751f6133a28` |
| lastVerifiedCommitDate | 2026-08-24T21:21:58+02:00 |
| governingOverview | `overview.md` |

## Governing Overview

[Python testing boundary](overview.md)

## Purpose

Contains pytest session fixtures that exist only in the certifying Dagger route.

## Code Commentary

The autouse session fixture binds worktree services for the certifying suite and guarantees
teardown. Root conftest loads this plugin after Dagger admission; the diagnostic command does not.

## Invariants And Boundaries

- Provider/worktree services never leak into diagnostic bootstrap.
- Admission must already have succeeded before pytest imports this plugin.
- Teardown runs through the fixture context on failure and success.

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| Certifying-only session setup binds worktree services. | `_bind_worktree_services_for_session` | mcp/src/agents_remember/testing/pytest_certifying_bootstrap.py:19-25 |

## Update History

- 2026-08-24T21:23+02:00 — Extracted from root conftest for 260824-PDLS.
