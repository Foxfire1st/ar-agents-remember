# test_sync_runtime.py

## Governing Overview

[Tests overview](overview.md)

## Purpose

Checks sync-runtime target replacement removes stale files and excludes cache directories. The
default target roster — which since 260915-CAPS-L9 includes the `eve-runtime` target — is confined
to MCP package data rather than harness starter directories. Since 260915-CAPS-L9 it also pins the
**per-target** ignore rule (only the eve application target ignores `node_modules`/`.eve`/
`.output`/`.vercel`) and the refusal to report an absent canonical source in sync. It is an actual
temporary-tree copy test, not proof that installed runtime projections have just been refreshed.

## Code Commentary

### Logic

The current evidence boundary is the source-listed behavior below. Earlier coverage claims in
history describe prior populations and must not be used to recreate removed tests or claim they
still run. The retained behavior and its fixture limits, described above, govern this card.

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

Each current definition below can be inspected in the exact source file. Historical references
to removed methods are superseded by this current inventory.

- Sync target replaces target with source tree [1]
- Default targets only write to mcp package data [2]
- A missing canonical source is never reported in sync [3]
- Only the eve application target ignores machine-local trees [4]

### Cross-Repo References

This card establishes test behavior, not a separate cross-repository protocol or live installation.

No external evidence is needed for these assertions.
