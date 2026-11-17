# mcp/src/agents_remember/canvas/explainer_workspace.py

## Governing Overview

[Route overview](overview.md)

## Purpose

The bytes of one leaf's environment — two detached Git worktrees, the instructions, the packet and the grants — and the build, Update and Retire sequences that prepare and remove them.

## Code Commentary

- `build_environment` prepares the two worktrees, instructions, packet and copied documents before writing the binding last. A failure removes the binding and retains worktrees that a retry can move.
- `update_environment` moves the same two worktrees, stages the instructions and packet, and binds last. An unchanged comparison returns current without writing; a failed moved Update leaves no binding.
- `retire_workspace` records the seat's process tree in a receipt before anything is archived; `settle_retire` archives the seat, ends its processes, removes the workspace and only then finishes the receipt.
- A retire that cannot finish leaves the receipt pending with the step it reached and the paths it held, so a repeat finishes that receipt instead of starting a second one.
- `_copy_planned_documents` writes a planning leaf's requirement packets and declared effects into `planned/` beside the kit and the task's reference notes, before the binding is written; a recorded binding copies none.

## Evidence

- The process tree is recorded in a receipt before the seat is archived or any file is removed [5]
- Archive, process end and removal are each recorded, and the receipt finishes only after the workspace is gone [6]

- A planned binding's folder receives the plan as text before the binding, and a recorded binding copies none. [7]

- Retired at the fifth freeze d59c3493: mcp/src/agents_remember/canvas/explainer_workspace.py:405-454 - the region it cited is not in the file at the candidate and no re-point was possible; it was removed in commit 5f8398b32760677c370e3145add73cfa8388357b; mcp/src/agents_remember/canvas/explainer_workspace.py:370-390 - the region it cited is not in the file at the candidate and no re-point was possible. Retired means the anchor no longer stands, not that the cited subject was deleted.

- Every input is written before the binding, so a failed build never claims an environment [1]

- An Update moves the same two worktrees and binds last; a failed moved Update leaves no binding [2]
