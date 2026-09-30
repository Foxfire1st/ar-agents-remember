# mcp/tests/test_onboarding_trace_gate.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/test_onboarding_trace_gate.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-30T20:16:46+02:00 |
| lastVerifiedCommitHash | `c052b2593b85d9baf425cc1d5c46f384b13fc9ea`|
| lastVerifiedCommitDate | 2026-09-30T21:09:40+02:00|
| governingOverview | `overview.md` |

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

### Conventions

- The file builds its own legacy fixture instead of consuming `knowledge_conversion_test_support.py`, so it
  adds no census-tracked consumer and needs no dependency-ownership re-pin.

### Invariants And Boundaries

- **The cases pin the architect rulings:** 18:49:50 (1: only a counted change or a row; 2: the items in the
  persisted worklist; 3: `onboarding:overview`; 4: the Markdown in the cache), 19:23:45 (N1, N2, N3, N5) and
  19:53:54 (R2-1, R2-2, R2-3).

### Todos

- None recorded.

## Docs References

No domain documentation source is configured for this repository (`system/sources.md` carries no
`Domain Documentation` entries). The design authority is the requirement packet `MIK-R30@v1` of task
`260928_maintained-invariant-knowledge`; it lives outside the code and memory repositories, so it is named
here and not cited as a row.

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured live documentation source was available for this pass. | — | — |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The fixture's description: real repositories plus a leaf series contract. | "the inputs the curator's memory-quality run and the closeout validator hand the gate" | mcp/tests/test_onboarding_trace_gate.py:1-6 |
| The leaf fixture. | `Leaf`; `leaf` | mcp/tests/test_onboarding_trace_gate.py:149-195; mcp/tests/test_onboarding_trace_gate.py:198-224 |
| Only mechanical anchor fields never count. | `test_only_an_anchors_blob_line_numbers_and_content_do_not_count` | mcp/tests/test_onboarding_trace_gate.py:242-290 |
| The conforming example and the nearest route. | `test_the_conforming_example_and_the_route_case` | mcp/tests/test_onboarding_trace_gate.py:298-332 |
| A missing trace is named and refused. | `test_a_missing_trace_is_one_named_repair_finding_and_the_closeout_refuses` | mcp/tests/test_onboarding_trace_gate.py:335-349 |
| The writer's carry is not a trace. | `test_the_writers_mechanical_anchor_update_is_not_a_trace` | mcp/tests/test_onboarding_trace_gate.py:352-365 |
| Unnecessary rows and the registered rule. | `test_rows_are_only_about_changed_files_and_the_registry_rule_is_both_halves` | mcp/tests/test_onboarding_trace_gate.py:368-398 |
| Moved markers count and survive a rewrite. | `test_a_moved_marker_row_satisfies_its_item_and_survives_a_rewrite` | mcp/tests/test_onboarding_trace_gate.py:401-435 |
| Mixed formats refuse. | `test_mixed_formats_are_an_incomplete_side_never_a_vacuous_pass` | mcp/tests/test_onboarding_trace_gate.py:438-461 |
| An unreadable K_C sidecar keeps its item open. | `test_an_unreadable_sidecar_never_satisfies_a_trace` | mcp/tests/test_onboarding_trace_gate.py:464-488 |
| An unreadable K_B sidecar is an input problem; a repair counts. | `test_an_unreadable_base_sidecar_is_an_incomplete_input_and_a_repair_counts` | mcp/tests/test_onboarding_trace_gate.py:491-510 |
| Unreadable history and unestablished sides are findings. | `test_unreadable_history_and_unestablished_sides_are_findings_never_a_pass` | mcp/tests/test_onboarding_trace_gate.py:513-533 |
| The conversion counts for nothing; a v1 cache file is rewritten. | `test_the_conversion_itself_counts_for_nothing_at_the_converting_leaf` | mcp/tests/test_onboarding_trace_gate.py:552-604 |
| No stamps and no history sort on converted trees. | `test_converted_trees_get_no_verification_stamps_and_no_history_sort` | mcp/tests/test_onboarding_trace_gate.py:607-620 |
| Each open item counts once toward `curatorActionableCount`: since MIK-R09 the two traces and the uncovered file's `unexplained_hunk` (3). | `test_the_memory_quality_run_counts_each_missing_trace_toward_the_actionable_count` | mcp/tests/test_onboarding_trace_gate.py:702-722 |
| The items are in the persisted worklist. | `test_the_persisted_worklist_carries_the_onboarding_items_in_its_one_list` | mcp/tests/test_onboarding_trace_gate.py:725-747 |
| An unconverted leaf keeps today's gate. | `test_an_unconverted_leaf_keeps_todays_gate_unchanged` | mcp/tests/test_onboarding_trace_gate.py:750-757 |
| The unit-lane registration. | "mcp/tests/test_onboarding_trace_gate.py" | mcp/tests/test-evidence-lanes.toml:121-121 |

## Cross-Repo References

No meaningful cross-repo references found: the fixtures are temporary repositories.

| Finding | Anchor | Source |
| --- | --- | --- |
| No cross-repo boundary is crossed by this file. | — | — |

## Update History
- 2026-09-30T20:16:46+02:00 — 260928-MIK-L09 curator (staged change set on `ar/260928-mik-l09`, code base `904e804b07a598d5d6c66f06b7e67ddab64d9b8e`; review R1 changes-required, fix round, R2 pass-with-notes, round, R3 pass with R3-1 and R3-2 fixed): **body updated for MIK-R09.** The Enforcement bullet records that the controller helper captures real candidate trees and that the count is now 3 (the two traces plus the uncovered file's `unexplained_hunk`, each open item counted once by the gate). **Reopened claim reworded:** the test's row; this pass's generated bullet for it was removed. The other rows were re-pointed by the installed fixer (bullets kept), including the lane row (`:121`).
- 2026-09-30T18:03:31+00:00: Generated citation repair: `test_the_persisted_worklist_carries_the_onboarding_items_in_its_one_list` repointed to mcp/tests/test_onboarding_trace_gate.py:725-747. No content impact: mechanical anchor-range projection bound to citation source snapshot 803b19843e659566c7bfb6d3591c23e601f4ac3121f25212eee667285e1dec03; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-30T18:03:31+00:00: Generated citation repair: `test_an_unconverted_leaf_keeps_todays_gate_unchanged` repointed to mcp/tests/test_onboarding_trace_gate.py:750-757. No content impact: mechanical anchor-range projection bound to citation source snapshot 803b19843e659566c7bfb6d3591c23e601f4ac3121f25212eee667285e1dec03; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-30T18:03:31+00:00: Generated citation repair: "mcp/tests/test_onboarding_trace_gate.py" repointed to mcp/tests/test-evidence-lanes.toml:121-121. No content impact: mechanical anchor-range projection bound to citation source snapshot 803b19843e659566c7bfb6d3591c23e601f4ac3121f25212eee667285e1dec03; claim bytes unchanged; generated by ccr-r10@v1.

<!-- newest entry by date and time is prepended at the top of the list; prepend-only -->
- 2026-09-29T20:47:37+02:00 — 260928-MIK-L30 curator (uncommitted change set on `ar/260928-mik-l30`, code base `719acba61e491d0b7f1ee82dbeea5314ecec5083` plus the staged delta, including the untracked-then-staged new files): created this card for the new test file MIK-R30 adds (15 cases). The verification stamp is left empty: the file is new and uncommitted, so no commit yet holds the content it would claim to have verified; closeout owns the real stamp.
