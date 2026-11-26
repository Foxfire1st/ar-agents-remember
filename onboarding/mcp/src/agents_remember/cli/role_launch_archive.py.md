# mcp/src/agents_remember/cli/role_launch_archive.py

## Governing Overview

[Route overview](../../../overview.md)

## Purpose

Archives the role agents recorded for a closing leaf or series task folder and settles their held-message stores. For a leaf it matches receipts by canonical leaf selection (and lifecycle generation); for a series it matches receipts whose workspace lies inside `worktree_group`. It checks for unowned held-message stores in the task folder, supports read-only `dry_run` preview, fences every validated receipt before any host call, settles waiting messages with their text onto the launch receipt while unlinking the store, and settles each recorded target through `agent-archive` (retrying an owed target after observing `agent-state`), keeping unresolved work as receipt-owned debt.

## Code Commentary

### Logic

`LeafAgentArchive.archive(contract, *, dry_run=False, check_census=None)` iterates `receipt_paths` under `notes/reports/paseo-native-executions`, admitting receipts owned by the leaf (`selected == task_ref` and same lifecycle generation) or series (`workspace.path` under `worktree_group`), checks `_check_unowned_stores` for waiting or unreadable stores in `worktree_group` without a scoped receipt, runs optional `check_census`, rejects duplicate receipts for the same agent ID, and validates held-store settlement via `preview_held_store_settlement`. On `dry_run=True`, `ArchiveAttempt.preview` observes owed, closing, and pending targets via `agent-state` without mutating receipts or stores. On apply, every admitted receipt is fenced via `ArchiveAttempt.prepare` before the first host call (`_save` writes `leafArchive` and calls `settle_held_store` to record waiting messages on the receipt and unlink the store), and then `ArchiveAttempt.record` settles each target via `_settle_target` (predecessor debt head first, then own ID), retrying an `owed` answer once via `_retry_archive` (`agent-state` then `agent-archive`) within the remaining budget. Unreadable, conflicting, duplicate, or unowned items are recorded in `leftAlone`.

`ARCHIVE_BUDGET_SECONDS` (8 s) is the closing pass's host-attempt deadline, and
`ARCHIVE_CALL_SECONDS` (2 s) bounds each bridge call inside it. These are controls on host attempts,
not an unconditional wall-clock bound on the whole operation: receipt traversal, parsing, metadata
locking and writes continue outside the preempted call. The report separates `archived`,
`alreadyArchived`, `gone`, `owed` and `leftAlone`, and an empty recorded selection states that no
role agents were recorded.

### Conventions

The service writes only the launch receipts' archive fields, `LeafAgentArchive` retirement attribution (`_record_retired_target` -> `settle_retirement(..., _TASK_FINISHED_RETIREMENT)` on confirmed `archived`/`gone` targets and prior already-archived/gone targets), and closed held-store settlement fields (`heldStoreClosures`, `heldWaiting`, `heldMessageLines`) and unlinks settled stores; it never rewrites launch status when refusing a closing start, the report or artifact references, or the task document.

### Invariants And Boundaries

- A receipt whose reader binding conflicts with the leaf is left alone, never archived.
- The debt head stays in the receipt; no second queue or store is created.
- A host that does not confirm the archive leaves the target owed; nothing is reported archived that
  was not confirmed.

## Evidence


- The archive service derives the exact leaf reference and enumerates current and historical receipts. [1]


- Receipt marking happens under the existing lock before host I/O. [2]


- A marked start is refused and a returned creation settled, with `_record_retired_target` recording `LeafAgentArchive` `retiredBy` attribution on confirmed archives. [3]

- Recorded targets are validated and unreadable or conflicting records are named. [4]
- The bounded host call settles debt and outcomes. [5]

- The host-attempt deadline and per-call cap bound host calls; receipt traversal, parsing, locking and writes are not preempted by them. [6]
