# mcp/src/agents_remember/worktrees/integration/closeout/integration_reopen.py

## Governing Overview

[Governing route overview](overview.md)

## Purpose

Owns the policy that decides whether a closeout must reopen an already completed integration.

## Code Commentary

### Logic

Completed external-memory reopening compares the newly accepted memory-content commit with its previous value and tests that same commit against the recorded memory source branch. A cache refresh cannot reopen integration because it supplies no produced commit.

`preview_integration_reopen` projects whether dirty or prospective code/memory output would need
another plane-owned integration. `completed_integration_reopen` evaluates the exact produced code and
memory-content commits against the recorded source branches. It reopens only when new
content is not yet landed; a no-op or already-landed closeout preserves completed state.

The helpers keep code and external-memory decisions separate so coverage and failure evidence name
the affected leg directly. They inspect ancestry but never move a branch, mutate the contract, or
integrate output themselves; the closeout coordinator owns publication of the returned decision.

### Conventions

Accepted input, exact Git facts, and typed owner results stay distinct from disposable projections.

### Invariants And Boundaries

- Integration status changes only from exact produced-commit and source-ancestry facts.
- A memory-only settings closeout can reopen memory without falsely reopening unchanged code.
- Already-landed or no-op output leaves completed integration intact.
- This module decides; it never mutates Git, contracts, or lifecycle journals.

### Todos

None recorded for the ledger-retirement boundary.

## Evidence

### Repo-Internal References

The following current source boundaries establish the ledger-retirement behavior.

- `completed_integration_reopen` evaluates the two actual output commits against their source branches. [1]
- `_completed_memory_is_unlanded` tests changed memory content and ancestry of that same content commit. [2]

- Preview distinguishes prospective code and memory reopen effects. (`preview_integration_reopen`) [3]
- Completed output is evaluated per code and memory leg. (`completed_integration_reopen`) [4]
- Memory reopening requires changed content and an unlanded memory-content commit. (`_completed_memory_is_unlanded`) [5]

### Cross-Repo References

No additional repository is consulted; the admitted worktree contract supplies both repository
and source-branch identities.

No additional cross-repository evidence applies.

### Docs References

No external Domain Documentation source is configured for this slice. The current behavior is repository-owned and is supported by the source references below.

No configured external source applies.
