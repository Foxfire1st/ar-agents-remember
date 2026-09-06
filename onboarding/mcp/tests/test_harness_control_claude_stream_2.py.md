# mcp/tests/test_harness_control_claude_stream_2.py

| Field                  | Value                                            |
| ---------------------- | ------------------------------------------------ |
| repository             | agents-remember                                  |
| path                   | `mcp/tests/test_harness_control_claude_stream_2.py`                                            |
| doc_type               | `file-level-onboarding`                          |
| lastUpdated | 2026-09-06T21:46+00:00 |
| lastVerifiedCommitHash | `d36109038b3f2b500c138f9dc1ea9c9f9a247489`                                        |
| lastVerifiedCommitDate | 2026-09-06T22:21:49+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[Test suite overview](overview.md)

## Purpose

Claude model/effort echo and ambiguous-delivery recovery.

## Code Commentary

### Logic

Model and effort setters require correlated terminal echoes and respect the selected model menu. Timed-out setter replay is neutralized before a clean retry. Disconnect stays unknown without resend; later structured history may reconcile accepted delivery. Nonzero exit fails control, and forced stop reclaims a reader blocked by a full event queue.

### Conventions

This card describes the retained source at IAS `d3610903`. Historical entries below record earlier test populations; they do not require restoring removed cases. Source inspection is memory preparation and does not claim a test run or acceptance.

### Invariants And Boundaries

Queued or unknown is not effective selection. Late transport evidence must reconcile the original operation rather than submit it again.

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
| Model and effort set require terminal echo and update model gate. | `test_model_and_effort_set_require_terminal_echo_and_update_model_gate` | mcp/tests/test_harness_control_claude_stream_2.py:26-78 |
| Set timeout neutralizes late replay before a clean retry. | `test_set_timeout_neutralizes_late_replay_before_a_clean_retry` | mcp/tests/test_harness_control_claude_stream_2.py:80-114 |
| Disconnect reconciliation stays unknown and never resends. | `test_disconnect_reconciliation_stays_unknown_and_never_resends` | mcp/tests/test_harness_control_claude_stream_2.py:116-144 |
| Late replay reconciles unknown from structured history without resend. | `test_late_replay_reconciles_unknown_from_structured_history_without_resend` | mcp/tests/test_harness_control_claude_stream_2.py:146-170 |
| Nonzero process exit maps to failed. | `test_nonzero_process_exit_maps_to_failed` | mcp/tests/test_harness_control_claude_stream_2.py:172-183 |
| Forced stop reclaims a reader blocked by full event queue. | `test_forced_stop_reclaims_a_reader_blocked_by_full_event_queue` | mcp/tests/test_harness_control_claude_stream_2.py:185-195 |

## Cross-Repo References

No cross-repository implementation evidence is required for these local test and fixture claims.

| Finding | Anchor | Source |
| --- | --- | --- |
| Fixture repositories and protocol doubles do not establish a live external integration. | N/A | N/A |

## Update History

- 2026-09-06T21:46+00:00 — Reconciled the actual retained source after IAS test simplification at d3610903: corrected fixture/test roles, removed obsolete current-coverage claims and refreshed existing-source citations. Earlier entries remain historical; verification stamps remain closeout-owned.


- 2026-08-12T23:08+02:00 — 260731-EFA-L23 Dagger flaky-test follow-up: raised only the late-replay regression's compressed acceptance timeout from 5ms to 50ms so loaded xdist scheduling cannot pre-empt the fake reader's replay/result consumption. Production remains 30 seconds. Evidence: 1/100 failure before plus one Dagger gw16 failure; 100/100 one-process repetitions after, with exact-file Ruff clean. Verification remains closeout-owned.
- 2026-08-08T17:18+02:00 — No content impact: 260731-EFA-L9 rewrote this source's imports/callers only (model-extraction caller wave); the behavior this card documents is unchanged and the body was re-verified current. Verification metadata pinned until closeout stamps the L9 code commit.

- 2026-08-07T22:45:00+02:00 — 260731-EFA-L7 curator: created this file-level onboarding card for the split module; content derived from the current worktree source. Verification metadata pinned until closeout stamps the 260731-EFA-L7 commit.
