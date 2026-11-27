# Native receipt-tracked retirement

[MCP package overview](../../../overview.md)

## Contract

`retire_native_seat` resolves the bound caller and one unique launch receipt of any role (including `bootstrap`, `investigator`, `manager`, `orchestrator`, `architect`, `worker`, `reviewer`, `curator`, normalizing legacy `system-specialist`) from current and archived launch receipts before any host effect. It refuses callerless, non-UUID, unknown, duplicated (including current plus history), out-of-scope, or unresolved-launch (`starting`/`unknown` or replayable `rejected` step-up) targets with no host call and no disk write.

Authorization uses caller scope via `application/seat_retirement_scope.retirement_scope_refusal` (Architect: any other seat; Manager: seats on its master and leaves; Orchestrator: seats on its sprint, masters and leaves; other roles: none; no self-retirement), checked from current task-document membership before idempotent `already-retired` or host archival.

Before archiving, `_require_no_open_children` refuses (`open-children`) with every open child seat (`parentAgentId == seat.agent_id`, no `retiredBy`, either an unclosed deferred held seat counted without a host read or found and unarchived on host) named in `openChildren`. For an uncreated deferred held seat (`is_deferred_held_receipt`), `_archive_retiree` skips host reads, `_require_interruptible`, and host archival, settling retirement and any held store locally with zero host calls while still recording caller, time, and reason. For any host-backed unarchived seat, `_require_interruptible` requires `interrupt_turn=true` when currently in a turn or with running provider subagents (naming the subagent count in `agent-in-turn`).

Retirement archives rather than deletes, settles any waiting held messages via `role_retirement_receipt.settle_retirement` -> `role_held_store.settle_held_store` (recording them as undelivered in `heldStoreClosures` and `heldMessageLines` with `heldWaiting=0` and unlinking the store), and records caller, time, and reason without giving the seat a turn. A repeated authorized retirement checks scope, settles and unlinks any leftover held store on disk, and returns `already-retired`.

The scan reads mixed report folders through `read_enumerated_receipt`, passing over valid JSON attachments that are not current-line launch receipts while retaining unreadable-document refusals.

## Failure custody

`_archive_retiree` persists `retireIntent` via `hold_retirement` BEFORE calling host `agent-archive` so a racing host refresh defers to the product-owned retirement. If Paseo definitively refuses (`paseo_archive_refused`), `_clear_refused_archive` withdraws `retireIntent` and returns `archive-refused`. If transport is uncertain, `retireIntent` stays for identical retry (`host-unreachable`). If host archive succeeds but `_finish_retirement` (`settle_retirement`) fails to persist, `retire-record-failed` returns the actual split with `retireIntent` so an identical retry completes settlement instead of reporting `already-retired`. Same-call replacement is handled separately by `cli/role_launch_liveness.py` and `cli/role_retirement_receipt.py`.

## Evidence

- `_retire_seat` locates a unique receipt, checks caller scope via `retirement_scope_refusal`, refuses unresolved launches, and handles authorized `already-retired` repeats before host archival. [1]

- `_locate_seat` enumerates current and archived receipts via `read_enumerated_receipt` and refuses unknown or duplicated agent IDs before any host or disk effect. [2]

- `_archive_retiree` checks open children (including unclosed deferred held children without host reads), settles uncreated deferred held seats locally with zero host calls, checks interruption for host-backed seats, records `retireIntent` via `hold_retirement` before `_archive_on_host`, clears definitive refusals, and settles via `_finish_retirement` with retryable `retire-record-failed` custody. [3]
