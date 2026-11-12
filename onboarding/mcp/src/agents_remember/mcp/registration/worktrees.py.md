# mcp/src/agents_remember/mcp/registration/worktrees.py

## Governing Overview

[registration route overview](overview.md)

## Purpose

`register_worktree_tools(server, config)` declares the **working half** of a worktree-backed task:
`worktree_start`, `worktree_enclosure_adopt`, `worktree_attach`, `worktree_status`, `worktree_sync` and
`worktree_pause`. The landing half (closeout, integrate, cleanup, abandon) is a
separate family in `closeout.py`, and `worktree_checkpoint_landing` — the explicitly requested
**publication** of an unfinished master — belongs to that half, not this one. The module docstring
says "create, re-attach, observe, sync, stop" for exactly that reason.

## Code Commentary

Worktree declarations use light worktree_tool_requests types and lazily access existing payloads; enclosure adoption resolves its request class with its payload at call time.

### Current Contract

The flat registrars retain their existing locator/provider/transaction owners while compact descriptions name outcomes and the longer reference. Status can include a copied-file drift notice. Current sync accepts contract_path, memory_sync_choice, resolution_action, dry_run and sync_source; it packs the admitted continue/cancel action and the repository-default source into one SyncResolutionInput. Content resolution is authored/staged in files, not a knowledge_resolution/reconcile input. Generic pause state/next wording invents neither a resume verb nor publication authority. The current worktree_sync source description is 600 characters, at the unchanged 600 limit; its state list, next-call/log guidance, pre-sync review, raw-memory-merge boundary, landing/fast-forward judgments and the sync_source="repository-default" line remain. Description compression changes neither signature nor forwarding behavior and is not live registration evidence.

### Logic

`worktree_start` is the widest declaration in the family and splits into the three parameter objects
its application entry point takes — who the task is, what it is cut from, and how the start runs:

- `TaskIdentity(repo_id, task_name, worktree_name, leaf_id, parent_task, workflow_kind)` —
  `workflow_kind` defaults to `light-task` (the other value is `chat-task`).
- `TaskBases(source_branch, work_branch, memory_mode, memory_choice, stale_base_choice)`.
- `StartExecution(dry_run, skip_provider_setup, retry_provider_setup)`.


Worktree attach re-attaches to an existing task contract without mutating Git and reports its addressed state/next call. Its current signature has no on_unsaved save/discard operand or public resolve_context fallback. Status keeps actual lifecycle/dirty/next-step/provider information through the retained contract owner.


### Invariants And Boundaries

- Flat signature, packing in the body — `TaskIdentity`/`TaskBases`/`StartExecution` and `TaskRef`
  belong to the application entry point boundary.
- `worktree_start` and `worktree_sync` are mutating and register `dry_run=False`; `worktree_attach`
  and `worktree_status` are read-only and take no dry-run flag.
- Contract creation, git mechanics, provider setup, and lifecycle promotion live in
  `application/worktree_tools.py` and the `worktrees/` package.
- Registration publishes the shared closed memory-choice, continue/cancel and sync-source (`repository-default`)
  vocabulary; no free-string compatibility parameter or alternate sync tool is registered.

## Evidence

### Docs References

No Domain Documentation source is configured for this memory root.

### Repo-Internal References

- Current pause declaration is contract-addressed, publishes nothing, hands control back and identifies separate checkpoint publication. [1]

- Current public sync takes five arguments and packs the continue/cancel action and the repository-default source into one SyncResolutionInput; there is no knowledge_resolution argument. [2]

- **Retained historical source account — superseded by the current contract:** The start payload forwards task identity, bases and execution configuration to the application owner. [3]
- **Retained historical source account — superseded by the current contract:** The attach payload forwards the requested worktree attachment to the application owner. [4]
- **Retained historical source account — superseded by the current contract:** The status payload reads status through the application owner. [5]
- **Retained historical source account — superseded by the current contract:** The sync payload forwards the paired resolution value to the application owner. [6]
- **Retained historical source account — superseded by the current contract:** The identity parameter object `TaskIdentity` (repo_id, task_name, worktree_name, leaf_id, parent_task, workflow_kind defaulting to `light-task`), defined in the application request boundary. [7]
- The bases parameter object `TaskBases` (source_branch, work_branch, memory_mode, memory_choice, stale_base_choice), defined in the application request boundary. [8]
- **Retained historical source account — superseded by the current contract:** The execution parameter object `StartExecution` (dry_run, skip_provider_setup, retry_provider_setup), defined in the application request boundary. [9]
- **Retained historical source account — superseded by the current contract:** `TaskRef` — the shared task locator attach and status pack. [10]

- The pairing this registrar performs: worktree_sync builds SyncResolutionInput(action=resolution_action, source=sync_source) from the shared continue/cancel and repository-default vocabulary. [11]

### Cross-Repo References

No meaningful cross-repository reference applies to this repository-owned registration surface.

## L23 Final Candidate Disposition

Public worktree registrations remain task-addressed and immediate-returning. Durable operation
identity, candidate trees, worker processes, and recovery state stay behind the application/service
boundary and are not added to the tool schema.


## 260821-CLIVE-L2 Current Contract

The current source seams include `register_worktree_tools`. The public schema/composition layer exposes task-addressed controls plus explicit legacy and enclosure-adoption routes without private operation ids. Registration and payload building do not own journal state or compatibility decisions.

### Reconciled Source Evidence

- Current register_worktree_tools registers the existing start, address, observation and stop owners. [12]



## 260831-LOCR-L37 Stop Registration

`_register_worktree_stop_tools(server, config)` is the fourth registrar in the family and declares
one tool, `worktree_pause(contract_path)`. `register_worktree_tools` calls the four in order: start,
address, observation, stop.


The signature is flat and single-argument (`contract_path`), like every other tool on this route, so
the published JSON schema stays a flat object. `mcp/tests/test_tools.py` pins its "PAUSE an atomic master" and
"Publishes NOTHING" wording.

**Two verbs, two registrars, two halves.** This file registers the stop; `closeout.py` registers the
publication. Neither is reachable through the other.

## 260915-KS-L40 The Authored Sync Resolution On The Public Surface


Current sync qualification: the flat signature is contract_path, memory_sync_choice, resolution_action, dry_run and sync_source. It builds SyncResolutionInput(action=resolution_action, source=sync_source); continue/cancel resolve retained file conflicts and sync_source="repository-default" pulls each repository's default branch. Memory merges belong to this route, and incoming converted fast-forwards validate before refs move. There is no knowledge_resolution argument and no reconcile action (`SyncResolutionAction` is `continue` or `cancel`).


- Current sync accepts contract_path, memory_sync_choice, resolution_action, dry_run and sync_source and packs the continue/cancel action and the repository-default source into one SyncResolutionInput; its compact description is 600 characters with whitespace collapsed, at the 600 limit. [13]

- Worktree declarations use light worktree_tool_requests types and lazily access existing payloads; enclosure adoption resolves its request class with its payload at call time. [14]
