# mcp/tests/_store_durability.py

## Governing Overview

[Tests overview](overview.md)

## Purpose

Forces one append into the read-to-replace compaction window of eight real JSONL stores. It is shared test support, not an assertion suite. Six controlplane adapters and two provider adapters call each store’s actual write/reclaim owners; the harness reports receipts versus durable records.

## Code Commentary

### Logic

`run_forced_lost_update` seeds a non-prunable anchor, forks a reclaimer and appender, and parks the
actual rewrite at a controlled rendezvous. The decoy is written before arming so a write that is
itself read-modify-write cannot trigger the hook prematurely. Bounded handoff and joins allow
correct locking to serialize the append without leaving child processes hung.

Successful append receipts are stored separately from store bytes. `surviving_ids` parses durable
records and counts torn lines; `_forced_result` reports attempted/surviving/lost records, errors
and stragglers. `harness_work_dir` derives a unique sibling directory from each exact root, so
sibling stores do not share receipt state. A zero-loss figure must be read alongside the actual
attempted count and errors.

### Invariants And Boundaries

- The anchor is never counted and keeps reclamation on the rewrite path instead of empty-log deletion.
- All eight adapters exercise real store behavior; no copied reclaim algorithm substitutes for it.
- Historical source extraction, model-path compatibility, stress loops and measurement CLI were removed.
- There is no import fallback for GateState; the canonical structural model is imported directly.
- Current controlplane/provider durability tests own the assertions, not this harness.

## Evidence

### Docs References

No external Domain Documentation source is configured; these are repository-owned implementation facts.

### Repo-Internal References

The exact source declarations below establish the current behavior; this inventory is not execution evidence.

- Shared real-store write/reclaim boundary [1]
- Provider stores share the same instrument [2]
- Independent durable-record/torn-line accounting [3]
- Controlled actual rewrite rendezvous [4]
- Per-root receipt isolation [5]
- Forked append/reclaim orchestration and bounded joins [6]

### Cross-Repo References

No separate cross-repository authority is established by this file.
