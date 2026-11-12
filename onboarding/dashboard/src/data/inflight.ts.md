# dashboard/src/data/inflight.ts

## Governing Overview

[data overview](overview.md)

## Purpose

Provide per-key single-flight ownership for idempotent dashboard boot reads without becoming a cache.

## Code Commentary

### Logic

Concurrent callers receive the first pending promise for a key. The promise's identity-guarded `finally`
removes only its own slot after success or rejection, allowing later reads to issue a fresh request.

### Conventions

Callers supply the async read and are responsible for an abort-capable transport bound. The retained production caller is the File Viewer repository catalog; earlier terminal/catalog-poll examples are historical after their retirement.

### Invariants And Boundaries

Sharing a promise shares both result and rejection. This module has no timeout and no value cache; adding
one would blur its ownership with a caller's cache policy.

### Todos

None.

## Evidence

### Docs References

No Domain Documentation entries are configured in this memory worktree's source registry.

No relevant external documentation is configured.

### Repo-Internal References

- The map shares a pending promise and releases it by identity on settle. [1]

- The live repository catalog fetchRepos uses shareInflight for its request; no removed terminal catalog is a current consumer. [2]

- The retained File Viewer repository-catalog read shares its in-flight callback and bounds its fetch; removed terminal/catalog-poll callers are not current consumers. [4]

### Cross-Repo References

No meaningful cross-repository references found.

- This is repository-local browser state coordination. [3]
