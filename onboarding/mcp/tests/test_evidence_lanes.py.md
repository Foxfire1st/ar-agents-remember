# mcp/tests/test_evidence_lanes.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/test_evidence_lanes.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-06T21:46+00:00 |
| lastVerifiedCommitHash | a06d2ffcfae2c277f2ae19330c17d09c616b77e8 |
| lastVerifiedCommitDate | 2026-08-28T13:58:55+02:00 |
| governingOverview | `overview.md` |

## Governing Overview

[Test suite overview](overview.md)

## Purpose

Evidence-lane registry completeness and uniqueness validation.

## Code Commentary

### Logic

The retained test removes a required category, duplicates a category and reuses a marker; each malformed registry raises the specific UsageError. Small item/config and manifest fixtures remain available to consumers.

### Conventions

This card describes the retained source at IAS `d3610903`. Historical entries below record earlier test populations; they do not require restoring removed cases. Source inspection is memory preparation and does not claim a test run or acceptance.

### Invariants And Boundaries

This single registry test does not enumerate every collected node or prove the historical classification matrix. Missing authority is a refusal rather than an implicit default lane.

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
| Incomplete or ambiguous registry is refused. | `test_incomplete_or_ambiguous_registry_is_refused` | mcp/tests/test_evidence_lanes.py:66-74 |

## Cross-Repo References

No cross-repository implementation evidence is required for these local test and fixture claims.

| Finding | Anchor | Source |
| --- | --- | --- |
| Fixture repositories and protocol doubles do not establish a live external integration. | N/A | N/A |

## Update History

- 2026-09-06T21:46+00:00 — Reconciled the actual retained source after IAS test simplification at d3610903: corrected fixture/test roles, removed obsolete current-coverage claims and refreshed existing-source citations. Earlier entries remain historical; verification stamps remain closeout-owned.


- 2026-08-28T06:28+02:00 — PDLS wave 005 curator: created the missing sidecar for exhaustive,
  explicit, fail-loud evidence-lane classification.
