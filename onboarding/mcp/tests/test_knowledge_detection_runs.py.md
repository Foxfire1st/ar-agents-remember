# mcp/tests/test_knowledge_detection_runs.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/test_knowledge_detection_runs.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-18T05:15+02:00 |
| lastVerifiedCommitHash | `3888cd8600e39a52c540d6038820759e3d4ffa7a`|
| lastVerifiedCommitDate | 2026-09-20T20:02:13+02:00|
| reviewedWorkingCandidate | `ar/260915-ks-l14` uncommitted source; base `4264dcc9decf50e64c863e9c6526ea09117be71b` |
| governingOverview | `overview.md` |

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

## Docs References

No domain documentation source is configured for this repository (`system/sources.md` carries no
`Domain Documentation` entries). The statements below are grounded in repository source only.

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured domain documentation could be checked. | — | — |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| **The scenario and its harmless control producing the same condition and the same signal identity, with no verdict on either.** | "test_a_budget_change_and_a_comments_only_change_produce_the_same_condition_and_signal" | mcp/tests/test_knowledge_detection_runs.py:293-324 |
| The grouped signal that retains every contributing match with its path and edges. | "test_a_grouped_signal_retains_every_contributing_match_with_its_path_and_edges" | mcp/tests/test_knowledge_detection_runs.py:325-338 |
| **The declared order as a total order over signal identity, independent of the order items were presented in.** | "test_the_declared_order_is_total_over_signal_identity_and_independent_of_item_order" | mcp/tests/test_knowledge_detection_runs.py:339-372 |
| **An unsupported locator as a declared scope limitation rather than a negative match.** | "test_an_unsupported_locator_is_a_declared_limitation_rather_than_a_negative_match" | mcp/tests/test_knowledge_detection_runs.py:373-399 |
| The incomplete scan and the unmapped path advertised rather than dropped. | "test_an_unmapped_changed_path_and_a_truncated_scan_are_advertised_rather_than_dropped" | mcp/tests/test_knowledge_detection_runs.py:400-420 |
| The probe outcome and the omission read from the comparison's own record. | "test_the_walk_declares_the_probe_and_the_omission_the_comparison_actually_recorded" | mcp/tests/test_knowledge_detection_runs.py:421-438 |
| The two-sided declaration refused rather than widened when one side was read. | "test_a_both_sides_declared_walk_over_one_side_is_refused_rather_than_widened" | mcp/tests/test_knowledge_detection_runs.py:439-453 |
| **The walk over a real two-snapshot comparison, driven through the shipped application seam.** | "test_the_walk_consumes_the_shipped_comparison_and_emits_facts_only_signals" | mcp/tests/test_knowledge_detection_runs.py:493-540 |
| **The write/read round trip: the recorded order served back, and the two-place versions.** | "test_a_recorded_run_reads_back_in_its_recorded_order_with_two_place_versions" | mcp/tests/test_knowledge_detection_runs.py:769-769 |
| Two signals with different declared sets recorded on one run rather than collapsed into a run default. | "test_two_signals_with_different_declared_sets_are_both_recorded_on_one_run" | mcp/tests/test_knowledge_detection_runs.py:818-818 |
| **The agreement refusal that also asserts zero rows were written.** | "test_a_signal_that_disagrees_with_its_run_is_refused_and_nothing_is_written"; "test_a_run_whose_declared_order_names_other_signals_is_refused" | mcp/tests/test_knowledge_detection_runs.py:864-864; mcp/tests/test_knowledge_detection_runs.py:892-892 |
| **Requirement 7.1: a detection write into an assessed database refused, so the measurement cannot invalidate itself.** | "test_a_detection_write_into_an_assessed_database_is_refused" | mcp/tests/test_knowledge_detection_runs.py:909-909 |
| **The recorded sequence that cannot be reordered or shortened, refused by generation 4's triggers.** | "test_a_recorded_detection_sequence_cannot_be_reordered_or_shortened" | mcp/tests/test_knowledge_detection_runs.py:946-946 |
| **A re-execution over a changed snapshot as a distinct run naming the difference.** | "test_a_reexecution_over_a_changed_snapshot_is_a_distinct_run_naming_the_difference" | mcp/tests/test_knowledge_detection_runs.py:981-981 |
| A moved policy version marking the run stale while its signals keep their recorded versions. | "test_a_run_whose_policy_version_moved_is_stale_and_its_signals_keep_their_versions" | mcp/tests/test_knowledge_detection_runs.py:1028-1028 |
| **Retention reported through the operation names the destination, and a worktree-local home is not retention.** | "test_a_manifest_reference_reported_through_the_operation_names_its_destination" | mcp/tests/test_knowledge_detection_runs.py:1058-1058 |
| The exact inputs recorded as identities rather than as paths. | "test_a_run_records_the_exact_inputs_it_read_as_identities" | mcp/tests/test_knowledge_detection_runs.py:1084-1084 |
| **The predating dataset: refused with both generation numbers as facts, migrated nowhere, table still absent.** | "test_a_detection_dataset_predating_generation_4_cannot_be_created_by_migration" | mcp/tests/test_knowledge_detection_runs.py:1108-1108 |
| The synthetic build of union items, family memberships and anchor resolutions the conditions are provoked from. | `realization_item`; `family_union`; `comparison`; `walk`; `ClaimSpec` | mcp/tests/test_knowledge_detection_runs.py:119-287 |
| The one anchor-resolution constructor every synthetic item is built through — re-cited at its own extent. | `anchor` | mcp/tests/test_knowledge_detection_runs.py:107-117 |
| The real store fixture and the run assembled from a walk's signals. | `detection_store`; `assembled_run`; `real_fixture`; `run_real_diff` | mcp/tests/test_knowledge_detection_runs.py:545-592; mcp/tests/test_knowledge_detection_runs.py:458-490; mcp/tests/test_knowledge_detection_runs.py:721-733; mcp/tests/test_knowledge_detection_runs.py:746-766 |
| The registered support fixtures this module consumes — **no new artifact and no new contract**. | `DiffFixture`; `build_diff_fixture` | mcp/tests/diff_scope_test_support.py:148-188; mcp/tests/diff_scope_test_support.py:189-215 |
| The production entry points these cases drive. | `record_detection_run`; `read_detection_run`; `detect_review_conditions`; `build_detection_run` | mcp/src/agents_remember/memory/knowledge/detection.py:263-289; mcp/src/agents_remember/memory/knowledge/detection.py:557-600; mcp/src/agents_remember/memory/knowledge/detection_walk.py:182-247; mcp/src/agents_remember/memory/knowledge/detection.py:144-173 |
| **The sequence table's two triggers, which are what refuse a reorder or a shortening of a recorded run.** | `APPENDED_TRIGGERS` | mcp/src/agents_remember/memory/knowledge/schema_v4.py:106-116 |
| The lane row this module is registered under, and the two catalog consumer rows it added. | "unit-regression = ["; "contract:knowledge-diff-cases" | mcp/tests/evidence-lifecycle.toml:1396-1396; mcp/tests/test-evidence-lanes.toml:5-5 |

