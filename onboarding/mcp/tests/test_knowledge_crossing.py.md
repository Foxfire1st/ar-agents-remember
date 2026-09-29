# mcp/tests/test_knowledge_crossing.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/test_knowledge_crossing.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-29T14:21:42+02:00 |
| lastVerifiedCommitHash | `8b0254263c6998b1d4814b2e97c1bd231d39350f`|
| lastVerifiedCommitDate | 2026-09-29T15:00:35+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[tests route overview](overview.md)

## Purpose

**MIK-R24 rules 7 and 8: the converted base and the crossing sync.** The item rules are exercised on the
pure merge. The whole crossing (markers first, conversion of every unconverted side, structural merge,
validation at commit) runs through the real managed sync transaction on real Git repositories. Eight
cases in the `unit-regression` lane. The module also holds `validate_plan`, the step 5 check for the pure
plan, which moved here from the product (review R1 finding 7).

## Code Commentary

### Logic

- `test_items_merge_by_their_mechanical_and_authored_fields`: one side only, authored beats mechanical,
  incoming for mechanical-only, deleted against mechanical, and authored against authored conflicts.
- `test_a_reference_number_both_sides_added_conflicts_even_when_the_markdown_merges`: `references.2` is a
  `renumber one side` conflict while the Markdown merged.
- `test_a_crossing_moves_the_leaf_markers_converts_each_side_and_merges`: marker rows with `markers` and
  the fixed reason, `markersNotMoved` for a subject that already has a row, the incoming marker taken, the
  converted sides, and a valid plan.
- `test_many_long_markers_move_into_one_valid_history_row`: more than 20,000 characters of markers, a
  45,034-character line split into 3 pieces without loss, and a valid `HistoryFile` (ruling N1).
- `test_a_master_line_record_conflict_opens_a_crossing_history_file_closed_at_commit`: a conflicting
  statement opens `260101-FIX-crossing-1`, and `close_crossing_history` closes and stages it.
- `test_the_commit_route_validates_against_the_conversion_of_an_unconverted_base`: refused
  (`R22.6-base-converted`) without the converter, and passing with it, converted at the base's own
  `Code-Commit`.
- `test_the_managed_sync_crosses_an_unconverted_leaf_into_a_converted_line`: the sync gives an exact
  two-parent merge and the layout marker, the untouched card equals the line's bytes, the marker row lands
  in the leaf's history file, Update History is gone, and the journal names a report under
  `<group>/reports/`. The fixture's first, ordinary sync writes no `crossingReport` key (ruling N2).
- `test_a_crossing_leaves_overlapping_edits_to_the_curator_and_a_failed_step_changes_nothing`:
  - with the crossing unbound, the sync fails at `convert`, with `HEAD` unchanged and no `MERGE_HEAD`;
  - then the resolution lists `(lines)` and `references.1`, and the report holds all three notes;
  - the sidecar holds the marker, and `continue` with the marker staged is
    `sync-knowledge-validation-refused`;
  - once the item is resolved, the sync is `synced`.

### Conventions

- The managed-sync cases reuse `test_worktree_sync.SyncFixture`. The fixture's cancel-after-memory-conflict
  path fails identically on a plain, non-crossing memory conflict (a pre-existing fixture issue the
  reviewer reproduced), so the crossing's cancel-after-conflict path is not covered here.

### Invariants And Boundaries

- The cases pin the packet's failure behaviour: a crossing that cannot complete leaves the line unchanged
  and names the step, and a conflicted item is never committed as a silent "ours".

### Todos

The cancel-after-conflict path of a crossing is uncovered because of the pre-existing `SyncFixture`
issue above (reported to the coordinator).

## Docs References

No domain documentation source is configured for this repository (`system/sources.md` carries no
`Domain Documentation` entries). The design authority is the requirement packet `MIK-R24@v1` of task
`260928_maintained-invariant-knowledge` (with the architect rulings in the task's leaf document
`24_conversion-and-boundary-crossing.json`) and the coordination-root note Doc14
(`notes/ar-intent-reviewer-and-beyond/Doc14-text-canonical-knowledge-layout.md`); they live outside the
code and memory repositories, so they are named here and not cited as rows.

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured live documentation source was available for this pass. | — | — |

## Repo-Internal References

The cases and the plan check.

| Finding | Anchor | Source |
| --- | --- | --- |
| The step 5 check for a pure plan (test-only). | `validate_plan` | mcp/tests/test_knowledge_crossing.py:60-78 |
| The item rules. | `test_items_merge_by_their_mechanical_and_authored_fields` | mcp/tests/test_knowledge_crossing.py:93-110 |
| A reference-number collision. | `test_a_reference_number_both_sides_added_conflicts_even_when_the_markdown_merges` | mcp/tests/test_knowledge_crossing.py:124-152 |
| Markers first, conversion, merge. | `test_a_crossing_moves_the_leaf_markers_converts_each_side_and_merges` | mcp/tests/test_knowledge_crossing.py:162-214 |
| Long markers in one valid row. | `test_many_long_markers_move_into_one_valid_history_row` | mcp/tests/test_knowledge_crossing.py:217-243 |
| The master-line crossing history file. | `test_a_master_line_record_conflict_opens_a_crossing_history_file_closed_at_commit` | mcp/tests/test_knowledge_crossing.py:246-290 |
| The converted base at the base's own code commit. | `test_the_commit_route_validates_against_the_conversion_of_an_unconverted_base` | mcp/tests/test_knowledge_crossing.py:293-336 |
| The managed crossing sync, and an ordinary journal without the new key. | `test_the_managed_sync_crosses_an_unconverted_leaf_into_a_converted_line`; `_crossing_fixture` | mcp/tests/test_knowledge_crossing.py:403-431; mcp/tests/test_knowledge_crossing.py:339-365 |
| Overlapping edits reach the curator; a failed step changes nothing. | `test_a_crossing_leaves_overlapping_edits_to_the_curator_and_a_failed_step_changes_nothing` | mcp/tests/test_knowledge_crossing.py:434-499 |
| Its lane row. | "mcp/tests/test_knowledge_crossing.py" | mcp/tests/test-evidence-lanes.toml:109-109 |

## Cross-Repo References

No meaningful cross-repo references found: the fixtures are `tmp_path` Git repositories built by the tests themselves.

| Finding | Anchor | Source |
| --- | --- | --- |
| No cross-repo boundary is crossed by this file. | — | — |

## Update History

<!-- newest entry by date and time is prepended at the top of the list; prepend-only -->
- 2026-09-29T14:21:42+02:00 — 260928-MIK-L24 curator (uncommitted change set on `ar/260928-mik-l24`, code base `cd3e943d740b490d391722389af0a6bca0ccf93e` plus the working-tree delta and untracked files): created this card for the new file MIK-R24 adds. The verification stamp is left empty: the file is new and uncommitted, so no commit yet holds the content it would claim to have verified; closeout owns the real stamp.
