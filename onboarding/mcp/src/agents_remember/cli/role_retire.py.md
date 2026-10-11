# Native receipt-tracked retirement

[MCP package overview](../../../overview.md)

## Contract

`retire_native_seat` resolves the bound caller and one native leaf agent from current and archived launch receipts before host effects. It refuses unknown, duplicated or callerless targets. The bound role caller must be the receipt’s original starter, including on an idempotent repeat. Dashboard replacement has its own explicit authority in the launch liveness owner; it is not a parentless admission to this MCP retirement entry. Empty IDs do not revive the removed hosted-seat implementation.

An active turn requires `interrupt_turn`. Retirement archives rather than deletes, ends that recipient’s waiting messages, and records the caller, time and reason without giving the child a turn. A repeated authorized retirement returns already-retired; authorization is still checked on a repeat. A current plus history duplicate is ambiguous, not a preferred current record.

## Failure custody

The native retirement archives before `_record_retirement` writes the launch record. If the host archives but that write fails, return `retire-record-failed` with the actual host/disk split and the caller/reason intent in the answer, not a claim that the receipt persisted it. An identical authorized retry records the caller and reason against the already archived host agent. A host read failure does not make a seat free. Same-call replacement is the separate launch-liveness path: it records replacement before the archival step. Neither path is leaf-close archival debt.

## Evidence

- The native entry checks original-starter authority before idempotent success or archive. [1]

- Unknown and ambiguous native targets refuse before retirement. [2]

- Host archive precedes receipt recording; failure is reported rather than rounded up. [3]
