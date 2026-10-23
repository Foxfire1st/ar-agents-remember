# mcp/tests/test_mik_r177_gate_groups_identical_copies.py

## Governing Overview

[Tests overview](overview.md)

## Purpose

Guard that every place judging onboarding traces builds its items with the worklist's
identical-copy groups, so one row binding a whole group answers the worklist and the memory-quality
gate alike -- and that a source without copies keeps the item it had. The closeout validator this
file also covered was retired with the certified closeout, and its cases were removed here.

## Code Commentary

### One group, two consumers

The module builds a real repository pair in which a canonical file and its generated copies are
deleted together and one carded owner remains. One card row authored by the product's writer binds
every source of the group. The cases then ask the same question twice: the leaf's own worklist
item and the memory-quality gate's item must be the same item, and the row must answer that item,
before the grouped change closes. The pre-change behaviour is kept as a control:
without groups the card item is the singleton, its id differs from the worklist's, and the row
matches but does not answer it.

### The refusal side

The memory-quality gate refuses an absent or incomplete worklist run with a named finding.
The outer controller gate returns the recomputation instruction when its group reader cannot read
the run. The gate test exercises this branch and asserts the named refusal and that no ungrouped
items are judged; it does not assert the instruction's wording. Separately, reader-only tests reject
six malformed group shapes and accept a complete run with an empty group map. These tests invoke
no second gate or closeout transaction.

### Writer bindings without a card

The writer cases cover a subject with no trace item: several deleted members, a deleted/live
pair and a single deleted path. They parse writer-authored history, compare its complete source
map with actual candidate blobs or `absent`, and ask the unchanged unexplained-item predicate
to accept each matching item. No cards or sidecars are created for these sources. The mixed
case supplies that persisted source-set shape explicitly; it does not establish that the native
grouping producer emits mixed candidate blobs. A separate case supplies conflicting unexplained
metadata and confirms that an existing trace item retains source authority.

### Bounds

The cases are source-level regressions over the writer, memory-quality gate, its group reader and the worklist.
The Worker's focused runs under its freeze are its own receipts; this card is not evidence that any
of them ran, and no case here speaks about the whole suite or an installed host.

## Evidence

The test symbols below carry the module's grouping and refusal proof at the recorded candidate.

- One row binding every copy closes the worklist item and the memory-quality gate sees that same answered item. [1]

- Without groups the card item is a different singleton and the matched row does not answer it; the trace gate reports MISSING_CODE. [2]

- The memory-quality gate refuses absent or incomplete worklist runs by name instead of judging ungrouped items. [3]

- Six malformed group shapes are refused by the controller group reader; this case invokes no closeout or second gate. [4]

- A complete run with an empty group map yields an empty map and no problem from the controller group reader. [5]

- A single-source card is the same answered item in the worklist and the memory-quality gate. [6]

- Existing trace-item sources prevail over conflicting unexplained-group metadata. [7]
- Cardless deleted groups, a deleted/live pair and a single path bind exact candidate source maps accepted by the unchanged unexplained-item predicate. [8]
