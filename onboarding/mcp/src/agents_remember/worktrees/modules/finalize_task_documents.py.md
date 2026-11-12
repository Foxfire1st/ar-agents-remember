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

Required leaf/master ownership is fail-closed: an absent contract-bound leaf/document, no folder master, or a master with no matching leaf row refuses before preparing completion/publication, with task_doc repair guidance. R55 rule9 supersedes the earlier standalone-success fallback. A valid series master without a commanding sprint may still complete its own document; that distinct path does not admit a masterless leaf or a missing task document. Named-parent/path checks and valid parent-row completion remain separate.

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

> **Retained historical source account — superseded by the current contract:**
> The leaf path (`_reconcile_task_documents`, `_leaf_completion_candidate`, `_parent_completion_candidate`,
> `_require_finalize_sources_current`) is the unchanged logic that was moved here.

Current leaf/master completion changes the own non-Completed document to Completed and stamps `completedAt` using local aware ISO time to seconds. An already Completed own document is returned unchanged: there is no timestamp backfill or log migration. The series-master path calls the same own-document helper. A selected parent row alone becomes Completed under the existing demotion rule; that row update does not stamp the parent completedAt. Neither helper appends a Finalize decision; all preexisting decision entries are retained. Kind/path/linkage/retired-row guards, exact captured-source rechecks, previews and publication ownership remain separate from the timestamp/log change. Named-parent resolution delegates to master_json_path_from_ref with the actual leaf id; ValueError is converted to FinalizeTaskDocumentError with the shared refusal text. This path guard neither discards L162 completion-time/decision preservation nor grants a parent-address fallback.

The leaf publication retains each owning `(path, document)` pair for the completed leaf and selected parent candidate. Preview and apply pass those pairs to the shared contract task-fact publisher, so a selected document is not silently rebound under the wrong task root. Completion timestamps, preserved decisions, exact-source validation and atomic publication retain their separate meanings above.

### Conventions

- Every refusal raises `FinalizeTaskDocumentError`; `finalize_result` turns it into
  `task-document-resolution-blocked` or `task-document-publication-blocked` before cleanup or without a task change.
- A dry run previews the same documents and publishes no task-document changes. This helper's document-state boundary does not remove the enclosing registered tool call's daily log or completed-call river record.

### Invariants And Boundaries

- Finalizing a master completes its document and any proven sprint row, and never archives its folder.
- The selected master-only or master-plus-sprint documents are published together or not at all.
- A broken sprint linkage refuses before any write, in a dry run as well.

## Evidence

- Missing leaf/master/row authority refuses with repair guidance rather than standalone completion. [6]



- Series finalization selects the master and any proven typed or correlated seat row; absent or ambiguous correlation is reported as skipped unless a parent was asserted. [1]

- Targets are resolved by contract kind. [2]
- The selected master-only or master-plus-sprint documents are previewed or published atomically after source rechecks. [3]

- Selected parent row becomes Completed after retired-row and exact-number checks, then existing unresolved-row demotion applies. Decisions and parent completedAt are not rewritten by row completion. [4]



- Retained survey concern: the former static correlated/absent/ambiguous-row evidence includes an obsolete Finalize-decision assertion and cannot establish current behavior. Current source selects targets as before, stamps own completion time once, and preserves own/parent decisions. No test was run or offered as current proof. [5]

- Leaf completion preserves each owning path/document pair for preview and publication. [7]
