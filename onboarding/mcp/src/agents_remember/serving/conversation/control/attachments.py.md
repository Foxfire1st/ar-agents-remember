# mcp/src/agents_remember/serving/conversation/control/attachments.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/serving/conversation/control/attachments.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-07-20T15:45+02:00 |
| lastVerifiedCommitHash |  `f3115ce8603f83b7b5cbd82aa402f66ec1d8a29d`|
| lastVerifiedCommitDate |  2026-07-31T19:28:50+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[Structured conversation control overview](overview.md)

## Purpose

R4: the typed attachment stage/status/reconcile/rebind/submit lifecycle. Stage binds each asset to
the caller, the exact `arSessionId + bridgeEpoch`, the caller-minted request id, and the attachment
kind, with fixture-backed MIME/count/byte limits; submit consumes one-use staged assets through the
L2E asset channel (refs on the wire, digest-verified bytes in the user-private spool); status and
reconcile advance the semantic lifecycle from the authority's retained timeline; withdrawal marks
assets recoverable under the same lease as text recovery; rebind atomically exchanges an authorized
recovery asset for a new one-use staged asset. Accessible alt text with provenance survives every
transition.

## Code Commentary

### Logic

`AttachmentOperation` (L102), `SubmitAnswer` (L118-L126), and `StageAnswer` (L129-L132) are the
ledger/answer types. `stage` (L135-L201) enforces the 1..4 asset count itself (L150-L151) and admits
each upload through `asset_spool.stage_one` (L185) — the kind-capability gate, then per-asset MIME
allow-list / byte-limit / description validation, digest compute, and the confined 0600 spool write;
the allow-list and the byte limit ride the kind capability and are never re-declared here. Identical
content replays idempotently, changed content under the same request id is `request-conflict`
(L166-L176). `submit` (L204-L270)
composes the one-use blocks (`_compose` L484, `_consume_block` L503, `_require_receipt_match` L534 —
exact receipt match refuses tampered blocks pre-dispatch), dispatches through the L2E asset channel,
maps the receipt's acceptance onto the operation's phase/outcome and builds the `SubmitAnswer`
(`_admit` L564-L591, called from `submit` at L253), and stores the answer
(`_store_submit_artifacts` L316); an identical submit replay returns the stored
answer with zero re-dispatch (`_replay_prior_submit` L283, `_staged_submit_conflict` L273).
`attachment_status` (L345) and `_advance_from_timeline` (L620) + `_timeline_transition` (L647, whose
live-state test reads `_LIVE_TIMELINE_STATES` L97 at L652) move
the lifecycle only from the retained timeline — `unknown` is retained (never re-uploaded), advancing
only into `accepted` (bytes deleted) or `failed`, never guessed. `rebind` (L375-L433) exchanges one
authorized recovery asset for a fresh one-use staged asset under a new request id (`_rebind_target`
L664, `_rebind_replay` L420 idempotent same-request; a different request conflicts). `mark_recoverable`
(L444) / `delete_recoverable` (L484) tie into the withdrawal lease; `_sweep_expired` (L710) deletes
staged bytes on the 900 s TTL; `_evict_attachment_operation` (L721) and `_delete_operation_bytes`
(L736) enforce the 32/channel bound with byte disposal. `_receipt` (L744-L762) and `_projection` (L765)
build the wire payloads with alt provenance.

### Conventions

Staging is bounded ephemeral transport, never conversation persistence. Alt text with its provenance
(supplied description, or a truthful `name`+`mime` fallback) is carried as data through staging,
submit, withdrawal recovery, and rebind — the renderer's accessibility obligation lands in L4. The
filesystem mechanics live in `asset_spool.py`; this module owns lifecycle policy.

### Invariants And Boundaries

- Each asset rides exactly one request; a tampered block (changed digest/name/alt) refuses before any
  native write; a second use of one asset is typed.
- MIME/count/byte limits are boundary-enforced (MIME refusal, 4+1 count refusal, 5 MiB+1 refusal,
  unsupported kind → 422) from the L2E constants, never re-declared.
- `unknown` submit acceptance keeps the operation `unknown` (no cleanup while unknown); reconcile only
  advances from the retained timeline.
- Recoverable/staged bytes die on ack-keep, lease expiry, or the staged TTL — never left on disk.
- Idempotent submit replay returns the stored answer with zero re-dispatch.

### Todos

None.

## Docs References

No Domain Documentation source is configured; the attachment contract is repository-owned.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No configured domain documentation was available. | — | — |

## Repo-Internal References

The filesystem boundary and asset limits are the sibling spool and the L2E substrate; the timeline is
the authority; the withdrawal lease ties recoverable assets to the text recovery.

