# mcp/tests/test_layering.py

| Field                  | Value                                                        |
| ---------------------- | ------------------------------------------------------------ |
| repository             | agents-remember                                              |
| path                   | `mcp/tests/test_layering.py`                                  |
| doc_type               | `file-level-onboarding`                                      |
| lastUpdated | 2026-09-06T21:46+00:00 |
| lastVerifiedCommitHash | a06d2ffcfae2c277f2ae19330c17d09c616b77e8 |
| lastVerifiedCommitDate | 2026-08-28T13:58:55+02:00 |
| governingOverview | `overview.md` |

## Governing Overview

[Test suite overview](overview.md)

## Purpose

Import-layer fitness validation over miniature source trees.

## Code Commentary

### Logic

A prohibited lower-to-higher rank import names its importer/imported layer. A compliant tree passes. Importing an undeclared package fails closed and renders the precise module evidence.

### Conventions

This card describes the retained source at IAS `d3610903`. Historical entries below record earlier test populations; they do not require restoring removed cases. Source inspection is memory preparation and does not claim a test run or acceptance.

### Invariants And Boundaries

These cases exercise semantic import boundaries, not a source-pinning matrix. Historical self/star/present-false cases are not independently retained here.

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
| Rank violation fails. | `test_rank_violation_fails` | mcp/tests/test_layering.py:45-64 |
| Clean tree passes. | `test_clean_tree_passes` | mcp/tests/test_layering.py:67-90 |
| Undeclared package import fails. | `test_undeclared_package_import_fails` | mcp/tests/test_layering.py:93-114 |

## Cross-Repo References

No cross-repository implementation evidence is required for these local test and fixture claims.

| Finding | Anchor | Source |
| --- | --- | --- |
| Fixture repositories and protocol doubles do not establish a live external integration. | N/A | N/A |

## Update History

- 2026-09-06T21:46+00:00 — Reconciled the actual retained source after IAS test simplification at d3610903: corrected fixture/test roles, removed obsolete current-coverage claims and refreshed existing-source citations. Earlier entries remain historical; verification stamps remain closeout-owned.


- 2026-08-28T11:32+02:00 — Added a non-default layout case proving exact project-root threading.

- 2026-08-28T06:40+02:00 — No content impact: the layer checker and its executable-module probe
  now resolve through the verification package; the enforced layering contract is unchanged.
- 2026-08-24T21:23+02:00 — Added typed admission to quality-wrapper construction.

- 2026-08-12T01:38+02:00 — 260731-EFA-L22 curator: extended the ignored-artifact regression with
  cache-only deleted-package debris while retaining undeclared real-source coverage.

- 2026-08-08T14:38+02:00 — 260731-EFA-L9 curator: created for the layering unit suite; F-3
  branches and F-4 cycle-coverage note reflected. Verification metadata pinned until closeout
  stamps the L9 code commit.
