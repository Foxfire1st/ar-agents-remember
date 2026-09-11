# mcp/test_support/agents_remember_test_support/testing/pytest_bootstrap.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/test_support/agents_remember_test_support/testing/pytest_bootstrap.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-08-28T07:20+02:00 |
| lastVerifiedCommitHash | a06d2ffcfae2c277f2ae19330c17d09c616b77e8 |
| lastVerifiedCommitDate | 2026-08-28T13:58:55+02:00 |
| governingOverview | `overview.md` |

## Governing Overview

[Python testing boundary](overview.md)

## Purpose

Owns route-neutral pytest hooks: process declaration, cache isolation, deterministic order, and
owned-global leak restoration.

## Code Commentary

The plugin begins the declared test process at import, exposes the random-order seed option/header,
shuffles collection deterministically when configured, isolates per-process cache, restores and
reports owned global leaks, and ends the process at pytest unconfigure.

## Invariants And Boundaries

- This module imports no Dagger admission, worktree service, or provider code.
- Both routes receive identical shared pytest behavior.
- Global restoration precedes leak failure.

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| Shared hooks own ordering and process cleanup. | `pytest_collection_modifyitems`; `reject_owned_global_state_leaks`; `pytest_unconfigure` | mcp/test_support/agents_remember_test_support/testing/pytest_bootstrap.py:22-24; mcp/test_support/agents_remember_test_support/testing/pytest_bootstrap.py:41-58; mcp/test_support/agents_remember_test_support/testing/pytest_bootstrap.py:61-70 |

## Update History

- 2026-08-24T21:23+02:00 — Extracted from root conftest for 260824-PDLS.
