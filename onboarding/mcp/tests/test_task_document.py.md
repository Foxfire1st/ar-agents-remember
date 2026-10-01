# test_task_document.py

## Governing Overview

[Tests overview](overview.md)

## Purpose

Checks JSON-primary task rendering and persistence: progress counts parent and child obligations, current-step selection is deterministic, light/master golden projections and extension fields retain content, pipes/newlines/fences render correctly, and writes round-trip without temporary residue. A later batch failure removes newly published earlier files. Historical application and tool-registration assertions are not all present here.

## Code Commentary

### Logic

The current evidence boundary is the source-listed behavior below. Earlier coverage claims in
history describe prior populations and must not be used to recreate removed tests or claim they
still run. The retained behavior and its fixture limits, described above, govern this card.

The shared `ApplicationTests` fixture gained a master prerequisite in 260913-LCA-L5:
`_create` (`:476-496`) now calls `_ensure_parent_master` (`:498-501`) before authoring its leaf, and
`_ensure_parent_master` writes the parent master through `_create_parent_master` (`:503-520`) only when
it is absent. This is not incidental scaffolding: the task-doc authoring plane refuses a leaf document
authored under a task root with no master document at all, because nothing would ever bind the leaf's
derived `seriesContractPath` and `enclosures[]` (see the `application/task_docs/task_doc_tools.py`
card). The helper keeps every leaf operation in this module on the flow the plane allows — master
document present, series contract not yet bootstrapped — rather than weakening the refusal.

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

- The leaf-operation fixture's master prerequisite: every `_create` ensures a parent master exists before authoring its leaf, which is the authoring flow the plane allows. [1]
- Progress counts every declared parent and child [2]
- Current step prefers active then first unfinished then none [3]
- Golden small light doc [4]
- Decision cell escapes pipe and newline [5]
- Code example fence preserves blank lines [6]
- Real subtask extensions round trip content complete [7]
- Golden master [8]
- Write then read roundtrips and leaves no tmp [9]
- Batch failure removes new files published before later document [10]

### Cross-Repo References

This card establishes test behavior, not a separate cross-repository protocol or live installation.

No external evidence is needed for these assertions.
