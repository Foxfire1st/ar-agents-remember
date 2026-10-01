# mcp/src/agents_remember/models/conversations/withdrawals.py

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

## Evidence

### Docs References

No external/domain documentation is configured.

No configured domain documentation was available.

### Repo-Internal References

- Withdrawal projection validates allowed phase/outcome/recovery products and coherent recovery expiry. [1]

### Cross-Repo References

No cross-repository implementation participates.

No meaningful cross-repo references found.
