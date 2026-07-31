# mcp/tests/test_conversation_control_attachments.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/test_conversation_control_attachments.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-07-20T15:45+02:00 |
| lastVerifiedCommitHash |  `f3115ce8603f83b7b5cbd82aa402f66ec1d8a29d`|
| lastVerifiedCommitDate |  2026-07-31T19:28:50+02:00|
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

`AttachmentStageTests` (L72): caller/session/epoch/request/kind binding; the fixture-backed MIME
allow-list, 4-count, and 5 MiB+1 boundary refusals; unsupported kind → 422; idempotent stage under
identical content; changed content + same request id → `request-conflict`; server-computed sha256 and
alt provenance. `AttachmentSubmitTests` (L158): one-use consumption through the L2E asset channel;
tampered block (changed digest/name/alt) refuses pre-dispatch; a second use of one asset is typed;
identical submit replay returns the stored answer with zero re-dispatch. `AttachmentRebindTests`
(L236): withdrawal → recoverable under the same lease; atomic exchange of one authorized recovery
asset for a new one-use staged asset (same-request replay idempotent, different request conflicts,
consumed asset conflicts); `keep-current-draft` deletes recoverable bytes on disk.
`AttachmentReconcileTransitionTests` (L405): unknown retained, advancing only into accepted (bytes
deleted) or failed from the retained timeline; staged expiry deletes bytes on the TTL.
`PolicyTelemetryTests` (L572): read-only policy (repoPolicy vs harnessMode, GET-only) and
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

| Finding | Citations | Source Path |
| --- | --- | --- |
| No configured domain documentation was available. | — | — |

## Repo-Internal References

The suite exercises the attachment lifecycle, spool, policy, and telemetry modules over the shared
topology.

| Finding | Citations | Source Path |
| --- | --- | --- |
| The typed attachment lifecycle under test. | L101-L780 | [control/attachments.py](agents-remember/mcp/src/agents_remember/serving/conversation/control/attachments.py) |
| The spool boundary whose on-disk deletion the rebind/expiry tests assert. | L34-L215 | [control/asset_spool.py](agents-remember/mcp/src/agents_remember/serving/conversation/control/asset_spool.py) |
| The read-only policy and evidence-bound telemetry projections. | L57-L147 | [control/telemetry.py](agents-remember/mcp/src/agents_remember/serving/conversation/control/telemetry.py) |
| The shared fake-topology harness with the L2E asset channel + spool. | L406-L518 | [_control_plane.py](agents-remember/mcp/tests/_control_plane.py) |

## Cross-Repo References

No meaningful cross-repo references found.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No meaningful cross-repo references found. | — | — |

## Update History

- 2026-07-31T17:20+02:00 — 260731-EFA-L2 curator: repaired 1 cross-file line citation into
  `control/attachments.py` (795 lines). The same `ControlRequest` expansion and `ruff format` reflow
  recorded below moved the module's own anchors, so the lifecycle row now cites L101-L780 rather
  than `L128-L781`: it opens on the `AttachmentOperation` dataclass at L101 instead of landing
  mid-DTO-block, and closes on `_as_operation` at L780 instead of inside the `__all__` list
  (L783-L795). Read both ends and confirmed the range still spans every entry point the suite
  drives — `stage` L135, `submit` L204, `attachment_status` L345, `rebind` L375, `mark_recoverable`
  L460, `delete_recoverable` L484.
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
