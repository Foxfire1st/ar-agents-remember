# mcp/src/agents_remember/worktrees/modules/finalize_task_documents.py

## Governing Overview

[Worktree operation modules overview](overview.md)

## Purpose

The exact task-document completion targets of `lifecycle_finalize_task` and their atomic publication. `finalize.py`
orchestrates cleanup and the result; this module proves which documents finalization completes and writes them. It was
split out of `finalize.py` to keep that file under the size limit, and it also owns the series case: finalizing a master
completes the master's own document and any proven typed or correlated seat row, reporting absent or ambiguous correlation as skipped unless a parent was asserted.

## Code Commentary

### Logic

`FinalizeArgs` carries the contract path, the optional document assertions (`task_doc_path`, `master_doc_path`,
`subtask_number`), `dry_run` and provider teardown. `_resolve_task_targets` dispatches on the contract kind. A leaf
contract resolves its one leaf document and its immediate parent row through `_resolve_parent_target` (the named master,
else the folder's `task.json` by the master sync's rule, with the checks documented on the finalize card); a series
contract resolves through `resolve_series_targets`, and refuses a leaf-document assertion.

`resolve_series_targets` reads the master's own document and uses `sprint_census` to find commanding sprints.
An unreadable census document whose text names this master or several commanding sprints refuses by name.
With no commanding sprint, the master alone is selected unless a parent was asserted. With one, linkage is
validated and `master_rows` selects one typed row or, without a typed row, one correlated legacy seat row.
No row or ambiguous correlated seat rows are linkage facts: without a parent assertion the master alone
is selected and the sprint row is reported as skipped; an asserted parent refuses.

Only admitted canonical existing unreadable sibling paths are omitted from the temporary validation view
and reported as facts. Stored membership, rows, graph nodes and bytes remain unchanged. Missing canonical
members, duplicate typed references, foreign references, unbound titles or IDs and the master's own
unreadable document remain named refusals. An unbound title or ID is repaired using the intended master's
canonical folder and matching typed or execution-graph reference.

`reconcile_series_documents` rechecks the captured sources and previews or atomically publishes the
selected documents: the master alone, or the master and proven sprint row together. The master becomes
`Completed`; a selected sprint row becomes `Completed` under the existing demotion rule. When no single
row stands for the commanded master, the result reports `sprint.state="skipped"`,
`reason="sprint-holds-no-single-row-for-this-master"` and its `linkageFact`, without writing the sprint.

The leaf path (`_reconcile_task_documents`, `_leaf_completion_candidate`, `_parent_completion_candidate`,
`_require_finalize_sources_current`) is the unchanged logic that was moved here.

### Conventions

- Every refusal raises `FinalizeTaskDocumentError`; `finalize_result` turns it into
  `task-document-resolution-blocked` or `task-document-publication-blocked` before cleanup or without a task change.
- A dry run previews the same documents and writes nothing.

### Invariants And Boundaries

- Finalizing a master completes its document and any proven sprint row, and never archives its folder.
- The selected master-only or master-plus-sprint documents are published together or not at all.
- A broken sprint linkage refuses before any write, in a dry run as well.

## Evidence

- Series finalization selects the master and any proven typed or correlated seat row; absent or ambiguous correlation is reported as skipped unless a parent was asserted. [1]
- Targets are resolved by contract kind. [2]
- The selected master-only or master-plus-sprint documents are previewed or published atomically after source rechecks. [3]
- A selected sprint row is completed, and a Completed sprint with unresolved rows is demoted. [4]
- Static cases distinguish a correlated seat row, absent or ambiguous correlation reported as skipped, and preserved linkage refusals. [5]
