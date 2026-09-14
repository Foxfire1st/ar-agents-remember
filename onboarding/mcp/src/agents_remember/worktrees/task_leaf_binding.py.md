# mcp/src/agents_remember/worktrees/task_leaf_binding.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/worktrees/task_leaf_binding.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-14T19:00+02:00 |
| lastVerifiedCommitHash |  `bb65a2073228c5e143b055a470f39c6c9e2f4d9d`|
| lastVerifiedCommitDate |  2026-09-14T19:36:04+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[Worktrees overview](overview.md)

## Purpose

Resolve the canonical master-row to leaf-task binding used by lifecycle admission.

## Code Commentary

### Logic

The resolver loads the exact parent task, identifies one child row, validates regular JSON/Markdown child sources, derives the canonical task reference and enclosure path, and supplies a source-CAS check for start. `plan_current_leaf_enclosure_registration` (`:178-202`) plans the leaf enclosure registration against the canonical parent row, and `require_current_leaf_enclosure_binding` (`:205-256`) is the admission gate start and closeout share.

### Invariants And Boundaries

- Parent row and child sources must name one exact leaf identity.
- Missing, symlinked, non-regular, or contradictory sources fail closed.
- Start revalidates the current task binding under the shared task-publication lock.
- No path naming inference replaces the canonical row/source binding.
- **Since 260913-LCA-L5 a doc with an exact enclosure address but no `seriesContractPath` refuses
  by name.** `require_current_leaf_enclosure_binding` reads the registration plan's state and, when
  the plan carries a candidate in state `master-link-missing`, raises `TaskLeafBindingError` with
  status `task-enclosure-binding-master-link-missing` and names the route that actually binds the
  field — "re-run worktree_start/worktree_attach so the start binding publisher writes this leaf
  document's seriesContractPath, then retry closeout" — rather than reusing the `mismatched`
  recovery ("run task_doc.replace against this exact leaf contract"), which could not have bound a
  derived field. Before this change such a document read as `present` and passed silently. This is
  a deliberate, load-bearing behaviour change, not an accident: it is what forced the two shared
  fixtures that had been modelling the damage state to carry the derived fields `task_doc` stamps.

### Todos

None recorded.

## Docs References

No configured domain-documentation source applies to this repository-internal route.

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| Binding models and resolution establish the canonical leaf identity through the shared pure task-domain owner. | `LeafTaskBinding`; `resolve_leaf_task_binding` | mcp/src/agents_remember/worktrees/task_leaf_binding.py:45-61; mcp/src/agents_remember/worktrees/task_leaf_binding.py:64-103 |
| Parent and child source readers enforce exact regular-file authority after canonical row/source derivation. | `_load_leaf_parent`; `_read_leaf_source` | mcp/src/agents_remember/worktrees/task_leaf_binding.py:106-116; mcp/src/agents_remember/worktrees/task_leaf_binding.py:119-143 |
| Start admission rechecks the same canonical composite binding before reserving lifecycle authority. | `require_current_start_task_binding` | mcp/src/agents_remember/worktrees/task_leaf_binding.py:160-175 |
| The registration planner this module delegates to, and the admission gate that now names the missing master link instead of reading it as present. | `plan_current_leaf_enclosure_registration`; `require_current_leaf_enclosure_binding` | mcp/src/agents_remember/worktrees/task_leaf_binding.py:178-202; mcp/src/agents_remember/worktrees/task_leaf_binding.py:205-256 |
| The typed facts carried by the new refusal, including the named recovery operation. | `_enclosure_binding_facts` | mcp/src/agents_remember/worktrees/task_leaf_binding.py:353-364 |
| The planner whose `master-link-missing` state this gate reads. | `plan_leaf_doc_enclosure_registration`; `_enclosure_registration_state` | mcp/src/agents_remember/tasks/leaf_doc.py:312-329; mcp/src/agents_remember/tasks/leaf_doc.py:332-391 |
| The start/attach publisher that is the named recovery, and therefore the operation that actually binds the field. | `_publish_leaf_task_enclosure_binding` | mcp/src/agents_remember/worktrees/modules/start.py:858-931 |
| The two shared fixtures that had to carry the derived fields once this refusal existed, because they were modelling the damage state. | `_leaf`; `_bind_task_without_review` | mcp/tests/test_closeout_queue.py:107-156; mcp/tests/test_transaction_only_worktree_delivery.py:93-116 |

## Cross-Repo References

No meaningful cross-repository boundary is owned by this file.

## CCR-L42 current candidate

Leaf binding now resolves the canonical parent row to one exact JSON task document, plans enclosure registration, and returns typed repair facts before closeout. Missing or mismatched bindings fail closed without sibling scans or compatibility fallbacks.

## Update History

- 2026-09-14T19:00+02:00 — 260913-LCA-L12 curator (residue citation pass): re-derived the source
  range of 1 claim(s) whose anchor no longer sat in its cited range and normalised 2 further
  range(s) from their anchors against the frozen source snapshot (`agents-remember memory-citations
  --fix --document`). No claim wording was changed to fit an anchor; every rewritten range was read
  back at its current position. Verification metadata remains closeout-owned.
- 2026-09-14T07:05+02:00 — 260913-LCA-L5 curator (uncommitted change set on `ar/260913-lca-l5-ar`, base
  `52875e7a`): recorded the new `task-enclosure-binding-master-link-missing` refusal. The card now states
  that a document with an exact enclosure address but no `seriesContractPath` refuses by name with the
  start/attach remedy instead of reading as `present`, and that this is an intended, load-bearing
  behaviour change — it is what forced `test_closeout_queue._leaf` and
  `test_transaction_only_worktree_delivery._bind_task_without_review` to carry the derived fields
  `task_doc` stamps. Also recorded why the new state gets its own recovery rather than reusing
  `mismatched`'s `task_doc.replace` remedy, which could not bind a derived field. Repaired five stale
  reference ranges, all measured with AST (`LeafTaskBinding` 30-45 → 46-61, `resolve_leaf_task_binding`
  48-87 → 64-103, `_load_leaf_parent` 90-100 → 106-116, `_read_leaf_source` 103-127 → 119-143,
  `require_current_start_task_binding` 144-177 → 160-175) and added four rows. Verification metadata is
  **not** advanced: the code commit does not exist and closeout owns the stamp; no acceptance claim.
- 2026-09-10T00:20:36+02:00 — CCR-L42 current candidate reconciliation: Leaf binding now resolves the canonical parent row to one exact JSON task document, plans enclosure registration, and returns typed repair facts before closeout. Missing or mismatched bindings fail closed without sibling scans or compatibility fallbacks.

- 2026-09-01T03:58+02:00 — 260831-CCR-L01 Attempt 8: re-read the reopened child-source claim,
  documented delegation to the shared canonical leaf-binding owner, regenerated moved ranges, and
  rebound the card to its nearest worktrees overview. Verification remains closeout-owned.

- 2026-08-24T14:48+02:00 — DAGQC cumulative CLIVE final-gap curation: created the strict source-mirroring card from current code. Verification hash/date remain blank for architect-owned final stamping.
