# mcp/tests/test_evidence_catalog_canonical_form.py

## Governing Overview

[mcp/tests route overview](overview.md)

## Purpose

The cases for the canonical form of the two test catalogs
(`mcp/tests/evidence-lifecycle.toml`, `mcp/tests/test-evidence-lanes.toml`): both loaders refuse a
catalog that is not canonical, the command `evidence_lifecycle --write` repairs it without making a
decision, and Git merges the catalogs by union without leaving an unchecked result. The cases drive
the real loaders, the real command entry (`main`), real Git and the real pytest start-up hook, most
of them over a small synthetic repository.

## Code Commentary

### The synthetic repository

`synthetic_repo` builds a committed Git repository under the test's temporary directory:

- a `pyproject.toml` that names `mcp/tests` as the test path, a governed artifact
  `mcp/tests/_catalog_anchor.py`, and the test modules `alpha` and `beta` (plus any `idle` modules
  the case asks for, which are in a lane but read no governed artifact);
- a lane manifest that lists every module in `unit-regression` (`write_lanes` writes every
  accepting lane, the others empty);
- a lifecycle catalog from the shared builder `write_synthetic_evidence_catalog`, with the anchor
  consumed by `alpha` and `beta` and the lane manifest, which is governed evidence itself, consumed
  by `alpha`;
- a `.gitattributes` that holds the `merge=union` lines copied from the real repository's file.

It commits everything on branch `main` and asserts that the validator passes. `add_test_module`
writes a test module that names the artifacts it reads in a literal tuple, the way the builder
does. `insert_line` adds one line before the closing bracket of a list, the edit a change makes by
hand. `write_command` and `validator` call `main` with and without `--write` and return the exit
code and the printed text.

### The real catalogs

- `test_the_repository_catalogs_are_in_canonical_form` loads both real catalogs through their
  loaders; a catalog that is not canonical would be refused.
- `test_both_catalogs_merge_by_union` asks `git check-attr merge` for both catalog paths in the real
  repository and expects `union` for each.

### Refusal at the loaders

- `test_a_consumer_list_out_of_order_is_refused_then_repaired`: the lifecycle loader names the
  artifact, says `consumers is out of order` and names the command; the command reports the list as
  reordered and the validator passes.
- `test_a_duplicate_consumer_is_refused_and_removed`: `consumers holds duplicates`; the command
  reports one removed duplicate line.
- `test_rows_are_ordered_by_key_and_none_is_added_or_removed`: an artifact row appended out of order
  is refused (`artifact row is out of order`); after the command the paths are sorted and the row
  count is unchanged.
- `test_contract_rows_are_ordered_by_id`: a contract row out of order is refused by name; the
  command reports `contract rows reordered`.
- `test_the_lane_loader_names_an_unordered_lane_and_a_duplicated_path`: the lane loader names the
  lane (`unit-regression: lane list is out of order`) and the command; a path listed twice in one
  lane is `lane list holds duplicates` and is not reported as `conflicting file lanes`.
- `test_the_validator_also_refuses_a_lane_manifest_that_is_not_canonical`: the validator command
  returns 1 for an unordered lane list, and 0 after the command ran.
- `test_a_list_with_two_paths_on_one_line_is_refused_then_rewritten` (a `consumers` list and a lane
  list): the validator names the row or lane, says the list `is not written with one path per line`
  and names the command; the command reports `whitespace normalised` and restores the file's text.
- `test_both_loaders_explain_an_interleaved_file`: for each catalog in turn, a file that does not
  parse is refused with the sentence `interleaved by the merge`.
- `test_pytest_start_up_explains_a_lane_manifest_that_does_not_parse`: `conftest.pytest_configure`,
  the first read of a test run, raises a `pytest.UsageError` that names the manifest file and holds
  the same sentence.
- `test_test_selection_names_a_base_catalog_that_does_not_parse`: the `HEAD` of the synthetic
  repository holds a lifecycle catalog that does not parse; test selection against that base returns
  one unresolved input whose detail names the catalog at the base revision and holds the sentence
  about interleaved rows.
