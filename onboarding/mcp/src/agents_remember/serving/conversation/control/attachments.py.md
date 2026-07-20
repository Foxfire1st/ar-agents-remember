# mcp/src/agents_remember/serving/conversation/control/attachments.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/serving/conversation/control/attachments.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-07-20T15:45+02:00 |
| lastVerifiedCommitHash |  `0be0099744bf1287805acf0b95072127b70f7104`|
| lastVerifiedCommitDate |  2026-07-20T15:34:11+02:00|
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

`AttachmentOperation` (L95), `SubmitAnswer` (L112), and `StageAnswer` (L123) are the ledger/answer
types. `stage` (L128) admits uploads through `_admit` (L548) — per-asset MIME/count/byte validation
(`_LIVE_TIMELINE_STATES` L90; the 4-count, 5 MiB byte, and MIME allow-list come from the L2E asset
constants), digest compute, and confined spool write via `asset_spool`; identical content replays
idempotently, changed content under the same request id is `request-conflict`. `submit` (L195)
composes the one-use blocks (`_compose` L484, `_consume_block` L503, `_require_receipt_match` L518 —
exact receipt match refuses tampered blocks pre-dispatch), dispatches through the L2E asset channel,
and stores the answer (`_store_submit_artifacts` L303); an identical submit replay returns the stored
answer with zero re-dispatch (`_replay_prior_submit` L285, `_staged_submit_conflict` L275).
`attachment_status` (L335) and `_advance_from_timeline` (L611) + `_timeline_transition` (L638) move
the lifecycle only from the retained timeline — `unknown` is retained (never re-uploaded), advancing
only into `accepted` (bytes deleted) or `failed`, never guessed. `rebind` (L363) exchanges one
authorized recovery asset for a fresh one-use staged asset under a new request id (`_rebind_target`
L664, `_rebind_replay` L420 idempotent same-request; a different request conflicts). `mark_recoverable`
(L444) / `delete_recoverable` (L468) tie into the withdrawal lease; `_sweep_expired` (L708) deletes
staged bytes on the 900 s TTL; `_evict_attachment_operation` (L719) and `_delete_operation_bytes`
(L734) enforce the 32/channel bound with byte disposal. `_receipt` (L747) and `_projection` (L768)
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
| Recoverable assets ride the same 900 s lease as the text recovery. | L444-L484 | [withdrawals.py](agents-remember/mcp/src/agents_remember/serving/conversation/control/withdrawals.py) |

## Cross-Repo References

No meaningful cross-repo references found.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No meaningful cross-repo references found. | — | — |

## Update History

- 2026-07-20T15:45+02:00 — 260718-CHATS-L3 curator: created the sidecar for the typed attachment
  lifecycle — bound stage with fixture-backed limits, one-use exact-receipt submit through the L2E
  asset channel, timeline-driven status/reconcile, recoverable-under-lease rebind, and alt
  provenance carried across every transition. Verification is blank because the new source file is
  uncommitted; closeout owns its first source stamp.
