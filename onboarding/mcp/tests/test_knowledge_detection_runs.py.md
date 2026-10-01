# mcp/tests/test_knowledge_detection_runs.py

## Governing Overview

[tests route overview](../overview.md)

## Purpose

**`DetectionRun`: the walk over the shipped comparison, its declared order, its write and read paths, its
reproducibility and currentness, and the refusals that keep a detection write out of the assessed dataset
— 20 cases.**

They occupy the `unit-regression` lane (registered in `mcp/tests/test-evidence-lanes.toml`) because what
they measure is the detection contract's own logic — which recorded facts produce which condition, which
order two executions produce, and which write is refused — and not a process, a publication or a Git
object. The one case that runs a *real* comparison drives the shipped seams through the registered
`diff_scope_test_support` fixture and reads its result through the application layer, so the walk is shown
to consume real comparison output rather than a shape invented beside it.

The module has two halves and says so: a synthetic half that builds union items, family memberships and
anchor resolutions by hand so a condition can be provoked exactly, and a store half that opens a real
generation-4 detection store and drives `record_detection_run`/`read_detection_run` through it.

## Code Commentary

### Logic

- **The scenario and its harmless control are indistinguishable to the detector.**
  `test_a_budget_change_and_a_comments_only_change_produce_the_same_condition_and_signal` is the
  acceptance shape of the responsibility boundary: both changes produce the same condition identity and
  the same signal identity, and neither carries a verdict.
- **A grouping keeps everything it grouped.**
  `test_a_grouped_signal_retains_every_contributing_match_with_its_path_and_edges`.
- **The declared order is total and independent of item order.**
  `test_the_declared_order_is_total_over_signal_identity_and_independent_of_item_order` — reproducibility
  by construction rather than by luck.
- **A declared limitation is not a negative match.**
  `test_an_unsupported_locator_is_a_declared_limitation_rather_than_a_negative_match` asserts the shipped
  resolver's `unsupported_locator` is reported as a scope limitation rather than as an error or as
  "nothing changed"; `test_an_unmapped_changed_path_and_a_truncated_scan_are_advertised_rather_than_dropped`
  asserts an incomplete scan and an unmapped path are advertised instead of smoothed; and
  `test_the_walk_declares_the_probe_and_the_omission_the_comparison_actually_recorded` asserts the probe
  outcome and the omission come from the comparison's own record.
- **A declaration is never silently widened.**
  `test_a_both_sides_declared_walk_over_one_side_is_refused_rather_than_widened`.
- **The real-comparison case.**
  `test_the_walk_consumes_the_shipped_comparison_and_emits_facts_only_signals` runs two real databases and
  two real Git trees through the shipped application seam, then checks every emitted signal for the
  facts-only boundary's properties.
- **One identity names one signal, measured on the shipped comparison rather than on a synthetic union.**
  `test_a_run_over_the_shipped_comparison_names_every_signal_once_and_is_recorded` (added by
  `260915-KS-L23`) walks the real comparison for a fixture whose union holds two realization items that are
  gone from the after side and speak for **one** claim record, and asserts in one run: the fixture still
  holds that shape (so the case cannot silently stop exercising the defect), every `signal_id` is unique,
  one `removed_or_reparented_attribution` signal per removed item with each signal's `observed_changes`
  naming that item, the same union walked in the **reversed** item order produces the identical ordered
  identities, and finally that `build_detection_run` + `record_detection_run` accept the walk and
  `read_detection_run` serves the order back. That last step is what makes the identity a property of the
  write path rather than of a walk asserted beside it: before the fix the two signals shared one identity
  and the run builder refused the whole run. Its two helpers are `real_input_sides` (each side named by its
  **own** dataset's `generation_of_database` + `logical_digest`, so a recorded run names what it read rather
  than copying one side's snapshot onto the other) and `claim_records_spoken_for_twice` (the union items
  whose `record_id` is spoken for more than once).
- **The write/read round trip carries the order and the two-place versions.**
  `test_a_recorded_run_reads_back_in_its_recorded_order_with_two_place_versions`, and
  `test_a_run_records_the_exact_inputs_it_read_as_identities` asserts the snapshots are recorded as
  identities rather than as paths.
- **Two declarations on one run are not collapsed.**
  `test_two_signals_with_different_declared_sets_are_both_recorded_on_one_run`.
- **The agreement refusals write nothing.**
  `test_a_signal_that_disagrees_with_its_run_is_refused_and_nothing_is_written` also asserts zero rows
  written, and `test_a_run_whose_declared_order_names_other_signals_is_refused`.
- **Requirement 7.1 as a refusal.**
  `test_a_detection_write_into_an_assessed_database_is_refused` is the self-invalidating sequence: write
  the measurement, the assessed digest moves, the measurement's own binding is stale.
- **The sequence is sealed by the database.**
  `test_a_recorded_detection_sequence_cannot_be_reordered_or_shortened` — generation 4's triggers are what
  refuse it, not the operation alone.
- **A re-execution over a moved input is a distinct run.**
  `test_a_reexecution_over_a_changed_snapshot_is_a_distinct_run_naming_the_difference`.
