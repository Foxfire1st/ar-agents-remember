# mcp/tests/test_conversation_control_attachments.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/test_conversation_control_attachments.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-06T21:38+00:00 |
| lastVerifiedCommitHash | a06d2ffcfae2c277f2ae19330c17d09c616b77e8 |
| lastVerifiedCommitDate | 2026-08-28T13:58:55+02:00 |
| governingOverview | `overview.md` |

## Governing Overview

[Test suite overview](overview.md)

## Purpose

Attachment limits, one-use identity, recovery and unknown-outcome retention.

## Code Commentary

### Logic

Actual control composition rejects invalid MIME/count/bytes/kind, binds the receipt to one submitted request, and rejects tampering before dispatch. Exact replay writes once; changed content conflicts. Withdrawal returns a recoverable asset whose rebind is idempotent for one new request and cannot be exchanged twice; native resubmission carries the rebound identity.

### Conventions

This card describes the retained source at IAS `d3610903`. Historical entries below record earlier test populations; they do not require restoring removed cases. Source inspection is memory preparation and does not claim a test run or acceptance.

### Invariants And Boundaries

Unknown outcomes preserve spool bytes and remain unknown after reconcile. The reduced source does not retain cleanup-on-expiry or policy/telemetry matrices.

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
| Mime count byte and kind limits are typed. | `test_mime_count_byte_and_kind_limits_are_typed` | mcp/tests/test_conversation_control_attachments.py:100-125 |
| Submit carries refs and consumes one use. | `test_submit_carries_refs_and_consumes_one_use` | mcp/tests/test_conversation_control_attachments.py:156-179 |
| Tampered asset block is rejected before dispatch. | `test_tampered_asset_block_is_rejected_before_dispatch` | mcp/tests/test_conversation_control_attachments.py:181-189 |
| Double use of one asset is typed. | `test_double_use_of_one_asset_is_typed` | mcp/tests/test_conversation_control_attachments.py:191-203 |
| Withdraw marks recoverable and rebind exchanges one use. | `test_withdraw_marks_recoverable_and_rebind_exchanges_one_use` | mcp/tests/test_conversation_control_attachments.py:269-348 |
| Unknown outcome is retained and never cleaned. | `test_unknown_outcome_is_retained_and_never_cleaned` | mcp/tests/test_conversation_control_attachments.py:394-426 |

## Cross-Repo References

No cross-repository implementation evidence is required for these local test and fixture claims.

| Finding | Anchor | Source |
| --- | --- | --- |
| Fixture repositories and protocol doubles do not establish a live external integration. | N/A | N/A |

## Update History

- 2026-09-06T21:38+00:00 — Reconciled the actual retained source after IAS test simplification at d3610903: corrected fixture/test roles, removed obsolete current-coverage claims and refreshed existing-source citations. Earlier entries remain historical; verification stamps remain closeout-owned.


- 2026-08-08T17:18+02:00 — 260731-EFA-L9 curator: body verified against the current worktree after the model-extraction/caller-rewrite wave; stale moved-path references repaired and the L9 change recorded. Verification metadata pinned until closeout stamps the L9 code commit.

- 2026-08-04T12:41:53+00:00 — 260731-EFA-L6 S18-B09 curator: narrowed the attachment claim to the focused test's digest-only mutation; the landing provenance mismatch remains an explicit Tier-3 item.
- 2026-07-31T17:20+02:00 — 260731-EFA-L2 curator: repaired the lifecycle citation after the
  `ControlRequest` expansion and formatter reflow; the current attachment reference row binds the
  dataclass and its entry points by generated ranges.
- 2026-07-31T16:50+02:00 — 260731-EFA-L2: `attachments.stage(...)` now takes a single
  `ControlRequest(service=…, authorization=…, ar_session_id=…, expected_bridge_epoch=…)` where it
  took four leading arguments, and that expansion — together with the leaf's `ruff format` reflow of
  the long `StagedUpload` and `submit` call sites — pushed every class anchor in this card down.
  Re-anchored all five (`AttachmentStageTests` L69 → L72, `AttachmentSubmitTests` L145 → L158,
  `AttachmentRebindTests` L214 → L236, `AttachmentReconcileTransitionTests` L363 → L405,
  `PolicyTelemetryTests` L512 → L572) and recorded the request object in Conventions. No test, no
  boundary limit and no on-disk deletion assertion changed.
- 2026-07-20T15:45+02:00 — 260718-CHATS-L3 curator: created the sidecar for the attachment/policy/
  telemetry suite — bound stage with boundary-exact limit refusals, one-use exact-receipt submit,
  recoverable-under-lease rebind with on-disk deletion proofs, timeline-driven reconcile, GET-only
  policy, and absent-not-zero telemetry. Verification is blank because the new source file is
  uncommitted; closeout owns its first source stamp.
