# mcp/tests/test_controlplane_gates_tool_2.py

| Field                  | Value                                            |
| ---------------------- | ------------------------------------------------ |
| repository             | agents-remember                                  |
| path                   | `mcp/tests/test_controlplane_gates_tool_2.py`                                            |
| doc_type               | `file-level-onboarding`                          |
| lastUpdated | 2026-09-06T21:38+00:00 |
| lastVerifiedCommitHash | `d36109038b3f2b500c138f9dc1ea9c9f9a247489`                                        |
| lastVerifiedCommitDate | 2026-09-06T22:21:49+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[Test suite overview](overview.md)

## Purpose

Gate cancellation, bounded waiting and stale-decision tests.

## Code Commentary

### Logic

Cancel removes the gate and associated inbox entries. Waiting on an open gate times out; response waiting returns a matching pending inbox entry without consuming it. An expected-gate mismatch refuses instead of deciding another lifecycle gate.

### Conventions

This card describes the retained source at IAS `d3610903`. Historical entries below record earlier test populations; they do not require restoring removed cases. Source inspection is memory preparation and does not claim a test run or acceptance.

### Invariants And Boundaries

Receiving a response and consuming it are separate operations. Stale identity cannot be substituted with the newest available gate.

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
| Cancel deletes gate and pending inbox entries. | `test_cancel_deletes_gate_and_pending_inbox_entries` | mcp/tests/test_controlplane_gates_tool_2.py:17-38 |
| Wait times out while open. | `test_wait_times_out_while_open` | mcp/tests/test_controlplane_gates_tool_2.py:40-52 |
| Response wait returns matching inbox entry without consuming. | `test_response_wait_returns_matching_inbox_entry_without_consuming` | mcp/tests/test_controlplane_gates_tool_2.py:54-79 |
| Decide for lifecycle rejects stale expected gate. | `test_decide_for_lifecycle_rejects_stale_expected_gate` | mcp/tests/test_controlplane_gates_tool_2.py:81-96 |

## Cross-Repo References

No cross-repository implementation evidence is required for these local test and fixture claims.

| Finding | Anchor | Source |
| --- | --- | --- |
| Fixture repositories and protocol doubles do not establish a live external integration. | N/A | N/A |

## Update History

- 2026-09-06T21:38+00:00 — Reconciled the actual retained source after IAS test simplification at d3610903: corrected fixture/test roles, removed obsolete current-coverage claims and refreshed existing-source citations. Earlier entries remain historical; verification stamps remain closeout-owned.


- 2026-08-07T22:45:00+02:00 — 260731-EFA-L7 curator: created this file-level onboarding card for the split module; content derived from the current worktree source. Verification metadata pinned until closeout stamps the 260731-EFA-L7 commit.
