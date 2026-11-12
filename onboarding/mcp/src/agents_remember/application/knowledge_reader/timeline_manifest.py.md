# mcp/src/agents_remember/application/knowledge_reader/timeline_manifest.py

## Governing Overview

[application route overview](../overview.md)

## Purpose

Freeze a complete timeline into an immutable, byte-accounted manifest for page reuse.

## Code Commentary

`TimelineManifest` holds source-state bytes, all ordered event bytes (or `SpilledEvents`), a complete manifest digest and retained-resident weight. `freeze_timeline` canonicalizes the source/events, accounts the manifest, event tuple/bytes, digest, complete key and 512-byte memo allowance once at admission, and spills events above the 8 MiB threshold. Spill offsets are on disk too. Disk cost is one cached history’s complete event bytes plus offsets with no per-history cap. This is retained-resident accounting, not a total-process, transient-build or in-flight-memory ceiling; full materialization exists during a miss. No event is truncated to fit the cache.

## Evidence

### Docs References

No Domain Documentation source is configured for this repository. Requirement packets are task authority, not an implementation proof or a fresh acceptance.

### Repo-Internal References

- The immutable manifest separates complete ordered storage, digest and resident weight. [1]
- Admission computes resident accounting once and substitutes anonymous spill storage only for oversized events. [2]

- The accounted resident-weight cache budget is 8 MiB. [3]
