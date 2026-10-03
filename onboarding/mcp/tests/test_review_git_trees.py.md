# mcp/tests/test_review_git_trees.py

## Governing Overview

[tests route overview](overview.md)

## Purpose

**The MIK-R25 cases for the reviewer on Git trees, and since MIK-L31 the focused-card read (19 collected): four
trees, pins, the tree view, reopen, legacy, the pin-naming round trip, the cards' entries, and the proof admission at
the route.** The `world` fixture is a coordination root holding one task (`task.json` with an
id) and one leaf enclosure, a code repository and a converted memory repository (`main` is the official line of
both; the memory commit carries the `Code-Commit` trailer), and the leaf's two linked worktrees on their work
branches. The leaf edits code and knowledge without committing, which is the live review's ordinary state. The
archive-hook cases moved to `test_review_artifact_cleanup.py` (ruling 2026-09-30T02:32:42, the test split); this
file is 1,022 lines after MIK-L31. It uses no shared support module, so there is no catalog change; it runs in the
`unit-regression` lane (`test-evidence-lanes.toml:123`).

## Current verification scope

The latest-attempt history proof clears the bounded live leaf-view memo after scratch fixture history mutations before recomputing. The actual latest-attempt subject rule and source _governing bytes are unchanged; this adjustment keeps fixture requests independent.

## Code Commentary

### Logic

- **Rule 1:** four trees with the uncommitted candidates pinned and reused; committed candidates need no ref and a
  failed pin refuses naming the repository and the ref; **a read writes only review refs and comparison objects,
  and a repeat writes nothing** (every ref, every object and every record file, bytes and mtime, compared by
  `_state`; ruling 22:22:37 Q5).
- **Rule 2 and 3:** the tree view shows the knowledge diff grouped by record and by source, the currentness per
  side and the worklist; a partial index shows its state on the affected side. Since MIK-L31 every key is
  snake_case, including the owners' own documents (`code_tree`, `tree_id`, `stale_members`, `owner_kind`; MIK-L25
  review F9), and the leaf-wide view carries no entries.
- **Rule 4:** a comparison reopens from its tree ids and names a tree Git can no longer produce (the refs deleted
  and both repositories garbage-collected; the code trees too, review F4); an unconverted before side is compared as
  its conversion; a comparison recorded before the conversion keeps its code sides only.
- **The no-`.sqlite` check:** every `apsw.Connection` and `sqlite3.connect` is recorded and every open lies inside
  `runtime/knowledge-index` (ruling 22:22:37 Q1).
- **Preservation:** an unconverted leaf keeps the dataset review; a tree comparison is never frozen into a dataset
  generation.
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

- These cases prove the candidate invariants recorded on `application/review_tree_comparison.py`: pins before
  display and idempotent re-reads; directory-name refs; `unavailable-history` never substituted; unconverted reads
  unchanged. Since MIK-L31 they also prove the one recorded on `application/review_tree_entries.py` (a card excerpt
  only from the pinned tree's exact blob, bounded, with per-side state) and the server half of the one on
  `application/review_tree_knowledge.py` (a numbered read answers for exactly that comparison).
- The radon D block `test_the_tree_view_shows_…` rose from D26 to D28 in MIK-L31 (review R1, pre-existing D).

### Todos

No additional work is asserted by this card.

## Evidence

### Docs References

No domain documentation source is configured; the requirement packet `MIK-R25@v1` lives outside the repositories.

No configured live documentation source was available for this pass.

### Repo-Internal References

- The converted-memory fixture world with its live leaf. [1]
- Pins and reuse. [2]
- A repeat read writes nothing. [3]
- Committed candidates and the refused pin. [4]
- The tree view (every key snake_case, no entries leaf-wide, the history row's `owner_kind`) and the partial index. [5]
- Reopen, the converted base, and the legacy comparison. [6]
- No database but the index; unconverted unchanged; never frozen. [7]
- Directory-name pins, and the route with the pinned numbered read, the cards read and the key bounds. [8]
- The cards read: four entries located on both sides, each helper's per-entry facts. [9]

- Unavailable against absent, and the history row found through `facts.row`. [10]

- The excerpt bound and the placement cache (review F3). [11]
- The proof admission at the route (review F12), with the asserted payload and tree IDs (R2-1). [12]
- The lane row. [13]

- Only an owner's latest attempt's row is shown; another owner's row stays. [14]

### Cross-Repo References

No cross-repo boundary is crossed by this file.
