# mcp/tests/test_knowledge_crossing.py

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
  **Since MIK-R08** the case also checks the worklist recompute of a completed managed sync (rule 8): the
  first sync, with both memory sides unconverted, carries no `knowledgeWorklist`; the crossing sync into
  the converted line carries a `complete` one, persisted as `knowledge-worklist.json` beside the contract,
  whose pairing names the line's new code tip as B and the converted line head as K_B.
- `test_a_crossing_leaves_overlapping_edits_to_the_curator_and_a_failed_step_changes_nothing`:
  - with the crossing unbound, the sync fails at `convert`, with `HEAD` unchanged and no `MERGE_HEAD`;
  - then the resolution lists `(lines)` and `references.1`, and the report holds all three notes;
  - the sidecar holds the marker, and `continue` with the marker staged is
    `sync-knowledge-validation-refused`;
  - once the item is resolved, the sync is `synced`.
- **L37: the crossing owner's resolution, the writer's converted base, and cancel.**
  - `test_a_record_both_sides_changed_is_resolved_at_one_more_than_the_higher_side`, parametrised `own-converted`
    and `own-unconverted` (ONT's case): a real `cross()` and `apply_crossing()` leave the record unmerged; a new
    record for the crossing owner is refused; the resolution plus a `changed` row is written at `max(sides) + 1`.
    With the own side unconverted the writer validates against the converted base, with no false
    `R22.6-anchor-path` refusal.
  - `test_the_writer_compares_an_unconverted_head_through_its_converted_base`: unconverted `HEAD`, converted
    working tree: a meaning change is written at the next revision, the row's `before` anchor is the base's, one
    cache file is written and reused, an unbuildable base refuses by name, and a converted `HEAD` is used as it
    is.
  - `test_a_trailerless_head_converts_at_the_gates_code_base_and_an_unreadable_one_refuses` (review R1 F10b, X14,
    F6).
  - `_cancel_and_cross_again`, called inside the existing crossing case: a conflicted crossing cancels cleanly
    (the leaf's head, no merge, no converted file left) and the same sync then crosses again.

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

## Evidence

### Docs References

No domain documentation source is configured for this repository (`system/sources.md` carries no
`Domain Documentation` entries). The design authority is the requirement packet `MIK-R24@v1` of task
`260928_maintained-invariant-knowledge` (with the architect rulings in the task's leaf document
`24_conversion-and-boundary-crossing.json`) and the coordination-root note Doc14
(`notes/ar-intent-reviewer-and-beyond/Doc14-text-canonical-knowledge-layout.md`); they live outside the
code and memory repositories, so they are named here and not cited as rows.

No configured live documentation source was available for this pass.

### Repo-Internal References

The cases and the plan check.

- The step 5 check for a pure plan (test-only). [1]
- The item rules. [2]
- A reference-number collision. [3]
- Markers first, conversion, merge. [4]
- Long markers in one valid row. [5]
- The master-line crossing history file. [6]
- The converted base at the base's own code commit. [7]
- The managed crossing sync, and an ordinary journal without the new key. [8]
- The unconverted first sync carries no worklist; the crossing sync's worklist is complete and persisted at the new base pair. [9]
- Overlapping edits reach the curator; a failed step changes nothing. [10]
- Its lane row. [11]

- A record both sides changed is resolved at one more than the higher side, on a converted and an unconverted own side. [12]
- The writer compares an unconverted HEAD through its converted base. [13]
- A trailerless HEAD converts at the gate's code base, and an unreadable one refuses. [14]
- A conflicted crossing cancels cleanly and crosses again. [15]

### Cross-Repo References

No meaningful cross-repo references found: the fixtures are `tmp_path` Git repositories built by the tests themselves.

No cross-repo boundary is crossed by this file.
