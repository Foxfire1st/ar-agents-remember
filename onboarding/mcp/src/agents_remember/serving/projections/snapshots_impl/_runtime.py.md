# mcp/src/agents_remember/serving/projections/snapshots_impl/_runtime.py

## Governing Overview

[serving projections overview](../overview.md)

## Purpose

Runtime process-surface readers: enclosures, gates, inbox, expectations, engine facts. These readers describe the live worktree population -- enclosure contracts, gate state, agent inbox pickups, expectation rows, and the enriched engine process facts the Engine Room map renders. The git-backed ledger enrichment is imported from the analytical readers, which own the ledger window.

## Code Commentary

L23 attaches the latest task-bound lifecycle-operation projection while building an enclosure snapshot, keeping dashboard status derived from durable operation state.

- `read_enclosures`
- `_enclosure_from_contract`
- `read_gates`
- `read_agent_pickups`
- `read_expectation_rows`
- `read_engine_process_facts`
- `refresh_engine_process_landing`
- `_safe_status_payload`
- `_cached_local_status`

`read_agent_pickups` projects entry, subject, and owner task-document references from inbox rows.
`read_expectation_rows` projects the expectation's `taskDocumentRef`; neither reader reconstructs
or publishes a leaf-key ownership field.

## Invariants And Boundaries

- The card mirrors the source file one-to-one at `mcp/src/agents_remember/serving/projections/snapshots_impl/_runtime.py`.

## Evidence

### Repo-Internal References

The module's own top-level surface is listed in Code Commentary; no cross-file citation rows are needed for this split module.