| Finding | Citations | Source Path |
| --- | --- | --- |
| The staged-bytes filesystem boundary and staged asset types. | L34-L215 | [asset_spool.py](agents-remember/mcp/src/agents_remember/serving/conversation/control/asset_spool.py) |
| The L2E asset channel (refs on the wire, digest verify at admission/construction) and MIME/count/byte constants. | L1-L120 | [harness_control_models.py](agents-remember/mcp/src/agents_remember/serving/harness_control_models.py) |
| The retained operation timeline this lifecycle advances from. | L236-L266 | [service.py](agents-remember/mcp/src/agents_remember/serving/conversation/control/service.py) |
| Recoverable assets ride the same 900 s lease as the text recovery. | L442-L467 | [withdrawals.py](agents-remember/mcp/src/agents_remember/serving/conversation/control/withdrawals.py) |

## Cross-Repo References

No meaningful cross-repo references found.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No meaningful cross-repo references found. | — | — |

## 260731-EFA-L2 Current Delta

Two named concepts now cross this module's boundaries:

- **`ControlRequest`** (from `service.py`) replaces the `service` / `authorization` /
  `ar_session_id` / `expected_bridge_epoch` quartet at the submit entry point — one authorized
  control request's scope.
- **`SubmittedContent`** (`body`, `receipt`, `text`, `asset_records`) names what one cockpit submit
  actually sent and what the bridge said about it. The request body, the sanitized text the daemon
  holds for recovery, the assets bound to it and the receipt that came back describe a single
  submission; splitting them let a journal entry be written from one submission's text against
  another's receipt.

The bridge call is now `submit_control_prompt(…, ControlSubmission(source="cockpit",
request_id=…, expected_bridge_epoch=…, assets=…))`, and refs are minted with `RefBinding` /
`RefTarget`. Recovery, journaling and digest behaviour are unchanged.

This entry supersedes any earlier description in this sidecar that conflicts with the current source behavior above; verification metadata stays pinned to the pre-commit source history until closeout.

## Update History

- 2026-07-31T17:48+02:00 — 260731-EFA-L2 curator: repaired 7 stale self-citations and corrected one
  false wiring claim. **The claim `stage` "admits uploads through `_admit`" was wrong**: `_admit`
  (L564-L591) is `submit`'s receipt mapper — it turns the bridge receipt's acceptance into the
  operation phase/outcome and the `SubmitAnswer`, and its only caller is `submit` (L253). `stage`
  (L135-L201) checks the 1..4 count inline (L150-L151) and delegates per-asset gating, MIME/byte
  validation, digest and the confined spool write to `asset_spool.stage_one` (L185). The
  `_LIVE_TIMELINE_STATES` reference moved with it: that constant (L97, correct) is read by
  `_timeline_transition` at L652 and has nothing to do with upload validation. Re-derived ranges:
  `SubmitAnswer` L118-L126, `StageAnswer` L129-L132, `submit` L204-L270, `rebind` L375-L433,
  `_receipt` L744-L762. Still stale and left for the next citation pass (verified, not repaired
  here): `_compose` is L500 (cited L484), `_consume_block` L519 (cited L503), `_rebind_replay` L436
  (cited L420), `mark_recoverable` L460 (cited L444), `_rebind_target` L667 (cited L664).
- 2026-07-31T17:20+02:00 — 260731-EFA-L2 curator: repaired 1 cross-file line citation. The shared 900 s
  lease is minted in `withdrawals._build_withdrawn_record`, now L442-L467: `expires_at` comes from
  `iso_seconds_after(withdrawn_at, RECOVERY_TTL_SECONDS)` (L458, `RECOVERY_TTL_SECONDS = 900` in
  `control/service.py` L74) and that same `expires_at` is passed straight into
  `recovery_assembly.recover_attachment_refs` (L465-L467). Was L444-L484, which now lands in the
  unrelated `WithdrawalRecord` field block.
- 2026-07-31T16:10+02:00 — 260731-EFA-L2 curator: recorded `SubmittedContent`, the `ControlRequest` entry shape, and the `ControlSubmission` / `RefBinding` / `RefTarget` call shapes.
- 2026-07-20T15:45+02:00 — 260718-CHATS-L3 curator: created the sidecar for the typed attachment
  lifecycle — bound stage with fixture-backed limits, one-use exact-receipt submit through the L2E
  asset channel, timeline-driven status/reconcile, recoverable-under-lease rebind, and alt
  provenance carried across every transition. Verification is blank because the new source file is
  uncommitted; closeout owns its first source stamp.
