# mcp/src/agents_remember/application/knowledge_reader/timeline_spill.py

## Governing Overview

[application route overview](../overview.md)

## Purpose

Store one oversized immutable event sequence on anonymous process-private temporary disk, with offsets on disk rather than an event-sized resident index.

## Code Commentary

`SpilledEvents` owns two unbuffered `TemporaryFile` handles: concatenated event bytes and big-endian 64-bit offsets, including the final endpoint. It checks zero link count and refuses non-anonymous backing. Construction uses `ExitStack` for failure cleanup and checks short writes. Reads lock the seek/read pair, verify complete bounds and event bytes, and materialize only requested indices/slices. `storage_bytes` counts data plus offsets; `retained_bytes` prices the resident handles/metadata/lock and allowance. A weak-reference finalizer closes both handles at last ownership release, allowing a page already holding the sequence to finish after eviction or clear; the OS reclaims anonymous backing on process termination. The admitted disk cost has no per-history cap, and no repository, coordination-tree or persisted-store pathname is written.

## Evidence

### Docs References

No Domain Documentation source is configured for this repository. Requirement packets are task authority, not an implementation proof or a fresh acceptance.

### Repo-Internal References

- Construction checks anonymity, keeps offsets on disk, bounds retained metadata and validates each requested read. [1]
- Final-owner cleanup closes both backing handles even if one close fails. [2]
- Short temporary-backing writes raise a read-path failure rather than silently truncate history. [3]
