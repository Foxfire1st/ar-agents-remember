# mcp/src/agents_remember/worktrees/task_leaf_binding.py

## Governing Overview

[Worktrees overview](overview.md)

## Purpose

Resolve the canonical master-row to leaf-task binding used by lifecycle admission.

## Code Commentary

### Current Contract

Mutating recovery is offered only for an established safe leaf target: task_doc.replace carries repo_id, contract_path, the exact leaf slug and required fields. A parent task.json or unavailable safe slug yields file-repair prose/path without a guessed nextTool. The separate master-link-missing start/attach remedy retains its own authority. Observation reads canonical files, never the removed task_doc.get.

The current registration planner preserves an existing TaskLeafBindingError and normalizes another ValueError into that typed refusal before its caller proceeds.

### Logic

> **Retained historical source account — superseded by the current contract:**
> The resolver loads the exact parent task, identifies one child row, validates regular JSON/Markdown child sources, derives the canonical task reference and enclosure path, and supplies a source-CAS check for start. `plan_current_leaf_enclosure_registration` (`:178-202`) plans the leaf enclosure registration against the canonical parent row, and `require_current_leaf_enclosure_binding` (`:205-256`) is the admission gate start and closeout share.

### Invariants And Boundaries

> **Retained historical source account — superseded by the current contract:**
> - Parent row and child sources must name one exact leaf identity.
> - Missing, symlinked, non-regular, or contradictory sources fail closed.
> - Start revalidates the current task binding under the shared task-publication lock.
> - No path naming inference replaces the canonical row/source binding.
> - **Since 260913-LCA-L5 a doc with an exact enclosure address but no `seriesContractPath` refuses
>   by name.** `require_current_leaf_enclosure_binding` reads the registration plan's state and, when
>   the plan carries a candidate in state `master-link-missing`, raises `TaskLeafBindingError` with
>   status `task-enclosure-binding-master-link-missing` and names the route that actually binds the
>   field — "re-run worktree_start/worktree_attach so the start binding publisher writes this leaf
>   document's seriesContractPath, then retry closeout" — rather than reusing the `mismatched`
>   recovery ("run task_doc.replace against this exact leaf contract"), which could not have bound a
>   derived field. Before this change such a document read as `present` and passed silently. This is
>   a deliberate, load-bearing behaviour change, not an accident: it is what forced the two shared
>   fixtures that had been modelling the damage state to carry the derived fields `task_doc` stamps.

### Todos

None recorded.

## Evidence

### Docs References

No configured domain-documentation source applies to this repository-internal route.

### Repo-Internal References

- Binding models and resolution establish the canonical leaf identity through the shared pure task-domain owner. [1]
- Parent and child source readers enforce exact regular-file authority after canonical row/source derivation. [2]
- Start admission rechecks the same canonical composite binding before reserving lifecycle authority. [3]

- The registration planner this module delegates to, and the admission gate that now names the missing master link instead of reading it as present. [4]

- The typed facts carried by the new refusal, including the named recovery operation. [5]
- The planner whose `master-link-missing` state this gate reads. [6]

> Retained earlier citation wording: - The start/attach publisher that is the named recovery, and therefore the operation that actually binds the field. [7]


- The two shared fixtures that had to carry the derived fields once this refusal existed, because they were modelling the damage state. [8]


### Cross-Repo References

No meaningful cross-repository boundary is owned by this file.

## CCR-L42 current candidate

> **Retained historical source account — superseded by the current contract:**
> Leaf binding now resolves the canonical parent row to one exact JSON task document, plans enclosure registration, and returns typed repair facts before closeout. Missing or mismatched bindings fail closed without sibling scans or compatibility fallbacks.


- Mutating recovery is offered only for an established safe leaf target: task_doc.replace carries repo_id, contract_path, the exact leaf slug and required fields. A parent task.json or unavailable safe slug yields file-repair prose/path without a guessed nextTool. The separate master-link-missing start/attach remedy retains its own authority. Observation reads canonical files, never the removed task_doc.get. [9]


## Current source evidence


- Registration planning preserves or normalizes a typed binding failure before publication. [10]

- The start/attach publisher that is the named recovery, and therefore the operation that actually binds the field.  Historical anchor: `_publish_leaf_task_enclosure_binding`. Current start/attach publication calls delegate to `publish_start_task_facts` in `worktrees/start_task_publication.py`. [7]