- `test_a_test_run_prints_the_lane_refusal_once_with_the_command` (a test file without a lane line
  and a lane list out of order, each without workers and with `-n=4 --dist loadfile`): it starts a
  real pytest process on the synthetic repository under the test's temporary directory, with a
  limit of 30 seconds, and expects exit code 4, the finding exactly once, the command, and neither
  `INTERNALERROR` nor a traceback.
- `test_the_validator_derives_the_source_graph_once_for_both_catalogs`: one validator run calls
  `RepositoryDependencyFacts.build` once, and a test file without a lane still fails the run.

### The command

- `test_the_command_derives_a_missing_and_drops_an_unsupported_consumer`: a new module that reads
  the anchor is added to the list and a listed module that does not exist is dropped. The case also
  removes a real consumer from the list beforehand; the validator passes after the command, which
  it can only do when that consumer is listed again.
- `test_the_command_derives_an_exact_source_consumer_list`: for an `exact-source` row the list
  becomes the source file that references the artifact.
- `test_the_second_run_changes_nothing_and_comments_survive`: after one run both files are
  byte-identical on a second run, which prints `already canonical`; a comment above `[files]` and a
  comment above an `[[artifact]]` header are still in place.
- `test_a_table_header_followed_by_a_comment_is_read_and_keeps_its_comment`: rows under
  `[[artifact]] # why this row` are ordered and their lists rewritten, and both header comments
  stay.
- `test_a_lane_manifest_without_a_files_table_is_refused_by_name_at_every_entry_point`: the lane
  loader, the validator, the command and the pytest start-up each refuse a manifest with no
  `[files]` table by that name.
- `test_a_list_with_other_quotes_or_commas_is_refused_and_the_command_says_what_it_rewrote`: a
  list whose quotes or commas are not canonical is reported by the loaders and rewritten by the
  command, which names the form it wrote in the report.
- `test_the_command_changes_no_field_of_a_row_but_its_consumers`: with rows of both kinds out of
  order, a list that is out of order with a duplicate and an unsupported consumer, and fields
  written by hand (a literal string, extra spaces, escaped quotes, a comment after a value, a
  comment between two fields, a comment above a header), every line of every row other than its
  `consumers` list is the same after the command, and so are the lines above the first row.
- `test_a_whitespace_only_change_is_reported`: trailing spaces are removed and reported as
  `whitespace normalised`, not as `already canonical`.
- `test_a_row_whose_artifact_file_is_gone_is_named_and_never_removed`: the command prints that the
  artifact file does not exist and keeps the row; the validator then refuses the row by name.
- `test_a_row_without_a_derived_consumer_keeps_every_consumer_that_exists`: for two rows that no
  module reads, the command removes the line of a missing file from the row that also lists an
  existing consumer, keeps the only line of the row that lists nothing else, and prints for both
  that the source tree shows no consumer.
- Refusals that write nothing, each checked by comparing the bytes of the catalogs before and after:
  an unparseable catalog (`test_the_command_refuses_an_unparseable_catalog_without_writing`, which
  also expects the interleaving sentence); incomplete dependency facts because a test module does
  not parse (`test_the_command_refuses_incomplete_dependency_facts_without_writing`); ambiguous
  module names (`test_the_command_refuses_ambiguous_modules_without_writing`); a directory that is
  not a Git repository (`test_the_command_refuses_a_directory_that_is_not_a_git_repository`); an
  artifact row or a contract row listed twice
  (`test_the_command_refuses_a_row_listed_twice_and_names_it`, where the loader says
  `duplicate catalog entry` or `duplicate contract identity` and the command adds the advice for a
  side that was not in canonical order); a catalog with CRLF line endings
  (`test_a_catalog_with_crlf_line_endings_is_refused_and_left_alone`, where the other catalog holds
  a repairable duplicate and is left alone too); a comment inside a lane list
  (`test_a_refusal_for_the_lane_manifest_leaves_a_repairable_lifecycle_catalog_alone`, where the
  lifecycle catalog holds a repairable duplicate and is not written either); and five forms the
  line rewrite does not read
  (`test_a_form_the_command_does_not_read_is_refused_and_nothing_is_written`: an indented table
  header, a lane manifest whose `[files]` header the line scan does not read, `consumers=[`, a lane
  key without spaces, and a list whose `]` stands on the line of its last path). The validator
  refuses each of those five forms too.

