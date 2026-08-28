# mcp/tests/test_code_quality_check_scope.py

| Field                  | Value                                            |
| ---------------------- | ------------------------------------------------ |
| repository             | agents-remember                                  |
| path                   | `mcp/tests/test_code_quality_check_scope.py`                                            |
| doc_type               | `file-level-onboarding`                          |
| lastUpdated | 2026-08-28T07:20+02:00 |
| lastVerifiedCommitHash | a06d2ffcfae2c277f2ae19330c17d09c616b77e8 |
| lastVerifiedCommitDate | 2026-08-28T13:58:55+02:00 |
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
| The configuration regression pins automatic xdist worker selection at the root pytest owner. | "self.assertIn(\"-n=auto\", ini_strings(\"addopts\"))" | mcp/tests/test_code_quality_check_scope.py:280-280 |

## 260824-PDLS Admission Boundary

Constructed quality configurations now carry the already-validated `QUALITY_TEST_ADMISSION`.
Scope derivation semantics are unchanged; the new field proves even direct unit construction cannot
reach pytest planning without certifying admission.

## 2026-08-26 Product-Only Coverage Scope

The derived quality scope now separates product measurement from test execution: product package
paths populate `coverage_paths`, while test paths remain in `test_paths` and are executed without
being offered as Coverage.py targets. The regression assertions pin that split both for this
repository and for synthetic package/test repositories.

## 2026-08-28 Explicit Package Authority

Scope derivation now starts from declared product and verification package roots. Every discovered
importable package must belong to exactly one side; overlap, stale declarations, new undeclared
packages, and an empty operational product set fail loudly. Verification packages remain in
lint/type scope while only product roots feed coverage and CRAP. The Dagger implementation package
is no longer conditionally inserted into product coverage.

## Update History

- 2026-08-28T06:28+02:00 — PDLS wave 005 curator: documented exhaustive product-versus-verification
  package ownership and the overlap/stale/undeclared/empty-product refusal cases.

- 2026-08-26T10:44:52+02:00 — Updated the scope contract to product-only coverage measurement while preserving test execution and whole-tree lint/type ownership.
- 2026-08-24T21:23+02:00 — Added the typed admission precondition; scope behavior is unchanged.

- 2026-08-12T15:56+02:00 — 260731-EFA-L23 curator body review: reconciled this card with the exact current source delta described above; verification provenance remains closeout-owned.

- 2026-08-12T00:20+02:00 — Corrected the test boundary after automatic worker selection moved
  from wrapper argv to root pytest `addopts`; the regression now asserts that single owner.
  Verification metadata remains pinned until closeout.

- 2026-08-11T23:56+02:00 — Recorded the focused assertion that the constructed pytest command
  contains `-n auto` alongside the derived coverage scope. Verification metadata remains pinned
  until closeout.

- 2026-08-07T22:45:00+02:00 — 260731-EFA-L7 curator: created this file-level onboarding card for the split module; content derived from the current worktree source. Verification metadata pinned until closeout stamps the 260731-EFA-L7 commit.
