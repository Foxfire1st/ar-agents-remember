# mcp/tests/test_mik_r177_gate_groups_identical_copies.py

## Governing Overview

[Tests overview](overview.md)

## Purpose

Guard that every place judging onboarding traces builds its items with the worklist's
identical-copy groups, so one row binding a whole group answers the worklist, the memory-quality
run and the closeout validator alike -- and that a source without copies keeps the item it had.

## Code Commentary

### One group, three consumers

The module builds a real repository pair in which a canonical file and its generated copies are
deleted together and one carded owner remains. One card row authored by the product's writer binds
every source of the group. The cases then ask the same question three times: the leaf's own worklist
item, the memory-quality gate's item and the closeout validator's item must be the same item, and the
row must answer it, before the grouped change closes. The pre-change behaviour is kept as a control:
without groups the card item is the singleton, its id differs from the worklist's, and the row
matches but does not answer it.

### The refusal side

A gate entry that cannot read a complete run's `identicalChanges` -- no run, a run that is not
complete, or a map with a malformed entry -- reports one named finding or refusal and judges no
ungrouped items. The closeout side additionally refuses a run that does not describe the candidate
being certified, and a group whose member has since gained a card, because either would answer the
row with another candidate's item. The remedy named in every one of those refusals is the documented
worklist recompute, never a silent regroup.

### Bounds

The cases are source-level regressions over the gate entries, the closeout adapter and the worklist.
The Worker's focused runs under its freeze are its own receipts; this card is not evidence that any
of them ran, and no case here speaks about the whole suite or an installed host.

## Evidence

The test symbols below carry the module's grouping and refusal proof at the recorded candidate.

- One row binding every copy closes the worklist item, and both gate entries raise that same item. [1]
- With no groups the item is the singleton and the row does not answer it. [2]
- The memory-quality entry refuses by name when the run names no readable groups. [3]
- The closeout takes the persisted run's groups and refuses without them. [4]
- A run recorded for another candidate is refused by name. [5]
- A group a card now contradicts is refused by name. [6]
- Six malformed group shapes are refused by name through both entries. [7]
- A run with no groups stays a valid empty map for both entries. [8]
- A single-source card is the same item in the worklist and both gate entries. [9]
