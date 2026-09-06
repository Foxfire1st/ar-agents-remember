# mcp/tests/test_file_size_detector.py

| Field                  | Value                                            |
| ---------------------- | ------------------------------------------------ |
| repository             | agents-remember                                  |
| path                   | `mcp/tests/test_file_size_detector.py`                                            |
| doc_type               | `file-level-onboarding`                          |
| lastUpdated | 2026-09-06T21:46+00:00 |
| lastVerifiedCommitHash | `d36109038b3f2b500c138f9dc1ea9c9f9a247489`|
| lastVerifiedCommitDate | 2026-09-06T22:21:49+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[Test suite overview](overview.md)

## Purpose

File-size measurement and report-versus-enforcement command selection.

## Code Commentary

### Logic

Newline counting matches wc-style measurement: 1199 stays below the hard limit while 1200 produces one hard-limit finding. The wrapper includes --report when unarmed and omits it when armed.

### Conventions

This card describes the retained source at IAS `d3610903`. Historical entries below record earlier test populations; they do not require restoring removed cases. Source inspection is memory preparation and does not claim a test run or acceptance.

### Invariants And Boundaries

The remaining cases do not assert every historical size band, CLI exit or empty-measurement path. Size reporting is distinct from restoring test-count or coverage requirements.

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
| Measure counts newlines like wc and flags only hard limit. | `test_measure_counts_newlines_like_wc_and_flags_only_hard_limit` | mcp/tests/test_file_size_detector.py:20-34 |
| Unarmed step reports and armed step fails. | `test_unarmed_step_reports_and_armed_step_fails` | mcp/tests/test_file_size_detector.py:38-68 |

## Cross-Repo References

No cross-repository implementation evidence is required for these local test and fixture claims.

| Finding | Anchor | Source |
| --- | --- | --- |
| Fixture repositories and protocol doubles do not establish a live external integration. | N/A | N/A |

## Update History

- 2026-09-06T21:46+00:00 — Reconciled the actual retained source after IAS test simplification at d3610903: corrected fixture/test roles, removed obsolete current-coverage claims and refreshed existing-source citations. Earlier entries remain historical; verification stamps remain closeout-owned.


- 2026-08-24T21:23+02:00 — Added the typed admission precondition to quality wiring.
- 2026-08-12T15:19+02:00 — L23 curator: re-read the current source-backed claims and retained their wording while the sanctioned MCP citation-fix wave regenerated exact ranges; verification provenance remains closeout-owned.

- 2026-08-07T22:45:00+02:00 — 260731-EFA-L7 curator: created this file-level onboarding card for the detector suite. Verification metadata pinned until closeout stamps the 260731-EFA-L7 commit.
