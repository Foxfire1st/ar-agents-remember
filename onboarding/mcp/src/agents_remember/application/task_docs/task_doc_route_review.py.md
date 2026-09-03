# mcp/src/agents_remember/application/task_docs/task_doc_route_review.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/application/task_docs/task_doc_route_review.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-03T12:30:00+02:00 |
| lastVerifiedCommitHash | `99dc249bd507c20b09ece1169c2b1fa2af8e8c1b` |
| lastVerifiedCommitDate | 2026-09-02T05:53:10+02:00 |
| governingOverview | `overview.md` |

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

### Logic

`TaskDocCall(dry_run, branch_addressed)` are call-level knobs that are not part of the edit;
`DEFAULT_TASK_DOC_CALL` is the ordinary call (real mutation, worktree-contract binding).
`_enforce_branch_addressed_policy` refuses a `branch_addressed` call the policy does not sanction:
the flag is defined only for `record_route_review` and requires `config.direct_execution_enabled`
(policy-gated, L16-R6).

`_RouteReviewBinding` captures how a route-review call binds its leaf: a worktree contract
(`contract`, `task_root`, `selected_path`) plus the `branch_addressed` opt-in. The binding form
`_record_route_review_bound` refuses a master doc, requires a review object, proves the binding via
`_require_route_review_binding`, then builds the stamped `RouteReviewRecord` through
`build_route_review(contract, ResolvedTaskDocument(ref=document_ref(contract, selected_path),
path=selected_path, document=doc), payload, branch_addressed=...)` (line 156-163) and re-validates
the whole document. The legacy positional `_record_route_review` (line 120-132) preserves the
pre-wave-2 call shape and its error dialect (master -> "record_route_review is valid only for a leaf
task document"; no contract -> "requires the leaf worktree contract").

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
- Policy gate (`direct_execution_enabled`) and per-call opt-in are both enforced.
- Route-review evidence can only be stamped through this machinery; `create`/`replace` cannot
  author or change it.
- A recorded review always binds the current canonical task intent of the exact selected leaf
  document; a legacy or missing-intent document cannot be stamped as current.
- This module validates and stamps; it does not perform review or mutate source.

### Todos

None recorded.

## Docs References

No configured Domain Documentation source applies.

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| Call-level knobs and the branch-addressed policy gate. | `TaskDocCall`; `_enforce_branch_addressed_policy` | mcp/src/agents_remember/application/task_docs/task_doc_route_review.py:36-45; mcp/src/agents_remember/application/task_docs/task_doc_route_review.py:52-67 |
| The binding form that records a review over the resolved candidate document and re-validates. | `_record_route_review_bound` | mcp/src/agents_remember/application/task_docs/task_doc_route_review.py:156-175 |
| The legacy positional recorder passing the resolved leaf document. | `_record_route_review` | mcp/src/agents_remember/application/task_docs/task_doc_route_review.py:120-132 |
| Exact-binding refusal with the L16-R9 recovery dialect. | `_require_route_review_binding` | mcp/src/agents_remember/application/task_docs/task_doc_route_review.py:157-196 |
| The route-review authority rule (create/replace cannot author or change evidence). | `_enforce_route_review_authority` | mcp/src/agents_remember/application/task_docs/task_doc_route_review.py:199-218 |
| The stamping owner it delegates to; now takes the resolved candidate document. | `build_route_review` | mcp/src/agents_remember/worktrees/route_review.py:56-90 |
| The typed candidate ref derived from the selected path. | `document_ref` | mcp/src/agents_remember/worktrees/route_review.py:166-180 |
| The facade that dispatches into this module. | `task_doc_tool` | mcp/src/agents_remember/application/task_docs/task_doc_tools.py:191-284 |

## Cross-Repo References

No meaningful cross-repository reference applies.

## CCR-R02@v2 Task-Intent-Bound Reviews

Per `requirements/CCR-R02-v2-normative-task-intent-identity.md`, a route review is evidence bound
to normative task intent: the recorders now pass the exact `ResolvedTaskDocument` so
`build_route_review` stamps the current `task-intent/v1` digest, and a review whose intent is
missing/stale refuses. The application seam itself performs no review and owns no intent
semantics. Part of the landed L25 candidate `99dc249b`.

## Update History

- 2026-09-03T12:30+02:00 — 260831-CCR memory curation pass for 99dc249bd507 (CCR-R02@v2/L25):
  both recorders now build the exact `ResolvedTaskDocument` (`document_ref(contract,
  selected_path)`) for `build_route_review`, so stamped reviews bind the canonical task-intent
  identity; documented the intent-bound review invariant. Verified at code commit
  99dc249bd507c20b09ece1169c2b1fa2af8e8c1b.

- 2026-08-21T00:45+02:00 — 260815-DAG master full-gate repair: source moved to `mcp/src/agents_remember/application/task_docs/task_doc_route_review.py` (new package route); the citation fixer repointed in-body references; import paths updated inside the module. Verified at code commit e5cb139f.


- 2026-08-20T09:35+02:00 — 260815-DAG-L16: created for L16-R6/R9 — the route-review binding
  machinery extracted from `task_doc_tools.py` with the branch-addressed series-contract mode,
  the direct-execution policy gate, and the error dialect naming binding + recovery. Verified at
  code commit a9d50e08.