## Cross-Repo References

No cross-repository behavior is implemented in this file.

| Finding | Anchor | Source |
| --- | --- | --- |
| No meaningful cross-repo references found. | — | — |

## Update History
- 2026-09-20T17:17:10+00:00: Generated citation repair: "unit-regression = ["; "contract:knowledge-diff-cases" repointed to mcp/tests/test-evidence-lanes.toml:5-5; mcp/tests/evidence-lifecycle.toml:1396-1396. No content impact: mechanical anchor-range projection bound to citation source snapshot 02d8f0b256fe50bf7458ae56160b7e02e4466423e76d3ab197e12477f370f5b8; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-20T03:57:45+00:00: Generated citation repair: "unit-regression = ["; "contract:knowledge-diff-cases" repointed to mcp/tests/test-evidence-lanes.toml:5-5; mcp/tests/evidence-lifecycle.toml:1398-1398. No content impact: mechanical anchor-range projection bound to citation source snapshot ef4a9932e0393a408ecd0f26b5bc2e0e1e335ad90b9e47a16092ffd6f3403af3; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-20T00:16:01+00:00: Generated citation repair: "unit-regression = ["; "contract:knowledge-diff-cases" repointed to mcp/tests/test-evidence-lanes.toml:5-5; mcp/tests/evidence-lifecycle.toml:1396-1396. No content impact: mechanical anchor-range projection bound to citation source snapshot b8fe5b3589f1357e836aaad1587e69ed38bbda0d58221eaa2150e96eb0561e93; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-19T22:28:52+00:00: Generated citation repair: "unit-regression = ["; "contract:knowledge-diff-cases" repointed to mcp/tests/test-evidence-lanes.toml:5-5; mcp/tests/evidence-lifecycle.toml:1394-1394. No content impact: mechanical anchor-range projection bound to citation source snapshot 440311ed835ff15c77271ad85c2bef2103d2b46ebe061b96476b211b3d19cd24; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T20:45:09+02:00 — 260915-KS-L23 post-closeout clearance (change set on `ar/260915-ks-l23`, memory base `ce3028e9`, code `5e4eb651`): **cleared the 1 enforced `citation_anchor_absent_from_range` row in this document.** The closeout's own code commit appended one `consumers` registration above every construct these cards cite, so each cited range ended exactly one line above the line that now carries the anchor row. Widened to the carrying line: `mcp/tests/evidence-lifecycle.toml:1390-1390` → `mcp/tests/evidence-lifecycle.toml:1390-1391` (row 179). Every line the author cited stays inside its range; no claim, Anchor cell or other range was dropped or re-worded, and each named anchor now resolves inside the widened range.
- 2026-09-18T19:53:42+02:00 — 260915-KS-L23 residue clearance, seat B (uncommitted change set on `ar/260915-ks-l23`, memory base `59eab7a0`): **cleared the two enforced `citation_anchor_absent_from_range` rows in this document** (one table row, two anchors). The row names four helpers but carried two ranges: `458-490` (the real-diff walk) and `545-592` (the `run_real_diff` signature), neither of which holds the fixture at `721-733` (`detection_store`) or the assembler at `746-766` (`assembled_run`). Both ranges that carried the other two anchors were kept as they are and the two that carry these anchors were added to the cell, which is the same additive repair this document's own 2026-09-17 entry records for the `status_payload` anchor. The claim, all four anchors and the two original ranges are unchanged. No claim was re-worded, no anchor or range was dropped to silence a row, and no verification stamp advanced: the candidate is uncommitted and the governed closeout owns the real code and memory commits.
- 2026-09-18T17:30:57+00:00: Generated citation repair: "test_a_recorded_run_reads_back_in_its_recorded_order_with_two_place_versions" repointed to mcp/tests/test_knowledge_detection_runs.py:769-769. No content impact: mechanical anchor-range projection bound to citation source snapshot 90ac134ffc3f8e781bc1feb4daa6ea3e6fd982366fb532c5a9c6ca2e3d9aa040; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T17:30:57+00:00: Generated citation repair: "test_two_signals_with_different_declared_sets_are_both_recorded_on_one_run" repointed to mcp/tests/test_knowledge_detection_runs.py:818-818. No content impact: mechanical anchor-range projection bound to citation source snapshot 90ac134ffc3f8e781bc1feb4daa6ea3e6fd982366fb532c5a9c6ca2e3d9aa040; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T17:30:57+00:00: Generated citation repair: "test_a_signal_that_disagrees_with_its_run_is_refused_and_nothing_is_written"; "test_a_run_whose_declared_order_names_other_signals_is_refused" repointed to mcp/tests/test_knowledge_detection_runs.py:864-864; mcp/tests/test_knowledge_detection_runs.py:892-892. No content impact: mechanical anchor-range projection bound to citation source snapshot 90ac134ffc3f8e781bc1feb4daa6ea3e6fd982366fb532c5a9c6ca2e3d9aa040; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T17:30:57+00:00: Generated citation repair: "test_a_detection_write_into_an_assessed_database_is_refused" repointed to mcp/tests/test_knowledge_detection_runs.py:909-909. No content impact: mechanical anchor-range projection bound to citation source snapshot 90ac134ffc3f8e781bc1feb4daa6ea3e6fd982366fb532c5a9c6ca2e3d9aa040; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T17:30:57+00:00: Generated citation repair: "test_a_recorded_detection_sequence_cannot_be_reordered_or_shortened" repointed to mcp/tests/test_knowledge_detection_runs.py:946-946. No content impact: mechanical anchor-range projection bound to citation source snapshot 90ac134ffc3f8e781bc1feb4daa6ea3e6fd982366fb532c5a9c6ca2e3d9aa040; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T17:30:57+00:00: Generated citation repair: "test_a_reexecution_over_a_changed_snapshot_is_a_distinct_run_naming_the_difference" repointed to mcp/tests/test_knowledge_detection_runs.py:981-981. No content impact: mechanical anchor-range projection bound to citation source snapshot 90ac134ffc3f8e781bc1feb4daa6ea3e6fd982366fb532c5a9c6ca2e3d9aa040; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T17:30:57+00:00: Generated citation repair: "test_a_run_whose_policy_version_moved_is_stale_and_its_signals_keep_their_versions" repointed to mcp/tests/test_knowledge_detection_runs.py:1028-1028. No content impact: mechanical anchor-range projection bound to citation source snapshot 90ac134ffc3f8e781bc1feb4daa6ea3e6fd982366fb532c5a9c6ca2e3d9aa040; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T17:30:57+00:00: Generated citation repair: "test_a_manifest_reference_reported_through_the_operation_names_its_destination" repointed to mcp/tests/test_knowledge_detection_runs.py:1058-1058. No content impact: mechanical anchor-range projection bound to citation source snapshot 90ac134ffc3f8e781bc1feb4daa6ea3e6fd982366fb532c5a9c6ca2e3d9aa040; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T17:30:57+00:00: Generated citation repair: "test_a_run_records_the_exact_inputs_it_read_as_identities" repointed to mcp/tests/test_knowledge_detection_runs.py:1084-1084. No content impact: mechanical anchor-range projection bound to citation source snapshot 90ac134ffc3f8e781bc1feb4daa6ea3e6fd982366fb532c5a9c6ca2e3d9aa040; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T17:30:57+00:00: Generated citation repair: "test_a_detection_dataset_predating_generation_4_cannot_be_created_by_migration" repointed to mcp/tests/test_knowledge_detection_runs.py:1108-1108. No content impact: mechanical anchor-range projection bound to citation source snapshot 90ac134ffc3f8e781bc1feb4daa6ea3e6fd982366fb532c5a9c6ca2e3d9aa040; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T17:30:57+00:00: Generated citation repair: "unit-regression = ["; "contract:knowledge-diff-cases" repointed to mcp/tests/test-evidence-lanes.toml:5-5; mcp/tests/evidence-lifecycle.toml:1390-1390. No content impact: mechanical anchor-range projection bound to citation source snapshot 90ac134ffc3f8e781bc1feb4daa6ea3e6fd982366fb532c5a9c6ca2e3d9aa040; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T19:28+02:00 — 260915-KS-L23 curator (uncommitted change set on `ar/260915-ks-l23`, base `c5a74a85`): recorded the case this pass added, and corrected the module's case count. The module now holds **20** cases (measured by AST over collected node names: 20 test functions, none parametrized, none marked integration), not the 19 the card stated. The new case is `test_a_run_over_the_shipped_comparison_names_every_signal_once_and_is_recorded` (`test_knowledge_detection_runs.py:597-714`), with helpers `real_input_sides` (`:544-582`) and `claim_records_spoken_for_twice` (`:585-594`); it exercises the duplicate-`signal_id` defect end to end on the shipped comparison — uniqueness, one signal per removed item, identity stability under a reversed item order, and a real `record_detection_run`/`read_detection_run` round trip — and the Logic, the Conventions and the Purpose now state it, including the two facts that make it a delivery case rather than a walk asserted beside one (the fixture precondition is asserted, and both input sides are named by their own datasets' logical digests). The additions are 3 import lines plus 2 helpers plus 1 case; **every existing case's cited range in the table above has therefore shifted**, which is reported rather than patched here because the citation-range repair pass owns those rows. No row, citation or range was rewritten by hand and no verification stamp advanced (the source is uncommitted and closeout owns the stamp).
- 2026-09-18T15:12:32+00:00: Generated citation repair: "unit-regression = ["; "contract:knowledge-diff-cases" repointed to mcp/tests/test-evidence-lanes.toml:5-5; mcp/tests/evidence-lifecycle.toml:1386-1386. No content impact: mechanical anchor-range projection bound to citation source snapshot 418f5ce580b3710b5d8fe417585d48fd22eccd55346c84b05f01fef243a17917; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T10:45:13+00:00: Generated citation repair: "unit-regression = ["; "contract:knowledge-diff-cases" repointed to mcp/tests/test-evidence-lanes.toml:5-5; mcp/tests/evidence-lifecycle.toml:1382-1382. No content impact: mechanical anchor-range projection bound to citation source snapshot a1ce4e2ec12e0f7b6d953d252db00653f23138548de5122388515485a9e05d23; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T05:15+02:00 — 260915-KS-L14 curator (uncommitted change set on `ar/260915-ks-l14`, base `4264dcc9`): created this one-to-one card for the new unit-regression suite over the detection *run*. It records the two halves (a synthetic half that provokes each condition exactly, and a store half that drives the real write and read paths), the scenario/control case that is the responsibility boundary's acceptance shape, the declared order that is total and independent of item order, the unsupported locator as a declared limitation rather than a negative match, the one case that runs a **real** two-snapshot comparison through the shipped application seam, the round trip that serves the recorded order back with the two-place versions, the agreement refusals that also assert nothing was written, requirement 7.1's self-reference refusal, the sequence sealed by generation 4's triggers rather than by the operation alone, the distinct-run re-execution, the stale-but-unreinterpreted run, retention that names its destination, and the predating dataset refused with both generation numbers. It records that this module consumes the already-registered `diff_scope_test_support` fixture and therefore added **no** governed evidence artifact — the catalog's counts stay thirteen contracts and fifty-four artifacts, with two consumer rows added. Verification metadata is the leaf's base commit `4264dcc9`: the code commit does not exist yet and closeout owns that stamp.
