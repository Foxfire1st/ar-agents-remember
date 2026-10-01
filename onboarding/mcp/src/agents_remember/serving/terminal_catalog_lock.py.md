# mcp/src/agents_remember/serving/terminal_catalog_lock.py

## Governing Overview

[overview.md](overview.md)
## Purpose

Cross-process catalog writers are fully serialized across one read, sweep body, and one write; list/get are lock-free atomic readers.

## Code Commentary

### Logic

Cross-process catalog writers are fully serialized across one read, sweep body, and one write; list/get are lock-free atomic readers.

### Invariants And Boundaries

Canonical lifecycle doctrine owns canonical skill content; generated copies are synchronization outputs. Dispatch proof remains exact-session and fail-closed.

## Evidence

### Docs References

No relevant documentation was configured in the resolved source registry; task artifacts and the final candidate are the direct evidence.

### Repo-Internal References

Worker source inventory, reviewer verdict, and governing route overview.

### Cross-Repo References

No meaningful cross-repo references.
