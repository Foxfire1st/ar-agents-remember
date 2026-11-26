# mcp/src/agents_remember/cli/role_receipt_files.py

## Governing Overview

[MCP package overview](../../../overview.md)

## Purpose

Owns atomic initial creation, strict and schema-filtering receipt reads, atomic replacement writes, pre-create leaf-scope gating, held-store-coupled archival, and history movement for role launch receipt JSON files.

## Code Commentary

- `RECEIPT_SCHEMA = "ar-role-execution/v1"` and `_now_iso()` define the receipt schema constant and UTC ISO timestamp helper.
- `_read_receipt(path)` inspects `lstat` mode (refusing non-regular files with HTTP 409), treats missing or concurrently moved files as `None`, refuses unreadable/invalid JSON/deeply nested bytes with HTTP 409 reconcile advice, and refuses non-dict or wrong-schema payloads as malformed.
- `read_enumerated_receipt(path)` wraps `_read_receipt` for mixed report-folder enumeration: readable JSON documents carrying another schema (`_names_another_document`) return `None`, while unreadable JSON retains HTTP 409 refusal.
- `_replace_receipt_bytes(path, receipt)` atomically replaces an existing receipt file via `_write_receipt_aside` + `temporary.replace(path)` while the receipt lock is held (used by `role_launch_receipts._write_receipt` and `role_retirement_receipt.hold_retirement`/`clear_retirement`).
- `_create_receipt` and `_install_initial_receipt` stage JSON into an fsynced sibling temporary file (`_write_receipt_aside`) and publish via `os.link(temporary, path, follow_symlinks=False)` under the receipt lock, returning `False` on `FileExistsError` so concurrent starts never overwrite an existing receipt.
- `_leaf_before_create` re-checks same-request identity, open receipt state, and `leaf_workspace_allows_creation` under the receipt lock before persisting `heldOpenPending` or `leafCreateEntered`; `_require_live_launch_scope` raises HTTP 409 for leaf receipts whose enclosure is terminal.
- `_archive_receipt` locks the receipt, settles its held store via `settle_held_store` when closed or host-confirmed (`archived`/`gone`), and delegates to `_move_receipt_to_history`.
- `_move_receipt_to_history` closes settled predecessor execution folders (`close_execution_role_folders`), refuses to overwrite an existing `history/<requestId>.json`, strips `reportCollectionFiles`, and moves the file via `path.replace(history)`.
- `_predecessor_held_ref` resolves a step-up predecessor's archived history receipt (verifying basename-only `requestId` and exact `(requestId, agentId)` match) into a `HeldSeatRef`.

## Relationships

- Consumed by `cli/role_launch_receipts.py` (which re-exports `RECEIPT_SCHEMA`, `_archive_receipt`, `_create_receipt`, `_now_iso`, `_read_receipt`, `read_enumerated_receipt`), `cli/role_launch_routes.py`, and `cli/role_retirement_receipt.py`.
- Coordinates receipt-locked held-store settlement with `cli/role_held_store.py`.

## Evidence

- `_install_initial_receipt` writes an fsynced temp file and links it with `os.link(..., follow_symlinks=False)`, returning `False` on `FileExistsError` without overwriting. [1]
- `_leaf_before_create` verifies same-request identity, non-closed state, and `leaf_workspace_allows_creation` under the receipt lock before recording `heldOpenPending` or `leafCreateEntered`. [2]
- `_archive_receipt` settles the seat's held store under the receipt lock when closed or host-confirmed before moving the receipt into history. [3]
- `_move_receipt_to_history` closes settled predecessor folders, rejects existing history collisions, strips `reportCollectionFiles`, and moves the receipt via `path.replace`. [4]

- `_read_receipt` enforces regular-file and `RECEIPT_SCHEMA` checks with HTTP 409 refusals, `read_enumerated_receipt` skips other-schema JSON attachments via `_names_another_document`, and `_replace_receipt_bytes` atomically updates receipts under the lock. [5]
