# mcp/src/agents_remember/serving/conversation/control/withdrawals.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/serving/conversation/control/withdrawals.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-07-20T15:45+02:00 |
| lastVerifiedCommitHash |  `f3115ce8603f83b7b5cbd82aa402f66ec1d8a29d`|
| lastVerifiedCommitDate |  2026-07-31T19:28:50+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[Structured conversation control overview](overview.md)

## Purpose

R3: authoritative `cockpit_only` withdrawal with bounded authorization-bound recovery. The authorized
withdrawalRef/operationRef pair is verified against the live queue row; the L2E substrate then
linearizes the queued-to-dispatching race with exactly one winner, the landed `cockpit_only`
atomicity untouched. A successful withdrawal retains the exact body (the substrate's pre-tombstone
recovery payload, cross-checked against this authority's submit journal) in a bounded, expiring
recovery record; fresh tabs discover only opaque pending-recovery identities, and the exact text and
asset-exchange refs cross only through an authenticated, unacknowledged fetch.

## Code Commentary

### Logic

`RecoveryRecord` (L90-L101) and `WithdrawalRecord` (L104-L118) are the bounded ledger rows.
`withdraw` (L121-L184) serializes on the per-session lock; `_verify_refs` (L757-L769) re-binds the
withdrawal+operation ref pair — it decodes BOTH refs under the one caller/session/epoch
`RefBinding` and refuses a pair that does not name the same operation identity — while the live
queue row is checked one step later: `_drive_withdrawal` (L358-L398) reads `_live_row` (L631-L648)
and settles a failure unless the row is a still-`queued` cockpit-source row, then drives the
substrate atomic withdraw and `_apply_withdrawal_result` (L401-L413) records the outcome —
`_build_withdrawn_record` (L442-L511) captures recovery via `recovery_assembly` and anchors the
900 s lease (`withdrawn_at = clock()`, expiry at `withdrawn_at + RECOVERY_TTL_SECONDS`, L457-L458),
while `_failure_for_result` (L416-L439) / `_settled_failure` (L514-L545) / `_unknown_withdrawal`
(L548-L574) type every other outcome.
`pending_recoveries` (L226) lists opaque identity/state/expiry only — no text, no preview.
`fetch_recovery` (L266-L297) returns the exact text/asset refs only while `withdrawn && unacknowledged`;
`acknowledge_recovery` (L300-L337) records the disposition, advances the operation revision, and permits
disposal (post-ack replays return the same outcome/revision with the body disposed). `withdraw_status`
(L187) and `_redrive_withdrawal` (L577) reconcile a lost `may_have_sent` response through the same
`withdrawRequestId` — the substrate replay is idempotent and carries no recovery, so the journal is
the recovery source of last resort. `sweep_recoveries` (L651) lazily disposes text and bytes at lease
expiry (L652-L660) and flips `recoveryState` to `expired`. `_replay_response` (L708-L732), the ref
mint `_mint_operation_ref` (L748-L754), and the projection/coercions (`_withdrawal_projection`
L735-L745, `_as_withdrawal` L772-L774, `_as_recovery` L777-L779) plus `withdraw_http_status`
(L782-L791) complete the wire surface.

### Conventions

Recovery is a bounded lease, not durable storage: acknowledgement disposes the raw content and
`keep-current-draft` deletes recoverable staged bytes on disk; expiry disposes both. The recovery
never fabricates content — without a substrate payload and without a journal entry it is honestly
empty. Newer-draft semantics survive: the recovery carries `submittedDraftRevision` so the browser's
replace/keep choice stays revision-safe.

### Invariants And Boundaries

- The landed `cockpit_only` atomicity is preserved; the substrate linearizes queued→dispatching with
  exactly one winner (`already-dispatching` 409 at the edge).
- Recovery is bounded (32/channel, named eviction), authorization-bound (signed `recoveryRef`), and
  expiring (900 s lease); pressure expires the oldest lease with full disposal rather than failing a
  completed withdrawal.
- Pending discovery is opaque (no text/preview); exact text/assets cross only via authenticated fetch
  while unacknowledged; status/reconcile never carry recovery bodies.
- A self-minted valid-signature ref on a durable row still refuses not-found — the source rule is the
  backstop behind the signature.
- Lost withdraw responses record `delivery-unknown` (202) and reconcile with the same
  `withdrawRequestId`; the substrate replay never mints a replacement.

### Todos

None.

## Docs References

No Domain Documentation source is configured; the withdrawal/recovery contract is repository-owned.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No configured domain documentation was available. | — | — |

## Repo-Internal References

The substrate owns the atomic withdraw + pre-tombstone recovery payload; the recovery assembly and
attachment recoverable-marking are sibling modules; the ref authority re-binds every wire.

| Finding | Citations | Source Path |
| --- | --- | --- |
| The L2E atomic `cockpit_only` withdraw and pre-tombstone recovery capture. | L1-L120 | [harness_submission_authority.py](agents-remember/mcp/src/agents_remember/serving/harness_submission_authority.py) |
| Recovery content/digest/asset-ref assembly extracted to the sibling module. | L37-L123 | [recovery_assembly.py](agents-remember/mcp/src/agents_remember/serving/conversation/control/recovery_assembly.py) |
| Attachment recoverable-marking and byte deletion under the same lease. | L460-L500 | [attachments.py](agents-remember/mcp/src/agents_remember/serving/conversation/control/attachments.py) |
| The withdrawal/operation/recovery ref brands re-bound on every wire. | L37-L44; L113-L219 | [refs.py](agents-remember/mcp/src/agents_remember/serving/conversation/control/refs.py) |

## Cross-Repo References

No meaningful cross-repo references found.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No meaningful cross-repo references found. | — | — |

## 260731-EFA-L2 Current Delta

**`WithdrawalTicket`** (`epoch`, `identity`, `operation_ref`, `fingerprint`, `withdraw_request_id`)
is now the value every record in this module is stamped from: the exact operation being withdrawn,
and the request that is withdrawing it. Settled, failed and unknown records all carry the same five
facts, and passing them as one ticket is what keeps a failure record from being stamped with a
different operation's identity than the attempt it describes. `_unknown_withdrawal(ticket, detail)`
is the named builder for the unknown case, and `_mint_operation_ref(scope, identity)` mints against
the verified `ControlScope`.

Withdrawal semantics — what may be withdrawn, the idempotent replay, and the recovery payload
crossing exactly once — are unchanged.

This entry supersedes any earlier description in this sidecar that conflicts with the current source behavior above; verification metadata stays pinned to the pre-commit source history until closeout.

## Update History

- 2026-07-31T19:30+02:00 — 260731-EFA-L2 curator: re-derived 11 stale self-citations in Logic and
  corrected one wrong claim they were hiding. The `WithdrawalTicket` refactor moved the record
  builders up and the wire helpers down, so: `RecoveryRecord` L87 → L90-L101, `WithdrawalRecord`
  L101 → L104-L118, `withdraw` L117 → L121-L184, `_failure_for_result` L425 → L416-L439,
  `_settled_failure` L538 → L514-L545, `_unknown_withdrawal` L573 → L548-L574, `fetch_recovery` L263
  → L266-L297, `_live_row` L657 → L631-L648, `_replay_response` L735 → L708-L732, `_verify_refs`
  L792 → L757-L769, and `withdraw_http_status` L832 → L782-L791 (L832 was past the end of an
  802-line file). The claim that `_verify_refs` re-binds the ref pair "against the live `_live_row`"
  is not what the code does: `_verify_refs` only decodes both refs under one `RefBinding` and
  refuses a pair naming different operation identities; `_live_row` is called from
  `_drive_withdrawal` (L365) to refuse anything that is not a still-`queued` cockpit-source row.
  Rewritten to say that, with `_drive_withdrawal` L358 → L358-L398,
  `_apply_withdrawal_result` L401 → L401-L413, `_build_withdrawn_record` L442 → L442-L511, the ref
  mint L775 → `_mint_operation_ref` L748-L754, and the projection/coercions L735/L822/L827 →
  `_withdrawal_projection` L735-L745 / `_as_withdrawal` L772-L774 / `_as_recovery` L777-L779.
  `pending_recoveries` L226, `withdraw_status` L187, `_redrive_withdrawal` L577, `sweep_recoveries`
  L651 and the lease anchors L457-L458 were re-checked and are correct. NOT fixed (beyond this
  worklist): the sweep's disposal span L652-L660 is really L657-L663 (the expiry branch through
  `attachments.delete_recoverable`).

