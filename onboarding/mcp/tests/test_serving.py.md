# test_serving.py

## Governing Overview

[Tests overview](overview.md)

## Purpose

Protects dashboard-serving behavior, including the existing two publication operations: a subscription cannot lose a projection interleaved with its initial snapshot, and HTTP ETag revalidation returns 304 until content changes. The broad historical SSE, simulation, actions and CLI inventory was removed; this card makes no current coverage claim for those paths.

## Background owner regressions

The retained subscription-gap and ETag operations are joined by native nested atomic-write delivery despite a polling override, completed-tick rest and retained pending domains, success/failure/prime completion ownership, two-size historical-zero-probe eligibility and reopen behavior, and honest failed finishing observations with no recurring repair. These are focused owner tests; installed CPU/lag, process isolation and whole-product acceptance remain separate evidence.


- The real native watcher observes the nested atomic rename. [3]
- Work/rest notifications and rest bounds share one timeline. [4]
- Terminal history and one in-flight finishing observation are distinguished. [5]
- A failed finishing attempt stays honest missing and never retries history. [6]

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

The volatile-only ETag negative assertion follows publication of the exact new projection object by the real projector. The held ETag and 304 are checked after that positive publication boundary instead of after several assumed ticks.

## Evidence

### Docs References

The repository has no configured Domain Documentation source. These claims concern its own test
fixtures and assertions, so the exact retained source is the direct evidence.

No external domain claim is required.

### Repo-Internal References

Each current definition below can be inspected in the exact source file. Historical references
to removed methods are superseded by this current inventory.

- Snapshot subscription cannot lose an interleaved projection [1]
- Etag 304 cycle then new etag on content change [2]

### Cross-Repo References

This card establishes test behavior, not a separate cross-repository protocol or live installation.

No external evidence is needed for these assertions.

- The unchanged ETag is checked after the volatile-only projection was actually published. [7]
