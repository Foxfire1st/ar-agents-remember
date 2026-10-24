# skills/c-10-adopt-memory-baseline/workflows/carryover-from-branch.md

## Governing Overview

[Repository overview](../../../overview.md)

## Purpose

The carryover procedure kept beside baseline adoption: prove which source-branch code changes landed, then carry their richer converted onboarding into the exact open external-memory recovery leaf, with the curator answering the worklist and normal closeout publishing.

## Code Commentary

The file is the surviving owner of the carryover procedure and its opening comment says so: `memory_carryover_plan` and `memory_carryover_apply` own the operations, while the recovery leaf, the curator's own row computation and the normal closeout that makes the one memory commit are this file's sequence. Carryover is selective memory reconciliation, not a Git merge: it never writes an official checkout and never moves protected refs, and its clean code worktree must stand at the selected official tip.

Plan is read-only and files no report; its candidates are reviewed before an approval-gated apply. Both memory trees must hold valid `knowledge/layout.json` markers with the same conversion-format version or nothing further is read, and unconverted memory is refused with the conversion command or the crossing sync named. Markdown and its sidecar are compared, selected and written together, and the sections keep their own keys: source path for file cards, the normalized route (`.` for the root) for route overviews, the memory-only path or route for memory-only documents, and the literal `entity-catalog` for that unit. Code evidence and anchors are observed at official code, records and history rows are read as aids rather than imported answers, and apply validates the whole worktree and commits nothing — `carryover-pending` holds cleanup and finalization until the publication lands.

## Evidence

- The kept procedure owns the carryover sequence beside baseline adoption: plan read-only, review, approval-gated apply, curator rows, normal closeout publication. [1]
- Candidate units keep their own selection keys and differ only within an identical conversion-format version; unconverted memory is refused rather than read further. [2]
- Apply commits nothing; `carryover-pending` blocks cleanup and finalization until the memory publication lands. [3]
