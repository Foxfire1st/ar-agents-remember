# mcp/tests/test_review_git_trees.py

## Governing Overview

[tests route overview](overview.md)

## Purpose

Tests of the reviewer on Git trees: the four trees of a comparison, the pins, the tree view, reopening,
an unconverted side, archival, the route, the focused cards and the file read. The module also provides
the fixture `world` that the other reviewer test modules import.

## Code Commentary

### The fixture

`world` builds a coordination root with one task and one leaf enclosure, a code repository and a converted
memory repository whose `main` is the official line, and the leaf's two linked worktrees on their work
branches. `World.edit()` changes code and knowledge in the worktrees without committing, which is the
state a live review reads. `World.contract()` writes the leaf's enclosure contract.

### The cases

- **Comparison and pins.** A live review is four trees with its uncommitted candidates pinned, and a
  repeated read reuses the record. A read writes only review refs, comparison objects and the record, and
  a repeat writes nothing. Committed candidates need no ref, and a failed pin refuses naming the
  repository and the ref. Pins are named by the task directory, and archival removes them.
- **Tree view:** the renamed current test asserts per-side currentness, a computed bound worklist with history rows/linkage, no leaf-wide entries and absence of `knowledge_diff`; partial index state remains named per side.
- **Reopen and conversion:** converted-base and historical reopen assertions retain exact tree/side states. An unconverted leaf is now source-only with `legacy-unavailable` knowledge: no candidate database or review pins, refused tree read, measured source context and explicit intent-unavailable limitation. No current test asserts dataset-review preservation for that leaf.
- **Route.** The route serves the port, keeps a live leaf's computed worklist for a numbered read of its
  current comparison, passes named invariants to the port, answers 400 for a name longer than 64
  characters and for more than 500 names, and answers 503 when no port is wired.
- **Cards.** The cards read locates each entry of the named invariants on both code sides, names an
  unreadable side unavailable and a missing file absent, carries an excerpt longer than its bound as a
  marked prefix, and its placement cache remembers answers only and stays within its bound. An unchanged
  path that only a proof names opens in a tree review.
- **History rows.** `test_history_rows_are_found_by_the_row_subject_an_item_names` replaces the
  collaborator `isolated_leaf_worklist` of `review_tree_knowledge` with a function that first runs the real
  isolated computation, so the view records real reads, and then returns a prepared worklist document. It
  checks that the view shows the row whose subject an item names in `facts.row`, and that of one owner's
  rows only the row of the latest attempt file is shown.

### Logic

- **Rule 1:** four trees with the uncommitted candidates pinned and reused; committed candidates need no ref and a
  failed pin refuses naming the repository and the ref; **a read writes only review refs and comparison objects,
  and a repeat writes nothing** (every ref, every object and every record file, bytes and mtime, compared by
  `_state`; ruling 22:22:37 Q5).
- **Rule 2 and 3:** currentness is bound to each code tree (the edited after side is stale), and the computed/bound worklist has touched/reached subjects, history rows without currency marks and linked source hunks. `knowledge_diff` is absent and entries are read only per selection. Existing snake_case owner fields and partial-side index assertions remain.
- **Rule 4:** a comparison reopens from its tree ids and names a tree Git can no longer produce (the refs deleted
  and both repositories garbage-collected; the code trees too, review F4); an unconverted before side is compared as
  its conversion; a comparison recorded before the conversion keeps its code sides only.
- **The no-`.sqlite` check:** every `apsw.Connection` and `sqlite3.connect` is recorded and every open lies inside
  `runtime/knowledge-index` (ruling 22:22:37 Q1).
- **Current unconverted path:** source remains readable, knowledge is `legacy-unavailable`, tree view is refused, no candidate database exists and no pins are written. The retired dataset-preservation test is historical, not current evidence.
- **Naming:** pins are named by the task directory name, and archival removes them (ruling 02:32:42 (a); the one
  case here that calls the hook, to prove the round trip).
