# test_cli_discovery.py

| Field                  | Value                                            |
| ---------------------- | ------------------------------------------------ |
| repository             | agents-remember                                  |
| path                   | `mcp/tests/test_cli_discovery.py`                |
| doc_type               | `file-level-onboarding`                          |
| lastUpdated | 2026-09-06T21:38+00:00 |
| lastVerifiedCommitHash | `ae8c47ce897b04380ebcb80f750d77ed4dc9f37d`       |
| lastVerifiedCommitDate | 2026-08-26T08:10:26+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[Test suite overview](overview.md)

## Purpose

Trusted CLI settings discovery through temporary directory trees.

## Code Commentary

### Logic

Same-directory convention settings beat registration, but a nearer registration beats a farther convention. Malformed, missing-config-argument and foreign-server registrations are skipped. A miss names both searched patterns and the resolved starting directory.

### Conventions

This card describes the retained source at IAS `d3610903`. Historical entries below record earlier test populations; they do not require restoring removed cases. Source inspection is memory preparation and does not claim a test run or acceptance.

### Invariants And Boundaries

Usable fixture settings point to an existing absolute coordination directory. The retained four cases do not include the old placeholder-template or missing-target-file tests.

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
| Convention wins over registration in the same directory. | `test_convention_wins_over_registration_in_the_same_directory` | mcp/tests/test_cli_discovery.py:43-51 |
| Nearest directory wins across levels. | `test_nearest_directory_wins_across_levels` | mcp/tests/test_cli_discovery.py:53-61 |
| Malformed and foreign registrations are skipped. | `test_malformed_and_foreign_registrations_are_skipped` | mcp/tests/test_cli_discovery.py:63-78 |
| Miss raises with both patterns and the origin. | `test_miss_raises_with_both_patterns_and_the_origin` | mcp/tests/test_cli_discovery.py:80-89 |

## Cross-Repo References

No cross-repository implementation evidence is required for these local test and fixture claims.

| Finding | Anchor | Source |
| --- | --- | --- |
| Fixture repositories and protocol doubles do not establish a live external integration. | N/A | N/A |

## Update History

- 2026-09-06T21:38+00:00 — Reconciled the actual retained source after IAS test simplification at d3610903: corrected fixture/test roles, removed obsolete current-coverage claims and refreshed existing-source citations. Earlier entries remain historical; verification stamps remain closeout-owned.

- 2026-08-02T16:44:03+02:00 — W1-B07 curator: repaired 2 repository-reference citations (2/2 anchored and sourced; scoped citation check clean).

- 2026-07-03T09:55+02:00 — Created for 260703 L1 alongside `cli/discovery.py` (8 tests: hits,
  precedence, nearest-wins, tolerance, template skip, miss error). Verification metadata pinned
  until closeout stamps the code commit.
