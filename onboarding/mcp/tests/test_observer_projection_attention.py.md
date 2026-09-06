# mcp/tests/test_observer_projection_attention.py

| Field                  | Value                                            |
| ---------------------- | ------------------------------------------------ |
| repository             | agents-remember                                  |
| path                   | `mcp/tests/test_observer_projection_attention.py`                                            |
| doc_type               | `file-level-onboarding`                          |
| lastUpdated | 2026-09-06T21:46+00:00 |
| lastVerifiedCommitHash | `d36109038b3f2b500c138f9dc1ea9c9f9a247489`                                        |
| lastVerifiedCommitDate | 2026-09-06T22:21:49+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[Test suite overview](overview.md)

## Purpose

Attention priority and occurrence-scoped dismissal behavior.

## Code Commentary

### Logic

Provider-down alarms precede blocked asks. A dismissal suppresses the current actionable-drift occurrence, while a newer snapshot surfaces it again. A later turn end similarly supersedes an awaiting-developer dismissal.

### Conventions

This card describes the retained source at IAS `d3610903`. Historical entries below record earlier test populations; they do not require restoring removed cases. Source inspection is memory preparation and does not claim a test run or acceptance.

### Invariants And Boundaries

Dismissal acknowledges one triggering occurrence, not every future event of the same kind. Durable timestamps determine resurfacing.

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
| Blocked and provider down rank alarm first. | `test_blocked_and_provider_down_rank_alarm_first` | mcp/tests/test_observer_projection_attention.py:21-43 |
| Dismiss suppresses actionable drift until newer snapshot. | `test_dismiss_suppresses_actionable_drift_until_newer_snapshot` | mcp/tests/test_observer_projection_attention.py:91-130 |
| Newer turn end supersedes dismissal. | `test_newer_turn_end_supersedes_dismissal` | mcp/tests/test_observer_projection_attention.py:132-158 |

## Cross-Repo References

No cross-repository implementation evidence is required for these local test and fixture claims.

| Finding | Anchor | Source |
| --- | --- | --- |
| Fixture repositories and protocol doubles do not establish a live external integration. | N/A | N/A |

## Update History

- 2026-09-06T21:46+00:00 — Reconciled the actual retained source after IAS test simplification at d3610903: corrected fixture/test roles, removed obsolete current-coverage claims and refreshed existing-source citations. Earlier entries remain historical; verification stamps remain closeout-owned.


- 2026-08-07T22:45:00+02:00 — 260731-EFA-L7 curator: created this file-level onboarding card for the split module; content derived from the current worktree source. Verification metadata pinned until closeout stamps the 260731-EFA-L7 commit.
