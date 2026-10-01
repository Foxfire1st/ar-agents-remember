# mcp/src/agents_remember/serving/conversation/control/withdrawals.py

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

cit:([`RecoveryRecord`], mcp/src/agents_remember/serving/conversation/control/withdrawals.py:90-101) and cit:([`WithdrawalRecord`], mcp/src/agents_remember/serving/conversation/control/withdrawals.py:104-118) are the bounded ledger rows.
cit:([`withdraw`], mcp/src/agents_remember/serving/conversation/control/withdrawals.py:121-184) serializes on the per-session lock; cit:([`_verify_refs`], mcp/src/agents_remember/serving/conversation/control/withdrawals.py:757-769) re-binds the
withdrawal+operation ref pair — it decodes BOTH refs under the one caller/session/epoch
`RefBinding` and refuses a pair that does not name the same operation identity — while the live
queue row is checked one step later: cit:([`_drive_withdrawal`], mcp/src/agents_remember/serving/conversation/control/withdrawals.py:358-398) reads cit:([`_live_row`], mcp/src/agents_remember/serving/conversation/control/withdrawals.py:631-648)
and settles a failure unless the row is a still-`queued` cockpit-source row, then drives the
substrate atomic withdraw and cit:([`_apply_withdrawal_result`], mcp/src/agents_remember/serving/conversation/control/withdrawals.py:401-413) records the outcome —
cit:([`_build_withdrawn_record`], mcp/src/agents_remember/serving/conversation/control/withdrawals.py:442-511) captures recovery via `recovery_assembly` and anchors the
900 s lease (`withdrawn_at = clock()`, expiry at `withdrawn_at + RECOVERY_TTL_SECONDS`, L457-L458),
while cit:([`_failure_for_result`], mcp/src/agents_remember/serving/conversation/control/withdrawals.py:416-439) / cit:([`_settled_failure`], mcp/src/agents_remember/serving/conversation/control/withdrawals.py:514-545) / cit:([`_unknown_withdrawal`], mcp/src/agents_remember/serving/conversation/control/withdrawals.py:548-574) type every other outcome.
cit:([`pending_recoveries`], mcp/src/agents_remember/serving/conversation/control/withdrawals.py:226-263) lists opaque identity/state/expiry only — no text, no preview.
cit:([`fetch_recovery`], mcp/src/agents_remember/serving/conversation/control/withdrawals.py:266-297) returns the exact text/asset refs only while `withdrawn && unacknowledged`;
cit:([`acknowledge_recovery`], mcp/src/agents_remember/serving/conversation/control/withdrawals.py:300-337) records the disposition, advances the operation revision, and permits
disposal (post-ack replays return the same outcome/revision with the body disposed). cit:([`withdraw_status`], mcp/src/agents_remember/serving/conversation/control/withdrawals.py:187-223) and cit:([`_redrive_withdrawal`], mcp/src/agents_remember/serving/conversation/control/withdrawals.py:577-628) reconcile a lost `may_have_sent` response through the same
`withdrawRequestId` — the substrate replay is idempotent and carries no recovery, so the journal is
the recovery source of last resort. cit:([`sweep_recoveries`], mcp/src/agents_remember/serving/conversation/control/withdrawals.py:651-669) lazily disposes text and bytes at lease
expiry and flips `recoveryState` to `expired`. cit:([`_replay_response`], mcp/src/agents_remember/serving/conversation/control/withdrawals.py:708-732), the ref
mint cit:([`_mint_operation_ref`], mcp/src/agents_remember/serving/conversation/control/withdrawals.py:755-761), and cit:([`_withdrawal_projection`, `_as_withdrawal`, `_as_recovery`, `withdraw_http_status`], mcp/src/agents_remember/serving/conversation/control/withdrawals.py:735-745; mcp/src/agents_remember/serving/conversation/control/withdrawals.py:772-774; mcp/src/agents_remember/serving/conversation/control/withdrawals.py:777-779; mcp/src/agents_remember/serving/conversation/control/withdrawals.py:782-791) the projection/coercions complete the wire surface.

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

## Evidence

### Docs References

No Domain Documentation source is configured; the withdrawal/recovery contract is repository-owned.

No configured domain documentation was available.

### Repo-Internal References

The substrate owns the atomic withdraw + pre-tombstone recovery payload; the recovery assembly and
attachment recoverable-marking are sibling modules; the ref authority re-binds every wire.

- The L2E atomic `cockpit_only` withdraw and pre-tombstone recovery capture. [1]
- Recovery content/digest/asset-ref assembly extracted to the sibling module. [2]
- Attachment recoverable-marking and byte deletion under the same lease. [3]
- The withdrawal/operation/recovery ref brands re-bound on every wire. [4]

### Cross-Repo References

No meaningful cross-repo references found.

No meaningful cross-repo references found.

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