### Git merging

`start_sync` adds a second worktree on a branch `leaf`; `land` commits a change on `main`. `reapply`
does what `worktree_sync` does: it parks the leaf's work with
`git stash push --include-untracked`, merges `main`, and applies the stash. It asserts whether the
merge produced a merge commit, as the case expects.

- `test_two_changes_that_add_a_test_file_at_the_same_place_sync_without_a_stop`: the leaf and the
  landed change each add a test module to the same consumer list and the same lane. The stash
  applies with exit code 0, no path is unmerged, both modules are in both catalogs, and after the
  command the validator passes.
- `test_the_same_line_on_both_sides_is_refused_with_the_command_then_removed`: both sides add the
  same consumer line with different neighbours. The reapply succeeds and leaves the line twice; the
  validator refuses with `holds duplicates` and the command; the command removes one copy.
- `test_two_whole_rows_at_the_same_place_end_in_the_refusal_that_says_what_to_do`: both sides append
  a whole artifact row at the end of the catalog. The lifecycle loader refuses the result with the
  sentence about interleaved rows and the instruction to restore the file from the landed commit.
  The case then follows that instruction (`git checkout HEAD` of the catalog, the leaf's row added
  again, the command) and the validator passes.
- `test_a_line_the_union_brings_back_for_a_deleted_file_is_refused_then_removed`: the landed change
  deletes a test file with its lane line and its consumer line, and the leaf adds lines next to
  them. The reapply succeeds without an unmerged path and both deleted lines are back. The
  validator refuses the missing consumer and names the command, the lane loader refuses the lane
  line of the missing file and names the command, and the command removes both lines and prints
  them; the validator then passes.
- `test_two_branches_that_both_changed_the_lists_merge_with_a_merge_commit`: the leaf has committed
  its change; `git merge main` creates a merge commit without an unmerged path.
- `test_parked_work_is_reapplied_over_a_merge_commit_without_a_stop`: the leaf has a commit and
  uncommitted work; park, merge and apply complete, and all three modules are in the catalog.

## Evidence

- The module states that every case drives the real loaders, the real command or real Git over a synthetic repository. [1]
- The synthetic repository is canonical, valid and committed, with the union attribute copied from the real file. [2]
- Both real catalogs load through their loaders. [3]
- Git reports the union merge attribute for both catalogs. [4]
- An unordered consumer list is refused by name with the command, then repaired. [5]
- The lane loader names the lane and does not call a duplicate a conflict. [6]
- A second run leaves both files byte-identical and comments in place. [7]
- An unparseable catalog is refused by the command and nothing is written. [8]
- The reapply helper parks, merges and applies, and asserts the kind of merge. [9]
- Two changes at the same place reapply without an unmerged path. [10]
- The same line on both sides stays twice, is refused, and is removed by the command. [11]
- Two whole rows at the same place end in the refusal that says how to recover, and the recovery passes. [12]
- The loaders and the command entry under test. [13]
- The rewrite under test. [14]
- Every line of a row other than its consumers list keeps its bytes. [15]
- A line that the union brings back for a deleted file is refused by both loaders and removed by the command. [17]
- The pytest start-up hook explains a lane manifest that does not parse. [19]
- The validator derives the source graph once. [20]

- The pytest start-up and the command refuse a lane manifest without a `[files]` table by name. [21]
- A list with non-canonical quotes or commas is reported and rewritten with a named report line. [22]

- Five forms the line rewrite does not read are refused by the validator and by the command. [23]
- A list with two paths on one line is refused and rewritten. [24]
