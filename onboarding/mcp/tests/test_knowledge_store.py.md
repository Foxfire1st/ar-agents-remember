# mcp/tests/test_knowledge_store.py

## Governing Overview

[tests route overview](overview.md)

## Purpose

The focused behavioural suite for the immutable knowledge identity store. Each case protects one consequential
operation or failure — a divergent-successor read, an identity reuse, a lineage violation, or a database-level
immutability guarantee. Constructor validation is not re-tested here; the failure each case protects is a
stored-state failure.

## Code Commentary

### Logic

Support in this module: a `fixture` pytest fixture that builds the shared branching fixture under
`tmp_path / "candidate"`; `ExtensionOptions` (optional invariant id, predecessors, statement and provenance for one
extension case); `_extension_request` (builds a `RevisionRequest` around `fixture_revision_draft`, allowing the
invariant id and provenance to be overridden); `_disable_immutability_triggers` and `_write_raw_cycle` /
`_write_raw_edge` (write cyclic state **outside** the operation, with a docstring stating why the triggers are
dropped); and a `_revision_and_edge_counts` helper used by the refusal-invariance assertions.

23 collected nodes, all in the unit lane and with no integration marker. The `KS-R03` increment added the one node marked below:

| Node | Protects |
| --- | --- |
| `test_two_same_label_successors_reopen_as_separate_revisions` | two `v2` successors stay independently addressable with their exact statements after a close/reopen cycle |
| `test_reopening_the_same_path_keeps_identity_and_schema` | reopen validates the same generation instead of creating or repairing |
| `test_a_repeated_identical_invariant_is_no_change_and_a_relabel_refuses` | **added by `KS-R03`**: the single-record identity operation confirms an identical repeat (`no_change`) and refuses a different label under one id (`duplicate_identity`) — the two-caller contract the batch refactor nearly unified away |
| `test_created_revision_stores_the_digest_the_store_recomputed` | the stored seal is the store's recomputation, not caller input |
| `test_identical_aggregate_is_no_change` | re-submitting the same aggregate is `no_change` rather than a duplicate refusal |
| `test_reused_revision_identity_with_other_content_refuses` | an identity reuse with different content refuses and leaves the stored row unchanged |
| `test_accepted_origin_data_requires_an_acceptance_reference` | proposal is distinct from acceptance at the vocabulary boundary |
| `test_cross_invariant_predecessor_refuses_with_the_named_endpoint` | a cross-invariant predecessor refuses as `invalid_reference` naming both invariants |
| `test_dangling_predecessor_refuses_without_leaving_a_row` | a nonexistent predecessor refuses with unchanged row counts |
| `test_self_predecessor_is_refused_at_the_vocabulary_boundary` | a self-referencing payload is refused before storage |
| `test_cycle_membership_reports_the_edges_of_an_on_cycle_revision` | the membership query reports both edges of a cycle, and an unrelated successor is admitted |
| `test_lineage_guard_refuses_a_candidate_descending_from_a_stored_cycle` | the write-path guard refuses a candidate below a stored cycle, naming the cycle, with no row written and wording that does not claim self-reachability |
| `test_lineage_cycle_refusal_describes_each_branch_honestly` | both branches of the rule are worded for the branch they describe |
| `test_lineage_guard_fires_before_the_candidate_insert` | the guard is evaluated before the candidate's own INSERT (disabling it fails this node) |
| `test_unknown_invariant_refuses_the_revision` | a revision for an unrecorded invariant refuses as `unknown_invariant` |
| `test_other_repository_namespace_is_refused` | a foreign namespace refuses as `unauthorized_scope` on every write operation |
| `test_stored_revision_rows_refuse_update_and_delete` | direct `UPDATE`/`DELETE` raises `immutable_revision` at the database level |
| `test_payload_digest_seals_more_than_the_statement` | the seal covers the predecessor set, so a re-pointed edge fails the read-time check |
| `test_schema_carries_the_declared_manifest_and_generation` | the live schema matches the declared tables, columns and `user_version` |
| `test_partial_schema_is_refused_instead_of_written_through` | a missing canonical table refuses at open |
| `test_dropped_immutability_trigger_is_refused` | a dropped trigger refuses at open |
| `test_application_seam_initializes_and_extends_one_namespace` | the composition seam initializes and extends one namespace end to end |
| `test_lower_ranked_owners_do_not_import_the_memory_domain` | the layer direction holds: no owner below `memory` imports the storage package |