- **A moved policy version marks a run stale without reinterpreting its signals.**
  `test_a_run_whose_policy_version_moved_is_stale_and_its_signals_keep_their_versions`.
- **Retention through the operation names its destination.**
  `test_a_manifest_reference_reported_through_the_operation_names_its_destination` asserts a
  worktree-local home is *not* reported retained.
- **A predating dataset is refused, not migrated.**
  `test_a_detection_dataset_predating_generation_4_cannot_be_created_by_migration` builds a genuine
  generation-3 dataset and asserts `unsupported_schema` with expected/observed `"4"`/`"3"`, then asserts
  the table is still absent.

### Conventions

- **Support is consumed, not added.** The real-comparison case imports `DiffFixture` and
  `build_diff_fixture` from the already-registered `mcp/tests/diff_scope_test_support.py` and drives
  `diff_knowledge_scope`/`open_diff_side` from the application layer; this module registers **no** new
  governed evidence artifact and no new contract, which is why the lifecycle catalog's counts stay at
  thirteen contracts and fifty-four artifacts and only two `consumers` rows were added. The shared-record
  case added later consumes the same support and nothing else — its other imports are production
  (`open_read_only_database`, `logical_digest`, `generation_of_database`) — so the module's evidence
  registration is unchanged by it.
- **A module-scoped fixture holds the expensive part.** `real_fixture` builds the two-snapshot fixture
  once for the module, and `run_real_diff` is the one place the shipped comparison is invoked. The
  shared-record case consumes both and adds no fixture of its own: it opens each side again read-only
  through `open_read_only_database` to name that side's own dataset identity.
- **The store fixtures are real.** `detection_store` opens a generation-4 knowledge store and
  `assembled_run` assembles one run from the signals a walk produced, so the write cases drive the
  production entry points rather than a hand-built row.
- **Fixed identities live in module constants** (`REPOSITORY_ID`, `ROUTE_ID`, the four digests, the claim
  and revision ids), so a case varies a fact rather than a UUID draw.
- **Refusal cases assert the refusal code and `expected`/`observed`**, so a case cannot pass on a
  neighbouring refusal.

### Invariants And Boundaries

- **Nothing here publishes, archives, deletes or commits.** The store cases are hermetic: temporary
  directories and in-process APSW databases.
- **The synthetic half never restates the walk's logic.** It builds *recorded comparison output*, and the
  assertions are about what the walk concludes from it; the real-comparison case is what keeps the
  synthetic shape honest.
- **Boundary.** This module protects the detection contract's behaviour; it makes no requirement-acceptance
  claim on its own, and it does not re-measure the shipped comparison's own contracts, which belong to
  the diff modules' cases.

### Todos

None recorded. The manifest's retention is exercised as a recorded state transition against a supplied
destination observation rather than against a real published archive, because the durable publication
route does not exist on this branch — the packet's declared forward reference, not a gap this module
invented.

## Evidence

### Docs References

No domain documentation source is configured for this repository (`system/sources.md` carries no
`Domain Documentation` entries). The statements below are grounded in repository source only.

No configured domain documentation could be checked.

### Repo-Internal References

- **The scenario and its harmless control producing the same condition and the same signal identity, with no verdict on either.** [1]
- The grouped signal that retains every contributing match with its path and edges. [2]
- **The declared order as a total order over signal identity, independent of the order items were presented in.** [3]
- **An unsupported locator as a declared scope limitation rather than a negative match.** [4]
- The incomplete scan and the unmapped path advertised rather than dropped. [5]
- The probe outcome and the omission read from the comparison's own record. [6]
- The two-sided declaration refused rather than widened when one side was read. [7]
- **The walk over a real two-snapshot comparison, driven through the shipped application seam.** [8]
- **The write/read round trip: the recorded order served back, and the two-place versions.** [9]
- Two signals with different declared sets recorded on one run rather than collapsed into a run default. [10]
- **The agreement refusal that also asserts zero rows were written.** [11]
- **Requirement 7.1: a detection write into an assessed database refused, so the measurement cannot invalidate itself.** [12]
- **The recorded sequence that cannot be reordered or shortened, refused by generation 4's triggers.** [13]
- **A re-execution over a changed snapshot as a distinct run naming the difference.** [14]
- A moved policy version marking the run stale while its signals keep their recorded versions. [15]
- **Retention reported through the operation names the destination, and a worktree-local home is not retention.** [16]
- The exact inputs recorded as identities rather than as paths. [17]
- **The predating dataset: refused with both generation numbers as facts, migrated nowhere, table still absent.** [18]
- The synthetic build of union items, family memberships and anchor resolutions the conditions are provoked from. [19]
- The one anchor-resolution constructor every synthetic item is built through — re-cited at its own extent. [20]
- The real store fixture and the run assembled from a walk's signals. [21]
- The registered support fixtures this module consumes — **no new artifact and no new contract**. [22]
- The production entry points these cases drive. [23]
- **The sequence table's two triggers, which are what refuse a reorder or a shortening of a recorded run.** [24]
- The lane row this module is registered under, and the two catalog consumer rows it added. [25]

### Cross-Repo References

No cross-repository behavior is implemented in this file.

No meaningful cross-repo references found.
