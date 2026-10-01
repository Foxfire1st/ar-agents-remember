# mcp/tests/test_task_documents_graph_projection.py

## Governing Overview

[Tests overview](overview.md)

## Purpose

Checks rendered graph projection joins actual master documents to segment titles, wave/predecessor facts and frontier state. Duplicate local leaf numbers keep master-qualified titles rather than colliding in a flat lookup. An `abandoned` master reads `abandoned` and stops gating the segment that waited on it. Projection is display data, not independent execution authority.

Since 260913-LCA-L10 it also pins the projection's **index reachability** contract: a master's sub-task
row must resolve to a projected document whatever build wrote the leaf's durable JSON, while a genuinely
broken document is still withheld. `SubTaskIndexReachabilityTests` drives that through the reader the
dashboard's own index rule uses, so a read edge that deletes unparseable documents fails here instead of
appearing in the UI as a row of dead text.

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

- Segmented master scenario projects titles and predecessors [1]
- An abandoned master reads `abandoned` and no longer gates its successor, whose frontier becomes ready [2]
- Duplicate local leaf numbers keep master qualified titles [3]
- The dashboard's own index rule, reproduced: a row drills in only when the pool holds a document in the master's own directory whose file stem is the row's `file`. [4]
- The reachability contract: a completed leaf written by a newer build stays reachable, an unstarted one stays reachable, and a broken document is still withheld. [5]

### Cross-Repo References

This card establishes test behavior, not a separate cross-repository protocol or live installation.

No external evidence is needed for these assertions.

## 260913-LCA-L10 Sub-Task Index Reachability

The module gained `_index_doc` (224-240) and `SubTaskIndexReachabilityTests` (243-343) with one case,
`test_completed_leaf_written_by_another_build_stays_reachable_from_the_index` (307-343). `_index_doc`
reproduces the dashboard's own index rule (`sliceForRef`): a master's sub-task row drills in only when
the projected pool holds a document in the master's own directory whose file stem is the row's `file`.
The case therefore asserts the exact property the projection owes every authored row, through
`read_task_documents`, rather than a proxy for it.

The fixture writes three rows over one temporary task root: `D-L1` completed, `D-L2` unstarted, and
`D-L3` whose master row points at a genuinely broken document. It then republishes the completed leaf's
durable JSON with one unknown field added at the step level — the skew the live incident carried — and
writes the broken document by **deleting a required field**. The assertions split by outcome:
`D-L1` (written by a newer build) resolves with `("01_DONE", "Completed", 1, 1)`, `D-L2` resolves as
before, and `D-L3` is `None`, i.e. still withheld. That third assertion is the fail-closed half: an
unknown key must not become "project anything".

Two mechanics a future reader must not "fix": the skewed payload is written with `Path.write_text`
rather than `write_task_doc`, because `write_task_doc` takes a validated `TaskDocument` and **must**
refuse a document carrying the unknown key — the direct write is what models another build's durable
output, not a workaround; and the unknown field is spelled `checkpoint` on the step, mirroring where the
live skew landed (`step.note`, `tasks/document.py:121`) without depending on a field this reader may
later learn.

The case is the module's only protection for the tolerant read edge: reverting the single
`extra_forbidden` condition fails exactly this case and nothing else.
