# mcp/tests/test_atomic_series_activation.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/test_atomic_series_activation.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-06T21:38+00:00 |
| lastVerifiedCommitHash |  `ae8c47ce897b04380ebcb80f750d77ed4dc9f37d`|
| lastVerifiedCommitDate |  2026-08-26T08:10:26+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[Test suite overview](overview.md)

## Purpose

Source-pair-scoped atomic-series selection tests.

## Code Commentary

### Logic

Selecting master B pauses master A logically without deleting either contract. A second case changes the code source branch and observes a distinct vacant activation path, establishing isolation by source pair.

### Conventions

This card describes the retained source at IAS `d3610903`. Historical entries below record earlier test populations; they do not require restoring removed cases. Source inspection is memory preparation and does not claim a test run or acceptance.

### Invariants And Boundaries

Logical active ownership is separate from work retirement; selecting another master must not imply abandoned work.

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
| Selection switches logical active owner without retiring work. | `test_selection_switches_logical_active_owner_without_retiring_work` | mcp/tests/test_atomic_series_activation.py:104-123 |
| Source pairs are isolated. | `test_source_pairs_are_isolated` | mcp/tests/test_atomic_series_activation.py:125-137 |

## Cross-Repo References

No cross-repository implementation evidence is required for these local test and fixture claims.

| Finding | Anchor | Source |
| --- | --- | --- |
| Fixture repositories and protocol doubles do not establish a live external integration. | N/A | N/A |

## Update History

- 2026-09-06T21:38+00:00 — Reconciled the actual retained source after IAS test simplification at d3610903: corrected fixture/test roles, removed obsolete current-coverage claims and refreshed existing-source citations. Earlier entries remain historical; verification stamps remain closeout-owned.


- 2026-08-26T08:20+02:00 — Final frozen reconciliation of selector replacement, isolation,
  archive, vacancy, and exact-release forcing.

- 2026-08-26T05:40+02:00 — Added the completed nonregular selector quarantine forcing case to the
  suite description. Final ranges remain post-Dagger-owned.

- 2026-08-26T02:55+02:00 — Drafted focused selector-test onboarding; post-Dagger test inventory,
  nonregular-entry case, exact ranges, and verification remain open.