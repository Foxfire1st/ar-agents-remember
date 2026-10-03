# mcp/src/agents_remember/worktrees/modules/startup/start_memory.py

## Governing Overview

[Nearest governing overview](../overview.md)

## Purpose

Own external-memory admission/preparation and truthful named-ref facts during worktree start.

## Code Commentary

`prepare_memory_for_start` first settles disabled/external repository availability. Ordinary apply/default use calls `_ensure_memory_source_branch`, requiring the exact task-derived protected source ref; this owner creates no source branch.

Only explicit dry run carrying an admitted unpublished, non-symlink parent may report the exact source ref `would-create`, and only when that named ref is actually absent. A partial bootstrap journal may already own the ref while its parent contract is unpublished: then the original named-ref helper returns `existing`. Contract absence and ref absence are distinct facts. The planned base commit remains the owner's validated readable input; no fallback or guessed source is selected.

Ledger response metadata comes from `derive_memory_ledger` at that recorded base and remains informational. The existing worktree/mTime preparation keeps its dry-run boundary: no worktree creation or mTime synchronization. Divergent/missing source paths retain existing explicit indexing/mTime behavior. Generic ambient tool-completion logging is outside this startup-owned no-materialization claim.

## Evidence

No Domain Documentation source is configured in system/sources.md. These are current source/assertion anchors; the approved requirement and bound public receipts remain task artifacts.


- Preview facts distinguish absent exact refs from existing journal-owned refs. [5]
- Ordinary default/apply requires the exact named ref and writes none. [6]
- Dry run skips mTime mutation; divergence remains explicit. [7]
