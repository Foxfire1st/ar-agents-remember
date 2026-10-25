# mcp/tests/test_task_doc_structural_publication_l2.py

## Governing Overview

[Tests overview](overview.md)

## Purpose

Checks exact JSON and Markdown source-set binding for structural task publication. Drift on either representation refuses an attach; a completed detach permits a later exact absence-bound create without changing unrelated membership. The test fixtures preserve compare-and-swap authority rather than trusting a rendered title.

## Code Commentary

### Logic

The detach-first/create-later case delays the background `run_task_doc_call` before delegating to the real call; the main-thread detach bypasses that delay. Its publication wrapper separately asserts that source snapshots contain the selected master JSON but not the sprint JSON, then delegates without waiting. After detach changes sprint membership to `master-a`, release permits create; the case asserts create succeeds and that membership remains unchanged. The wait is therefore before call compilation, not a pause of an already-captured publication. These are declared concurrency assertions, not a new run result.

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

- The background native call is delayed before delegation while main-thread detach proceeds; the publisher checks the accepted source set and the later create preserves detached sprint membership. [4]


### Docs References

The repository has no configured Domain Documentation source. These claims concern its own test
fixtures and assertions, so the exact retained source is the direct evidence.

No external domain claim is required.

### Repo-Internal References

Each current definition below can be inspected in the exact source file. Historical references
to removed methods are superseded by this current inventory.

- Attach refuses json side drift across selected master batch [1]
- Attach refuses markdown side drift across selected master batch [2]

- Detach first allows later exact absence bound create [3]


### Cross-Repo References

This card establishes test behavior, not a separate cross-repository protocol or live installation.

No external evidence is needed for these assertions.
