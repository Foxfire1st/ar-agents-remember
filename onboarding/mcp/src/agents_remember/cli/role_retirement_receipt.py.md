# mcp/src/agents_remember/cli/role_retirement_receipt.py

## Governing Overview

[MCP package overview](../../../overview.md)

## Purpose

Owns receipt-locked retirement intent reservation (`retireIntent`), confirmed retirement settlement (`retiredBy` + held-store settlement), replacement predecessor settlement, and retirement-field preservation on existing launch receipts.

## Code Commentary

- `Retirement` models attribution fields (`caller`, `callerAgentId`, `reason`, `detail`, optional `replacementRequestId`).
- `hold_retirement(path, receipt, intent)` acquires the receipt lock, verifies exact `(requestId, agentId)` identity and absence of conflicting `retiredBy`/`retireIntent`, and atomically persists `retireIntent` via `role_receipt_files._replace_receipt_bytes` before any host archive call so a racing refresh defers to the product-owned retirement.
- `clear_retirement(path, receipt, intent)` removes a matching `retireIntent` after a definitive host refusal (`paseo_archive_refused`).
- `settle_retirement(path, receipt, intent, *, host_state=None)` validates receipt state under the lock, builds `retiredBy`, `retireReason`, `canRevive=False`, and terminal status updates (`_retirement_updates`, preserving `rejected` and pending leaf-archive reconciliation states), and delegates to `role_held_store.settle_held_store(..., remove_receipt_fields=("retireIntent",))` so waiting messages are recorded in `heldStoreClosures` and `heldMessageLines` (`heldWaiting=0`) and the held store is unlinked atomically.
- `finish_replacing_predecessor` and `settle_confirmed_replacement` settle an exact archived history predecessor matching `predecessorReports.requestId`, `archiveAgentId`, and `retireIntent.replacementRequestId` only after the host acknowledges predecessor archival, then close non-enclosure predecessor folders via `close_execution_role_folders` (recording collection failures in `predecessorCollectionError` without discarding the host launch outcome).
- `preserve_retirement(current, receipt)` prevents an ordinary receipt writer from reopening a retired seat, erasing `retiredBy`/`heldMessageLines`, or resurrecting a cleared `retireIntent`, while preserving `status`/`detail` when `_prepared_start_refused(receipt)` holds.

## Relationships

- Consumed by `cli/role_retire.py`, `cli/role_launch_liveness.py`, `cli/role_launch_receipts.py`, and `cli/role_launch_archive.py`.
- Delegates atomic receipt persistence to `cli/role_receipt_files.py`, held-store settlement to `cli/role_held_store.py`, and non-enclosure folder closure to `worktrees/role_reports.py`.

## Evidence

- `hold_retirement` and `clear_retirement` persist and withdraw matching `retireIntent` under the receipt lock via `role_receipt_files._replace_receipt_bytes`. [1]
- `settle_retirement` delegates retirement attribution, held-store closure/unlinking, and `retireIntent` removal to `role_held_store.settle_held_store`. [2]
- `finish_replacing_predecessor` and `settle_confirmed_replacement` settle the exact history predecessor after acknowledged archival and close non-enclosure predecessor folders. [3]
- `preserve_retirement` keeps committed `retiredBy`, `retireReason`, `canRevive`, `heldWaiting`, `terminalObservedAt`, `heldMessageLines`, and pending `retireIntent` across ordinary receipt writes while preserving refused prepared starts. [4]
