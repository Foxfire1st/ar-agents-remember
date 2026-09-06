# mcp/tests/test_code_quality_check_scope.py

| Field                  | Value                                            |
| ---------------------- | ------------------------------------------------ |
| repository             | agents-remember                                  |
| path                   | `mcp/tests/test_code_quality_check_scope.py`                                            |
| doc_type               | `file-level-onboarding`                          |
| lastUpdated | 2026-09-06T21:38+00:00 |
| lastVerifiedCommitHash | a06d2ffcfae2c277f2ae19330c17d09c616b77e8 |
| lastVerifiedCommitDate | 2026-08-28T13:58:55+02:00 |
| governingOverview | `overview.md` |

## Governing Overview

[Test suite overview](overview.md)

## Purpose

Explicit product/verification package ownership tests.

## Code Commentary

### Logic

A newly importable support package refuses until assigned a product or verification owner. Declaring it verification preserves lint/type inclusion while excluding it from product coverage paths. Overlapping and stale ownership declarations refuse.

### Conventions

This card describes the retained source at IAS `d3610903`. Historical entries below record earlier test populations; they do not require restoring removed cases. Source inspection is memory preparation and does not claim a test run or acceptance.

### Invariants And Boundaries

Coverage paths describe measurement scope, not a percentage requirement. No fallback ownership broadening is allowed for unowned packages.

### Todos

No file-local implementation change is requested by this reconciliation.

## Docs References

No Domain Documentation entries are configured in this memory root. These are repository-owned fixture and assertion contracts; no external library behavior is inferred.

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured domain evidence applies to the file-local claims above. | N/A | N/A |

## Repo-Internal References

The retained source anchors below support the fixture roles and assertion boundaries described above. They identify current behavior, not a request to restore historical test counts or percentage targets.

| Finding | Anchor | Source |
| --- | --- | --- |
| New importable package requires explicit product or verification owner. | `test_new_importable_package_requires_explicit_product_or_verification_owner` | mcp/tests/test_code_quality_check_scope.py:15-40 |
| Package authority rejects overlap and stale declarations. | `test_package_authority_rejects_overlap_and_stale_declarations` | mcp/tests/test_code_quality_check_scope.py:42-71 |

## Cross-Repo References

No cross-repository implementation evidence is required for these local test and fixture claims.

| Finding | Anchor | Source |
| --- | --- | --- |
| Fixture repositories and protocol doubles do not establish a live external integration. | N/A | N/A |

## Update History

- 2026-09-06T21:38+00:00 — Reconciled the actual retained source after IAS test simplification at d3610903: corrected fixture/test roles, removed obsolete current-coverage claims and refreshed existing-source citations. Earlier entries remain historical; verification stamps remain closeout-owned.


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
