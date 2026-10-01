# dashboard/src/data/submitRetention.test.ts

## Governing Overview

[data overview](overview.md)

## Purpose

Proves that submit retention stays bounded while preserving every live or unresolved request.

## Code Commentary

### Logic

The suite creates mixed active and settled histories/queues, verifies both 64-row settled-tail
limits, and confirms that compaction never discards protected phases even when they exceed the
normal display window.

### Invariants And Boundaries

- A retention test failure is a correctness issue when an active row disappears, not merely a UI
  pagination issue.
- The suite tests pure projection compaction; server ledger bounds are covered separately.

## Evidence

### Docs References

No Domain Documentation source is configured for this repository.

No configured live domain-documentation source was available.

### Repo-Internal References

- The system under test defines protected phases and settled-tail bounds. [1]

### Cross-Repo References

No meaningful cross-repo references found.

This is a repository-local unit suite.
