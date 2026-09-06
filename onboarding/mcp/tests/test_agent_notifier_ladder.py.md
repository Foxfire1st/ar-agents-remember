# mcp/tests/test_agent_notifier_ladder.py

| Field                  | Value                                            |
| ---------------------- | ------------------------------------------------ |
| repository             | agents-remember                                  |
| path                   | `mcp/tests/test_agent_notifier_ladder.py`                                            |
| doc_type               | `file-level-onboarding`                          |
| lastUpdated | 2026-09-06T21:38+00:00 |
| lastVerifiedCommitHash | `d36109038b3f2b500c138f9dc1ea9c9f9a247489`                                        |
| lastVerifiedCommitDate | 2026-09-06T22:21:49+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[Test suite overview](overview.md)

## Purpose

Task-topology builders shared by notifier consumers.

## Code Commentary

### Logic

_write_topology writes a sprint, one master and sixty real leaf documents beneath the supplied temporary root. _task_doc validates model inputs and _leaf_ref returns exact document references. No ladder-walk tests remain in this file.

### Conventions

This card describes the retained source at IAS `d3610903`. Historical entries below record earlier test populations; they do not require restoring removed cases. Source inspection is memory preparation and does not claim a test run or acceptance.

### Invariants And Boundaries

The historical ladder filename does not establish escalation behavior or authorize restoring retired ladder tests.

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
| Task doc. | `_task_doc` | mcp/tests/test_agent_notifier_ladder.py:14-25 |
| Write topology. | `_write_topology` | mcp/tests/test_agent_notifier_ladder.py:28-71 |
| Leaf ref. | `_leaf_ref` | mcp/tests/test_agent_notifier_ladder.py:74-75 |

## Cross-Repo References

No cross-repository implementation evidence is required for these local test and fixture claims.

| Finding | Anchor | Source |
| --- | --- | --- |
| Fixture repositories and protocol doubles do not establish a live external integration. | N/A | N/A |

## Update History

- 2026-09-06T21:38+00:00 — Reconciled the actual retained source after IAS test simplification at d3610903: corrected fixture/test roles, removed obsolete current-coverage claims and refreshed existing-source citations. Earlier entries remain historical; verification stamps remain closeout-owned.


- 2026-08-11T19:58+02:00 — Reconciled `test_agent_notifier_ladder.py` with its current structural task/seat, tool-vocabulary, or quality-boundary regression contract and removed stale exact-id/leaf implications where present.
- 2026-08-10T13:00+02:00 — 260731-EFA-L9 curator: No content impact: re-read the current staged ladder-demolition and agent-notifier assertions; the existing test card remains accurate. Verification metadata remains pinned until closeout.
- 2026-08-09T12:08+02:00 — 260713-TES-L5 curator: recorded the escalation-predicate
  demolition, the grace-path fixed-point conversion, and the new `escalationBudget`
  load-shed/expectation-compaction scaling tests. Verification metadata pinned until
  closeout stamps the 260713-TES-L5 commit.
- 2026-08-09T06:48+02:00 — 260713-TES-L4 curator: recorded the ladder-retirement conversions
  (attempt-ceiling `unresolved`, landed-never-retried, relay-restart reconcile-by-request_id,
  dispatch exact-pinning, rebind/grace-expiry to the architect mailbox) and the
  `Cs6SweepScalingTests` verdict-by fixture + one-per-row-per-sweep expiry emission test.
  Verification metadata pinned until closeout stamps the 260713-TES-L4 commit.
- 2026-08-09T01:21+02:00 — 260713-TES-L2 curator: recorded the `Cs6SweepScalingTests` fixture
  kind swap from `briefed-by` to `ack-by` (the scaling fixture now exercises an expectation kind
  that still drives findings). Verification metadata pinned until closeout stamps the
  260713-TES-L2 commit.
- 2026-08-08T22:10+02:00 — 260713-TES-L1 completion round (curator): refreshed this sidecar body for the supervisor -> agent-notifier rename (module paths, identifiers, settings keys, wire keys, prose) and the compat seams; verification metadata pinned until closeout stamps the 260713-TES-L1 commit.
- 2026-08-07T22:45:00+02:00 — 260731-EFA-L7 curator: created this file-level onboarding card for the split module; content derived from the current worktree source. Verification metadata pinned until closeout stamps the 260731-EFA-L7 commit.
