# mcp/tests/test_master_end_document_staleness.py

## Governing Overview

[tests route overview](overview.md)

## Purpose

Exercise master-end dependent-document staleness classification, standing-base resolution, own-leaf attribution, post-landing parent repair, fail-closed uncomputable and unverifiable guards, checkpoint non-refusal, and four-kind answer/refusal formatting over real Git repositories, canonical task documents, and series/leaf enclosure contracts.

## Code Commentary

- `_Harness` builds paired real code and external converted-memory Git repositories (with `knowledge/layout.json` and `dependent_links`), a canonical series contract, master/leaf task documents, and leaf enclosures, binding default worktree services via an autouse fixture (`_bound_services`).
- **Standing base and checkpoints**: `test_repository_default_sync_moves_base_and_ignores_post_landing_sync` checks `master_document_base` on `repository-default` sync entries (including `memorySourceCommit=""` skip-memory fallback to `memoryBaseTo`) and excludes syncs performed after the judged landing; `test_checkpoint_landing_reports_debt_without_refusing` checks that `worktree_checkpoint_landing` passes while `worktree_integrate` refuses the same own-leaf debt.
- **Since-base, synced parent, and own-leaf debt**: `test_unlanded_master_work_refuses_since_base`, `test_parent_staleness_brought_by_sync_is_named_only`, `test_own_leaf_staleness_refuses_after_sync` (parametrized over `merge` and `squash`), `test_own_leaf_document_confirmed_after_landing_passes`, `test_confirmed_after_leaf_then_restaled_by_sync_is_named_only`, `test_deferral_only_update_after_own_leaf_still_refuses`, and `test_next_leaf_confirmation_at_previous_landed_commit_clears_debt` verify ownership attribution and non-strict `confirmed.commit` clearing.
- **Post-landing parent repair**: `test_repaired_on_parent_after_landing_refuses_nothing` (parametrized over `since_base` and `own_leaf`, using a non-`main` source branch `release/next` and `record_landing._landing_request`), `test_integration_gate_before_landing_refuses_even_when_parent_current`, and `test_unresolvable_parent_ref_fails_closed` verify that parent repair applies only after landing and fails closed on unresolvable parent refs.
- **Fail-closed uncomputable and tip-only unverifiable edges**: `test_unreadable_confirmed_commit_makes_end_uncomputable`, `test_leaf_pair_integrity_and_uncomputable_refusals` (open/abandoned leaves ignored; missing pair, nonexistent commit, code-only ancestry, and memory-only ancestry refused as uncomputable), and `test_unreadable_links_refuse_only_when_introduced_after_base` (base-only or both-sides unverifiable allowed; tip-only refused).
- **Separated four-kind output**: `test_answer_and_refusal_message_name_all_four_kinds_apart` asserts `refusedSinceBase`, `refusedByOwnLeaf` (with `leaves`), `repairedOnParent`, and `namedOnly` each carry their read and refusal remedy in both `landing_document_answer` and `DocumentStaleness.refusal_message()`.

## Relationships

- Directly exercises `application/knowledge_gate/document_staleness.py`, `application/knowledge_gate/landing.py`, `worktrees/knowledge_gate.py::{master_document_base, landing_document_answer, landing_gate_refusal}`, `worktrees/modules/integration_gate.py::integration_gate_block`, and `worktrees/modules/record_landing.py::_landing_request`.
- Registered once in `mcp/tests/test-evidence-lanes.toml` under `unit-regression` and listed as an exact consumer of `mcp/tests/_user_settings_guard.py` and `mcp/tests/fixtures/repository_profiles/node/package-lock.json` in `mcp/tests/evidence-lifecycle.toml` (catalog membership selects evidence and certifies no execution).

## Evidence

- `_Harness` constructs paired real Git code/memory repositories, canonical task documents, series/leaf enclosures, sync logs, and landing requests for master-end staleness tests. [1]
- Dedicated tests cover since-base refusal, synced parent naming, merge/squash own-leaf attribution, confirmation clearing (including equal-commit and deferral-only), unreadable `confirmed.commit`, and post-landing vs pre-landing parent repair. [2]
- Dedicated tests cover open/abandoned vs broken/one-sided leaf enclosures, tip-only unverifiable filtering, `repository-default` standing-base walks, checkpoints, and four-kind answer and refusal formatting. [3]
