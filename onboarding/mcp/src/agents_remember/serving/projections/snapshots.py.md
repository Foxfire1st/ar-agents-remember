# mcp/src/agents_remember/serving/projections/snapshots.py

## Governing Overview

[serving projections overview](overview.md)

## Purpose

File-surface projection edge for current provider snapshots and re-exported enclosure, analytical and task-document readers. Gate, pickup and expectation readers are absent.

## Code Commentary

`read_providers` combines the configured workspace snapshot with contract-admitted worktree groups. Workspace existence uses configured identities via `workspace_repository_id`; only explicit producer health proves recovery. Worktree resources/settings are inspected with existing partial-Docker fallback, never invented readiness. Incomplete current-state, settings, container or fixed-level enumeration reads invalidate removal proof, even if some nodes remain displayable. The facade exports canonical task readers rather than lifecycle/series readers, and enclosure/engine readers reuse supplied immutable ContractSnapshot values. Engine landing refresh retains its separate publication owner.

Task-document observation deliberately tolerates unknown writer-version fields without loosening authoring: `_projected_document` removes only paths diagnosed as extra_forbidden and validates again in a bounded pass loop. Any missing-required, bad enum or malformed nested field without that removable-extra route still withholds the document. A newer optional field must not erase an otherwise valid completed leaf; tolerance does not admit arbitrary malformed truth. The facade re-exports the canonical reader from snapshots_impl/_task_documents.py, where the enforcement lives.

## Evidence boundary

Current source interpretation only; no fresh execution or grade.

## Source-bound reference inputs

- Canonical task-source and document readers remain read-only. [1]
- The extracted parser retains addressed unknown-field pruning without forgiving other malformed data. [5]
- [7]
- [8]
- [9]
- [10]
- [11]
- [12]
- [13]
