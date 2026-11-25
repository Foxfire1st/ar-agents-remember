# mcp/src/agents_remember/cli/shared_held_store_reconciliation.py

## Governing Overview

[MCP package overview](../../../overview.md)

## Purpose

Reclaims legacy shared held-message store files and obsolete `.lock` files under `<workspace>/.ar-product/held-messages/` once older server writers have stopped, while preserving ambiguous, open, or unconfirmed seats.

## Code Commentary

- `reconcile_shared_held_stores` returns `state: "blocked"` on non-dry-run calls when `_older_writer_refusal` detects an unknown serving build digest or any running server whose `loadedDigest` differs from `process_serving_build().source_digest`, or when `_shared_agent_ids` raises `OSError` or `AuthorityError`.
- `_shared_agent_ids` confines the held-messages directory via `confine_non_symlink_rel`, treats an absent directory as empty, and extracts minted agent IDs (`is_minted_agent_id`) from both `<id>.json` stores and standalone `<id>.json.lock` files.
- `_shared_owners` matches discovered agent IDs against `_line_receipts(config)` whose `workspace.path` equals `config.workspace_root`; `_reconcile_agent` preserves any agent with zero or multiple matching receipts.
- For an open receipt, `_host_closure` queries `paseo_status.read_agent` and accepts only reachable `"archived"` or `"gone"` seats; reachable active seats or unreachable hosts raise `AuthorityError` and keep the store intact.
- Delegates per-agent preview and live settlement to `role_held_store.preview_held_store_reconciliation` and `role_held_store.reconcile_held_store`.

## Relationships

- Invoked from `mcp/tools/core.py` during opt-in `runtime_install(reconcile_shared_held_stores=True)`.
- Relies on `cli/role_held_store.py` for generation-checked settlement and on `serving/server_registry.py` for running-server digest inventory.

## Evidence

- `reconcile_shared_held_stores` blocks live mutation when older writers remain or directory confinement fails, then previews or reconciles each discovered minted agent ID. [1]
- `_older_writer_refusal` checks `process_serving_build().source_digest` against every running server's `loadedDigest` and refuses reconciliation if any mismatch or unknown digest exists. [2]
- `_shared_agent_ids` confines the held-messages directory against symlinks and recognizes minted agent IDs from both `.json` stores and standalone `.json.lock` files. [3]
- `_reconcile_agent` preserves zero/ambiguous owners and errors, checks `_host_closure` for open receipts, and dispatches to `preview_held_store_reconciliation` or `reconcile_held_store`. [4]
