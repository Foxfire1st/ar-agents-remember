# dashboard/src/panels/review/codeFacts.ts

## Governing Overview

[dashboard/src/panels route overview](../overview.md)

## Purpose

Matching leaf-wide code facts without prefetch.

## Code Commentary

matchingTreeRead admits a trees result only if any requested comparison number matches. codeFacts returns an invariant-key map only for state facts; absent/unavailable never becomes an empty successful map. codeChangesCount counts unique outlined unchanged invariants with established implementation, not changed records or family occurrences twice. Summary states ellipsis, unavailable or C code changes. CodeFactsScrollAnchor snapshots list and ancestor positions before same-comparison count changes and restores them after mutation, without focus/selection. useCodeFactsNotice announces each comparison/count key through its caller. No requests, storage, roster or subject prefetch occur.

## Invariants And Boundaries

This is the inspected source contract, not an execution certificate. Parent and direct callers retain authority for identity, reads and state.

## Evidence

- Matching leaf-wide code facts without prefetch: `matchingTreeRead` owns the described branch. [1]
- Matching leaf-wide code facts without prefetch: `codeFacts` owns the described branch. [2]
- Matching leaf-wide code facts without prefetch: `codeChangesCount` owns the described branch. [3]
- Matching leaf-wide code facts without prefetch: `codeChangesSummary` owns the described branch. [4]
- Matching leaf-wide code facts without prefetch: `CodeFactsScrollAnchor` owns the described branch. [5]
- Matching leaf-wide code facts without prefetch: `useCodeFactsNotice` owns the described branch. [6]

