# mcp/src/agents_remember/serving/conversation/control/withdrawals.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/serving/conversation/control/withdrawals.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-07-20T15:45+02:00 |
| lastVerifiedCommitHash |  `0be0099744bf1287805acf0b95072127b70f7104`|
| lastVerifiedCommitDate |  2026-07-20T15:34:11+02:00|
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

`RecoveryRecord` (L87) and `WithdrawalRecord` (L101) are the bounded ledger rows. `withdraw` (L117)
serializes on the per-session lock, `_verify_refs` (L792) re-binds the withdrawal+operation ref pair
against the live `_live_row` (L657), then `_drive_withdrawal` (L337) drives the substrate atomic
withdraw and `_apply_withdrawal_result` (L390) records the outcome — `_build_withdrawn_record` (L455)
captures recovery via `recovery_assembly` and anchors the 900 s lease (`withdrawn_at = clock()`,
expiry at `withdrawn_at + RECOVERY_TTL_SECONDS`, L473-L474), while `_failure_for_result` (L425) /
`_settled_failure` (L538) / `_unknown_withdrawal` (L573) type every other outcome.
`pending_recoveries` (L221) lists opaque identity/state/expiry only — no text, no preview.
`fetch_recovery` (L263) returns the exact text/asset refs only while `withdrawn && unacknowledged`;
`acknowledge_recovery` (L297) records the disposition, advances the operation revision, and permits
disposal (post-ack replays return the same outcome/revision with the body disposed). `withdraw_status`
(L182) and `_redrive_withdrawal` (L606) reconcile a lost `may_have_sent` response through the same
`withdrawRequestId` — the substrate replay is idempotent and carries no recovery, so the journal is
the recovery source of last resort. `sweep_recoveries` (L678) lazily disposes text and bytes at lease
expiry (L679-L687) and flips `recoveryState` to `expired`. `_replay_response` (L735), the ref mint
(L775), and the projections/coercions (L762/L822/L827) plus `withdraw_http_status` (L832) complete
the wire surface.

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
| Recovery content/digest/asset-ref assembly extracted to the sibling module. | L36-L128 | [recovery_assembly.py](agents-remember/mcp/src/agents_remember/serving/conversation/control/recovery_assembly.py) |
| Attachment recoverable-marking and byte deletion under the same lease. | L444-L484 | [attachments.py](agents-remember/mcp/src/agents_remember/serving/conversation/control/attachments.py) |
| The withdrawal/operation/recovery ref brands re-bound on every wire. | L112-L204 | [refs.py](agents-remember/mcp/src/agents_remember/serving/conversation/control/refs.py) |

## Cross-Repo References

No meaningful cross-repo references found.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No meaningful cross-repo references found. | — | — |

## Update History

- 2026-07-20T15:45+02:00 — 260718-CHATS-L3 curator: created the sidecar for the cockpit-only
  withdrawal + bounded recovery authority — preserved atomicity, 900 s authorization-bound recovery
  lease with opaque discovery/authenticated fetch/ack disposal/expiry, journal-of-last-resort
  reconciliation, and revision-safe newer-draft semantics. Verification is blank because the new
  source file is uncommitted; closeout owns its first source stamp.
