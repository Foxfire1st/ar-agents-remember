# mcp/src/agents_remember/models/conversations/withdrawals.py

| Field                  | Value                                                          |
| ---------------------- | -------------------------------------------------------------- |
| repository             | agents-remember                                                |
| path                   | `mcp/src/agents_remember/models/conversations/withdrawals.py`   |
| doc_type               | `file-level-onboarding`                                        |
| lastUpdated            | 2026-08-08T14:38+02:00                                         |
| lastVerifiedCommitHash | `7bf564a663bb61f12844dee39538dd09a1633cdb`                     |
| lastVerifiedCommitDate | 2026-08-10T12:28:42+02:00|
| governingOverview      | `overview.md`                                                  |

## Governing Overview

[models conversations overview](overview.md)

## Purpose

`models/conversations/withdrawals.py` (260731-EFA-L9, moved from
`serving/conversation/_models_operations.py`) owns the withdrawal/recovery DTO family: queue
withdraw requests, attachment recovery refs, success/failure responses, operation projections,
and the bounded pending-recovery list.

## Code Commentary

### Logic

`WithdrawQueueRequest` (cit:(["class WithdrawQueueRequest"], mcp/src/agents_remember/models/conversations/withdrawals.py:16-16)) starts the family;
`WithdrawalRecovery` (cit:(["class WithdrawalRecovery"], mcp/src/agents_remember/models/conversations/withdrawals.py:35-35)) is the pre-tombstone recovery payload;
`FailedWithdrawalResponse` (cit:(["class FailedWithdrawalResponse"], mcp/src/agents_remember/models/conversations/withdrawals.py:53-53)) stays raw-free;
`PendingWithdrawalRecoveryList` (cit:(["class PendingWithdrawalRecoveryList"], mcp/src/agents_remember/models/conversations/withdrawals.py:132-132)) bounds the
recovery projection.

### Invariants And Boundaries

- Withdrawal raw recovery is a successful-response-only privacy boundary; lists and failures stay
  raw-free.
- Pending-recovery projections remain raw-free.

### Todos

No known follow-up.

## Docs References

No external/domain documentation is configured.

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured domain documentation was available. | — | — |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| Hostile tests pin withdrawal/recovery products. | `test_cursor_bindings_preserve_authorization_identity_scope_and_purpose` | mcp/tests/test_conversation_contracts.py:196-220 |

## Cross-Repo References

No cross-repository implementation participates.

| Finding | Anchor | Source |
| --- | --- | --- |
| No meaningful cross-repo references found. | — | — |

## Update History

- 2026-08-08T14:38+02:00 — 260731-EFA-L9 curator: created for the withdrawals module moved from
  `serving/conversation/_models_operations.py`. Verification metadata pinned until closeout
  stamps the L9 code commit.
