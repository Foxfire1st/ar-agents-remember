# mcp/src/agents_remember/serving/projections/snapshots.py

## Governing Overview

[serving projections overview](overview.md)

## Purpose

File-surface projection edge that re-exports the split runtime, analytical and task-document readers under one `__all__`. Provider, gate, pickup and expectation readers are absent.

## Code Commentary

The export list is the module's whole surface: enclosures and engine process facts, the analytical readers (drift, route coverage, tool reports, ledgers, start progress) and the canonical task-document readers. The facade exports canonical task readers rather than lifecycle/series readers, and enclosure/engine readers reuse supplied immutable ContractSnapshot values. No provider reader is exported: there is no configured-workspace snapshot read, contract-admitted worktree-group combination, `workspace_repository_id` existence check, producer-health proof, worktree resource/settings inspection or current-state/Docker enumeration here, so a caller must not expect provider nodes from this module. Engine landing refresh retains its separate publication owner.

Task-document observation deliberately tolerates unknown writer-version fields without loosening authoring: `_projected_document` removes only paths diagnosed as extra_forbidden and validates again in a bounded pass loop. Any missing-required, bad enum or malformed nested field without that removable-extra route still withholds the document. A newer optional field must not erase an otherwise valid completed leaf; tolerance does not admit arbitrary malformed truth. The facade re-exports the canonical reader from snapshots_impl/_task_documents.py, where the enforcement lives.

### Retained L56 converted-memory boundary

The verification-age sidecar reader remains removed. Persisted drift/route/tool/ledger analytical readers remain at the call edge; converted code-anchor/tree measurement belongs to the on-demand memory-quality producer, not a restored verification-date reader or registered drift-check tool. [14]

## Evidence boundary

Current source interpretation only; no fresh execution or grade.

## Source-bound reference inputs

- Canonical task-source and document readers remain read-only. [1]
- The extracted parser retains addressed unknown-field pruning without forgiving other malformed data. [5]
- [11]
- [12]
- [13]

- The current reader hub re-exports enclosure/engine, analytical and canonical task-document readers; it exports no workspace or worktree provider reader. [10]

- No provider-node reader is exported from this facade. Retained engine and analytical readers do not supply provider display nodes. [8]

- The hub retains drift, route coverage, tool-report, ledger and worktree-start progress readers; verification-age and provider-setup readers are absent. [14]
