# mcp/tests/test_source_lineage.py

## Governing Overview

[Tests overview](overview.md)

## Purpose

Builds real Git repositories and canonical sprint/master/leaf contracts to check transitive code and memory lineage. Parent movement blocks the leaf; start and attach recheck exact source tips; sibling worktrees of the same repository remain legitimate. The lineage chain comes from task authority rather than caller-invented identifiers. `CloseoutSourceLineageHealTests` extends the same fixture to the closeout boundary, where a settleable stale break is now carried, an unprovable one escalates, a `dry_run` mutates nothing, and a retained sync conflict hands back both worktrees with their duties.

## Code Commentary

### Logic

The current evidence boundary is the source-listed behavior below. Earlier coverage claims in
history describe prior populations and must not be used to recreate removed tests or claim they
still run. The retained behavior and its fixture limits, described above, govern this card.

The closeout-boundary class covers both halves of the change: the plain fast-forward, the leaf that
owns its own commit, the unprovable-escalation and retained-conflict paths, the read-only preview,
and the parked-candidate cases (uncommitted carry and retained reapply conflict) whose transaction
detail is pinned in `test_sync_parked_candidate.py`.

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

- Leaf identity proves code and memory transitively [1]
- Organizational super move blocks the leaf boundary [2]
- Start rechecks exact source tips before start effects [3]
- Attach refuses before stale task context is resumed [4]
- Parent and leaf paths may be sibling worktrees of one repository [5]
- Lifecycle boundary requires the full transitive chain [6]
- The closeout-boundary class proves the self-healing source-lineage guard. [7]
- A plain fast-forward break is carried by the closeout boundary. [8]
- A `dry_run` closeout refuses with the preview duty and moves nothing. [9]
- A leaf that owns its own commit is carried (merge, not refusal). [10]
- An unprovable break escalates to the human developer. [11]
- A retained sync conflict hands back both worktrees and their duties. [12]
- A dirty (uncommitted) candidate is parked, carried, and returned by the closeout boundary. [13]
- A parked-candidate reapply conflict surfaces as `source-lineage-sync-conflict` with the candidate recoverable. [14]
- The moved-source integration guidance routes through the sync. [15]

### Cross-Repo References

This card establishes test behavior, not a separate cross-repository protocol or live installation.

No external evidence is needed for these assertions.
