# mcp/tests/test_canvas_explainer_grades.py

## Governing Overview

[Route overview](overview.md)

## Purpose

The grade store's meaning: a category's scale is its meaning, a grade is stored with the binding and fingerprint it was made at, and a reference that cannot be fingerprinted is refused rather than graded.

## Code Commentary

- A stored grade keeps its grade word, reason, fingerprint and binding, and reads back not stale.
- The same category name declared with another scale is refused, as is an unknown category or an off-scale grade word.
- A reference the caller could not fingerprint is refused outright, never stored as a grade.
- Removing a category takes its grades with it, and a block the target no longer holds is pruned and counted.

## Evidence

- The case `test_a_grade_is_the_judgment_it_was_made_as` protects a grade keeping the meaning, reason, fingerprint and binding it was made at. [1]
- The case `test_the_same_category_name_with_another_scale_is_refused` protects a category name that cannot be redefined on another scale. [2]
- The case `test_the_category_bound_is_named_and_removal_takes_its_grades` protects the named category bound and a removal taking its grades. 
- The case `test_a_reference_without_a_fingerprint_is_refused_not_graded` protects an unfingerprinted reference being refused instead of graded. [4]
- The case `test_a_gone_block_is_pruned_and_counted` protects a grade on a block the target no longer holds being pruned and counted. [5]

- Retired at the fifth freeze d59c3493: mcp/tests/test_canvas_explainer_grades.py::test_the_category_bound_is_named_and_removal_takes_its_grades - the region it cited is not in the file at the candidate and no re-point was possible; it was removed in commit 5f8398b32760677c370e3145add73cfa8388357b. Retired means the anchor no longer stands, not that the cited subject was deleted.
