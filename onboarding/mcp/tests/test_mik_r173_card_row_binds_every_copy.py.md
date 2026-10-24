# mcp/tests/test_mik_r173_card_row_binds_every_copy.py

## Governing Overview

[Tests route overview](overview.md)

## Purpose

A card row binds every copy of its source (MIK-R173): a group of two identical copies (canonical and packaged) deleted or reworded at the
candidate is bound by one card row, and the worklist item the row answers closes. A single-source card keeps
today's one-source row, and an overview row keeps its refusal while binding its item's files.

## Code Commentary

### Logic

`_grouped_leaf()` builds the two identical copies at the code base with the one card that owns them, `_rebased()`
re-bases the leaf contract on the commits holding the group and its card, `_blob()` reads a path's blob at the
candidate the writer and the worklist both read, and `_writer()` runs one committing leaf whose whole document
is a `no_impact` row for the subject. `_trace_item()` reads the leaf's own `onboarding_trace` item out of its
worklist run.

- **Deleted group.** `test_a_card_row_binds_every_copy_of_its_source` binds both copies and the item closes.
- **Reworded group.** `test_a_grouped_card_row_binds_the_copies_blobs_when_they_are_present` binds each copy's own
  blob when the copies are present at the candidate.
- **One source.** `test_a_single_source_card_row_is_unchanged` keeps the one-source row, whichever way the source
  is named.
- **Overview.** `test_an_overview_row_keeps_its_refusal_and_binds_its_items_sources` keeps the refusal for an
  uncovered overview and binds the files of a covered one.
- **Author input.** `test_an_author_supplied_sources_field_is_still_refused` keeps `RowRequest` as it is: the
  sources are the writer's, never the curator's input.

### Conventions

The row is read back from the stored history the writer wrote, not from the writer's answer, so a row that is
reported but not stored fails.

### Invariants And Boundaries

- A group's row binds every member's blob at the candidate.
- A curator cannot hand the writer a `sources` list.

## Evidence


- A card row binds both sources of its deleted canonical/package group, and the item comes back satisfied by that row. [1]

- A reworded group binds each copy's own blob and closes its worklist item. [2]

- A card with one source keeps its one-source row whether or not an item names it. [3]
- An uncovered overview is refused, and a covered one binds its item's files. [4]
- An author-supplied `sources` field is still refused. [5]
