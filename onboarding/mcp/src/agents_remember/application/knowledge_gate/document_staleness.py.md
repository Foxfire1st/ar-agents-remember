# mcp/src/agents_remember/application/knowledge_gate/document_staleness.py

## Governing Overview

[application route overview](../overview.md)

## Purpose

Compute dependent-document staleness for incremental landings (`full=False`) and a master's end (`full=True`), classify master-end debt by ownership and parent-line repair state, and render the `staleDocuments` answer payload and master-end refusal text.

## Code Commentary

### Incremental vs Master-End Classification

- **`document_staleness(request, *, full=False)`** returns a frozen `DocumentStaleness`. On an incremental landing (`full=False`), it reads only dependent records touched by changed code paths (`_changed_paths`) or changed memory record IDs (`_changed_record_ids`) through the layout marker's `dependent_links` index (`_dependent_paths_saying`). Any document stale at the tip and current or absent at the base goes to `documents`; any document already stale at the base goes to `already_stale` and refuses nothing.
- On a master's end (`full=True`), `_effective_request` substitutes `request.document_base` (the standing base pair) when supplied, `_observe_pair` reads every dependent record at both base and tip, and `_classify_master_end` splits stale tip documents into four disjoint sets:
  - `made_stale_since_base`: stale at tip and not stale at the standing base (minus post-landing parent repairs).
  - `made_stale_by_leaf` (with `made_stale_by_leaf_ids`): stale at both standing base and tip, made stale by one of this master's own completed integrated leaves (`_master_integrated_leaves`, `_documents_made_stale_by_leaves`) without a tip `confirmed.commit` that equals or descends from that leaf's landed code commit (`_confirmed_after_leaf`, non-strict `git merge-base --is-ancestor`, minus post-landing parent repairs). A deferral-only update does not advance `confirmed.commit` and therefore does not clear own-leaf debt.
  - `repaired_on_parent`: documents otherwise refusing that exist and evaluate `current` (with no moved links) at the parent line's present tip resolved from `series.code_source_branch` and `series.memory_source_branch` (`_repaired_on_parent`). This exemption activates only when both judged commits are already ancestors of the parent line's present tip (after landing, never before `worktree_integrate`); any ref-resolution or read error disables the exemption (fail closed).
  - `already_stale` (`namedOnly`): all remaining base-stale documents; named without refusing.

### Fail-Closed Boundaries

- `_master_integrated_leaves` loads `exact_atomic_leaf_contracts(series, require_all=False)` and inspects only `integration_status == "completed"` leaves (ignoring open and abandoned leaves). `_validated_leaf_pairs` requires all four commit hashes (`code_base_commit`, `memory_base_commit`, `integrated_code_commit`, `integrated_memory_content_commit`) to be present and readable commits (`_require_commit`), and raises `ValueError` if only one side of a leaf is an ancestor of the judged tip.
- `_confirmed_after_leaf` returns `False` on an empty `confirmed.commit` and raises `ValueError` through `_strict_is_ancestor` when Git cannot read `confirmed.commit`.
- `document_staleness` catches `KnowledgeSideUnreadable`, `GitPreparationError`, `CloseoutQueueError`, `ContractError`, `TaskDocumentRefError`, `ValueError`, `OSError`, and `subprocess.SubprocessError` and returns `DocumentStaleness(uncomputable=...)` so a master's end fails closed rather than passing.
- On a master's end, `_classify_master_end` filters `unverifiable` links to tip-only entries (`doc not in observed.base_unverifiable`), so a document unreadable only at the standing base does not refuse.

### Answer And Refusal Formatting

- `DocumentStaleness.answer(name_already_stale=...)` emits `{"state": "uncomputable", "detail": ...}` or `{"state": "unverifiable", "detail": ..., "count": ..., "documents": ...}` before any zero-count omission. Otherwise it returns `count`, `documents`, `read` (`view="dependent"`, `staleOnly=True`), `alreadyStale` when present, and per-kind blocks (`refusedSinceBase`, `refusedByOwnLeaf` with `leaves`, `repairedOnParent`, `namedOnly`) carrying their own `read` and refusal `remedy`. When `name_already_stale=True`, it retains `count: 0` whenever `already_stale` or `repaired_on_parent` is non-empty.
- `DocumentStaleness.refusal_message()` renders separate sentences for each non-empty category with its read command and category-specific remedy.

## Relationships

- Re-exported by sibling [`landing.py`](landing.py.md) (`DocumentStaleness`, `document_staleness`, `_changed_paths`), whose `_findings` turns `uncomputable`, `unverifiable`, and `documents` into master-end gate refusals.
- Called by `worktrees/knowledge_gate.py::landing_document_answer`, `worktrees/modules/integration_gate.py`, and `worktrees/modules/record_landing.py` (which supply `master_document_base(...)` as `document_base` on master-end series requests).
- Uses `application/knowledge_reader/marks.py::dependent_movement`, `application/knowledge_gate/change_reach.py::dependent_touches`, `worktrees/series_leaf_contracts.py::exact_atomic_leaf_contracts`, and `worktrees/modules/git.py::{branch_commit, is_ancestor}`.
- Verified over real Git repositories by `mcp/tests/test_master_end_document_staleness.py` and `mcp/tests/test_mik_r118_r124_marks.py`.

## Evidence

- `DocumentStaleness` holds split master-end ownership and repair fields and formats `answer()` with separate `refusedSinceBase`, `refusedByOwnLeaf`, `repairedOnParent`, and `namedOnly` sections and `refusal_message()`. [1]
- `document_staleness` dispatches incremental vs master-end evaluation and folds unreadable contract, leaf, and Git errors into `DocumentStaleness(uncomputable=...)`. [2]
- `_classify_master_end` separates since-base staleness, own-leaf debt, post-landing parent repairs, named-only debt, and tip-only unverifiable links. [3]
- `_master_integrated_leaves`, `_validated_leaf_pairs`, `_documents_made_stale_by_leaves`, and `_confirmed_after_leaf` attribute own-leaf staleness with fail-closed commit/ancestry validation and non-strict confirmation clearing. [4]
- `_repaired_on_parent` exempts documents current on the parent line only after both judged commits are ancestors of the resolved parent source branches, failing closed on any ref-resolution or read error. [5]
