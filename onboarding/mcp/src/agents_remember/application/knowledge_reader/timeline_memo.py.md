# mcp/src/agents_remember/application/knowledge_reader/timeline_memo.py

## Governing Overview

[application route overview](../overview.md)

## Purpose

Retain immutable timeline manifests in a thread-protected resident-weighted LRU, with at most one cached complete spill.

## Code Commentary

`put` rejects an entry whose retained-resident weight exceeds capacity, replaces the same key, drops a previously cached spilled key before retaining another spilled entry, and evicts oldest entries while over capacity. `get` updates LRU order without walking events. `discard` checks object identity so a failed old backing cannot remove a concurrent replacement. `clear` drops cache references and resets weight/spill bookkeeping; backing is reclaimed when its final owner, including an in-flight page, releases it. One cached spill is not a process-wide bound on concurrently built or still-referenced evicted spills. `spilled_bytes` exposes complete event-plus-offset disk cost independently of resident weight; no repository/persisted store or background worker is added.

## Evidence

### Docs References

No Domain Documentation source is configured for this repository. Requirement packets are task authority, not an implementation proof or a fresh acceptance.

### Repo-Internal References

- The cache owns LRU, exact-object discard, clear and separate resident/disk accounting. [1]
