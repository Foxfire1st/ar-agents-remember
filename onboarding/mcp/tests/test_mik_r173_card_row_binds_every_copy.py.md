# mcp/tests/test_mik_r173_card_row_binds_every_copy_of_its_source.py

## Governing Overview

[Tests overview](overview.md)

## Purpose

Guard that a card's onboarding row binds every source of the leaf's persisted worklist item of its subject -- the whole identical-copy group -- and that the single-source card and uncovered overview keep the rows and the refusal they had before.

## Code Commentary

### The group proof is the leaf's own worklist loop

This module builds a real repository pair instead of composing the item by hand. The code base holds L56's shape: one canonical `c-05` template and its nine generated copies. The leaf contract is re-based on the commit that holds the group, so at the candidate the leaf's own `leaf_worklist` raises the card's `onboarding_trace` item with ten sources, all `absent` when the group is deleted and each with its real blob when the group is reworded; the item is open before the row exists.

The product's writer then captures its own code snapshot from that worktree -- no constructed snapshot and no injected blobs -- writes the row from the persisted worklist document, and the stored row carries the item's ten `(path, blob)` pairs. A second `leaf_worklist` run must return the same item `satisfiedBy` the written row's ID, which is the gate's own question asked again.

### The branches that stay as they were

A card no item names and a card whose item names only its own path both keep a one-source row. An overview with no covering item is still refused with the original `no worklist item covers` problem, while an overview whose item names its governed files binds them. A hand-off that tries to supply a `sources` field is refused as `the writer owns ['sources']`, so the writer keeps sole authorship of the row's sources.

### Bounds

The cases are source-level regressions over the writer, the worklist and the history file. The RED 2-failed/4-passed and GREEN 6-passed runs belong to the Worker's receipts under the passed freeze; this Curator did not execute them, and neither lane substitutes for the gate's own onboarding evidence.

## Evidence

- A card row binds all ten sources of its deleted group, and the item comes back satisfied by that row. [1]
- A reworded group binds each copy's own blob. [2]
- A card with one source keeps its one-source row whether or not an item names it. [3]
- An uncovered overview is refused and a covered one binds its item's files. [4]
- An author-supplied `sources` field is still refused. [5]
