# mcp/src/agents_remember/application/knowledge_worklist/classification_context.py

## Governing Overview

[application route overview](../overview.md)

## Purpose

Share one worklist run’s already-computed classifier, exact candidate side and path placements with reviewer projections without changing the serialized gate worklist.

## Code Commentary

`classification_run` binds a request-scoped `WorklistClassification` through a ContextVar and restores the previous binding on exit, then clears this owner’s classifier, candidate, pairing and paths even after failure. `share_classifier` and `share_path` are no-ops outside that scope. Path facts retain each actual hunk and per-side intersecting entry IDs plus resolved placements. These are gate-mapped placements, not reviewer attribution: the reviewer must still require the entry’s recorded blob to equal that side’s actual blob. This is reference/context cleanup, not rollback of code or memory mutations, and no cache or serialized second classifier is introduced.

## Evidence

### Docs References

No Domain Documentation source is configured for this repository. Requirement packets are task authority, not an implementation proof or a fresh acceptance.

### Repo-Internal References

- One request owner holds the classifier, exact candidate, pairing and computed paths. [1]
- Exit restores context and releases the run’s held references on success or failure. [2]
- Path facts distinguish gate placements from exact-blob reviewer attribution. [3]
