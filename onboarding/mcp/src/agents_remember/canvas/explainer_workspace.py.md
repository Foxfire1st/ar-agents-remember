# mcp/src/agents_remember/canvas/explainer_workspace.py

## Governing Overview

[Route overview](overview.md)

Preparation copies the supplied starter and exemplar directories as private reading material. An empty draft may inherit prior revision assets while skipping that revision’s top-level reserved kit directory.

## Purpose

The bytes of one leaf's environment — two detached Git worktrees, the instructions, the packet and the grants — and the build, Update and Retire sequences that prepare and remove them.

## Code Commentary

- `build_environment` prepares the two worktrees, instructions, packet and copied documents before writing the binding last. A failure removes the binding and retains worktrees that a retry can move.
- A moved `update_environment` refreshes instructions, packet and copied reading inputs before binding the same two worktrees. It creates missing workspace folders and preserves existing stage files. An unchanged comparison returns current without writing.
- `retire_workspace` records the seat's process tree in a receipt before anything is archived; `settle_retire` archives the seat, ends its processes, removes the workspace and only then finishes the receipt.
- A retire that cannot finish leaves the receipt pending with the step it reached and the paths it held, so a repeat finishes that receipt instead of starting a second one.
- Both bindings copy the task and named requirement packets into `inputs/` and list selected leaf report paths and digests in `inputs/reports.md`. The reports stay in their canonical locations. A planned binding also copies its plan and effects into `planned/`.

## Evidence



- Retired at the fifth freeze d59c3493: mcp/src/agents_remember/canvas/explainer_workspace.py:405-454 - the region it cited is not in the file at the candidate and no re-point was possible; it was removed in commit 5f8398b32760677c370e3145add73cfa8388357b; mcp/src/agents_remember/canvas/explainer_workspace.py:370-390 - the region it cited is not in the file at the candidate and no re-point was possible. Retired means the anchor no longer stands, not that the cited subject was deleted.


- Both bindings receive shared reading inputs, shipped starters and the exemplar. The planned binding receives its planned materials. An empty draft seeded from a retained revision omits the reserved kit directory. [7]
- A moved update refreshes the inputs and binding after preserving existing stage artifacts. An unchanged binding returns current. [2]
- A populated report manifest gives the path and SHA-256 of each selected report. [8]
- Build writes the inputs before it publishes the binding. [1]
- Retire stores the process snapshot in a receipt before archival and removal. [5]
- Retire finishes its receipt after archival, process cleanup and workspace removal. [6]
