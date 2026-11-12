# mcp/tests/test_explainer_staleness.py

## Governing Overview

[Route overview](overview.md)

## Purpose

Block fingerprints, per-part staleness and the judgment sorts: which locators keep a grade across a shift, how each basis kind is fingerprinted, and which parts a page must call stale.

## Code Commentary

- A symbol and a held line range survive a line shift; a file locator never does, so a card on a file moves when the file changes anywhere.
- A side never read is uncomputable and an absent side is a deletion; an unexplained hunk is identified by its subject and span, a deletion by its base span.
- Merged hunks carry their grades onto one hunk, all stale, with the highest chip.
- Exactly the part resting on the changed blob is stale, and the trusted list and regeneration message name that part, its basis and its stale grade.
- The judgment sort orders by grade then priority and puts ungraded subjects last.

## Evidence

- The case `test_a_line_shift_keeps_a_symbol_and_a_held_line_range_but_never_a_file` protects which locators survive a line shift and which never do. [1]
- The case `test_a_card_side_never_read_is_uncomputable_and_an_absent_side_is_a_deletion` protects an unread side being uncomputable and an absent side a deletion. [2]
- The case `test_merged_hunks_carry_their_grades_onto_one_hunk_all_stale_with_the_highest_chip` protects merged hunks carrying their grades onto one stale hunk with the highest chip. [3]
- The case `test_exactly_the_part_resting_on_the_changed_blob_is_stale` protects only the part resting on the changed blob being stale. [4]
- The case `test_the_regeneration_message_names_the_part_its_changed_basis_and_the_stale_grade` protects the regeneration text naming the part, its basis and the stale grade. [5]
- The case `test_the_judgment_sort_orders_by_grade_then_priority_and_puts_the_ungraded_last` protects the judgment sort ordering by grade and priority with ungraded last. [6]
