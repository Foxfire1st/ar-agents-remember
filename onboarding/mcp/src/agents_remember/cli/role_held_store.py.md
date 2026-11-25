# mcp/src/agents_remember/cli/role_held_store.py

## Governing Overview

[MCP package overview](../../../overview.md)

## Purpose

Owns generation-fenced admission, closure settlement, reconciliation, and restart handoff for per-seat held-message stores under each launch receipt's exclusive lock. Ensures closed or superseded launch generations accept no new held-store writes and records waiting message texts in the launch receipt before removing the store file.

## Code Commentary

- Serializes store writes (`open_held_store`), waiting-count refreshes (`refresh_waiting_count`), closure settlement (`settle_held_store`), reconciliation (`reconcile_held_store`), and generation rollover (`begin_held_generation`) under `exclusive_file_lock(ref.receipt_path, "role execution receipt")`.
- `_current` re-reads the live receipt under the lock and refuses with `HeldSeatClosed` when the receipt moved or changed identity (`receipt-moved`) or changed `heldStoreGeneration` (`generation-changed`); `open_held_store` additionally refuses closed receipts (`closed`) and absent workspaces (`workspace-missing`).
- `receipt_is_closed` treats a seat as closed only on durable marks (`retiredBy`, `status == "rejected"`, or `leafArchive.closing`); a `stopped` status alone never closes a seat.
- `_settle` validates non-symlink parent directories and regular store files, merges `pendingLines`, records remaining messages under `heldStoreClosures[<generation>].waitingMessages` (distinguishing `closed-with-delivery-unconfirmed` for claimed IDs from `not-delivered-archived-or-gone`), persists the receipt with `heldWaiting: 0`, and unlinks the store file only after receipt persistence.
- `reconcile_held_store` refuses `host_state="gone"` while `receipt_may_create` is true (`creation-pending`), settles the store, and removes any obsolete `.lock` sidecar; `preview_held_store_reconciliation` and `preview_held_store_settlement` validate the same operands without taking the lock.
- `leaf_workspace_allows_creation` checks the worktree contract's `lifecycle_id`, `cleanup` state, and `terminal_contract_authority_if_present`, allowing only absent or `reopen-reset`.

## Relationships

- Consumed by `role_held_messages.py`, `role_launch_receipts.py`, `role_launch_enclosure.py`, `role_launch_publication.py`, `role_receipt_files.py`, `role_retire.py`, `role_launch_archive.py`, `role_launch_liveness.py`, `role_launch_outcome.py`, `paseo_role_tools.py`, `paseo_role_recipients.py`, `developer_delivery.py`, `provider_limit_drain.py`, `product_messages.py`, `role_message_delivery.py`, and `shared_held_store_reconciliation.py`.
- Delegates store file schema and atomic I/O to `controlplane/held_store_layout.py`.

## Evidence

- `open_held_store` acquires the receipt lock, verifies exact live seat identity and generation via `_current`, and refuses closed receipts or absent workspaces with `HeldSeatClosed`. [1]
- `settle_held_store` requires prior closure, closure-marking receipt updates, or confirmed host closure (`archived`/`gone`) before delegating to `_settle`. [2]
- `_settle` validates store paths, merges `pendingLines`, writes `heldStoreClosures` and `heldWaiting: 0` to the receipt, and unlinks the store file only after durable receipt publication. [3]
- `begin_held_generation` restricts restarts to non-retired, non-closing `stopped`/`rejected` seats, settles the prior generation, increments `heldStoreGeneration`, and writes with `prior_generation` checking. [4]