- **The route:** served over the port, and 503 when unwired. Since MIK-L31: the numbered read for the live leaf's
  current comparison keeps its `computed` worklist (review F11), a cards read passes its invariants to the port, a
  65-character key and 501 keys are each a 400 (review F10 and ruling Q2's bound).
- **The cards read (MIK-L31):**
  - `test_the_cards_read_locates_each_entry_of_the_named_invariants_on_both_code_sides`: K_C retires `keep`
    (RLZ-A00002), adds a proof PRF-A00003 and a realization of a gone name (RLZ-A00004); the four entries come back in
    order with one invariant key. The helpers assert one changed range with each side's own excerpt and MIK-R03
    state (`_changed_range`), the retired entry located on both sides with its text carried once and unrecorded
    after (`_retired_entry`), the proof's facet with no role (`_proof_entry`), and the unresolved entry with a reason
    and no range (`_unresolved_entry`). An identity no tree holds contributes nothing.
  - `test_the_cards_read_names_an_unreadable_side_unavailable_and_a_missing_file_absent`: a deleted file is
    `absent` and `changed`; an unreadable candidate tree is `unavailable` with its problem, `undetermined`, and no
    excerpt.
  - `test_history_rows_are_found_by_the_row_subject_an_item_names`: the PS-1 lookup through `facts.row`.
  - Review F3: `test_an_excerpt_longer_than_its_bound_is_a_stated_prefix` (a 500-line range gives the first 400
    lines with `excerpt_truncated`) and `test_the_placement_cache_remembers_answers_only_and_stays_within_its_bound`
    (an answer is remembered, a `CodeReadError` is asked again, the table evicts past its bound, `PLACEMENTS` is
    8,192).
  - Review F12 (ruling Q1 at the route): `test_an_unchanged_path_only_a_proof_names_opens_in_a_tree_review` adds an
    unchanged test file with its paired memory commit; before a proof exists the content read refuses it, after a
    K_C proof it is `attributed_unchanged` with the detail "a realization or proof recorded for the path in the
    comparison's after knowledge" naming "the after snapshot records a proof here". `_inventory` and `_named`
    assert the payload and the tree IDs before use (review R2-1's pyright fix).
- **L37.** `test_history_rows_are_found_by_the_row_subject_an_item_names` also writes the leaf's attempt-2 file
  with a row about the same subject, and another leaf's file: the worklist view shows the attempt-2 row for this
  leaf and the other owner's row, and no longer the first attempt's (a proof of INV-MS9BMJ).

### Conventions

- The module's docstring still ends "… archive" although the archive cases moved out (reviewer R6 note 3,
  cosmetic).

### Invariants And Boundaries

- Retained pins/reopen/index/card assertions remain source-bound. The unconverted path's current proof is source-only plus explicit unavailable knowledge, not the former unchanged dataset review. The removed grouped-knowledge-diff test and its historical radon grade are not current witnesses.

### Todos

No additional work is asserted by this card.

The renamed `test_the_tree_view_shows_currentness_per_side_and_the_worklist_without_a_knowledge_diff` asserts `"knowledge_diff" not in view.model_dump(by_alias=True)` alongside per-side currentness against each side's own code tree (body edit makes the after side stale), the computed bound worklist with items, history rows and gate linkage, and per-selection (never leaf-wide) card entries. The unconverted-base case carries the same absence assertion. Fixture, pin, legacy and archive behaviour are unchanged.
## Evidence

- The module docstring: the fixture world. [15]
- The fixture's state and helpers. [16]
- Four trees, pinned candidates, and reuse. [17]
- A repeat read writes nothing. [18]
- Reopening names a tree Git cannot produce. [20]
- The route serves the port and refuses without one. [21]
- Rows are found by the row subject an item names, through the real isolated computation. [22]

### Docs References

No domain documentation source is configured; the requirement packet `MIK-R25@v1` lives outside the repositories.

No configured live documentation source was available for this pass.

### Repo-Internal References

- The converted-memory fixture world with its live leaf. [23]
- Pins and reuse. [24]
- A repeat read writes nothing. [25]
- Committed candidates and the refused pin. [26]
- Reopen, the converted base, and the legacy comparison. [28]
- No database but the derived index; unconverted leaf is source-only with explicit legacy-unavailable knowledge. [29]
- Directory-name pins, and the route with the pinned numbered read, the cards read and the key bounds. [30]
- The cards read: four entries located on both sides, each helper's per-entry facts. [31]
- Unavailable against absent, and the history row found through `facts.row`. [32]
- The excerpt bound and the placement cache (review F3). [33]
- The proof admission at the route (review F12), with the asserted payload and tree IDs (R2-1). [34]
- The lane row. [35]
- Only an owner's latest attempt's row is shown; another owner's row stays. [36]

### Cross-Repo References

No cross-repo boundary is crossed by this file.

- The tree-view fixture preserves per-side currentness and computed linked worklist while omitting knowledge_diff. [19]
- The leaf-wide tree answer omits knowledge_diff and focused entries, keeps snake_case currentness and leaf-owned history rows; a separate case names the affected side’s partial index. [27]
- The leaf-wide tree answer omits knowledge_diff and focused entries, keeps snake_case currentness and leaf-owned history rows; a separate case names the affected side’s partial index. [37]
