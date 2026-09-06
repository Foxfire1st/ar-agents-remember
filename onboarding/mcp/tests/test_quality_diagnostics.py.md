# mcp/tests/test_quality_diagnostics.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/test_quality_diagnostics.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-06T21:35:26+00:00 |
| lastVerifiedCommitHash | `d36109038b3f2b500c138f9dc1ea9c9f9a247489`|
| lastVerifiedCommitDate | 2026-09-06T22:21:49+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[Tests overview](overview.md)

## Purpose

Proves that diagnostic metric findings remain visible without blocking delivery.

## Code Commentary

### Logic

Two tests inject a measured zero-percent diff result and a production CRAP score of 72. The real post-coverage reporting functions return zero while printing the findings and review threshold 20. Measurement/calculation are mocked; these cases prove result interpretation, not real Git diff parsing or actual coverage collection. They also reject a required-branch-coverage prescription.

### Conventions

These are focused unit cases under the canonical evidence-lane manifest. Reuse their behavior
boundary when changing policy rather than adding duplicate metric or collection assertions.

### Invariants And Boundaries

Default budgets are 1000 unit and150 integration collected cases. Coverage is diagnostic; production
CRAP 20 triggers review without failing delivery. Full suites and whole-candidate review occur at
master completion. A green unit result is not a certification certificate.

### Todos

Verification metadata remains closeout-owned; this card records source inspection only.

## Docs References

No Domain Documentation source is configured; this behavior is repository-owned.

| Finding | Anchor | Source |
| --- | --- | --- |
| No external domain claim is needed. | N/A | N/A |

## Repo-Internal References

The exact functions below establish the tested boundary and its test doubles.

| Finding | Anchor | Source |
| --- | --- | --- |
| Proves that diagnostic metric findings remain visible without blocking delivery. | `test_low_coverage_is_reported_without_failing_delivery` | mcp/tests/test_quality_diagnostics.py:20-49 |
| Proves that diagnostic metric findings remain visible without blocking delivery. | `test_high_crap_requests_review_without_failing_delivery` | mcp/tests/test_quality_diagnostics.py:52-75 |

## Cross-Repo References

No cross-repository protocol is exercised by these unit cases.

| Finding | Anchor | Source |
| --- | --- | --- |
| No external boundary is claimed. | N/A | N/A |

## Update History

- 2026-09-06T21:35:26+00:00 — Documented the actual d3610903 unit behavior and test-double limits without claiming an unrun verification pass.
