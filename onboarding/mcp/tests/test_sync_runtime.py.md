# test_sync_runtime.py

## Governing Overview

[overview](overview.md)

## Purpose

Checks sync-runtime target replacement removes stale files and excludes cache directories. The
current target roster is exactly `benchmarks`, `providers` and `system`, confined
to MCP package data rather than harness starter directories. The missing-canonical-source case
refuses to call two absent trees synchronized and accepts matching present trees.
These are temporary-tree fixture assertions, not proof that installed runtime projections have
just been refreshed.


## Code Commentary

### Logic

The current evidence boundary is the source-listed behavior below. The retained behavior and its fixture limits, described above, govern this card.

### Conventions

The table lists retained test definitions, not collected parametrized or subtest counts.
Inspect the cited setup and collaborators before treating a focused result as end-to-end evidence.

### Invariants And Boundaries

Preserve exact refusal, identity, and cleanup assertions rather than adding overlapping helper
cases. Coverage percentages are diagnostic and production CRAP 20 prompts review; neither implies
an obligation to restore removed cases. Full suites and whole-candidate review remain master-end
work. This source inspection does not claim a newly executed test or acceptance result.

### Todos

No additional implementation scope is opened by this memory reconciliation.

## Evidence

### Docs References

The repository has no configured Domain Documentation source. These claims concern its own test
fixtures and assertions, so the exact retained source is the direct evidence.

No external domain claim is required.

### Repo-Internal References

Each current definition below can be inspected in the exact source file.

- Sync target replaces target with source tree [1]

- Default targets only write to mcp package data [2]

- A missing canonical source is never reported in sync [3]

### Cross-Repo References

This card establishes test behavior, not a separate cross-repository protocol or live installation.

No external evidence is needed for these assertions.
