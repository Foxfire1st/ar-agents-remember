# mcp/tests/test_crap_calculator.py

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember                            |
| path                   | `mcp/tests/test_crap_calculator.py`        |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated | 2026-09-06T21:46+00:00 |
| lastVerifiedCommitHash | a06d2ffcfae2c277f2ae19330c17d09c616b77e8 |
| lastVerifiedCommitDate | 2026-08-28T13:58:55+02:00 |
| governingOverview | `overview.md` |

## Governing Overview

[Test suite overview](overview.md)

## Purpose

CRAP diagnostic arithmetic and branch-measured function scoring.

## Code Commentary

### Logic

The formula uses a coverage ratio; the fixture joins Radon complexity with Coverage.py executable-line and branch information. A partially covered branchy function receives a higher score than a fully covered simple function. Reports without branch measurement refuse instead of fabricating a ratio.

### Conventions

This card describes the retained source at IAS `d3610903`. Historical entries below record earlier test populations; they do not require restoring removed cases. Source inspection is memory preparation and does not claim a test run or acceptance.

### Invariants And Boundaries

These tests validate measurement, not a coverage percentage floor or blocking CRAP threshold. CLI rendering and historical rollup matrices are not retained cases here.

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
| Crap score formula uses coverage ratio. | `test_crap_score_formula_uses_coverage_ratio` | mcp/tests/test_crap_calculator.py:16-18 |
| Calculates function scores from radon and coverage json. | `test_calculates_function_scores_from_radon_and_coverage_json` | mcp/tests/test_crap_calculator.py:20-43 |
| A report without branch measurement is refused. | `test_a_report_without_branch_measurement_is_refused` | mcp/tests/test_crap_calculator.py:45-67 |

## Cross-Repo References

No cross-repository implementation evidence is required for these local test and fixture claims.

| Finding | Anchor | Source |
| --- | --- | --- |
| Fixture repositories and protocol doubles do not establish a live external integration. | N/A | N/A |

## Update History

- 2026-09-06T21:46+00:00 — Reconciled the actual retained source after IAS test simplification at d3610903: corrected fixture/test roles, removed obsolete current-coverage claims and refreshed existing-source citations. Earlier entries remain historical; verification stamps remain closeout-owned.


- 2026-08-05T00:45:16+02:00 — 260731-EFA-L6 S18-B23 curator: replaced the `n/a` rows with exact
  anchors and fixer-generated ranges; exact non-fixing check returns zero findings.

- 2026-07-31T15:32+02:00 — 260731-EFA-L2 curator: rewritten. The previous card described a
  statement-coverage reader; CRAP now consumes branch coverage and refuses a report without
  it. Recorded the five branch-arc tests, the 30.0 → 20.0 threshold change and where its
  justification lives, and `coverage_clearing`'s split-instead-of-test answer. Verification
  metadata is pinned to the leaf's reformat commit until closeout stamps the code commit.
- 2026-05-24T06:12+02:00: Updated after tests added rollup and CLI rendering coverage.
- 2026-05-24T06:05+02:00: Created unit coverage for CRAP-Calculator.
