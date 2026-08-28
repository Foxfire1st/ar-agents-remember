# mcp/tests/test_conversation_control_attachments.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/test_conversation_control_attachments.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-08-28T07:20+02:00 |
| lastVerifiedCommitHash | a06d2ffcfae2c277f2ae19330c17d09c616b77e8 |
| lastVerifiedCommitDate | 2026-08-28T13:58:55+02:00 |
| governingOverview | `overview.md` |

## Governing Overview

[mcp/tests overview](overview.md)

## Purpose

Attachment lifecycle, policy, and telemetry contract tests (R4/R5/R6/R7) over the real composition up
to the harness edge (bridge + IPC + real authority + the L2E asset channel + the user-private spool),
with the structural fake adapter as the only double. Bytes are tiny; every limit is exercised at its
boundary.

## Code Commentary

### Logic

cit:([`AttachmentStageTests`], mcp/tests/test_conversation_control_attachments.py:72-155): caller/session/epoch/request/kind binding; the fixture-backed MIME
allow-list, 4-count, and 5 MiB+1 boundary refusals; unsupported kind → 422; idempotent stage under
identical content; changed content + same request id → `request-conflict`; server-computed sha256 and
alt provenance. cit:([`AttachmentSubmitTests`], mcp/tests/test_conversation_control_attachments.py:158-233): one-use consumption through the L2E asset channel;
  the focused tamper test mutates the digest only before asserting pre-dispatch refusal; a second use of one asset is typed;
  identical submit replay returns the stored answer with zero re-dispatch. cit:([`AttachmentRebindTests`], mcp/tests/test_conversation_control_attachments.py:236-402):
  withdrawal → recoverable under the same lease; atomic exchange of one authorized recovery
asset for a new one-use staged asset (same-request replay idempotent, different request conflicts,
consumed asset conflicts); `keep-current-draft` deletes recoverable bytes on disk.
cit:([`AttachmentReconcileTransitionTests`], mcp/tests/test_conversation_control_attachments.py:405-569): unknown retained, advancing only into accepted (bytes
deleted) or failed from the retained timeline; staged expiry deletes bytes on the TTL.
cit:([`PolicyTelemetryTests`], mcp/tests/test_conversation_control_attachments.py:572-650): read-only policy (repoPolicy vs harnessMode, GET-only) and
evidence-bound codex usage with absent-not-zero missing data.

### Conventions

Every limit is proven at its exact boundary; disk deletion is asserted on the real spool directory.
The service is `harness.service` (the `NOW`-anchored instance) so recoverable-asset lease arithmetic
is time-consistent. Every `attachments.stage(...)` call passes the caller context as one
`ControlRequest(service=…, authorization=…, ar_session_id=…, expected_bridge_epoch=…)`; `submit`
still takes those three positionally plus `body=`.

### Invariants And Boundaries

- MIME/count/byte limits refuse at the boundary; each asset rides exactly one request; tampered blocks
  refuse before any native write.
- `unknown` is retained (never re-uploaded); reconcile advances only from the retained timeline.
- Recoverable/staged bytes are deleted on ack-keep, lease expiry, or the staged TTL (proven on disk).
- Policy has no mutation surface (GET-only); missing telemetry data is absent, never zero.

### Todos

None.

## Docs References

No Domain Documentation source is configured; the attachment/policy/telemetry contracts are
repository-owned.

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured domain documentation was available. | — | — |

## Repo-Internal References

The suite exercises the attachment lifecycle, spool, policy, and telemetry modules over the shared
topology.

| Finding | Anchor | Source |
| --- | --- | --- |
| The typed attachment lifecycle under test. | `AttachmentOperation`; `stage`; `submit`; `attachment_status`; `rebind`; `mark_recoverable`; `delete_recoverable` | mcp/src/agents_remember/serving/conversation/control/attachments.py:101-115; mcp/src/agents_remember/serving/conversation/control/attachments.py:135-201; mcp/src/agents_remember/serving/conversation/control/attachments.py:204-270; mcp/src/agents_remember/serving/conversation/control/attachments.py:345-372; mcp/src/agents_remember/serving/conversation/control/attachments.py:375-433; mcp/src/agents_remember/serving/conversation/control/attachments.py:460-481; mcp/src/agents_remember/serving/conversation/control/attachments.py:484-497 |
| The asset-spool deletion primitive whose on-disk effect the rebind/expiry tests assert. | `delete_asset_bytes` | mcp/src/agents_remember/serving/conversation/control/asset_spool.py:161-168 |
| The read-only policy and evidence-bound telemetry projections. | `conversation_policy`; `_harness_mode`; `conversation_telemetry`; `_codex_usage` | mcp/src/agents_remember/serving/conversation/control/policy.py:58-101; mcp/src/agents_remember/serving/conversation/control/policy.py:104-130; mcp/src/agents_remember/serving/conversation/control/telemetry.py:41-73; mcp/src/agents_remember/serving/conversation/control/telemetry.py:76-121 |
| The shared fake-topology harness with the L2E asset channel + spool. | `FakeControlAdapter`; `ControlHarness`; `make_harness` | mcp/tests/_control_plane.py:100-289; mcp/tests/_control_plane.py:300-383; mcp/tests/_control_plane.py:386-397 |

## Cross-Repo References

No meaningful cross-repo references found.

| Finding | Anchor | Source |
| --- | --- | --- |
| No meaningful cross-repo references found. | — | — |

## Update History

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
