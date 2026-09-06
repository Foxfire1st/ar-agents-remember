# mcp/tests/test_harness_submission_authority.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/test_harness_submission_authority.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-06T21:46+00:00 |
| lastVerifiedCommitHash | `25841d0ddc2d93c4950abf097168fa24b220c5ad` |
| lastVerifiedCommitDate | 2026-08-18T11:30:22+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[Test suite overview](overview.md)

## Purpose

Bridge-owned submission ordering, withdrawal and idempotency races.

## Code Commentary

### Logic

A slow operation leaves status and queued withdrawal responsive. Dispatch claim and withdrawal have an explicit winner; withdrawal during preflight prevents a native write. Early completion is buffered until the exact head can release. Same IDs replay but changed source/payload conflict. Certified pre-send busy requeues locally; epoch/source scope refuse and a pinned full ledger declines new room.

### Conventions

This card describes the retained source at IAS `d3610903`. Historical entries below record earlier test populations; they do not require restoring removed cases. Source inspection is memory preparation and does not claim a test run or acceptance.

### Invariants And Boundaries

No vendor queue or resend substitutes for bridge authority. Capacity refusal preserves records that cannot safely be dropped.

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
| Slow active operation does not block status or queued withdrawal. | `test_slow_active_operation_does_not_block_status_or_queued_withdrawal` | mcp/tests/test_harness_submission_authority.py:231-262 |
| Dispatch claim wins atomic withdrawal race. | `test_dispatch_claim_wins_atomic_withdrawal_race` | mcp/tests/test_harness_submission_authority.py:264-278 |
| Withdrawal during preflight wins before dispatch claim. | `test_withdrawal_during_preflight_wins_before_dispatch_claim` | mcp/tests/test_harness_submission_authority.py:280-306 |
| Completion before receipt is buffered and releases exact head. | `test_completion_before_receipt_is_buffered_and_releases_exact_head` | mcp/tests/test_harness_submission_authority.py:308-336 |
| Same id is idempotent but source or payload change conflicts. | `test_same_id_is_idempotent_but_source_or_payload_change_conflicts` | mcp/tests/test_harness_submission_authority.py:338-353 |
| Certified pre send busy requeues without vendor queue or resend. | `test_certified_pre_send_busy_requeues_without_vendor_queue_or_resend` | mcp/tests/test_harness_submission_authority.py:355-369 |
| Epoch and public source scope fail closed. | `test_epoch_and_public_source_scope_fail_closed` | mcp/tests/test_harness_submission_authority.py:371-397 |
| A ledger with nothing droppable refuses room rather than forgetting a row. | `test_a_ledger_with_nothing_droppable_refuses_room_rather_than_forgetting_a_row` | mcp/tests/test_harness_submission_authority.py:432-449 |

## Cross-Repo References

No cross-repository implementation evidence is required for these local test and fixture claims.

| Finding | Anchor | Source |
| --- | --- | --- |
| Fixture repositories and protocol doubles do not establish a live external integration. | N/A | N/A |

## Update History

- 2026-09-06T21:46+00:00 — Reconciled the actual retained source after IAS test simplification at d3610903: corrected fixture/test roles, removed obsolete current-coverage claims and refreshed existing-source citations. Earlier entries remain historical; verification stamps remain closeout-owned.


- 2026-08-18T09:10+02:00 — No content impact: renamed the atomic 'barrier' concept to 'blocker' throughout; behavior unchanged. Verification remains closeout-owned.

- 2026-08-08T17:18+02:00 — No content impact: 260731-EFA-L9 rewrote this source's imports/callers only (model-extraction caller wave); the behavior this card documents is unchanged and the body was re-verified current. Verification metadata pinned until closeout stamps the L9 code commit.

- 2026-08-04T18:16+02:00 — 260731-EFA-L6 S18-B16 curator: repaired 3 citation rows: the concurrency/race tests at test_harness_submission_authority.py L230-L350, the early-completion/invalid-ref tests at L351-L687, and the authority class under test at harness_submission_authority.py L116-L150. Scoped fixer + non-fixing recheck green under the frozen snapshot; verification metadata unchanged.

- 2026-07-31T16:50+02:00 — 260731-EFA-L2 curator: corrected both self-file line ranges in
  Repo-Internal References and recorded the fixture's new shape. The leaf rewired the `_authority`
  helper to construct `HarnessSubmissionAuthority` from a `BridgeSnapshotPort` and a
  `SubmissionLimits` parameter object instead of six loose keywords, and collapsed five wrapped
  `authority.withdraw`/`authority.status` calls onto single lines; together those shifted this
  file's contents by up to six lines in either direction. Verified against the current source,
  the slow-adapter and dispatch/withdraw race block now spans L222-L339 (was cited L214-L292) and
  the early-completion through invalid-operation-reference block spans L341-L674 (was cited
  L293-L636). No test method was added, removed or renamed and no assertion changed, so the
  Purpose, Logic and all four invariants stand as written.
- 2026-07-24T13:18:47Z — 260718-CHATS-L5I curator: refreshed the regression-coverage record for the current backend/shared behavior and preserved the pre-commit verification stamp.

- 2026-07-17T21:39+02:00 — Created for 260715-FEUI-L5; captured authoritative pop-back races,
  completion-before-receipt, exact-ref id reuse, ordering, idempotency/conflict, retry safety,
  retention, epoch, and privacy proofs. Verification metadata remains pinned to the leaf base.
