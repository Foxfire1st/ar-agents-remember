# mcp/tests/test_clean_quality_executor.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/test_clean_quality_executor.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-08-12T15:19+02:00 |
| lastVerifiedCommitHash |  `c9ae4dbd8adb650f116b9d4f86343b496c3e5f32`|
| lastVerifiedCommitDate |  2026-08-12T17:53:40+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[mcp/tests overview](overview.md)

## Purpose

This suite forces the host-side Dagger executor through exact candidate capture, export, result parsing, report publication, Git guards, progress streaming, and native executable resolution.

## Code Commentary

### Logic

Tests build temporary Git repositories and intercept only the Dagger process boundary. They prove the staged candidate and ancestry are passed once, invalid modes and Windows roots refuse, export failures cannot proceed, invalid results cannot be guessed green, and partial output is observable before completion.

### Conventions

Real Git state is used where candidate identity matters; process transport is doubled narrowly.

### Invariants And Boundaries

- The executor must publish no invented result after export failure.
- Candidate and report Git guards fail closed.
- Dagger resolution passes through the native-command policy.

### Todos

None.

## Docs References

No external Domain Documentation source is configured for this suite.

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured external document is required for the repository-owned executor contract. | — | — |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| Exact candidate, refusal, export, result, reporting, and native-command behavior are forced. | `CleanQualityExecutorTests` | mcp/tests/test_clean_quality_executor.py:38-223 |

## Cross-Repo References

No sibling-repository contract is exercised.

| Finding | Anchor | Source |
| --- | --- | --- |
| Temporary Git repositories isolate each executor proof. | `repository` | mcp/tests/test_clean_quality_executor.py:18-36 |

## Update History

- 2026-08-12T15:19+02:00 — Created with L23 clean quality executor tests; verification provenance remains closeout-owned.