- 2026-07-31T17:20+02:00 — 260731-EFA-L2 curator: repaired 2 sibling-module citations, both read
  back. `recovery_assembly.py` is 123 lines, so the stamped `L36-L128` ran off the end; the real
  extraction is L37-L123 — `EMPTY_DIGEST` plus `recovery_text` / `recovery_digest` /
  `recovery_payload` / `recover_attachment_refs` / `attachment_recovery_ref`, i.e. exactly the
  content/digest/asset-ref trio the claim names, ending at the last line of the file. `refs.py`
  needed two ranges instead of one: the brands are the `RefPurpose` literal and
  `_PREFIX_BY_PURPOSE` prefix table at L37-L44, and the re-binding is L113-L219 — `RefBinding` /
  `RefTarget`, `mint_ref`, `decode_ref`, and `_check_payload`, whose docstring is literally
  "Re-validate the decoded payload's full binding on every wire". Claims unchanged; both still true.

- 2026-07-31T16:10+02:00 — 260731-EFA-L2 curator: recorded `WithdrawalTicket` as the single stamp for every withdrawal record, plus `_unknown_withdrawal` and `_mint_operation_ref`.
- 2026-07-20T15:45+02:00 — 260718-CHATS-L3 curator: created the sidecar for the cockpit-only
  withdrawal + bounded recovery authority — preserved atomicity, 900 s authorization-bound recovery
  lease with opaque discovery/authenticated fetch/ack disposal/expiry, journal-of-last-resort
  reconciliation, and revision-safe newer-draft semantics. Verification is blank because the new
  source file is uncommitted; closeout owns its first source stamp.
