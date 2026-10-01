# mcp/src/agents_remember/application/task_docs/task_doc_discard.py

## Governing Overview

[governing route overview](overview.md)

## Purpose

Implement audited discard of a planning leaf proven never to have started.

## Code Commentary

### Logic

The module validates a nonblank discard request, resolves the exact parent/child binding, obtains the centralized unstarted-evidence proof, publishes a versioned parent audit, and removes the exact child JSON/Markdown bytes in one rollback-safe task transaction. Lost-response retries resume only against the recorded source digests and modes.

### Invariants And Boundaries

- Discard never marks the leaf or its steps Completed.
- Any enclosure, door, operation, worker, review, commit, progress, or unreadable execution evidence refuses the mutation.
- Changed or non-regular child bytes are preserved; replay removes only the exact audited sources.
- The ordinary task-first projection invalidation/rebuild effect follows successful publication.

### Todos

None recorded.

## Evidence

### Docs References

No configured domain-documentation source applies to this repository-internal route.

### Repo-Internal References

- The request and candidate models bind discard input to exact source evidence. [1]
- The apply and resume paths publish the parent audit and exact child removals. [2]
- Replay removal is guarded by recorded digest, size, and regular-file mode. [3]

### Cross-Repo References

No meaningful cross-repository boundary is owned by this file.
