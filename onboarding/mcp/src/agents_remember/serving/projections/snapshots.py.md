# mcp/src/agents_remember/serving/projections/snapshots.py

## Governing Overview

[serving projections overview](overview.md)

## Purpose

File-surface projection edge for current provider snapshots and re-exported enclosure, analytical and task-document readers. Gate, pickup and expectation readers are absent.

## Code Commentary

read_providers combines the captured workspace snapshot with only admitted active worktree provider groups. Worktree resource identities come from the isolated provider settings and are inspected together, with individual fallback for partial Docker failures; unavailable inspection is not invented readiness. The facade re-exports split current readers so file I/O remains at the edge while observer reduction is pure. Shared ContractSnapshot permits one per-tick contract census; task-document readers retain JSON-primary validation and lifecycle/series identity, while engine landing refresh keeps its own publication boundary.

Task-document observation deliberately tolerates unknown writer-version fields without loosening authoring: `_projected_document` removes only paths diagnosed as extra_forbidden and validates again in a bounded pass loop. Any missing-required, bad enum or malformed nested field without that removable-extra route still withholds the document. A newer optional field must not erase an otherwise valid completed leaf; tolerance does not admit arbitrary malformed truth. The facade re-exports the canonical reader from snapshots_impl/_task_documents.py, where the enforcement lives.

## Evidence boundary

Current source interpretation only; no fresh execution or grade.

## Source-bound reference inputs

- [1]
- [2]
- The canonical projected-document reader prunes only extra_forbidden paths, revalidates in bounded passes and still withholds other malformed truth. [5]
- [6]
- [7]
- [8]
- [9]
- [10]
- [11]
- [12]
- [13]
