# mcp/tests/test_onboarding_trace_gate.py

## Governing Overview

[tests route overview](overview.md)

## Purpose

**The MIK-R30@v1 gate cases on converted-format fixtures (15 cases).** The `leaf` fixture is a real code
repository and a real converted memory repository (`main` is the official line, its commit carries the
`Code-Commit` trailer naming the leaf's base) plus a leaf series contract: the inputs the curator's
memory-quality run and the closeout validator hand the gate. The file runs in the unit lane
(`test-evidence-lanes.toml`).

## Code Commentary

### Logic

- **Rule 3.** `test_only_an_anchors_blob_line_numbers_and_content_do_not_count` checks the counted-change
  rule field by field; `test_the_writers_mechanical_anchor_update_is_not_a_trace` runs the real writer carry
  and the item stays open.
- **Rule 2 and the examples.** `test_the_conforming_example_and_the_route_case` (a prose edit plus a
  "test-only rename" row; only the nearest route; `onboarding:overview` for a root-level file) and
  `test_a_missing_trace_is_one_named_repair_finding_and_the_closeout_refuses`.
- **Rows.** `test_rows_are_only_about_changed_files_and_the_registry_rule_is_both_halves` (unnecessary rows
  are report-only; the registered kind and `onboarding_item_open`);
  `test_a_moved_marker_row_satisfies_its_item_and_survives_a_rewrite` (rule 4).
- **Fail closed.** `test_mixed_formats_are_an_incomplete_side_never_a_vacuous_pass` (both mixed cases: the
  reason, the closeout refusal and the persisted `incomplete` worklist);
  `test_an_unreadable_sidecar_never_satisfies_a_trace` (a K_C sidecar corrupted beside a row and a Markdown
  edit: open, `countedChange` false, and `onboarding_item_open` open in both cases);
  `test_an_unreadable_base_sidecar_is_an_incomplete_input_and_a_repair_counts`;
  `test_unreadable_history_and_unestablished_sides_are_findings_never_a_pass`.
- **The converting leaf.** `test_the_conversion_itself_counts_for_nothing_at_the_converting_leaf` builds a
  legacy K_B (`_legacy_card`), converts it, and shows that only a change beyond the conversion counts. It also
  writes a `knowledge-worklist-base/v1` cache file and shows it is ignored and rewritten as v2.
- **Retired checks.** `test_converted_trees_get_no_verification_stamps_and_no_history_sort`.
- **Enforcement.** `test_the_memory_quality_run_counts_each_missing_trace_toward_the_actionable_count`
  drives the controller (`_run_controller`). Since MIK-R09 (leaf 260928-MIK-L09) `_run_controller` captures the real
  candidate trees (the gate judges exact trees), and the case asserts `curatorActionableCount` 3 and
  `knowledgeGate.openItemCount` 3, not 2: the gate counts each open item once, so the card's and the route's traces
  are joined by the uncovered file's `unexplained_hunk` (MIK-R10), which the card's own trace answers once it is
  written; `onboardingTrace.open` still names the two traces; `test_the_persisted_worklist_carries_the_onboarding_items_in_its_one_list`
  pins ruling Q2 and the `(kind, subject)` order; `test_an_unconverted_leaf_keeps_todays_gate_unchanged`
  asserts that the sides and the worklist are `None` and today's gate runs.
- **L37 (review R3-1).** `_run_controller` patches `run_memory_quality_check` with the module-level mock
  `_QUALITY_RUN`, and `test_the_memory_quality_run_counts_each_missing_trace_toward_the_actionable_count` now also
  asserts that the run's drift context carries a callable `knowledge_base`: the converted check is given its
  comparison base (MIK-R24 rule 7). No case was added.

### Conventions

- The file builds its own legacy fixture instead of consuming `knowledge_conversion_test_support.py`, so it
  adds no census-tracked consumer and needs no dependency-ownership re-pin.

### Invariants And Boundaries

- **The cases pin the architect rulings:** 18:49:50 (1: only a counted change or a row; 2: the items in the
  persisted worklist; 3: `onboarding:overview`; 4: the Markdown in the cache), 19:23:45 (N1, N2, N3, N5) and
  19:53:54 (R2-1, R2-2, R2-3).

### Todos

- None recorded.

## Evidence

### Docs References

No domain documentation source is configured for this repository (`system/sources.md` carries no
`Domain Documentation` entries). The design authority is the requirement packet `MIK-R30@v1` of task
`260928_maintained-invariant-knowledge`; it lives outside the code and memory repositories, so it is named
here and not cited as a row.

No configured live documentation source was available for this pass.

### Repo-Internal References

- The fixture's description: real repositories plus a leaf series contract. [1]
- The leaf fixture. [2]
- Only mechanical anchor fields never count. [3]
- The conforming example and the nearest route. [4]
- A missing trace is named and refused. [5]
- The writer's carry is not a trace. [6]
- Unnecessary rows and the registered rule. [7]
- Moved markers count and survive a rewrite. [8]
- Mixed formats refuse. [9]
- An unreadable K_C sidecar keeps its item open. [10]
- An unreadable K_B sidecar is an input problem; a repair counts. [11]
- Unreadable history and unestablished sides are findings. [12]
- The conversion counts for nothing; a v1 cache file is rewritten. [13]
- No stamps and no history sort on converted trees. [14]
- Each open item counts once toward `curatorActionableCount`: since MIK-R09 the two traces and the uncovered file's `unexplained_hunk` (3). [15]
- The items are in the persisted worklist. [16]
- An unconverted leaf keeps today's gate. [17]
- The unit-lane registration. [18]

- The memory-quality run gives the converted check its comparison base. [19]

### Cross-Repo References

No meaningful cross-repo references found: the fixtures are temporary repositories.

No cross-repo boundary is crossed by this file.
