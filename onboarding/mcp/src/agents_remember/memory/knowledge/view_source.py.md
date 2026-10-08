# mcp/src/agents_remember/memory/knowledge/view_source.py

## Governing Overview

[memory route overview](../overview.md)

## Purpose

Provides the read-only StoreViewReader port over a selected index snapshot.

## Code Commentary

The reader projects typed invariant/family/revision/member/realization values and provenance from the supplied connection and snapshot. `open_view_reader` opens that snapshot read-only and returns the handle and reader; the caller owns closing the handle. The former store_view_reader(OpenedKnowledgeStore) bridge is removed. This read port neither selects a substitute canonical store nor admits mutations.

## Evidence

### Repo-Internal References

- `StoreViewReader` owns the current boundary described above. [19]
- `open_view_reader` owns the current boundary described above. [20]
