# mcp/tests/test_cross_store_lock_order.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/test_cross_store_lock_order.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-06T21:46+00:00 |
| lastVerifiedCommitHash | `97e8ed2e1fae21756c3ad995c30613d4fbfcc503` |
| lastVerifiedCommitDate | 2026-09-06T02:09:33+02:00 |
| governingOverview | `overview.md` |

## Governing Overview

[Test suite overview](overview.md)

## Purpose

Cross-store sweep concurrency and event-loop responsiveness.

## Code Commentary

### Logic

Two actual sweep paths share a catalog and inbox under a controlled rendezvous and must both finish without failures or lost observation. Separate async cases verify control entry resolution and terminal-image catalog/write work run on worker threads.

### Conventions

This card describes the retained source at IAS `d3610903`. Historical entries below record earlier test populations; they do not require restoring removed cases. Source inspection is memory preparation and does not claim a test run or acceptance.

### Invariants And Boundaries

The motivating ABBA incident involved catalog-to-inbox versus inbox-to-catalog nesting. Daemon-thread watchdogs bound the failure; no fake immediate-success lock substitutes for the shared-store race.

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
| Liveness sweep and agent notifier sweep do not abba deadlock. | `test_liveness_sweep_and_agent_notifier_sweep_do_not_abba_deadlock` | mcp/tests/test_cross_store_lock_order.py:202-287 |
| Control resolve entry runs off the event loop. | `test_control_resolve_entry_runs_off_the_event_loop` | mcp/tests/test_cross_store_lock_order.py:289-310 |
| Terminal image response offloads catalog read and write. | `test_terminal_image_response_offloads_catalog_read_and_write` | mcp/tests/test_cross_store_lock_order.py:312-347 |

## Cross-Repo References

No cross-repository implementation evidence is required for these local test and fixture claims.

| Finding | Anchor | Source |
| --- | --- | --- |
| Fixture repositories and protocol doubles do not establish a live external integration. | N/A | N/A |

## Update History

- 2026-09-06T21:46+00:00 — Reconciled the actual retained source after IAS test simplification at d3610903: corrected fixture/test roles, removed obsolete current-coverage claims and refreshed existing-source citations. Earlier entries remain historical; verification stamps remain closeout-owned.


- 2026-09-06T00:23:26+00:00 — L30 recovery: Reverified retained source or route ownership against actual candidate commit 97e8ed2e1fae21756c3ad995c30613d4fbfcc503; replaced the superseded private-candidate stamp.

- 2026-09-06T00:28+02:00 — Moved lock-placement documentation and references to the real kernel mutex patched by both full-sweep and starting-path tests; retained the non-vacuous ABBA and event-loop placement guarantees.


- 2026-08-08T17:18+02:00 — 260731-EFA-L9 curator: body verified against the current worktree after the model-extraction/caller-rewrite wave; stale moved-path references repaired and the L9 change recorded. Verification metadata pinned until closeout stamps the L9 code commit.

- 2026-08-07T22:45:00+02:00 — 260731-EFA-L7 curator: this test module was split in place into a family under 1,200 lines (L7-R5); the card remains the family entry point and the name set was reconciled item for item. Verification metadata stays pinned until closeout stamps the 260731-EFA-L7 commit.

- 2026-08-05T20:20+02:00 — 260731-EFA-L16 curator: the quality wrapper's diff-coverage rail grew
  the file from five pins to the current set — the starting-fast-path placement pin with its
  early returns, and the legacy inline direct-observe pin — and the wrapper's ruff/type findings
  were repaired. Verification stays blank until closeout stamps the L16 commit.
- 2026-08-05T19:58+02:00 — 260731-EFA-L16 curator: created the sidecar for the cross-store
  lock-order forcing tests (synchronizer placement, rendezvous-parked ABBA reproduction on the
  real sweep paths, event-loop offload of control/active/image resolution). Verification is
  blank because the new source file is uncommitted; closeout owns its first source stamp.
