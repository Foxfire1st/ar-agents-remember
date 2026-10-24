# mcp/tests/test_explainer_target.py

## Governing Overview

[Route overview](overview.md)

## Purpose

The real target reads over real Git objects and the one staleness answer composed from them, each case naming the row of the staleness table it proves.

## Code Commentary

- A whole blob is current while its bytes agree; a line range is mapped through the diff and hashed, and an unmappable range answers none rather than a neighbouring blob.
- Every question answers none when the trees cannot be read, so an unreadable target is never mistaken for a current one.
- A record is fingerprinted by its revision, its proof entry by execution and fingerprint, and its sidecar names a proof entry that records no id.
- A proof entry's changed fingerprint makes its claim stale, and an edited, moved or purely deleted hunk keeps its grade on the target block.
- A staleness read writes nothing in the repositories or the task.

## Evidence

- The case `test_a_line_range_maps_through_the_diff_and_hashes_the_same_bytes` protects a line range mapping through the diff and hashing the bytes it names. [1]
- The case `test_an_unmappable_range_and_a_blob_the_tree_lacks_answer_none` protects an unmappable range and a missing blob answering none. [2]
- The case `test_every_question_answers_none_when_the_trees_cannot_be_read` protects every read answering none when the trees cannot be read. [3]
- The case `test_a_proof_entries_changed_fingerprint_makes_its_claim_stale` protects a claim going stale when its proof entry's fingerprint changes. [4]
- The case `test_a_staleness_read_writes_nothing_in_the_repositories_or_the_task` protects a staleness read leaving every file untouched. [5]
- The case `test_an_edited_moved_or_purely_deleted_hunk_keeps_its_grade_on_the_target_block` protects an edited, moved or purely deleted hunk keeping its grade on its target block. [6]
