# mcp/src/agents_remember/serving/conversation/control/attachments.py

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

cit:([`AttachmentOperation`], mcp/src/agents_remember/serving/conversation/control/attachments.py:101-115), cit:([`SubmitAnswer`], mcp/src/agents_remember/serving/conversation/control/attachments.py:127-135), and cit:([`StageAnswer`], mcp/src/agents_remember/serving/conversation/control/attachments.py:138-141) are the
ledger/answer types. cit:([`stage`], mcp/src/agents_remember/serving/conversation/control/attachments.py:135-201) enforces the 1..4 asset count itself (cit:(["attachment staging requires 1..4 assets per request"], mcp/src/agents_remember/serving/conversation/control/attachments.py:160-160)) and admits
each upload through cit:([`stage_one`], mcp/src/agents_remember/serving/conversation/control/asset_spool.py:68-85) — the kind-capability gate, then per-asset MIME
allow-list / byte-limit / description validation, digest compute, and the confined 0600 spool write;
the allow-list and the byte limit ride the kind capability and are never re-declared here. Identical
content replays idempotently, changed content under the same request id is `request-conflict`
(cit:(["class OperationConflictError"], mcp/src/agents_remember/serving/conversation/control/service.py:116-120)). cit:([`submit`], mcp/src/agents_remember/serving/conversation/control/attachments.py:204-270)
composes the one-use blocks (cit:([`_compose`], mcp/src/agents_remember/serving/conversation/control/attachments.py:500-516), cit:([`_consume_block`], mcp/src/agents_remember/serving/conversation/control/attachments.py:519-531), `_require_receipt_match` L534 —
exact receipt match refuses tampered blocks pre-dispatch), dispatches through the L2E asset channel,
maps the receipt's acceptance onto the operation's phase/outcome and builds the `SubmitAnswer`
(`_admit` L564-L591, called from `submit` at L253), and stores the answer
cit:([`_store_submit_artifacts`], mcp/src/agents_remember/serving/conversation/control/attachments.py:316-342); an identical submit replay returns the stored
answer with zero re-dispatch (`_replay_prior_submit` L283, `_staged_submit_conflict` L273).
cit:([`attachment_status`], mcp/src/agents_remember/serving/conversation/control/attachments.py:345-372) and cit:([`_advance_from_timeline`], mcp/src/agents_remember/serving/conversation/control/attachments.py:620-644) + `_timeline_transition` (L647, whose
live-state test reads `_LIVE_TIMELINE_STATES` L97 at L652) move
the lifecycle only from the retained timeline — `unknown` is retained (never re-uploaded), advancing
only into `accepted` (bytes deleted) or `failed`, never guessed. cit:([`rebind`], mcp/src/agents_remember/serving/conversation/control/attachments.py:375-433) exchanges one
authorized recovery asset for a fresh one-use staged asset under a new request id (cit:([`_rebind_target`], mcp/src/agents_remember/serving/conversation/control/attachments.py:667-707), cit:([`_rebind_replay`], mcp/src/agents_remember/serving/conversation/control/attachments.py:436-457) idempotent same-request; a different request conflicts). cit:([`mark_recoverable`], mcp/src/agents_remember/serving/conversation/control/attachments.py:460-481) / cit:([`delete_recoverable`], mcp/src/agents_remember/serving/conversation/control/attachments.py:484-497) tie into the withdrawal lease; cit:([`_sweep_expired`], mcp/src/agents_remember/serving/conversation/control/attachments.py:719-727) deletes
staged bytes on the 900 s TTL; cit:([`_evict_attachment_operation`], mcp/src/agents_remember/serving/conversation/control/attachments.py:721-733) and cit:([`_delete_operation_bytes`], mcp/src/agents_remember/serving/conversation/control/attachments.py:745-750) enforce the 32/channel bound with byte disposal. cit:([`_receipt`], mcp/src/agents_remember/serving/conversation/control/attachments.py:744-762) and cit:([`_projection`], mcp/src/agents_remember/serving/conversation/control/attachments.py:765-775)
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

## Evidence

### Docs References

No Domain Documentation source is configured; the attachment contract is repository-owned.

No configured domain documentation was available.

### Repo-Internal References

The filesystem boundary and asset limits are the sibling spool and the L2E substrate; the timeline is
the authority; the withdrawal lease ties recoverable assets to the text recovery.

- The staged-bytes filesystem boundary and staged asset types. [1]
- The L2E asset channel (refs on the wire, digest verify at admission/construction) and MIME/count/byte constants. [2]
- The retained operation timeline this lifecycle advances from. [3]
- Recoverable assets ride the same 900 s lease as the text recovery. [4]

### Cross-Repo References

No meaningful cross-repo references found.

No meaningful cross-repo references found.

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
