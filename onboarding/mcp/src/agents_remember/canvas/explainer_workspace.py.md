# mcp/src/agents_remember/canvas/explainer_workspace.py

## Governing Overview

[Route overview](overview.md)

## Purpose

The bytes of one leaf's environment — the read-only snapshot of both bound trees, the instructions, the packet and the grants — and the build, Update and Retire sequences that write and remove them.

## Code Commentary

- `build_environment` writes the workspace, a snapshot, the instructions and the packet, and binds last, so a failure before that step leaves an environment that claims no binding and is cleaned up.
- `update_environment` writes the next binding the same way, keeps the snapshot it replaced while a turn is active, and reclaims the replaced snapshots otherwise; an unchanged comparison answers as current without writing.
- `write_snapshot` hard-links a file whose blob the previous snapshot already held, writes only the rest in bounded batches, and seals a manifest of blob and size read-only.
- `next_snapshot_number` reclaims orphaned snapshots above the bound one, so an interrupted build cannot leave a number a later build would reuse.
- `retire_workspace` records the seat's process tree in a receipt before anything is archived; `settle_retire` archives the seat, ends its processes, removes the workspace and only then finishes the receipt.
- A retire that cannot finish leaves the receipt pending with the step it reached and the paths it held, so a repeat finishes that receipt instead of starting a second one.

## Evidence

- Every input is written before the binding, so a failed build never claims an environment [1]
- An Update binds last, and keeps the snapshot it replaced while a turn may still be reading it [2]
- A snapshot links the files whose blobs are unchanged and writes the rest, recording each one in a read-only manifest [3]
- A snapshot number above the bound one is reclaimed, so an interrupted build leaves nothing to reuse [4]
- The process tree is recorded in a receipt before the seat is archived or any file is removed [5]
- Archive, process end and removal are each recorded, and the receipt finishes only after the workspace is gone [6]
