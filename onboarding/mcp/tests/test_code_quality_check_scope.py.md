# mcp/tests/test_code_quality_check_scope.py

| Field                  | Value                                            |
| ---------------------- | ------------------------------------------------ |
| repository             | agents-remember                                  |
| path                   | `mcp/tests/test_code_quality_check_scope.py`                                            |
| doc_type               | `file-level-onboarding`                          |
| lastUpdated            | 2026-08-11T23:56+02:00                                            |
| lastVerifiedCommitHash | `5aff1e8f01dfa949efc8f68e46bc62a99ed31432`                                        |
| lastVerifiedCommitDate | 2026-08-14T14:36:50+02:00|
| governingOverview      | `overview.md`                                          |

## Governing Overview

[mcp/tests overview](overview.md)

## Purpose

`test_code_quality_check_scope.py` pins repository-derived gate scope, fixed command vectors, and
the root pytest configuration inherited by raw and wrapped test runs.

## Code Commentary

L23 lets whole-tree scope expectations include the Dagger package when present, while preserving MCP coverage and test roots.

- `GateScopeDerivationTests`
- `PytestConfigurationTests`
- `PytestConfigurationTests` asserts root `addopts` contains `-n=auto` alongside the strictness
  switches; the derived-scope command test remains focused on coverage arguments.

## Invariants And Boundaries

- The card mirrors the source file one-to-one at `mcp/tests/test_code_quality_check_scope.py`.

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The module's own top-level surface is listed in Code Commentary; no cross-file citation rows are needed for this split module. | — | — |
| The configuration regression pins automatic xdist worker selection at the root pytest owner. | "self.assertIn(\"-n=auto\", ini_strings(\"addopts\"))" | mcp/tests/test_code_quality_check_scope.py:215-223 |

## Update History

- 2026-08-12T15:56+02:00 — 260731-EFA-L23 curator body review: reconciled this card with the exact current source delta described above; verification provenance remains closeout-owned.

- 2026-08-12T00:20+02:00 — Corrected the test boundary after automatic worker selection moved
  from wrapper argv to root pytest `addopts`; the regression now asserts that single owner.
  Verification metadata remains pinned until closeout.

- 2026-08-11T23:56+02:00 — Recorded the focused assertion that the constructed pytest command
  contains `-n auto` alongside the derived coverage scope. Verification metadata remains pinned
  until closeout.

- 2026-08-07T22:45:00+02:00 — 260731-EFA-L7 curator: created this file-level onboarding card for the split module; content derived from the current worktree source. Verification metadata pinned until closeout stamps the 260731-EFA-L7 commit.