### Conventions

The module imports the fixture through the bare module name `knowledge_fixture_test_support`, which is how
`mcp/tests/conftest.py` puts this directory on `sys.path`. Assertions name the observable outcome (state, refusal
code, offending record, row counts) rather than internal call order.

### Invariants And Boundaries

- The suite is the executable counterpart of the requirement's failure list. Two nodes are load-bearing for
  enforcement rather than for reading: disabling the write-path lineage guard makes
  `test_lineage_guard_refuses_a_candidate_descending_from_a_stored_cycle` and
  `test_lineage_guard_fires_before_the_candidate_insert` fail; reintroducing the superseded refusal wording fails
  the descending node and the branch node.
- **`test_a_repeated_identical_invariant_is_no_change_and_a_relabel_refuses` is not a duplicate of the
  aggregate node.** `test_identical_aggregate_is_no_change` covers revision reuse; this one covers the *identity*
  operation, and it exists because the `KS-R03` refactor moved the invariant insert into a shared helper and
  silently dropped the `no_change` branch — the base tree returned `no_change` for an identical repeat while the
  candidate refused `duplicate_identity` (sealed finding `260915-KS-L3-RV-2`). The repair restored the branch via
  `confirm_repeat` and this node would fail if it were removed again. The suite passed 54/54 while the behaviour
  was wrong, which is why the node had to be added rather than a passing suite trusted.
- Cyclic state has no reachable creation path through `create_revision` — admission accepts only existing
  predecessors and the vocabulary refuses a self-referencing payload — so the cycle cases write the raw edges
  outside the operation and say so. That construction is labelled, not a workaround: the finding it once carried
  was about what a node asserted, not about how the state was built.
- The module is registered in exactly one lane, `unit-regression`, in `mcp/tests/test-evidence-lanes.toml`.
  Without that row `load_lane_manifest` refuses the repository and the certifying collection path cannot start, so
  the registration is a load-bearing part of this change set rather than bookkeeping.
- The 23 nodes all live inside the unit collected-case budget; no integration marker is used and no case spawns a
  repository or a subprocess.

### Todos

None recorded. Later leaves (KS-R02 … KS-R08) extend the fixture and add their own modules rather than growing this
one.

## Evidence

### Docs References

No domain documentation source is configured for this repository (`system/sources.md` carries no
`Domain Documentation` entries). The statements below are grounded in repository source only.

No configured domain documentation could be checked.

### Repo-Internal References

- The divergent-successor read, the node registered as the shared fixture's evidence node. [1]
- The two-caller identity contract the `KS-R03` repair restored, added to this suite in that same change. [2]
- The identity reuse refusal and its unchanged stored row. [3]
- The write-path guard's descending branch, including the wording assertions. [4]
- The before-the-insert evaluation a disabled guard fails. [5]
- The database-level immutability proof against the stored revision rows. [6]
- The seal covering more than the statement. [7]
- The seam case that drives the production composition path, including the batch entry points this leaf added to that module. [8]
- The layer-direction case. [9]
- The shared fixture every case builds from. [10]
- The lane registration that makes the repository's manifest load (this module's row inside the lane, after the `KS-R03` insertions). [11]
- The fixture's registered stable contract and evidence node. [12]
- The store contract the added node pins, including the two-caller distinction. [13]

### Cross-Repo References

No cross-repository behavior is implemented in this file.

No meaningful cross-repo references found.
