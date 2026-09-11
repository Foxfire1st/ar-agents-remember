# mcp/tests/test_harness_control_claude_interrupt.py

| Field                  | Value                                            |
| ---------------------- | ------------------------------------------------ |
| repository             | agents-remember                                  |
| path                   | `mcp/tests/test_harness_control_claude_interrupt.py`                                            |
| doc_type               | `file-level-onboarding`                          |
| lastUpdated | 2026-09-06T21:46+00:00 |
| lastVerifiedCommitHash | `d36109038b3f2b500c138f9dc1ea9c9f9a247489`                                        |
| lastVerifiedCommitDate | 2026-09-06T22:21:49+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[Test suite overview](overview.md)

## Purpose

Claude native interrupt acknowledgement and terminal-outcome correlation.

## Code Commentary

### Logic

Accepted interrupt settles a matching interrupted turn as cancelled and replays its first acknowledgement without another native write. Guard failures write nothing. A racing rate-limit error stays failed and natural completion stays completed. Lost acknowledgement remains unknown until late correlated evidence resolves it.

### Conventions

This card describes the retained source at IAS `d3610903`. Historical entries below record earlier test populations; they do not require restoring removed cases. Source inspection is memory preparation and does not claim a test run or acceptance.

### Invariants And Boundaries

Interrupt acknowledgement is not terminal success. The fixture uses structured stream-json frames, not a terminal paste or inferred text match.

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
| Accepted interrupt settles interrupted not failed. | `test_accepted_interrupt_settles_interrupted_not_failed` | mcp/tests/test_harness_control_claude_interrupt.py:66-107 |
| Interrupt replays first acknowledgement without a second write. | `test_interrupt_replays_first_acknowledgement_without_a_second_write` | mcp/tests/test_harness_control_claude_interrupt.py:109-123 |
| Interrupt guards reject before any native write. | `test_interrupt_guards_reject_before_any_native_write` | mcp/tests/test_harness_control_claude_interrupt.py:125-138 |
| Accepted interrupt racing a rate limit error stays failed. | `test_accepted_interrupt_racing_a_rate_limit_error_stays_failed` | mcp/tests/test_harness_control_claude_interrupt.py:155-184 |
| Natural completion after an accepted interrupt stays completed. | `test_natural_completion_after_an_accepted_interrupt_stays_completed` | mcp/tests/test_harness_control_claude_interrupt.py:186-204 |
| Lost acknowledgement is unknown and a late success still correlates. | `test_lost_acknowledgement_is_unknown_and_a_late_success_still_correlates` | mcp/tests/test_harness_control_claude_interrupt.py:207-245 |

## Cross-Repo References

No cross-repository implementation evidence is required for these local test and fixture claims.

| Finding | Anchor | Source |
| --- | --- | --- |
| Fixture repositories and protocol doubles do not establish a live external integration. | N/A | N/A |

## Update History

- 2026-09-06T21:46+00:00 — Reconciled the actual retained source after IAS test simplification at d3610903: corrected fixture/test roles, removed obsolete current-coverage claims and refreshed existing-source citations. Earlier entries remain historical; verification stamps remain closeout-owned.


- 2026-08-08T17:18+02:00 — No content impact: 260731-EFA-L9 rewrote this source's imports/callers only (model-extraction caller wave); the behavior this card documents is unchanged and the body was re-verified current. Verification metadata pinned until closeout stamps the L9 code commit.

- 2026-08-07T22:45:00+02:00 — 260731-EFA-L7 curator: created this file-level onboarding card for the split module; content derived from the current worktree source. Verification metadata pinned until closeout stamps the 260731-EFA-L7 commit.
