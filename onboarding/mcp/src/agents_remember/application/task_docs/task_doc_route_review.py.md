# mcp/src/agents_remember/application/task_docs/task_doc_route_review.py

## Governing Overview

[application overview](overview.md)

## Purpose

Route-review binding machinery for the `task_doc` tool, facade-extracted from
`application/task_doc_tools.py` (L16-R6) so the facade stays under the file-size cap. It owns the
call-level knobs (`TaskDocCall`), the policy gate for branch-addressed direct execution
(`_enforce_branch_addressed_policy`), the leaf/series contract binding behind
`record_route_review` (`_RouteReviewBinding`, `_record_route_review_bound`,
`_require_route_review_binding`), and the route-review authority rule
(`_enforce_route_review_authority`). The facade re-exports the names its callers import (same
pattern as `task_reopen.py`). Since 260831-CCR (commit `99dc249b`) the recorders pass the exact
resolved leaf document (a `ResolvedTaskDocument` built from `document_ref(contract,
selected_path)`) into `build_route_review`, so the stamped review binds the canonical
`task-intent/v1` digest to the exact candidate document.

## Code Commentary

### Settings and record-only seams

`review_settings_limit` loads `orchestration.loops.defaults.maxRounds` afresh and translates a settings refusal to `review-settings-unreadable`. `_begin_task_review_bound` passes the selected number to the transition. `candidate_root_for_review` selects the contract memory worktree or configured memory root for memory reviews; code/default still prefers an existing leaf code worktree and otherwise uses the configured repository root; unresolved identity cannot admit a same-round result. Generic and route recorders pass both the settings limit and authority-resolved identity. `_state_payload` takes `candidateTree` from the route builder, not from caller route evidence.


### Logic

`TaskDocCall(dry_run, branch_addressed)` are call-level knobs, not a task edit. Ordinary record_route_review uses the exact leaf enclosure. Branch-addressed review opts in for the exact canonical task_name/slug subTask, requires its current readable external grant, and uses the exact task-root series contract. Missing/unreadable authority names that leaf and the grant givers, never a settings switch. Review evidence still binds the selected document intent and the exact contract mode; create/replace cannot author it. A grant does not waive atomic-child review policy.

`_RouteReviewBinding` captures the contract, task root, exact selected path and branch-addressed opt-in. `_record_route_review_bound` requires a review object and refuses memory kind: memory publication uses record_review with reviewKind=memory. For a master it requires the canonical series/task.json binding and calls `build_master_route_review`; for a leaf it enforces exact leaf or sanctioned branch-addressed binding, rejects atomic-child route review, and calls `build_route_review` with the exact `ResolvedTaskDocument`. Both branches pass the plane-stamped route candidate and independently resolved candidate identity into the shared fixed-list transition, then revalidate the whole document. The legacy positional `_record_route_review` preserves the call shape and delegates to the same binding form.

`_require_route_review_binding` is the L16-R9 error-dialect owner: a missing binding names the
recovery ("re-stamp the series contract (series-contract.md) or use branch_addressed=true for
direct execution"), branch-addressed mode requires the task-root series contract and a target
inside the task root, and the non-branch path requires the leaf worktree contract and resolves the
exact terminal leaf document (`resolve_terminal_leaf_doc`, asserted-path equality).
`_enforce_route_review_authority` forbids `create` from authoring route-review evidence and
`replace` from changing it — both must route through `record_route_review`.

### Conventions

One shared binding/authority implementation consumed by the facade; no duplicated validators.
Errors are `TaskDocError` (an `AgentsRememberError` subclass) so the tool surface keeps its typed
dialect.

### Invariants And Boundaries

- `branch_addressed` is exact per contract kind: a leaf contract with `branch_addressed=true`
  refuses ("requires the task-root series contract") and a series contract without it refuses
  ("requires the leaf worktree contract... use branch_addressed=true"); no silent cross-mode.
- Live canonical-leaf grant and per-call branch opt-in are both enforced; an open direct sibling refuses.
- Route-review evidence can only be stamped through this machinery; `create`/`replace` cannot
  author or change it.
- A recorded review always binds the current canonical task intent of the exact selected leaf
  document; a legacy or missing-intent document cannot be stamped as current.
- This module validates and stamps; it does not perform review or mutate source.

### Todos

None recorded.

## Current Contract

Explicit reviewKind=memory selects the independent memory candidate: contract.memory_worktree when present, otherwise the configured memory root. Default/code still selects an existing leaf code worktree or repository root. `candidate_identity_for_review` validates the lane before resolving its actual byte identity. `with_review_lane_result` retains present memory state and labels review mutations, with memory-specific updated phrases. Route evidence stays code-only: memory results use record_review and are refused by record_route_review before route stamping. Generic create cannot seed memoryReviewState, and replace cannot change or erase it. Existing branch grants, exact task binding and route/intent authority remain separate.


The governing workflow opens an independent memory review after CODE PASS on the same task using begin_review/record_review with reviewKind=memory. It has its own immutable baseline and shrinking IDs, under the same settings limit and extra-round approval rule, and never resets code reviewState. The signed rollout applies only to memory reviews begun after L88 lands; already-underway reviews (L168, L56, L57, L59) finish with their sealed-report workflow, with no migration/backfill. This describes the candidate contract, not a claim that the serving build already supports it.

This account is bound to the candidate source, not a claim of a running serving build or a fresh execution/acceptance verdict. Existing historical accounts remain historical.

## Evidence


- Worker/Curator typed review census, record-only exclusion and unknown history. [10]
- Reason admission, threshold and differing-harness/model inheritance boundary. [11]
- Record-only memory identity comes from memory authority, never the sibling code root. [12]
- File-local implementation of the stated contract; caller-owned effects and governing workflow are separate evidence. [13]
- File-local implementation of the stated contract; caller-owned effects and governing workflow are separate evidence. [14]
- File-local implementation of the stated contract; caller-owned effects and governing workflow are separate evidence. [15]
- File-local implementation of the stated contract; caller-owned effects and governing workflow are separate evidence. [16]

### Docs References

No configured Domain Documentation source applies.

### Repo-Internal References

- Call-level knobs and the branch-addressed policy gate. [1]
- The binding form that records a review over the resolved candidate document and re-validates. [2]
- The legacy positional recorder passing the resolved leaf document. [3]
- Exact-binding refusal with the L16-R9 recovery dialect. [4]
- The route-review authority rule (create/replace cannot author or change evidence). [5]
- The stamping owner it delegates to; now takes the resolved candidate document. [6]
- The typed candidate ref derived from the selected path. [7]
- The facade that dispatches into this module. [8]

### Cross-Repo References

No meaningful cross-repository reference applies.

## CCR-R02@v2 Task-Intent-Bound Reviews

Per `requirements/CCR-R02-v2-normative-task-intent-identity.md`, a route review is evidence bound
to normative task intent: the recorders now pass the exact `ResolvedTaskDocument` so
`build_route_review` stamps the current `task-intent/v1` digest, and a review whose intent is
missing/stale refuses. The application seam itself performs no review and owns no intent
semantics. Part of the landed L25 candidate `99dc249b`.

- Branch review is canonical-leaf opt-in under the live grant, not a runtime setting. [9]
