# mcp/tests/test_candidate_batch_transaction.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/test_candidate_batch_transaction.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-16T10:10+02:00 |
| lastVerifiedCommitHash | `76c7697ca275a8d2764729145c950c166f3f9ec3`|
| lastVerifiedCommitDate | 2026-09-16T10:27:28+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[mcp/tests overview](overview.md)

## Purpose

**The focused behaviour of the candidate batch's transaction boundary and its admission rules.** Each case
protects one consequential failure: a late-invalid batch whose earlier inserts must be gone, a competing writer
whose batch must be refused rather than rebased, a payload that tries to carry its own authority, a lane that is
not a candidate, and an expectation that no longer holds.

Every refusal case measures the stored dataset before and after, because "nothing was written" is the property the
whole operation exists to provide. The module is the reason the leaf's atomicity claim is evidence rather than
prose: mutating the rollback to a commit fails a named node here.

It is registered in `mcp/tests/test-evidence-lanes.toml` under **unit-regression** (hermetic: temporary
directories, in-process APSW databases, no integration marker).

## Code Commentary

### Logic

The 27 nodes group into five concerns, and each group is where a later reader should look:

- **Atomicity and the transaction boundary.** `test_a_late_invalid_command_rolls_back_every_earlier_insert_in_the_batch`
  (the named rollback proof, and the harness's registered evidence node),
  `test_a_late_constraint_failure_inside_one_batch_rolls_the_whole_batch_back`,
  `test_a_refused_batch_leaves_no_audit_row_of_its_own`, and
  `test_a_database_refusal_mid_batch_names_the_command_that_actually_failed`, which reaches a genuine
  `apsw.Error` at a **non-final** command by disabling the concept's own pair pre-check inside a
  `monkeypatch.context()` and asserts the mapped refusal names `"<index>:<kind>"`. Its sibling
  `test_the_membership_guard_refuses_a_pair_the_declared_unique_tuple_would_also_refuse` drives the concept
  guard directly, so the two mechanisms the earlier single node conflated now each have their own evidence.
- **Admission and authority.** The baseline-lane refusal, the cross-namespace refusal, the spoofed-provenance case
  (a payload carrying its own actor, authorization, operation id and instant is stored under the admitted
  envelope), the accepted-origin promotion refusal, and the task-candidate lane refusal, which is asserted both
  with no `task_ref` and with a caller-asserted one — the caller cannot self-authorize by supplying a reference.
- **Preconditions.** The changed-expectation and expected-absence cases, the two-commands-one-identity case, and
  the cross-batch competing-writer case where the second batch is refused `stale_precondition` and the winner's
  rows stand.
- **The completed-graph lineage rule.** `test_a_batch_may_cite_a_record_an_earlier_command_created`,
  `test_a_batch_may_author_its_lineage_in_any_order` (a successor authored *before* the command that creates its
  predecessor is accepted and read back as declared),
  `test_a_cycle_the_batch_declares_among_its_own_revisions_is_refused_by_name` (refused `lineage_cycle` with zero
  rows written), `test_the_completed_graph_pass_refuses_a_cycle_the_operation_cannot_see_yet`, the family twin,
  and `test_the_batch_cycle_rule_is_handed_the_batchs_own_declared_edges`, which wraps the shared
  `lineage.find_cycle` in a spy around the **public** operation and asserts the rule was reached carrying the
  batch's other declared edges. That spy is not vacuous: neutering the shared rule removes the refusal and fails
  that node, so the refusal is produced by the shared rule rather than by a second rule beside it.
- **Receipts and removals.** `test_a_removal_only_batch_of_each_kind_returns_a_typed_result` and its all-three
  twin (a removal-only batch is a normal `changed` result whose every entry is a `state="removed"` entry carrying
  the digest the row had), `test_a_mixed_batch_reports_both_the_removal_and_the_write`,
  `test_a_no_op_label_edit_inside_a_mixed_batch_is_not_reported_as_a_write`,
  `test_a_batch_with_no_net_change_commits_nothing_and_reports_no_change`,
  `test_an_unknown_invariant_refuses_the_revision_and_writes_nothing`, and
  `test_a_context_smuggled_past_the_model_seal_is_refused_by_the_operation` — the operation-level companion to
  the commands module's model-level seal case, built through the public `model_copy` path so it exercises the
  in-transaction re-derivation rather than the validator.
- `_apply_one_removal` is the shared helper the three removal cases use to seed a row and apply a removal
  through the admitted destination.

### Conventions

- The `candidate` fixture supplies the shared `CandidateHarness`; no case opens a store by hand except through the
  harness's context manager.
- A refusal case asserts on `measure_refusal`'s before/after snapshots rather than on the returned result, so the
  atomicity claim is measured from storage.
- The monkeypatch context is scoped to one batch, so the mutated mechanism cannot leak into another assertion.
- Registration: `mcp/tests/test-evidence-lanes.toml` `unit-regression` (row 19). Classification only, never
  execution or acceptance evidence.

### Invariants And Boundaries

- **This is the module that makes atomicity load-bearing.** If a redesign removes the rollback, the named nodes
  here — not a prose claim — are what fail. Keep that property when editing.
- **A named node must discriminate the mechanism it names.** The database-caught case was split precisely because
  the earlier node's assertions held for the concept's pre-check rather than the database's constraint; the same
  rule now applies to the lineage spy, which fails when the shared rule is neutered.
- **Coverage of a mechanism belongs where the mechanism decides.** Cycle behaviour is asserted through the public
  operation; the concept-level guard has its own node; the standalone label CAS is the label-operations module's.
- **Boundary.** This module owns the transaction boundary, lane admission, preconditions and the completed-graph
  rule. The union's coverage and the receipt's fidelity belong to `test_candidate_batch_commands.py`, and the
  standalone label path to `test_knowledge_label_operations.py`.

### Todos

None recorded for this slice.

## Docs References

No domain documentation source is configured for this repository (`system/sources.md` carries no
`Domain Documentation` entries). The statements below are grounded in repository source only.

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured domain documentation could be checked. | — | — |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The module's scope statement, and that every refusal case measures the dataset before and after. | "measures the stored dataset before and after" | mcp/tests/test_candidate_batch_transaction.py:1-10 |
| The named rollback proof — the harness's registered evidence node. | "test_a_late_invalid_command_rolls_back_every_earlier_insert_in_the_batch" | mcp/tests/test_candidate_batch_transaction.py:62-110 |
| The constraint-failure rollback and the audit-row case. | "test_a_late_constraint_failure_inside_one_batch_rolls_the_whole_batch_back"; "test_a_refused_batch_leaves_no_audit_row_of_its_own" | mcp/tests/test_candidate_batch_transaction.py:111-171; mcp/tests/test_candidate_batch_transaction.py:888-911 |
| The mid-batch attribution case and the concept guard's own node, which together replaced one conflated case. | "test_a_database_refusal_mid_batch_names_the_command_that_actually_failed"; "test_the_membership_guard_refuses_a_pair_the_declared_unique_tuple_would_also_refuse" | mcp/tests/test_candidate_batch_transaction.py:993-1061; mcp/tests/test_candidate_batch_transaction.py:1062-1119 |
| The competing-writer, changed-expectation and expected-absence cases. | "test_a_competing_writer_leaves_the_second_batch_refused_with_the_state_untouched"; "test_an_expected_record_that_changed_refuses_and_leaves_the_row_alone"; "test_an_expected_absence_that_is_not_absent_refuses_the_batch" | mcp/tests/test_candidate_batch_transaction.py:172-224; mcp/tests/test_candidate_batch_transaction.py:225-268; mcp/tests/test_candidate_batch_transaction.py:269-290 |
| The admission cases: spoofed provenance, accepted origin, baseline lane, foreign namespace and the task lane. | "test_a_payload_that_claims_its_own_author_and_approval_is_not_an_authority"; "test_an_accepted_origin_state_is_refused_as_a_promotion"; "test_a_baseline_lane_is_refused_as_a_non_candidate_target"; "test_a_batch_from_another_namespace_is_refused"; "test_a_task_candidate_lane_is_refused_until_its_binding_can_be_resolved" | mcp/tests/test_candidate_batch_transaction.py:291-338; mcp/tests/test_candidate_batch_transaction.py:339-373; mcp/tests/test_candidate_batch_transaction.py:374-394; mcp/tests/test_candidate_batch_transaction.py:395-416; mcp/tests/test_candidate_batch_transaction.py:1162-1188 |
| The completed-graph nodes, including the spy that proves the shared rule receives the batch's edges. | "test_a_batch_may_author_its_lineage_in_any_order"; "test_a_cycle_the_batch_declares_among_its_own_revisions_is_refused_by_name"; "test_the_completed_graph_pass_refuses_a_cycle_the_operation_cannot_see_yet"; "test_the_batch_cycle_rule_is_handed_the_batchs_own_declared_edges"; "test_a_cycle_among_a_batchs_own_family_revisions_is_refused_by_name" | mcp/tests/test_candidate_batch_transaction.py:470-516; mcp/tests/test_candidate_batch_transaction.py:517-560; mcp/tests/test_candidate_batch_transaction.py:561-604; mcp/tests/test_candidate_batch_transaction.py:605-675; mcp/tests/test_candidate_batch_transaction.py:676-710 |
| The receipt and removal nodes, including the smuggled-context case. | "test_a_removal_only_batch_of_each_kind_returns_a_typed_result"; "test_a_removal_only_batch_removing_all_three_kinds_at_once_returns_a_typed_result"; "test_a_mixed_batch_reports_both_the_removal_and_the_write"; "test_a_no_op_label_edit_inside_a_mixed_batch_is_not_reported_as_a_write"; "test_a_context_smuggled_past_the_model_seal_is_refused_by_the_operation" | mcp/tests/test_candidate_batch_transaction.py:933-962; mcp/tests/test_candidate_batch_transaction.py:963-992; mcp/tests/test_candidate_batch_transaction.py:711-776; mcp/tests/test_candidate_batch_transaction.py:799-845; mcp/tests/test_candidate_batch_transaction.py:1120-1161 |
| The unit-lane row that makes the module's classification explicit. | "mcp/tests/test_candidate_batch_transaction.py" | mcp/tests/test-evidence-lanes.toml:19-19 |
| The harness whose refusal measurement these cases assert on. | `measure_refusal`; `CandidateHarness` | mcp/tests/candidate_batch_test_support.py:324-344; mcp/tests/candidate_batch_test_support.py:92-235 |
| The shared lineage rule the spy case instruments. | `find_cycle`; `declared_cycle` | mcp/src/agents_remember/memory/knowledge/lineage.py:107-131; mcp/src/agents_remember/memory/knowledge/lineage.py:71-105 |

## Cross-Repo References

No cross-repository behavior is involved in this module. The mutation evidence for it was taken in isolated
copies outside the repository, and no case writes outside its temporary directory.

| Finding | Anchor | Source |
| --- | --- | --- |
| No meaningful cross-repo references found. | — | — |

## Update History

- 2026-09-16T10:10+02:00 — 260915-KS-L3 curator (uncommitted change set on `ar/260915-ks-l03`, base `27242ecb`): created this one-to-one card for the new candidate-batch transaction suite (27 nodes, unit-regression lane). It records the five concerns the module covers, that the atomicity claim is load-bearing here rather than in prose, and the reusable rule the two split cases teach: a node named for a mechanism must discriminate that mechanism — which is why the database-caught path and the membership guard each have their own node, and why the lineage spy fails when the shared rule is neutered. Verification metadata remains empty until closeout stamps the code commit.
