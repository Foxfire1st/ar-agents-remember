# mcp/tests/test_dependent_version_only_change.py

## Governing Overview

[Tests route overview](overview.md)

## Purpose

Exercise the dependent whole-file version exception through both a converted-memory reader and landing document-staleness computation at exact Git trees. These are source assertions; this card does not claim a fresh test run.

## Current contract

The fixture writes `project.version`, the installed-metadata resolver shape and a lockfile, then confirms a dependent against an exact commit/code tree. Both consumers select committed code and the same converted-memory dependent record. A product-only change is current for the metadata, resolver-shaped module, lockfile and document links. An unchanged dependency token or unchanged old product mention may remain beside a replaced product token.

A change to other prose or whitespace moves the link. A distinguishable changed dependency token also moves it, including an epoch, an extra release component, pre/post/dev/local parts and an embedded product-looking local fragment. A leading `v` is preserved as part of the exact product substitution.

The version identity comes from the selected code tree rather than later working-file text. An unavailable confirmation revision, missing project version or uncommitted confirmation without an exact code tree excuses no changed file.

Text comparison cannot distinguish a dependency whose complete old and new tokens exactly equal the product's: the equal-token case is current in both consumers. This is the architect-ruled weakness of the rule, not a claim that dependency ownership was established.

## Evidence

- `_state` selects the reader or landing consumer over real converted-memory records.
- `test_a_bump_of_the_products_own_version_does_not_move_a_file_link` covers four linked file types.
- The unchanged-dependency/old-mention tests preserve unchanged tokens.
- The changed-byte, whitespace, dependency and complete-token tests distinguish other changes.
- The leading-v and equal-complete-token tests state the admitted boundary and its weakness.
- The selected-tree and unreadable-confirmation tests retain provenance requirements.

- Source assertion: `_state`. [1]
- Source assertion: `test_a_bump_of_the_products_own_version_does_not_move_a_file_link`. [2]
- Source assertion: `test_an_unchanged_dependency_version_does_not_hide_a_product_only_change`. [3]
- Source assertion: `test_an_old_version_mention_can_stay_beside_a_replaced_one`. [4]
- Source assertion: `test_any_other_changed_byte_still_moves_the_link`. [5]
- Source assertion: `test_a_changed_dependency_version_still_moves`. [6]
- Source assertion: `test_a_changed_complete_dependency_version_still_moves`. [7]
- Source assertion: `test_a_leading_v_tag_keeps_the_products_version_identity`. [8]
- Source assertion: `test_an_equal_complete_dependency_version_is_textually_indistinguishable`. [9]
- Source assertion: `test_a_whitespace_only_change_still_moves`. [10]
- Source assertion: `test_version_identity_comes_from_the_selected_tree_not_working_files`. [11]
- Source assertion: `test_an_unreadable_old_product_version_does_not_excuse_a_changed_file`. [12]
